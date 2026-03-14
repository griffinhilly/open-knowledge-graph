---
id: newton-cotes-quadrature
title: Newton-Cotes Quadrature
domain: mathematics
course: numerical-analysis
prerequisites:
- id: lagrange-polynomial-interpolation
  type: hard
builds-toward:
- composite-quadrature-rules
- romberg-integration
tags:
- numerical-integration
- quadrature
- newton-cotes
stage: advanced
status: draft
---

# Newton-Cotes Quadrature

## Core Idea
Newton-Cotes quadrature rules approximate integrals using weighted sums of function values at equally-spaced nodes, with weights determined by integrating the Lagrange interpolating polynomial. Common examples are the trapezoidal rule (2 nodes, degree 1 accuracy) and Simpson's rule (3 nodes, degree 3 accuracy). Closed formulas include endpoints; open formulas exclude them.
