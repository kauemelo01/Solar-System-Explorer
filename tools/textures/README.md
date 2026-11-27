# Textures

`build_textures.py` rebuilds the surface maps in `textures/` from their original sources. It downloads each source file, or reuses it from the cache, and converts it as described in the documentation, under [Surface maps](../../docs/sources.md#surface-maps) and [Surface map processing](../../docs/interface.md#surface-map-processing). Its output matches the committed files pixel for pixel; the exact bytes can differ between Pillow versions.

## Setup

- Python 3 with Pillow (`pip install pillow`).
- About 400 MB of downloads, mostly the two Dawn mosaics (Ceres and Vesta). They are kept in the cache folder, so reruns are quick.

## Usage

From the repository root:

```
python3 tools/textures/build_textures.py                                   # writes textures/, cache in .texture-cache/
python3 tools/textures/build_textures.py --out /tmp/tex --cache ~/tex-cache
```

- `--out`: the output folder (default `textures`).
- `--cache`: the download cache folder (default `.texture-cache`, which git ignores).

## What it does

- **Solar System Scope:** the 2K maps and the ring strips are copied as published; the large maps are recompressed to JPEG quality 80.
- **NASA 3D Resources full maps:** recompressed to JPEG quality 85.
- **Partial maps** (Io, the Uranian moons, Triton): the unmapped black area is made transparent and saved as WebP quality 85. The app fills it with the painted texture.
- **Triton** (PIA18668), **Ceres** and **Vesta** (DLR Dawn mosaics): scaled down to 2048 × 1024.
- **Saturn's icy moons** (Cassini maps PIA18434–PIA18439): converted to greyscale and scaled to 2048 × 1024.
- **Callisto** (USGS Voyager/Galileo mosaic): scaled to 2048 × 1024, with the no-data area made transparent (WebP).
