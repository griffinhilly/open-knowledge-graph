---
id: metric-spaces-definition-and-examples
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
- metric-spaces
- distance-functions
- examples
stage: advanced
status: draft
---

# Metric Spaces: Definition and Examples

## Core Idea
A metric space is a set X equipped with a distance function d: X × X → ℝ satisfying three axioms: non-negativity (d(x,y) ≥ 0 with equality iff x = y), symmetry (d(x,y) = d(y,x)), and the triangle inequality (d(x,z) ≤ d(x,y) + d(y,z)). The Euclidean metric on ℝⁿ is the most familiar example, but the discrete metric (d = 0 if equal, 1 otherwise) and the taxicab metric on ℝ² show that the same set can carry very different metrics. Every metric induces a topology via open balls B(x, r) = {y : d(x,y) < r}, making metric spaces a concrete gateway to general topology.

## How It's Best Learned
Verify the three axioms for several concrete metrics—Euclidean, taxicab, discrete, and the sup metric on function spaces. Draw open balls in each to see how different metrics produce different notions of "nearness" on the same underlying set.

## Common Misconceptions
A metric is not the same as a norm—norms require a vector space structure, while metrics apply to any set. Students also sometimes forget that the triangle inequality is doing essential work; without it, the notion of "closeness" becomes incoherent.

## Questions

```yaml
- question: "Define d on the set {cat, dog, fish} by d(x, x) = 0 and d(x, y) = 1 whenever x ≠ y. Is this a valid metric?"
  type: multiple-choice
  options:
    - "No, because distance requires a notion of subtraction, which words do not have"
    - "No, because d(x, y) must depend continuously on x and y"
    - "Yes — it satisfies non-negativity, symmetry, and the triangle inequality (since 1 ≤ 1 + 1)"
    - "Yes, but only if the set has a vector space structure, which this set lacks"
  answer: 2
  explanation: "This is the discrete metric, and it is a perfectly valid metric on any set — including abstract sets of words. Non-negativity: d ≥ 0, and d(x, x) = 0. Symmetry: d(x, y) = d(y, x) by definition. Triangle inequality: d(x, z) ≤ d(x, y) + d(y, z) becomes 1 ≤ 1 + 1 = 2 when x ≠ z, which holds. This example illustrates that a metric is purely axiomatic — it requires no algebraic structure on the underlying set, no continuity, and no connection to subtraction."

- question: "In the taxicab metric on ℝ² defined by d((x₁, y₁), (x₂, y₂)) = |x₁ − x₂| + |y₁ − y₂|, what does the open ball B((0,0), 1) look like geometrically?"
  type: multiple-choice
  options:
    - "A circle of radius 1 centered at the origin, identical to the Euclidean ball"
    - "A square with sides parallel to the axes, with corners at (±1, 0) and (0, ±1)"
    - "A square rotated 45°, with vertices at (±1, 0) and (0, ±1)"
    - "The entire plane, since taxicab distance is always less than Euclidean distance"
  answer: 2
  explanation: "The taxicab ball B((0,0), 1) = {(x, y) : |x| + |y| < 1}. This is a square rotated 45° — a diamond shape — with vertices at (1,0), (0,1), (−1,0), (0,−1). Option B describes a different square (with sides parallel to axes). Option A is the Euclidean ball — a circle. This geometric difference illustrates how the same underlying set (ℝ²) with different metrics generates different open balls and potentially different topologies."

- question: "The same underlying set can carry multiple different metrics, which may produce different notions of 'closeness' and even different topologies."
  type: true-false
  answer: true
  explanation: "This is a central insight: a metric is structure *imposed on* a set, not inherent to it. The Euclidean metric, taxicab metric, and discrete metric on ℝ² are all valid metrics, but they produce different open balls and different families of open sets. The Euclidean and taxicab metrics on ℝ² are actually topologically equivalent (they generate the same open sets), but the discrete metric generates a strictly different topology — every subset is open. The same set, different structures."

- question: "Every metric on a vector space is equivalent to the metric induced by some norm on that space."
  type: true-false
  answer: false
  explanation: "Metrics are more general than norms. A norm requires a vector space and satisfies homogeneity (‖λv‖ = |λ|‖v‖) and the triangle inequality; every norm induces a metric via d(x, y) = ‖x − y‖. But you can put metrics on vector spaces that no norm induces — for instance, the discrete metric on ℝ (d = 0 or 1) cannot come from any norm, since norms scale with scalar multiplication. Metrics apply to any set; norms require vector space structure. The Common Misconceptions section flags this directly."

- question: "Why is the triangle inequality the most essential of the three metric axioms? What would fail about the concept of 'distance' if it were dropped?"
  type: short-answer
  answer: "The triangle inequality d(x, z) ≤ d(x, y) + d(y, z) expresses that the direct route between two points is never longer than going via a detour. Without it, 'closeness' becomes incoherent: you could have x very close to y and y very close to z, yet x and z arbitrarily far apart. This would mean that 'being near' is not transitive in any useful sense, and the topological notion of a limit — where points within ε of a center form a coherent neighborhood — would break down. The triangle inequality is what makes the open ball B(x, r) a sensible notion of 'all points near x.'"
  explanation: "Non-negativity and symmetry are relatively weak requirements. The triangle inequality is the load-bearing axiom that gives metric spaces their geometric and topological character. It ensures that open balls overlap in controlled ways, that sequences can converge meaningfully, and that the induced topology has the Hausdorff property. Removing it produces a structure that fails to behave like distance in any intuitive or mathematically useful sense."
```

