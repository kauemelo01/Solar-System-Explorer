[← Documentation index](../README.md) · [Project README](https://github.com/kauemelo01/Solar-System-Explorer#readme)

# The sky beyond the solar system

Everything outside the solar system shown in the app, with its position, distance and sources. Positions are J2000 right ascension and declination from **CDS SIMBAD/Sesame**. They are drawn on a sphere in the same ecliptic J2000 frame as the planets, so each object sits where it really is in the sky.

> **Why the sky does not move when you change the centre.** Hold Earth still, then Neptune: the Pleiades and Andromeda stay put. Neptune is about 30 AU from the Sun, while even the nearest star, Proxima Centauri, is about 268,000 AU away. The shift (parallax) is under 25 arcseconds, far too small to see. The solar system is tiny compared with the distances to the stars.

## Background layers

| Layer | What it is | Source |
|---|---|---|
| Milky Way and faint stars | All-sky star map, plate carrée in J2000 RA/Dec, 4096 × 2048 and 8192 × 4096 | NASA/Goddard Space Flight Center Scientific Visualization Studio, [*Deep Star Maps*](https://svs.gsfc.nasa.gov/3895) (2009), files `starmap_4k.jpg` and `starmap_8k.jpg`. Built from the Bright Star, Tycho-2 and UCAC3 catalogues |
| Constellations (off by default) | The 88 IAU constellations: boundaries, stick figures and names, with a Zodiac (13) filter | See [constellations.md](constellations.md) |
| Stars | 9,096 stars brighter than about magnitude 6.5, coloured by their B−V index | *Yale Bright Star Catalogue*, 5th revised ed. (Hoffleit & Warren 1991, CDS V/50), via NASA HEASARC table [`bsc5p`](https://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html) |

## Nebulae, clusters and galaxies

Distances are rounded values commonly quoted by NASA and in the literature; follow the SIMBAD link for current measurements. *Apparent size* is the object's true size in the sky. In the app each object is a small marker with a label at its true position; clicking it opens a card. The NASA image column links a reference picture of the object, which is not drawn in the sky.

| Object | Type | Constellation | RA (J2000) | Dec (J2000) | Apparent size | Distance | NASA reference image | Image credit | Position |
|---|---|---|---|---|---|---|---|---|---|
| <a id="dso-m45"></a>**Pleiades (M45)** | Open star cluster | Taurus | 03h 46m 38.0s | +24° 10′ 41″ | 1.8° | ≈ 444 light-years | [PIA09263](https://images.nasa.gov/details/PIA09263) | NASA/JPL-Caltech | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M45) |
| <a id="dso-hyades"></a>**Hyades** | Open star cluster | Taurus | 04h 30m 27.4s | +16° 46′ 43″ | 5.5° | ≈ 153 light-years | — | — | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=Hyades) |
| <a id="dso-m44"></a>**Beehive Cluster (M44)** | Open star cluster | Cancer | 08h 39m 58.4s | +19° 36′ 33″ | 1.6° | ≈ 580 light-years | — | — | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M44) |
| <a id="dso-doublecluster"></a>**Double Cluster (NGC 869 & 884)** | Pair of open clusters | Perseus | 02h 20m 36.4s | +57° 08′ 30″ | 1.0° | ≈ 7,500 light-years | — | — | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=NGC%20869) |
| <a id="dso-omegacen"></a>**Omega Centauri** | Globular cluster | Centaurus | 13h 26m 47.3s | −47° 28′ 46″ | 36′ | ≈ 17,000 light-years | [PIA13125](https://images.nasa.gov/details/PIA13125) | NASA/JPL-Caltech/UCLA | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=NGC%205139) |
| <a id="dso-m13"></a>**Hercules Cluster (M13)** | Globular cluster | Hercules | 16h 41m 41.6s | +36° 27′ 41″ | 20′ | ≈ 23,000 light-years | — | — | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M13) |
| <a id="dso-m42"></a>**Orion Nebula (M42)** | Star-forming nebula | Orion | 05h 35m 16.8s | −05° 23′ 15″ | 1.1° | ≈ 1,340 light-years | [PIA13959](https://images.nasa.gov/details/PIA13959) | NASA/ESA/JPL-Caltech/IRAM | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M42) |
| <a id="dso-horsehead"></a>**Horsehead Nebula** | Dark nebula | Orion | 05h 40m 59.0s | −02° 27′ 30″ | 8′ | ≈ 1,400 light-years | [PIA04215](https://images.nasa.gov/details/PIA04215) | JPL/NASA, NOAO, ESA and The Hubble Heritage Team, STScI/AURA | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=Barnard%2033) |
| <a id="dso-m16"></a>**Eagle Nebula (M16)** | Star-forming nebula · Pillars of Creation | Serpens | 18h 18m 45.1s | −13° 47′ 31″ | 35′ | ≈ 6,500 light-years | [GSFC_20171208_Archive_e000842](https://images.nasa.gov/details/GSFC_20171208_Archive_e000842) | NASA, ESA, and the Hubble Heritage Team (STScI/AURA) | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M16) |
| <a id="dso-carina"></a>**Carina Nebula** | Star-forming nebula · Cosmic Cliffs | Carina | 10h 45m 02.2s | −59° 41′ 60″ | 2.0° | ≈ 7,500 light-years | [carina_nebula](https://images.nasa.gov/details/carina_nebula) | NASA ESA CSA STScI | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=NGC%203372) |
| <a id="dso-m1"></a>**Crab Nebula (M1)** | Supernova remnant · seen exploding in 1054 | Taurus | 05h 34m 31.8s | +22° 01′ 03″ | 7′ | ≈ 6,500 light-years | [PIA03606](https://images.nasa.gov/details/PIA03606) | NASA/ESA/JPL/Arizona State Univ. | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M1) |
| <a id="dso-m57"></a>**Ring Nebula (M57)** | Planetary nebula | Lyra | 18h 53m 35.1s | +33° 01′ 45″ | 3.8′ | ≈ 2,500 light-years | [GSFC_20171208_Archive_e001464](https://images.nasa.gov/details/GSFC_20171208_Archive_e001464) | NASA, ESA, C.R. O’Dell (Vanderbilt Univ.), G.J. Ferland (Univ. of Kentucky), W.J. Henney and M. Peimbert (UNAM); Large Binocular Telescope | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M57) |
| <a id="dso-helix"></a>**Helix Nebula** | Planetary nebula | Aquarius | 22h 29m 38.5s | −20° 50′ 14″ | 25′ | ≈ 650 light-years | [PIA15817](https://images.nasa.gov/details/PIA15817) | NASA/JPL-Caltech | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=NGC%207293) |
| <a id="dso-ngc3132"></a>**Southern Ring Nebula (NGC 3132)** | Planetary nebula · Webb first image | Vela | 10h 07m 01.8s | −40° 26′ 11″ | 1.5′ | ≈ 2,500 light-years | — | — | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=NGC%203132) |
| <a id="dso-tarantula"></a>**Tarantula Nebula** | Star-forming nebula in the Large Magellanic Cloud | Dorado | 05h 38m 42.0s | −69° 05′ 60″ | 40′ | ≈ 160,000 light-years | [PIA05062](https://images.nasa.gov/details/PIA05062) | NASA/JPL-Caltech/Cornell University and University of Leiden | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=NGC%202070) |
| <a id="dso-m8"></a>**Lagoon Nebula (M8)** | Star-forming nebula | Sagittarius | 18h 03m 37.0s | −24° 23′ 12″ | 1.5° | ≈ 4,100 light-years | [PIA14728](https://images.nasa.gov/details/PIA14728) | NASA/JPL-Caltech | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M8) |
| <a id="dso-sgra"></a>**Galactic Centre (Sgr A*)** | Centre of the Milky Way · supermassive black hole | Sagittarius | 17h 45m 40.0s | −29° 00′ 28″ | — | ≈ 26,000 light-years | [PIA13932](https://images.nasa.gov/details/PIA13932) | NASA/JPL-Caltech | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=Sgr%20A%2A) |
| <a id="dso-m31"></a>**Andromeda Galaxy (M31)** | Spiral galaxy · largest in the Local Group | Andromeda | 00h 42m 44.3s | +41° 16′ 07″ | 3.2° | ≈ 2.5 million light-years | [PIA08787](https://images.nasa.gov/details/PIA08787) | NASA/JPL-Caltech | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M31) |
| <a id="dso-m33"></a>**Triangulum Galaxy (M33)** | Spiral galaxy | Triangulum | 01h 33m 50.9s | +30° 39′ 37″ | 1.2° | ≈ 2.7 million light-years | [PIA03033](https://images.nasa.gov/details/PIA03033) | NASA/JPL-Caltech | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M33) |
| <a id="dso-lmc"></a>**Large Magellanic Cloud** | Satellite galaxy of the Milky Way | Dorado / Mensa | 05h 23m 34.6s | −69° 45′ 22″ | 10.8° | ≈ 160,000 light-years | — | — | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=LMC) |
| <a id="dso-smc"></a>**Small Magellanic Cloud** | Satellite galaxy of the Milky Way | Tucana | 00h 52m 38.0s | −72° 48′ 01″ | 5.3° | ≈ 200,000 light-years | — | — | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=SMC) |
| <a id="dso-m51"></a>**Whirlpool Galaxy (M51)** | Spiral galaxy | Canes Venatici | 13h 29m 52.7s | +47° 11′ 43″ | 11′ | ≈ 31 million light-years | [PIA04230](https://images.nasa.gov/details/PIA04230) | NASA and The Hubble Heritage Team STScI/AURA Acknowledgement: N. Scoville Caltech and T. Rector NOAO | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M51) |
| <a id="dso-m101"></a>**Pinwheel Galaxy (M101)** | Spiral galaxy | Ursa Major | 14h 03m 12.6s | +54° 20′ 56″ | 29′ | ≈ 21 million light-years | [PIA04631](https://images.nasa.gov/details/PIA04631) | NASA/JPL/Caltech | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M101) |
| <a id="dso-m104"></a>**Sombrero Galaxy (M104)** | Spiral galaxy | Virgo | 12h 39m 59.4s | −11° 37′ 23″ | 9′ | ≈ 31 million light-years | [PIA15226](https://images.nasa.gov/details/PIA15226) | NASA/STScI/AURA | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=M104) |
| <a id="dso-cena"></a>**Centaurus A** | Active elliptical galaxy | Centaurus | 13h 25m 27.6s | −43° 01′ 09″ | 26′ | ≈ 12 million light-years | [GSFC_20171208_Archive_e001893](https://images.nasa.gov/details/GSFC_20171208_Archive_e001893) | NASA Goddard Hubble release, 16 Jun 2011 (no credit line in NASA metadata) | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=NGC%205128) |
| <a id="dso-stephan"></a>**Stephan's Quintet** | Compact galaxy group · Webb first image | Pegasus | 22h 35m 57.5s | +33° 57′ 36″ | 3.5′ | ≈ 290 million light-years | — | — | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=Stephan%27s%20Quintet) |
| <a id="dso-hdf"></a>**Hubble Deep Field** | Deep field · thousands of galaxies | Ursa Major | 12h 36m 49.5s | +62° 12′ 58″ | 2.6′ | galaxies up to ≈ 12 billion light-years | [PIA12110](https://images.nasa.gov/details/PIA12110) | NASA/JPL/STScI Hubble Deep Field Team | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=Hubble%20Deep%20Field) |
| <a id="dso-hudf"></a>**Hubble Ultra Deep Field** | Deep field · thousands of galaxies | Fornax | 03h 32m 39.0s | −27° 47′ 29″ | 3.1′ | galaxies up to ≈ 13 billion light-years | [GSFC_20171208_Archive_e001061](https://images.nasa.gov/details/GSFC_20171208_Archive_e001061) | NASA/ESA | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=Hubble%20Ultra%20Deep%20Field) |
| <a id="dso-smacs0723"></a>**Webb First Deep Field (SMACS 0723)** | Galaxy cluster acting as a gravitational lens | Volans | 07h 23m 13.3s | −73° 27′ 25″ | 2.4′ | cluster ≈ 4.6 billion light-years | [webb_first_deep_field](https://images.nasa.gov/details/webb_first_deep_field) | NASA ESA CSA STScI | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=SMACS%20J0723.3-7327) |

## Stars with known planets

Data from the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) (`pscomppars` table, queried November 2026). These stars are too faint to be in the bright-star layer except 51 Pegasi; they appear as labels at their true positions.

| Star | RA (J2000) | Dec (J2000) | Distance | Known planets | NASA Exoplanet Archive | Position |
|---|---|---|---|---|---|---|
| <a id="exo-proxima"></a>**Proxima Centauri** | 14h 29m 42.9s | −62° 40′ 46″ | ≈ 4.2 light-years | 2 | [overview](https://exoplanetarchive.ipac.caltech.edu/overview/Proxima%20Cen) | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=Proxima%20Cen) |
| <a id="exo-trappist1"></a>**TRAPPIST-1** | 23h 06m 29.4s | −05° 02′ 29″ | ≈ 40.5 light-years | 7 | [overview](https://exoplanetarchive.ipac.caltech.edu/overview/TRAPPIST-1) | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=TRAPPIST-1) |
| <a id="exo-51peg"></a>**51 Pegasi** | 22h 57m 28.0s | +20° 46′ 08″ | ≈ 50.4 light-years | 1 | [overview](https://exoplanetarchive.ipac.caltech.edu/overview/51%20Peg) | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=51%20Peg) |
| <a id="exo-kepler186"></a>**Kepler-186** | 19h 54m 36.6s | +43° 57′ 18″ | ≈ 579.2 light-years | 5 | [overview](https://exoplanetarchive.ipac.caltech.edu/overview/Kepler-186) | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=Kepler-186) |
| <a id="exo-kepler452"></a>**Kepler-452** | 19h 44m 00.9s | +44° 16′ 39″ | ≈ 1,799.5 light-years | 1 | [overview](https://exoplanetarchive.ipac.caltech.edu/overview/Kepler-452) | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=Kepler-452) |

## Named bright stars

Proper names follow the IAU Working Group on Star Names ([IAU-CSN list](https://www.pas.rochester.edu/~emamajek/WGSN/IAU-CSN.txt)). Position, magnitude and spectral type are from the Yale Bright Star Catalogue (HR number). The catalogue's parallaxes predate Hipparcos, so the app does not show star distances; use the SIMBAD link for modern values.

| Star | Designation | HR | RA (J2000) | Dec (J2000) | V mag | Spectral type | Position |
|---|---|---|---|---|---|---|---|
| <a id="star-sirius"></a>**Sirius** | Alp CMa | 2491 | 06h 45m 08.9s | −16° 42′ 58″ | -1.46 | A1Vm | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%202491) |
| <a id="star-canopus"></a>**Canopus** | Alp Car | 2326 | 06h 23m 57.1s | −52° 41′ 45″ | -0.72 | F0II | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%202326) |
| <a id="star-rigil-kentaurus"></a>**Rigil Kentaurus** | Alp1Cen | 5459 | 14h 39m 35.9s | −60° 50′ 07″ | -0.01 | G2V | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%205459) |
| <a id="star-arcturus"></a>**Arcturus** | Alp Boo | 5340 | 14h 15m 39.7s | +19° 10′ 57″ | -0.04 | K1.5IIIFe-0.5 | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%205340) |
| <a id="star-vega"></a>**Vega** | Alp Lyr | 7001 | 18h 36m 56.3s | +38° 47′ 01″ | 0.03 | A0Va | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%207001) |
| <a id="star-capella"></a>**Capella** | Alp Aur | 1708 | 05h 16m 41.4s | +45° 59′ 53″ | 0.08 | G5IIIe+G0III | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%201708) |
| <a id="star-rigel"></a>**Rigel** | Bet Ori | 1713 | 05h 14m 32.3s | −08° 12′ 06″ | 0.12 | B8Ia: | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%201713) |
| <a id="star-procyon"></a>**Procyon** | Alp CMi | 2943 | 07h 39m 18.1s | +05° 13′ 30″ | 0.38 | F5IV-V | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%202943) |
| <a id="star-achernar"></a>**Achernar** | Alp Eri | 472 | 01h 37m 42.9s | −57° 14′ 12″ | 0.46 | B3Vpe | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%20472) |
| <a id="star-betelgeuse"></a>**Betelgeuse** | Alp Ori | 2061 | 05h 55m 10.3s | +07° 24′ 25″ | 0.50 | M1-2Ia-Iab | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%202061) |
| <a id="star-hadar"></a>**Hadar** | Bet Cen | 5267 | 14h 03m 49.4s | −60° 22′ 23″ | 0.61 | B1III | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%205267) |
| <a id="star-altair"></a>**Altair** | Alp Aql | 7557 | 19h 50m 47.0s | +08° 52′ 06″ | 0.77 | A7V | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%207557) |
| <a id="star-acrux"></a>**Acrux** | Alp1Cru | 4730 | 12h 26m 35.9s | −63° 05′ 57″ | 1.33 | B0.5IV | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%204730) |
| <a id="star-aldebaran"></a>**Aldebaran** | Alp Tau | 1457 | 04h 35m 55.2s | +16° 30′ 33″ | 0.85 | K5+III | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%201457) |
| <a id="star-antares"></a>**Antares** | Alp Sco | 6134 | 16h 29m 24.4s | −26° 25′ 55″ | 0.96 | M1.5Iab-Ib+B4Ve | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%206134) |
| <a id="star-spica"></a>**Spica** | Alp Vir | 5056 | 13h 25m 11.6s | −11° 09′ 41″ | 0.98 | B1III-IV+B2V | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%205056) |
| <a id="star-pollux"></a>**Pollux** | Bet Gem | 2990 | 07h 45m 18.9s | +28° 01′ 34″ | 1.14 | K0IIIb | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%202990) |
| <a id="star-fomalhaut"></a>**Fomalhaut** | Alp PsA | 8728 | 22h 57m 39.1s | −29° 37′ 20″ | 1.16 | A3V | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%208728) |
| <a id="star-deneb"></a>**Deneb** | Alp Cyg | 7924 | 20h 41m 25.9s | +45° 16′ 49″ | 1.25 | A2Ia | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%207924) |
| <a id="star-mimosa"></a>**Mimosa** | Bet Cru | 4853 | 12h 47m 43.2s | −59° 41′ 19″ | 1.25 | B0.5III | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%204853) |
| <a id="star-regulus"></a>**Regulus** | Alp Leo | 3982 | 10h 08m 22.3s | +11° 58′ 02″ | 1.35 | B7V | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%203982) |
| <a id="star-castor"></a>**Castor** | Alp Gem | 2891 | 07h 34m 36.0s | +31° 53′ 18″ | 1.98 | A1V | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%202891) |
| <a id="star-polaris"></a>**Polaris** | Alp UMi | 424 | 02h 31m 48.7s | +89° 15′ 51″ | 2.02 | F7:Ib-II | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%20424) |
| <a id="star-bellatrix"></a>**Bellatrix** | Gam Ori | 1790 | 05h 25m 07.9s | +06° 20′ 59″ | 1.64 | B2III | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%201790) |
| <a id="star-alnilam"></a>**Alnilam** | Eps Ori | 1903 | 05h 36m 12.8s | −01° 12′ 07″ | 1.70 | B0Ia | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%201903) |
| <a id="star-alnitak"></a>**Alnitak** | Zet Ori | 1948 | 05h 40m 45.5s | −01° 56′ 34″ | 2.05 | O9.7Ib | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%201948) |
| <a id="star-mintaka"></a>**Mintaka** | Del Ori | 1852 | 05h 32m 00.4s | −00° 17′ 57″ | 2.23 | O9.5II | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%201852) |
| <a id="star-mizar"></a>**Mizar** | Zet UMa | 5054 | 13h 23m 55.5s | +54° 55′ 31″ | 2.27 | A1VpSrSi | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%205054) |
| <a id="star-dubhe"></a>**Dubhe** | Alp UMa | 4301 | 11h 03m 43.7s | +61° 45′ 03″ | 1.79 | K0IIIa | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%204301) |
| <a id="star-alcyone"></a>**Alcyone** | Eta Tau | 1165 | 03h 47m 29.1s | +24° 06′ 18″ | 2.87 | B7IIIe | [SIMBAD](https://simbad.harvard.edu/simbad/sim-id?Ident=HR%201165) |

## Reference images

Reference images are in the [NASA Image and Video Library](https://images.nasa.gov/) and are linked, not copied into this project. NASA material is generally not subject to copyright in the United States ([NASA media usage guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/)). Images produced with partners (ESA, CSA, STScI and universities) carry the credit lines listed above, which should be kept when the images are reused.
