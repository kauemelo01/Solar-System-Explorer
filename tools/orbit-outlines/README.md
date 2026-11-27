# Orbit outlines

`drift.js` decides which bodies orbiting the Sun get an orbit outline in the app. The rule and the list are in the documentation, under [Orbit outlines](../../docs/sources.md#orbit-outlines). Every moon has an outline; these scripts don't cover them.

## What it measures

For each planet, dwarf planet, candidate, asteroid, centaur and comet, it takes the orbit the app uses on a start date and holds it fixed:
- a planet's or Pluto's elements on that date, with the mean longitude still moving;
- a small body's fitted time window, or its one SBDB orbit.

It then follows the body's own positions over the next 30 years (`helio()` in `index.html`) and records the largest distance from the body to that fixed ellipse, as an angle seen from the Sun. It does this for start dates 1800, 1820, … 2020.

A body passes if that angle stays within the limit (0.3°) from every start date. Long-period comets, with periods over 200 years, are left out whatever they measure.

It runs the app's own code from `index.html` and `data/sb-orbits.js`, prints every body with its result, and checks the list `OUTLINED` in `index.html` against the rule. After a change to the orbits, run it again and update `OUTLINED` if they differ.

## Usage

- Node.js 18 or later.
- `node drift.js [limit in degrees]`, from this folder. The default limit is 0.3. It takes about a minute.
