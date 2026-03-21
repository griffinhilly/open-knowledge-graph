---
id: modulus-and-argument
title: Modulus and Argument of Complex Numbers
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-plane
  type: hard
builds-toward:
- polar-form-complex-numbers
- complex-exponential-form
tags:
- complex-numbers
- polar-coordinates
- geometry
stage: advanced
status: draft
---

# Modulus and Argument of Complex Numbers

## Core Idea
The modulus (absolute value) |z| = √(x² + y²) measures the distance from the origin, while the argument arg(z) = θ is the angle from the positive real axis. These polar coordinates (r, θ) capture the magnitude and direction of a complex number and are essential for understanding complex multiplication geometrically.

## How It's Best Learned
Use polar plotting to visualize modulus as radius and argument as angle. Practice converting between (x, y) and (r, θ) forms. Notice how argument is multi-valued: arg(z) and arg(z) + 2π represent the same point.

## Common Misconceptions
Assuming argument has a unique value; it is defined only up to multiples of 2π. Confusing |z₁z₂| = |z₁||z₂| with arg(z₁z₂) = arg(z₁) + arg(z₂) when arguments wrap around.

## Questions

```yaml
- question: "The complex number z = 1 + i is multiplied by i. What is the geometric effect on z?"
  type: multiple-choice
  options:
    - "z is scaled by a factor of √2 with no change in direction"
    - "z is rotated 90° counterclockwise about the origin, with its modulus unchanged"
    - "z is reflected across the imaginary axis"
    - "z is rotated 45° counterclockwise, since i is at 45° from the real axis"
  answer: 1
  explanation: "Multiplication by a complex number with modulus r and argument θ scales by r and rotates by θ. The number i has modulus 1 and argument π/2 (it lies on the positive imaginary axis, 90° from the real axis). Multiplying any complex number by i therefore scales it by 1 (no change in size) and rotates it by π/2 = 90° counterclockwise. For z = 1 + i: z has modulus √2 and argument π/4. After multiplying by i, the modulus stays √2 and the argument becomes π/4 + π/2 = 3π/4, which corresponds to the point −1 + i. The common error in option D is confusing the argument of i (90°) with the argument of z (45°) — multiplication adds the arguments."

- question: "What is the principal argument Arg(z) of z = −√3 + i?"
  type: multiple-choice
  options:
    - "−π/6"
    - "π/3"
    - "5π/6"
    - "−5π/6"
  answer: 2
  explanation: "The point −√3 + i lies in the second quadrant (negative real part, positive imaginary part). Its modulus is √(3 + 1) = 2. The reference angle is arctan(1/√3) = π/6. Since the point is in the second quadrant, the argument is π − π/6 = 5π/6. The principal argument Arg(z) is the unique value in (−π, π], so 5π/6 is correct — it lies in (0, π), well within the principal range. Option A applies the formula arctan(y/x) without adjusting for quadrant. Option D gives a negative angle appropriate for the third quadrant."

- question: "The argument of a product of two complex numbers equals the sum of their individual arguments — but this sum may need to be adjusted by adding or subtracting 2π to bring it within the chosen standard range."
  type: true-false
  answer: true
  explanation: "The rule arg(z₁z₂) = arg(z₁) + arg(z₂) holds exactly, but 'argument' here is multi-valued (defined only up to multiples of 2π). If we use principal arguments Arg(z) ∈ (−π, π], the sum Arg(z₁) + Arg(z₂) may fall outside (−π, π]. For example, Arg(−1 + 0i) = π and Arg(−1 + 0i) = π, but (−1)(−1) = 1 has Arg = 0, not 2π. So we must reduce: π + π = 2π ≡ 0 (mod 2π). The adjustment is real and necessary — this is exactly why the multi-valuedness of arg matters."

- question: "Every complex number has a unique argument, just as every positive real number has a unique absolute value."
  type: true-false
  answer: false
  explanation: "The argument is defined only up to integer multiples of 2π — any angle θ and θ + 2πk (for integer k) point in the same direction and represent the same complex number. The principal argument Arg(z) ∈ (−π, π] is a unique representative chosen by convention, but the argument itself is inherently multi-valued. This multi-valuedness has serious consequences in complex analysis: when defining log z = ln|z| + i·arg(z), the multi-valuedness of arg makes log itself multi-valued, requiring a choice of 'branch' to work with a single-valued function. This is distinct from the absolute value |z|, which genuinely has a unique value for each z."

- question: "Why does multiplying a complex number by i rotate it by 90°, and how does this explain why i² = −1?"
  type: short-answer
  answer: "The number i sits on the unit circle at argument π/2 (90° counterclockwise from the positive real axis) and has modulus 1. When you multiply any complex number z by i, the moduli multiply (1 × |z| = |z|, so the distance from the origin is unchanged) and the arguments add (arg(z) + π/2). Multiplication by i is therefore a 90° counterclockwise rotation. Applying this twice — computing i² — rotates by 90° + 90° = 180°. A 180° rotation maps any point to its antipodal point on the opposite side of the origin. For the real number 1 (which lies at argument 0 on the unit circle), a 180° rotation lands at −1. So i × i = i² = −1. This is not a coincidence or an arbitrary rule — it is the geometric content of what it means to rotate the complex plane by 90° twice."
```

## Explainer

From the complex plane, you know that a complex number z = x + iy corresponds to a point (x, y) in the plane. Points in the plane have two natural coordinate systems: Cartesian (x, y) and polar (r, θ). The **modulus** |z| = √(x² + y²) is the polar radius r — the straight-line distance from the origin to z, given by the Pythagorean theorem applied to the right triangle with legs x and y. The **argument** arg(z) = θ is the polar angle — the angle the ray from the origin to z makes with the positive real axis, measured counterclockwise.

Converting between the two representations uses the same trigonometry as polar coordinates. Given z = x + iy: r = √(x² + y²) and θ = arctan(y/x) (adjusted for the correct quadrant using the signs of x and y). Going back: x = r cos θ and y = r sin θ, so z = r(cos θ + i sin θ). This is the **polar form** of a complex number. It sets the stage for Euler's formula e^(iθ) = cos θ + i sin θ, which lets you write z = re^(iθ) — the **exponential form** that makes multiplication and powers of complex numbers especially elegant.

The geometric payoff from polar form appears most clearly when multiplying. If z₁ = r₁e^(iθ₁) and z₂ = r₂e^(iθ₂), then z₁z₂ = r₁r₂ e^(i(θ₁+θ₂)). Multiplication **scales** by the moduli and **rotates** by the arguments. This is why complex multiplication has such clean geometry: multiplying by i (which has modulus 1 and argument π/2) rotates any complex number by 90°, which is exactly why i² = −1 — two 90° rotations land you at 180°, corresponding to multiplication by −1 on the real line.

The **multi-valued nature** of the argument is a genuine subtlety. Any angle θ and θ + 2π point in the same direction, so arg(z) is determined only up to integer multiples of 2π. The **principal argument** Arg(z) is the unique value in the interval (−π, π]. Choosing a consistent range for the argument is called choosing a **branch**, and this choice becomes critical in complex analysis when defining logarithms (log z = ln|z| + i·arg(z)) and roots — operations that are multi-valued precisely because the argument is multi-valued.
