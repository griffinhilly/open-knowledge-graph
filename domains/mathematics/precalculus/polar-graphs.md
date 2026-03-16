---
id: polar-graphs
title: Polar Graphs
domain: mathematics
course: precalculus
prerequisites:
- id: polar-coordinates
  type: hard
- id: graphing-sine-and-cosine
  type: soft
- id: conic-sections-overview
  type: soft
builds-toward:
- polar-area
- polar-arc-length
tags:
- polar
- graphing
- curves
stage: formal-systems
status: validated
---
# Polar Graphs

## Core Idea
Polar equations r = f(theta) produce a rich family of curves: circles, cardioids, limacons, rose curves, lemniscates, and spirals. Graphing them requires thinking radially: for each angle theta, plot the point at distance r = f(theta) from the origin. Symmetry tests (replacing theta with -theta, pi - theta, or theta + pi) and plotting key values help sketch these curves efficiently.

## How It's Best Learned
Start with simple polar equations (r = constant, r = a*cos(theta)) and build to more complex curves. Create tables of (theta, r) values, test for symmetry, and plot point by point. Use technology to verify hand-sketched graphs. Classify curve types by their equation form.

## Common Misconceptions
- Plotting polar graphs on rectangular axes instead of polar axes.
- Forgetting to handle negative r values correctly (plot in the opposite direction).
- Missing petals on rose curves because of incomplete theta range.

## Explainer

In rectangular coordinates, you graph y = f(x) by scanning left to right: for each x-value, the function tells you how high the point is. In **polar coordinates**, which you already know, each point is described by its distance r from the origin and its angle θ from the positive x-axis. A polar equation r = f(θ) does the same thing but radially: scan through angles, and the equation tells you how far out the corresponding point sits.

Start with the simplest case: r = 3 (a constant). For every angle θ, the distance from the origin is 3. Rotating all the way around traces a circle of radius 3. Now consider r = 2cos(θ). From your work with sine and cosine graphs, you know cos(θ) oscillates between −1 and 1. When θ = 0, r = 2 — the point is 2 units to the right. As θ increases to π/2, cos(θ) → 0, so r → 0. When θ = π, r = −2. A **negative r** means plot in the opposite direction from θ: a point at angle π with r = −2 lands at angle 0 with r = +2 — the same starting point. The curve traces a complete circle in the range θ ∈ [0, π], and the second half of the range just retraces it.

The **cardioid** r = 1 + cos(θ) shows the character of polar curves more vividly. When θ = 0, r = 2 (maximum distance); when θ = π, r = 0 (the curve touches the origin). The resulting heart shape has no natural Cartesian description. **Rose curves** like r = cos(nθ) reveal another pattern: the number of petals equals n if n is odd, and 2n if n is even. For r = cos(2θ), you get 4 petals; for r = cos(3θ), you get 3. The petals are produced because cos(nθ) completes n full oscillations as θ sweeps from 0 to π, and negative r values map those oscillations to the opposite direction, filling in the remaining petals.

Symmetry tests make graphing much faster. If replacing θ with −θ leaves the equation unchanged (as in r = cos(θ), since cos is even), the graph is symmetric about the polar axis. If replacing θ with π − θ leaves it unchanged, the graph is symmetric about the vertical axis through the origin. Exploiting symmetry means you only need to plot half the curve and reflect it — then focus your table of (θ, r) values on the portion where the curve has interesting behavior and maximum extent.
