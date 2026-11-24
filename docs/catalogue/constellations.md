[← Documentation index](../README.md) · [Project README](https://github.com/kauemelo01/Solar-System-Explorer#readme)

# The 88 constellations

The International Astronomical Union (IAU) divides the whole sky into **88 constellations**: regions with official boundaries, not just star patterns. In the app they are **off by default**. Turn them on under *Beyond the solar system → Constellations (IAU)*, then choose **All 88** or **Zodiac (13)**, and whether to show the stick figures and the boundaries. Click a constellation's name for its card.

## Sources

| Layer | Source |
|---|---|
| Boundaries | E. Delporte (1930), *Délimitation scientifique des constellations*, adopted by the IAU. Digitised by N. G. Roman (1987, *PASP* 99, 695; CDS catalogue [VI/42](https://vizier.cfa.harvard.edu/ftp/cats/VI/42/ReadMe)) and A. C. Davenhall & S. K. Leggett (1989; CDS catalogue [VI/49](https://vizier.cfa.harvard.edu/ftp/cats/VI/49/ReadMe)), retrieved from the VizieR mirror at Harvard-Smithsonian CfA |
| Stick figures | NASA/Goddard Space Flight Center Scientific Visualization Studio, [*Deep Star Maps*](https://svs.gsfc.nasa.gov/3895), files `constellation_figures.jpg` (8192 × 4096) and `constellation_figures_print.jpg` (1024 × 512, used where 8K images are not supported). Figures based on those developed for the IAU by Alan MacRobert of *Sky & Telescope* (Roger Sinnott and Rick Fienberg) |
| Names and abbreviations | IAU three-letter abbreviations (Delporte 1930) |

## How the data were built and checked

1. **Boundaries.** Delporte's boundaries run along lines of constant right ascension and declination for the equinox of 1875. Roman's table defines them completely, so each boundary segment was rebuilt from it, densified, and precessed to J2000 with the IAU 1976 precession model.
2. **Check against Roman.** All 8 test positions published with Roman's catalogue are placed in the correct constellation.
3. **Check against the published J2000 boundaries.** All 1,533 original vertices of Davenhall & Leggett's J2000 file are matched within 3.7″ (median 1.5″). The small difference is between precession models.
4. **Areas** are exact spherical areas of the boundary cells. They add up to the whole sky (41,252.96 square degrees) and match the IAU values to 0.01 square degrees: Hydra 1,302.85, Crux 68.45.
5. **Membership map.** A 2048 × 1024 map, in the same layout as the sky map, records which constellation each point belongs to. The app uses it to show only the selected constellations' figures, for example just the zodiac.
6. **Label positions** are each constellation's area-weighted centre, checked to lie inside it. Serpens is the only constellation in two separate parts, so it has two labels, one for Serpens Caput and one for Serpens Cauda.

## The zodiac: 13 constellations, not 12

The ecliptic, the Sun's yearly path across the sky, passes through **13** IAU constellations. Astrology's 12 signs are equal 30° slices of the ecliptic and do not match the real constellations, which differ in width. The 13th is **Ophiuchus**, where the Sun spends more time than in neighbouring Scorpius.

Dates are when the Sun is inside each constellation's boundaries in 2026, computed from where the J2000 ecliptic crosses the IAU boundaries and the Sun's position (Meeus's low-precision formula). They shift by about a day from year to year.

| Constellation | Sun enters | Sun leaves | Days |
|---|---|---|---|
| [Aries](#con-ari) | Apr 19 | May 14 | 25 |
| [Taurus](#con-tau) | May 14 | Jun 21 | 37 |
| [Gemini](#con-gem) | Jun 21 | Jul 21 | 28 |
| [Cancer](#con-cnc) | Jul 21 | Aug 11 | 20 |
| [Leo](#con-leo) | Aug 11 | Sep 17 | 36 |
| [Virgo](#con-vir) | Sep 17 | Oct 31 | 45 |
| [Libra](#con-lib) | Oct 31 | Nov 23 | 24 |
| [Scorpius](#con-sco) | Nov 23 | Nov 30 | 7 |
| [Ophiuchus](#con-oph) | Nov 30 | Dec 18 | 19 |
| [Sagittarius](#con-sgr) | Dec 18 | Jan 20 | 34 |
| [Capricornus](#con-cap) | Jan 20 | Feb 16 | 28 |
| [Aquarius](#con-aqr) | Feb 16 | Mar 12 | 24 |
| [Pisces](#con-psc) | Mar 12 | Apr 19 | 38 |

## All 88 constellations

| # | Constellation | Abbreviation | Area (sq. degrees) | Size rank | Zodiac |
|---|---|---|---|---|---|
| 1 | <a id="con-and"></a>**Andromeda** | And | 722.27 | 19 |  |
| 2 | <a id="con-ant"></a>**Antlia** | Ant | 238.89 | 62 |  |
| 3 | <a id="con-aps"></a>**Apus** | Aps | 206.33 | 67 |  |
| 4 | <a id="con-aqr"></a>**Aquarius** | Aqr | 979.84 | 10 | yes |
| 5 | <a id="con-aql"></a>**Aquila** | Aql | 652.47 | 22 |  |
| 6 | <a id="con-ara"></a>**Ara** | Ara | 237.06 | 63 |  |
| 7 | <a id="con-ari"></a>**Aries** | Ari | 441.39 | 39 | yes |
| 8 | <a id="con-aur"></a>**Auriga** | Aur | 657.43 | 21 |  |
| 9 | <a id="con-boo"></a>**Boötes** | Boo | 906.83 | 13 |  |
| 10 | <a id="con-cae"></a>**Caelum** | Cae | 124.86 | 81 |  |
| 11 | <a id="con-cam"></a>**Camelopardalis** | Cam | 756.83 | 18 |  |
| 12 | <a id="con-cnc"></a>**Cancer** | Cnc | 505.88 | 31 | yes |
| 13 | <a id="con-cvn"></a>**Canes Venatici** | CVn | 465.19 | 38 |  |
| 14 | <a id="con-cma"></a>**Canis Major** | CMa | 380.12 | 43 |  |
| 15 | <a id="con-cmi"></a>**Canis Minor** | CMi | 183.36 | 71 |  |
| 16 | <a id="con-cap"></a>**Capricornus** | Cap | 413.95 | 40 | yes |
| 17 | <a id="con-car"></a>**Carina** | Car | 494.19 | 34 |  |
| 18 | <a id="con-cas"></a>**Cassiopeia** | Cas | 598.41 | 25 |  |
| 19 | <a id="con-cen"></a>**Centaurus** | Cen | 1,060.43 | 9 |  |
| 20 | <a id="con-cep"></a>**Cepheus** | Cep | 587.78 | 27 |  |
| 21 | <a id="con-cet"></a>**Cetus** | Cet | 1,231.42 | 4 |  |
| 22 | <a id="con-cha"></a>**Chamaeleon** | Cha | 131.59 | 79 |  |
| 23 | <a id="con-cir"></a>**Circinus** | Cir | 93.35 | 85 |  |
| 24 | <a id="con-col"></a>**Columba** | Col | 270.18 | 54 |  |
| 25 | <a id="con-com"></a>**Coma Berenices** | Com | 386.47 | 42 |  |
| 26 | <a id="con-cra"></a>**Corona Australis** | CrA | 127.70 | 80 |  |
| 27 | <a id="con-crb"></a>**Corona Borealis** | CrB | 178.71 | 73 |  |
| 28 | <a id="con-crv"></a>**Corvus** | Crv | 183.80 | 70 |  |
| 29 | <a id="con-crt"></a>**Crater** | Crt | 282.39 | 53 |  |
| 30 | <a id="con-cru"></a>**Crux** | Cru | 68.45 | 88 |  |
| 31 | <a id="con-cyg"></a>**Cygnus** | Cyg | 803.99 | 16 |  |
| 32 | <a id="con-del"></a>**Delphinus** | Del | 188.54 | 69 |  |
| 33 | <a id="con-dor"></a>**Dorado** | Dor | 179.18 | 72 |  |
| 34 | <a id="con-dra"></a>**Draco** | Dra | 1,082.95 | 8 |  |
| 35 | <a id="con-equ"></a>**Equuleus** | Equ | 71.64 | 87 |  |
| 36 | <a id="con-eri"></a>**Eridanus** | Eri | 1,137.92 | 6 |  |
| 37 | <a id="con-for"></a>**Fornax** | For | 397.50 | 41 |  |
| 38 | <a id="con-gem"></a>**Gemini** | Gem | 513.76 | 30 | yes |
| 39 | <a id="con-gru"></a>**Grus** | Gru | 365.51 | 45 |  |
| 40 | <a id="con-her"></a>**Hercules** | Her | 1,225.17 | 5 |  |
| 41 | <a id="con-hor"></a>**Horologium** | Hor | 248.88 | 58 |  |
| 42 | <a id="con-hya"></a>**Hydra** | Hya | 1,302.85 | 1 |  |
| 43 | <a id="con-hyi"></a>**Hydrus** | Hyi | 243.04 | 61 |  |
| 44 | <a id="con-ind"></a>**Indus** | Ind | 294.01 | 49 |  |
| 45 | <a id="con-lac"></a>**Lacerta** | Lac | 200.69 | 68 |  |
| 46 | <a id="con-leo"></a>**Leo** | Leo | 946.98 | 12 | yes |
| 47 | <a id="con-lmi"></a>**Leo Minor** | LMi | 231.96 | 64 |  |
| 48 | <a id="con-lep"></a>**Lepus** | Lep | 290.30 | 51 |  |
| 49 | <a id="con-lib"></a>**Libra** | Lib | 538.06 | 29 | yes |
| 50 | <a id="con-lup"></a>**Lupus** | Lup | 333.67 | 46 |  |
| 51 | <a id="con-lyn"></a>**Lynx** | Lyn | 545.39 | 28 |  |
| 52 | <a id="con-lyr"></a>**Lyra** | Lyr | 286.47 | 52 |  |
| 53 | <a id="con-men"></a>**Mensa** | Men | 153.48 | 75 |  |
| 54 | <a id="con-mic"></a>**Microscopium** | Mic | 209.51 | 66 |  |
| 55 | <a id="con-mon"></a>**Monoceros** | Mon | 481.56 | 35 |  |
| 56 | <a id="con-mus"></a>**Musca** | Mus | 138.36 | 77 |  |
| 57 | <a id="con-nor"></a>**Norma** | Nor | 165.29 | 74 |  |
| 58 | <a id="con-oct"></a>**Octans** | Oct | 291.05 | 50 |  |
| 59 | <a id="con-oph"></a>**Ophiuchus** | Oph | 948.33 | 11 | yes |
| 60 | <a id="con-ori"></a>**Orion** | Ori | 594.11 | 26 |  |
| 61 | <a id="con-pav"></a>**Pavo** | Pav | 377.66 | 44 |  |
| 62 | <a id="con-peg"></a>**Pegasus** | Peg | 1,120.81 | 7 |  |
| 63 | <a id="con-per"></a>**Perseus** | Per | 614.99 | 24 |  |
| 64 | <a id="con-phe"></a>**Phoenix** | Phe | 469.32 | 37 |  |
| 65 | <a id="con-pic"></a>**Pictor** | Pic | 246.74 | 59 |  |
| 66 | <a id="con-psc"></a>**Pisces** | Psc | 889.41 | 14 | yes |
| 67 | <a id="con-psa"></a>**Piscis Austrinus** | PsA | 245.38 | 60 |  |
| 68 | <a id="con-pup"></a>**Puppis** | Pup | 673.44 | 20 |  |
| 69 | <a id="con-pyx"></a>**Pyxis** | Pyx | 220.83 | 65 |  |
| 70 | <a id="con-ret"></a>**Reticulum** | Ret | 113.93 | 82 |  |
| 71 | <a id="con-sge"></a>**Sagitta** | Sge | 79.92 | 86 |  |
| 72 | <a id="con-sgr"></a>**Sagittarius** | Sgr | 867.42 | 15 | yes |
| 73 | <a id="con-sco"></a>**Scorpius** | Sco | 496.78 | 33 | yes |
| 74 | <a id="con-scl"></a>**Sculptor** | Scl | 474.77 | 36 |  |
| 75 | <a id="con-sct"></a>**Scutum** | Sct | 109.12 | 84 |  |
| 76 | <a id="con-ser"></a>**Serpens** | Ser | 636.93 | 23 |  |
| 77 | <a id="con-sex"></a>**Sextans** | Sex | 313.52 | 47 |  |
| 78 | <a id="con-tau"></a>**Taurus** | Tau | 797.26 | 17 | yes |
| 79 | <a id="con-tel"></a>**Telescopium** | Tel | 251.51 | 57 |  |
| 80 | <a id="con-tri"></a>**Triangulum** | Tri | 131.85 | 78 |  |
| 81 | <a id="con-tra"></a>**Triangulum Australe** | TrA | 109.98 | 83 |  |
| 82 | <a id="con-tuc"></a>**Tucana** | Tuc | 294.55 | 48 |  |
| 83 | <a id="con-uma"></a>**Ursa Major** | UMa | 1,279.65 | 3 |  |
| 84 | <a id="con-umi"></a>**Ursa Minor** | UMi | 255.86 | 56 |  |
| 85 | <a id="con-vel"></a>**Vela** | Vel | 499.65 | 32 |  |
| 86 | <a id="con-vir"></a>**Virgo** | Vir | 1,294.43 | 2 | yes |
| 87 | <a id="con-vol"></a>**Volans** | Vol | 141.35 | 76 |  |
| 88 | <a id="con-vul"></a>**Vulpecula** | Vul | 268.16 | 55 |  |
