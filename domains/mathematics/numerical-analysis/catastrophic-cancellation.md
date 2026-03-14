---
id: catastrophic-cancellation
title: Catastrophic Cancellation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: floating-point-representation
  type: hard
- id: machine-epsilon-and-rounding-errors
  type: hard
builds-toward:
- numerical-stability-and-conditioning
- numerical-differentiation
tags:
- cancellation
- loss-of-precision
- subtraction
stage: advanced
status: draft
---

# Catastrophic Cancellation

## Core Idea
Catastrophic cancellation occurs when subtracting two nearly equal numbers, resulting in severe loss of significant digits despite each number being accurately represented. Although each operand may be accurate to machine precision, their difference can have very few correct digits when leading significant figures cancel. This is a major source of error in many numerical algorithms and motivates careful problem reformulation.
