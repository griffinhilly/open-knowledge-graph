---
id: arc-length-parametric
title: Arc Length of Parametric Curves
domain: mathematics
course: calculus-2
prerequisites:
  - id: parametric-curves-calculus
    type: hard
  - id: arc-length
    type: hard
builds-toward:
  - polar-arc-length
tags: [parametric, arc-length, integration]
stage: formal-systems
status: validated
---

# Arc Length of Parametric Curves

## Core Idea
The arc length of a parametric curve x = f(t), y = g(t) from t = alpha to t = beta is L = integral from alpha to beta of sqrt((dx/dt)^2 + (dy/dt)^2) dt. This generalizes the Cartesian arc length formula and is often easier to evaluate because parametric representations frequently simplify the integrand. The formula follows from the Pythagorean theorem applied to infinitesimal displacements.

## How It's Best Learned
Derive from the Cartesian formula by substituting parametric expressions. Compute arc length for the circle (x = cos(t), y = sin(t)) to verify the known circumference. Practice with cycloids, ellipses, and other curves where parametric form simplifies the integral.

## Common Misconceptions
- Forgetting to use the derivatives dx/dt and dy/dt (not x and y themselves).
- Using wrong bounds (t bounds, not x bounds).
- Not verifying that the curve is traversed exactly once over the integration interval.
