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
