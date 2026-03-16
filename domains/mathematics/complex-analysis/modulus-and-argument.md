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

## Explainer

From the complex plane, you know that a complex number z = x + iy corresponds to a point (x, y) in the plane. Points in the plane have two natural coordinate systems: Cartesian (x, y) and polar (r, θ). The **modulus** |z| = √(x² + y²) is the polar radius r — the straight-line distance from the origin to z, given by the Pythagorean theorem applied to the right triangle with legs x and y. The **argument** arg(z) = θ is the polar angle — the angle the ray from the origin to z makes with the positive real axis, measured counterclockwise.

Converting between the two representations uses the same trigonometry as polar coordinates. Given z = x + iy: r = √(x² + y²) and θ = arctan(y/x) (adjusted for the correct quadrant using the signs of x and y). Going back: x = r cos θ and y = r sin θ, so z = r(cos θ + i sin θ). This is the **polar form** of a complex number. It sets the stage for Euler's formula e^(iθ) = cos θ + i sin θ, which lets you write z = re^(iθ) — the **exponential form** that makes multiplication and powers of complex numbers especially elegant.

The geometric payoff from polar form appears most clearly when multiplying. If z₁ = r₁e^(iθ₁) and z₂ = r₂e^(iθ₂), then z₁z₂ = r₁r₂ e^(i(θ₁+θ₂)). Multiplication **scales** by the moduli and **rotates** by the arguments. This is why complex multiplication has such clean geometry: multiplying by i (which has modulus 1 and argument π/2) rotates any complex number by 90°, which is exactly why i² = −1 — two 90° rotations land you at 180°, corresponding to multiplication by −1 on the real line.

The **multi-valued nature** of the argument is a genuine subtlety. Any angle θ and θ + 2π point in the same direction, so arg(z) is determined only up to integer multiples of 2π. The **principal argument** Arg(z) is the unique value in the interval (−π, π]. Choosing a consistent range for the argument is called choosing a **branch**, and this choice becomes critical in complex analysis when defining logarithms (log z = ln|z| + i·arg(z)) and roots — operations that are multi-valued precisely because the argument is multi-valued.
