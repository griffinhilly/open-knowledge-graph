---
id: wronskian-linear-independence
title: The Wronskian and Linear Independence
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: determinants-2x2-3x3
  type: hard
builds-toward:
- variation-of-parameters
- higher-order-linear-odes
tags:
- second-order
- independence
- linear-algebra
stage: advanced
status: draft
---

# The Wronskian and Linear Independence

## Core Idea
The Wronskian W(y₁, y₂) = y₁y₂' - y₁'y₂ is a determinant-based test for linear independence of two solutions. If W ≠ 0 on an interval, y₁ and y₂ are linearly independent, ensuring that y = c₁y₁ + c₂y₂ is the general solution.

## How It's Best Learned
Compute the Wronskian for pairs of solutions (exponentials, polynomials, trig functions). Verify Abel's formula: W(y₁, y₂) = ce^{-∫p(x)dx} for y'' + p(x)y' + q(x)y = 0.

## Common Misconceptions
- Thinking W = 0 proves linear dependence everywhere; it only does so in a continuous region. - Forgetting that W and linear independence are tied to the differential equation context, not just any functions. - Computing the determinant incorrectly due to sign errors in the cross-product terms.
