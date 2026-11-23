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

## What's inside

- **494 real objects**, each with orbital elements from NASA/JPL:
  - the Sun, 8 planets, the Moon and Pluto
  - **459 natural satellites** (status as of November 2026): Mars 2 · Jupiter 115 · Saturn 292 · Uranus 29 · Neptune 16 · Pluto 5
  - 8 dwarf planets and candidates, 12 asteroids and centaurs, 4 comets
- **Real-time positions** computed from JPL Keplerian and mean orbital elements, for any date (forward or backward in time)
- **True scale** or magnified body sizes, orbit trails of adjustable length, distance rings in AU
- Moon families (Galilean, Himalia, Carme, Pasiphae, Norse, Inuit, Gallic…) that you can switch on one group at a time
- Statistical belts (main asteroid belt, Jupiter trojans, Kuiper belt) to show where those populations live
- Runs fully in the browser: a single `index.html` with [three.js](https://threejs.org/), no build step and no server

### Controls

| Action | How |
|---|---|
| Rotate / zoom | Drag; scroll or pinch |
| Fly to an object | Click its name, or use **Find** (`/`) |
| **Make an object the centre** | Double-click it, pick it under *Hold still*, or press **C** for the selected one |
| Pause / speed / reverse | `Space` · `←` `→` · `R` |
| Toggle trails | `T` |

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

**Every object has its own reference entry.** The catalogue lists each body with the values the app uses and links to its JPL Horizons or SBDB record, plus its NASA Science page where one exists:

- [Sun, planets, the Moon and Pluto](docs/catalogue/sun-planets.md) (11)
- [Dwarf planets, asteroids, centaurs and comets](docs/catalogue/small-bodies.md) (24)
- [Moons of Mars](docs/catalogue/moons-mars.md) (2)
- [Moons of Jupiter](docs/catalogue/moons-jupiter.md) (115)
- [Moons of Saturn](docs/catalogue/moons-saturn.md) (292)
- [Moons of Uranus](docs/catalogue/moons-uranus.md) (29)
- [Moons of Neptune](docs/catalogue/moons-neptune.md) (16)
- [Moons of Pluto](docs/catalogue/moons-pluto.md) (5)

The full methodology, accuracy notes and bibliography are in [docs/sources.md](docs/sources.md).

## Running locally

```bash
git clone https://github.com/kauemelo01/Solar-System-Explorer.git
cd Solar-System-Explorer
python3 -m http.server 8000   # or just open index.html in a browser
```

## Accuracy and limits

This is an educational model built on mean and osculating Keplerian elements, not a full n-body integration. Planet positions are good to roughly arc-minutes within 1800–2050. Small-body positions drift slowly away from their element epoch. Moon positions follow mean elements, which do not include short-period perturbations. For mission-grade ephemerides, use [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) directly. See [docs/sources.md](docs/sources.md#accuracy) for details.

## Contributing

New moons are announced every year. To add or update an object, open an issue or pull request that cites its JPL Horizons/SBDB record or its Minor Planet Electronic Circular, and update the matching page in [`docs/catalogue/`](docs/catalogue/).
