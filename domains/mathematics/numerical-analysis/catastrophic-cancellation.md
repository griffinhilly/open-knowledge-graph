---
id: catastrophic-cancellation
title: Catastrophic Cancellation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: rounding-errors
  type: hard
builds-toward:
- numerical-stability
tags:
- cancellation
- subtraction
- error-amplification
stage: abstract-reasoning
status: draft
---

# Catastrophic Cancellation

## Core Idea
Catastrophic cancellation occurs when subtracting two nearly equal floating point numbers, losing most significant digits in the result. A relative error of 10⁻¹⁶ in the inputs can become an error of magnitude 1 in the output. Recognizing and avoiding this phenomenon through algebraic reformulation is critical for stable algorithms.

## How It's Best Learned
Compute examples like √(x²+1) - √(x²) for large x using direct and rationalized forms to see the difference in accuracy.

## Common Misconceptions
- Thinking all subtraction loses precision equally; only nearly-equal magnitudes cause catastrophic cancellation.
- Assuming higher precision (using doubles instead of floats) solves all cancellation problems; reformulation is often necessary.
