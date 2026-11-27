# Solar System Explorer

**An interactive 3D orrery where *any* body in the solar system can be the centre.**

> [!IMPORTANT]
> **WORK IN PROGRESS.** The app and its documentation are still being improved. Every position is checked against JPL Horizons, and the [accuracy targets](docs/sources.md#accuracy-targets) say what counts as right; what is measured meets them from 1800 to 2050 AD, and what is not yet measured, or simplified on purpose, is listed under [Limitations](docs/sources.md#limitations-of-the-model).

▶ **Live app:** <https://kauemelo01.github.io/Solar-System-Explorer/>

📚 **Documentation and object catalogue:** [docs/](docs/README.md)

---

## Why this exists: the Sun-centred view is a model

We usually draw the solar system with the Sun fixed in the middle and everything circling around it. That picture is useful, but it is a **choice of reference frame**, not a fact about where the "true centre" is.

Galileo made the point with his ship thought experiment (*Dialogue Concerning the Two Chief World Systems*, 1632): shut inside a cabin on a smoothly sailing ship, you can't run any experiment that tells you whether the ship is moving or standing still. There is no **absolute** frame of rest. Motion only means something *relative to* something else. Newton built his mechanics on this, and Einstein took it further.

So for describing positions and motions, the question "what orbits what?" has no single right answer:

- **Seen from the Sun**, Mars traces a near-ellipse.
- **Seen from the Earth**, the same Mars drifts across the sky, stops, goes backward (*retrograde motion*) and loops. Ptolemy's epicycles were built to describe exactly these loops.
- **Seen from Jupiter**, the Sun itself traces a 12-year circle, and the inner planets wind tight spirals around it.

The motion of each body is the same in every case; only the vantage point changes. The heliocentric frame is popular because it makes the motions *simplest*. It is not the only one that is *correct*. (A frame centred on a planet does involve accelerations, so its "physics" includes fictitious forces. That is exactly why the Sun-centred frame, nearly inertial, is the convenient default, and why it stays a convenience.)

**Solar System Explorer makes this something you can see.** Pick any object (the Sun, the Earth, the Moon, Io, a comet, a tiny irregular moon of Saturn) and hold it still. Everything else then moves relative to it, and the orbit trails redraw in that frame. Students can watch retrograde loops appear when Earth is held still, see the Moon's "orbit" around the Sun as a gently wavy line, or see what the sky would look like from Titan.

## What is an orrery?

An **orrery** is a working model of the solar system that shows the planets and moons moving around their orbits at their relative speeds. The first ones were clockwork machines: the name comes from Charles Boyle, 4th Earl of Orrery, for whom an early example was built around 1713, after a design by George Graham and Thomas Tompion. Turn a crank and gears carry each planet around the Sun, so a year of motion can play out in seconds. The much older Greek Antikythera mechanism (2nd–1st century BC) used gears for similar astronomical predictions.

Mechanical orreries have two built-in limits. They are almost never to scale, because true distances and sizes would make the planets invisible specks, and their gears fix the Sun at the centre. A digital orrery removes both: positions are computed from real orbital elements for any date, distances and sizes stay true to scale (you zoom in instead of shrinking the solar system), and nothing stops you from moving the centre. Solar System Explorer is that kind of orrery.

## What's inside

- **544 real objects**, each with orbital elements from NASA/JPL or peer-reviewed orbit papers:
  - the Sun, 8 planets and the Moon
  - **469 natural satellites** (status as of November 2026): Mars 2 · Jupiter 115 · Saturn 292 · Uranus 29 · Neptune 16 · Pluto 5 · other dwarf planets and candidates 6 (Dysnomia, Hiʻiaka, Namaka, Weywot, Vanth, Xiangliu) · asteroids 4 (Dimorphos, Skamandrios, Queta, Menoetius)
  - 5 dwarf planets (Pluto among them) and 4 dwarf planet candidates, 35 asteroids, centaurs and Kuiper belt objects, 21 comets
- **7 ring systems** at their true radii: Jupiter, Saturn, Uranus, Neptune, Haumea, Quaoar and Chariklo
- **Real-time positions** for any date from 1000 to 3000 AD (forward or backward in time): planets from Standish and Williams's Keplerian elements (JPL SSD), the Moon from a lunar theory, and the other moons, dwarf planets, asteroids and comets from orbits fitted to JPL Horizons (or published orbits); outside 1800–2050 AD positions are estimates
- **Always true to scale**: real distances and real body sizes, with orbit trails of adjustable length and distance rings in AU
- Statistical belts (main asteroid belt, Hilda asteroids, Jupiter trojans, Neptune trojans, Kuiper belt) to show where those populations live; the Hildas form the triangle that turns with Jupiter
- **What is and is not included, and why:** [What's included](docs/sources.md#whats-included), [What's not included](docs/sources.md#whats-not-included), and the [Watchlist](docs/sources.md#watchlist) of objects waiting for published data
- **The real sky behind it all**:
  - 9,096 stars from the Yale Bright Star Catalogue
  - NASA's all-sky star map (Milky Way and faint stars), up to 8192 × 4096
  - 29 nebulae, clusters, galaxies and deep fields, such as the Pleiades, the Orion Nebula, Andromeda, the Pillars of Creation and the Hubble and Webb deep fields
  - 30 named bright stars and 5 stars with known planets (including Proxima Centauri and TRAPPIST-1)
  - the **88 IAU constellations** (off by default): official boundaries, stick figures and names, with a **Zodiac** filter showing the 13 constellations the Sun actually passes through, Ophiuchus included

  Everything is at its true position. Change the centre from Earth to Neptune and the sky does not move: the stars are that far away.
- **Real surface maps** where spacecraft have mapped a body: the Sun, the planets, the Moon, Saturn's rings, Ceres, Vesta and 18 major moons, from Solar System Scope, NASA, NASA/JPL, USGS and DLR. Large versions load on capable screens. Everything else gets a simple painted texture, and Earth gets painted clouds so the cloud-free map looks natural. **Each object's card says whether its surface is real photos, a partial map or a painted illustration**, and the *Images* panel can switch all maps off (see [Surface maps](docs/sources.md#surface-maps))
- **An interface built for exploring**: a menu to choose the body held still and what is shown (moons by family, small bodies, belts, sky layers), a time bar from 1000 to 3000 AD, trails of adjustable length, cards with each object's data and sources, a camera position card and a fullscreen mode for classrooms ([the interface](docs/interface.md))
- Runs fully in the browser: `index.html` with [three.js](https://threejs.org/), plus the sky data in [`sky/`](sky/) and the surface maps in [`textures/`](textures/). No build step; any static web host (such as GitHub Pages) can serve it

### Controls

Drag to rotate, scroll or pinch to zoom, click a name to fly to it, and double-click an object to hold it still. `Space` pauses, `←` `→` change the speed and `R` reverses time; `/` opens **Find**. The menu, the time bar, the cards, trails, every keyboard shortcut and the settings the app remembers are described in **[the interface](docs/interface.md)**.

## Data provenance

Everything in the app traces back to public, citable sources, mostly from NASA's Jet Propulsion Laboratory:

| Data | Source |
|---|---|
| Planet orbits | Standish and Williams, [Keplerian elements](https://ssd.jpl.nasa.gov/planets/approx_pos.html) (JPL SSD): Table 1 over 1800–2050 AD, Tables 2a and 2b outside |
| Moon orbits | Positions: orbits fitted to [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) over 1800–2050 AD ([`data/moon-orbits.js`](data/moon-orbits.js); [method and accuracy](docs/sources.md#moon-orbits)). Orbit shapes listed in the catalogue: JPL SSD, [*Planetary Satellite Mean Elements*](https://ssd.jpl.nasa.gov/sats/elem/) |
| Moon sizes | JPL SSD, [*Planetary Satellite Physical Parameters*](https://ssd.jpl.nasa.gov/sats/phys_par/), then each moon's JPL Horizons record, then NASA Science pages and published surveys ([which source for each moon](docs/sources.md#moon-sizes)) |
| Asteroids, dwarf planets, comets | Positions: orbits fitted to [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) over 1800–2050 AD ([`data/sb-orbits.js`](data/sb-orbits.js); [method and accuracy](docs/sources.md#small-body-orbits)). Orbital elements, sizes and rotation listed in the catalogue: [JPL Small-Body Database](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html) |
| Moons of dwarf planets and asteroids | Orbits fitted to [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) satellite solutions, and for Haumea's moons to the ephemeris of Proudfoot et al. (2024); published orbits: Kiss et al. (2019), Marchis et al. (2014), Brown et al. (2021), Brozović et al. (2024) ([method and accuracy](docs/sources.md#moons-of-dwarf-planets-and-asteroids-10)) |
| Ring systems | NASA NSSDCA ring fact sheets; occultation studies (Ortiz et al. 2017, Morgado et al. and Pereira et al. 2023, Braga-Ribas et al. 2014) |
| Planet radii, rotation, poles | [NASA NSSDCA fact sheets](https://nssdc.gsfc.nasa.gov/planetary/planetfact.html); IAU WGCCRE 2015 report ([Archinal et al. 2018](https://doi.org/10.1007/s10569-017-9805-5)) |
| Object identifiers | NAIF / JPL SPK IDs, checked against [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) |
| Stars | *Yale Bright Star Catalogue*, 5th ed., via [NASA HEASARC](https://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html) |
| Milky Way and faint stars | NASA/Goddard SVS, [*Deep Star Maps*](https://svs.gsfc.nasa.gov/3895) (2009) |
| Deep-sky reference images (linked) | [NASA Image and Video Library](https://images.nasa.gov/) |
| Deep-sky positions | CDS SIMBAD / Sesame |
| Stars with planets | [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) |
| Constellation boundaries | IAU (Delporte 1930), via CDS catalogues VI/42 (Roman 1987) and VI/49 (Davenhall & Leggett 1989) |
| Constellation figures | NASA/Goddard SVS, [*Deep Star Maps*](https://svs.gsfc.nasa.gov/3895) (figures after Sky & Telescope for the IAU) |
| Surface maps: Sun, planets, the Moon, Saturn's rings | [Solar System Scope](https://www.solarsystemscope.com/textures/) (CC BY 4.0), based on NASA mission data, with gaps filled by the publisher |
| Surface maps: Ceres, Vesta | Dawn mosaics by [DLR](https://dawngis.dlr.de/) (NASA/JPL-Caltech/UCLA/MPS/DLR/IDA) |
| Surface map: Triton | NASA/JPL [PIA18668](https://www.jpl.nasa.gov/images/pia18668-map-of-triton/) (Paul Schenk, LPI), from Voyager 2 |
| Surface maps: Saturn's icy moons | NASA/JPL [PIA18434–PIA18439](https://photojournal.jpl.nasa.gov/catalog/PIA18437) (Paul Schenk, LPI), global maps from Cassini, shown in black-and-white |
| Surface map: Callisto | [USGS Astrogeology](https://planetarymaps.usgs.gov/mosaic/Callisto_Voyager_GalileoSSI_global_mosaic_1km.tif) Voyager/Galileo global mosaic |
| Surface maps: 10 other major moons | [NASA 3D Resources](https://github.com/nasa/NASA-3D-Resources), old Voyager and Viking mosaics. **Several are partial or gap-filled**; each object's card says so, and [the per-map list](docs/sources.md#every-map-with-its-coverage) has the details |

**Every object has its own reference entry.** The catalogue lists each body with the values the app uses and links to its JPL Horizons or SBDB record, plus its NASA Science page where one exists:

- [Sun, planets and the Moon](docs/catalogue/sun-planets.md) (10)
- [Dwarf planets, asteroids, centaurs and comets](docs/catalogue/small-bodies.md) (65)
- [Moons of Mars](docs/catalogue/moons-mars.md) (2)
- [Moons of Jupiter](docs/catalogue/moons-jupiter.md) (115)
- [Moons of Saturn](docs/catalogue/moons-saturn.md) (292)
- [Moons of Uranus](docs/catalogue/moons-uranus.md) (29)
- [Moons of Neptune](docs/catalogue/moons-neptune.md) (16)
- [Moons of Pluto](docs/catalogue/moons-pluto.md) (5)
- [Moons of dwarf planets and asteroids](docs/catalogue/moons-small-bodies.md) (10)
- [Ring systems](docs/catalogue/rings.md) (7)
- [The sky beyond the solar system](docs/catalogue/sky.md): stars, the Milky Way, deep-sky objects and planet-hosting stars (64 named objects)
- [The 88 constellations](docs/catalogue/constellations.md), with the 13 of the zodiac and the dates the Sun passes through them

The full methodology, accuracy notes and bibliography are in [Sources, methodology and accuracy](docs/sources.md).

## Running locally

```bash
git clone https://github.com/kauemelo01/Solar-System-Explorer.git
cd Solar-System-Explorer
python3 -m http.server 8000   # then open http://localhost:8000
```

Opening `index.html` directly from disk works, but browsers block the sky map and surface maps over `file://` (bodies then use their simpler painted textures), so use a local server to see them.

## Project files

| Path | What it is |
|---|---|
| `index.html` | The whole app: page, styles and code |
| `sky/` | Sky data: star catalogue, NASA star maps, deep-sky objects, constellation boundaries and figures |
| `textures/` | Surface maps for the Sun, planets, Saturn's rings, Ceres, Vesta and the major moons ([sources](docs/sources.md#surface-maps)) |
| `data/moon-orbits.js` | The planets' moon orbits fitted to JPL Horizons over 1800–2050 AD ([method](docs/sources.md#moon-orbits)) |
| `data/sb-orbits.js` | The orbits of 56 dwarf planets, asteroids and comets fitted to JPL Horizons over 1800–2050 AD ([method](docs/sources.md#small-body-orbits)) |
| `tools/build_textures.py` | Rebuilds `textures/` from the original sources (downloads them; needs Pillow) |
| `tools/planet-checks/` | Measures the planets against JPL Horizons ([how to run](tools/planet-checks/README.md)) |
| `tools/moon-orbit-fits/` | Rebuilds `data/moon-orbits.js` from JPL Horizons and checks it ([how to run](tools/moon-orbit-fits/README.md)) |
| `tools/small-body-orbit-fits/` | Rebuilds `data/sb-orbits.js` from JPL Horizons and checks it ([how to run](tools/small-body-orbit-fits/README.md)) |
| `docs/` | Documentation and the per-object catalogue |
| `icon.svg`, `favicon-32.png`, `apple-touch-icon.png` | App icon (browser tab and home-screen versions): an orbit, the Sun, and a planet with its own moon |
| `social-card.png` | Preview image shown when the link is shared (Open Graph / Twitter card) |
| `_config.yml`, `sitemap.xml` | Search-engine setup for GitHub Pages: page titles and descriptions, and the list of pages for Google Search Console |
| `google93f522f8da0be4f0.html` | Site ownership check for Google Search Console |
| `LICENSE` | GNU General Public License v3 |

## Accuracy and limits

This is an educational model built on Keplerian orbits, not a full n-body integration: the planets use Standish and Williams's Keplerian elements (JPL SSD), and the moons, dwarf planets, asteroids and comets use orbits fitted to JPL Horizons over 1800–2050 AD, which meet the [accuracy targets](docs/sources.md#accuracy-targets). Planet positions are within 12.3′ of JPL Horizons over 1800–2050 AD and within 0.5° from 1000 to 3000 AD. The time bar covers **1000 to 3000 AD** ([the time bar](docs/interface.md#the-time-bar)); outside 1800–2050 AD positions are estimates. Known issues: none at the moment ([Known issues](docs/sources.md#known-issues)).

Distances and body sizes are always to true scale. A few visual aids are not; they are among the [limitations of the model](docs/sources.md#limitations-of-the-model), and each is described under [What is not to scale](docs/interface.md#what-is-not-to-scale):
- the fixed-size dots and labels that mark each body;
- the Sun's glow;
- comet tails;
- placeholder sizes for moons and small bodies with no published radius;
- exaggerated ring opacity (ring radii are true);
- computer-generated shapes for irregular bodies;
- the statistical belts;
- the sky backdrop, whose directions are true but whose distances are not drawn.

## Contributing

New moons are announced every year; the rules for adding objects are in [What's included](docs/sources.md#whats-included). To add or update an object, open an issue or pull request that cites its JPL Horizons/SBDB record or its Minor Planet Electronic Circular, and update the matching page in [`docs/catalogue/`](docs/catalogue/).

## Releases

- **Release 4** (in progress, branch `wip-release-4`):
  - **One inclusion rule for every object**: a defined group, and an orbit published by JPL, the IAU or a mission team ([What's included](docs/sources.md#whats-included), [What's not included](docs/sources.md#whats-not-included) and a [Watchlist](docs/sources.md#watchlist) of objects waiting for data). Under it, 26 more small bodies (spacecraft targets such as Gaspra, Toutatis and the Lucy trojans, parents of the major meteor showers, and the great comet Hyakutake), the asteroid moons Skamandrios, Queta and Menoetius, and the Hilda and Neptune trojan belts; Selam moves to the Watchlist, since only its distance and period are published (544 objects).
  - **Written [accuracy targets](docs/sources.md#accuracy-targets)** (within 1° or 1 day of JPL Horizons; close planetary encounters within 3 hours), and orbits that meet them:
    - 56 dwarf planets, asteroids and comets fitted to JPL Horizons over 1800–2050 AD, so every close planetary encounter of the period happens (Apophis passes the Earth on 13 April 2029 at 38,026 km, against JPL's 38,011);
    - the moons of dwarf planets and asteroids fitted to JPL Horizons or to Proudfoot et al. (2024): Dimorphos before and after NASA's DART impact, and Haumea's moons, pole and ring in the right plane;
    - the Moon from a lunar theory (Meeus), within 0.02° instead of up to 5°;
    - the planets and Pluto from Standish and Williams's Table 2 outside 1800–2050 AD (Table 1 inside, unchanged), within 0.5° of JPL Horizons from 1000 to 3000 AD instead of up to 5.5° (Saturn).
  - **Better data**: each small body's size and rotation from its most recent published measurement (Arrokoth measured by New Horizons, Torifune by Hayabusa2), published sizes for 354 more moons (10 still have none), the Jupiter trojans back at L4 and L5, and 9P/Tempel 1 turned to its real prime meridian.
  - **Interface**: a start-up screen that turns into an error message if the app cannot start, a camera position card, smooth trails around perihelion, and *source* links on the object card for any value not from NASA or JPL ([the interface](docs/interface.md)).
- **Release 3** (current, branch `main`, tag `v3`):
  - The planets' moons placed by orbits fitted to JPL Horizons over 1800–2050 AD: typically within 1.5°, against about 90° before.
  - A time bar from 1000 to 3000 AD, with an *Estimated positions* alert outside 1800–2050 AD; a trail length slider for each group of bodies.
  - Published spin axes and rotation periods, and the Sun, the planets, the Moon and 58 other bodies turned so the side facing you is the real one.
  - Every published moon radius, from JPL or a cited publication; Cassini maps of Saturn's six icy moons and a new Callisto map.
  - Documentation checked against the app, with *What's included*, *What's not included*, and how each orbit model's error grows over time.
- **Release 2** (tag `v2`, branch `release-2`): real spacecraft surface maps, Earth's clouds, the moons menu grouped by parent body, 22 more bodies and 7 ring systems, the *Images* panel, data corrected against NASA/JPL/IAU, and the documentation's *Known issues* and *Limitations* lists. To view it: `git switch release-2`.
- **Release 1** (tag `v1`, branch `release-1`): the first published version, kept unchanged. To view it: `git switch release-1`. To make it the published app again, point `main` back to it: `git push --force origin refs/heads/release-1:refs/heads/main` (GitHub Pages publishes `main`). The `release-1` branch is locked on GitHub so it cannot change.

## License

The code is released under the [GNU General Public License v3](LICENSE). Data and images keep the terms of their sources (NASA, JPL, CDS, the IAU and the papers cited), listed in [Sources, methodology and accuracy](docs/sources.md).
