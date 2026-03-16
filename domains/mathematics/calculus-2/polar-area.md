---
id: polar-area
title: Area in Polar Coordinates
domain: mathematics
course: calculus-2
prerequisites:
  - id: polar-coordinates
    type: hard
  - id: polar-graphs
    type: hard
  - id: fundamental-theorem-of-calculus-part-2
    type: hard
builds-toward:
  - polar-arc-length
tags: [polar, area, integration]
stage: formal-systems
status: validated
---

# Area in Polar Coordinates

## Core Idea
The area enclosed by a polar curve r = f(theta) from theta = alpha to theta = beta is A = (1/2) integral from alpha to beta of [f(theta)]^2 d(theta). This formula comes from summing infinitesimal circular sectors (each with area (1/2)r^2 d(theta)) rather than rectangles. For area between two polar curves, use (1/2) integral of (r_outer^2 - r_inner^2) d(theta).

## How It's Best Learned
Derive the formula from the area of a circular sector. Practice with cardioids, rose curves, and limacons. Emphasize finding the correct theta bounds by analyzing where the curve starts and ends (or where two curves intersect). Graph the region before integrating.

## Common Misconceptions
- Forgetting the 1/2 factor in the area formula.
- Using wrong theta bounds (especially for curves that are symmetric or have multiple petals).
- Integrating from 0 to 2*pi for all curves (some curves complete in less or more than a full revolution).

## Explainer

In Cartesian coordinates, you compute area by slicing a region into thin vertical strips: each strip has width dx and height f(x), contributing f(x) dx to the total. You then integrate — which is precisely the limit of summing these rectangular strips as they become infinitely thin. Polar coordinates present a different geometry: a curve is described by its radial distance r from the origin as a function of angle θ. Thin vertical rectangles don't fit this setup naturally. Instead, you partition the region using thin **circular sectors** — pie slices sweeping through a small angle dθ.

A circular sector with radius r and central angle dθ has area (1/2)r² dθ. You can derive this from the full circle: a circle of radius r has area πr², and the sector is the fraction dθ/(2π) of the full circle, giving πr² · dθ/(2π) = (1/2)r² dθ. Summing infinitely many such sectors as dθ → 0 gives the integral A = (1/2) ∫_α^β [f(θ)]² dθ. This derivation is the same Riemann sum reasoning used in Cartesian integration — the only change is the shape of the infinitesimal piece (sector instead of rectangle) and the presence of the 1/2 factor, which reflects the sector formula.

Selecting the correct bounds α and β is the critical skill. You must identify the angular range over which the curve sweeps out exactly the region you want to enclose. For a cardioid r = 1 + cos θ, the full curve traces once as θ runs from 0 to 2π. For a rose curve like r = cos(2θ), each petal completes in a quarter-revolution: one petal from θ = −π/4 to π/4, the next from π/4 to 3π/4, and so on. Using 0 to 2π for the rose would trace all four petals but also re-trace some portions, giving incorrect results. A reliable strategy: graph the curve, identify where r = 0 (these are usually natural petal endpoints), and trace one loop carefully before writing the integral.

For the area *between* two polar curves, the formula extends to A = (1/2) ∫_α^β (r_outer² − r_inner²) dθ, where r_outer and r_inner are evaluated at the same angle θ. This parallels the Cartesian formula for area between two functions, with r² in place of f(x) and the 1/2 still accounting for sector geometry. Finding intersection points by setting r_outer = r_inner (and solving for θ) typically determines the bounds when the two curves bound the region together. Watch for intersections that arise from different θ values — polar curves can meet at the pole even when r₁(θ₁) = 0 and r₂(θ₂) = 0 at different angles.
