---
id: uniform-convergence-preserves-continuity
title: Uniform Convergence Preserves Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-convergence-functions
  type: hard
- id: epsilon-delta-continuity
  type: hard
builds-toward:
- interchange-limit-integral
- weierstrass-approximation-theorem
tags:
- uniform-convergence
- continuity
- preservation
stage: advanced
status: draft
---

# Uniform Convergence Preserves Continuity

## Core Idea
If (fₙ) converges uniformly to f and each fₙ is continuous, then f is continuous. This is the key theorem justifying when lim can be exchanged with continuity and derivatives. Pointwise convergence does not guarantee this: fₙ(x) = xⁿ on [0,1] is pointwise but not uniformly convergent to the discontinuous step function.

## Explainer

Before engaging with the theorem, you need a sharp picture of the difference between **pointwise** and **uniform** convergence, which you have from your prerequisite. Pointwise convergence says: for each fixed x, fₙ(x) → f(x). The rate of convergence is allowed to depend on x — at some points the sequence might converge quickly, at others arbitrarily slowly. Uniform convergence says: for every ε > 0, there is a single N that works for *all* x simultaneously. Geometrically, uniform convergence means the graphs of fₙ eventually lie inside an ε-tube around the graph of f, with the tube width shrinking to zero.

The canonical example where pointwise fails is fₙ(x) = xⁿ on [0,1]. Each fₙ is continuous — a polynomial. But pointwise, fₙ(x) → 0 for x ∈ [0,1) and fₙ(1) = 1 for all n. The limiting function is 0 on [0,1) and 1 at x=1 — a discontinuous step. This is not a pathological edge case; it is the generic behavior when convergence is non-uniform. Near x=1, xⁿ does not become small quickly: for any ε and any N, you can find x close enough to 1 such that xᴺ > 1−ε. The convergence is fastest near 0 and arbitrarily slow near 1 — the speed varies with x, so pointwise convergence fails to protect continuity.

The theorem's proof is the classic **three-ε argument** (or ε/3 argument). To show f is continuous at a point x, you want |f(x) − f(y)| < ε for y sufficiently close to x. Split the difference into three parts: |f(x) − fₙ(x)| + |fₙ(x) − fₙ(y)| + |fₙ(y) − f(y)|. By **uniform convergence**, choose n large enough that the first and third terms are each less than ε/3 *for all points at once* — this is the step that requires uniformity, not just pointwise convergence. Then by **continuity of fₙ**, choose δ small enough that the middle term is less than ε/3 when |x − y| < δ. The three pieces sum to less than ε. The uniformity of convergence is precisely what allows you to choose n without depending on y — if convergence were merely pointwise, you could not control the third term independently of y.

The theorem has consequences that reach throughout analysis. It justifies swapping limits with continuity (lim fₙ is continuous), and its spirit extends to swapping limits with integrals: if fₙ → f uniformly on [a,b], then ∫fₙ → ∫f. This interchange-of-limits theme — knowing when lim and ∫ or lim and d/dx can be swapped — is one of the central problems of real analysis. Uniform convergence is the sufficient condition that makes these swaps legal, which is why the theorem is a foundational tool rather than an isolated result.
