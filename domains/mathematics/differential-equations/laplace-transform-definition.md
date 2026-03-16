---
id: laplace-transform-definition
title: 'Laplace Transform: Definition and Properties'
domain: mathematics
course: differential-equations
prerequisites:
- id: improper-integrals-convergence
  type: hard
- id: exponential-functions-and-graphs
  type: hard
builds-toward:
- common-laplace-transforms
- inverse-laplace-transform
tags:
- laplace-transform
- integral-transform
- definition
stage: formal-systems
status: draft
---

# Laplace Transform: Definition and Properties

## Core Idea
The Laplace transform converts f(t) to F(s) = ∫₀^∞ e^(-st)f(t)dt, mapping time-domain differential equations to frequency-domain algebra. Key properties: linearity, the derivative rule L[f'(t)] = sF(s) - f(0), and shifting theorems. These transform initial conditions into the equation automatically, making Laplace transforms powerful for solving IVPs, especially with discontinuous forcing functions.

## Explainer

You've already studied improper integrals and know that ∫₀^∞ e^(−at) dt converges for a > 0. The **Laplace transform** wraps that convergence trick into a machine for solving differential equations. Given a function f(t) defined for t ≥ 0, the transform is ℒ{f}(s) = F(s) = ∫₀^∞ e^(−st) f(t) dt. The exponential e^(−st) acts as a damping factor: for large enough s, it forces the integral to converge even if f(t) grows (as long as f doesn't grow faster than some exponential). The output F(s) is a new function of the parameter s.

The whole point of the transform is the **derivative rule**: ℒ{f′(t)} = sF(s) − f(0). Differentiation in t becomes multiplication by s in the s-domain, with the initial condition f(0) appearing algebraically. For a second derivative: ℒ{f″(t)} = s²F(s) − sf(0) − f′(0). Every derivative lowers the problem by one degree. So a second-order ODE like f″ + 3f′ + 2f = g(t) with initial conditions f(0) = a, f′(0) = b transforms into a purely algebraic equation in F(s) and G(s) = ℒ{g}. Solve for F(s), then transform back. The initial conditions are absorbed automatically — no separate step needed to impose them.

**Linearity** ℒ{αf + βg} = αF + βG follows directly from linearity of integration and lets you handle sums of functions term by term. The **s-shifting theorem** says ℒ{e^(at)f(t)} = F(s − a): multiplying by an exponential in t shifts the argument in s. This handles forcing functions with exponential growth or decay. The **t-shifting theorem** ℒ{u_c(t)f(t − c)} = e^(−cs)F(s) handles functions that "switch on" at time t = c, where u_c is the unit step function. This is where the Laplace transform genuinely outperforms variation of parameters — discontinuous forcing functions like step functions and impulses are handled with almost no extra complexity.

The Laplace transform establishes convergence for Re(s) > some abscissa of convergence. For polynomials, ℒ{tⁿ} = n!/s^(n+1) for s > 0; for exponentials, ℒ{e^(at)} = 1/(s − a) for s > a. These basic transforms, combined with the linearity and shifting properties, form a table that covers almost every forcing function you'll encounter. The transform method's procedure is always the same: transform the ODE → solve the algebraic equation for F(s) → apply partial fractions and the table → invert back to f(t).
