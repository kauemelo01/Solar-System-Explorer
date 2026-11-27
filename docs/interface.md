[← Documentation index](README.md) · [Project README](https://github.com/kauemelo01/Solar-System-Explorer#readme) · [Open the app](https://kauemelo01.github.io/Solar-System-Explorer/)

# The interface

How Solar System Explorer is laid out and used: the menu, the time bar, the cards, trails, and the settings it remembers. Where every value comes from, and how accurate it is, is in [Sources, methodology and accuracy](sources.md).

## Layout

- **The menu** (left): every control, in folding sections ([The menu](#the-menu)).
- **The object card** (top right): the selected body ([The object card](#the-object-card)), or the selected star, nebula, galaxy or constellation.
- **The time bar** (bottom centre): the date and the speed of time ([The time bar](#the-time-bar)).
- **The camera position card** (bottom right, wide screens only): where the camera is ([The camera position card](#the-camera-position-card)).

On screens at least 1300 px wide, the menu (360 px) runs the full height of the window, the time bar narrows to stay centred beside it, and the camera position card sits to its right. On smaller screens the menu stops above the time bar and the camera position card is hidden; on phones the menu, cards and time bar stack, and the object card is shorter.

**Fullscreen mode**, for classrooms and presentations, hides the menu, the cards and the time bar, leaving only the sky and the solar system: the corner-arrows button at the top of the menu, or `F`; exit with `Esc`, `F` or the **Exit fullscreen** button.

## Start-up

While the app loads, a splash screen shows its name and what it is doing (*Loading…*, *Building the solar system…*, *Drawing the first frame…*, *Loading the sky map (6.9 MB)…*). It disappears once the 3D view has been drawn with the sky map in place ([sky map loading](sources.md#sky-map-loading)), so the first view is complete. It does not wait for the sky map when the *Milky Way & faint stars* layer is off or the map cannot be downloaded, and waits at most 30 seconds after the first frame, after which the map appears whenever it arrives. If the app cannot start, the splash turns into an error message instead of leaving an empty view:

- **When:** before the first frame is drawn, an error stops the app's start-up code; one of its scripts cannot be downloaded; the browser or device cannot show 3D graphics (WebGL); or no frame is drawn within 20 seconds (up to 60 seconds while the page is still downloading, as on a slow connection). Problems after the first frame, or a texture or font that fails to download, do not bring it back.
- **What it shows:** a short explanation and the error itself, with **Reload**, **Reset saved settings and reload** (which clears the settings the app remembers on this device, in case one of them stops it from starting after an update) and a link to report the problem on GitHub, with the error and the browser's name filled in for review before sending.
- Without JavaScript, the page shows a short description of the app and a link to this documentation instead.

## Controls

| Action | How |
|---|---|
| Rotate / zoom | Drag; scroll or pinch |
| Fly to an object | Click its name, or use **Find** (`/`) |
| **Make an object the centre** (hold it still) | Double-click it, pick it under *Reference body*, use the **Hold … still** button on its card, or press `C` for the selected one |
| Look at a star, nebula or galaxy | Click its label to open its card, or type its name in **Find** to turn the view towards it; the card's **✕** goes back to the selected body |
| Go back to the previously selected object | `Backspace` (repeat to go further back; bodies and sky objects alike) |
| Read about an object | Click it ([The object card](#the-object-card)) |

**Keyboard shortcuts** (not while typing in a box):

| Key | Action |
|---|---|
| `/` | Open the menu and put the cursor in **Find** |
| `C` | Hold the selected object still (make it the centre) |
| `Space` | Pause / play |
| `←` `→` | Slower / faster |
| `R` | Reverse time |
| `T` | Turn all trails off, and back to their previous lengths |
| `Backspace` | Go back to the previously selected object |
| `F` | Fullscreen mode on or off (`Esc` also leaves it) |

## The menu

Each section folds and unfolds when its heading is clicked. The arrow button at the top collapses the whole menu, keeping the **Find and fly to** search bar (on phones: **Controls**); the corner-arrows button next to it starts fullscreen mode.

- **Find and fly to…**: type any object's name to point the camera at it (the camera only: the body held still does not change). Stars, nebulae, galaxies and constellations can be found too.
- **Reference body**: the body held still, the centre of the frame: a button for the Sun, each planet and the Moon, or **Hold any other object still…** to type any other.
- **Show**:
  - quick views: **Show everything** or **Planets only**;
  - **Moons**: **Major moons**, **All moons** or **No moons**, or open a planet, *Dwarf planets & candidates* or *Asteroids* and switch moon groups on one at a time (**All** / **None** per group). Switching on a moon of a dwarf planet or asteroid also shows its parent. A planet's moons appear only as you zoom towards it ([When moons appear](#when-moons-appear));
  - **Moon orbit outlines**;
  - **Small bodies**: **Dwarf planets**, **Candidates**, **Asteroids & centaurs**, **Comets**, or **All** / **None**;
  - **Belts**: **Main asteroid belt**, **Hilda asteroids**, **Jupiter trojans**, **Neptune trojans**, **Kuiper belt** (statistical clouds, not catalogued objects; [Belts](sources.md#belts)), or **All** / **None**.
- **Beyond the solar system**: **Milky Way & faint stars**, **Nebulae, clusters & galaxies**, **Bright star names**, **Stars with known planets**, and **Constellations (IAU)** (off by default) with **All 88** or **Zodiac (13)**, **Figures** and **Boundaries** ([constellations](catalogue/constellations.md)).
- **Trails**: a length slider for each group of bodies ([Trails](#trails)).
- **View**: **Labels**, **Distance rings (AU)** (circles at 1, 2, 5, 10, 20, 30, 50 and 100 AU around the body held still, in the ecliptic plane), and framing buttons: **Inner planets** or **Whole system**.
- **Images**:
  - **Realistic surface textures** (on by default): off, every body uses its painted texture, Saturn's rings the painted ring, Earth's clouds are hidden, the surface notes on the cards are hidden, and no map files are downloaded; turning it back on reuses any maps already downloaded ([Surface maps](sources.md#surface-maps));
  - **Sky map detail**: **Auto** (8K on capable devices, otherwise 4K), **4K** or **8K**. Forcing 8K still falls back to 4K if the 8K file fails to load; the 8K option is disabled on devices whose graphics cannot show textures 8192 pixels wide. Each map is downloaded at most once per visit ([Sky map loading](sources.md#sky-map-loading)).

## The time bar

Play / pause, reverse, the speed slider (real time, then 1 hour, 6 hours, 1 day, 1 week, 1 month, 3 months, 1 year, 5, 20 and 100 years per second), the date and time (UTC), a date box to jump to any date, and **Today**.

- **Range:** 1 January 1000 AD to 1 January 3000 AD (UTC, Gregorian calendar). Playing stops at either end, and a date entered outside the range is moved to the nearest end.
- **Outside 1800–2050 AD** the time bar turns amber and shows *Estimated positions* (next to the speed on wide screens, after the clock on phones): positions there are estimates ([Error and drift over time](sources.md#error-and-drift-over-time)).
- The app always opens at the current date and time.

## The object card

Clicking an object, or finding it with *Find*, opens its card:

- its name and type, for example *Moon of Saturn · Norse group · retrograde irregular*;
- the [surface note](sources.md#card-notes), and for a moon outside its fitted range an *Estimated position* note ([Moon orbits](sources.md#moon-orbits));
- **From** the body held still: the distance, in kilometres below 20 million km and in AU above;
- **Light time:** how long light takes to cover that distance;
- **From the Sun**, **Radius** (with ≈ and *est.* for a [placeholder size](sources.md#what-is-not-to-scale)), **Rotation** (dwarf planets, asteroids, centaurs and comets: the spin period the app uses, in minutes, hours or days, or *illustrative* where none is published) and **Orbital period** (in hours, days or years; *retrograde* for moons that orbit backwards). Where a radius, rotation period or orbital period does not come from NASA or JPL, a **source** link after the value opens the paper or record it comes from (for example Uranus's irregular moons' radii, the IAU rotation rates of the bodies turned to their prime meridian, and the orbits of Hiʻiaka, Namaka, Xiangliu, Skamandrios, Queta and Menoetius); a placeholder, which has no source, links instead to the note that explains it (**why est.** for a [placeholder size](sources.md#what-is-not-to-scale), **why** for an illustrative rotation). Which values: [moon sizes](sources.md#moon-sizes), [small bodies](catalogue/small-bodies.md#notes-on-sizes-and-rotation), [moons of dwarf planets and asteroids](catalogue/moons-small-bodies.md#notes);
- links: **Details** (its catalogue entry), **Rings** (for ringed bodies), **JPL** (its JPL Horizons record) or **JPL SBDB** (small bodies), and **NASA** (its NASA Science page, for 139 objects);
- a **Hold … still** button, which makes it the reference body.

On phones the card is shorter: it leaves out the type, the distance from the Sun, the radius, the rotation and the period.

Objects in the sky have their own card: deep-sky objects give their distance, constellation and apparent size; named stars their magnitude and spectral type; stars with planets their distance and number of planets; all three their position (RA and Dec). Constellations give their abbreviation, area, size rank and, for the zodiac, the dates the Sun passes through. Links go to the catalogue entry and SIMBAD, plus the NASA image or the NASA Exoplanet Archive where there is one. The card's **✕** goes back to the selected body.

## The camera position card

On screens at least 1300 px wide, a small card at the bottom right, as tall as the time bar, shows where the camera is:

- **From** the selected object (the one the camera looks at and orbits, named on the card): the camera's distance from it, in metres below 1 km, then in kilometres, megametres (Mm, 1,000 km) and gigametres (Gm, 1 million km) in steps of 1,000, and in AU from 1 AU (149.60 Gm); with two decimals, except for metres.
- **Ecliptic latitude** (−90° to +90°): the camera's angle above or below the plane of the distance rings, which is the ecliptic (the plane of Earth's orbit) through the body held still. At 0° the camera is in that plane and the rings appear as a single horizontal line; positive values are on the side of the ecliptic north pole.
- **Galactic latitude** (*b*, −90° to +90°) of the camera's direction as seen from the selected object: 0° is the plane of the Milky Way's disk, and positive values are on the side of the north galactic pole (in Coma Berenices).
- **How:** the camera's position is taken in the app's J2000 ecliptic frame; for the galactic latitude its direction is turned into J2000 equatorial coordinates and then into galactic coordinates with the standard rotation from the Hipparcos catalogue (ESA 1997, vol. 1, §1.5.3). Checked: a camera towards the galactic centre reads *b* = 0°, and one towards the north galactic pole *b* = +90°; a camera level with the rings reads 0° ecliptic latitude.

The card is hidden on narrower screens, where the time bar takes the width, and in fullscreen mode. It updates several times a second while the view moves.

## Trails

A trail is the path a body has followed **as seen from the body held still**. With the Sun held still, planets trace their orbits; with Earth held still, Mars traces its loops in the sky; and a moon's trail combines its orbit with its planet's path.

- **One slider per group** under *Trails*: planets (and the Sun, when another body is held still), major moons, minor moons, dwarf planets, candidates, asteroids & centaurs, and comets. Each runs from off (far left) through 1 week, 1 month, 3 months, 1 year, 5, 12, 30 and 100 years to 250 years. **Everything** sets them all at once, and reads *Mixed* when they differ. A group with nothing on screen says *None shown*; its slider still works.
- **Defaults:** 30 years for planets and small bodies, 1 year for major moons, off for minor moons.
- **`T`** turns all trails off, and back to the previous lengths.
- **When a trail is drawn:** only for bodies that are shown. A moon's trail appears only when its planet's moons are visible (see below), and is dropped when time runs so fast that the moon would go round more than 15 times a second.
- **Detail:** a trail is sampled about 180 times per orbit and keeps at most 6,000 points (2,000 for minor moons), so a long trail of a fast moon shows only its most recent part. Older parts fade out.

## When moons appear

A planet's moons (their dots, labels and trails) appear as you zoom toward the planet: once its moon system is a few dozen pixels across on screen. They also appear when the planet or one of its moons is selected or held still.

## Saved settings

The app remembers its settings on the device (in the browser's local storage): the body held still, the speed, trail lengths, labels, distance rings and moon orbit outlines, which moons, small bodies, belts and sky layers are shown (constellation options included), realistic surface textures, the sky map size and whether the menu is collapsed. The date is not saved: the app always opens at the current date and time.
