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

## Explainer

From your earlier study of arc length, you know that the length of a Cartesian curve y = f(x) from x = a to x = b is L = ∫_a^b √(1 + (dy/dx)²) dx. The formula comes from the Pythagorean theorem: each infinitesimal piece of the curve is approximately a hypotenuse with horizontal leg dx and vertical leg dy, so its length is √(dx² + dy²). Parametric curves extend this idea naturally.

When a curve is described parametrically as x = f(t), y = g(t), the same logic applies. An infinitesimal step in t from t to t + dt produces a horizontal displacement dx = f'(t) dt and a vertical displacement dy = g'(t) dt. The length of that infinitesimal segment is √(dx² + dy²) = √((f'(t))² + (g'(t))²) dt. Summing these up over t from α to β gives the **parametric arc length formula**: L = ∫_α^β √((dx/dt)² + (dy/dt)²) dt. You integrate with respect to t, using the derivatives of x and y with respect to t — not x and y themselves.

The connection to the Cartesian formula is exact: if you parametrize a Cartesian curve y = f(x) by x = t, y = f(t), then dx/dt = 1 and dy/dt = f'(t), so the parametric formula gives ∫ √(1 + (f'(t))²) dt, which matches. The parametric version is strictly more general. Consider the unit circle: x = cos(t), y = sin(t), t ∈ [0, 2π]. Then dx/dt = −sin(t), dy/dt = cos(t), and (dx/dt)² + (dy/dt)² = sin²(t) + cos²(t) = 1. So L = ∫_0^{2π} √1 dt = 2π. The Pythagorean identity makes the integrand exactly 1, and the answer is the familiar circumference. This is a clean verification: the formula gives the right answer for a curve whose length you already know.

A crucial subtlety is ensuring the parametrization **traces the curve exactly once**. If t runs from 0 to 4π for the circle above, the formula gives 4π — because the circle is traversed twice. The parameter t is a traversal clock, and the arc length formula measures the total distance traveled by the clock, not the geometric length of the path. When setting up an arc length integral, always check whether the parametrization retraces itself, and restrict to an interval over which the curve is traversed exactly once unless you explicitly want total path length.
