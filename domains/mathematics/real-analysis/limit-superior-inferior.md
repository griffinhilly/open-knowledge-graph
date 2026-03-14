---
id: limit-superior-inferior
title: Limit Superior and Inferior
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
- id: supremum-infimum
  type: hard
- id: monotone-convergence-theorem
  type: soft
builds-toward:
- uniform-convergence
- root-test
- ratio-test
tags:
- limsup
- liminf
- limits
- convergence
stage: abstract-reasoning
status: draft
---

# Limit Superior and Inferior

## Core Idea
For a bounded sequence (aₙ), the limit superior (limsup aₙ) is the limit of the decreasing sequence of suprema {sup{aₖ : k ≥ n}}, and the limit inferior (liminf aₙ) is the limit of the increasing sequence of infima {inf{aₖ : k ≥ n}}. A sequence converges if and only if limsup aₙ = liminf aₙ.
