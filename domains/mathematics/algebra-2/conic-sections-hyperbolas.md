---
id: conic-sections-hyperbolas
title: 'Conic Sections: Hyperbolas'
domain: mathematics
course: algebra-2
prerequisites:
- id: conic-sections-ellipses
  type: hard
- id: rational-functions-and-asymptotes
  type: soft
builds-toward:
- conic-sections-overview
tags:
- conics
- hyperbolas
- foci
- asymptotes
- transverse-axis
stage: abstract-reasoning
status: validated
---
# Conic Sections: Hyperbolas

## Core Idea
A hyperbola is the set of all points where the absolute difference of distances to two foci is constant. Standard forms: (x-h)^2/a^2 - (y-k)^2/b^2 = 1 (horizontal transverse axis) or (y-k)^2/a^2 - (x-h)^2/b^2 = 1 (vertical transverse axis). Unlike ellipses, c^2 = a^2 + b^2. The hyperbola has two branches and two asymptotes that guide the shape: y - k = +/-(b/a)(x - h) for horizontal, y - k = +/-(a/b)(x - h) for vertical.

## How It's Best Learned
Contrast with ellipses: sum of distances (ellipse) vs. difference of distances (hyperbola). Identify center, vertices (a units from center on the transverse axis), and foci (c units from center). Draw the "box" formed by a and b to find asymptotes. Graph by sketching asymptotes first, then drawing the two branches approaching them. Practice converting from general form.

## Common Misconceptions
- Confusing the c relationship: ellipses use c^2 = a^2 - b^2, hyperbolas use c^2 = a^2 + b^2.
- Getting asymptote slopes wrong (b/a for horizontal, a/b for vertical).
- Thinking a must always be greater than b (for hyperbolas, a is simply the denominator under the positive term).
- Drawing the branches crossing the asymptotes (they approach but never cross).

## Explainer

You learned that an **ellipse** is defined by a constant sum of distances to two foci: for any point on the ellipse, d₁ + d₂ = 2a. A **hyperbola** swaps sum for difference: |d₁ − d₂| = 2a, where a is the semi-transverse axis length. This single change — from sum to absolute difference — produces a dramatically different shape. Where an ellipse is a closed oval, a hyperbola splits into two separate **branches** opening away from each other. The two foci are now outside the curve rather than inside it, and the curve stretches outward toward infinity rather than closing back on itself.

The standard form (x−h)²/a² − (y−k)²/b² = 1 describes a hyperbola centered at (h, k) with a **horizontal transverse axis** — the two vertices are a units left and right of center, and the branches open left and right. Flip the subtraction to (y−k)²/a² − (x−h)²/b² = 1 and the transverse axis is vertical, with branches opening up and down. In either case, a is always the denominator under the **positive** term, regardless of whether a > b or not. The foci lie c units from center along the transverse axis, where c² = a² + b². Compare this to the ellipse formula c² = a² − b²: for ellipses the foci are inside (c < a), so subtracting b² shrinks c; for hyperbolas the foci are outside (c > a), so adding b² enlarges c.

The most distinctive feature of a hyperbola is its pair of **asymptotes** — lines the branches approach but never touch. The trick to finding them is to draw a rectangle: go a units from center along the transverse axis and b units perpendicular to it, forming a box. The asymptotes are the diagonals of that box, passing through the center. For a horizontal hyperbola, those slopes are ±b/a; for a vertical one, ±a/b. This "box method" also gives you a reliable graphing strategy: draw the box, draw the asymptotes through its corners, then sketch two branches curving away from center and hugging the asymptotes as they extend outward.

Your background in rational functions and asymptotes from the prerequisite makes the asymptotic behavior intuitive. As x gets very large in (x²/a²) − (y²/b²) = 1, solving for y gives y ≈ ±(b/a)x — the curve looks more and more like its asymptote lines at large distances. Near the vertices the branches curve away sharply; far from the center they appear almost straight. This interplay between the local behavior (curved branches near vertices) and global behavior (approaching straight lines at infinity) is exactly the pattern you studied in rational functions, now appearing geometrically as a conic section.
