---
id: eulers-method-convergence
title: 'Euler''s Method: Error Analysis'
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eulers-method
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- runge-kutta-methods
tags:
- euler-method
- ode
- error-analysis
stage: abstract-reasoning
status: draft
---

# Euler's Method: Error Analysis

## Core Idea
Euler's method y_{n+1} = y_n + hf(t_n, y_n) has local truncation error O(h²) at each step and global error O(h) over a fixed time interval. The method converges as h → 0 under standard Lipschitz conditions, but slowly—halving h halves the error. Understanding error behavior guides practical choices of step size and informs when faster methods are needed.
