#!/usr/bin/env python3
"""Rebuild the surface maps in textures/ from their original sources.

Downloads each source file (or reuses it from the cache folder), then converts it
exactly as described in docs/sources.md#surface-maps:

  - Solar System Scope 2K maps and ring strips: copied as published.
  - Solar System Scope large maps: recompressed to JPEG quality 80.
  - NASA 3D Resources full maps: recompressed to JPEG quality 85.
  - Partial maps (Io, the Uranian moons, Triton): the unmapped black area is made
    transparent and saved as WebP quality 85; the app fills it with the painted texture.
  - Triton (PIA18668), Ceres and Vesta (DLR Dawn mosaics): scaled down to 2048 x 1024.
  - Saturn's icy moons (Cassini maps PIA18434-PIA18439): converted to greyscale, scaled to 2048 x 1024.
  - Callisto (USGS Voyager/Galileo mosaic): scaled to 2048 x 1024; the no-data area made transparent (WebP).

Requires Python 3 and Pillow (pip install pillow). The downloads total about 400 MB,
mostly the two Dawn mosaics; they are kept in the cache folder so reruns are quick.
Output is pixel-for-pixel reproducible; the exact bytes can differ between Pillow versions.

Usage, from the repository root:
  python3 tools/build_textures.py                  # writes textures/, cache in .texture-cache/
  python3 tools/build_textures.py --out /tmp/tex --cache ~/tex-cache
"""
import argparse
import os
import shutil
import sys
import urllib.parse
import urllib.request

try:
    from PIL import Image, ImageDraw, ImageFilter
except ImportError:
    sys.exit('Pillow is required: pip install pillow')

Image.MAX_IMAGE_PIXELS = None  # the Dawn mosaics are larger than Pillow's safety limit

SSS = 'https://www.solarsystemscope.com/textures/download/'
NASA3D = 'https://raw.githubusercontent.com/nasa/NASA-3D-Resources/master/Images%20and%20Textures/'
TRITON = 'https://assets.science.nasa.gov/content/dam/science/psd/photojournal/pia/pia18/pia18668/PIA18668.jpg'
DAWN = 'https://dawngis.dlr.de/data/'
# Cassini global maps of Saturn's icy moons (NASA/JPL-Caltech/SSI/LPI, Paul Schenk, 2014), enhanced colour; the app uses them in greyscale.
CASSINI = 'https://assets.science.nasa.gov/content/dam/science/psd/photojournal/pia/pia18/pia{n}/PIA{n}.jpg'
CASSINI_MAPS = {'m-mimas': 18437, 'm-enceladus': 18435, 'm-tethys': 18439, 'm-dione': 18434, 'm-rhea': 18438, 'm-iapetus': 18436}
# USGS Astrogeology: Callisto Voyager/Galileo SSI global mosaic, 1 km/pixel; pixel value 0 = no data.
CALLISTO = 'https://planetarymaps.usgs.gov/mosaic/Callisto_Voyager_GalileoSSI_global_mosaic_1km.tif'

# Solar System Scope: app id -> (2K file, large file or None). CC BY 4.0.
SSS_MAPS = {
    'sun': ('2k_sun.jpg', '8k_sun.jpg'),
    'mercury': ('2k_mercury.jpg', '8k_mercury.jpg'),
    'venus': ('2k_venus_atmosphere.jpg', '4k_venus_atmosphere.jpg'),
    'earth': ('2k_earth_daymap.jpg', '8k_earth_daymap.jpg'),
    'moon': ('2k_moon.jpg', '8k_moon.jpg'),
    'mars': ('2k_mars.jpg', '8k_mars.jpg'),
    'jupiter': ('2k_jupiter.jpg', '8k_jupiter.jpg'),
    'saturn': ('2k_saturn.jpg', '8k_saturn.jpg'),
    'uranus': ('2k_uranus.jpg', None),
    'neptune': ('2k_neptune.jpg', None),
}
SSS_RINGS = {'saturn_ring_2k.png': '2k_saturn_ring_alpha.png', 'saturn_ring_hi.png': '8k_saturn_ring_alpha.png'}

# NASA 3D Resources: app id -> folder name. Full maps (JPEG) and partial maps (WebP with transparency).
NASA_FULL = {
    'm-phobos': 'Mars - Phobos', 'm-deimos': 'Mars - Deimos',
    'm-europa': 'Jupiter - Europa', 'm-ganymede': 'Jupiter - Ganymede',
}
NASA_PARTIAL = {
    'm-io': 'Jupiter - Io (A)', 'm-miranda': 'Uranus - Miranda', 'm-ariel': 'Uranus - Ariel',
    'm-umbriel': 'Uranus - Umbriel', 'm-titania': 'Uranus - Titania', 'm-oberon': 'Uranus - Oberon',
}

# DLR Dawn global clear-filter mosaics. Credit: NASA/JPL-Caltech/UCLA/MPS/DLR/IDA.
DAWN_MAPS = {
    'ceres': 'Ceres/mosaics/HAMO/clear/Ceres_HAMO_mosaic_global.png',
    'vesta': 'Vesta/mosaics/HAMO/clear/Vesta_mosaic_HAMO-1-2_global.png',
}


def fetch(url, cache, name):
    """Return the path of the cached download, downloading it first if needed."""
    path = os.path.join(cache, name)
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        print('  downloading', url)
        req = urllib.request.Request(url, headers={'User-Agent': 'build_textures.py'})
        with urllib.request.urlopen(req) as r, open(path + '.part', 'wb') as f:
            shutil.copyfileobj(r, f)
        os.replace(path + '.part', path)
    return path


def save_jpeg(im, path, quality):
    im.convert('RGB').save(path, 'JPEG', quality=quality, optimize=True, progressive=True)


def transparent_unmapped(im):
    """Make the unmapped area transparent: black (<= 12) regions connected to the top or bottom edge.
    Dark areas inside the mapped surface stay opaque. The mask is shrunk 2 px and feathered 2 px."""
    im = im.convert('RGB')
    w, h = im.size
    mask = im.convert('L').point(lambda v: 255 if v > 12 else 0)
    for y in (0, h - 1):
        for x in range(0, w, 4):
            if mask.getpixel((x, y)) == 0:
                ImageDraw.floodfill(mask, (x, y), 128)
    mask = mask.point(lambda v: 0 if v == 128 else 255).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(2))
    im.putalpha(mask)
    return im


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', default='textures', help='output folder (default: textures)')
    ap.add_argument('--cache', default='.texture-cache', help='download cache folder (default: .texture-cache)')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    out = lambda name: os.path.join(a.out, name)

    print('Solar System Scope')
    for oid, (lo, hi) in SSS_MAPS.items():
        shutil.copyfile(fetch(SSS + lo, a.cache, 'sss/' + lo), out(oid + '_2k.jpg'))
        if hi:
            save_jpeg(Image.open(fetch(SSS + hi, a.cache, 'sss/' + hi)), out(oid + '_hi.jpg'), 80)
    for dst, src in SSS_RINGS.items():
        shutil.copyfile(fetch(SSS + src, a.cache, 'sss/' + src), out(dst))

    print('NASA 3D Resources')
    for oid, folder in {**NASA_FULL, **NASA_PARTIAL}.items():
        q = urllib.parse.quote(folder)
        src = fetch(f'{NASA3D}{q}/{q}.jpg', a.cache, f'nasa3d/{folder}.jpg')
        if oid in NASA_FULL:
            save_jpeg(Image.open(src), out(oid + '.jpg'), 85)
        else:
            transparent_unmapped(Image.open(src)).save(out(oid + '.webp'), 'WEBP', quality=85, method=6)

    print('Triton (NASA/JPL PIA18668)')
    im = Image.open(fetch(TRITON, a.cache, 'PIA18668.jpg')).convert('RGB').resize((2048, 1024), Image.LANCZOS)
    transparent_unmapped(im).save(out('m-triton.webp'), 'WEBP', quality=85, method=6)

    print('Saturn\'s icy moons (Cassini, NASA/JPL PIA18434-PIA18439), in greyscale')
    for oid, n in CASSINI_MAPS.items():
        im = Image.open(fetch(CASSINI.format(n=n), a.cache, f'cassini/PIA{n}.jpg'))
        save_jpeg(im.convert('L').resize((2048, 1024), Image.LANCZOS), out(oid + '.jpg'), 85)

    print('Callisto (USGS Voyager/Galileo mosaic); the no-data area is made transparent')
    im = Image.open(fetch(CALLISTO, a.cache, 'usgs/Callisto_Voyager_GalileoSSI_global_mosaic_1km.tif')).convert('L')
    data = im.point(lambda v: 255 if v > 0 else 0).resize((2048, 1024), Image.BILINEAR).point(lambda v: 255 if v > 250 else 0)
    im = im.resize((2048, 1024), Image.LANCZOS).convert('RGB')
    im.putalpha(data.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1)))
    im.save(out('m-callisto.webp'), 'WEBP', quality=85, method=6)

    print('Ceres and Vesta (DLR Dawn mosaics)')
    for oid, path in DAWN_MAPS.items():
        im = Image.open(fetch(DAWN + path, a.cache, 'dawn/' + os.path.basename(path)))
        save_jpeg(im.convert('L').resize((2048, 1024), Image.LANCZOS), out(oid + '.jpg'), 85)

    print('Done:', len(os.listdir(a.out)), 'files in', a.out)


if __name__ == '__main__':
    main()
