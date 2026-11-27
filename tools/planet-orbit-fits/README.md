# Planet orbit fits

These scripts build `data/planet-orbits.js`: the heliocentric orbits of Mercury, Venus, the Earth–Moon barycentre, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto, fitted to their JPL Horizons ephemerides (DE440) over 1800–2050 AD as a series of time windows. The method and the accuracy are described in the documentation, under [Planets](../../docs/sources.md#planets).

## Setup

- Python 3 with `numpy` and `scipy`; Node.js 18 or later (for `fetch`, and to run the app's own orbit code from `index.html`).
- A work folder (default `~/solar-system-explorer-work/sbfit`, shared with the [small-body fits](../small-body-orbit-fits/README.md), or set `SSE_WORK`). Horizons downloads are cached in `planets-hz/`, the fits written to `planet-fits/`.

## Steps

1. `node hz.js fit`, `node hz.js check`, `node hz.js far`: Horizons state vectors (Sun-centred, J2000 ecliptic, UT) for each body: every 2 days (Mercury) to 60 days (Neptune, Pluto) over 1800–2050 for the fit; on a step of about 3.4 times that, which never lands on a fitting sample, for the test dates; and every 73 days over 1600–1800 and 2051–2250, to measure the positions outside the fitted span. Neptune and Pluto are in Horizons only from 1800 to 2199.
2. `SSE_PL_TOL=0.002 python plfit.py`: fits each body in windows of 20 years to start with, in the app's orbit model, halving a window until every sample in it (and in the 10% beyond each end, where the app blends it with its neighbours) is within `SSE_PL_TOL` degrees, as seen from the Sun (the full 3-D error over the distance). The published fits use 0.002° (7.2″); windows are never halved below 200 days.
3. `python writefits.py`: writes `data/planet-orbits.js` from `planet-fits/`.
4. `node validate.js check` and `node validate.js far`: the app's own code against the test dates, as seen from the Sun and from the Earth–Moon barycentre, next to Standish's elements on the same dates; and, for `check`, the step across every window boundary against the steps beside it.

After a change to the planets, refit the small bodies that come near them (`tools/small-body-orbit-fits`): their fits follow JPL *relative to the app's planet* in a planet's zone, so they depend on where the app puts it.

## Files

`hz.js` downloads and caches the Horizons vectors; `plfit.py` holds the orbit model (the same as `sbfit.py`'s copy of the app's `moonOrbit` and `ell1`) and the fitting rule; `writefits.py` writes the data file; `validate.js` runs the app's own code from `index.html`. The window format is the small bodies' (`[t0, t1, M0, n, ω0, ω′, Ω0, Ω′, M″, a km, e, i]`, J2000 ecliptic, times in days from J2000). Outside the fitted span the app uses Standish's elements (`EL` in `index.html`), turned and scaled to meet the fit at its first or last date, with that correction fading out over half an orbit (`plHelio()` in `index.html`).
