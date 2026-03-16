---
id: metric-spaces-definition-examples
title: 'Metric Spaces: Definition and Examples'
domain: mathematics
course: topology
prerequisites:
- id: set-theory-basics
  type: hard
- id: open-and-closed-sets-real-line
  type: soft
builds-toward:
- metric-topology-from-metric
- cauchy-sequences-metric-spaces
tags:
- metric-spaces
- distance
stage: abstract-reasoning
status: draft
---

# Metric Spaces: Definition and Examples

## Core Idea
A metric space (X, d) has a metric d: X × X → ℝ with d(x,y) ≥ 0 (equality iff x=y), symmetry d(x,y) = d(y,x), and triangle inequality d(x,z) ≤ d(x,y) + d(y,z). Examples include ℝⁿ with Euclidean distance, function spaces with supremum norm, and discrete metrics where d(x,y) = 1 for x ≠ y.

## Explainer

You already know open and closed sets on the real line ℝ. That familiar notion of closeness in ℝ comes from the absolute value distance: d(x, y) = |x − y|. A metric space abstracts this idea: it is a set X equipped with a distance function d that can measure how far apart any two elements are, subject to axioms that capture what "distance" must mean to support rigorous analysis.

The three axioms are: (1) **non-negativity with identity** — d(x, y) ≥ 0, with d(x, y) = 0 if and only if x = y (zero distance means you are the same point, nothing else); (2) **symmetry** — d(x, y) = d(y, x) (the distance from A to B equals the distance from B to A); (3) the **triangle inequality** — d(x, z) ≤ d(x, y) + d(y, z) (no detour through an intermediate point can be shorter than going directly). These three conditions are the minimal requirements for "distance" to produce a coherent geometry.

The diversity of examples is what makes the abstraction powerful. The **Euclidean metric** on ℝⁿ, d(x, y) = √(Σ(xᵢ − yᵢ)²), is the standard geometric distance you know from coordinates. The **discrete metric** sets d(x, y) = 1 for any x ≠ y — every pair of distinct points is the same distance apart. In this metric, every singleton {x} is an open ball of radius 1/2, so every subset is open; the discrete metric makes every subset "open" and "closed." The **supremum metric** on continuous functions, d(f, g) = sup_{x∈[a,b]} |f(x) − g(x)|, measures the worst-case pointwise gap between two functions — this is exactly the metric whose convergence notion is uniform convergence.

The abstract axioms unify these disparate examples: any theorem proved from only the three metric axioms applies simultaneously to ℝⁿ, function spaces, sequence spaces, and more. Open balls, convergent sequences, Cauchy sequences, completeness, and compactness all make sense in any metric space. The specific metric you choose for a given set determines which subsets are open, which sequences converge, and which functions are continuous — the entire analytical character of the space flows from d. This is why metric spaces are the natural habitat for real analysis and the first step toward the more general structure of topological spaces.
