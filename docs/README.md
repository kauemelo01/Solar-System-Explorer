[← Project README](https://github.com/kauemelo01/Solar-System-Explorer#readme) · [Open the app](https://kauemelo01.github.io/Solar-System-Explorer/)

# Solar System Explorer: documentation

This folder documents **every object** in Solar System Explorer: the values the app uses and the public NASA/JPL record each value comes from.

## Object catalogue (494 solar-system objects + the sky)

| Page | Objects | Primary reference |
|---|---:|---|
| [Sun, planets, the Moon and Pluto](catalogue/sun-planets.md) | 11 | JPL Keplerian elements · NASA fact sheets |
| [Dwarf planets, asteroids, centaurs and comets](catalogue/small-bodies.md) | 24 | JPL Small-Body Database |
| [Moons of Mars](catalogue/moons-mars.md) | 2 | JPL satellite mean elements |
| [Moons of Jupiter](catalogue/moons-jupiter.md) | 115 | JPL satellite mean elements |
| [Moons of Saturn](catalogue/moons-saturn.md) | 292 | JPL satellite mean elements |
| [Moons of Uranus](catalogue/moons-uranus.md) | 29 | JPL satellite mean elements |
| [Moons of Neptune](catalogue/moons-neptune.md) | 16 | JPL satellite mean elements |
| [Moons of Pluto](catalogue/moons-pluto.md) | 5 | JPL satellite mean elements |
| [The sky beyond the solar system](catalogue/sky.md) | 63 named objects + 9,096 stars | Yale Bright Star Catalogue (NASA HEASARC) · NASA SVS · NASA images · NASA Exoplanet Archive · SIMBAD |

Each row in the catalogue links to:

- **JPL Horizons** object record (planets and moons, by NAIF ID), or the **JPL SBDB** record (asteroids, dwarf planets, comets), the authoritative NASA source;
- the **NASA Science** page for the object, where NASA has published one (129 objects).

## Method and sources

- [Sources, methodology and accuracy](sources.md)

## How the catalogue was verified (November 2026)

1. The data tables were read directly from `index.html`.
2. Every planet and moon was matched to its NAIF ID in the JPL *Planetary Satellite Mean Elements* table, and the ID was confirmed in JPL Horizons. 493 of 494 resolve in Horizons. The exception, S/2025 U 1, is listed by JPL's table but not yet in Horizons.
3. Every small body was resolved through the JPL SBDB API to its SPK ID and full designation.
4. Each NASA Science link was checked to return HTTP 200 at the time of writing.
