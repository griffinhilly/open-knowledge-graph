---
id: metric-spaces-definition
title: 'Metric Spaces: Definition and Examples'
domain: mathematics
course: topology
prerequisites:
- id: set-theory-basics
  type: hard
builds-toward:
- metric-topology
- completeness-metric-spaces
tags:
- metric
- distance
stage: formal-systems
status: draft
---

# Metric Spaces: Definition and Examples

## Core Idea
A metric space (X, d) is a set X with a distance function d: X × X → ℝ satisfying positivity, symmetry, and triangle inequality. Metrics provide explicit distance structure underlying topological properties.

## Questions

```yaml
- question: "A student proposes d(x, y) = (x − y)² as a metric on ℝ. She notes it is always nonnegative, equals zero only when x = y, and is symmetric. Is this a valid metric?"
  type: multiple-choice
  options:
    - "Yes — all three metric axioms are satisfied"
    - "No — it fails positivity because (x − y)² can be arbitrarily large"
    - "No — it fails the triangle inequality: d(0, 2) = 4, but d(0, 1) + d(1, 2) = 1 + 1 = 2 < 4"
    - "No — squaring is not a symmetric operation, so the symmetry axiom fails"
  answer: 2
  explanation: "Positivity and symmetry both hold, but the triangle inequality fails. d(0, 2) = 4, while d(0, 1) + d(1, 2) = 1 + 1 = 2. Since 4 > 2, the requirement d(x, z) ≤ d(x, y) + d(y, z) is violated. Passing two out of three axioms is not enough — all three must hold. The triangle inequality is often the hardest to verify and the most commonly violated by plausible-seeming distance functions."

- question: "The set of continuous functions on [0,1] with d(f, g) = sup|f(x) − g(x)| forms a metric space. What does this example most directly illustrate?"
  type: multiple-choice
  options:
    - "Metric spaces only work for finite-dimensional real vector spaces like ℝⁿ"
    - "The supremum norm is always the most natural metric for function spaces"
    - "The metric axioms are flexible enough to apply to sets whose 'points' are functions, not just numbers"
    - "Any set equipped with a supremum operation automatically satisfies the metric axioms"
  answer: 2
  explanation: "The 'points' in this metric space are functions — infinite-dimensional objects. d(f, g) measures the worst-case gap between two functions. All three axioms hold: d(f, g) ≥ 0, it equals 0 iff f = g everywhere, it is symmetric, and the triangle inequality holds for suprema. The key message is that the three axioms are an abstract template that applies to any reasonable notion of distance, regardless of what the 'points' are — numbers, vectors, functions, or anything else."

- question: "Every metric space is automatically a topological space."
  type: true-false
  answer: true
  explanation: "A metric generates a topology: the open balls B(x, r) = {y : d(x, y) < r} form a basis for a topology on X, and open sets are unions of open balls. This metric topology satisfies all topological axioms. The converse is false — not every topological space has a metric that generates it (non-metrizable spaces exist). Metric spaces are topological spaces with extra structure (an explicit distance function), which is why studying them first gives concrete intuition for the more abstract topological setting."

- question: "The triangle inequality is the least important metric axiom because it merely captures an obvious geometric fact about straight-line distances."
  type: true-false
  answer: false
  explanation: "The triangle inequality is arguably the most important axiom. It makes 'closeness' transitive: if x is close to y and y is close to z, then x must be reasonably close to z. This transitivity is essential for convergence — without it, you couldn't chain together bounds or conclude that a sequence approaching a limit stays near it. Positivity and symmetry are sanity conditions; the triangle inequality is the structural condition that makes the distance function useful for proving theorems in analysis."

- question: "Why is the triangle inequality the 'load-bearing' axiom of the metric space definition — what breaks down if you remove it?"
  type: short-answer
  answer: "The triangle inequality makes closeness transitive: if d(x, y) < ε and d(y, z) < ε, then d(x, z) < 2ε. Without it, two points each 'close' to a third need not be close to each other, which breaks the concept of convergence. A sequence could have each term close to the limit but terms arbitrarily far from each other, destroying Cauchy-type arguments. Most bounding arguments in analysis chain inequalities of the form d(a, c) ≤ d(a, b) + d(b, c); this structure depends entirely on the triangle inequality."
  explanation: "Positivity says distances are nonnegative; symmetry says direction doesn't matter. These are sanity checks. The triangle inequality is the condition that makes the distance function structurally useful — it ensures open balls behave like neighborhoods, that limits are unique, and that convergence is a meaningful concept worth studying."
```

## Explainer

You already know what sets are: collections of elements with no additional structure. A metric space adds just one thing — a way to measure distance between any two elements. Formally, a **metric** on a set X is a function d: X × X → ℝ satisfying three axioms for all x, y, z ∈ X: (1) d(x, y) ≥ 0, with d(x, y) = 0 if and only if x = y; (2) d(x, y) = d(y, x) (symmetry); and (3) d(x, z) ≤ d(x, y) + d(y, z) (the **triangle inequality**). Each axiom captures something you expect from any reasonable notion of distance: distances are nonnegative, the distance from A to B equals the distance from B to A, and going directly from A to C is never longer than stopping at B along the way.

The axioms are more flexible than they first appear because they apply to wildly different kinds of sets. The familiar case is ℝⁿ with the **Euclidean metric** d(x, y) = √∑(xᵢ − yᵢ)². But consider these alternatives on the same set ℝⁿ: the **taxicab metric** d₁(x, y) = ∑|xᵢ − yᵢ| (add up coordinate differences, like distances along city blocks); or the **max metric** d∞(x, y) = max|xᵢ − yᵢ| (only the largest coordinate difference counts). Both satisfy all three axioms and are therefore valid metrics. Even more striking: the set of all continuous functions on [0,1] becomes a metric space under d(f, g) = sup|f(x) − g(x)|, measuring how far apart two functions are at their worst-case point. Here the "points" are functions, not numbers.

The metric axioms are the minimal conditions needed for the important theorems of analysis to hold. The triangle inequality, in particular, appears constantly: it is what lets you chain together bounds (if x is close to y and y is close to z, then x is close to z). Without it, "closeness" wouldn't be transitive, and the notion of convergence would break down. Every metric space automatically carries a **topology** — the collection of open balls B(x, r) = {y : d(x, y) < r} generates a topology in which the open sets are unions of open balls. This is the **metric topology**, and it is why metric spaces sit inside the broader framework of topological spaces: a metric space is a topological space with extra structure (the distance function) that generates its topology.

Understanding metric spaces is the right starting point for topology because they make the abstract intuitions concrete. When you later define compactness through open covers, or continuity through preimages of open sets, you can check your understanding against the metric-space versions (where compactness means closed and bounded in ℝⁿ, and continuity means the epsilon-delta condition), then gradually shed the distance structure to see what survives in the purely topological setting.
