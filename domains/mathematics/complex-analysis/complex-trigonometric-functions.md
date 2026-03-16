---
id: complex-trigonometric-functions
title: Complex Trigonometric Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-exponential-function
  type: hard
builds-toward:
- evaluating-integrals-residues
tags:
- trigonometric-functions
- entire-function
- periodicity
stage: advanced
status: draft
---

# Complex Trigonometric Functions

## Core Idea
Complex sine and cosine are defined by sin(z) = (e^(iz) - e^(-iz))/(2i) and cos(z) = (e^(iz) + e^(-iz))/2. They are entire, periodic with period 2π (on the real axis), but unlike their real counterparts, they grow exponentially in the imaginary direction: |sin(iy)| = sinh(y) → ∞ as |y| → ∞.

## Explainer

From your study of the complex exponential, you know Euler's formula: e^(iθ) = cos(θ) + i·sin(θ) for real θ. This gives a beautiful pair of identities: adding e^(iθ) and e^(−iθ) gives 2cos(θ), and subtracting gives 2i·sin(θ). The **complex trigonometric functions** simply promote these identities to a definition: for any complex number z, declare cos(z) = (e^(iz) + e^(−iz))/2 and sin(z) = (e^(iz) − e^(−iz))/(2i). This is not an extension by guesswork — it is the only definition consistent with the complex exponential and the familiar real values.

Because e^z is entire (analytic everywhere in ℂ), and the definitions are just linear combinations of entire functions, sin(z) and cos(z) are **entire functions** — no singularities anywhere in the complex plane. All the algebraic identities from real trigonometry carry over: sin²(z) + cos²(z) = 1, the addition formulas, the derivative formulas (d/dz sin(z) = cos(z)), and periodicity with period 2π. So far, complex trig feels like a smooth generalization.

The surprise comes when you plug in purely imaginary values. Set z = iy for real y. Then sin(iy) = (e^(i·iy) − e^(−i·iy))/(2i) = (e^(−y) − e^(y))/(2i) = i·(e^y − e^(−y))/2 = i·sinh(y). So |sin(iy)| = sinh(y), which grows exponentially as |y| increases. This is completely unlike real sine, which is forever bounded between −1 and 1. The complex sine function is **unbounded** — you can make |sin(z)| as large as you like by moving z far enough into the imaginary direction. This exposes a fundamental difference: boundedness is not preserved when you extend real functions to the complex plane.

This unboundedness is not a pathology; it is a consequence of how exponentials behave in the complex plane, and it has real consequences. In complex analysis, Liouville's theorem states that the only bounded entire functions are constants — so the fact that sin(z) is entire and unbounded is perfectly consistent. When you later evaluate integrals using residues, the behavior of trig functions along contours in the complex plane (where z has large imaginary part) determines whether certain integrals converge or diverge. Understanding that complex trig functions grow exponentially off the real axis is essential for choosing the right contour in those calculations.
