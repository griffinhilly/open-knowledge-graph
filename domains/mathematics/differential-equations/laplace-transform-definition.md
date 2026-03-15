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
