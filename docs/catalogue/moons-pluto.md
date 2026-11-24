[← Documentation index](../README.md) · [Project README](https://github.com/kauemelo01/Solar-System-Explorer#readme)

# Moons of Pluto

**5 moons.** Orbits use the **JPL mean orbital elements** of planetary satellites (mean equatorial elements, referred to Pluto's equator with the IAU 2015 pole, as published by JPL SSD). The *a*, *e*, *i* and *P* columns below are the exact values used by the app. Every moon links to its **JPL Horizons** object record by NAIF ID, and to its NASA Science page where NASA has published one.

The *Surface image* column says what the app draws on each body: real photos, partial maps, painted illustrations or plain shapes. Details and sources: [Surface maps](../sources.md#surface-maps).

- NASA Science overview: <https://science.nasa.gov/dwarf-planets/pluto/moons/>
- JPL mean elements table: <https://ssd.jpl.nasa.gov/sats/elem/sep.html>
- JPL physical parameters: <https://ssd.jpl.nasa.gov/sats/phys_par/>
- JPL discovery circumstances: <https://ssd.jpl.nasa.gov/sats/discovery.html>
- IAU Minor Planet Center satellite announcements (MPECs): <https://minorplanetcenter.net/mpec/RecentMPECs.html>

Radius values marked *est.* are not published; the app uses a placeholder size for display only (a [limitation of the model](../sources.md#limitations-of-the-model)).

## Charon (1)

*binary companion*

| # | Moon | a (km) | e | i (°) | Period (days) | Radius (km) | NAIF ID | References | [Surface image](../sources.md#card-notes) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | <a id="m-charon"></a>**Charon** | 19,600 | 0 | 0 | 6.3872 | 606 | 901 | [JPL Horizons](https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27901%27&OBJ_DATA=YES&MAKE_EPHEM=NO) · [NASA](https://science.nasa.gov/dwarf-planets/pluto/moons/charon/) | Painted |

## Small moons (4)

*small moon*

| # | Moon | a (km) | e | i (°) | Period (days) | Radius (km) | NAIF ID | References | [Surface image](../sources.md#card-notes) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | <a id="m-styx"></a>**Styx** | 43,200 | 0.025 | 0 | 20.1600 | 6 | 905 | [JPL Horizons](https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27905%27&OBJ_DATA=YES&MAKE_EPHEM=NO) · [NASA](https://science.nasa.gov/dwarf-planets/pluto/moons/styx/) | Plain shape |
| 2 | <a id="m-nix"></a>**Nix** | 49,300 | 0.015 | 0 | 24.8500 | 25 | 902 | [JPL Horizons](https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27902%27&OBJ_DATA=YES&MAKE_EPHEM=NO) · [NASA](https://science.nasa.gov/dwarf-planets/pluto/moons/nix/) | Plain shape |
| 3 | <a id="m-kerberos"></a>**Kerberos** | 58,300 | 0.01 | 0.4 | 32.1700 | 6 | 904 | [JPL Horizons](https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27904%27&OBJ_DATA=YES&MAKE_EPHEM=NO) · [NASA](https://science.nasa.gov/dwarf-planets/pluto/moons/kerberos/) | Plain shape |
| 4 | <a id="m-hydra"></a>**Hydra** | 65,200 | 0.009 | 0.3 | 38.2000 | 26 | 903 | [JPL Horizons](https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27903%27&OBJ_DATA=YES&MAKE_EPHEM=NO) · [NASA](https://science.nasa.gov/dwarf-planets/pluto/moons/hydra/) | Plain shape |

Charon's position matches JPL Horizons to about 0.1°. Phases of the four small moons (Styx, Nix, Kerberos, Hydra) along their orbits are approximate. Radii are under review; see [Known issues](../sources.md#known-issues).
