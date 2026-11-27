[← Documentation index](../README.md) · [Project README](https://github.com/kauemelo01/Solar-System-Explorer#readme)

# Moons of Mars

**2 moons.** Positions along the orbits are **fitted to JPL Horizons over 1800–2050 AD** ([Moon orbits](../sources.md#moon-orbits)): checked against Horizons on other dates, the typical error for this planet's moons is 1.0° (median), and the least accurate is Phobos at 1.9°. The *a*, *e*, *i* and *P* columns below are the **JPL mean orbital elements** (Laplace-plane or ecliptic, as published by JPL SSD); the fitted orbits keep these shapes, or refine them where Horizons shows they change. Every moon links to its **JPL Horizons** object record by NAIF ID, and to its NASA Science page where NASA has published one.

The *Surface image* column says what the app draws on each body: real photos, partial maps, painted illustrations or plain shapes. Details and sources: [Surface maps](../sources.md#surface-maps).

- NASA Science overview: <https://science.nasa.gov/mars/moons/>
- JPL mean elements table: <https://ssd.jpl.nasa.gov/sats/elem/sep.html>
- JPL physical parameters: <https://ssd.jpl.nasa.gov/sats/phys_par/>
- JPL discovery circumstances: <https://ssd.jpl.nasa.gov/sats/discovery.html>
- IAU Minor Planet Center satellite announcements (MPECs): <https://minorplanetcenter.net/mpec/RecentMPECs.html>

Radius values marked *est.* are not published; the app uses a placeholder size for display only (a [limitation of the model](../sources.md#limitations-of-the-model)).

**Radii.** From JPL *Planetary Satellite Physical Parameters* <https://ssd.jpl.nasa.gov/sats/phys_par/>: Phobos, Deimos. See [Moon sizes](../sources.md#moon-sizes).

## Phobos & Deimos (2)

*major moon*

| # | Moon | a (km) | e | i (°) | Period (days) | Radius (km) | NAIF ID | References | [Surface image](../interface.md#card-notes) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | <a id="m-phobos"></a>**Phobos** | 9,375 | 0.015 | 1.1 | 0.3187 | 11.1 | 401 | [JPL Horizons](https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27401%27&OBJ_DATA=YES&MAKE_EPHEM=NO) · [NASA](https://science.nasa.gov/mars/moons/phobos/) | Real photos |
| 2 | <a id="m-deimos"></a>**Deimos** | 23,457 | 0 | 1.8 | 1.2625 | 6.2 | 402 | [JPL Horizons](https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27402%27&OBJ_DATA=YES&MAKE_EPHEM=NO) · [NASA](https://science.nasa.gov/mars/moons/deimos/) | Real photos, gaps filled |

