---
id: machine-epsilon
title: Machine Epsilon and Unit Roundoff
domain: mathematics
course: numerical-analysis
prerequisites:
- id: floating-point-representation
  type: hard
builds-toward:
- rounding-errors
- numerical-stability
tags:
- machine-epsilon
- precision
- floating-point
stage: abstract-reasoning
status: draft
---

# Machine Epsilon and Unit Roundoff

## Core Idea
Machine epsilon is the smallest positive number such that 1 + ε ≠ 1 in floating point arithmetic, quantifying the relative precision of a computer's number system. It determines the accuracy threshold for all numerical computations. For double-precision arithmetic, machine epsilon is approximately 2.22 × 10⁻¹⁶.
