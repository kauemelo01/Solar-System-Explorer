[← Documentation index](../README.md) · [Project README](https://github.com/kauemelo01/Solar-System-Explorer#readme)

# Dwarf planets, asteroids, centaurs and comets

39 named bodies. Moons of dwarf planets and asteroids are on [their own page](moons-small-bodies.md), Pluto's moons on [Moons of Pluto](moons-pluto.md), and the rings of Haumea, Quaoar and Chariklo on the [rings page](rings.md). Orbital elements are osculating heliocentric elements taken from the **JPL Small-Body Database (SBDB)**, except Pluto's (see the note under the dwarf planets); most use epoch JD 2461200.5 (2026-Jun-24 TDB). Comet orbits use the elements of their most recent perihelion passage in the SBDB. Each row links to the live SBDB record, so values can be re-checked at any time.

The *Surface image* column says what the app draws on each body: real photos, partial maps, painted illustrations or plain shapes. Details and sources: [Surface maps](../sources.md#surface-maps).

## Dwarf planets

The five dwarf planets recognised by the IAU. In the app: the *Dwarf planets* switch.

| Body | Designation (JPL) | Class | a (AU) | e | i (°) | Radius (km) | JPL SBDB | NASA page | [Surface image](../sources.md#card-notes) |
|---|---|---|---|---|---|---|---|---|---|
| <a id="ceres"></a>**Ceres** | 1 Ceres (A801 AA) | Dwarf planet · asteroid belt | 2.766 | 0.0797 | 10.59 | 469.7 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20000001) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20000001&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/dwarf-planets/ceres/) | Real photos |
| <a id="pluto"></a>**Pluto** | 134340 Pluto (1930 BM) | Dwarf planet · Kuiper belt | 39.48 | 0.2488 | 17.14 | 1,188.3 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20134340) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20134340&phys-par=1) · [Horizons](https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27999%27&OBJ_DATA=YES&MAKE_EPHEM=NO) | [science.nasa.gov](https://science.nasa.gov/dwarf-planets/pluto/) | Painted |
| <a id="eris"></a>**Eris** | 136199 Eris (2003 UB313) | Dwarf planet · scattered disc | 67.93 | 0.4382 | 43.93 | 1,163 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20136199) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20136199&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/dwarf-planets/eris/) | Painted |
| <a id="haumea"></a>**Haumea** | 136108 Haumea (2003 EL61) | Dwarf planet · Kuiper belt | 43.06 | 0.1944 | 28.21 | 1,050 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20136108) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20136108&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/dwarf-planets/haumea/) · [rings](rings.md#haumea) | Painted |
| <a id="makemake"></a>**Makemake** | 136472 Makemake (2005 FY9) | Dwarf planet · Kuiper belt | 45.57 | 0.1589 | 29.03 | 715 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20136472) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20136472&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/dwarf-planets/makemake/) | Painted |

**Pluto** is a dwarf planet, but the app computes its orbit like the planets', from the JPL *Approximate Positions of the Planets* elements (E. M. Standish, valid 1800–2050), not from the SBDB. The *a*, *e* and *i* shown are that table's J2000 values; its NAIF ID is 999. Its five moons, including Charon, are listed in [Moons of Pluto](moons-pluto.md).

## Dwarf planet candidates

Large trans-Neptunian objects widely considered dwarf planets but not recognised by the IAU. In the app: the *Candidates* switch.

| Body | Designation (JPL) | Class | a (AU) | e | i (°) | Radius (km) | JPL SBDB | NASA page | [Surface image](../sources.md#card-notes) |
|---|---|---|---|---|---|---|---|---|---|
| <a id="gonggong"></a>**Gonggong** | 225088 Gonggong (2007 OR10) | Dwarf planet candidate · scattered disc | 66.87 | 0.5043 | 30.9 | 615 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20225088) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20225088&phys-par=1) | — | Painted |
| <a id="quaoar"></a>**Quaoar** | 50000 Quaoar (2002 LM60) | Dwarf planet candidate · Kuiper belt | 43.16 | 0.0352 | 7.99 | 555 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20050000) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20050000&phys-par=1) | [rings](rings.md#quaoar) | Painted |
| <a id="sedna"></a>**Sedna** | 90377 Sedna (2003 VB12) | Dwarf planet candidate · detached object | 543.7 | 0.8599 | 11.93 | 500 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20090377) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20090377&phys-par=1) | — | Painted |
| <a id="orcus"></a>**Orcus** | 90482 Orcus (2004 DW) | Dwarf planet candidate · Kuiper belt | 39.38 | 0.2205 | 20.56 | 455 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20090482) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20090482&phys-par=1) | — | Painted |

## Asteroids and centaurs

| Body | Designation (JPL) | Class | a (AU) | e | i (°) | Radius (km) | JPL SBDB | NASA page | [Surface image](../sources.md#card-notes) |
|---|---|---|---|---|---|---|---|---|---|
| <a id="vesta"></a>**Vesta** | 4 Vesta (A807 FA) | Main-belt asteroid · Dawn visited | 2.361 | 0.0902 | 7.14 | 262 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20000004) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20000004&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/4-vesta/) | Real photos |
| <a id="pallas"></a>**Pallas** | 2 Pallas (A802 FA) | Main-belt asteroid | 2.77 | 0.2307 | 34.93 | 256 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20000002) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20000002&phys-par=1) | — | Painted |
| <a id="juno"></a>**Juno** | 3 Juno (A804 RA) | Main-belt asteroid | 2.671 | 0.2557 | 12.99 | 123 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20000003) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20000003&phys-par=1) | — | Painted |
| <a id="hygiea"></a>**Hygiea** | 10 Hygiea (A849 GA) | Main-belt asteroid | 3.151 | 0.1067 | 3.83 | 204 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20000010) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20000010&phys-par=1) | — | Painted |
| <a id="psyche"></a>**Psyche** | 16 Psyche (A852 FA) | Metal-rich main-belt asteroid | 2.926 | 0.1349 | 3.1 | 111 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20000016) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20000016&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/16-psyche/) | Painted |
| <a id="lutetia"></a>**Lutetia** | 21 Lutetia (A852 VA) | Main-belt asteroid · Rosetta flyby | 2.434 | 0.1648 | 3.06 | 49 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20000021) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20000021&phys-par=1) | — | Painted |
| <a id="ida"></a>**Ida** | 243 Ida (A884 SB) | Main-belt asteroid · Galileo flyby | 2.863 | 0.0461 | 1.13 | 15.7 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20000243) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20000243&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/243-ida/) | Painted |
| <a id="eros"></a>**Eros** | 433 Eros (A898 PA) | Near-Earth asteroid · NEAR landed | 1.458 | 0.2229 | 10.83 | 8.4 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20000433) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20000433&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/433-eros/) | Painted |
| <a id="bennu"></a>**Bennu** | 101955 Bennu (1999 RQ36) | Near-Earth asteroid · OSIRIS-REx sample | 1.126 | 0.2037 | 6.03 | 0.245 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20101955) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20101955&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/101955-bennu/) | Painted |
| <a id="apophis"></a>**Apophis** | 99942 Apophis (2004 MN4) | Near-Earth asteroid · Earth flyby 2029 | 0.922 | 0.1911 | 3.34 | 0.17 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20099942) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20099942&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/apophis/) | Painted |
| <a id="hektor"></a>**Hektor** | 624 Hektor (A907 CF) | Jupiter trojan (L4) | 5.277 | 0.0243 | 18.15 | 112 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20000624) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20000624&phys-par=1) | — | Painted |
| <a id="chiron"></a>**Chiron** | 2060 Chiron (1977 UB) | Centaur | 13.68 | 0.3798 | 6.93 | 83 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20002060) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20002060&phys-par=1) | — | Painted |
| <a id="didymos"></a>**Didymos** | 65803 Didymos (1996 GT) | Near-Earth asteroid · DART target system | 1.643 | 0.3831 | 3.41 | 0.39 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20065803) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20065803&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/didymos/) | Painted |
| <a id="ryugu"></a>**Ryugu** | 162173 Ryugu (1999 JU3) | Near-Earth asteroid · Hayabusa2 sample return | 1.191 | 0.1911 | 5.87 | 0.448 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20162173) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20162173&phys-par=1) | — | Painted |
| <a id="itokawa"></a>**Itokawa** | 25143 Itokawa (1998 SF36) | Near-Earth asteroid · Hayabusa sample return | 1.324 | 0.2802 | 1.62 | 0.165 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20025143) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20025143&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/25143-itokawa/) | Painted |
| <a id="dinkinesh"></a>**Dinkinesh** | 152830 Dinkinesh (1999 VD57) | Main-belt asteroid · Lucy flyby | 2.192 | 0.1127 | 2.09 | 0.36 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20152830) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20152830&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/dinkinesh/) | Painted |
| <a id="donaldjohanson"></a>**Donaldjohanson** | 52246 Donaldjohanson (1981 EQ5) | Main-belt asteroid · Lucy flyby | 2.384 | 0.1869 | 4.43 | 1.95 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20052246) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20052246&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/donaldjohanson/) | Painted |
| <a id="eurybates"></a>**Eurybates** | 3548 Eurybates (1973 SO) | Jupiter trojan (L4) · Lucy target | 5.217 | 0.0906 | 8.05 | 31.94 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20003548) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20003548&phys-par=1) | — | Painted |
| <a id="phaethon"></a>**Phaethon** | 3200 Phaethon (1983 TB) | Near-Earth asteroid · parent of the Geminids | 1.271 | 0.8897 | 22.31 | 3.125 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20003200) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20003200&phys-par=1) | — | Painted |
| <a id="arrokoth"></a>**Arrokoth** | 486958 Arrokoth (2014 MU69) | Kuiper belt object · New Horizons flyby | 44.053 | 0.0356 | 2.45 | ≈ 9 *est.* | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20486958) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20486958&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/kuiper-belt/arrokoth-2014-mu69/) | Painted |
| <a id="chariklo"></a>**Chariklo** | 10199 Chariklo (1997 CU26) | Centaur · first small body found with rings | 15.734 | 0.1708 | 23.43 | 124 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20010199) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=20010199&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/asteroids/10199-chariklo/) · [rings](rings.md#chariklo) | Painted |

## Comets

| Body | Designation (JPL) | Class | a (AU) | e | i (°) | Radius (km) | JPL SBDB | NASA page | [Surface image](../sources.md#card-notes) |
|---|---|---|---|---|---|---|---|---|---|
| <a id="halley"></a>**1P/Halley** | 1P/Halley | Periodic comet · returns 2061 | 17.969 | 0.968 | 162 | 5.5 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1000036) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1000036&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/comets/1p-halley/) | Painted |
| <a id="encke"></a>**2P/Encke** | 2P/Encke | Periodic comet · 3.3-year orbit | 2.216 | 0.847 | 11.3 | 2.4 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1000025) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1000025&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/comets/2p-encke/) | Painted |
| <a id="c67p"></a>**67P/Churyumov-Gerasimenko** | 67P/Churyumov-Gerasimenko | Periodic comet · Rosetta landed | 3.454 | 0.641 | 7.04 | 2 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1000012) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1000012&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/comets/67p-churyumov-gerasimenko/) | Painted |
| <a id="halebopp"></a>**C/1995 O1 (Hale-Bopp)** | C/1995 O1 (Hale-Bopp) | Long-period comet · 1997 apparition | 178.2 | 0.995 | 89.3 | 30 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1000132) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1000132&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/comets/c-1995-o1-hale-bopp/) | Painted |
| <a id="c109p"></a>**109P/Swift-Tuttle** | 109P/Swift-Tuttle | Halley-type comet · parent of the Perseids | 26.092 | 0.9632 | 113.45 | 13 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1000140) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1000140&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/comets/109p-swift-tuttle/) | Painted |
| <a id="c55p"></a>**55P/Tempel-Tuttle** | 55P/Tempel-Tuttle | Halley-type comet · parent of the Leonids | 10.338 | 0.9056 | 162.49 | 1.8 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1000095) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1000095&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/comets/55p-tempel-tuttle/) | Painted |
| <a id="c9p"></a>**9P/Tempel 1** | 9P/Tempel 1 | Jupiter-family comet · Deep Impact | 3.146 | 0.5097 | 10.47 | 3 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1000093) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1000093&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/comets/9p-tempel-1/) | Painted |
| <a id="c81p"></a>**81P/Wild 2** | 81P/Wild 2 | Jupiter-family comet · Stardust sample return | 3.45 | 0.5374 | 3.24 | 2 | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1000107) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1000107&phys-par=1) | [science.nasa.gov](https://science.nasa.gov/solar-system/comets/81p-wild/) | Painted |
| <a id="neowise"></a>**C/2020 F3 (NEOWISE)** | C/2020 F3 (NEOWISE) | Long-period comet · 2020 apparition | 358.468 | 0.9992 | 128.94 | ≈ 2.5 *est.* | [lookup](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1003667) · [JSON](https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=1003667&phys-par=1) | — | Painted |

## Notes on sizes

- **Chariklo:** equivalent radius 124 ± 9 km from the 2013 stellar occultation (Braga-Ribas et al. 2014, *Nature*; [arXiv:1409.7259](https://arxiv.org/abs/1409.7259)), used instead of the older radiometric diameter in the SBDB.
- **Dinkinesh:** about 790 m at its widest (Lucy team, [NASA](https://science.nasa.gov/solar-system/asteroids/dinkinesh/)); the app uses the SBDB-scale mean radius of 0.36 km.
- **Arrokoth:** a contact binary about 36 km long (Spencer et al. 2020, *Science*; [arXiv:2004.00727](https://arxiv.org/abs/2004.00727)). The app draws it as one body of radius ≈ 9 km, marked *est.*
- **C/2020 F3 (NEOWISE):** no published nucleus size was found in a source we could verify; the app uses a placeholder radius of 2.5 km, marked *est.*
- **Comet nuclei** (109P, 55P, 9P, 81P): diameters from the SBDB physical parameters.

## Sources for this group

- JPL Small-Body Database Lookup: <https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html>
- Pluto's orbit: JPL SSD, *Approximate Positions of the Planets* <https://ssd.jpl.nasa.gov/planets/approx_pos.html>; NASA NSSDCA *Pluto Fact Sheet* <https://nssdc.gsfc.nasa.gov/planetary/factsheet/plutofact.html>
- JPL SBDB API documentation: <https://ssd-api.jpl.nasa.gov/doc/sbdb.html>
- IAU Minor Planet Center: <https://www.minorplanetcenter.net/>
- NASA Science — Asteroids, Comets & Meteors: <https://science.nasa.gov/solar-system/asteroids/>, <https://science.nasa.gov/solar-system/comets/>
- NASA Science — Dwarf planets and the Kuiper belt: <https://science.nasa.gov/dwarf-planets/>, <https://science.nasa.gov/solar-system/kuiper-belt/>

> **About the belts.** The *Main asteroid belt*, *Jupiter trojans* and *Kuiper belt* layers in the app are statistical clouds drawn from typical orbit distributions to show where these populations live. They are **not** individual catalogue objects and are therefore not listed here.
