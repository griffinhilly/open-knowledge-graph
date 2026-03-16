---
id: complex-exponential-form
title: Complex Exponential Form and Euler's Formula
domain: mathematics
course: complex-analysis
prerequisites:
- id: polar-form-complex-numbers
  type: hard
- id: power-series
  type: soft
builds-toward:
- complex-exponential-function
- complex-logarithm-branch-cuts
tags:
- complex-exponentials
- euler-formula
- power-series
stage: advanced
status: draft
---

# Complex Exponential Form and Euler's Formula

## Core Idea
Euler's formula e^(iθ) = cos θ + i sin θ allows us to write z = r e^(iθ) in exponential form. This unifies trigonometry with exponentials and makes complex multiplication simple: z₁z₂ = r₁r₂ e^(i(θ₁+θ₂)). The exponential form is fundamental to all of complex analysis because it extends naturally to complex exponents.

## How It's Best Learned
Verify Euler's formula by expanding e^(iθ) = Σ(iθ)ⁿ/n! and grouping real/imaginary parts. Compute specific examples like e^(iπ) = -1. Use the exponential form to multiply complex numbers and see how arguments add.

## Common Misconceptions
Treating e^(iθ) as purely formal; it represents a real geometric transformation (rotation). Forgetting the 2π periodicity: e^(i(θ+2π)) = e^(iθ).

## Questions

```yaml
- question: "Using Euler's formula, what is e^(iπ/2)?"
  type: multiple-choice
  options:
    - "-1"
    - "i"
    - "-i"
    - "1"
  answer: 1
  explanation: "e^(iπ/2) = cos(π/2) + i sin(π/2) = 0 + i(1) = i. Geometrically, multiplying by e^(iπ/2) rotates a point 90° counterclockwise on the unit circle, mapping 1 to i. The famous identity e^(iπ) = -1 corresponds to a 180° rotation, landing at -1 on the real axis."

- question: "e^(iπ) and e^(i·3π) represent the same complex number."
  type: true-false
  answer: true
  explanation: "Since 3π = π + 2π, we have e^(i·3π) = e^(i(π + 2π)) = e^(iπ) · e^(i·2π) = e^(iπ) · 1 = e^(iπ) = -1. The 2π periodicity of the complex exponential means adding any multiple of 2π to the argument returns the same point on the unit circle. This periodicity is a key difference from the real exponential, which is injective."

- question: "Two complex numbers z₁ = 2e^(iπ/6) and z₂ = 5e^(iπ/4) are multiplied. What are the modulus and argument of z₁z₂, without converting to rectangular form?"
  type: short-answer
  answer: "The modulus of z₁z₂ is 2 · 5 = 10, and the argument is π/6 + π/4 = 5π/12."
  explanation: "In exponential form, multiplication is: (r₁ e^(iθ₁))(r₂ e^(iθ₂)) = r₁r₂ e^(i(θ₁+θ₂)). Moduli multiply and arguments add. This is the primary computational advantage of exponential form — multiplication that would require expanding (a+bi)(c+di) in rectangular form reduces to multiplying two real numbers and adding two angles."
```

## Explainer

In polar form, you learned to write a complex number as z = r(cos θ + i sin θ), where r is the modulus and θ is the argument. Euler's formula, e^(iθ) = cos θ + i sin θ, compresses this into elegant exponential notation: z = re^(iθ). This is not merely a notational convenience — it reveals a deep connection between exponential functions and rotation.

The formula can be derived from the power series for eˣ. Substituting x = iθ gives e^(iθ) = 1 + iθ + (iθ)²/2! + (iθ)³/3! + .... Expanding the powers of i (which cycle: i, -1, -i, 1, i, ...) and grouping real and imaginary terms produces exactly the Taylor series for cos θ and sin θ respectively. This derivation — which you can verify using the power series prerequisite — is what makes Euler's formula more than a trick: it is a theorem, proved by direct computation.

Geometrically, e^(iθ) is a point on the unit circle at angle θ from the positive real axis. Multiplying any complex number by e^(iθ) rotates it by θ radians without changing its modulus. This is why exponential form makes complex multiplication transparent: (r₁e^(iθ₁))(r₂e^(iθ₂)) = r₁r₂ e^(i(θ₁+θ₂)). The moduli multiply and the angles add — the same rules as real exponentials. Division, nth roots, and powers all follow the same pattern, which would be laborious to compute in rectangular form.

The 2π periodicity deserves special attention: because cos and sin repeat every 2π, we have e^(iθ) = e^(i(θ+2π)) for any θ. This means the complex exponential is not injective — multiple distinct complex numbers map to the same value. This periodicity drives the multi-valued nature of the complex logarithm, the concept of branch cuts, and much of what makes complex analysis richer (and trickier) than real analysis. The formula e^(iπ) + 1 = 0, often called Euler's identity, follows immediately: at θ = π, e^(iπ) = -1.
