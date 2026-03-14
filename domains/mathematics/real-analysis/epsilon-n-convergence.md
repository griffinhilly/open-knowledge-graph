---
id: epsilon-n-convergence
title: 'Sequences: Epsilon-N Convergence'
domain: mathematics
course: real-analysis
prerequisites:
- id: sequences-intro
  type: hard
- id: limit-laws
  type: hard
- id: archimedean-property
  type: soft
builds-toward:
- monotone-convergence-theorem
- cauchy-sequences-completeness
- limit-superior-inferior
tags:
- sequences
- convergence
- limits
- epsilon-n
stage: abstract-reasoning
status: draft
---

# Sequences: Epsilon-N Convergence

## Core Idea
A sequence (aₙ) converges to L if for every ε > 0, there exists an N such that for all n > N, |aₙ − L| < ε. This is the rigorous epsilon-N definition of convergence, making precise the intuitive idea that terms get arbitrarily close to the limit. It is the foundation for all rigorous limit proofs in analysis.
