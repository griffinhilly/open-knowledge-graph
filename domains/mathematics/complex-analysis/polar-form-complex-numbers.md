---
id: polar-form-complex-numbers
title: Polar Form of Complex Numbers
domain: mathematics
course: complex-analysis
prerequisites:
- id: modulus-and-argument
  type: hard
- id: trigonometric-ratios-review
  type: soft
builds-toward:
- complex-exponential-form
- de-moivres-theorem
tags:
- complex-numbers
- polar-coordinates
- trigonometry
stage: advanced
status: draft
---

# Polar Form of Complex Numbers

## Core Idea
Any complex number z can be written as z = r(cos θ + i sin θ) = r cis θ, where r = |z| and θ = arg(z). This polar form makes multiplication and division geometrically transparent: to multiply, multiply moduli and add arguments; to divide, divide moduli and subtract arguments.

## How It's Best Learned
Start with z = 1 + i, find its modulus and argument, and verify the polar form. Practice multiplying two complex numbers in polar form (e.g., 2e^(iπ/4) · 3e^(iπ/3)) and visualize the result. Compare to Cartesian multiplication to see the simplification.

## Common Misconceptions
Thinking polar form is harder to compute with; it is actually easier for multiplication and division. Forgetting that cos and sin must be in radians when computing the argument.

## Explainer

You already know that a complex number has a **modulus** r = |z| (its distance from the origin in the complex plane) and an **argument** θ = arg(z) (the angle it makes with the positive real axis). The polar form z = r(cos θ + i sin θ) is simply the Cartesian coordinate conversion you know from trigonometry, applied to the complex plane: the real part is r cos θ and the imaginary part is r sin θ. Every complex number lives somewhere in the plane, and polar form describes that location using distance and direction instead of horizontal and vertical offsets.

The power of polar form is revealed in **multiplication**. In Cartesian form, multiplying (a + bi)(c + di) requires expanding and simplifying — straightforward but mechanical. In polar form, the result is geometric: multiplying z₁ = r₁(cos θ₁ + i sin θ₁) by z₂ = r₂(cos θ₂ + i sin θ₂) gives z₁z₂ = r₁r₂(cos(θ₁ + θ₂) + i sin(θ₁ + θ₂)). The moduli multiply and the arguments add. In the complex plane, this is a stretch by factor r₂ followed by a rotation by θ₂. Division does the reverse: divide moduli and subtract arguments. These rules follow directly from the angle addition formulas for cosine and sine — formulas you know from trigonometry — applied to the product.

To convert a specific number: start with z = 1 + i. Its modulus is √(1² + 1²) = √2 and its argument is arctan(1/1) = π/4. So z = √2 (cos(π/4) + i sin(π/4)). To multiply z² = (√2)²(cos(π/2) + i sin(π/2)) = 2(0 + i) = 2i. The same calculation in Cartesian form gives (1+i)² = 1 + 2i + i² = 2i — same answer, but the polar route gives geometric insight: squaring a complex number squares its modulus and doubles its argument. This geometric interpretation — that multiplication acts on the complex plane as scaling and rotation — is the key idea polar form unlocks, and it leads directly to De Moivre's theorem and the exponential form e^(iθ) that unifies complex numbers and trigonometry.
