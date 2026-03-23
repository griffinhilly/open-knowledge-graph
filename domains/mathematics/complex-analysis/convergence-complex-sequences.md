---
id: convergence-complex-sequences
title: Sequences and Convergence in the Complex Plane
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-plane
  type: hard
- id: epsilon-n-convergence
  type: soft
builds-toward:
- limits-continuity-complex-functions
- power-series-complex-plane
tags:
- sequences
- convergence
- topology
stage: advanced
status: validated
---

# Sequences and Convergence in the Complex Plane

## Core Idea
A sequence {zₙ} in the complex plane converges to w if for every ε > 0, there exists N such that |zₙ - w| < ε for all n > N. Convergence is equivalent to both the real and imaginary parts converging separately. Complex sequences inherit all key properties: uniqueness of limits, Cauchy sequences, Bolzano-Weierstrass.

## Questions

```yaml
- question: "Consider the sequence zₙ = (n/(n+1)) + i·(1/n). What is the limit as n → ∞?"
  type: multiple-choice
  options:
    - "The sequence diverges because complex sequences behave differently from real sequences"
    - "1 + 0i = 1, because both real and imaginary parts converge separately"
    - "1 + i, because the modulus of the terms converges to 1"
    - "The limit cannot be determined without knowing the spiral behavior in the plane"
  answer: 1
  explanation: "Complex convergence reduces to simultaneous real convergence: Re(zₙ) = n/(n+1) → 1 and Im(zₙ) = 1/n → 0. Since both parts converge, zₙ → 1 + 0i = 1 in ℂ. Option A is wrong — complex sequences use the same epsilon-modulus definition as real sequences. Option C confuses the modulus of the terms (which approaches 1) with the limit of the sequence. The key tool: |zₙ − 1| = √((n/(n+1)−1)² + (1/n)²) → 0, confirmed by checking each component."

- question: "A sequence of complex numbers {zₙ} satisfies |zₙ| ≤ 5 for all n but does not converge. Which is the most that the Bolzano-Weierstrass theorem guarantees?"
  type: multiple-choice
  options:
    - "The sequence converges — boundedness in ℂ implies convergence"
    - "There exists a subsequence {zₙₖ} that converges to some complex number w"
    - "The sequence is Cauchy even though it does not converge"
    - "The sequence has at most finitely many distinct values"
  answer: 1
  explanation: "Bolzano-Weierstrass guarantees a convergent subsequence from any bounded sequence, not convergence of the sequence itself. The sequence zₙ = (−1)ⁿ is bounded (|zₙ| = 1) but does not converge — it oscillates between 1 and −1. However, it has convergent subsequences: {z₂ₙ} → 1 and {z₂ₙ₊₁} → −1. Option A is the common misconception that boundedness implies convergence (it guarantees only a convergent subsequence). Option C is false — a non-convergent sequence need not be Cauchy."

- question: "A sequence {zₙ} in ℂ converges to w if and only if Re(zₙ) → Re(w) and Im(zₙ) → Im(w) as real sequences."
  type: true-false
  answer: true
  explanation: "This equivalence is the central practical tool. It follows from the identity |zₙ − w|² = (Re(zₙ) − Re(w))² + (Im(zₙ) − Im(w))². The modulus is small exactly when both squared real differences are small — so complex convergence is equivalent to simultaneous convergence of real and imaginary parts. This lets you reduce all questions about complex sequences to the real analysis you already know."

- question: "Since ℂ contains square roots of negative numbers and behaves differently from ℝ algebraically, Cauchy sequences in ℂ may fail to converge."
  type: true-false
  answer: false
  explanation: "ℂ is complete: every Cauchy sequence in ℂ converges to a limit in ℂ. This follows because ℂ inherits completeness from ℝ via the isomorphism ℂ ≅ ℝ × ℝ. A Cauchy sequence {zₙ} in ℂ has Cauchy sequences of real and imaginary parts (since |Re(zₙ) − Re(zₘ)| ≤ |zₙ − zₘ|), and since ℝ is complete, those converge. The algebraic 'exoticness' of i has no bearing on completeness, which is a metric property."

- question: "Why does extending convergence from ℝ to ℂ require replacing the absolute value with the complex modulus, and what geometric change does this represent?"
  type: short-answer
  answer: "In ℝ, |xₙ − L| measures distance on the real line — a one-dimensional notion of closeness. In ℂ, convergence must capture closeness in the complex plane, which is two-dimensional. The complex modulus |zₙ − w| = √((xₙ−u)² + (yₙ−v)²) is the Euclidean distance between two points in ℝ², measuring closeness in all directions simultaneously. This matters for limits of complex functions, where approaching a limit point means approaching from any direction in the plane — a richer geometry than the real case where approach is only from left or right."
  explanation: "The modulus is the bridge between algebraic structure (complex numbers as a+bi) and metric structure (complex numbers as points in the plane). All of convergence theory transfers because the modulus satisfies the same properties as the absolute value: positivity, symmetry, and the triangle inequality."
```

## Explainer

You already understand convergence for real sequences: {xₙ} → L if xₙ eventually stays arbitrarily close to L. The definition uses |xₙ − L| < ε as the measure of closeness. Extending this to the complex plane requires only one change: replace the real absolute value with the **complex modulus**. A sequence {zₙ} in ℂ converges to w if for every ε > 0, there exists N such that |zₙ − w| < ε for all n > N. The modulus |zₙ − w| is the Euclidean distance between zₙ and w in the complex plane — it measures how close the two points are as 2D vectors. The epsilon-delta machinery is otherwise identical.

The key insight is that complex convergence reduces to two simultaneous real convergences. Write zₙ = xₙ + iyₙ and w = u + iv. Then |zₙ − w|² = (xₙ − u)² + (yₙ − v)². This quantity is small exactly when both (xₙ − u)² and (yₙ − v)² are small — that is, when the real parts converge and the imaginary parts converge separately. More precisely, {zₙ} → w in ℂ if and only if {xₙ} → u in ℝ and {yₙ} → v in ℝ. This equivalence is tremendously practical: it lets you reduce questions about complex sequences to questions about two real sequences, where you can apply all the tools you already know.

Because the modulus is a distance function, the **Cauchy criterion** carries over exactly. A sequence {zₙ} is Cauchy if |zₙ − zₘ| < ε for all sufficiently large n, m — meaning the terms cluster together without explicitly referencing a limit. And since ℂ is complete (every Cauchy sequence of complex numbers converges to a complex number), Cauchy sequences and convergent sequences are the same thing in ℂ. This completeness is not automatic for all spaces but holds here because ℝ is complete and ℂ inherits completeness from the product ℝ × ℝ.

The **Bolzano-Weierstrass theorem** also extends: every bounded sequence in ℂ has a convergent subsequence. Boundedness for complex sequences means |zₙ| ≤ M for all n — the sequence stays inside a disk of radius M. This follows from the real version applied to xₙ and yₙ separately. These inheritance results matter because they mean complex analysis does not need to rebuild limit theory from scratch; it adapts real analysis by replacing the real absolute value with the complex modulus and recasting 1D proximity as 2D proximity. This foundation directly supports limits of complex functions, where the same epsilon-delta language applies but where approaching a point means approaching from any direction in the plane — a richer and more subtle geometry than the real case.
