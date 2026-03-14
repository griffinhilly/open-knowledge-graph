---
id: machine-epsilon-and-rounding-errors
title: Machine Epsilon and Rounding Errors
domain: mathematics
course: numerical-analysis
prerequisites:
- id: floating-point-representation
  type: hard
builds-toward:
- catastrophic-cancellation
- numerical-stability-and-conditioning
tags:
- machine-epsilon
- rounding
- error-analysis
stage: advanced
status: draft
---

# Machine Epsilon and Rounding Errors

## Core Idea
Machine epsilon is the smallest positive number ε such that 1 + ε ≠ 1 in floating point arithmetic, quantifying the relative error in number representation. It characterizes the precision limit of the floating point system and allows us to estimate rounding errors in arithmetic operations. Understanding machine epsilon enables prediction and control of accumulated errors in numerical computations.
