# Planet checks

These scripts measure the app's planets, the Earth–Moon barycentre and Pluto against JPL Horizons, with the app's own code from `index.html`. They give the figures in the documentation, under [Planets](../../docs/sources.md#planets) and [Accuracy](../../docs/sources.md#accuracy).

The app uses E. M. Standish and J. G. Williams's Keplerian elements (JPL SSD, <https://ssd.jpl.nasa.gov/planets/approx_pos.html>):
- Table 1 over 1800–2050 AD;
- Table 2a and 2b outside;
- a blend of the two positions over the 30 years beyond each end.

The code is `EL`, `EL2`, `kep()` and `plHelio()` in `index.html`. Nothing is fitted, so these scripts only check.

## Setup

- Node.js 18 or later (for `fetch`).
- A work folder (default `~/solar-system-explorer-work/sbfit`, shared with the [small-body fits](../small-body-orbit-fits/README.md), or set `SSE_WORK`). Horizons downloads are cached in `planets-hz/`.

## Steps

1. `node hz.js check`, `node hz.js far`, `node hz.js wide`: Horizons positions around the Sun (J2000 ecliptic, UT).
   - `check` covers 1800–2050, every 7 days for Mercury up to every 202 days for Neptune and Pluto.
   - `far` covers 1600–1800 and 2051–2250, every 73 days.
   - `wide` covers 1000–1600 and 2250–3000 every 365 days, plus Neptune and Pluto over 1600–1800. It uses the system barycentres, which Horizons covers over the whole span; it has the planets themselves only for shorter spans (Neptune and Pluto from 1800).
2. `node validate.js`: prints the following.
   - The largest error in each span of years, seen from the Sun and from the Earth–Moon barycentre, for three models: the app, Table 1 alone and Table 2 alone.
   - How smooth the blends are.
   - A check that the app is exactly Table 1 over 1800–2050. The small-body fits near the planets depend on that, through `tools/small-body-orbit-fits`.
   - How much of the inner planets' error before 1600 comes from the app using Universal Time where the elements use Terrestrial Time.

   Options: `BINS='[[1000,1800],[1800,2051],[2051,3000]]'` chooses the spans of years. `FADE=100` tries another blend length, in years.
