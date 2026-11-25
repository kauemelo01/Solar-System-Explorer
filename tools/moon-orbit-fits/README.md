# Moon orbit fits

These scripts build `data/moon-orbits.js`: every planetary moon's orbit fitted to its JPL Horizons ephemeris over 1800–2050. The method and the accuracy are described in [docs/sources.md, Moon orbits](../../docs/sources.md#moon-orbits).

## Setup

- Python 3 with `numpy` and `scipy`; Node.js for the check.
- A work folder (default `~/solar-system-explorer-work`, or set `SSE_WORK`) holding a copy of these scripts and `sep.html` (a copy of `jpl-sat-elements.html`, JPL's *Planetary Satellite Mean Elements* page). Horizons downloads are cached in its `hzcache/` folder.
- Set `SSE_REPO` to this repository's folder: the scripts read the moon list from its `index.html` and the NAIF IDs from `docs/catalogue/`.

## Steps (run in the work folder)

1. `python coverage.py`: which part of 1800–2051 Horizons covers for each moon (`coverage.json`).
2. `python fit1800.py`: fit every moon (one JSON per moon in `fits1800/`; resumable, about an hour with 8 cores).
3. `python checkfetch.py`: independent check positions on other dates (`check.json`).
4. `python writefits2.py <repo>/data/moon-orbits.js`, then `node validate.js <repo>/index.html <repo>/data/moon-orbits.js check.json`: the check, with the app's own code (`validate.json`).
5. Fixes for moons the check finds poor, then steps 4 again:
   - `refitA.py`: fast inner moons, with a dense series near 2000 (Janus and Epimetheus in daily windows);
   - `phasetab.py`: along-track correction tables for moons in co-orbital resonances (Janus, Epimetheus, Helene, Polydeuces);
   - `refitB.py`: irregular moons, with windows split down to 2.5 years.
6. Distances, then step 4 again. The fits above match directions only, which leaves an orbit's size free (and, for windows, drifting); the check reports distance errors (`dmax`, `drms`) as well as angles:
   - `fixscale_g.py`: single-orbit fits with a fitted shape get their semi-major axis scaled to Horizons' distances;
   - `fixscale.py`, then `fitdist.py`: windows are scaled to Horizons' distances, then refitted on direction and distance together (about 20 minutes with 8 cores).
7. Smoothness, with the app's own code: `node jumps.js <repo>/index.html <repo>/data/moon-orbits.js` (no moon should jump at a window boundary) and `node bends.js <repo>/index.html <repo>/data/moon-orbits.js` (sharp turns in each moon's path, sampled like a 250-year trail; add a moon's name to check one). The app blends neighbouring windows (`ell()` in `index.html`); the moons that keep a bend are listed in docs/sources.md, *Limitations of the model*.

S/2009 S 2 is fitted in Saturn's equatorial plane (IAU pole 40.589°, 83.537°), which the JPL table does not give. S/2025 U 1 is not in Horizons (its NAIF number matches an asteroid there), so it has no fit.

`moonmodel.py`, `fitall.py`, `runfits2.py`, `runfits3.py` and `appdata.py` hold the shared model and helpers.
