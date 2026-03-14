---
id: variation-of-parameters
title: Variation of Parameters Method
domain: mathematics
course: differential-equations
prerequisites:
- id: undetermined-coefficients
  type: hard
- id: wronskian-linear-independence
  type: hard
builds-toward:
- higher-order-linear-odes
tags:
- second-order
- non-homogeneous
- method
stage: advanced
status: draft
---

# Variation of Parameters Method

## Core Idea
Variation of parameters is a general method for finding a particular solution to y'' + p(x)y' + q(x)y = g(x) given two linearly independent solutions y₁, y₂ of the homogeneous equation. The particular solution has the form y_p = u₁(x)y₁ + u₂(x)y₂ where u₁, u₂ are found via integration.

## How It's Best Learned
Derive the formula using the substitution y_p = u₁y₁ + u₂y₂ and the constraint u₁'y₁ + u₂'y₂ = 0. Then apply it to concrete examples, noting that it always works (unlike undetermined coefficients) but may require difficult integrals.

## Common Misconceptions
- Forgetting the constraint equation u₁'y₁ + u₂'y₂ = 0; this is essential, not optional. - Computing the integrals for u₁ and u₂ incorrectly or missing constants of integration. - Confusing the roles of y₁, y₂, y_p, and the final solution y = y_h + y_p.
