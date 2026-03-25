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
- id: sequential-characterization-continuity
  type: soft
- id: sequential-continuity
  type: soft
builds-toward:
- interchange-limit-integral
- weierstrass-approximation-theorem
tags:
- uniform-convergence
- continuity
- preservation
stage: advanced
status: validated
---
# Uniform Convergence Preserves Continuity

## Core Idea
If (fₙ) converges uniformly to f and each fₙ is continuous, then f is continuous. This is the key theorem justifying when lim can be exchanged with continuity and derivatives. Pointwise convergence does not guarantee this: fₙ(x) = xⁿ on [0,1] is pointwise but not uniformly convergent to the discontinuous step function.

## Questions

```yaml
- question: "Consider fₙ(x) = xⁿ on [0,1]. The sequence converges pointwise to a limit function f. Which of the following correctly describes f?"
  type: multiple-choice
  options:
    - "f(x) = 0 for all x ∈ [0,1], since xⁿ → 0 for large n"
    - "f(x) = 0 for x ∈ [0,1) and f(1) = 1, making f discontinuous"
    - "f(x) = x for all x ∈ [0,1], since the identity is the natural limit"
    - "f does not exist because the sequence fails to converge at every point"
  answer: 1
  explanation: "For any fixed x ∈ [0,1), xⁿ → 0 as n → ∞. But at x = 1, 1ⁿ = 1 for every n, so fₙ(1) = 1. The pointwise limit is thus 0 on [0,1) and 1 at x=1 — a discontinuous step function. Each fₙ is continuous (it's a polynomial), yet the limit is not. This is exactly the counterexample showing that pointwise convergence does not preserve continuity."

- question: "In the ε/3 proof that uniform convergence preserves continuity, what is the critical role of uniform convergence that pointwise convergence cannot fill?"
  type: multiple-choice
  options:
    - "Uniform convergence guarantees each fₙ is bounded, which is needed to apply the triangle inequality"
    - "Uniform convergence allows choosing N large enough that |fₙ(y) − f(y)| < ε/3 for all y simultaneously, without N depending on y"
    - "Uniform convergence implies the functions are integrable, so the limit integral equals the integral of the limit"
    - "Pointwise convergence fails only for unbounded functions, which are automatically excluded here"
  answer: 1
  explanation: "The ε/3 argument splits |f(x) − f(y)| ≤ |f(x) − fₙ(x)| + |fₙ(x) − fₙ(y)| + |fₙ(y) − f(y)|. The first and third terms require bounding |fₙ(z) − f(z)| for the specific points x and y. With uniform convergence, one N controls all points at once: choose N so that |fₙ(z) − f(z)| < ε/3 for all z. With only pointwise convergence, the N for x might differ from the N for y — and since y may vary, no single N suffices."

- question: "If each function in a sequence (fₙ) is continuous and the sequence converges pointwise to f on a closed interval, then f is necessarily continuous."
  type: true-false
  answer: false
  explanation: "False. The counterexample is fₙ(x) = xⁿ on [0,1]: each fₙ is continuous, the convergence is pointwise, and yet the limit is discontinuous at x=1. The theorem requires uniform convergence, not merely pointwise. The failure occurs because pointwise convergence allows the convergence speed to vary with x — near x=1, xⁿ converges arbitrarily slowly — so the limit function can inherit discontinuities."

- question: "Uniform convergence of (fₙ) to f on a set E means: for every ε > 0, there exists N such that for all x ∈ E and all n > N, |fₙ(x) − f(x)| < ε."
  type: true-false
  answer: true
  explanation: "This is precisely the definition of uniform convergence. The key feature is that N depends only on ε, not on x — a single N works simultaneously for every point in E. Geometrically, the graphs of fₙ eventually lie inside an ε-band around the graph of f. Pointwise convergence allows N to depend on x: N(x,ε) might grow without bound as x approaches some point, and that is exactly what goes wrong in the xⁿ example near x=1."

- question: "Explain in your own words why pointwise convergence fails to guarantee continuity of the limit, and what uniform convergence adds that fixes this."
  type: short-answer
  answer: "With pointwise convergence, the sequence can converge arbitrarily slowly near certain points, allowing the limit to 'jump' discontinuously. Uniform convergence forces a single convergence rate across all points simultaneously, which is precisely what the ε/3 argument needs: it lets you choose n large enough to control |fₙ(y) − f(y)| for all y at once, regardless of where y is."
  explanation: "The failure mode is illustrated by xⁿ on [0,1]: near x=1, convergence is arbitrarily slow, so the limit can 'suddenly' equal 1 at x=1 while being 0 nearby. Uniform convergence closes this gap by banning slow-near-some-point convergence. In the proof, once you fix n large enough that fₙ is uniformly within ε/3 of f everywhere, you can then use fₙ's continuity (choose δ for the middle term) knowing the outer terms are already controlled everywhere — including at the nearby point y you're comparing x to."
```

## Explainer

Before engaging with the theorem, you need a sharp picture of the difference between **pointwise** and **uniform** convergence, which you have from your prerequisite. Pointwise convergence says: for each fixed x, fₙ(x) → f(x). The rate of convergence is allowed to depend on x — at some points the sequence might converge quickly, at others arbitrarily slowly. Uniform convergence says: for every ε > 0, there is a single N that works for *all* x simultaneously. Geometrically, uniform convergence means the graphs of fₙ eventually lie inside an ε-tube around the graph of f, with the tube width shrinking to zero.

The canonical example where pointwise fails is fₙ(x) = xⁿ on [0,1]. Each fₙ is continuous — a polynomial. But pointwise, fₙ(x) → 0 for x ∈ [0,1) and fₙ(1) = 1 for all n. The limiting function is 0 on [0,1) and 1 at x=1 — a discontinuous step. This is not a pathological edge case; it is the generic behavior when convergence is non-uniform. Near x=1, xⁿ does not become small quickly: for any ε and any N, you can find x close enough to 1 such that xᴺ > 1−ε. The convergence is fastest near 0 and arbitrarily slow near 1 — the speed varies with x, so pointwise convergence fails to protect continuity.

The theorem's proof is the classic **three-ε argument** (or ε/3 argument). To show f is continuous at a point x, you want |f(x) − f(y)| < ε for y sufficiently close to x. Split the difference into three parts: |f(x) − fₙ(x)| + |fₙ(x) − fₙ(y)| + |fₙ(y) − f(y)|. By **uniform convergence**, choose n large enough that the first and third terms are each less than ε/3 *for all points at once* — this is the step that requires uniformity, not just pointwise convergence. Then by **continuity of fₙ**, choose δ small enough that the middle term is less than ε/3 when |x − y| < δ. The three pieces sum to less than ε. The uniformity of convergence is precisely what allows you to choose n without depending on y — if convergence were merely pointwise, you could not control the third term independently of y.

The theorem has consequences that reach throughout analysis. It justifies swapping limits with continuity (lim fₙ is continuous), and its spirit extends to swapping limits with integrals: if fₙ → f uniformly on [a,b], then ∫fₙ → ∫f. This interchange-of-limits theme — knowing when lim and ∫ or lim and d/dx can be swapped — is one of the central problems of real analysis. Uniform convergence is the sufficient condition that makes these swaps legal, which is why the theorem is a foundational tool rather than an isolated result.
