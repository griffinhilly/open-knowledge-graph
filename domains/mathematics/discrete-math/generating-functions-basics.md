---
id: generating-functions-basics
title: Generating Functions
domain: mathematics
course: discrete-math
prerequisites:
- id: power-series
  type: soft
- id: linear-recurrences-homogeneous
  type: soft
builds-toward:
- algorithm-complexity-discrete
tags:
- generating-functions
- power-series
- counting
- manipulation
stage: formal-systems
status: draft
---

# Generating Functions

## Core Idea
A generating function encodes a sequence {aₙ} as a formal power series G(x) = Σ aₙxⁿ. Convolution of generating functions corresponds to counting composite structures. They transform recurrences into algebraic equations, yielding closed forms.

## How It's Best Learned
Build simple generating functions: (1 + x)ⁿ for binomial coefficients, 1/(1−x) for constant sequences. Manipulate series: shift indices, multiply, compose. Solve a recurrence by setting up and solving an equation for G(x).

## Common Misconceptions
Generating functions are formal—convergence is not the point. The notation Σ aₙxⁿ is algebraic manipulation, not analysis.
