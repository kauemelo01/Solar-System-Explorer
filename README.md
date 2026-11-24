# Solar System Explorer

**An interactive 3D orrery where *any* body in the solar system can be the centre.**

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

## What is an orrery model?

An **orrery** is a working model of the solar system that shows the planets and moons moving around their orbits at their relative speeds. The first ones were clockwork machines: the name comes from Charles Boyle, 4th Earl of Orrery, for whom an early example was built around 1713, after a design by George Graham and Thomas Tompion. Turn a crank and gears carry each planet around the Sun, so a year of motion can play out in seconds. The much older Greek Antikythera mechanism (2nd–1st century BC) used gears for similar astronomical predictions.

Mechanical orreries have two built-in limits. They are almost never to scale, because true distances and sizes would make the planets invisible specks, and their gears fix the Sun at the centre. A digital orrery removes both: positions are computed from real orbital elements for any date, distances and sizes stay true to scale (you zoom in instead of shrinking the solar system), and nothing stops you from moving the centre. Solar System Explorer is that kind of orrery.

## What's inside

- **494 real objects**, each with orbital elements from NASA/JPL:
  - the Sun, 8 planets, the Moon and Pluto
  - **459 natural satellites** (status as of November 2026): Mars 2 · Jupiter 115 · Saturn 292 · Uranus 29 · Neptune 16 · Pluto 5
  - 8 dwarf planets and candidates, 12 asteroids and centaurs, 4 comets
- **Real-time positions** computed from JPL Keplerian and mean orbital elements, for any date (forward or backward in time)
- **Always true to scale**: real distances and real body sizes, with orbit trails of adjustable length and distance rings in AU
- Moon families (Galilean, Himalia, Carme, Pasiphae, Norse, Inuit, Gallic…) that you can switch on one group at a time
- Statistical belts (main asteroid belt, Jupiter trojans, Kuiper belt) to show where those populations live
- **The real sky behind it all**:
  - 9,096 stars from the Yale Bright Star Catalogue
  - NASA's all-sky star map (Milky Way and faint stars), up to 8192 × 4096
  - 29 nebulae, clusters, galaxies and deep fields, such as the Pleiades, the Orion Nebula, Andromeda, the Pillars of Creation and the Hubble and Webb deep fields
  - 29 named bright stars and 5 stars with known planets (including Proxima Centauri and TRAPPIST-1)
  - the **88 IAU constellations** (off by default): official boundaries, stick figures and names, with a **Zodiac** filter showing the 13 constellations the Sun actually passes through, Ophiuchus included

  Everything is at its true position. Change the centre from Earth to Neptune and the sky does not move: the stars are that far away.
- **Real surface maps** where spacecraft have mapped a body: the Sun, the planets, the Moon, Saturn's rings, Ceres, Vesta and 18 major moons, from Solar System Scope, NASA, NASA/JPL and DLR. Large versions load on capable screens. Everything else gets a simple painted texture, and Earth gets painted clouds so the cloud-free map looks natural. **Each object's card says whether its surface is real photos, a partial map or a painted illustration**, and the *Images* panel can switch all maps off (see [Surface maps](docs/sources.md#surface-maps))
- **Fullscreen mode** for classrooms and presentations: hides the menu, cards and time bar, leaving only the sky and the solar system
- Runs fully in the browser: `index.html` with [three.js](https://threejs.org/), plus the sky data in [`sky/`](sky/) and the surface maps in [`textures/`](textures/). No build step; any static web host (such as GitHub Pages) can serve it

### Controls

| Action | How |
|---|---|
| Rotate / zoom | Drag; scroll or pinch |
| Fly to an object | Click its name, or use **Find** (`/`) |
| Show constellations | *Beyond the solar system → Constellations (IAU)*; choose **All 88** or **Zodiac (13)**, figures and boundaries |
| Look at a star, nebula or galaxy | Click its label to open its card, or type its name in **Find** to turn the view towards it |
| **Make an object the centre** | Double-click it, pick it under *Hold still*, or press **C** for the selected one |
| Pause / speed / reverse | `Space` · `←` `→` · `R` |
| Toggle trails | `T` |
| Realistic or painted surfaces | *Images → Realistic surface textures*. Off: every body uses its painted texture, the surface notes on the cards are hidden, and no map files are downloaded |
| Sky map detail | *Images → Sky map detail*: **Auto** (8K on large screens, otherwise 4K), **4K** or **8K** (disabled on devices whose graphics cannot show 8K textures) |
| Fold or unfold a menu section | Click the section's heading |
| Collapse / expand the menu | The arrow button at the top of the menu (on phones: **Controls**) |
| Fullscreen mode (hides menus, cards and the time bar) | The corner-arrows button at the top of the menu, or `F`; exit with `Esc`, `F` or the **Exit fullscreen** button |

On screens at least 1240 px wide, the menu runs the full height of the window and the time bar narrows to stay centred beside it. On smaller screens the menu stops above the time bar; on phones the menu, cards and time bar stack.

## Data provenance

Everything in the app traces back to public, citable sources, mostly from NASA's Jet Propulsion Laboratory:

| Data | Source |
|---|---|
| Planet orbits | JPL SSD, [*Approximate Positions of the Planets*](https://ssd.jpl.nasa.gov/planets/approx_pos.html) (Standish; best 1800–2050) |
| Moon orbits | JPL SSD, [*Planetary Satellite Mean Elements*](https://ssd.jpl.nasa.gov/sats/elem/) |
| Moon sizes | JPL SSD, [*Planetary Satellite Physical Parameters*](https://ssd.jpl.nasa.gov/sats/phys_par/) |
| Asteroids, dwarf planets, comets | [JPL Small-Body Database](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html) |
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
| Surface maps: 17 other major moons | [NASA 3D Resources](https://github.com/nasa/NASA-3D-Resources), old Voyager and Viking mosaics. **Several are partial or gap-filled**; each object's card says so, and [the per-map list](docs/sources.md#every-map-with-its-coverage) has the details |

**Every object has its own reference entry.** The catalogue lists each body with the values the app uses and links to its JPL Horizons or SBDB record, plus its NASA Science page where one exists:

- [Sun, planets, the Moon and Pluto](docs/catalogue/sun-planets.md) (11)
- [Dwarf planets, asteroids, centaurs and comets](docs/catalogue/small-bodies.md) (24)
- [Moons of Mars](docs/catalogue/moons-mars.md) (2)
- [Moons of Jupiter](docs/catalogue/moons-jupiter.md) (115)
- [Moons of Saturn](docs/catalogue/moons-saturn.md) (292)
- [Moons of Uranus](docs/catalogue/moons-uranus.md) (29)
- [Moons of Neptune](docs/catalogue/moons-neptune.md) (16)
- [Moons of Pluto](docs/catalogue/moons-pluto.md) (5)
- [The sky beyond the solar system](docs/catalogue/sky.md): stars, the Milky Way, deep-sky objects and planet-hosting stars (63 named objects)
- [The 88 constellations](docs/catalogue/constellations.md), with the 13 of the zodiac and the dates the Sun passes through them

The full methodology, accuracy notes and bibliography are in [docs/sources.md](docs/sources.md).

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
| `tools/build_textures.py` | Rebuilds `textures/` from the original sources (downloads them; needs Pillow) |
| `docs/` | Documentation and the per-object catalogue |
| `icon.svg`, `favicon-32.png`, `apple-touch-icon.png` | App icon (browser tab and home-screen versions): an orbit, the Sun, and a planet with its own moon |
| `social-card.png` | Preview image shown when the link is shared (Open Graph / Twitter card) |
| `_config.yml`, `sitemap.xml` | Search-engine setup for GitHub Pages: page titles and descriptions, and the list of pages for Google Search Console |
| `LICENSE` | GNU General Public License v3 |

## Accuracy and limits

This is an educational model built on mean and osculating Keplerian elements, not a full n-body integration. Planet positions are good to roughly arc-minutes within 1800–2050. The time bar covers **1 January 1000 AD to 1 January 3000 AD**: playing stops at either end, and dates typed outside that range are moved to the nearest end. Outside 1800–2050 the date is marked *approximate*. Small-body positions drift slowly away from their element epoch. Moon positions follow mean elements, which do not include short-period perturbations. For mission-grade ephemerides, use [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) directly. See [docs/sources.md](docs/sources.md#accuracy) for details.

Distances and body sizes are always to true scale. A few visual aids are not. Each is described in [docs/sources.md](docs/sources.md#what-is-not-to-scale):
- the fixed-size dots and labels that mark each body;
- the Sun's glow;
- comet tails;
- placeholder sizes for moons with no published radius;
- computer-generated shapes for irregular bodies;
- the statistical belts;
- the sky backdrop, whose directions are true but whose distances are not drawn.

## Contributing

New moons are announced every year. To add or update an object, open an issue or pull request that cites its JPL Horizons/SBDB record or its Minor Planet Electronic Circular, and update the matching page in [`docs/catalogue/`](docs/catalogue/).

## License

The code is released under the [GNU General Public License v3](LICENSE). Data and images keep the terms of their sources (NASA, JPL, CDS, the IAU and the papers cited), listed in [docs/sources.md](docs/sources.md).
