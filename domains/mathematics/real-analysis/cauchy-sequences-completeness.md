---
id: cauchy-sequences-completeness
title: Cauchy Sequences and Completeness
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
builds-toward:
- metric-space-topology
tags:
- cauchy
- completeness
- convergence
stage: advanced
status: draft
---

# Cauchy Sequences and Completeness

## Core Idea
A sequence (aₙ) is Cauchy if for every ε > 0, there exists N such that n, m > N implies |aₙ - aₘ| < ε. In ℝ, a sequence converges if and only if it is Cauchy. This characterization requires no knowledge of the limit beforehand, making it powerful for existence proofs. ℝ is 'complete' because Cauchy sequences always converge.
