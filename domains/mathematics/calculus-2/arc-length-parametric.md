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

## Questions

```yaml
- question: "A student computes the arc length of the parametric curve x = t², y = t³ over t ∈ [1, 3] by setting up ∫₁³ √(x² + y²) dt. What is wrong with this setup?"
  type: multiple-choice
  options:
    - "The bounds should be x = 1 to x = 9, not t = 1 to t = 3"
    - "The integrand should use the derivatives dx/dt and dy/dt, not the functions x and y themselves"
    - "The formula should use x² + y² without the square root"
    - "The formula is correct but only applies when the curve does not self-intersect"
  answer: 1
  explanation: "The parametric arc length formula is L = ∫ √((dx/dt)² + (dy/dt)²) dt. The integrand is built from the derivatives of x and y with respect to t, not the values of x and y. Here dx/dt = 2t and dy/dt = 3t², so the correct integrand is √(4t² + 9t⁴). Using x and y directly (√(t⁴ + t⁶)) has no geometric meaning in this context — it does not measure the speed of the parametric path."

- question: "For the unit circle parametrized as x = cos(t), y = sin(t), what happens if you integrate the arc length formula from t = 0 to t = 4π?"
  type: multiple-choice
  options:
    - "You get the circumference 2π, because the circle's total length is fixed regardless of how t is parametrized"
    - "You get 4π, because the circle is traversed twice and the formula measures total distance traveled by the parameter"
    - "You get an error — the formula requires that the curve be traversed exactly once, so the integral is undefined"
    - "You get π, because the formula accounts for retracing and divides by the number of traversals"
  answer: 1
  explanation: "The arc length formula measures total path length — the total distance traveled as t moves from the lower to upper bound. If the circle is traversed twice (t from 0 to 4π), the formula gives 4π, not 2π. The parameter t is a traversal clock; the formula doesn't know or care whether you've retraced the same geometric path. This is why checking that a parametrization traces the curve exactly once is essential when you want the geometric length of the curve, not the total path length."

- question: "The parametric arc length formula L = ∫ √((dx/dt)² + (dy/dt)²) dt reduces exactly to the Cartesian arc length formula when the curve is parametrized as x = t, y = f(t)."
  type: true-false
  answer: true
  explanation: "With x = t, y = f(t), we get dx/dt = 1 and dy/dt = f'(t). Substituting into the parametric formula gives ∫ √(1 + (f'(t))²) dt, which is exactly the Cartesian arc length formula ∫ √(1 + (dy/dx)²) dx (with t playing the role of x). This confirms that the parametric formula is a strict generalization: every Cartesian curve can be viewed as a special case of a parametric curve, but parametric curves can represent many things (like circles) that cannot be expressed as single-valued y = f(x)."

- question: "The arc length of a parametric curve always equals the straight-line distance between its starting and ending points."
  type: true-false
  answer: false
  explanation: "Arc length is the total length along the curve, which is always greater than or equal to the straight-line distance between endpoints (by the triangle inequality), with equality only when the curve is a straight line segment. A circle, for example, has endpoints at the same point (after a full traversal), so the straight-line distance is zero, but the arc length is 2πr. A winding or looping curve can have endpoints very close together while having enormous arc length."

- question: "Why must you verify that a parametric curve is traversed exactly once over the integration interval when computing arc length? What goes wrong if the curve retraces itself?"
  type: short-answer
  answer: "The arc length formula measures total distance traveled by the parameter, not the geometric length of the curve's image. If the parametrization retraces a portion of the curve, that portion gets counted multiple times in the integral. For example, integrating the unit circle from 0 to 4π gives 4π because the circle is traversed twice, even though the geometric circumference is only 2π. To get the geometric arc length, you must restrict to an interval over which each point on the curve is hit exactly once."
  explanation: "The parameter t is a clock that records how the curve is traversed, not a label for position on the curve. Two different values of t can produce the same point (x, y) if the curve crosses or retraces itself. The integral sums up infinitesimal path lengths dt at each moment in time — it doesn't subtract anything when the path revisits a location. This distinction matters practically: always sketch or reason about the traversal before setting up bounds."
```

## Explainer

From your earlier study of arc length, you know that the length of a Cartesian curve y = f(x) from x = a to x = b is L = ∫_a^b √(1 + (dy/dx)²) dx. The formula comes from the Pythagorean theorem: each infinitesimal piece of the curve is approximately a hypotenuse with horizontal leg dx and vertical leg dy, so its length is √(dx² + dy²). Parametric curves extend this idea naturally.

When a curve is described parametrically as x = f(t), y = g(t), the same logic applies. An infinitesimal step in t from t to t + dt produces a horizontal displacement dx = f'(t) dt and a vertical displacement dy = g'(t) dt. The length of that infinitesimal segment is √(dx² + dy²) = √((f'(t))² + (g'(t))²) dt. Summing these up over t from α to β gives the **parametric arc length formula**: L = ∫_α^β √((dx/dt)² + (dy/dt)²) dt. You integrate with respect to t, using the derivatives of x and y with respect to t — not x and y themselves.

The connection to the Cartesian formula is exact: if you parametrize a Cartesian curve y = f(x) by x = t, y = f(t), then dx/dt = 1 and dy/dt = f'(t), so the parametric formula gives ∫ √(1 + (f'(t))²) dt, which matches. The parametric version is strictly more general. Consider the unit circle: x = cos(t), y = sin(t), t ∈ [0, 2π]. Then dx/dt = −sin(t), dy/dt = cos(t), and (dx/dt)² + (dy/dt)² = sin²(t) + cos²(t) = 1. So L = ∫_0^{2π} √1 dt = 2π. The Pythagorean identity makes the integrand exactly 1, and the answer is the familiar circumference. This is a clean verification: the formula gives the right answer for a curve whose length you already know.

A crucial subtlety is ensuring the parametrization **traces the curve exactly once**. If t runs from 0 to 4π for the circle above, the formula gives 4π — because the circle is traversed twice. The parameter t is a traversal clock, and the arc length formula measures the total distance traveled by the clock, not the geometric length of the path. When setting up an arc length integral, always check whether the parametrization retraces itself, and restrict to an interval over which the curve is traversed exactly once unless you explicitly want total path length.
