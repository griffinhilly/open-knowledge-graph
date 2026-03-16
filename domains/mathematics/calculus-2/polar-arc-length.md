---
id: polar-arc-length
title: Arc Length in Polar Coordinates
domain: mathematics
course: calculus-2
prerequisites:
  - id: polar-area
    type: soft
  - id: arc-length-parametric
    type: hard
  - id: polar-coordinates
    type: hard
builds-toward: []
tags: [polar, arc-length, integration]
stage: formal-systems
status: validated
---

# Arc Length in Polar Coordinates

## Core Idea
The arc length of a polar curve r = f(theta) from theta = alpha to theta = beta is L = integral from alpha to beta of sqrt(r^2 + (dr/d(theta))^2) d(theta). This formula is derived from the parametric arc length formula by substituting x = r cos(theta) and y = r sin(theta). The r^2 term (not just (dr/d(theta))^2) accounts for the circular component of motion.

## How It's Best Learned
Derive from the parametric arc length formula using x = r*cos(theta), y = r*sin(theta). Practice with circles (r = constant) to verify. Apply to cardioids and spirals. Emphasize that most polar arc length integrals do not simplify to closed form.

## Common Misconceptions
- Forgetting the r^2 term inside the square root (arc length is not just integral of dr/d(theta)).
- Confusing the polar arc length formula with the polar area formula.
- Using x-based arc length formula instead of the polar-specific version.

## Explainer

From arc length in parametric form, you know the formula L = ∫√((dx/dt)² + (dy/dt)²) dt. Polar coordinates are a special case of parametric curves: a polar curve r = f(θ) can be written parametrically as x(θ) = r·cos θ and y(θ) = r·sin θ. The arc length formula in polar coordinates is derived by substituting these into the parametric formula and simplifying. Computing dx/dθ = (dr/dθ)cos θ − r sin θ and dy/dθ = (dr/dθ)sin θ + r cos θ, then squaring and adding: (dx/dθ)² + (dy/dθ)² = (dr/dθ)² + r². The resulting **polar arc length formula** is L = ∫√(r² + (dr/dθ)²) dθ.

The r² term inside the square root is the piece that surprises students. Why isn't arc length just ∫|dr/dθ| dθ, which measures how fast the radius changes? Because motion in polar coordinates has two components: radial motion (the radius growing or shrinking) and angular motion (the point sweeping around the origin). Even if dr/dθ = 0 — meaning the radius is constant — a point tracing a circle of radius r still covers actual distance as θ increases. That distance is r per radian, captured by the r² term. The formula accounts for both components simultaneously.

As a sanity check, try a circle of constant radius R: r = R, so dr/dθ = 0. The formula gives L = ∫₀^{2π} √(R² + 0) dθ = 2πR. Correct — the circumference of a circle of radius R. For a more interesting case, consider the spiral r = θ from θ = 0 to θ = 2π: L = ∫₀^{2π} √(θ² + 1) dθ, which does not simplify to a clean closed form and must be evaluated numerically. This is typical — most polar arc length integrals, including those for cardioids (r = 1 + cos θ) and limaçons, require either a trigonometric identity to simplify or numerical integration.

The key skill is distinguishing this formula from the polar area formula A = ½∫r² dθ. Both involve integrating in θ and both involve r², but they compute fundamentally different things. Area is an accumulation of infinitesimal sector slices (proportional to r²); arc length is an accumulation of infinitesimal distances (the square root of r² plus the radial rate of change). When you see a polar integral, always identify first whether the problem asks for area or arc length — the setup is entirely different even though both are written as single integrals from α to β.


