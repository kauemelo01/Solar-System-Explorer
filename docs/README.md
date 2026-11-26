[← Project README](https://github.com/kauemelo01/Solar-System-Explorer#readme) · [Open the app](https://kauemelo01.github.io/Solar-System-Explorer/)

# Solar System Explorer: documentation

This folder documents **every object** in Solar System Explorer: the values the app uses and the public NASA/JPL record each value comes from.

## Object catalogue (536 solar-system objects, 7 ring systems + the sky)

| Page | Objects | Primary reference |
|---|---:|---|
| [Sun, planets and the Moon](catalogue/sun-planets.md) | 10 | JPL Keplerian elements · NASA fact sheets |
| [Dwarf planets, asteroids, centaurs and comets](catalogue/small-bodies.md) | 56 | JPL Small-Body Database; Pluto from the JPL planet table |
| [Moons of Mars](catalogue/moons-mars.md) | 2 | JPL Horizons (fitted orbits) · JPL satellite mean elements |
| [Moons of Jupiter](catalogue/moons-jupiter.md) | 115 | JPL Horizons (fitted orbits) · JPL satellite mean elements |
| [Moons of Saturn](catalogue/moons-saturn.md) | 292 | JPL Horizons (fitted orbits) · JPL satellite mean elements |
| [Moons of Uranus](catalogue/moons-uranus.md) | 29 | JPL Horizons (fitted orbits) · JPL satellite mean elements |
| [Moons of Neptune](catalogue/moons-neptune.md) | 16 | JPL Horizons (fitted orbits) · JPL satellite mean elements |
| [Moons of Pluto](catalogue/moons-pluto.md) | 5 | JPL Horizons (fitted orbits) · JPL satellite mean elements |
| [Moons of dwarf planets and asteroids](catalogue/moons-small-bodies.md) | 11 | JPL Horizons satellite solutions · peer-reviewed orbit papers |
| [Ring systems](catalogue/rings.md) | 7 systems | NASA NSSDCA ring fact sheets · occultation papers |
| [The 88 constellations](catalogue/constellations.md) | 88 | IAU boundaries (Delporte 1930; CDS VI/42, VI/49) · NASA SVS figures |
| [The sky beyond the solar system](catalogue/sky.md) | 64 named objects + 9,096 stars | Yale Bright Star Catalogue (NASA HEASARC) · NASA SVS · NASA images · NASA Exoplanet Archive · SIMBAD |

Each row in the catalogue links to:

- **JPL Horizons** object record (planets and moons, by NAIF ID), or the **JPL SBDB** record (asteroids, dwarf planets, comets), the authoritative NASA source;
- the **NASA Science** page for the object, where NASA has published one (142 objects).

## Method and sources

- [Sources, methodology and accuracy](sources.md), starting with [What's included](sources.md#whats-included) and [What's not included](sources.md#whats-not-included)

## How the catalogue was verified (November 2026)

1. The data tables were read directly from `index.html`.
2. Every planet and planetary moon was matched to its NAIF ID in the JPL *Planetary Satellite Mean Elements* table, and the ID was confirmed in JPL Horizons. All resolve in Horizons except S/2025 U 1. S/2025 U 1 is listed by JPL's table but not yet in Horizons.
3. Every small body was resolved through the JPL SBDB API to its SPK ID and full designation.
4. Each NASA Science link was checked to return HTTP 200 at the time of writing.
5. Moons of dwarf planets and asteroids: Dysnomia, Weywot, Vanth, Dimorphos and Menoetius come from their JPL Horizons satellite solutions. Hiʻiaka, Namaka, Xiangliu, Selam, Skamandrios and Queta come from the published orbit papers. Objects without a verifiable published orbit were left out ([What's not included](sources.md#whats-not-included)).
6. Rings: radii and widths come from the NASA NSSDCA ring fact sheets and, for small bodies, from the occultation papers.
7. Sky objects: each deep-sky object and planet-hosting star was resolved by name in CDS SIMBAD/Sesame for its J2000 position. Planet-hosting stars were cross-checked against the NASA Exoplanet Archive. Named stars were matched to their Bayer designations in the Yale Bright Star Catalogue.
8. Constellations: boundaries rebuilt from Roman's table pass all 8 of its published test positions, match the 1,533 published J2000 vertices within 3.7″, and give areas that add up to the whole sky. See [constellations.md](catalogue/constellations.md#how-the-data-were-built-and-checked).
9. The sky map's orientation was checked by mapping the SIMBAD positions of the Large and Small Magellanic Clouds and the galactic centre onto the NASA star map: each lands on the matching feature.
