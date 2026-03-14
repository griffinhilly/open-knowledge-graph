---
id: composite-quadrature
title: Composite Quadrature Rules
domain: mathematics
course: numerical-analysis
prerequisites:
- id: newton-cotes-formulas
  type: hard
builds-toward:
- gaussian-quadrature
- romberg-integration
tags:
- composite-quadrature
- integration
- error-control
stage: abstract-reasoning
status: draft
---

# Composite Quadrature Rules

## Core Idea
Composite quadrature divides the integration interval into n subintervals and applies a simple rule (e.g., Simpson's rule) to each, summing the results. This approach achieves high accuracy with far fewer function evaluations than using high-order rules on the full interval. Composite rules enable adaptive refinement, with finer divisions in regions where f varies rapidly.

## How It's Best Learned
Compute integrals using composite trapezoidal and Simpson's rules with increasing numbers of subintervals, observing convergence rates and comparing to exact values.

## Common Misconceptions
- Thinking composite rules are less efficient than single high-order rules; composites often win in accuracy-per-evaluation.
- Assuming uniform subinterval spacing is optimal; adaptive methods concentrate evaluations where needed.
