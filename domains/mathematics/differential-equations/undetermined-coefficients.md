---
id: undetermined-coefficients
title: Method of Undetermined Coefficients
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: superposition-principle
  type: soft
builds-toward:
- variation-of-parameters
- higher-order-linear-odes
tags:
- second-order
- non-homogeneous
- method
stage: advanced
status: draft
---

# Method of Undetermined Coefficients

## Core Idea
To solve y'' + py' + qy = g(x) (non-homogeneous), find the general solution to the homogeneous equation (y_h), then guess a particular solution (y_p) based on the form of g(x). The total solution is y = y_h + y_p.

## How It's Best Learned
Learn the ansatz templates: if g(x) = P_n(x)e^{αx}, try y_p = x^s·Q_n(x)e^{αx} where s accounts for resonance. Practice building y_p, then substitute into the ODE to solve for coefficients.

## Common Misconceptions
- Forgetting to check if y_p overlaps with y_h and adjust by multiplying by x (or x²) accordingly. - Using the method when g(x) has forms like ln(x) or 1/x that don't fit standard guesses. - Confusing the coefficient-solving step with the rest of the solution.
