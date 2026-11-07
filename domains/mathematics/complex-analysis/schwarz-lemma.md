---
id: schwarz-lemma
title: Schwarz's Lemma and Automorphisms of the Disk
domain: mathematics
course: complex-analysis
prerequisites:
  - id: maximum-modulus-principle
    type: hard
  - id: singularities-classification
    type: soft
  - id: mobius-transformations
    type: soft
builds-toward:
  - riemann-mapping-theorem
tags: [complex-analysis, schwarz-lemma, unit-disk, automorphisms, conformal-maps, maximum-modulus]
stage: advanced
status: validated
---

# Schwarz's Lemma and Automorphisms of the Disk

## Core Idea
Schwarz's lemma says that if f is holomorphic on the open unit disk D, maps D into D, and fixes the origin, then |f(z)| ≤ |z| for all z in D and |f'(0)| ≤ 1. If equality |f(z)| = |z| holds at a single nonzero point, or if |f'(0)| = 1, then f is a rotation, f(z) = e^(iθ)z. A short argument with the maximum modulus principle gives this rigid conclusion. Combined with Möbius transformations, it identifies every conformal self-map of the disk as a map of the form e^(iθ)(z - a)/(1 - āz) with |a| < 1.

## How It's Best Learned
Prove the lemma by applying the maximum modulus principle to g(z) = f(z)/z on circles |z| = r and letting r approach 1. Then check by direct computation that φₐ(z) = (z - a)/(1 - āz) maps the disk to itself and sends a to 0. Use φₐ to move any point to the origin, which is the step that lets the lemma apply to maps that do not fix 0.

## Common Misconceptions
- Schwarz's lemma applies to any bounded holomorphic function on the disk. (It needs f(0) = 0 and |f| < 1 on D; for maps not fixing 0, first compose with a disk automorphism.)
- The bound |f'(0)| ≤ 1 means |f'(z)| ≤ 1 everywhere in the disk. (The lemma bounds the derivative only at the origin; f(z) = z² has |f'(z)| = 2|z|, which exceeds 1 for |z| > 1/2.)
- Any one-to-one holomorphic map of the disk onto itself fixing 0 might be complicated. (By the equality case, it must be a rotation z ↦ e^(iθ)z.)

## Questions

```yaml
- question: "Let f be holomorphic on the unit disk with |f(z)| < 1 and f(0) = 0. What is the largest possible value of |f(1/2)|?"
  type: multiple-choice
  options: ["1/4", "1/2", "1", "2"]
  answer: 1
  explanation: "Schwarz's lemma gives |f(z)| ≤ |z|, so |f(1/2)| ≤ 1/2. The bound is reached by the identity f(z) = z, and in the equality case f must be a rotation."

- question: "If f maps the unit disk into itself holomorphically with f(0) = 0 and f'(0) = i, then f(z) = iz."
  type: true-false
  answer: true
  explanation: "|f'(0)| = |i| = 1 is the equality case of Schwarz's lemma, so f(z) = e^(iθ)z for some θ. Then f'(0) = e^(iθ) = i, which gives f(z) = iz."

- question: "Explain why g(z) = f(z)/z, with g(0) = f'(0), is holomorphic on the disk when f(0) = 0, and how the maximum modulus principle gives |g(z)| ≤ 1."
  type: short-answer
  answer: "Since f(0) = 0, f(z) = f'(0)z + a₂z² + ..., so f(z)/z = f'(0) + a₂z + ... is a power series and holomorphic. On |z| = r < 1, |g(z)| ≤ 1/r, so by maximum modulus |g| ≤ 1/r on |z| ≤ r; letting r → 1 gives |g| ≤ 1."
  explanation: "The singularity of f(z)/z at 0 is removable because f vanishes there. The maximum modulus principle moves the boundary estimate to the interior, and the limit r → 1 removes the factor 1/r."

- question: "Which map is a holomorphic bijection of the unit disk onto itself that sends a = 1/2 to 0?"
  type: multiple-choice
  options: ["z - 1/2", "(z - 1/2)/(1 - z/2)", "2z - 1", "(z - 1/2)/(1 + z/2)"]
  answer: 1
  explanation: "The map φₐ(z) = (z - a)/(1 - āz) with a = 1/2 is a disk automorphism sending a to 0. The map z - 1/2 shifts part of the disk outside it, 2z - 1 doubles distances, and (z - 1/2)/(1 + z/2) sends z = -0.9 to about -2.5, outside the disk. The denominator must use the conjugate with a minus sign, 1 - āz."
```

## Explainer

Holomorphic functions are surprisingly rigid, and Schwarz's lemma is a sharp example. It concerns a holomorphic map f of the open unit disk D = {|z| < 1} into itself with f(0) = 0.

The lemma. Under these hypotheses, |f(z)| ≤ |z| for every z in D and |f'(0)| ≤ 1. Moreover, if |f(z₀)| = |z₀| for some z₀ ≠ 0, or if |f'(0)| = 1, then f(z) = e^(iθ)z for some real θ.

The proof is short. Since f(0) = 0, the power series of f has no constant term, so g(z) = f(z)/z extends to a holomorphic function on D with g(0) = f'(0). Fix r < 1. On the circle |z| = r we have |g(z)| = |f(z)|/r < 1/r. By the maximum modulus principle, |g(z)| ≤ 1/r on the closed disk |z| ≤ r. Letting r increase to 1 gives |g(z)| ≤ 1 on all of D, which is |f(z)| ≤ |z|, and at z = 0 it gives |f'(0)| ≤ 1. If |g| equals 1 at an interior point, the maximum modulus principle forces g to be a constant of modulus 1, so f is a rotation.

The lemma has a geometric reading: a holomorphic self-map of the disk that fixes the center cannot push any point farther from the center. It can only rotate the disk or pull points inward.

The condition f(0) = 0 is removed with a family of Möbius transformations. For |a| < 1, let

φₐ(z) = (z - a)/(1 - āz).

A direct calculation shows |φₐ(z)| < 1 when |z| < 1, that φₐ(a) = 0, and that its inverse is φ₋ₐ. So φₐ is a holomorphic bijection of the disk onto itself, an automorphism, that moves a to the origin.

These maps describe every automorphism. Suppose h is a holomorphic bijection of D onto D with h(a) = 0. Then F = h ∘ φ₋ₐ is an automorphism fixing 0. Applying Schwarz's lemma to F and to its inverse gives |F(z)| ≤ |z| and |z| ≤ |F(z)|, so |F(z)| = |z| and F is a rotation. Therefore h(z) = e^(iθ)(z - a)/(1 - āz). The automorphisms of the disk are exactly these maps.

This classification is a key step in the proof of the Riemann mapping theorem, where it shows that the conformal map onto the disk is unique once a point and a direction are fixed.
