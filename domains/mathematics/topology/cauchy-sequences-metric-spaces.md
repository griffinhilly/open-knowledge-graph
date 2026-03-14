---
id: cauchy-sequences-metric-spaces
title: Cauchy Sequences in Metric Spaces
domain: mathematics
course: topology
prerequisites:
- id: metric-topology-from-metric
  type: hard
- id: cauchy-sequences-and-completeness
  type: soft
builds-toward:
- completeness-metric-spaces-definition
tags:
- cauchy-sequences
- convergence
stage: abstract-reasoning
status: draft
---

# Cauchy Sequences in Metric Spaces

## Core Idea
A sequence (xₙ) is Cauchy if for every ε > 0 there exists N such that d(xₙ, xₘ) < ε for all n,m > N. In ℝ every Cauchy sequence converges (completeness). In ℚ or incomplete spaces, Cauchy sequences may fail to converge. Cauchy sequences measure whether terms 'cluster' without requiring a limit point.
