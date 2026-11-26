[← Documentation index](README.md) · [Project README](https://github.com/kauemelo01/Solar-System-Explorer#readme)

# Sources, methodology and accuracy

## What's included

Each group of objects follows its own rule:

| Group | What is included | Rule |
|---|---|---|
| The Sun, the planets and the Moon | All of them | — |
| Moons of the planets and Pluto (459) | **Every moon in JPL's *Planetary Satellite Mean Elements* table** <https://ssd.jpl.nasa.gov/sats/elem/>, as of November 2026 | Complete: a moon is added when JPL lists it. S/2025 U 1 is in that table but not yet in JPL Horizons, so it keeps JPL's mean elements ([Moon orbits](#moon-orbits)) |
| Moons of dwarf planets and asteroids (11) | Dysnomia, Hiʻiaka, Namaka, Weywot, Vanth, Xiangliu, Dimorphos, Selam, Skamandrios (Hektor), Queta (Eurybates) and Menoetius (Patroclus) | Complete: every moon of a body in the app with an orbit published in JPL Horizons or a peer-reviewed paper |
| Dwarf planets and candidates (5 + 4) | All five IAU dwarf planets (Ceres, Pluto, Eris, Haumea, Makemake), and the four largest candidates by measured diameter (Gonggong, Quaoar, Sedna, Orcus) | The four largest candidates, not every proposed one. A candidate is added when a measured diameter puts it among the four largest |
| Asteroids, centaurs and Kuiper belt objects (32) | The first asteroids discovered after Ceres (Pallas, Juno, Vesta) and Hygiea, the fourth largest; every body visited, or targeted by a mission already launched (Gaspra, Ida, Mathilde, Eros, Annefrank, Itokawa, Šteins, Lutetia, Toutatis, Bennu, Ryugu, Psyche, Didymos, Dinkinesh, Donaldjohanson, Eurybates, Polymele, Leucus, Orus, Patroclus, 1998 KY26, Arrokoth); parents of major meteor showers (Phaethon, Geminids; 2003 EH1, Quadrantids); and notable others (Apophis, Earth flyby in 2029; Hektor, the largest Jupiter trojan; Chiron, the first centaur found; Chariklo, the first small body found with rings) | Complete for spacecraft targets and shower parents, among bodies with a published size and orbit; a selection otherwise |
| Comets (15) | Every comet visited, or targeted by a mission already launched (1P/Halley, 9P/Tempel 1, 19P/Borrelly, 21P/Giacobini-Zinner, 26P/Grigg-Skjellerup, 67P/Churyumov-Gerasimenko, 81P/Wild 2, 103P/Hartley 2); parents of major meteor showers (109P/Swift-Tuttle, Perseids; 55P/Tempel-Tuttle, Leonids; 8P/Tuttle, Ursids; 21P/Giacobini-Zinner, Draconids; 1P/Halley, η-Aquariids and Orionids; 2P/Encke, Taurids); 2P/Encke, also one of the shortest periods known (3.3 years); and the great comets since 1990 with a published nucleus size (C/1996 B2 Hyakutake, C/1995 O1 Hale-Bopp), plus C/2020 F3 NEOWISE, kept from earlier releases with a placeholder size (see [Watchlist](#watchlist)) | Complete for spacecraft targets, shower parents and great comets since 1990, among comets with a published size and orbit |
| Ring systems (7) | Jupiter, Saturn, Uranus, Neptune, Haumea, Quaoar and Chariklo | Rings with measured radii ([catalogue/rings.md](catalogue/rings.md)) |
| Belts | The main asteroid belt, the Hilda asteroids, the Jupiter trojans, the Neptune trojans and the Kuiper belt | As statistical clouds, not catalogued objects ([Belts](#belts)) |
| Stars | All 9,096 stars of the *Yale Bright Star Catalogue* with a position and magnitude: essentially every star brighter than magnitude 6.5, about the naked-eye limit | Complete for that catalogue |
| Milky Way and faint stars | NASA's all-sky star map, built from over 100 million stars | Complete as a background image |
| Named bright stars (30) | The 21 brightest stars in the sky, down to Regulus (magnitude 1.35), plus well-known stars of familiar patterns (Castor, Polaris, Bellatrix, Orion's Belt, Mizar, Dubhe, Alcyone in the Pleiades) | A selection |
| Stars with known planets (5) | Proxima Centauri (the nearest), TRAPPIST-1 (seven planets), 51 Pegasi (first planet found around a Sun-like star), Kepler-186 and Kepler-452 (planets near Earth's size in the habitable zone) | A selection |
| Nebulae, clusters, galaxies and deep fields (29) | Well-known showpieces and famous NASA, Hubble and Webb images, such as the Pleiades, the Orion Nebula, Andromeda, the Pillars of Creation and the deep fields | A selection ([catalogue/sky.md](catalogue/sky.md)) |
| Constellations | All 88 IAU constellations | Complete |
| Surface maps | Bodies with a map made from spacecraft images: the Sun, the planets, the Moon, Saturn's rings, Ceres, Vesta and 18 major moons | Real images only ([Surface maps](#surface-maps)) |

## What's not included

Left out on purpose, and why:

- **Moons without a verifiable published orbit,** such as Makemake's moon (S/2015 (136472) 1, "MK2", whose orbit is only bounded) and Ida's moon Dactyl. They are added when an orbit is published.
- **Moons of small bodies that are not in the app.** Many asteroids and Kuiper belt objects have moons; only those of bodies in the app are shown.
- **Very small bodies, one by one.** More than a million asteroids and thousands of comets are known, most of them very small. The app draws a selection of well-known ones (see above). The rest are not drawn individually but treated as statistics: the belts (main asteroid belt, Jupiter trojans, Kuiper belt) show where they are, as statistical clouds.
- **Small bodies without a published size and orbit.** A body that meets an inclusion rule is added only when both its size and its orbit are published in a credible source (JPL, the IAU, a mission team or a peer-reviewed paper). Until then it goes on the [Watchlist](#watchlist).
- **Candidates beyond the four largest.** Other large trans-Neptunian objects, such as Salacia, 2002 MS4, Varda, Ixion and Varuna, have measured diameters smaller than Orcus (910 km), the smallest of the four candidates shown.
- **Unconfirmed rings,** such as the material seen around the centaur Chiron in stellar occultations (Sickafoose et al. 2023, *Planetary Science Journal* 4:221, [doi:10.3847/PSJ/ad0632](https://doi.org/10.3847/PSJ/ad0632)). The observations show material around Chiron, but whether it is a stable ring, and what its radius is, are still debated, so Chiron is drawn without rings. Rings are drawn only when they are confirmed and their radii measured ([catalogue/rings.md](catalogue/rings.md)).
- **Distant views from passing spacecraft.** A body counts as visited only when a spacecraft was sent past it, into orbit around it or onto it. Bodies photographed from far away on the way somewhere else, such as Masursky (Cassini, 1.6 million km, 2000) and 2002 JF56, now 132524 APL (New Horizons, 2006), are not included.
- **Targets of missions not yet launched,** such as the seven asteroids of the Emirates Mission to the Asteroid Belt. They are added when the mission launches ([Watchlist](#watchlist)).
- **Comets that no longer exist,** such as C/2011 W3 (Lovejoy), which broke up after its 2011 perihelion, and D/1993 F2 (Shoemaker-Levy 9), which hit Jupiter in 1994. They have no nucleus left to draw and no current orbit.
- **Interstellar objects,** such as 1I/ʻOumuamua, 2I/Borisov and 3I/ATLAS.
- **Spacecraft.** No spacecraft are drawn, such as the Voyagers, New Horizons or the James Webb Space Telescope, although many of the bodies they visited are in the app.
- **Planets of other stars.** Their host stars are labelled, but the planets themselves are not drawn.
- **Names for most stars.** All 9,096 catalogue stars are drawn, but only 30 have a name label; other bright stars, such as Adhara (ε Canis Majoris), are drawn without one.
- **Fainter stars as individual objects.** Stars fainter than about magnitude 6.5 appear only in the Milky Way background image.
- **Reference images in the sky.** The NASA images of nebulae, clusters and galaxies are linked from their cards and the catalogue, not drawn in the sky.
- **Invented surface maps.** Earlier versions used maps of Pluto, Charon and Titan that NASA calls "Fictional"; they were removed ([Surface maps](#every-map-with-its-coverage)). Bodies with no real map get a painted texture instead.

## Watchlist

Objects that meet an inclusion rule but are missing a piece of published data, or that may meet one soon. Each is added when the data it is waiting for is published. Checked against the JPL Small-Body Database in November 2026.

| Object | Rule it would meet | Waiting for |
|---|---|---|
| 9969 Braille | Visited (Deep Space 1 flyby, 1999) | A size we could verify. SBDB lists none, and the published shape (Oberst et al. 2001, *Icarus* 153; Buratti et al. 2004, *Icarus* 167) could not be checked in an open source |
| 98943 Torifune (2001 CC21) | Targeted (Hayabusa2 flyby, 2026) | A published size, expected from the flyby. SBDB lists none |
| 469219 Kamoʻoalewa (2016 HO3) | Targeted (Tianwen-2 sample return) | A published size, expected from Tianwen-2. SBDB lists none, and ground-based estimates are only ranges |
| 311P/PANSTARRS | Targeted (Tianwen-2, after Kamoʻoalewa) | A measured nucleus size; only an upper limit is published |
| C/1861 G1 (Thatcher) | Parent of the Lyrids | A nucleus size. Its orbit is in SBDB, from the 1861 apparition |
| C/2006 P1 (McNaught) and C/2023 A3 (Tsuchinshan-ATLAS) | Great comets since 1990 | A published nucleus size. Both are on open (hyperbolic) orbits, which the app would also need a new orbit solver for (`solveE()` handles closed orbits only) |
| C/2020 F3 (NEOWISE) | Great comets since 1990 (already in the app) | A published nucleus size, to replace the app's placeholder (2.5 km, marked *est.*) |
| (2026 ED138) | Dwarf planet candidates | A measured diameter. Its brightness (H = 2.85) suggests it could be among the four largest candidates |
| Makemake's moon (S/2015 (136472) 1) and Ida's moon Dactyl | Moons of bodies in the app | A published orbit |
| Shaun, Polymele's moon | Moon of a body in the app | A published orbit, expected from Lucy's 2027 flyby |
| Material around Chiron | Ring systems | Confirmation that it is a ring, with a measured radius |
| The seven Emirates Mission to the Asteroid Belt targets (Westerwald, Chimaera, Rockox, Ghaf, Ousha, Moza and Justitia; SBDB 10253, 623, 13294, 88055, 23871, 59980 and 269) | Targeted | The mission's launch, planned for 2028 |

## Naming convention

Object names follow **NASA/JPL**: the JPL Horizons record for planets and moons, and the JPL Small-Body Database plus NASA Science for small bodies. Comets therefore carry their full IAU designation (*1P/Halley*, *2P/Encke*, *67P/Churyumov-Gerasimenko*, *C/1995 O1 (Hale-Bopp)*). Numbered asteroids and dwarf planets appear by name only (*Ceres* for SBDB `1 Ceres`); their number and provisional designation are in the catalogue's *Designation (JPL)* column. Provisional moon designations use the IAU form *S/2023 S 1*, which Horizons stores as `S2023_S01`.

## Reference frame

All positions are computed in the **heliocentric ecliptic J2000** frame, the standard NASA/JPL frame for solar-system work. When you hold another body still, the app subtracts that body's position from every other position at each instant. That is a pure change of origin: the physics is unchanged, and only the point of view moves. This is the whole idea behind the project. A frame centred on the Sun, the Earth or Io describes the same motions.

## Scale

Distances and body sizes are always drawn to true scale. Bodies are therefore tiny compared with their orbits, as they really are, and you zoom in (or click a name to fly to it) to see them.

**To scale:** every position (computed in kilometres from the orbital elements), every body's radius, Saturn's rings (74,658–136,780 km), the orbit trails and the distance rings in AU.

### What is not to scale

These are visual aids drawn on top of the true-scale model; each is a [limitation of the model](#limitations-of-the-model):

| Element | What it really is |
|---|---|
| Coloured dots and labels marking bodies | A fixed 3.5–6 pixels on screen whatever the zoom, so bodies smaller than a pixel can still be found |
| The Sun's glow | A glow 7 times the Sun's radius, plus a halo of fixed screen size. The Sun's sphere itself is true size |
| Comet tails and comas | Drawn only while the comet is within 5 AU of the Sun. Illustrative length: the shorter of 0.6 AU and 0.3 / r² AU, where r is the comet's distance from the Sun in AU. Real tails vary widely and can exceed 1 AU |
| Bodies with no published radius | Placeholder radii, marked *est.* in the app and the catalogue: 1.5–40 km for moons, plus Arrokoth (≈ 9 km, a 36 km-long contact binary) and comet C/2020 F3 (NEOWISE) (2.5 km) |
| Irregular asteroids and small moons | Mean radius is correct; the lumpy shape is computer-generated, not the real shape |
| Main asteroid belt, Hildas, Jupiter and Neptune trojans, Kuiper belt | Statistical clouds of fixed-size points, not individual catalogued objects (see [Belts](#belts)) |
| Ring opacity | Radii are true, but rings are drawn more opaque than they are, so that faint and narrow rings (for example Jupiter's, with optical depths around 10⁻⁶) can be seen |
| The sky (stars, Milky Way, deep-sky objects) | Directions are true, but the sky is drawn on a backdrop that moves with the camera, so distances are not represented; the object's card gives its real distance. Star dot size shows brightness, not physical size |

## Planets

- **Elements:** E. M. Standish, *Keplerian Elements for Approximate Positions of the Major Planets*, JPL SSD. Table 1 (valid 1800 AD – 2050 AD), with linear rates per Julian century. <https://ssd.jpl.nasa.gov/planets/approx_pos.html>
- The Earth and the Moon are placed around the **Earth–Moon barycentre** (EMB) using the Earth/Moon mass ratio (μ = 0.0121505).
- **Pluto** uses the Pluto row of the original version of Standish's Table 1, which JPL has since removed from its web copy (the page now notes that "the former planet Pluto has also been removed"). Checked against JPL Horizons, it places Pluto within 0.01° (about 0.01 AU) of its true position from 1900 to 2100 AD, much closer than a single osculating orbit from the SBDB would (up to 0.45 AU). Pluto is a dwarf planet and is listed and shown with the dwarf planets.
- **Physical data:** JPL *Planetary Physical Parameters* <https://ssd.jpl.nasa.gov/planets/phys_par.html>; NASA NSSDCA *Planetary Fact Sheets* <https://nssdc.gsfc.nasa.gov/planetary/planetfact.html>.
- **Spin poles and rotation periods:** B. A. Archinal et al. (2018), *Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015*, Celestial Mechanics and Dynamical Astronomy 130:22. <https://doi.org/10.1007/s10569-017-9805-5>. Machine-readable form: NAIF PCK `pck00011.tpc` <https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc>.

## The Moon

A mean-element lunar orbit (node and perigee regressing and precessing at their mean rates; e = 0.0549, i = 5.145°, a = 384,400 km) around the Earth. Reference: NASA NSSDCA *Moon Fact Sheet* <https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html>.

## Natural satellites of the planets and Pluto (459)

- **Elements:** JPL SSD, *Planetary Satellite Mean Elements*. <https://ssd.jpl.nasa.gov/sats/elem/>. Regular moons use elements referred to their local Laplace plane (pole RA/Dec given in the table). Distant irregular moons use elements referred to the ecliptic.
- **Sizes:** from JPL first, then from NASA and published surveys; 363 moons with no published radius use a placeholder. See [Moon sizes](#moon-sizes) below.
- **Identifiers:** NAIF integer IDs, cross-checked in JPL Horizons. <https://ssd.jpl.nasa.gov/horizons/>
- **Discoveries and families:** JPL *Satellite Discovery Circumstances* <https://ssd.jpl.nasa.gov/sats/discovery.html>; S. S. Sheppard (Carnegie Science) moon pages <https://sites.google.com/carnegiescience.edu/sheppard/moons>; IAU Minor Planet Center electronic circulars <https://minorplanetcenter.net/mpec/RecentMPECs.html>.
- **Count:** 459 moons as of November 2026 (Mars 2, Jupiter 115, Saturn 292, Uranus 29, Neptune 16, Pluto 5). Earth's Moon is counted with the planets. With the 8 moons of other dwarf planets, candidates and asteroids below, the app has 467 moons.
- **Naming differences:** *S/2009 S 2* (NAIF 65304) follows JPL Horizons. *Megaclite* and *Philophrosyne* follow JPL Horizons; the JPL mean-elements table spells them `Magaclite` and `Philophrosyn`.
- **Pluto's moons** use JPL's mean equatorial elements, referred to Pluto's equator with the IAU 2015 pole (RA 132.993°, Dec −6.163°), and are fitted to Horizons like the other moons: Charon to 0.06°, the four small moons to 1.4–2.8°.
- **Positions:** fitted to JPL Horizons over 1800–2050 AD; see [Moon orbits](#moon-orbits) below. The fits replace the mean elements' epochs (JPL gives most for 2000-01-01, some groups for 2009, 2020 or 2025), which the app used to treat as 2000.

### Moon sizes

Each moon's radius comes from the first of these sources that gives one, checked in November 2026:

1. **JPL SSD, *Planetary Satellite Physical Parameters*** <https://ssd.jpl.nasa.gov/sats/phys_par/>: 45 moons (46 with Earth's Moon), with measured mean radii.
2. **The moon's JPL Horizons record** <https://ssd.jpl.nasa.gov/horizons/>: 27 more. Where Horizons gives three axes (for example Pan, 17.2 × 15.4 × 10.4 km), the app uses the radius of a sphere of the same volume, as JPL's table does.
3. **Published elsewhere**: 24 more, all small irregular or ring moons whose size is estimated from their brightness, assuming a dark surface (geometric albedo 0.04 to 0.06):
   - NASA Science moon pages: Ymir, Paaliaq, Tarvos, Ijiraq, Kiviuq, Albiorix, Skathi and Siarnaq (Saturn), Perdita (Uranus) and Hippocamp (Neptune);
   - Sheppard, Jewitt & Kleyna (2005), *AJ* 129, 518, Table 3 ([arXiv:astro-ph/0410059](https://arxiv.org/abs/astro-ph/0410059)): Uranus's Prospero, Setebos, Stephano, Trinculo, Francisco, Ferdinand and Margaret;
   - Sheppard, Jewitt & Kleyna (2006), *AJ* 132, 171, Table 3 ([arXiv:astro-ph/0604552](https://arxiv.org/abs/astro-ph/0604552)): Neptune's Halimede, Sao, Laomedeia, Psamathe and Neso;
   - Jewitt, Sheppard & Porco (2004), *Jupiter's Outer Satellites and Trojans*, Table 12.1: Jupiter's Themisto and Callirrhoe (half the listed diameter).
4. **None of these**: the other 363 moons have no published radius, so the app gives them a small placeholder size for display, marked *est.* in the app and the catalogue ([What is not to scale](#what-is-not-to-scale)). Mab and Cupid are among them: their discovery paper gives sizes, but it is not openly available to check.

Each moon page in the catalogue lists which source each radius comes from. Earlier versions used radii from compilations whose sources were not documented; 35 of them differed from JPL's current values (for example Leda 10.8 km, now 5; Sycorax 78.5 km, now 60; Nix 25 km, now 18).

### Moon orbits

The app places every planetary moon with an orbit fitted to its **JPL Horizons ephemeris** <https://ssd.jpl.nasa.gov/horizons/>, from 4 January 1800 to 1 January 2051 AD, or the part of that range Horizons covers. The fits are in `data/moon-orbits.js` and are built by the scripts in [`tools/moon-orbit-fits/`](../tools/moon-orbit-fits/) (how to rerun them: its README). Each moon has one of two kinds of fit:

- **One orbit for the whole range (113 moons, most regular moons).** JPL's orbit shape, with its phase, mean motion, apsidal and nodal precession, a slow drift and up to two periodic terms fitted to Horizons. For the four moons in co-orbital resonances (Janus and Epimetheus, which swap orbits every four years, and Dione's companions Helene and Polydeuces) a table of along-track corrections every 5 or 10 days, taken from Horizons, is added.
- **Time windows (345 moons, mostly irregular).** The Sun disturbs these orbits too much for one ellipse, so each moon has consecutive windows of 10 years, split down to 2.5 years where needed, each with its own fitted ellipse. Each window is fitted to both the direction and the distance of the Horizons positions, and the app blends neighbouring windows across each boundary (over 120 days either side, or 15% of the orbital period for slow moons such as Neso), so a moon never jumps from one window's orbit to the next, and its path (and its trail) bends smoothly there. Seven moons keep a visible bend; see [Limitations of the model](#limitations-of-the-model).

The fits use Horizons positions every 60 days, plus a dense stretch near 2000 for the fast inner moons, so that their speed is not mistaken for another one that fits the same 60-day samples. S/2009 S 2 is fitted in Saturn's equatorial plane, which the JPL table does not give.

**Checked independently.** Every fit is compared with Horizons positions on dates it was not fitted to (every 211 days), computed with the app's own code. Typical errors (median over the moons of each planet; for each moon, the root-mean-square error over 1800–2050 AD):

| Moons of | Moons | Typical error | Least accurate |
|---|---|---|---|
| Mars | 2 | 1.0° | Phobos, 1.9° |
| Jupiter | 115 | 1.5° | Carpo, 3.6° |
| Saturn | 292 | 1.5° | Methone, 3.4° |
| Uranus | 28 | 0.8° | Desdemona, 2.9° |
| Neptune | 16 | 0.3° | Naiad, 3.4° |
| Pluto | 5 | 1.7° | Styx, 2.8° |

Over all 458 fitted moons the typical error is 1.5°, and 90% of moons are within 2.4°; no moon's typical error is above 3.6°. The major moons are within a fraction of a degree (Io 0.03°, Titan 0.03°, Triton 0.29°, Charon 0.06°; Mimas, in resonance with Tethys, 2.8°). Before these fits, with JPL's mean elements alone, the same check gave a typical error of 92°. The largest single errors come from eccentric irregular orbits near their closest approach to the planet: S/2023 S 5 up to 24°, S/2023 S 38 and Pasiphae up to 21°.

**Distances** are checked the same way: the distance from the planet is typically within 1.6% of Horizons, and every moon is within 5% on average (root-mean-square over 1800–2050 AD).

**Where Horizons covers less than 1800–2050 AD**, the moon's card says *Estimated position* outside its own range: Uranus's 13 inner moons from Cordelia to Cupid (Horizons from 1900 AD), Saturn's Janus, Epimetheus, Atlas, Prometheus, Pandora, Pan, Pallene, Anthe, Aegaeon and S/2009 S 2 (1950–2050 AD), and Daphnis (1990–2018 AD). **S/2025 U 1** is not yet in Horizons: it keeps JPL's mean elements, at their 2025 epoch, and its card says so.

**Outside 1800–2050 AD** the fits are extended, and the time bar shows *Estimated positions*. A test of the same method 150 years beyond its fitted range kept one-orbit moons within about 0.5° (Io 0.06°, Titan 0.16°, Iapetus 0.38°), and their errors grow slowly beyond that. Windowed moons keep their first or last window: their orbit's size, shape and direction stay right, but within a few decades their position along it is no longer meaningful.

Orbit outlines follow the fits, so they turn as the orbits precess.

## Moons of dwarf planets and asteroids (11)

- **JPL Horizons satellite solutions:** Dysnomia (Eris), Weywot (Quaoar), Vanth (Orcus) and Dimorphos (Didymos), as osculating J2000 ecliptic elements about each primary, 2025-Jan-1. Menoetius (Patroclus): elements computed from the Horizons satellite solution's position and velocity relative to Patroclus on 2025-Jan-1, with the measured period of 4.282753 days (Brozović et al. 2024, *AJ* 167:104, [doi:10.3847/1538-3881/ad1f6e](https://doi.org/10.3847/1538-3881/ad1f6e)).
- **Published orbits:**
  - Hiʻiaka and Namaka (Haumea): Ragozzine & Brown 2009, *AJ*, [arXiv:0903.4213](https://arxiv.org/abs/0903.4213).
  - Xiangliu (Gonggong): Kiss et al. 2019, *Icarus*, [arXiv:1903.05439](https://arxiv.org/abs/1903.05439); prograde solution, orientation uncertain ([limitation of the model](#limitations-of-the-model)).
  - Selam (Dinkinesh): Levison et al. 2024, *Nature*, [arXiv:2406.19337](https://arxiv.org/abs/2406.19337); distance and period only.
  - Skamandrios (Hektor): Marchis et al. 2014, *ApJ* 783:L37, [arXiv:1402.7336](https://arxiv.org/abs/1402.7336); elements in the J2000 equatorial frame, Table 2.
  - Queta (Eurybates): Brown et al. 2021, *Planetary Science Journal* 2:170, [doi:10.3847/PSJ/ac07b0](https://doi.org/10.3847/PSJ/ac07b0); J2000 ecliptic elements, Table 1.
- **Left out:** moons without a verifiable published orbit, such as Makemake's moon (orbit only bounded), Ida's moon Dactyl and Polymele's moon Shaun (a [limitation of the model](#limitations-of-the-model); see [What's not included](#whats-not-included)).
- **In the app:** listed in the moons menu under *Dwarf planets & candidates* or *Asteroids*; switching one on also shows its parent's group.
- Details per moon: [catalogue/moons-small-bodies.md](catalogue/moons-small-bodies.md).

## Ring systems (7)

- **Jupiter, Uranus, Neptune, Saturn:** NASA NSSDCA ring fact sheets. Saturn's rings also use an image strip from Solar System Scope when realistic textures are on (see [Surface maps](#surface-maps)).
- **Haumea:** Ortiz et al. 2017, *Nature*, [arXiv:2006.03113](https://arxiv.org/abs/2006.03113).
- **Quaoar:** Morgado et al. 2023, *Nature*; Pereira et al. 2023, *A&A*, [arXiv:2304.09237](https://arxiv.org/abs/2304.09237).
- **Chariklo:** Braga-Ribas et al. 2014, *Nature*, [arXiv:1409.7259](https://arxiv.org/abs/1409.7259).
- Rings are drawn in the body's equatorial plane at true radii; opacity is exaggerated. Details: [catalogue/rings.md](catalogue/rings.md).

## Dwarf planets, candidates, asteroids, centaurs and comets (55, plus Pluto)

Pluto is grouped with the dwarf planets in the app and the catalogue, but its orbit comes from the planetary table above, so it is not counted in this section's data. In the app, the five IAU dwarf planets (Ceres, Pluto, Eris, Haumea, Makemake) are under the *Dwarf planets* switch and the four candidates (Gonggong, Quaoar, Sedna, Orcus) under *Candidates*.

- **Elements:** JPL Small-Body Database (osculating heliocentric elements; epoch JD 2461200.5 = 2026-Jun-09 TDB for most objects, and the most recent perihelion solution for comets). <https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html>, API: <https://ssd-api.jpl.nasa.gov/doc/sbdb.html>
- **Sizes and rotation periods:** the most recent published measurement: the SBDB diameter and rotation period, unless a newer source exists or the SBDB lists none. Every value from another source is cited in [the catalogue's notes](catalogue/small-bodies.md#notes-on-sizes-and-rotation) and linked from the object's card (*source*). Eight bodies with no published rotation period we could verify spin at an illustrative 12 hours.
- **Designations:** IAU Minor Planet Center. <https://www.minorplanetcenter.net/>
- **Spin poles** of small bodies are not modelled from data. They are randomised for display only (a [limitation of the model](#limitations-of-the-model)), except thirty taken from published data: Ceres and Vesta (IAU 2015, Archinal et al. 2018, so that their surface maps sit north-up); Pallas, Lutetia, Eros, Itokawa, Gaspra, Šteins, 9P/Tempel 1, 19P/Borrelly and 67P/Churyumov-Gerasimenko (IAU 2015, as given in NAIF's [`pck00011.tpc`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc)); Bennu (OSIRIS-REx, [`bennu_v17.tpc`](https://naif.jpl.nasa.gov/pub/naif/ORX/kernels/pck/bennu_v17.tpc)); Ryugu (Hayabusa2, [`ryugu_v10.tpc`](https://naif.jpl.nasa.gov/pub/naif/pds/pds4/hyb2/hyb2_spice/spice_kernels/pck/ryugu_v10.tpc)); Psyche (Shepard et al. 2021, *Planetary Science Journal* 2:125, [doi:10.3847/PSJ/abfdba](https://doi.org/10.3847/PSJ/abfdba)); Haumea (Hiʻiaka's orbit pole, which its ring shares), Quaoar (ring pole), Chariklo (ring pole) and Ida (NAIF `pck00011`); Didymos (DART, [`didymos_system_15.tpc`](https://naif.jpl.nasa.gov/pub/naif/pds/pds4/dart/dart_spice/spice_kernels/pck/didymos_system_15.tpc)); Donaldjohanson and Eurybates (Lucy, [`donaldjohanson_v12.tpc`](https://naif.jpl.nasa.gov/pub/naif/LUCY/kernels/pck/donaldjohanson_v12.tpc) from Lucy's 2025 flyby images, and [`eurybates_v11.tpc`](https://naif.jpl.nasa.gov/pub/naif/LUCY/kernels/pck/eurybates_v11.tpc) from Mottola et al. 2023, *Planetary Science Journal* 4:18); Arrokoth (New Horizons, [`nh_arrokoth_002.tpc`](https://naif.jpl.nasa.gov/pub/naif/pds/data/nh-j_p_ss-spice-6-v1.0/nhsp_1000/data/pck/nh_arrokoth_002.tpc), Porter 2024 shape model); Polymele (Lucy, [`polymele_v11.tpc`](https://naif.jpl.nasa.gov/pub/naif/LUCY/kernels/pck/polymele_v11.tpc)); Leucus (Mottola et al. 2020, *Planetary Science Journal* 1:73, [arXiv:2009.08951](https://arxiv.org/abs/2009.08951)); Orus (Mottola et al. 2023, *Planetary Science Journal* 4:18, Table 3, [doi:10.3847/PSJ/acaf79](https://doi.org/10.3847/PSJ/acaf79)); Patroclus (the orbit pole of its moon Menoetius, which it turns in step with; Brozović et al. 2024); and Juno, Hygiea, Hektor and Phaethon from the [DAMIT](https://damit.cuni.cz/projects/damit/) database of asteroid models (Viikinkoski et al. 2015, *A&A* 581, L3; Vernazza et al. 2020, *Nature Astronomy* 4; Hanuš et al. 2015, *Icarus* 256; Hanuš et al. 2018, *A&A* 620), whose ecliptic poles (λ, β) are converted to RA and Dec. The other twenty-five have no published pole the app can use: Eris, Makemake, Gonggong, Sedna, Orcus, Chiron, Mathilde, Annefrank, 1998 KY26, 2003 EH1, Dinkinesh (Lucy's kernel uses a placeholder pole), Apophis, Toutatis, 1P/Halley and 103P/Hartley 2 (these four tumble, with no single spin axis), 81P/Wild 2 (Stardust's kernel gives a pole but not which way the comet turns), 2P/Encke, C/1995 O1 (Hale-Bopp), C/1996 B2 (Hyakutake), 109P/Swift-Tuttle, 55P/Tempel-Tuttle, 8P/Tuttle, 21P/Giacobini-Zinner, 26P/Grigg-Skjellerup and C/2020 F3 (NEOWISE).

## Belts

The main asteroid belt, the Hilda asteroids, the Jupiter and Neptune trojans and the Kuiper belt are **statistical point clouds** drawn from typical orbital distributions (semi-major axis, eccentricity, inclination ranges). They show where those populations are, not individual catalogued objects. Overview: NASA Science <https://science.nasa.gov/solar-system/asteroids/>, <https://science.nasa.gov/solar-system/kuiper-belt/>. This is a [limitation of the model](#limitations-of-the-model).

- **Jupiter trojans (1,600 points):** around Jupiter's L4 and L5 points, 60° ahead of and behind Jupiter, moving with it.
- **Hilda asteroids (1,200 points):** asteroids in the 3:2 resonance with Jupiter (three orbits for every two of Jupiter's). The resonant angle 3λ<sub>J</sub> − 2λ − ϖ stays near 0°, so each Hilda reaches aphelion near Jupiter's L3, L4 or L5 point, and together they form a triangle that turns with Jupiter. The proper semi-major axis, eccentricity and inclination are drawn from the bias-corrected model of the background population in Vokrouhlický et al. 2025, *Astronomical Journal* 169:242 ([doi:10.3847/1538-3881/adbe7b](https://doi.org/10.3847/1538-3881/adbe7b), Table 3); each eccentricity adds the forced term, 1.47 times Jupiter's eccentricity along Jupiter's perihelion, as in that paper. Simplifications: every Hilda moves exactly 1.5 times as fast as Jupiter, so the triangle never smears; the libration amplitude is derived from the proper semi-major axis with a pendulum approximation (not part of the published model), and stays fixed rather than librating over its 250–350-year period; the inclinations, which the paper refers to the invariable plane, are applied to the ecliptic (1.6° apart).
- **Neptune trojans (800 points):** around Neptune's L4 and L5 points, with a libration amplitude (Rayleigh, width 15°), eccentricity (Rayleigh, width 0.045) and inclination (sin i times a Gaussian, width 14°) from the debiased distributions of Lin et al. 2021, *Icarus* 361, 114391 ([arXiv:2006.10674](https://arxiv.org/abs/2006.10674)), the OSSOS survey. That study covers L4; the app assumes the same distribution at L5.

## The sky beyond the solar system

- **Stars:** *Yale Bright Star Catalogue*, 5th revised ed. (D. Hoffleit & W. H. Warren Jr., 1991; CDS V/50), via the NASA HEASARC table `bsc5p` <https://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html>. All 9,096 entries with a position and V magnitude are drawn; colour comes from B−V.
- **Milky Way and faint stars:** NASA/Goddard Space Flight Center Scientific Visualization Studio, *Deep Star Maps* (2009) <https://svs.gsfc.nasa.gov/3895>. Plate carrée map in J2000 right ascension and declination, built from over 100 million stars in the Bright Star, Tycho-2 and UCAC3 catalogues. The app ships two sizes; see [Sky map loading](#sky-map-loading).
- **Deep-sky positions:** CDS SIMBAD and the Sesame name resolver (J2000).
- **Deep-sky reference images:** NASA Image and Video Library <https://images.nasa.gov/>, linked from each object's card and catalogue entry (not drawn in the sky; see [What's not included](#whats-not-included)). Credits are listed in [catalogue/sky.md](catalogue/sky.md).
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

Bodies with a surface map in `textures/` are drawn with it. All others keep a simple texture painted in code (`texFor()` in `index.html`). **Not every map is complete.** Some are partial and some have gaps filled in by their makers. Each map is listed below with what its publisher says about it. Each object's card in the app also carries a one-line note saying what its surface image is (see [Card notes](#card-notes)). The remaining gaps, where no better published map exists, are [limitations of the model](#limitations-of-the-model).

### Sources

- **Solar System Scope**, *Solar Textures* <https://www.solarsystemscope.com/textures/>, CC BY 4.0. The publisher says the maps are "based on NASA elevation and imagery data", with colours tuned to true-colour photos from MESSENGER, Viking and Cassini and made "slightly more saturated". Gaps in the data "are filled with fictional terrain that corresponds with the rest of the landscape". The publisher does not say which parts are filled (a [limitation of the model](#limitations-of-the-model)).
- **NASA 3D Resources** <https://github.com/nasa/NASA-3D-Resources>, free to use under NASA's media guidelines. These maps come from the JPL/Caltech planetary map database and are mostly old Voyager and Viking mosaics, from before Galileo and Cassini. The descriptions below are quoted from each map's page at <https://science.nasa.gov/3d-resources/>.
- **NASA/JPL Photojournal**, PIA18668 *Map of Triton* <https://www.jpl.nasa.gov/images/pia18668-map-of-triton/> (Paul Schenk, Lunar and Planetary Institute, 2014), from Voyager 2 images. Public domain.
- **NASA/JPL Photojournal**, PIA18434–PIA18439 *Color Maps of* Dione, Enceladus, Iapetus, Mimas, Rhea and Tethys (Paul Schenk, Lunar and Planetary Institute, 2014), global maps from Cassini images: <https://photojournal.jpl.nasa.gov/catalog/PIA18437> (Mimas; the others are PIA18434 Dione, PIA18435 Enceladus, PIA18436 Iapetus, PIA18438 Rhea, PIA18439 Tethys). Credit: NASA/JPL-Caltech/Space Science Institute/Lunar and Planetary Institute. Their colours are enhanced beyond human vision (into the ultraviolet and infrared), so the app uses them in black-and-white.
- **USGS Astrogeology**, *Callisto Voyager/Galileo SSI global mosaic*, 1 km per pixel <https://planetarymaps.usgs.gov/mosaic/Callisto_Voyager_GalileoSSI_global_mosaic_1km.tif>. Public domain.
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
| Deimos | NASA 3D Resources | 1440 × 720 | Viking images, processed by USGS | Roughly a third of the map (one side) is smeared filler, and no better global map is published (a [limitation of the model](#limitations-of-the-model)) |
| Io | NASA 3D Resources | 1440 × 720 | USGS mosaic of Voyager images; "data gaps near the poles" | The polar gaps (black in the original) are filled in the app with the painted texture (a [limitation of the model](#limitations-of-the-model)) |
| Europa, Ganymede | NASA 3D Resources | 1440 × 720 | USGS mosaic with Voyager images | Black-and-white; some smeared filler near the poles |
| Callisto | USGS Astrogeology | 2048 × 1024 | Global mosaic of Voyager and Galileo images | About 3% has no images (a wedge near the south pole and a corner of the north): the app fills it with the painted texture |
| Mimas, Enceladus, Tethys, Dione, Rhea, Iapetus | NASA/JPL PIA18434–PIA18439 (Cassini) | 2048 × 1024 | Global maps from Cassini images, shown in black-and-white | Complete; the published colours are enhanced, so the app uses brightness only |
| Miranda, Ariel, Umbriel, Titania, Oberon | NASA 3D Resources | 1440 × 720 | USGS (Tammy Becker) mosaic of Voyager 2 images | Black-and-white. Voyager 2 saw only the southern hemispheres; the app fills the north (about 60% of each map) with the painted texture (a [limitation of the model](#limitations-of-the-model)) |
| Triton | NASA/JPL PIA18668 (Paul Schenk, 2014) | 2048 × 1024 | Voyager 2 images, enhanced colour | About half of Triton, mostly the southern hemisphere; the north was in polar night during the 1989 flyby. The app fills the unseen part with the painted texture, so a seam is visible (a [limitation of the model](#limitations-of-the-model)) |

Bodies with no map keep the painted texture (a [limitation of the model](#limitations-of-the-model); see [What's not included](#whats-not-included)): Hyperion, all dwarf planets and candidates except Ceres, the asteroids except Vesta, and the comets.

**Removed maps** (see [What's not included](#whats-not-included)). Earlier versions used NASA 3D Resources maps for Pluto, Charon and Titan. NASA's own pages call all three "Fictional": Pluto was stitched from a painting by Pat Rawlings, Charon was "faked from some Magellan images", and Titan is a "concept". They were dropped, and these bodies use the painted texture again. Real maps exist for Pluto and Charon (New Horizons, 2015) and Titan (Cassini radar and infrared) and could be added later.

### Processing

All of the steps below are done by [`tools/build_textures.py`](../tools/build_textures.py), which downloads every source and rebuilds `textures/` (run `python3 tools/build_textures.py` from the repository root; it needs Pillow and about 400 MB of downloads, cached in `.texture-cache/`). Its output matches the committed files exactly.

- The large Solar System Scope maps are recompressed to JPEG quality 80; the 2K ones are used as published.
- The NASA maps are recompressed to JPEG quality 85.
- For Io, the Uranian moons and Triton, the unmapped area (black in the originals) is made transparent and saved as WebP. In the app it is filled with the painted texture, so a seam is visible where they meet.
- The Ceres and Vesta mosaics (21093 and 26703 pixels wide) and the Triton map (14138 pixels wide) are scaled down to 2048 × 1024.
- The Cassini maps of Saturn's six icy moons (11741 to 15960 pixels wide) are converted to black-and-white and scaled down to 2048 × 1024.
- The USGS Callisto mosaic (15138 pixels wide) is scaled down to 2048 × 1024; its no-data area is made transparent and saved as WebP, so the app fills it with the painted texture.

### How they load

1. **Each body starts in its plain colour** and switches to its map when the file arrives. Maps are downloaded only while realistic textures are on (see below), and then every map is requested as soon as the page opens, not when you fly to a body.
2. **Capable devices try the large map first** (same test as the [sky map](#sky-map-loading)); if it fails they load the 2K map. Other devices load the 2K map directly. The test is made once, when the page opens. Saturn's ring strip follows the same rule (8192 px, then 2048 px).
3. **The painted texture is the fallback**, used only if every file for that body fails to load.

There is no manual choice of size for surface maps: the *Auto / 4K / 8K* buttons under *Images → Sky map detail* apply to the sky map only.

**Turning them off.** The side panel's *Images → Realistic surface textures* switch (on by default, remembered on the device) turns all real maps off. Every body then uses its painted texture, Saturn's rings use the painted ring, Earth's clouds are hidden, the surface notes on the cards are hidden, and no map files are downloaded. Turning it back on reuses any maps already downloaded.

**Sphere detail.** Bodies with a map are drawn as smoother spheres (64 × 40 segments, as for the planets) so the map does not look faceted; other moons and small bodies use 32 × 20. Sizes and shapes are unchanged, and Vesta, Phobos and Deimos keep their lumpy shapes.

### Orientation

- **North is up on every map, and for 68 bodies longitude is aligned too**, so the side facing you is the real one: see [Which side faces you](#which-side-faces-you) below.
- **Some maps are turned 180°: those of bodies that rotate backwards.** The IAU defines a planet's or moon's *north* pole as the one on the north side of the solar system's main plane (the invariable plane), whichever way the body turns. Seen from that pole, most bodies turn counter-clockwise (*prograde*). Venus, Uranus, Uranus's five major moons (Miranda, Ariel, Umbriel, Titania, Oberon) and Neptune's moon Triton turn clockwise (*retrograde*): their IAU 2015 spin rates are negative. Triton turns once per orbit, and its orbit is retrograde.
  - The app always turns a body counter-clockwise about the pole it is given. To make these eight bodies turn the right way, it gives them the pole opposite the IAU north pole: for Venus (92.76°, −67.16°) instead of (272.76°, +67.16°), for Uranus and its moons (77.31°, +15.18°) instead of (257.31°, −15.18°), and for Triton (118.45°, −20.30°) instead of (298.45°, +20.30°). Both are the IAU 2015 values ([Archinal et al. 2018](https://doi.org/10.1007/s10569-017-9805-5)), only reversed.
  - Surface maps are drawn with IAU north at the top. Placed with their top at the app's pole, these eight maps would be upside down, so the app turns them 180°. This is a rotation, not a mirror image: north ends up at the IAU north pole, east and west keep their real layout, and the body still spins the right way.
  - Example: Voyager 2 photographed only the southern hemispheres of Uranus's moons. After the turn, the mapped half sits around each moon's IAU south pole, as it should.
  - Prograde bodies use the IAU north pole directly, and their maps are not turned: the Sun, Mercury, Earth, the Moon, Mars, Jupiter, Saturn, Neptune, Ceres, Vesta, and the moons of Mars, Jupiter and Saturn that have maps.
  - One approximation: the app gives Uranus's five moons Uranus's own pole. The IAU's poles for these moons differ from it by about 0.1° (for example Ariel at 257.43°, −15.10°), which is not visible. This is a [limitation of the model](#limitations-of-the-model).
  - Triton's IAU pole moves: it circles Neptune's pole about every 690 years, following Triton's orbit. The app uses its value at J2000, computed from the IAU 2015 series as given in NAIF's [`pck00011.tpc`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc). It lies within about 0.5° of the axis of the app's Triton orbit at J2000. Holding the pole fixed is a [limitation of the model](#limitations-of-the-model).
  - **Iapetus** uses its IAU spin pole (318.16°, 75.03°), not the pole of its orbit plane from JPL's table (288.7°, 78.9°), which is about 8° away. Its IAU pole drifts slowly; the app uses the J2000 value (a [limitation of the model](#limitations-of-the-model)).

The logic is in `index.html`, next to the comment `surface maps`.

### Which side faces you

The app turns **71 bodies** so that their prime meridian (longitude 0°) points where the IAU says it does at that moment: the Sun, the eight planets, the Moon, Pluto and Charon, 49 moons of the planets (all of Mars's, Jupiter's four large moons and four inner ones, Saturn's seven main moons, Phoebe and nine small inner ones, Uranus's five major and ten inner moons, Triton and Neptune's six inner moons), and Ceres, Pallas, Gaspra, Lutetia, Šteins, Eros, Itokawa, 9P/Tempel 1, 19P/Borrelly and 67P/Churyumov-Gerasimenko.

- **Source:** IAU 2015 rotational elements ([Archinal et al. 2018](https://doi.org/10.1007/s10569-017-9805-5)) as given in NAIF's [`pck00011.tpc`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc): W = W₀ + Ẇ·d (+ Ẅ·d²), plus the periodic terms that the IAU gives for many bodies, such as the Moon's libration terms. d is days from J2000.
- **Maps:** to place the prime meridian, the app needs each map's longitude layout. Every map has 0° at its centre and east to the right, checked against landmarks at known longitudes: Greenwich (Earth), Mare Crisium (the Moon), Olympus Mons and Syrtis Major (Mars), the Caloris basin and Kuiper crater (Mercury), Valhalla (Callisto), Cassini Regio (Iapetus), Herschel crater (Mimas), Pele and Loki (Io). The exceptions have 180° at their centre: **Ceres**'s Dawn mosaic (checked with Occator crater at 239°E), the Cassini maps of Saturn's icy moons (Herschel on Mimas, Odysseus on Tethys, Cassini Regio on Iapetus, the bright wisps on Dione and Rhea) and the USGS Callisto mosaic (Valhalla).
- **Checked** with the app's own code: on 21 June 2026 at 12:00 UTC the Sun is overhead at 0.6°E on Earth (expected about 0.4°E); the Moon faces Earth within 8°, its real libration; the other tidally locked moons face their planet within 1–7°, including the backward-spinning ones (Uranus's moons within 2°, Triton within 6°). Mimas is off by up to about 20°: the IAU's model for it has a 45° libration term, from its resonance with Tethys, that is not quite in step with the app's fitted orbit.
- **Not aligned** (a [limitation of the model](#limitations-of-the-model)): Vesta, whose Dawn mosaic does not say which of Vesta's two longitude systems it uses (the Dawn team's or the IAU's), and every body without IAU rotational elements (most small moons and small bodies). These spin at their true rate from an arbitrary starting angle. On the giant planets, Venus and the Sun the surfaces are clouds or gas that move, so the map shows a representative view.

### Earth's clouds

The Earth map is cloud-free, which looks artificial, so the app draws a separate layer of random clouds just above it. There is no weather model: the clouds are fixed noise patterns, the same on every visit, and they turn with the planet. They are shaped to look plausible: stretched east–west, a little denser near the equator and at mid-latitudes, and thinner in the subtropics. They cover about a fifth of the globe (real cloud cover is about two-thirds). The layer is generated a few rows at a time after the Earth map loads, so the page does not stall. It is added only on top of the real map, not the painted fallback. The code is in `index.html`, next to the comment `Earth's clouds`. The painted clouds are a [limitation of the model](#limitations-of-the-model).

### Card notes

Each object's card in the app has a short note under its type saying what its surface image is. Every note fits in two lines on the card, on desktop and phone screens.

| Note | Used for |
|---|---|
| Surface: real spacecraft photos | Ceres, Vesta, Phobos, Mimas, Enceladus, Tethys, Dione, Rhea, Iapetus |
| Surface: based on real spacecraft photos | Mercury, Earth, the Moon, Mars (Solar System Scope: colours tuned and any gaps filled by the publisher) |
| Clouds: based on real photos, but they change constantly | Venus, Jupiter, Saturn, Uranus, Neptune |
| Representative image: the Sun has no fixed surface | The Sun |
| Surface: real photos; gaps filled in by map makers | Deimos, Europa, Ganymede |
| Surface: real photos, partial; the rest is painted | Io, Callisto, Miranda, Ariel, Umbriel, Titania, Oberon, Triton |
| Surface: painted illustration, not a real image | Every other body drawn as a sphere or lumpy shape, including Pluto, Charon and Titan |
| Plain shape; no surface image | The small moons, including the moons of dwarf planets, candidates and asteroids, drawn as plain-coloured shapes |

Some notes add a short detail: Earth "Clouds are painted", Venus "Surface hidden", Neptune "Dark spot of 1989, now gone", Vesta "Far north in shadow", Io "Small polar gaps", Callisto "Small gap near the south pole", Triton "Voyager 2 saw half", and the five Uranian moons "Only the south was seen". If a body's map fails to load, its note says it is showing the painted texture instead. The notes are defined in `index.html` next to the comment `one-line note on each object's card`.

## In the app

### The object card

Clicking an object, or finding it with *Find*, opens its card:

- its name and type, for example *Moon of Saturn · Norse group · retrograde irregular*;
- the [surface note](#card-notes), and for a moon outside its fitted range an *Estimated position* note ([Moon orbits](#moon-orbits));
- **From** the body held still: the distance, in kilometres below 20 million km and in AU above;
- **Light time:** how long light takes to cover that distance;
- **From the Sun**, **Radius** (with ≈ and *est.* for a [placeholder size](#what-is-not-to-scale)), **Rotation** (dwarf planets, asteroids, centaurs and comets: the spin period the app uses, in minutes, hours or days, or *illustrative* where none is published) and **Orbital period** (in hours, days or years; *retrograde* for moons that orbit backwards). Where a dwarf planet's, asteroid's or comet's radius or rotation period comes from a source other than the JPL SBDB, a **source** link after the value opens that paper or record ([which values](catalogue/small-bodies.md#notes-on-sizes-and-rotation));
- links: **Details** (its catalogue entry), **Rings** (for ringed bodies), **JPL** (its JPL Horizons record) or **JPL SBDB** (small bodies), and **NASA** (its NASA Science page, for 139 objects);
- a **Hold … still** button, which makes it the reference body.

On phones the card is shorter: it leaves out the type, the distance from the Sun, the radius, the rotation and the period.

Objects in the sky have their own card: deep-sky objects give their distance, constellation and apparent size; named stars their magnitude and spectral type; stars with planets their distance and number of planets; all three their position (RA and Dec). Constellations give their abbreviation, area, size rank and, for the zodiac, the dates the Sun passes through. Links go to the catalogue entry and SIMBAD, plus the NASA image or the NASA Exoplanet Archive where there is one. The card's **✕** goes back to the selected body.

### Trails

A trail is the path a body has followed **as seen from the body held still**. With the Sun held still, planets trace their orbits; with Earth held still, Mars traces its loops in the sky; and a moon's trail combines its orbit with its planet's path.

- **One slider per group** under *Trails*: planets (and the Sun, when another body is held still), major moons, minor moons, dwarf planets, candidates, asteroids & centaurs, and comets. Each runs from off (far left) through 1 week, 1 month, 3 months, 1 year, 5, 12, 30 and 100 years to 250 years. **Everything** sets them all at once, and reads *Mixed* when they differ. A group with nothing on screen says *None shown*; its slider still works.
- **Defaults:** 30 years for planets and small bodies, 1 year for major moons, off for minor moons.
- **`T`** turns all trails off, and back to the previous lengths.
- **When a trail is drawn:** only for bodies that are shown. A moon's trail appears only when its planet's moons are visible (see below), and is dropped when time runs so fast that the moon would go round more than 15 times a second.
- **Detail:** a trail is sampled about 180 times per orbit and keeps at most 6,000 points (2,000 for minor moons), so a long trail of a fast moon shows only its most recent part. Older parts fade out.

### When moons appear

A planet's moons (their dots, labels and trails) appear as you zoom toward the planet: once its moon system is a few dozen pixels across on screen. They also appear when the planet or one of its moons is selected or held still.

### Saved settings

The app remembers its settings on the device (in the browser's local storage): the body held still, the speed, trail lengths, labels, distance rings and moon orbit outlines, which moons, small bodies, belts and sky layers are shown (constellation options included), realistic surface textures, the sky map size and whether the menu is collapsed. The date is not saved: the app always opens at the current date and time.

## Accuracy

| Object type | Model | Typical accuracy |
|---|---|---|
| Planets | Standish Keplerian elements + secular rates | ~arc-minutes, 1800–2050 AD |
| The Moon | Mean elements (no periodic perturbations) | within a few degrees in longitude |
| Regular moons | One orbit fitted to JPL Horizons over 1800–2050 AD ([Moon orbits](#moon-orbits)) | Major moons within a fraction of a degree; small inner moons typically 1–3° |
| Irregular moons | Orbits fitted to JPL Horizons in windows of 2.5–10 years | Typically 1–2.5°, at most 3.6°; distance typically within 2% |
| Asteroids, dwarf planets | Two-body orbit from SBDB epoch | Very good near the epoch, slowly degrading away from it; planetary encounters are missed ([Error and drift over time](#error-and-drift-over-time)) |
| Comets | Two-body orbit from the SBDB solution for the latest perihelion | Good near perihelion; drifts faster than asteroids (Jupiter encounters, outgassing): after a pass by Jupiter, tens of degrees within a decade (67P about 60°, 9P/Tempel 1 up to 43°; a [known issue](#known-issues), measured in [Error and drift over time](#error-and-drift-over-time)) |
| Moons of dwarf planets and asteroids | Two-body orbit about the primary (JPL Horizons or published elements) | Orbit size and period good; phases drift; Selam's plane and Xiangliu's orientation are uncertain (a [limitation of the model](#limitations-of-the-model)) |

### Error and drift over time

Each orbit model is accurate in its best period and drifts away from it. Measured in November 2026 with the app's own code, against JPL Horizons positions every 10 days from 1800 to 2050 AD and the JPL [Small-Body Database close-approach data](https://ssd-api.jpl.nasa.gov/doc/cad.html); where a figure is taken from a source rather than measured, the table says so.

| Objects | Model | Best period | Error there | Away from it |
|---|---|---|---|---|
| Planets and Pluto | Standish Keplerian elements | 1800–2050 AD | about arc-minutes (JPL's figure) | grows; the time bar shows *Estimated positions* (not measured here) |
| The Moon | Mean elements | — | within a few degrees | no long-term drift measured |
| Planets' moons, one orbit (113) | Fitted to JPL Horizons ([Moon orbits](#moon-orbits)) | 1800–2050 AD | typically 1.5° (all fitted moons), distance 1.6% | within about 0.5° 150 years beyond (Io 0.06°, Titan 0.16°) |
| Planets' moons, time windows (345) | Fitted to JPL Horizons | 1800–2050 AD | as above | orbit size, shape and direction stay right; the position along the orbit is meaningless within a few decades |
| S/2025 U 1 | JPL mean elements, 2025 epoch | near 2025 | not measured | drifts |
| Moons of dwarf planets and asteroids | Two-body orbit about the primary | — | orbit size and period right | phases drift |
| Asteroids and dwarf planets | One two-body orbit, epoch 2026-Jun-09 | near 2026 | very good | slow drift, and planetary encounters are missed (below) |
| Comets | One two-body orbit from the latest perihelion | near that perihelion | good | faster drift; Jupiter encounters are missed (below) |

**Encounters that change an orbit, 1800–2050 AD.** Found from each small body's orbit history in JPL Horizons (a sudden change in its orbit, with a planet nearby), so they are ranked by their effect, not only by distance. A planet's *Hill sphere* is the region where its gravity outweighs the Sun's.

| Kind | Encounters |
|---|---|
| Strong flybys, well inside a planet's Hill sphere | **81P/Wild 2** passed Jupiter at 989,000 km on 10 Sep 1974 (period 49 → 6.1 yr, perihelion 4.96 → 1.47 AU); **67P/Churyumov-Gerasimenko** passed Jupiter at 7.7 million km on 4 Feb 1959 (period 9.0 → 6.5 yr, perihelion 2.74 → 1.28 AU, inclination 23° → 7°); **Apophis** passes Earth at 38,000 km on 13 Apr 2029 (period 0.886 → 1.159 yr) and the Moon at 96,000 km the next day |
| Distant passes by Jupiter that still change the orbit | **Hale-Bopp** at 0.77 AU on 5 Apr 1996 (period about 4,260 → 2,400 yr); **9P/Tempel 1** at 0.36–0.91 AU in 1870, 1881, 1941, 1953, 2024 and 2036 (each shifts its period by 0.3–0.7 yr; after 1881 it was lost until 1967); **67P** at 0.37–0.93 AU in 1840, 1876, 1923 and 2018 |
| Passes through the planetary region (the sum of many planets' pulls) | **NEOWISE** in 2020 (period 4,480 → 6,800 yr); **1P/Halley** in 1835, 1910 and 1986 (period 76.7 → 74.5 → 75.9 → 75.5 yr); **109P/Swift-Tuttle** in 1862 and 1992 (125 → 130 → 134 yr); **55P/Tempel-Tuttle** (about 0.4 yr per pass) |
| Weak passes by Earth (1.4–3 Hill radii; each changes the orbit by less than 0.5%) | Apophis 1823, 1866, 1907, 1998; Itokawa 1858, 1905, 2004; Bennu 1911, 1970, 1999; and Chiron passed Saturn at 1.9 AU in 1899 (about 1%) |
| None that matter | between two small bodies (the closest pair, Bennu and Itokawa, pass about 1.75 million km apart; even Vesta changes 67P's speed by only about 1 mm/s); the main-belt asteroids, Jupiter trojans, Kuiper belt objects, Sedna and Chariklo; and between planets or moons. A small body's pull on a planet is always negligible |

**How the app shows these encounters**, compared with JPL (closest distance from the planet's centre, and its time):

| Encounter | JPL | App | Difference |
|---|---|---|---|
| Apophis – Earth, 13 Apr 2029 | 37,998 km at 21:46 UTC | 194,303 km | 2.3 h late, five times too far |
| Apophis – Moon, 14 Apr 2029 | 95,743 km | 254,988 km | 14.7 h late |
| 81P/Wild 2 – Jupiter, 10 Sep 1974 | 988,842 km | 36 million km, in July 1975 | the flyby does not happen |
| 67P – Jupiter, 4 Feb 1959 | 7.7 million km | 288 million km | the flyby does not happen |
| 9P/Tempel 1 – Jupiter, 1941 | 62 million km | 132 million km | 23 days late |
| Bennu – Earth, 1999 / 1911 | 2.2 / 2.1 million km | 17 / 284 million km | 48 days late / no approach |
| Itokawa – Earth, 1905 | 1.7 million km | 7.9 million km | |
| Apophis – Earth, 1907 | 4.3 million km | 204 million km | no approach |
| 1P/Halley – Earth, 1910 | 22.7 million km | 23.8 million km | 25 days early |
| Hale-Bopp – Jupiter, 1996; 67P – Jupiter, 2018; 9P – Jupiter, 2024 | 115 / 56 / 82 million km | 117 / 59 / 84 million km | 2 / 7 / 3 days off: good |

**Small bodies from worst to best** (the app's perihelion times and positions compared with JPL Horizons):

*Not yet measured for the 17 small bodies added in Release 4.* On 2026-Nov-26 their positions agree with JPL Horizons within 0.01° for the asteroids, 0.04–1.4° for the Jupiter-family comets (26P/Grigg-Skjellerup is the furthest off, its SBDB orbit being from its 2013 perihelion) and 0.06° for C/1996 B2 (Hyakutake); their drift over 1800–2050 and the planetary encounters they miss are still to be measured.

- **9P/Tempel 1:** each Jupiter pass changes its orbit. Before about 1960 its position is essentially random (perihelion years off); after the 2024 pass it is 31–43° off by 2027–2028.
- **81P/Wild 2 before 1974 and 67P before 1959:** both are shown on the orbit they only got after their Jupiter flyby, so their positions are random (up to 180° off) and their perihelia years off. 67P drifts again after its 2018 pass: 18° off at the 2021 perihelion, about 60° near 2028.
- **Apophis:** good from about 1990 until April 2029, then it stays on its old orbit; in the 2030s it is on the other side of the Sun from its real position.
- **1P/Halley:** perihelion 1.6 years early in 1835, 40 days early in 1910, within a day in 1986. **2P/Encke:** 116 days early in 1803, right from about 2000. **Chiron:** years off in the 1800s, months before 2000. **55P and 109P:** about 1 and 3 years off before 1900, right since the 1960s. **Bennu and Itokawa:** weeks to months off before about 1990, after many small passes by Earth.
- **Eros, Didymos, Ryugu, Phaethon:** perihelia within about 2–24 days over the whole range. Phaethon and Ryugu can still look tens of degrees off near perihelion, where they move fastest.
- **Hale-Bopp and NEOWISE:** within a few degrees throughout; they are far out and slow for most of the period.

**Date range.** The app covers 1 January 1000 AD to 1 January 3000 AD (UTC, Gregorian calendar). Playing stops at either end, and a date entered outside the range is moved to the nearest end. **Outside 1800–2050 AD: positions are estimates.** That is the range in which the planets' elements are valid. Outside it the time bar turns amber and shows *Estimated positions* (next to the speed on wide screens, after the clock on phones); the further from that range, the larger the errors. The limits are `JD_MIN` and `JD_MAX` in `index.html`. Estimated positions outside 1800–2050 AD are a [limitation of the model](#limitations-of-the-model).

## Known issues

Things that are wrong compared with official NASA, JPL or IAU data. Every issue found in the November 2026 check of every value has been fixed, each checked against JPL Horizons, the IAU or the mission's own data before it replaced the old value. Deliberate simplifications and gaps in the published data are listed under [Limitations of the model](#limitations-of-the-model). Found since:

- **Small-body orbits drift, and miss planetary encounters.** Each asteroid, dwarf planet and comet follows one two-body orbit, fitted near 2026 (comets: at their latest perihelion), so the pulls of the planets are left out. Near that date the app matches JPL Horizons; away from it the error grows, and an encounter that changes an orbit does not happen in the app. For example, Apophis's Earth flyby on 13 April 2029 is shown at 194,000 km instead of 38,000 km and 2.3 hours late, and Apophis keeps its old orbit afterwards; Comet 81P/Wild 2's 1974 and 67P's 1959 flybys of Jupiter do not happen, so both are in the wrong place before them; 9P/Tempel 1 is far off before about 1960 and after its 2024 Jupiter pass. Every case, with measurements: [Error and drift over time](#error-and-drift-over-time).

## Limitations of the model

Simplifications kept on purpose. They are listed so you know what the app does and does not show.

- **Visual aids not to scale:** the fixed-size dots and labels, the Sun's glow, comet tails, exaggerated ring opacity and computer-generated lumpy shapes. Each is described in [What is not to scale](#what-is-not-to-scale).
- **Placeholders:** bodies with no published radius get a placeholder size, marked *est.*; eight small bodies with no published rotation period we could verify spin at an illustrative 12 hours ([details](catalogue/small-bodies.md#notes-on-sizes-and-rotation)).
- **Orbit models are simple, so precision depends on the date and the body** (see [Accuracy](#accuracy)):
  - planets and Pluto use Keplerian elements valid for 1800–2050 AD; outside that range the time bar shows *Estimated positions*;
  - the Moon uses mean elements without periodic terms, good to a few degrees;
  - small bodies use a single two-body orbit. Asteroids stay close for years, but comets drift faster, because Jupiter and their own outgassing change their orbits (in November 2026, 9P/Tempel 1 is about 6° off and 1P/Halley about 0.2 AU off). How far each one drifts, and the planetary encounters this misses, are a [known issue](#known-issues), measured in [Error and drift over time](#error-and-drift-over-time);
  - planetary moons are fitted to JPL Horizons over 1800–2050 AD; outside that range, and outside the shorter range Horizons covers for 24 of them, their positions are estimates, and S/2025 U 1, not yet in Horizons, uses JPL's mean elements ([Moon orbits](#moon-orbits));
  - seven irregular moons keep a visible bend in their path, and so in their trail, where two of their fitted time windows meet ([Moon orbits](#moon-orbits)). Neighbouring windows are blended, which removes the jumps and the sharp turns elsewhere, but these moons' windows disagree too much on the direction of motion for the blend to hide it. A 250-year trail held on the parent planet shows: Margaret (Uranus) about 22° in 2032; Psamathe (Neptune) about 9° in 1814; S/2023 S 18 (Saturn) about 9° in 2007; Neso (Neptune) about 8° in 2050; S/2020 S 38 (Saturn) about 7° in 2027; S/2023 S 33 (Saturn) about 6° in 1999. S/2023 S 38 (Saturn) also turns sharply, mostly for a real reason: its orbit is extremely elongated (eccentricity about 0.9), so it swings round Saturn at each closest approach. The positions themselves stay within these moons' usual accuracy;
  - moons of dwarf planets and asteroids use two-body orbits, so their positions drift slowly, and the published orbits of Selam and Xiangliu leave their orientation uncertain. Skamandrios's period is known to ±0.0003 days, so its phase may be up to about 30° off by 2026;
  - Patroclus is drawn at the SBDB orbit, which is the centre of mass of the Patroclus–Menoetius pair, and Menoetius is placed relative to it. Both are therefore about 150 km from their true positions (the pair is 692 km apart; Menoetius holds about 22% of the mass).
- **Objects left out:** moons without a verifiable published orbit, such as Makemake's moon, Ida's moon Dactyl and Polymele's moon Shaun, and others listed in [What's not included](#whats-not-included). The main asteroid belt, Hildas, Jupiter and Neptune trojans and Kuiper belt are statistical clouds, not catalogued objects ([Belts](#belts)).
- **Surfaces:** bodies with no spacecraft map get a painted texture, and Earth gets painted clouds. Some maps have gaps or filler from their sources: Solar System Scope fills gaps with invented terrain; Voyager 2 saw only part of Uranus's moons and Triton, and the app paints the rest (and Callisto's small unmapped area); about a third of Deimos's map and parts of Europa's and Ganymede's are filler from their map makers; cloud maps (Venus, the giant planets) are snapshots, and Neptune's shows a dark spot that is now gone. See [Surface maps](#surface-maps).
- **One fixed rotation period per body:** comets' spins change at each pass near the Sun. 67P/Churyumov-Gerasimenko spins at its IAU 2015 rate (12.4043 h), while its most recent measured period is 12.055 h (2016), so its spin is only approximate at most dates ([details](catalogue/small-bodies.md#notes-on-sizes-and-rotation)).
- **Random spin axes for twenty-five small bodies:** those with no published pole the app can use, listed under [Dwarf planets, candidates, asteroids, centaurs and comets](#dwarf-planets-candidates-asteroids-centaurs-and-comets-55-plus-pluto). Their spin axes are random, for display only.
- **Which side faces you is not set for every body:** Vesta and bodies without IAU rotational elements spin from an arbitrary starting angle, and tidally locked moons face their planet within a few degrees (Mimas within about 20°); see [Which side faces you](#which-side-faces-you).
- **One shared pole:** Uranus's five moons use Uranus's pole; their own IAU poles differ by about 0.1°.
- **Fixed spin poles for Triton and Iapetus:** both use their IAU 2015 pole at J2000, although the real poles move. Triton's circles Neptune's pole about every 690 years, so the app's axis is about 5° off in 2026 and up to about 46° off at the ends of the time bar (1000 and 3000). Iapetus's drifts more slowly: about 0.4° off in 2026, 12° in 1000 and 17° in 3000. See [Orientation](#orientation).
- **The sky:** star proper motion and precession are not modelled, and the sky is drawn as a backdrop at infinite distance, so its directions are true but distances are not shown ([The sky](#the-sky-beyond-the-solar-system)).

This is an educational model. For precise ephemerides, query [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/), which uses full numerical integrations (DE440 and satellite ephemerides).

## Further reading on reference frames

- Galileo Galilei (1632), *Dialogue Concerning the Two Chief World Systems*, Second Day (the ship thought experiment, the origin of Galilean relativity).
- NASA Science, *Solar System overview*: <https://science.nasa.gov/solar-system/>
- JPL, *Basics of Space Flight*, Chapter 2 "Reference Systems": <https://science.nasa.gov/learn/basics-of-space-flight/chapter2-1/>
