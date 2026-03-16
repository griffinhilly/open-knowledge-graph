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
status: draft
---

# Sequences and Convergence in the Complex Plane

## Core Idea
A sequence {zₙ} in the complex plane converges to w if for every ε > 0, there exists N such that |zₙ - w| < ε for all n > N. Convergence is equivalent to both the real and imaginary parts converging separately. Complex sequences inherit all key properties: uniqueness of limits, Cauchy sequences, Bolzano-Weierstrass.

## Explainer

You already understand convergence for real sequences: {xₙ} → L if xₙ eventually stays arbitrarily close to L. The definition uses |xₙ − L| < ε as the measure of closeness. Extending this to the complex plane requires only one change: replace the real absolute value with the **complex modulus**. A sequence {zₙ} in ℂ converges to w if for every ε > 0, there exists N such that |zₙ − w| < ε for all n > N. The modulus |zₙ − w| is the Euclidean distance between zₙ and w in the complex plane — it measures how close the two points are as 2D vectors. The epsilon-delta machinery is otherwise identical.

The key insight is that complex convergence reduces to two simultaneous real convergences. Write zₙ = xₙ + iyₙ and w = u + iv. Then |zₙ − w|² = (xₙ − u)² + (yₙ − v)². This quantity is small exactly when both (xₙ − u)² and (yₙ − v)² are small — that is, when the real parts converge and the imaginary parts converge separately. More precisely, {zₙ} → w in ℂ if and only if {xₙ} → u in ℝ and {yₙ} → v in ℝ. This equivalence is tremendously practical: it lets you reduce questions about complex sequences to questions about two real sequences, where you can apply all the tools you already know.

Because the modulus is a distance function, the **Cauchy criterion** carries over exactly. A sequence {zₙ} is Cauchy if |zₙ − zₘ| < ε for all sufficiently large n, m — meaning the terms cluster together without explicitly referencing a limit. And since ℂ is complete (every Cauchy sequence of complex numbers converges to a complex number), Cauchy sequences and convergent sequences are the same thing in ℂ. This completeness is not automatic for all spaces but holds here because ℝ is complete and ℂ inherits completeness from the product ℝ × ℝ.

The **Bolzano-Weierstrass theorem** also extends: every bounded sequence in ℂ has a convergent subsequence. Boundedness for complex sequences means |zₙ| ≤ M for all n — the sequence stays inside a disk of radius M. This follows from the real version applied to xₙ and yₙ separately. These inheritance results matter because they mean complex analysis does not need to rebuild limit theory from scratch; it adapts real analysis by replacing the real absolute value with the complex modulus and recasting 1D proximity as 2D proximity. This foundation directly supports limits of complex functions, where the same epsilon-delta language applies but where approaching a point means approaching from any direction in the plane — a richer and more subtle geometry than the real case.
