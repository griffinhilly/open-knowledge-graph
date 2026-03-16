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
stage: abstract-reasoning
status: draft
---

# Metric Spaces: Definition and Examples

## Core Idea
A metric space (X, d) is a set X with a distance function d: X × X → ℝ satisfying positivity, symmetry, and triangle inequality. Metrics provide explicit distance structure underlying topological properties.

## Explainer

You already know what sets are: collections of elements with no additional structure. A metric space adds just one thing — a way to measure distance between any two elements. Formally, a **metric** on a set X is a function d: X × X → ℝ satisfying three axioms for all x, y, z ∈ X: (1) d(x, y) ≥ 0, with d(x, y) = 0 if and only if x = y; (2) d(x, y) = d(y, x) (symmetry); and (3) d(x, z) ≤ d(x, y) + d(y, z) (the **triangle inequality**). Each axiom captures something you expect from any reasonable notion of distance: distances are nonnegative, the distance from A to B equals the distance from B to A, and going directly from A to C is never longer than stopping at B along the way.

The axioms are more flexible than they first appear because they apply to wildly different kinds of sets. The familiar case is ℝⁿ with the **Euclidean metric** d(x, y) = √∑(xᵢ − yᵢ)². But consider these alternatives on the same set ℝⁿ: the **taxicab metric** d₁(x, y) = ∑|xᵢ − yᵢ| (add up coordinate differences, like distances along city blocks); or the **max metric** d∞(x, y) = max|xᵢ − yᵢ| (only the largest coordinate difference counts). Both satisfy all three axioms and are therefore valid metrics. Even more striking: the set of all continuous functions on [0,1] becomes a metric space under d(f, g) = sup|f(x) − g(x)|, measuring how far apart two functions are at their worst-case point. Here the "points" are functions, not numbers.

The metric axioms are the minimal conditions needed for the important theorems of analysis to hold. The triangle inequality, in particular, appears constantly: it is what lets you chain together bounds (if x is close to y and y is close to z, then x is close to z). Without it, "closeness" wouldn't be transitive, and the notion of convergence would break down. Every metric space automatically carries a **topology** — the collection of open balls B(x, r) = {y : d(x, y) < r} generates a topology in which the open sets are unions of open balls. This is the **metric topology**, and it is why metric spaces sit inside the broader framework of topological spaces: a metric space is a topological space with extra structure (the distance function) that generates its topology.

Understanding metric spaces is the right starting point for topology because they make the abstract intuitions concrete. When you later define compactness through open covers, or continuity through preimages of open sets, you can check your understanding against the metric-space versions (where compactness means closed and bounded in ℝⁿ, and continuity means the epsilon-delta condition), then gradually shed the distance structure to see what survives in the purely topological setting.
