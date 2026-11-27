# Small-body orbit fits

These scripts build `data/sb-orbits.js`: the orbits of the dwarf planets, asteroids, centaurs and comets fitted to their JPL Horizons ephemerides over 1800–2050 AD, as a series of time windows. The method, the targets and the accuracy are described in [docs/sources.md, Small-body orbits](../../docs/sources.md#small-body-orbits) and [Accuracy targets](../../docs/sources.md#accuracy-targets).

## Setup

- Python 3 with `numpy` and `scipy`; Node.js (the scripts run the app's own orbit code from `index.html`).
- A work folder (default `~/solar-system-explorer-work/sbfit`, or set `SSE_WORK`). Horizons downloads are cached there: `hz/` (fitting samples), `check/` (test dates), `planets/` (the planets every 30 days).
- `SSE_REPO`: this repository's folder (default: two folders up from these scripts). The list of bodies comes from `SB` and `LINKS` in its `index.html`.

## Steps

1. Base samples, every 10 days, for each body to fit (`python sbfit.py --list` prints them: every small body except the eight that already meet the targets with their single SBDB orbit, listed in `SKIP` in `hz.py`):

   ```
   python -c "import hz;[hz.span(k,'1800-01-01','2050-12-31','10 d') for k in hz.IDS if k not in hz.SKIP]"
   ```

   Where Horizons covers less (Bennu: from 1901), the span is clipped and recorded in `hz/coverage.json`.
2. `python sbfit.py <id>` for each body (`python sbfit.py --list | xargs -P 4 -I{} python sbfit.py {}`; a few hours in all, mostly spent downloading). For each body it:
   - adds samples wherever the body moves more than 0.05 radian between two samples, as seen from the Sun or, within 0.08 AU of Venus, Earth or Mars or 0.8 AU of Jupiter, from that planet (near perihelion and in planetary encounters);
   - near a planet, moves the target onto the app's own planet: JPL's position plus the app's planet error (the app's planets are simple Keplerian orbits, Jupiter up to 0.14° off), blended in between 0.03 and 0.08 AU (Jupiter: 0.35 and 0.8 AU), so that flybys happen at the right distance and time from the planet as the app draws it;
   - fits each window (20 years to start with) in the app's orbit model, halving it until every sample is within 0.25° (seen from the Sun, or from the planet when one is near), or along its path within 0.2 days; windows longer than 400 days may also take slow drifts of the perihelion, node and mean motion. Each window is fitted over its own span plus 10% on each side, where the app blends it with its neighbours.
   Near a planet the tolerance is 0.05° (`SSE_TOL_NEAR`, in degrees). The published fits use `SSE_TOL_NEAR=0.01` for 21P/Giacobini-Zinner and `SSE_TOL_NEAR=0.005` for 26P/Grigg-Skjellerup, whose distant passes by Jupiter have very flat closest points: `SSE_TOL_NEAR=0.005 python sbfit.py c26p`.
3. `python writefits.py`: writes `data/sb-orbits.js` from `fits/`.
4. Checks, with the app's own code:
   - `python mkcheck.py <id>` for each body: 600 test dates never used in the fit (300 at random, 300 between the fitter's own samples, which concentrates them near perihelia and flybys); then `node validate.js $SSE_WORK/check`: the 1°-or-1-day target at every test date;
   - `python encounters.py`: every pass within 0.05 AU of Venus, Earth, the Moon or Mars, or inside Jupiter's Hill sphere (0.35 AU), found in the samples and refined with planet-centred Horizons vectors (`encounters.json`; resumable); then `node flycheck.js $SSE_WORK/encounters.json`: whether each happens in the app with its closest point within 3 hours of JPL's.
   - `node jumps.js`: smoothness at every window boundary (the step across a boundary against the steps beside it; the published data: at most 3% larger).

## Files

`hz.py` downloads and caches Horizons state vectors; `sbfit.py` holds the orbit model (a copy of the app's `moonOrbit` and `ell1`, with the same Kepler solver) and the fitting rule; `appplanets.js` gives the app's planet positions to Python; `validate.js`, `flycheck.js` and `jumps.js` run the app's own code from `index.html`. The window format is the moons' (`[t0, t1, M0, n, ω0, ω′, Ω0, Ω′, M″, a km, e, i]`, J2000 ecliptic, times in days from J2000); the app blends neighbouring windows over 10% of the shorter one (`blendB()` in `index.html`).
