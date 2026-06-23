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
tags:
- complex-numbers
- polar-coordinates
- trigonometry
stage: advanced
status: validated
---

# Polar Form of Complex Numbers

## Core Idea
Any complex number z can be written as z = r(cos θ + i sin θ) = r cis θ, where r = |z| and θ = arg(z). This polar form makes multiplication and division geometrically transparent: to multiply, multiply moduli and add arguments; to divide, divide moduli and subtract arguments.

## How It's Best Learned
Start with z = 1 + i, find its modulus and argument, and verify the polar form. Practice multiplying two complex numbers in polar form (e.g., 2e^(iπ/4) · 3e^(iπ/3)) and visualize the result. Compare to Cartesian multiplication to see the simplification.

## Common Misconceptions
Thinking polar form is harder to compute with; it is actually easier for multiplication and division. Forgetting that cos and sin must be in radians when computing the argument.

## Questions

```yaml
- question: "Two complex numbers z₁ = 2(cos(π/6) + i sin(π/6)) and z₂ = 3(cos(π/3) + i sin(π/3)) are multiplied. What is z₁z₂ in polar form?"
  type: multiple-choice
  options:
    - "5(cos(π/2) + i sin(π/2))"
    - "6(cos(π/2) + i sin(π/2))"
    - "6(cos(π/18) + i sin(π/18))"
    - "6(cos(π/9) + i sin(π/9))"
  answer: 1
  explanation: "In polar form, multiplication multiplies moduli and adds arguments. The moduli are 2 and 3, so the product modulus is 2 × 3 = 6. The arguments are π/6 and π/3, so the product argument is π/6 + π/3 = π/6 + 2π/6 = π/2. Result: 6(cos(π/2) + i sin(π/2)) = 6i. Option A (modulus 5) is the classic error of adding moduli instead of multiplying them. Options C and D use incorrect combinations of the arguments."

- question: "What geometric transformation does multiplying any complex number z by i correspond to in the complex plane?"
  type: multiple-choice
  options:
    - "Reflection across the imaginary axis"
    - "Scaling by a factor of 1 (no change)"
    - "Rotation by π/2 counterclockwise about the origin"
    - "Reflection across the line y = x"
  answer: 2
  explanation: "The number i has modulus 1 and argument π/2. Multiplying z by i multiplies z's modulus by 1 (unchanged) and adds π/2 to z's argument — a 90° counterclockwise rotation. For example: 1 (angle 0) → i (angle π/2) → −1 (angle π) → −i (angle 3π/2) → 1. This four-step rotation is the geometric picture behind i⁴ = 1. The polar form makes this rotation interpretation immediate; in Cartesian form, multiplying (a + bi)(0 + i) = −b + ai is mechanically correct but geometrically opaque."

- question: "Raising a complex number z = r(cos θ + i sin θ) to the nth power gives rⁿ(cos(nθ) + i sin(nθ)) — the modulus is raised to the nth power and the argument is multiplied by n."
  type: true-false
  answer: true
  explanation: "This is De Moivre's theorem, which follows directly from the multiplication rule for polar form. Multiplying z by itself multiplies the moduli (r × r = r²) and adds the arguments (θ + θ = 2θ). Repeating n times gives rⁿ(cos(nθ) + i sin(nθ)). Geometrically: raising a complex number to the nth power scales its distance from the origin by rⁿ and rotates it by n times its original angle. For example, (1+i)⁸ has modulus (√2)⁸ = 16 and argument 8 × π/4 = 2π, so (1+i)⁸ = 16."

- question: "Polar form is mainly a notational convenience — computing with it is about the same difficulty as using the Cartesian form a + bi."
  type: true-false
  answer: false
  explanation: "This underestimates polar form. For multiplication and division, polar form is dramatically simpler: multiply moduli and add arguments vs. expanding (a+bi)(c+di) = (ac−bd) + (ad+bc)i and simplifying. For powers and roots, the advantage is overwhelming — computing (1+i)¹⁰ in Cartesian form requires nine multiplications; in polar form it is immediate: modulus (√2)¹⁰ = 32, argument 10 × π/4 = 5π/2 = π/2. Polar form is not a notational choice; it is the form that makes multiplication, division, powers, and roots geometrically transparent."

- question: "Why does multiplying two complex numbers in polar form reduce to multiplying their moduli and adding their arguments? Explain the geometric meaning of this rule."
  type: short-answer
  answer: "The rule follows from the cosine and sine addition formulas. Expanding z₁z₂ = r₁r₂[(cos θ₁ cos θ₂ − sin θ₁ sin θ₂) + i(sin θ₁ cos θ₂ + cos θ₁ sin θ₂)] gives r₁r₂(cos(θ₁ + θ₂) + i sin(θ₁ + θ₂)) by the angle addition identities. Geometrically, multiplying by z₂ performs two operations: it scales the entire complex plane by r₂ (stretching z₁'s distance from the origin) and rotates by angle θ₂. Complex multiplication is scaling + rotation. This geometric picture — that multiplication in the complex plane combines distance and direction independently — is the key insight polar form provides."
  explanation: "The mathematical derivation uses angle addition formulas, but the geometric interpretation is the important takeaway. Every complex number z = r(cos θ + i sin θ) is completely characterized by how far it is from the origin (r) and what direction it points (θ), and multiplication combines these by the simplest possible rules. This interpretation leads directly to De Moivre's theorem and to the connection e^(iθ) = cos θ + i sin θ that polar form anticipates."
```

## Explainer

You already know that a complex number has a **modulus** r = |z| (its distance from the origin in the complex plane) and an **argument** θ = arg(z) (the angle it makes with the positive real axis). The polar form z = r(cos θ + i sin θ) is simply the Cartesian coordinate conversion you know from trigonometry, applied to the complex plane: the real part is r cos θ and the imaginary part is r sin θ. Every complex number lives somewhere in the plane, and polar form describes that location using distance and direction instead of horizontal and vertical offsets.

The power of polar form is revealed in **multiplication**. In Cartesian form, multiplying (a + bi)(c + di) requires expanding and simplifying — straightforward but mechanical. In polar form, the result is geometric: multiplying z₁ = r₁(cos θ₁ + i sin θ₁) by z₂ = r₂(cos θ₂ + i sin θ₂) gives z₁z₂ = r₁r₂(cos(θ₁ + θ₂) + i sin(θ₁ + θ₂)). The moduli multiply and the arguments add. In the complex plane, this is a stretch by factor r₂ followed by a rotation by θ₂. Division does the reverse: divide moduli and subtract arguments. These rules follow directly from the angle addition formulas for cosine and sine — formulas you know from trigonometry — applied to the product.

To convert a specific number: start with z = 1 + i. Its modulus is √(1² + 1²) = √2 and its argument is arctan(1/1) = π/4. So z = √2 (cos(π/4) + i sin(π/4)). To multiply z² = (√2)²(cos(π/2) + i sin(π/2)) = 2(0 + i) = 2i. The same calculation in Cartesian form gives (1+i)² = 1 + 2i + i² = 2i — same answer, but the polar route gives geometric insight: squaring a complex number squares its modulus and doubles its argument. This geometric interpretation — that multiplication acts on the complex plane as scaling and rotation — is the key idea polar form unlocks, and it leads directly to De Moivre's theorem and the exponential form e^(iθ) that unifies complex numbers and trigonometry.
