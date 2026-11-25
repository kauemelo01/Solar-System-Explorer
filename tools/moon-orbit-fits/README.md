# Moon orbit fits

These scripts build `data/moon-orbits.js`: every planetary moon's orbit fitted to its JPL Horizons ephemeris over 1800–2050 AD. The method and the accuracy are described in [docs/sources.md, Moon orbits](../../docs/sources.md#moon-orbits).

## Setup

- Python 3 with `numpy` and `scipy`; Node.js for the checks.
- A work folder (default `~/solar-system-explorer-work`, or set `SSE_WORK`) holding a copy of these scripts and `sep.html` (a copy of `jpl-sat-elements.html`, JPL's *Planetary Satellite Mean Elements* page). Horizons downloads are cached in its `hzcache/` folder.
- Set `SSE_REPO` to this repository's folder: the scripts read the moon list from its `index.html` and the NAIF IDs from `docs/catalogue/`.
- `names.json` in the work folder, which maps each fit file's name back to the moon's name in the app (`S_2009_S_2` → `S/2009 S 2`); `writefits2.py` needs it. To make it:

  ```
  python -c "import os,json,appdata;M=appdata.load(os.environ['SSE_REPO']+'/index.html')[0];json.dump({m[0].replace('/','_').replace(' ','_'):m[0] for m in M},open('names.json','w'),ensure_ascii=False)"
  ```

`jpl-sat-physical-parameters.html` is a copy of JPL's *Planetary Satellite Physical Parameters* page, kept for reference; no script reads it.

## Steps (run in the work folder)

1. `python coverage.py`: which part of 1800–2051 AD Horizons covers for each moon (`coverage.json`).
2. `python fit1800.py`: fit every moon (one JSON per moon in `fits1800/`; resumable, about an hour with 8 cores).
3. `python checkfetch.py`: independent check positions on other dates (`check.json`).
4. `python writefits2.py <repo>/data/moon-orbits.js` (also writes the training errors to `fitstats1800.json`), then `node validate.js <repo>/index.html <repo>/data/moon-orbits.js check.json`: the check, with the app's own code (`validate.json`).
5. Fixes for moons the check finds poor, in this order, then step 4 again:
   - `refitA.py`: fast inner moons get a single orbit fitted with the dense series near 2000 added; Janus and Epimetheus get 2-year windows fitted to a daily series (replaced by `phasetab.py` below);
   - `phasetab.py`: a single orbit plus a table of along-track corrections every 5 or 10 days, for the moons in co-orbital resonances (Janus, Epimetheus, Helene, Polydeuces). It overwrites their fit files, so it runs after `refitA.py`. Its list `K` also names S/2009 S 2 and S/2025 U 1: remove both before running it, as the published data has no table for S/2009 S 2, and S/2025 U 1 has no Horizons data (see below);
   - `refitB.py`: moons still more than 3° off in `validate.json` (irregular moons), refitted with 10-year windows split down to 2.5 years; the new fit is kept only if it is better.
6. Distances, then step 4 again. The fits above match directions only, which leaves an orbit's size free (and, for windows, drifting); the check reports distance errors (`dmax`, `drms`) as well as angles:
   - `fixscale_g.py`: single-orbit fits with a fitted shape get their semi-major axis scaled to Horizons' distances;
   - `fixscale.py`, then `fitdist.py`: windows are scaled to Horizons' distances (`fixscale.json`), then refitted on direction and distance together (`fitdist.json`; about 20 minutes with 8 cores).
7. Smoothness, with the app's own code: `node jumps.js <repo>/index.html <repo>/data/moon-orbits.js` (no moon should jump at a window boundary) and `node bends.js <repo>/index.html <repo>/data/moon-orbits.js` (sharp turns in each moon's path, sampled like a 250-year trail; add a moon's name to check one). The app blends neighbouring windows (`ell()` in `index.html`); the moons that keep a bend are listed in docs/sources.md, *Limitations of the model*.

## Special cases

- **S/2009 S 2** is fitted in Saturn's equatorial plane (IAU pole RA 40.589°, Dec 83.537°), which the JPL table does not give. The scripts do not set this pole: `POLES` in `moonmodel.py` has Uranus, Neptune and Pluto only. Without it the moon is fitted in the J2000 ecliptic. To reproduce the published fit, add `'saturn':(40.589,83.537)` to `POLES` for this moon's fit only: `POLES` applies to every moon of that planet for which the JPL table gives no plane.
- **S/2025 U 1** is not in Horizons (its NAIF number matches an asteroid there), so it has no fit. `refitA.py` lists it and prints an error for it, which is harmless.

## Files

`moonmodel.py` holds the orbit model and the Horizons downloads; `appdata.py` reads the moon list from `index.html`; `fitlib.py` builds the list of moons to fit (with their NAIF IDs) and holds the fitting rule (one orbit if it fits within 0.5°, otherwise time windows). The other scripts load `fitlib.py`, or `fit1800.py`, which adds the 1800–2051 AD span.
