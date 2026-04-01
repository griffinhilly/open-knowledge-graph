---
id: metric-spaces-definition-examples
title: 'Metric Spaces: Definition and Examples'
domain: mathematics
course: topology
prerequisites:
- id: set-theory-basics
  type: hard
- id: open-closed-sets-real-line
  type: soft
builds-toward:
- metric-topology-from-metric
- cauchy-sequences-metric-spaces
tags:
- metric-spaces
- distance
stage: formal-systems
status: validated
---

# Metric Spaces: Definition and Examples

## Core Idea
A metric space (X, d) has a metric d: X × X → ℝ with d(x,y) ≥ 0 (equality iff x=y), symmetry d(x,y) = d(y,x), and triangle inequality d(x,z) ≤ d(x,y) + d(y,z). Examples include ℝⁿ with Euclidean distance, function spaces with supremum norm, and discrete metrics where d(x,y) = 1 for x ≠ y.

## Questions

```yaml
- question: "Define d: ℝ × ℝ → ℝ by d(x, y) = (x − y)². Is d a valid metric on ℝ?"
  type: multiple-choice
  options:
    - "Yes — it is non-negative, zero only when x = y, and symmetric"
    - "No — it fails symmetry: d(x, y) ≠ d(y, x) in general"
    - "No — it fails the triangle inequality: d(x, z) can exceed d(x, y) + d(y, z)"
    - "No — it fails non-negativity: squared values can be negative"
  answer: 2
  explanation: "d(x, y) = (x−y)² satisfies non-negativity, the identity condition, and symmetry. However, it fails the triangle inequality. For example: d(0, 2) = 4, but d(0, 1) + d(1, 2) = 1 + 1 = 2 < 4. A detour through 1 is 'shorter' than going directly from 0 to 2 under this function. The triangle inequality is the most substantive of the three axioms — squaring destroys the additive structure it requires."

- question: "In the discrete metric on a set X (where d(x, y) = 1 for x ≠ y and d(x, x) = 0), what does the open ball B(p, r) look like?"
  type: multiple-choice
  options:
    - "For any r > 0, the open ball contains all points within Euclidean distance r of p"
    - "For r ≤ 1, B(p, r) = {p}; for r > 1, B(p, r) = X"
    - "The open ball always contains exactly the two nearest neighbors of p"
    - "Open balls are not defined in the discrete metric because all points are equidistant"
  answer: 1
  explanation: "In the discrete metric every pair of distinct points is distance 1 apart. B(p, r) = {x : d(x, p) < r}. If r ≤ 1, only p itself satisfies d(p, p) = 0 < r, so the ball is just {p}. If r > 1, then d(q, p) = 1 < r for every q ≠ p, so the ball is all of X. This means every singleton {p} is open (take r = 1/2), and therefore every subset of X is open — a radically different topology from the real line."

- question: "The same underlying set can be equipped with different metrics, producing different notions of convergence and different collections of open sets."
  type: true-false
  answer: true
  explanation: "This is one of the central points of the metric space abstraction. On the set of continuous functions on [0, 1], the supremum metric d(f, g) = sup|f(x) − g(x)| defines uniform convergence, while the L² metric defines mean-square convergence. A sequence can converge in one metric but not the other. The metric determines the entire analytical character of the space — the set alone determines none of this."

- question: "The function d(x, y) = |x − y|² is a valid metric on ℝ."
  type: true-false
  answer: false
  explanation: "Despite satisfying non-negativity, identity, and symmetry, d(x, y) = (x − y)² fails the triangle inequality. For x = 0, y = 1, z = 2: d(0, 2) = 4, but d(0, 1) + d(1, 2) = 1 + 1 = 2. Since 4 > 2, the inequality d(x, z) ≤ d(x, y) + d(y, z) is violated. The standard metric d(x, y) = |x − y| is valid; raising to any power greater than 1 typically destroys the triangle inequality on ℝ."

- question: "Why is the triangle inequality the most mathematically significant of the three metric axioms, and what would break down if it failed?"
  type: short-answer
  answer: "The triangle inequality ensures that direct paths are never worse than detours, and that nearness is transitive in the right sense. Without it, a point could be far from p yet very close to something very close to p — making limits, continuity, and Cauchy sequences incoherent. It is what allows open balls to overlap sensibly and enables the entire machinery of analysis."
  explanation: "Non-negativity and symmetry capture basic definitional intuitions about distance. The triangle inequality is the substantive constraint that makes metric geometry work. You can compose paths, estimate distances indirectly, and prove that Cauchy sequences are eventually close to each other — all rely on it. When verifying a proposed metric, the triangle inequality is always the hard and interesting step."
```

## Explainer

You already know open and closed sets on the real line ℝ. That familiar notion of closeness in ℝ comes from the absolute value distance: d(x, y) = |x − y|. A metric space abstracts this idea: it is a set X equipped with a distance function d that can measure how far apart any two elements are, subject to axioms that capture what "distance" must mean to support rigorous analysis.

The three axioms are: (1) **non-negativity with identity** — d(x, y) ≥ 0, with d(x, y) = 0 if and only if x = y (zero distance means you are the same point, nothing else); (2) **symmetry** — d(x, y) = d(y, x) (the distance from A to B equals the distance from B to A); (3) the **triangle inequality** — d(x, z) ≤ d(x, y) + d(y, z) (no detour through an intermediate point can be shorter than going directly). These three conditions are the minimal requirements for "distance" to produce a coherent geometry.

The diversity of examples is what makes the abstraction powerful. The **Euclidean metric** on ℝⁿ, d(x, y) = √(Σ(xᵢ − yᵢ)²), is the standard geometric distance you know from coordinates. The **discrete metric** sets d(x, y) = 1 for any x ≠ y — every pair of distinct points is the same distance apart. In this metric, every singleton {x} is an open ball of radius 1/2, so every subset is open; the discrete metric makes every subset "open" and "closed." The **supremum metric** on continuous functions, d(f, g) = sup_{x∈[a,b]} |f(x) − g(x)|, measures the worst-case pointwise gap between two functions — this is exactly the metric whose convergence notion is uniform convergence.

The abstract axioms unify these disparate examples: any theorem proved from only the three metric axioms applies simultaneously to ℝⁿ, function spaces, sequence spaces, and more. Open balls, convergent sequences, Cauchy sequences, completeness, and compactness all make sense in any metric space. The specific metric you choose for a given set determines which subsets are open, which sequences converge, and which functions are continuous — the entire analytical character of the space flows from d. This is why metric spaces are the natural habitat for real analysis and the first step toward the more general structure of topological spaces.
