[← Documentation index](README.md) · [Project README](https://github.com/kauemelo01/Solar-System-Explorer#readme)

# Sources, methodology and accuracy

## Naming convention

Object names follow **NASA/JPL**: the JPL Horizons record for planets and moons, and the JPL Small-Body Database plus NASA Science for small bodies. Comets therefore carry their full IAU designation (*1P/Halley*, *2P/Encke*, *67P/Churyumov-Gerasimenko*, *C/1995 O1 (Hale-Bopp)*). Numbered asteroids and dwarf planets appear by name only (*Ceres* for SBDB `1 Ceres`); their number and provisional designation are in the catalogue's *Designation (JPL)* column. Provisional moon designations use the IAU form *S/2023 S 1*, which Horizons stores as `S2023_S01`.

## Reference frame

All positions are computed in the **heliocentric ecliptic J2000** frame, the standard NASA/JPL frame for solar-system work. When you hold another body still, the app subtracts that body's position from every other position at each instant. That is a pure change of origin: the physics is unchanged, and only the point of view moves. This is the whole idea behind the project. A frame centred on the Sun, the Earth or Io describes the same motions.

## Scale

Distances and body sizes are always drawn to true scale. Bodies are therefore tiny compared with their orbits, as they really are, and you zoom in (or click a name to fly to it) to see them.

**To scale:** every position (computed in kilometres from the orbital elements), every body's radius, Saturn's rings (74,500–136,780 km), the orbit trails and the distance rings in AU.

### What is not to scale

These are visual aids drawn on top of the true-scale model; each is a [limitation of the model](#limitations-of-the-model):

| Element | What it really is |
|---|---|
| Coloured dots and labels marking bodies | A fixed 3.5–6 pixels on screen whatever the zoom, so bodies smaller than a pixel can still be found |
| The Sun's glow | A glow 7 times the Sun's radius, plus a halo of fixed screen size. The Sun's sphere itself is true size |
| Comet tails and comas | Illustrative length: the shorter of 0.6 AU and 0.3 / r² AU, where r is the comet's distance from the Sun in AU. Real tails vary widely and can exceed 1 AU |
| Bodies with no published radius | Placeholder radii, marked *est.* in the app and the catalogue: 1.5–40 km for moons, plus Arrokoth (≈ 9 km, a 36 km-long contact binary) and comet C/2020 F3 (NEOWISE) (2.5 km) |
| Irregular asteroids and small moons | Mean radius is correct; the lumpy shape is computer-generated, not the real shape |
| Main asteroid belt, Jupiter trojans, Kuiper belt | Statistical clouds of fixed-size points, not individual catalogued objects (see [Belts](#belts)) |
| Ring opacity | Radii are true, but rings are drawn more opaque than they are, so that faint and narrow rings (for example Jupiter's, with optical depths around 10⁻⁶) can be seen |
| The sky (stars, Milky Way, deep-sky objects) | Directions are true, but the sky is drawn on a backdrop that moves with the camera, so distances are not represented; the object's card gives its real distance. Star dot size shows brightness, not physical size |

## Planets

- **Elements:** E. M. Standish, *Keplerian Elements for Approximate Positions of the Major Planets*, JPL SSD. Table 1 (valid 1800 AD – 2050 AD), with linear rates per Julian century. <https://ssd.jpl.nasa.gov/planets/approx_pos.html>
- The Earth and the Moon are placed around the **Earth–Moon barycentre** (EMB) using the Earth/Moon mass ratio (μ = 0.0121505).
- **Pluto** uses the Pluto row of the original version of Standish's Table 1, which JPL has since removed from its web copy (the page now notes that "the former planet Pluto has also been removed"). Checked against JPL Horizons, it places Pluto within 0.01° (about 0.01 AU) of its true position from 1900 to 2100, much closer than a single osculating orbit from the SBDB would (up to 0.45 AU). Pluto is a dwarf planet and is listed and shown with the dwarf planets.
- **Physical data:** JPL *Planetary Physical Parameters* <https://ssd.jpl.nasa.gov/planets/phys_par.html>; NASA NSSDCA *Planetary Fact Sheets* <https://nssdc.gsfc.nasa.gov/planetary/planetfact.html>.
- **Spin poles and rotation periods:** B. A. Archinal et al. (2018), *Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015*, Celestial Mechanics and Dynamical Astronomy 130:22. <https://doi.org/10.1007/s10569-017-9805-5>. Machine-readable form: NAIF PCK `pck00011.tpc` <https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc>.

## The Moon

A mean-element lunar orbit (node and perigee regressing and precessing at their mean rates; e = 0.0549, i = 5.145°, a = 384,400 km) around the Earth. Reference: NASA NSSDCA *Moon Fact Sheet* <https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html>.

## Natural satellites of the planets and Pluto (459)

- **Elements:** JPL SSD, *Planetary Satellite Mean Elements*. <https://ssd.jpl.nasa.gov/sats/elem/>. Regular moons use elements referred to their local Laplace plane (pole RA/Dec given in the table). Distant irregular moons use elements referred to the ecliptic.
- **Sizes:** JPL SSD, *Planetary Satellite Physical Parameters* <https://ssd.jpl.nasa.gov/sats/phys_par/> lists 46 moons; the other radii come from earlier compilations whose sources are not yet documented, and a few differ from JPL's values (see [Known issues](#known-issues)). Where no radius is published, the app uses a small placeholder (marked *est.* in the catalogue).
- **Identifiers:** NAIF integer IDs, cross-checked in JPL Horizons. <https://ssd.jpl.nasa.gov/horizons/>
- **Discoveries and families:** JPL *Satellite Discovery Circumstances* <https://ssd.jpl.nasa.gov/sats/discovery.html>; S. S. Sheppard (Carnegie Science) moon pages <https://sites.google.com/carnegiescience.edu/sheppard/moons>; IAU Minor Planet Center electronic circulars <https://minorplanetcenter.net/mpec/RecentMPECs.html>.
- **Count:** 459 moons as of November 2026 (Mars 2, Jupiter 115, Saturn 292, Uranus 29, Neptune 16, Pluto 5). Earth's Moon is counted with the planets. With the 8 moons of other dwarf planets, candidates and asteroids below, the app has 467 moons.
- **Naming differences:** *S/2009 S 2* (NAIF 65304) follows JPL Horizons. *Megaclite* and *Philophrosyne* follow JPL Horizons; the JPL mean-elements table spells them `Magaclite` and `Philophrosyn`.
- **Pluto's moons** use JPL's mean equatorial elements, referred to Pluto's equator with the IAU 2015 pole (RA 132.993°, Dec −6.163°), and are fitted to Horizons like the other moons: Charon to 0.06°, the four small moons to 1.4–2.8°.
- **Positions:** fitted to JPL Horizons over 1800–2050; see [Moon orbits](#moon-orbits) below. The fits replace the mean elements' epochs (JPL gives most for 2000-01-01, some groups for 2009, 2020 or 2025), which the app used to treat as 2000.

### Moon orbits

The app places every planetary moon with an orbit fitted to its **JPL Horizons ephemeris** <https://ssd.jpl.nasa.gov/horizons/>, from 4 January 1800 to 1 January 2051, or the part of that range Horizons covers. The fits are in `data/moon-orbits.js` and are built by the scripts in [`tools/moon-orbit-fits/`](../tools/moon-orbit-fits/) (how to rerun them: its README). Each moon has one of two kinds of fit:

- **One orbit for the whole range (113 moons, most regular moons).** JPL's orbit shape, with its phase, mean motion, apsidal and nodal precession, a slow drift and up to two periodic terms fitted to Horizons. For the four moons in co-orbital resonances (Janus and Epimetheus, which swap orbits every four years, and Dione's companions Helene and Polydeuces) a table of along-track corrections every 5 or 10 days, taken from Horizons, is added.
- **Time windows (345 moons, mostly irregular).** The Sun disturbs these orbits too much for one ellipse, so each moon has consecutive windows of 10 years, split down to 2.5 years where needed, each with its own fitted ellipse. Each window is fitted to both the direction and the distance of the Horizons positions, and the app blends neighbouring windows across each boundary (over 120 days either side, or 15% of the orbital period for slow moons such as Neso), so a moon never jumps from one window's orbit to the next, and its path (and its trail) bends smoothly there. Seven moons keep a visible bend; see [Limitations of the model](#limitations-of-the-model).

The fits use Horizons positions every 60 days, plus a dense stretch near 2000 for the fast inner moons, so that their speed is not mistaken for another one that fits the same 60-day samples. S/2009 S 2 is fitted in Saturn's equatorial plane, which the JPL table does not give.

**Checked independently.** Every fit is compared with Horizons positions on dates it was not fitted to (every 211 days), computed with the app's own code. Typical errors (median over the moons of each planet; for each moon, the root-mean-square error over 1800–2050):

| Moons of | Moons | Typical error | Least accurate |
|---|---|---|---|
| Mars | 2 | 1.0° | Phobos, 1.9° |
| Jupiter | 115 | 1.5° | Carpo, 3.6° |
| Saturn | 292 | 1.5° | Methone, 3.4° |
| Uranus | 28 | 0.8° | Desdemona, 2.9° |
| Neptune | 16 | 0.3° | Naiad, 3.4° |
| Pluto | 5 | 1.7° | Styx, 2.8° |

Over all 458 fitted moons the typical error is 1.5°, and 90% of moons are within 2.4°; no moon's typical error is above 3.6°. The major moons are within a fraction of a degree (Io 0.03°, Titan 0.03°, Triton 0.29°, Charon 0.06°; Mimas, in resonance with Tethys, 2.8°). Before these fits, with JPL's mean elements alone, the same check gave a typical error of 92°. The largest single errors come from eccentric irregular orbits near their closest approach to the planet: S/2023 S 5 up to 24°, S/2023 S 38 and Pasiphae up to 21°.

**Distances** are checked the same way: the distance from the planet is typically within 1.6% of Horizons, and every moon is within 5% on average (root-mean-square over 1800–2050).

**Where Horizons covers less than 1800–2050**, the moon's card says *Estimated position* outside its own range: Uranus's 13 inner moons from Cordelia to Cupid (Horizons from 1900), Saturn's Janus, Epimetheus, Atlas, Prometheus, Pandora, Pan, Pallene, Anthe, Aegaeon and S/2009 S 2 (1950–2050), and Daphnis (1990–2018). **S/2025 U 1** is not yet in Horizons: it keeps JPL's mean elements, at their 2025 epoch, and its card says so.

**Outside 1800–2050** the fits are extended, and the time bar shows *Estimated positions*. A test of the same method 150 years beyond its fitted range kept one-orbit moons within about 0.5° (Io 0.06°, Titan 0.16°, Iapetus 0.38°), and their errors grow slowly beyond that. Windowed moons keep their first or last window: their orbit's size, shape and direction stay right, but within a few decades their position along it is no longer meaningful.

Orbit outlines follow the fits, so they turn as the orbits precess.

## Moons of dwarf planets and asteroids (8)

- **JPL Horizons satellite solutions:** Dysnomia (Eris), Weywot (Quaoar), Vanth (Orcus) and Dimorphos (Didymos), as osculating J2000 ecliptic elements about each primary, 2025-Jan-1.
- **Published orbits:**
  - Hiʻiaka and Namaka (Haumea): Ragozzine & Brown 2009, *AJ*, [arXiv:0903.4213](https://arxiv.org/abs/0903.4213).
  - Xiangliu (Gonggong): Kiss et al. 2019, *Icarus*, [arXiv:1903.05439](https://arxiv.org/abs/1903.05439); prograde solution, orientation uncertain ([limitation of the model](#limitations-of-the-model)).
  - Selam (Dinkinesh): Levison et al. 2024, *Nature*, [arXiv:2406.19337](https://arxiv.org/abs/2406.19337); distance and period only.
- **Left out:** moons without a verifiable published orbit, such as Makemake's moon (orbit only bounded) and Ida's moon Dactyl (a [limitation of the model](#limitations-of-the-model)).
- **In the app:** listed in the moons menu under *Dwarf planets & candidates* or *Asteroids*; switching one on also shows its parent's group.
- Details per moon: [catalogue/moons-small-bodies.md](catalogue/moons-small-bodies.md).

## Ring systems (7)

- **Jupiter, Uranus, Neptune, Saturn:** NASA NSSDCA ring fact sheets. Saturn's rings also use an image strip from Solar System Scope when realistic textures are on (see [Surface maps](#surface-maps)).
- **Haumea:** Ortiz et al. 2017, *Nature*, [arXiv:2006.03113](https://arxiv.org/abs/2006.03113).
- **Quaoar:** Morgado et al. 2023, *Nature*; Pereira et al. 2023, *A&A*, [arXiv:2304.09237](https://arxiv.org/abs/2304.09237).
- **Chariklo:** Braga-Ribas et al. 2014, *Nature*, [arXiv:1409.7259](https://arxiv.org/abs/1409.7259).
- Rings are drawn in the body's equatorial plane at true radii; opacity is exaggerated. Details: [catalogue/rings.md](catalogue/rings.md).

## Dwarf planets, candidates, asteroids, centaurs and comets (38, plus Pluto)

Pluto is grouped with the dwarf planets in the app and the catalogue, but its orbit comes from the planetary table above, so it is not counted in this section's data. In the app, the five IAU dwarf planets (Ceres, Pluto, Eris, Haumea, Makemake) are under the *Dwarf planets* switch and the four candidates (Gonggong, Quaoar, Sedna, Orcus) under *Candidates*.

- **Elements:** JPL Small-Body Database (osculating heliocentric elements; epoch JD 2461200.5 = 2026-Jun-24 TDB for most objects, and the most recent perihelion solution for comets). <https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html>, API: <https://ssd-api.jpl.nasa.gov/doc/sbdb.html>
- **Sizes and rotation periods:** SBDB diameters and rotation periods where listed; otherwise published measurements, each cited in [the catalogue's notes](catalogue/small-bodies.md#notes-on-sizes-and-rotation). Five bodies with no published rotation period spin at an illustrative 12 hours.
- **Designations:** IAU Minor Planet Center. <https://www.minorplanetcenter.net/>
- **Spin poles** of small bodies are not modelled from data. They are randomised for display only (a [known issue](#known-issues)), except fifteen taken from published data: Ceres and Vesta (IAU 2015, Archinal et al. 2018, so that their surface maps sit north-up); Pallas, Lutetia, Eros, Itokawa, 9P/Tempel 1 and 67P/Churyumov-Gerasimenko (IAU 2015, as given in NAIF's [`pck00011.tpc`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc)); Bennu (OSIRIS-REx, [`bennu_v17.tpc`](https://naif.jpl.nasa.gov/pub/naif/ORX/kernels/pck/bennu_v17.tpc)); Ryugu (Hayabusa2, [`ryugu_v10.tpc`](https://naif.jpl.nasa.gov/pub/naif/pds/pds4/hyb2/hyb2_spice/spice_kernels/pck/ryugu_v10.tpc)); Psyche (Shepard et al. 2021, *Planetary Science Journal* 2:125, [doi:10.3847/PSJ/abfdba](https://doi.org/10.3847/PSJ/abfdba)); Haumea (Hiʻiaka's orbit pole, which its ring shares), Quaoar (ring pole), Chariklo (ring pole) and Ida (NAIF `pck00011`).

## Belts

The main asteroid belt, Jupiter trojans and Kuiper belt are **statistical point clouds** drawn from typical orbital distributions (semi-major axis, eccentricity, inclination ranges). They show where those populations are, not individual catalogued objects. Overview: NASA Science <https://science.nasa.gov/solar-system/asteroids/>, <https://science.nasa.gov/solar-system/kuiper-belt/>. This is a [limitation of the model](#limitations-of-the-model).

## The sky beyond the solar system

- **Stars:** *Yale Bright Star Catalogue*, 5th revised ed. (D. Hoffleit & W. H. Warren Jr., 1991; CDS V/50), via the NASA HEASARC table `bsc5p` <https://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html>. All 9,096 entries with a position and V magnitude are drawn; colour comes from B−V.
- **Milky Way and faint stars:** NASA/Goddard Space Flight Center Scientific Visualization Studio, *Deep Star Maps* (2009) <https://svs.gsfc.nasa.gov/3895>. Plate carrée map in J2000 right ascension and declination, built from over 100 million stars in the Bright Star, Tycho-2 and UCAC3 catalogues. The app ships two sizes; see [Sky map loading](#sky-map-loading).
- **Deep-sky positions:** CDS SIMBAD and the Sesame name resolver (J2000).
- **Deep-sky reference images:** NASA Image and Video Library <https://images.nasa.gov/>, linked from each object's card and catalogue entry (not drawn in the sky). Credits are listed in [catalogue/sky.md](catalogue/sky.md).
- **Planet-hosting stars:** NASA Exoplanet Archive, `pscomppars` table <https://exoplanetarchive.ipac.caltech.edu/>.
- **Star names:** IAU Working Group on Star Names.
- **Constellations:** boundaries from Delporte (1930) via Roman (1987, CDS VI/42) and Davenhall & Leggett (1989, CDS VI/49), precessed from B1875 to J2000 (IAU 1976 model). Stick figures from NASA/Goddard SVS *Deep Star Maps* (figures after Sky & Telescope for the IAU). Off by default. Details and checks: [catalogue/constellations.md](catalogue/constellations.md).
- **Frame:** J2000 equatorial positions are rotated into the ecliptic J2000 frame used for the planets. The sky sphere is centred on the camera, so it behaves as infinitely far away. That is a very good approximation: from Neptune, even Proxima Centauri shifts by less than 25″.
- **Not modelled:** proper motion (the catalogue is J2000; Barnard's Star, the fastest, moves about 10″ per year) and precession (a [limitation of the model](#limitations-of-the-model)).

### Sky map loading

The star map comes in two sizes, in `sky/`:

| File | Size | Download |
|---|---|---|
| `starmap_4k.jpg` | 4096 × 2048 | 2.2 MB |
| `starmap_8k.jpg` | 8192 × 4096 | 6.9 MB |

1. **Capable devices try the 8K map first.** A device counts as capable when both of these hold:
   - the graphics chip accepts textures at least 8192 pixels wide (`renderer.capabilities.maxTextureSize >= 8192`);
   - the screen's longer side is at least 1600 device pixels (`max(screen.width, screen.height) × devicePixelRatio >= 1600`).
2. **The 4K map is the fallback.** It loads only if the 8K map fails to load, or straight away on devices that are not capable.

In practice:

- **Most desktops and laptops** use 8K; a 1920 × 1080 monitor already qualifies.
- **Recent phones usually use 8K too.** For example, an iPhone screen's long side is 844 × 3 = 2,532 device pixels, and its graphics chip supports 8192.
- **Older or low-end devices** use 4K.

Each device normally downloads only one file: 6.9 MB for 8K or 2.2 MB for 4K. On capable devices the sky appears once the 8K map has arrived, so it takes a little longer to show up than when the 4K map loaded first.

**Choosing the size.** The side panel's *Images → Sky map detail* control picks **Auto** (the rule above), **4K** or **8K**. Forcing 8K still falls back to 4K if the 8K file fails to load; the 8K option is disabled on devices whose graphics cannot show textures 8192 pixels wide. Each map is downloaded at most once per visit, so switching back and forth does not download it again. The choice is remembered on the device. The logic is in `index.html`, next to the comment `Sky map size`.

## Surface maps

Bodies with a surface map in `textures/` are drawn with it. All others keep a simple texture painted in code (`texFor()` in `index.html`). **Not every map is complete.** Some are partial and some have gaps filled in by their makers. Each map is listed below with what its publisher says about it. Each object's card in the app also carries a one-line note saying what its surface image is (see [Card notes](#card-notes)). Gaps that better data could fill are [known issues](#known-issues); the rest are [limitations of the model](#limitations-of-the-model).

### Sources

- **Solar System Scope**, *Solar Textures* <https://www.solarsystemscope.com/textures/>, CC BY 4.0. The publisher says the maps are "based on NASA elevation and imagery data", with colours tuned to true-colour photos from MESSENGER, Viking and Cassini and made "slightly more saturated". Gaps in the data "are filled with fictional terrain that corresponds with the rest of the landscape". The publisher does not say which parts are filled (a [limitation of the model](#limitations-of-the-model)).
- **NASA 3D Resources** <https://github.com/nasa/NASA-3D-Resources>, free to use under NASA's media guidelines. These maps come from the JPL/Caltech planetary map database and are mostly old Voyager and Viking mosaics, from before Galileo and Cassini. The descriptions below are quoted from each map's page at <https://science.nasa.gov/3d-resources/>.
- **NASA/JPL Photojournal**, PIA18668 *Map of Triton* <https://www.jpl.nasa.gov/images/pia18668-map-of-triton/> (Paul Schenk, Lunar and Planetary Institute, 2014), from Voyager 2 images. Public domain.
- **DLR Dawn mosaics** <https://dawngis.dlr.de/>: global clear-filter mosaics from Dawn's framing camera, made by the German Aerospace Center (DLR). Credit: NASA/JPL-Caltech/UCLA/MPS/DLR/IDA.

### Every map, with its coverage

| Body | Source | Size | What it shows | Notes |
|---|---|---|---|---|
| Sun | Solar System Scope | 2048 × 1024; 4096 × 2048 | A representative image of the photosphere | The Sun's surface changes constantly; no real map exists |
| Mercury | Solar System Scope | 2048 × 1024; 8192 × 4096 | Global map, MESSENGER-era | Any gaps were filled by the publisher |
| Venus | Solar System Scope | 2048 × 1024; 4096 × 2048 | Cloud tops (what Venus looks like), not the radar-mapped surface | Clouds change constantly; representative only |
| Earth | Solar System Scope, plus a painted cloud layer | 2048 × 1024; 8192 × 4096 | Cloud-free composite (Blue Marble), with random clouds drawn on top | The map itself has no known problems; the publisher calls Earth "the most precise part of the pack". **The clouds are not real**: they are generated in code (see below) only so the planet looks less artificial |
| The Moon | Solar System Scope | 2048 × 1024; 8192 × 4096 | Global map | Any gaps were filled by the publisher |
| Mars | Solar System Scope | 2048 × 1024; 8192 × 4096 | Global map, Viking-era colour | Any gaps were filled by the publisher |
| Jupiter, Saturn | Solar System Scope | 2048 × 1024; 4096 × 2048 | Cloud bands, Cassini-era colour | Clouds change constantly; representative only |
| Uranus | Solar System Scope | 2048 × 1024 | Nearly featureless cloud tops | Representative only |
| Neptune | Solar System Scope | 2048 × 1024 | Cloud tops including the Great Dark Spot | The Great Dark Spot seen by Voyager 2 in 1989 had gone by 1994 |
| Saturn's rings | Solar System Scope | 2048 and 8192 px strip | Radial brightness and transparency | The strip's scale was fitted by the C-ring inner edge and Cassini Division (about ±1%) |
| Ceres | DLR, *Ceres HAMO mosaic* (Dawn) | 2048 × 1024 | Global map from Dawn's high-altitude mapping orbit | Black-and-white; thin strips at the poles |
| Vesta | DLR, *Vesta HAMO mosaic* (Dawn) | 2048 × 1024 | Global map from Dawn's high-altitude mapping orbit | Black-and-white. The far north is dark: it was in winter shadow when Dawn photographed it. The app's Vesta is a generic lumpy shape, so the map is only approximately placed |
| Phobos | NASA 3D Resources | 1440 × 720 | Viking images, processed by USGS | Few visible gaps |
| Deimos | NASA 3D Resources | 1440 × 720 | Viking images, processed by USGS | Roughly a third of the map (one side) is smeared filler (a [known issue](#known-issues)) |
| Io | NASA 3D Resources | 1440 × 720 | USGS mosaic of Voyager images; "data gaps near the poles" | The polar gaps (black in the original) are filled in the app with the painted texture (a [limitation of the model](#limitations-of-the-model)) |
| Europa, Ganymede | NASA 3D Resources | 1440 × 720 | USGS mosaic with Voyager images | Black-and-white; some smeared filler near the poles |
| Callisto | NASA 3D Resources | 1440 × 720 | USGS mosaic with Voyager images | Black-and-white; a band of longitude and the south polar region are filled with flat white, which is wrong for dark Callisto (a [known issue](#known-issues)) |
| Mimas, Enceladus, Tethys, Dione, Rhea, Iapetus | NASA 3D Resources | 1440 × 720 | "Mosaic from the Voyager imagery" (before Cassini) | Black-and-white. Unmapped areas are filled with flat white or smears: about half of Enceladus and Mimas, a third of Dione, the south of Tethys and Iapetus, and both sides of Rhea (a [known issue](#known-issues)) |
| Miranda, Ariel, Umbriel, Titania, Oberon | NASA 3D Resources | 1440 × 720 | USGS (Tammy Becker) mosaic of Voyager 2 images | Black-and-white. Voyager 2 saw only the southern hemispheres; the app fills the north (about 60% of each map) with the painted texture (a [limitation of the model](#limitations-of-the-model)) |
| Triton | NASA/JPL PIA18668 (Paul Schenk, 2014) | 2048 × 1024 | Voyager 2 images, enhanced colour | About half of Triton, mostly the southern hemisphere; the north was in polar night during the 1989 flyby. The app fills the unseen part with the painted texture, so a seam is visible (a [limitation of the model](#limitations-of-the-model)) |

Bodies with no map keep the painted texture (a [limitation of the model](#limitations-of-the-model)): Hyperion, all dwarf planets and candidates except Ceres, the asteroids except Vesta, and the comets.

**Removed maps.** Earlier versions used NASA 3D Resources maps for Pluto, Charon and Titan. NASA's own pages call all three "Fictional": Pluto was stitched from a painting by Pat Rawlings, Charon was "faked from some Magellan images", and Titan is a "concept". They were dropped, and these bodies use the painted texture again. Real maps exist for Pluto and Charon (New Horizons, 2015) and Titan (Cassini radar and infrared) and could be added later.

### Processing

All of the steps below are done by [`tools/build_textures.py`](../tools/build_textures.py), which downloads every source and rebuilds `textures/` (run `python3 tools/build_textures.py` from the repository root; it needs Pillow and about 400 MB of downloads, cached in `.texture-cache/`). Its output matches the committed files exactly.

- The large Solar System Scope maps are recompressed to JPEG quality 80; the 2K ones are used as published.
- The NASA maps are recompressed to JPEG quality 85.
- For Io, the Uranian moons and Triton, the unmapped area (black in the originals) is made transparent and saved as WebP. In the app it is filled with the painted texture, so a seam is visible where they meet.
- The Ceres and Vesta mosaics (21093 and 26703 pixels wide) and the Triton map (14138 pixels wide) are scaled down to 2048 × 1024.

### How they load

1. **Each body starts in its plain colour** and switches to its map when the file arrives. Maps are downloaded only while realistic textures are on (see below), and then every map is requested as soon as the page opens, not when you fly to a body.
2. **Capable devices try the large map first** (same test as the [sky map](#sky-map-loading)); if it fails they load the 2K map. Other devices load the 2K map directly. The test is made once, when the page opens. Saturn's ring strip follows the same rule (8192 px, then 2048 px).
3. **The painted texture is the fallback**, used only if every file for that body fails to load.

There is no manual choice of size for surface maps: the *Auto / 4K / 8K* buttons under *Images → Sky map detail* apply to the sky map only.

**Turning them off.** The side panel's *Images → Realistic surface textures* switch (on by default, remembered on the device) turns all real maps off. Every body then uses its painted texture, Saturn's rings use the painted ring, Earth's clouds are hidden, the surface notes on the cards are hidden, and no map files are downloaded. Turning it back on reuses any maps already downloaded.

**Sphere detail.** Bodies with a map are drawn as smoother spheres (64 × 40 segments, as for the planets) so the map does not look faceted; other moons and small bodies use 32 × 20. Sizes and shapes are unchanged, and Vesta, Phobos and Deimos keep their lumpy shapes.

### Orientation

- **North is up on every map**, but longitude is not aligned. The app spins each body at its true rate but does not model where its prime meridian points, so the side facing you at a given moment is not the real one (a [known issue](#known-issues)).
- **Some maps are turned 180°: those of bodies that rotate backwards.** The IAU defines a planet's or moon's *north* pole as the one on the north side of the solar system's main plane (the invariable plane), whichever way the body turns. Seen from that pole, most bodies turn counter-clockwise (*prograde*). Venus, Uranus, Uranus's five major moons (Miranda, Ariel, Umbriel, Titania, Oberon) and Neptune's moon Triton turn clockwise (*retrograde*): their IAU 2015 spin rates are negative. Triton turns once per orbit, and its orbit is retrograde.
  - The app always turns a body counter-clockwise about the pole it is given. To make these eight bodies turn the right way, it gives them the pole opposite the IAU north pole: for Venus (92.76°, −67.16°) instead of (272.76°, +67.16°), for Uranus and its moons (77.31°, +15.18°) instead of (257.31°, −15.18°), and for Triton (118.45°, −20.30°) instead of (298.45°, +20.30°). Both are the IAU 2015 values ([Archinal et al. 2018](https://doi.org/10.1007/s10569-017-9805-5)), only reversed.
  - Surface maps are drawn with IAU north at the top. Placed with their top at the app's pole, these eight maps would be upside down, so the app turns them 180°. This is a rotation, not a mirror image: north ends up at the IAU north pole, east and west keep their real layout, and the body still spins the right way.
  - Example: Voyager 2 photographed only the southern hemispheres of Uranus's moons. After the turn, the mapped half sits around each moon's IAU south pole, as it should.
  - Prograde bodies use the IAU north pole directly, and their maps are not turned: the Sun, Mercury, Earth, the Moon, Mars, Jupiter, Saturn, Neptune, Ceres, Vesta, and the moons of Mars, Jupiter and Saturn that have maps.
  - One approximation: the app gives Uranus's five moons Uranus's own pole. The IAU's poles for these moons differ from it by about 0.1° (for example Ariel at 257.43°, −15.10°), which is not visible. This is a [limitation of the model](#limitations-of-the-model).
  - Triton's IAU pole moves: it circles Neptune's pole about every 690 years, following Triton's orbit. The app uses its value at J2000, computed from the IAU 2015 series as given in NAIF's [`pck00011.tpc`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc). It lies within about 0.5° of the axis of the app's Triton orbit, which is also fixed (see [Known issues](#known-issues)). Holding the pole fixed is a [limitation of the model](#limitations-of-the-model).
  - **Iapetus** uses its IAU spin pole (318.16°, 75.03°), not the pole of its orbit plane from JPL's table (288.7°, 78.9°), which is about 8° away. Its IAU pole drifts slowly; the app uses the J2000 value (a [limitation of the model](#limitations-of-the-model)).

The logic is in `index.html`, next to the comment `surface maps`.

### Earth's clouds

The Earth map is cloud-free, which looks artificial, so the app draws a separate layer of random clouds just above it. There is no weather model: the clouds are fixed noise patterns, the same on every visit, and they turn with the planet. They are shaped to look plausible: stretched east–west, a little denser near the equator and at mid-latitudes, and thinner in the subtropics. They cover about a fifth of the globe (real cloud cover is about two-thirds). The layer is generated a few rows at a time after the Earth map loads, so the page does not stall. It is added only on top of the real map, not the painted fallback. The code is in `index.html`, next to the comment `Earth's clouds`. The painted clouds are a [limitation of the model](#limitations-of-the-model).

### Card notes

Each object's card in the app has a short note under its type saying what its surface image is. Every note fits in two lines on the card, on desktop and phone screens.

| Note | Used for |
|---|---|
| Surface: real spacecraft photos | Ceres, Vesta, Phobos |
| Surface: based on real spacecraft photos | Mercury, Earth, the Moon, Mars (Solar System Scope: colours tuned and any gaps filled by the publisher) |
| Clouds: based on real photos, but they change constantly | Venus, Jupiter, Saturn, Uranus, Neptune |
| Representative image: the Sun has no fixed surface | The Sun |
| Surface: real photos; gaps filled in by map makers | Deimos, Europa, Ganymede, Callisto, Mimas, Enceladus, Tethys, Dione, Rhea, Iapetus |
| Surface: real photos, partial; the rest is painted | Io, Miranda, Ariel, Umbriel, Titania, Oberon, Triton |
| Surface: painted illustration, not a real image | Every other body drawn as a sphere or lumpy shape, including Pluto, Charon and Titan |
| Plain shape; no surface image | The small moons, including the moons of dwarf planets, candidates and asteroids, drawn as plain-coloured shapes |

Some notes add a short detail: Earth "Clouds are painted", Venus "Surface hidden", Neptune "Dark spot of 1989, now gone", Vesta "Far north in shadow", Io "Small polar gaps", Triton "Voyager 2 saw half", and the five Uranian moons "Only the south was seen". If a body's map fails to load, its note says it is showing the painted texture instead. The notes are defined in `index.html` next to the comment `one-line note on each object's card`.

## Accuracy

| Object type | Model | Typical accuracy |
|---|---|---|
| Planets | Standish Keplerian elements + secular rates | ~arc-minutes, 1800–2050 |
| The Moon | Mean elements (no periodic perturbations) | within a few degrees in longitude |
| Regular moons | One orbit fitted to JPL Horizons over 1800–2050 ([Moon orbits](#moon-orbits)) | Major moons within a fraction of a degree; small inner moons typically 1–3° |
| Irregular moons | Orbits fitted to JPL Horizons in windows of 2.5–10 years | Typically 1–2.5°, at most 3.6°; distance typically within 2% |
| Asteroids, dwarf planets | Two-body orbit from SBDB epoch | Very good near the epoch, slowly degrading away from it |
| Comets | Two-body orbit from the SBDB solution for the latest perihelion | Good near perihelion; drifts faster than asteroids (Jupiter encounters, outgassing), up to several degrees within a decade (a [limitation of the model](#limitations-of-the-model)) |
| Moons of dwarf planets and asteroids | Two-body orbit about the primary (JPL Horizons or published elements) | Orbit size and period good; phases drift; Selam's plane and Xiangliu's orientation are uncertain (a [limitation of the model](#limitations-of-the-model)) |

**Date range.** The app covers 1 January 1000 AD to 1 January 3000 AD (UTC, Gregorian calendar). Playing stops at either end, and a date entered outside the range is moved to the nearest end. **Outside 1800–2050: positions are estimates.** That is the range in which the planets' elements are valid. Outside it the time bar turns amber and shows *Estimated positions* (next to the speed on wide screens, after the clock on phones); the further from that range, the larger the errors. The limits are `JD_MIN` and `JD_MAX` in `index.html`. Estimated positions outside 1800–2050 are a [limitation of the model](#limitations-of-the-model).

## Known issues

Things that are wrong compared with official NASA, JPL or IAU data, found in a November 2026 check of every value. They are not fixed yet; work in progress is on the `audit-fixes-wip` branch.

- **Moon sizes.** Only 46 moon radii can be traced to JPL's *Planetary Satellite Physical Parameters*, and 12 of those differ slightly from JPL's current values (for example Nix 25 km in the app, 18 km at JPL). The remaining radii have no documented source yet.
- **Spin axes of small bodies.** All but fifteen small bodies have a random spin axis. Published axes exist for some others, for example Arrokoth, Didymos and Apophis.
- **Which side of a body faces you.** The app spins every body at its true rate, but does not set where its prime meridian points, so the side facing you at a given moment is not the real one. The IAU publishes this for every planet and major moon.
- **Gaps in some moon maps that could be filled with better data.** Callisto's map has a band of longitude and its south polar region filled with flat white, which is wrong for dark Callisto. About a third of Deimos's map is smeared filler. The Voyager-era maps of Mimas, Enceladus, Tethys, Dione, Rhea and Iapetus have large areas filled with white or smears, although Cassini later mapped these moons. Details in the [map table](#every-map-with-its-coverage).

All of these will be fixed, with every value checked against JPL Horizons and the IAU before it replaces the current one.

## Limitations of the model

Simplifications kept on purpose. They are listed so you know what the app does and does not show.

- **Visual aids not to scale:** the fixed-size dots and labels, the Sun's glow, comet tails, exaggerated ring opacity and computer-generated lumpy shapes. Each is described in [What is not to scale](#what-is-not-to-scale).
- **Placeholders:** bodies with no published radius get a placeholder size, marked *est.*; five small bodies with no published rotation period spin at an illustrative 12 hours ([details](catalogue/small-bodies.md#notes-on-sizes-and-rotation)).
- **Orbit models are simple, so precision depends on the date and the body** (see [Accuracy](#accuracy)):
  - planets and Pluto use Keplerian elements valid for 1800–2050; outside that range the time bar shows *Estimated positions*;
  - the Moon uses mean elements without periodic terms, good to a few degrees;
  - small bodies use a single two-body orbit. Asteroids stay close for years, but comets drift faster, because Jupiter and their own outgassing change their orbits (in November 2026, 9P/Tempel 1 is about 7° off and 1P/Halley about 0.3 AU off);
  - planetary moons are fitted to JPL Horizons over 1800–2050; outside that range, and outside the shorter range Horizons covers for 24 of them, their positions are estimates, and S/2025 U 1, not yet in Horizons, uses JPL's mean elements ([Moon orbits](#moon-orbits));
  - seven irregular moons keep a visible bend in their path, and so in their trail, where two of their fitted time windows meet ([Moon orbits](#moon-orbits)). Neighbouring windows are blended, which removes the jumps and the sharp turns elsewhere, but these moons' windows disagree too much on the direction of motion for the blend to hide it. A 250-year trail held on the parent planet shows: Margaret (Uranus) about 22° in 2032; Psamathe (Neptune) about 9° in 1814; S/2023 S 18 (Saturn) about 9° in 2007; Neso (Neptune) about 8° in 2050; S/2020 S 38 (Saturn) about 7° in 2027; S/2023 S 33 (Saturn) about 6° in 1999. S/2023 S 38 (Saturn) also turns sharply, mostly for a real reason: its orbit is extremely elongated (eccentricity about 0.9), so it swings round Saturn at each closest approach. The positions themselves stay within these moons' usual accuracy;
  - moons of dwarf planets and asteroids use two-body orbits, so their positions drift slowly, and the published orbits of Selam and Xiangliu leave their orientation uncertain.
- **Objects left out:** moons without a verifiable published orbit, such as Makemake's moon and Ida's moon Dactyl. The main asteroid belt, Jupiter trojans and Kuiper belt are statistical clouds, not catalogued objects ([Belts](#belts)).
- **Surfaces:** bodies with no spacecraft map get a painted texture, and Earth gets painted clouds. Some maps have gaps or filler from their sources: Solar System Scope fills gaps with invented terrain; Voyager 2 saw only part of Uranus's moons and Triton, and the app paints the rest; cloud maps (Venus, the giant planets) are snapshots, and Neptune's shows a dark spot that is now gone. See [Surface maps](#surface-maps).
- **One fixed rotation period per body:** comets' spins change at each pass near the Sun. 67P/Churyumov-Gerasimenko uses its last measured period (12.055 h, 2016), so its spin is only approximate at other dates ([details](catalogue/small-bodies.md#notes-on-sizes-and-rotation)).
- **One shared pole:** Uranus's five moons use Uranus's pole; their own IAU poles differ by about 0.1°.
- **Fixed spin poles for Triton and Iapetus:** both use their IAU 2015 pole at J2000, although the real poles move. Triton's circles Neptune's pole about every 690 years, so the app's axis is about 5° off in 2026 and up to about 46° off at the ends of the time bar (1000 and 3000). Iapetus's drifts more slowly: about 0.4° off in 2026, 12° in 1000 and 17° in 3000. See [Orientation](#orientation).
- **The sky:** star proper motion and precession are not modelled, and the sky is drawn as a backdrop at infinite distance, so its directions are true but distances are not shown ([The sky](#the-sky-beyond-the-solar-system)).

This is an educational model. For precise ephemerides, query [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/), which uses full numerical integrations (DE440 and satellite ephemerides).

## Further reading on reference frames

- Galileo Galilei (1632), *Dialogue Concerning the Two Chief World Systems*, Second Day (the ship thought experiment, the origin of Galilean relativity).
- NASA Science, *Solar System overview*: <https://science.nasa.gov/solar-system/>
- JPL, *Basics of Space Flight*, Chapter 2 "Reference Systems": <https://science.nasa.gov/learn/basics-of-space-flight/chapter2-1/>
