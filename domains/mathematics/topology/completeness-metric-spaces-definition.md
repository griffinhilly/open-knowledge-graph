---
id: completeness-metric-spaces-definition
title: Completeness of Metric Spaces
domain: mathematics
course: topology
prerequisites:
- id: cauchy-sequences-metric-spaces
  type: hard
builds-toward:
- contraction-mapping-theorem
- baire-category-metric-spaces
tags:
- completeness
- metric-spaces
stage: formal-systems
status: draft
---

# Completeness of Metric Spaces

## Core Idea
A metric space is complete if every Cauchy sequence converges to a limit within the space. Euclidean space ℝⁿ, the p-adic numbers, and ℓᵖ spaces are complete, while the rationals ℚ and the open interval (0, 1) are not. Completeness means there are no "missing limits"—sequences that should converge have somewhere to land. Key structural results follow: every compact metric space is complete, every closed subset of a complete space is complete, and the Baire category theorem applies only in complete spaces. When a space is incomplete, it can be completed by adding limit points, analogous to how ℝ completes ℚ.

## How It's Best Learned
Construct a Cauchy sequence in ℚ converging to √2 to see incompleteness concretely. Then show the same sequence converges in ℝ. This example makes the abstract definition tangible and motivates why completion is a natural construction.

## Common Misconceptions
Completeness is a metric property, not a topological one—the same set can be complete under one metric and incomplete under another. Students also confuse completeness with compactness; ℝ is complete but not compact. Compactness implies completeness (in metric spaces), but not conversely.

## Explainer

A metric space (X, d) is **complete** if every Cauchy sequence in X converges to a limit that belongs to X. From your study of Cauchy sequences, you know that a sequence (xₙ) is Cauchy if for every ε > 0 there exists N such that d(xₘ, xₙ) < ε for all m, n ≥ N — the terms become arbitrarily close to each other. Completeness guarantees that this internal coherence always produces a target: if the terms are clustering together, there is a point in the space they are clustering toward. A space that lacks this guarantee has "holes" where Cauchy sequences try to converge but find no limit.

The standard example of an incomplete space is the rationals ℚ with the usual metric. The sequence of decimal approximations to √2 — namely 1, 1.4, 1.41, 1.414, ... — is Cauchy in ℚ, since successive terms differ by less than 10⁻ⁿ. But √2 is irrational, so the sequence has no limit within ℚ. The rationals have a "hole" at every irrational number. The real numbers ℝ are precisely the **completion** of ℚ: they are constructed (via Dedekind cuts or equivalence classes of Cauchy sequences) to fill every such hole, making ℝ complete. Another instructive example is the open interval (0, 1) with the standard metric: the sequence xₙ = 1/n is Cauchy but converges to 0, which lies outside the space. The interval is incomplete because its boundary points are missing.

A critical distinction is that completeness is a **metric** property, not a purely topological one. Two spaces can be homeomorphic (topologically identical) yet differ in completeness. The open interval (0, 1) and the entire real line ℝ are homeomorphic via x ↦ tan(π(x − 1/2)), but (0, 1) is incomplete while ℝ is complete. You can even make the same underlying set complete or incomplete by changing the metric: ℝ with the standard metric |x − y| is complete, but ℝ with the metric d(x, y) = |arctan(x) − arctan(y)| is incomplete because the sequence xₙ = n is Cauchy under d yet has no limit. Completeness depends on the specific distance function, not just on which sets are open.

Completeness enables powerful existence theorems. The **Contraction Mapping Theorem** guarantees that any contraction on a complete metric space has a unique fixed point — a result used throughout differential equations, numerical analysis, and computer science. The **Baire Category Theorem** states that a complete metric space cannot be expressed as a countable union of nowhere-dense sets, a result with deep consequences in functional analysis. Every compact metric space is complete (compactness implies completeness), and every closed subset of a complete space is complete. When a space is incomplete, it can always be completed — embedded as a dense subset of a complete space — just as ℚ sits densely inside ℝ.

## Questions

```yaml
- question: "The open interval (0, 1) with the usual metric is incomplete. What is the correct explanation?"
  type: multiple-choice
  options:
    - "The interval is bounded, so sequences cannot converge to a limit"
    - "There are Cauchy sequences in (0, 1) whose limit lies outside the space — e.g., xₙ = 1/n is Cauchy but converges to 0, which is not in (0, 1)"
    - "Cauchy sequences do not exist in (0, 1) because the interval is open"
    - "(0, 1) is incomplete because it is homeomorphic to ℚ"
  answer: 1
  explanation: "Incompleteness means some Cauchy sequences 'want' to converge but have nowhere to land within the space. In (0, 1), the sequence xₙ = 1/n satisfies the Cauchy condition (terms get arbitrarily close) but converges to 0, which is missing from the open interval. The interval is not 'too small' or bounded in a problematic way — it simply has gaps at its boundary. Completeness is about whether limits stay inside the space, not about the space's size or boundedness."

- question: "Consider ℝ equipped with the metric d(x, y) = |arctan(x) − arctan(y)|. Under this metric, ℝ is:"
  type: multiple-choice
  options:
    - "Still complete, because ℝ contains all real numbers"
    - "Compact, because the metric is bounded"
    - "Incomplete, because this metric makes ℝ isometric to the open interval (−π/2, π/2), which is incomplete under the usual metric"
    - "Complete, because completeness is a topological property and ℝ is homeomorphic to itself"
  answer: 2
  explanation: "Completeness is a metric property, not a topological one. Under d(x,y) = |arctan(x) − arctan(y)|, the sequence xₙ = n is Cauchy (since arctan(n) → π/2 and the terms converge in this metric) but has no limit in ℝ under d (there is no real number mapping to π/2 under arctan). So ℝ with this metric is incomplete — even though the underlying set is all of ℝ. The same set, complete under the standard metric, is incomplete under a different metric. This is the key lesson: completeness depends on the metric, not the set."

- question: "Every compact metric space is complete."
  type: true-false
  answer: true
  explanation: "True — compactness implies completeness in metric spaces. If every sequence has a convergent subsequence (sequential compactness), then any Cauchy sequence has a convergent subsequence, and a Cauchy sequence that has a convergent subsequence must itself converge to the same limit. So compactness is the stronger property. However, the converse fails: ℝ is complete but not compact (the sequence 1, 2, 3, ... has no convergent subsequence in ℝ). Compactness implies completeness; completeness does not imply compactness."

- question: "Completeness is a topological property — if two metric spaces are homeomorphic and one is complete, the other must also be complete."
  type: true-false
  answer: false
  explanation: "False — completeness is a metric property, not a topological invariant. The open interval (0, 1) and ℝ are homeomorphic (a homeomorphism is given by f(x) = tan(π(x − 1/2))), yet ℝ is complete and (0, 1) is not. The homeomorphism preserves open sets and continuity but not the Cauchy structure. Two Cauchy sequences in ℝ that map to sequences in (0, 1) under f may fail to converge in (0, 1). Topological equivalence is weaker than metric equivalence — homeomorphisms do not preserve distances or Cauchy sequences."

- question: "Give a concrete example showing that completeness is a property of the metric, not just the underlying set. Use the same set with two different metrics."
  type: short-answer
  answer: "Take the set ℝ with two metrics: the standard metric d(x,y) = |x − y| (complete — every Cauchy sequence converges in ℝ) and the metric d*(x,y) = |arctan(x) − arctan(y)| (incomplete — the sequence xₙ = n is Cauchy under d* since arctan(n) → π/2, but it has no limit in ℝ under d*). The underlying set is identical; only the metric changes, and completeness changes with it."
  explanation: "This example also shows why the completion construction is natural: ℝ under d* is incomplete, and its completion is what you get by formally adding the 'missing' limit points — which corresponds to the compactification that adds ±∞. Completeness is about whether the metric captures enough structure to ensure limits stay inside the space, not about how many points the space has."
```

