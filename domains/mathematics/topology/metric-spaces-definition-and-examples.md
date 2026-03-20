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

