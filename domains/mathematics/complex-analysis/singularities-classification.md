---
id: singularities-classification
title: Classification of Isolated Singularities
domain: mathematics
course: complex-analysis
prerequisites:
- id: laurent-series
  type: hard
builds-toward:
- residues-definition-computation
- argument-principle
tags:
- singularities
- poles
- essential-singularities
stage: advanced
status: draft
---

# Classification of Isolated Singularities

## Core Idea
An isolated singularity of f at z₀ is classified by its Laurent expansion: a removable singularity has no negative powers (f extends analytically); a pole of order m has principal part with m terms (f ~ a₋ₘ/(z - z₀)^m near z₀); an essential singularity has infinitely many negative powers (f is wildly oscillating near z₀).

## Questions

```yaml
- question: "The function f(z) = (1 - cos z)/z² near z = 0 has what type of singularity?"
  type: multiple-choice
  options:
    - "A simple pole, because the denominator has a zero of order 2 and cos(0) = 1 makes the numerator vanish once"
    - "A pole of order 2, because the denominator is z²"
    - "A removable singularity, because expanding 1 - cos z = z²/2 - z⁴/24 + ... makes the Laurent series have no negative powers"
    - "An essential singularity, because cos z involves an infinite series"
  answer: 2
  explanation: "Expanding: 1 - cos z = z²/2 - z⁴/24 + ..., so (1 - cos z)/z² = 1/2 - z²/24 + ... This is a pure power series with no negative powers of z, so the singularity is removable — f extends analytically to z = 0 by setting f(0) = 1/2. The tempting wrong answer is A or B: students often see z² in the denominator and conclude 'pole of order 2,' but the numerator vanishes to the same order, canceling the negative powers. Classification depends on the Laurent expansion, not just the denominator."

- question: "Near z = 0, the function e^(1/z) takes values arbitrarily close to every nonzero complex number in every punctured neighborhood of 0. What type of singularity does e^(1/z) have at z = 0, and which theorem guarantees this dense-range behavior?"
  type: multiple-choice
  options:
    - "A pole of infinite order; the Residue Theorem guarantees the behavior"
    - "An essential singularity; the Casorati-Weierstrass theorem guarantees this dense-range behavior"
    - "A removable singularity; the behavior follows from the analytic continuation principle"
    - "A simple pole; the behavior reflects the 1/z term dominating the Laurent expansion"
  answer: 1
  explanation: "e^(1/z) = 1 + 1/z + 1/(2z²) + ... has infinitely many negative-power terms, making z = 0 an essential singularity. The Casorati-Weierstrass theorem states that near an essential singularity, f comes arbitrarily close to every complex value — the image of any punctured neighborhood is dense in ℂ. The stronger Picard Great Theorem says f actually achieves every value with at most one exception. No other singularity type has this wild behavior: removable singularities have finite limits, and poles blow up to ∞ in a controlled way."

- question: "If (z - z₀)² · f(z) has a finite nonzero limit as z → z₀, then f has a pole of order exactly 2 at z₀."
  type: true-false
  answer: true
  explanation: "This is the standard detection criterion for poles. A pole of order m at z₀ means the Laurent expansion of f has leading term a₋ₘ/(z - z₀)^m with a₋ₘ ≠ 0. Multiplying by (z - z₀)^m cancels the leading singularity, giving a function with a nonzero, finite limit. So (z - z₀)^m · f(z) → a₋ₘ ≠ 0 as z → z₀ iff f has a pole of exactly order m. If the limit were zero, the pole would be of lower order; if the limit were infinite, the order would be higher."

- question: "Near an essential singularity z₀, the modulus |f(z)| must tend to infinity as z → z₀, distinguishing it from a removable singularity where |f(z)| stays bounded."
  type: true-false
  answer: false
  explanation: "This is false — and it is a common misconception. Near an essential singularity, |f(z)| does NOT tend to infinity along every path. By Casorati-Weierstrass, f(z) comes arbitrarily close to every complex value, including 0, so |f(z)| oscillates wildly and can be made close to 0 or any other value. For poles, |f(z)| → ∞ in a controlled way. For removable singularities, f(z) approaches a finite limit. Essential singularities are precisely the case where none of these controlled behaviors apply."

- question: "Why is the principal part of the Laurent expansion — rather than, say, the behavior of |f(z)| as z → z₀ — the correct basis for classifying isolated singularities?"
  type: short-answer
  answer: "The principal part (the negative-power terms in the Laurent expansion) is algebraically precise and directly determines every aspect of the singularity: zero negative-power terms means analytic extension is possible (removable); finitely many means controlled blow-up (pole); infinitely many means chaotic behavior (essential). Behavioral descriptions like |f(z)| → ∞ are consequences of the Laurent structure, not the cause, and they are ambiguous: knowing |f(z)| → ∞ tells you f has a pole but not its order; knowing the principal part tells you everything needed to compute residues and apply the Residue Theorem."
  explanation: "The Laurent expansion is also the practical tool: to classify, expand and count negative-power terms. This is why Laurent series are prerequisite to singularity classification — the expansion IS the classification. Behavioral tests (limit tests for removable singularities, the pole-order test) are shortcuts derived from the Laurent structure, and they work because the Laurent expansion is the ground truth."
```

## Explainer

From your study of Laurent series, you know that a complex function near an isolated singularity z₀ can be expanded in both positive and negative powers of (z − z₀): f(z) = ... + a₋₂/(z − z₀)² + a₋₁/(z − z₀) + a₀ + a₁(z − z₀) + ... The **negative-power part** (called the **principal part**) is what determines the type of singularity. There are exactly three cases, and they describe increasingly wild behavior.

**Removable singularities** have no principal part — all coefficients aₙ with n < 0 are zero. The Laurent expansion is just a regular power series a₀ + a₁(z − z₀) + ..., so by defining (or redefining) f(z₀) = a₀, the function extends analytically through z₀. The singularity was only apparent — a hole that can be plugged. The canonical example is sin(z)/z at z = 0: expanding sin(z)/z = 1 − z²/6 + z⁴/120 − ..., there are no negative powers, so the singularity is removable by setting f(0) = 1. The function approaches a finite, well-defined limit as z → z₀.

**Poles** have a finite principal part: a₋ₘ/(z − z₀)^m + ... + a₋₁/(z − z₀) with a₋ₘ ≠ 0. Near a pole of order m, the function blows up like |f(z)| ~ |a₋ₘ|/|z − z₀|^m → ∞ as z → z₀. A first-order pole (m = 1) is a **simple pole** — the most common type, and the most important for the Residue Theorem. The coefficient a₋₁ of the simple pole term is the **residue**, which drives complex contour integrals. You can detect a pole of order m by checking that (z − z₀)^m · f(z) has a nonzero, finite limit as z → z₀.

**Essential singularities** have infinitely many negative powers — the principal part is an infinite series. The behavior near an essential singularity is famously chaotic. The **Casorati-Weierstrass theorem** says f comes arbitrarily close to every complex value in any neighborhood of the singularity; the stronger **Picard Great Theorem** says f actually takes every complex value, with at most one exception, infinitely often. The canonical example is e^(1/z) near z = 0: e^(1/z) = 1 + 1/z + 1/(2z²) + ... — infinitely many negative powers. As z → 0 along different paths, e^(1/z) spirals, explodes, and vanishes in completely different ways. Classifying which type of singularity you have is the essential first step in computing residues and applying the Residue Theorem.
