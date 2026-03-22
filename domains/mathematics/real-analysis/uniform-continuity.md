---
id: uniform-continuity
title: Uniform Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
builds-toward:
- uniform-continuity-compact-sets
- riemann-integral-darboux-sums
tags:
- uniform-continuity
- epsilon-delta
- strengthened
stage: advanced
status: draft
---

# Uniform Continuity

## Core Idea
A function f is uniformly continuous on a set S if for every ε > 0, there exists δ > 0 (independent of the point) such that for all x, y ∈ S, |x - y| < δ implies |f(x) - f(y)| < ε. This is stronger than pointwise continuity: δ works at all points simultaneously. It is essential for convergence of integrals and derivatives.

## How It's Best Learned
Show f(x) = x is uniformly continuous but f(x) = x² is not on ℝ (though it is on [0,1]). Prove f(x) = 1/x is not uniformly continuous on (0,1) but is on [1,∞).

## Common Misconceptions
- Confusing 'δ depends on ε but not on x' with 'δ is constant'; it can depend on ε.
- Thinking uniform continuity at a point makes sense; it's a property of a function on a set.
- Assuming every continuous function is uniformly continuous; f(x) = x² on ℝ is a counterexample.

## Explainer

From your study of ε-δ continuity, you know what it means for a function f to be continuous at a single point x₀: for every ε > 0, there exists δ > 0 such that |x − x₀| < δ implies |f(x) − f(x₀)| < ε. The δ you find typically depends on both ε and the particular point x₀. **Uniform continuity** strengthens this by demanding that a single δ works at all points simultaneously. Formally, f is uniformly continuous on a set S if: for every ε > 0, there exists δ > 0 such that for all x, y ∈ S, |x − y| < δ implies |f(x) − f(y)| < ε. The δ depends only on ε, not on the location within S.

The distinction is about how the "required δ" varies across the domain. For f(x) = x on ℝ, continuity is trivially uniform: choosing δ = ε works everywhere, because |f(x) − f(y)| = |x − y| < δ = ε. The function's "rate of change" is constant (slope 1), so the same δ suffices at every point. For f(x) = x² on ℝ, the situation is different. To ensure |x² − y²| = |x + y||x − y| < ε when |x − y| < δ, you need δ < ε/|x + y|. As x grows, |x + y| ≈ 2|x| grows without bound, forcing the required δ toward 0. No single δ can work for all x ∈ ℝ simultaneously, so f(x) = x² is continuous but not uniformly continuous on ℝ.

The same function can be uniformly continuous on one domain but not another. f(x) = 1/x is not uniformly continuous on (0, 1) — near x = 0, the function grows arbitrarily steep, and any proposed δ fails for sufficiently small x. But on [1, ∞), the slope |f'(x)| = 1/x² ≤ 1 is bounded, so δ = ε works everywhere by the mean value theorem. The key structural fact is the **Heine-Cantor theorem**: every continuous function on a compact set is uniformly continuous. Since [a, b] is compact and (0, 1) is not, the theorem explains why continuity on [a, b] automatically upgrades to uniform continuity, while continuity on open or unbounded domains need not.

Uniform continuity matters because it is the condition needed to guarantee that function-level operations behave well. The proof that continuous functions on [a, b] are Riemann integrable relies on uniform continuity: it lets you choose a single mesh size δ for the partition that controls the oscillation of f on every subinterval simultaneously. Without uniform continuity, you would need finer and finer partitions in different parts of the domain, and the integral might not exist. Similarly, uniform continuity is the hypothesis (stronger than pointwise continuity) that ensures certain limits can be interchanged with integration. Understanding when continuity is automatically uniform — and when it is not — is one of the key practical skills in real analysis.

## Questions

```yaml
- question: "Consider f(x) = 1/x on the interval (0, 1). Why is f NOT uniformly continuous on this domain?"
  type: multiple-choice
  options:
    - "f is not differentiable at x = 0, which lies in the closure of (0, 1)"
    - "Near x = 0, the function grows arbitrarily steep, so any fixed δ eventually fails: for small enough x and y = x + δ/2, |f(x) − f(y)| can exceed any ε"
    - "The interval (0, 1) is open, and no function on an open interval can be uniformly continuous"
    - "f(x) = 1/x is discontinuous at x = 0, which makes the whole interval fail"
  answer: 1
  explanation: "Near x = 0, the slope of 1/x grows without bound. For any proposed δ > 0, we can find x small enough that |f(x) − f(x + δ/2)| is arbitrarily large — the same δ that works near x = 1/2 will catastrophically fail near x = 0.001. This is the essence of non-uniform continuity: the δ required to control |f(x) − f(y)| depends on x and cannot be bounded below by a single positive constant over the whole domain. Option C is wrong: f(x) = x is uniformly continuous on any open interval."

- question: "A student argues: 'f(x) = x² is continuous everywhere on ℝ, so it must be uniformly continuous on ℝ.' This reasoning fails because:"
  type: multiple-choice
  options:
    - "f(x) = x² is not actually continuous on all of ℝ"
    - "Continuity guarantees a δ for each (ε, x) pair separately, but for x² the required δ shrinks to 0 as x → ∞ — no single δ covers all points simultaneously"
    - "Uniform continuity and pointwise continuity are equivalent on all unbounded intervals"
    - "Unbounded domains never support uniformly continuous functions"
  answer: 1
  explanation: "For f(x) = x², to control |x² − y²| = |x + y||x − y| < ε when |x − y| < δ, we need δ < ε / |x + y|. As x → ∞, this upper bound on δ goes to 0 — no single positive δ can work for all x ∈ ℝ. Pointwise continuity only requires a δ that works at each fixed x; uniform continuity requires one δ that works at all x simultaneously. Option D is wrong: f(x) = x is uniformly continuous on all of ℝ."

- question: "In the definition of uniform continuity, the key distinction from pointwise continuity is that δ does not depend on ε — a fixed δ works regardless of what ε is."
  type: true-false
  answer: false
  explanation: "This is a common confusion that reverses the key distinction. In BOTH uniform and pointwise continuity, δ may (and typically does) depend on ε — a smaller ε generally requires a smaller δ. The actual distinction is about dependence on the POINT x: in pointwise continuity, δ may also depend on x (shrinking to 0 as x changes); in uniform continuity, δ depends only on ε and works simultaneously for ALL pairs of points in the domain. Saying 'δ is constant' or 'δ independent of ε' both misstate the definition."

- question: "Uniform continuity is a property of a function on a set, not at a point — it is a category error to ask whether f is 'uniformly continuous at x₀.'"
  type: true-false
  answer: true
  explanation: "The definition of uniform continuity quantifies over ALL pairs x, y in the domain: for every ε > 0, there exists δ > 0 such that |x − y| < δ implies |f(x) − f(y)| < ε for ALL x, y in S. There is no 'local' version — no way to say this property holds 'at' a particular point, since it is inherently about the behavior of the function across the entire domain at once. By contrast, pointwise continuity at x₀ is a local property."

- question: "Explain what goes wrong when you try to prove that f(x) = x² is uniformly continuous on ℝ. Why does the argument that works for f(x) = x fail here?"
  type: short-answer
  answer: "For f(x) = x, |f(x) − f(y)| = |x − y|, so choosing δ = ε works for ALL points simultaneously — the same δ covers the entire real line. For f(x) = x², |f(x) − f(y)| = |x² − y²| = |x + y| · |x − y|. To make this less than ε when |x − y| < δ, we need δ · |x + y| < ε, so δ < ε / |x + y|. The required δ depends on x: as x grows, |x + y| ≈ 2|x| grows without bound, forcing δ to shrink toward 0. No single δ can satisfy the constraint for all x ∈ ℝ simultaneously. The linear function had a bounded 'rate of variation'; the quadratic's rate grows unboundedly."
  explanation: "The key structural difference is that f(x) = x has constant derivative (slope always 1), while f(x) = x² has unbounded derivative (slope 2x). Lipschitz functions — those with bounded derivatives — are always uniformly continuous, because the Lipschitz constant gives a global bound on how much f can vary per unit of x. Uniform continuity fails exactly when this 'rate of change' is unbounded across the domain."
```
