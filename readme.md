# Planet ephemerides (work in progress)

This branch is a work in progress. It keeps only the essential files: those that are new or changed in this work, which fits the planets, the Earth–Moon barycentre and Pluto to JPL Horizons over 1800–2050 AD. It doesn't hold the rest of the app, so it won't run on its own.

The files are relative to `wip-release-4` at commit `d4c2ddc`. To try them, copy them over a checkout of that branch, keeping their paths.

- `index.html`: planet positions come from the fits, and switch to Standish's elements outside 1800–2050.
- `data/planet-orbits.js`: the planet fits (new).
- `data/sb-orbits.js`: the 24 small bodies that come near a planet, refitted to the new planet positions.
- `tools/planet-orbit-fits/`: the scripts that build and check the planet fits (new).
- `tools/small-body-orbit-fits/`: the small-body tools, now using the fitted planets.
- `docs/`: the method, the accuracy and the updated flyby distances.
