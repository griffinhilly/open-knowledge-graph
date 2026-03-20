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

