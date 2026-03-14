---
id: fundamental-theorem-line-integrals
title: Fundamental Theorem for Line Integrals
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: conservative-fields
  type: hard
- id: fundamental-theorem-of-calculus-part-2
  type: hard
builds-toward:
- greens-theorem
- stokes-theorem
tags:
- fundamental-theorem
- line-integral
- conservative
- potential
stage: formal-systems
status: validated
---

# Fundamental Theorem for Line Integrals

## Core Idea
If F = ∇f is a conservative vector field with potential function f, then ∫_C F · dr = f(r(b)) − f(r(a)), where r(a) and r(b) are the start and end points of C. This is the multivariable analogue of the Fundamental Theorem of Calculus: integration of a 'derivative' (the gradient) depends only on boundary values. It reduces line integrals of conservative fields from path-dependent computations to simple function evaluations.

## How It's Best Learned
Present this as the direct multivariable generalization of FTC: just as ∫_a^b f′(x) dx = f(b) − f(a), we have ∫_C ∇f · dr = f(end) − f(start). Practice finding potential functions first, then applying the theorem. Students should internalize that for conservative fields, only the endpoints matter.

## Common Misconceptions
- The theorem applies only to conservative fields (F = ∇f). For non-conservative fields, the integral must be computed directly.
- The potential function f must be evaluated at the endpoints of C, not integrated over C.
- The theorem requires finding f explicitly; the test ∂P/∂y = ∂Q/∂x confirms conservativeness but doesn't supply f.
