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

## Questions

```yaml
- question: "A student computes the arc length of r = 5 (a circle of radius 5) from θ = 0 to θ = 2π using L = ∫₀^{2π} |dr/dθ| dθ. What result do they get, and why is it wrong?"
  type: multiple-choice
  options:
    - "They get L = 0, because dr/dθ = 0 for a constant radius — the formula misses the angular component of motion entirely."
    - "They get L = 10π, which is the correct circumference of the circle."
    - "They get L = 5, because the radius is 5 regardless of θ."
    - "They get L = 2π, from integrating 1 dθ without the radius factor."
  answer: 0
  explanation: "Since r = 5 is constant, dr/dθ = 0 everywhere, so ∫|dr/dθ| dθ = 0. But a point sweeping around a circle of radius 5 clearly travels a distance of 10π — the circumference. The error is treating arc length as though only radial motion (change in r) contributes. In polar coordinates, angular motion also covers distance: even with constant r, moving through angle dθ covers a distance of r dθ. The r² term in the correct formula √(r² + (dr/dθ)²) captures this angular component."

- question: "Which feature of the polar arc length formula L = ∫√(r² + (dr/dθ)²) dθ most distinguishes it from the naive formula L = ∫|dr/dθ| dθ?"
  type: multiple-choice
  options:
    - "The polar formula uses θ as the integration variable rather than x."
    - "The polar formula is derived from the Pythagorean theorem, while the naive formula is not."
    - "Even when dr/dθ = 0 (constant radius), the polar formula correctly yields nonzero arc length because angular motion contributes actual distance."
    - "The polar formula involves a square root, which accounts for the curvature of the coordinate system."
  answer: 2
  explanation: "The r² term captures the distance covered by angular motion. When r is constant, dr/dθ = 0, and the formula gives ∫√(r²) dθ = ∫r dθ = r·Δθ — the standard arc length for a circular arc. The naive formula gives zero in this case, which is clearly wrong. The key insight is that polar motion has two components: radial (dr/dθ) and angular (r), and the formula accounts for both."

- question: "The polar arc length formula L = ∫√(r² + (dr/dθ)²) dθ is derived by treating the polar curve as a parametric curve and substituting x = r cos θ, y = r sin θ into the parametric arc length formula."
  type: true-false
  answer: true
  explanation: "This is exactly how the formula is derived. Setting x(θ) = r cos θ and y(θ) = r sin θ, computing dx/dθ and dy/dθ, then squaring and adding yields (dx/dθ)² + (dy/dθ)² = (dr/dθ)² + r². The polar arc length formula follows directly from the parametric formula L = ∫√((dx/dθ)² + (dy/dθ)²) dθ."

- question: "The polar arc length formula A = ½∫r² dθ and the arc length formula L = ∫√(r² + (dr/dθ)²) dθ compute different quantities, but are equivalent when dr/dθ is small."
  type: true-false
  answer: false
  explanation: "These formulas compute fundamentally different things — area and arc length — and no assumption about dr/dθ makes them equivalent. The area formula accumulates infinitesimal sector slices (proportional to r²); the arc length formula accumulates infinitesimal distances (involving r² and (dr/dθ)²). The similarity in notation (both integrate in θ, both involve r²) is superficial. Always identify which quantity is being requested before setting up the integral."

- question: "Why does the polar arc length formula include an r² term inside the square root, even for a curve where dr/dθ = 0 throughout?"
  type: short-answer
  answer: "Because even when the radius isn't changing, a point moving along the curve is still sweeping through angle θ, covering actual distance proportional to r per radian. The r² term captures this angular component of motion. Without it, a circle (constant r, dr/dθ = 0 everywhere) would be computed to have zero arc length — clearly wrong. The formula accounts for both radial motion (dr/dθ) and angular motion (r) simultaneously."
  explanation: "This is the central insight of the polar arc length formula. Motion in polar coordinates is inherently two-dimensional: you can move radially (changing r) or angularly (sweeping θ), and both contribute to arc length. The parametric derivation makes this explicit: (dx/dθ)² + (dy/dθ)² = (dr/dθ)² + r², so both components always appear."
```

## Explainer

From arc length in parametric form, you know the formula L = ∫√((dx/dt)² + (dy/dt)²) dt. Polar coordinates are a special case of parametric curves: a polar curve r = f(θ) can be written parametrically as x(θ) = r·cos θ and y(θ) = r·sin θ. The arc length formula in polar coordinates is derived by substituting these into the parametric formula and simplifying. Computing dx/dθ = (dr/dθ)cos θ − r sin θ and dy/dθ = (dr/dθ)sin θ + r cos θ, then squaring and adding: (dx/dθ)² + (dy/dθ)² = (dr/dθ)² + r². The resulting **polar arc length formula** is L = ∫√(r² + (dr/dθ)²) dθ.

The r² term inside the square root is the piece that surprises students. Why isn't arc length just ∫|dr/dθ| dθ, which measures how fast the radius changes? Because motion in polar coordinates has two components: radial motion (the radius growing or shrinking) and angular motion (the point sweeping around the origin). Even if dr/dθ = 0 — meaning the radius is constant — a point tracing a circle of radius r still covers actual distance as θ increases. That distance is r per radian, captured by the r² term. The formula accounts for both components simultaneously.

As a sanity check, try a circle of constant radius R: r = R, so dr/dθ = 0. The formula gives L = ∫₀^{2π} √(R² + 0) dθ = 2πR. Correct — the circumference of a circle of radius R. For a more interesting case, consider the spiral r = θ from θ = 0 to θ = 2π: L = ∫₀^{2π} √(θ² + 1) dθ, which does not simplify to a clean closed form and must be evaluated numerically. This is typical — most polar arc length integrals, including those for cardioids (r = 1 + cos θ) and limaçons, require either a trigonometric identity to simplify or numerical integration.

The key skill is distinguishing this formula from the polar area formula A = ½∫r² dθ. Both involve integrating in θ and both involve r², but they compute fundamentally different things. Area is an accumulation of infinitesimal sector slices (proportional to r²); arc length is an accumulation of infinitesimal distances (the square root of r² plus the radial rate of change). When you see a polar integral, always identify first whether the problem asks for area or arc length — the setup is entirely different even though both are written as single integrals from α to β.


