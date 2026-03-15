---
id: laplace-transform-definition-and-properties
title: 'Laplace Transform: Definition and Properties'
domain: mathematics
course: differential-equations
prerequisites:
- id: integration-by-parts
  type: hard
- id: improper-integrals-convergence
  type: hard
builds-toward:
- common-laplace-transforms
- inverse-laplace-transform
- laplace-transform-of-derivatives
tags:
- laplace-transform
- integral-transform
- definition
stage: formal-systems
status: draft
---

# Laplace Transform: Definition and Properties

## Core Idea
The Laplace transform of f(t) is F(s) = ∫₀^∞ e^{-st}·f(t) dt (for Re(s) > some threshold). It converts ODEs in the t-domain to algebraic equations in the s-domain, simplifying IVP solution. Key properties: linearity, shifting, scaling, and the derivative rule L{f'} = s·F(s) - f(0).

## How It's Best Learned
Compute Laplace transforms directly from the definition for simple functions like e^{at}, sin(bt), cos(bt). Use property tables to extend to more complex functions.

## Common Misconceptions
- Confusing the Laplace transform with Fourier transform; Laplace includes e^{-st} decay ensuring convergence for larger class of functions. - Forgetting the lower limit is 0, not -∞. - Not paying attention to convergence regions (s > σ, the abscissa of convergence).
