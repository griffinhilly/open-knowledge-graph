---
id: arzela-ascoli-theorem
title: Equicontinuity and the Arzelà-Ascoli Theorem
domain: mathematics
course: real-analysis
prerequisites:
  - id: uniform-convergence
    type: hard
  - id: uniform-continuity
    type: hard
  - id: compact-metric-spaces
    type: hard
  - id: bolzano-weierstrass-theorem
    type: soft
  - id: cantor-diagonalization
    type: soft
builds-toward:
  - compact-operators
tags: [real-analysis, equicontinuity, compactness, function-spaces, uniform-convergence]
stage: advanced
status: validated
---

# Equicontinuity and the Arzelà-Ascoli Theorem

## Core Idea
The Bolzano-Weierstrass theorem says every bounded sequence of real numbers has a convergent subsequence. The Arzelà-Ascoli theorem is the corresponding result for sequences of continuous functions on a compact metric space K. Boundedness alone is not enough; the functions must also be equicontinuous, meaning one δ works for a given ε across the whole family. The theorem states that a pointwise bounded, equicontinuous sequence in C(K) has a uniformly convergent subsequence. In its full form, a subset of C(K) has compact closure in the sup norm exactly when it is bounded and equicontinuous.

## How It's Best Learned
Begin with sequences that are bounded but have no uniformly convergent subsequence, such as xⁿ on [0, 1] and sin(nx) on [0, π], and locate where they fail equicontinuity. Show that a uniform bound on derivatives gives equicontinuity through the Mean Value Theorem. Then walk through the proof in two stages: a diagonal argument gives convergence on a countable dense set, and equicontinuity upgrades it to uniform convergence.

## Common Misconceptions
- A uniformly bounded sequence of continuous functions on [0, 1] has a uniformly convergent subsequence. (fₙ(x) = xⁿ is bounded by 1, but every subsequence converges pointwise to a discontinuous limit, so none converges uniformly.)
- Equicontinuity means each function is uniformly continuous. (Each continuous function on a compact set is uniformly continuous; equicontinuity requires the same δ for every function in the family.)
- The compactness of the domain can be dropped. (On ℝ, the bumps fₙ(x) = max(0, 1 - |x - n|) are bounded and equicontinuous, but no subsequence converges uniformly.)

## Questions

```yaml
- question: "Which family of functions on [0, 1] is equicontinuous?"
  type: multiple-choice
  options:
    - "fₙ(x) = xⁿ for n ≥ 1"
    - "fₙ(x) = sin(nx) for n ≥ 1"
    - "All differentiable f with |f'(x)| ≤ 5 on [0, 1]"
    - "All continuous f with |f(x)| ≤ 5 on [0, 1]"
  answer: 2
  explanation: "By the Mean Value Theorem, |f(x) - f(y)| ≤ 5|x - y| for every such f, so δ = ε/5 works for the whole family. The functions xⁿ become steep near x = 1, sin(nx) oscillates faster as n grows, and a bound on |f| alone does not control how fast f changes."

- question: "Every sequence of continuous functions on [0, 1] satisfying |fₙ(x)| ≤ 1 has a uniformly convergent subsequence."
  type: true-false
  answer: false
  explanation: "fₙ(x) = xⁿ satisfies the bound, but any subsequence converges pointwise to the function that is 0 on [0, 1) and 1 at x = 1. That limit is discontinuous, and a uniform limit of continuous functions must be continuous, so no subsequence converges uniformly. The missing hypothesis is equicontinuity."

- question: "State the definition of equicontinuity for a family F of functions on a metric space K."
  type: short-answer
  answer: "For every ε > 0 there is a δ > 0 such that |f(x) - f(y)| < ε for every f in F and every x, y in K with d(x, y) < δ."
  explanation: "The order of quantifiers is the whole point: δ depends only on ε, not on the particular function f. For a single continuous function on a compact set, this is uniform continuity."

- question: "In the proof of the Arzelà-Ascoli theorem, what role does the diagonal argument play?"
  type: short-answer
  answer: "It extracts a subsequence that converges at every point of a countable dense subset of K."
  explanation: "Pointwise boundedness gives a convergent subsequence at each point of the dense set, one point at a time, and the diagonal subsequence converges at all of them. Equicontinuity and compactness then show this subsequence is uniformly Cauchy on all of K."
```

## Explainer

In ℝ, bounded sequences always have convergent subsequences. In the space C(K) of continuous functions on a compact metric space, measured with the sup norm ‖f‖ = max |f(x)|, this fails. The sequence fₙ(x) = xⁿ on [0, 1] satisfies ‖fₙ‖ = 1, yet no subsequence converges uniformly. Each fₙ is continuous, but the family becomes steeper and steeper near x = 1. A second condition is needed to stop that.

A family F of functions on K is equicontinuous if for every ε > 0 there is a single δ > 0 such that d(x, y) < δ implies |f(x) - f(y)| < ε for every f in F. A single continuous function on a compact set is uniformly continuous, so it has its own δ. Equicontinuity asks that one δ serve the entire family. A common source of equicontinuity is a derivative bound. If |f'| ≤ M for every f in F, the Mean Value Theorem gives |f(x) - f(y)| ≤ M|x - y|, and δ = ε/M works.

The Arzelà-Ascoli theorem. Let K be a compact metric space and (fₙ) a sequence in C(K) that is pointwise bounded and equicontinuous. Then (fₙ) is uniformly bounded and has a uniformly convergent subsequence.

The proof has two stages. A compact metric space has a countable dense subset {x₁, x₂, ...}. At x₁ the numbers fₙ(x₁) are bounded, so Bolzano-Weierstrass gives a subsequence converging at x₁. From that subsequence take a further one converging at x₂, and so on. The diagonal subsequence, whose k-th term is the k-th term of the k-th subsequence, converges at every xⱼ. In the second stage, fix ε and take δ from equicontinuity. By compactness, there is a finite set of the xⱼ such that every point of K is within δ of one of them. For large indices the subsequence is within ε at those finitely many points, and equicontinuity spreads that closeness to all of K. So the subsequence is uniformly Cauchy, and it converges uniformly because C(K) is complete.

The theorem is the standard way to prove compactness in function spaces. It gives the Peano existence theorem for y' = f(t, y) with f only continuous, by extracting a convergent subsequence of approximate solutions. It also shows that integral operators with continuous kernels are compact operators.
