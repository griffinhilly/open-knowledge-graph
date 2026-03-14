---
id: composite-quadrature-rules
title: Composite Quadrature Rules
domain: mathematics
course: numerical-analysis
prerequisites:
- id: newton-cotes-quadrature
  type: hard
builds-toward:
- romberg-integration
tags:
- composite-rules
- piecewise-integration
- accuracy
stage: advanced
status: draft
---

# Composite Quadrature Rules

## Core Idea
Composite quadrature rules improve accuracy by dividing the integration interval into many subintervals and applying a basic Newton-Cotes rule to each piece. The total error is the sum of subinterval errors, giving O(h^p) convergence where h is the subinterval width. This approach is much more practical than single Newton-Cotes rules with many nodes.
