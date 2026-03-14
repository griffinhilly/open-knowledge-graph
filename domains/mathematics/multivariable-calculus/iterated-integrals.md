---
id: iterated-integrals
title: Iterated Integrals and Fubini's Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-cartesian
  type: hard
- id: antiderivatives
  type: hard
- id: u-substitution
  type: soft
builds-toward:
- double-integrals-polar
- triple-integrals
tags:
- Fubini
- iterated-integral
- order-of-integration
- region
stage: formal-systems
status: validated
---

# Iterated Integrals and Fubini's Theorem

## Core Idea
Fubini's theorem states that ∬_R f(x, y) dA = ∫_a^b [∫_{g₁(x)}^{g₂(x)} f(x,y) dy] dx for a region bounded between curves y = g₁(x) and y = g₂(x). The inner integral is computed first, treating x as a constant, producing a function of x alone, which the outer integral then evaluates. The same double integral can be computed by integrating in the opposite order (dx dy), which requires re-describing the region with x expressed in terms of y.

## How It's Best Learned
Mastery requires two skills: computing the iterated integral mechanically, and setting up the correct limits for a given region. Spend equal time on both. Sketching the region of integration is non-negotiable — students who skip the sketch almost always get limits wrong. Practice switching the order of integration on the same region to build flexibility.

## Common Misconceptions
- The inner integral's limits can be functions of the outer variable; the outer limits must be constants.
- Switching the order of integration requires completely re-describing the region — simply swapping dx and dy is incorrect.
- When f(x,y) = p(x)q(y) and R is a rectangle, the double integral factors: ∬ = (∫p(x)dx)(∫q(y)dy). This is a special case, not a general rule.
