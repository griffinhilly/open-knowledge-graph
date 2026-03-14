---
id: euler-method-error-analysis
title: Euler's Method for ODEs (Error Analysis)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eulers-method
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- runge-kutta-methods-for-odes
tags:
- euler-method
- ode-solving
- truncation-error
stage: advanced
status: draft
---

# Euler's Method for ODEs (Error Analysis)

## Core Idea
Euler's method y_{n+1} = y_n + h*f(x_n, y_n) has local truncation error O(h²) and global error O(h) by Taylor expansion analysis. The local error at each step accumulates over the integration interval, and the total accumulated error grows linearly with integration length. Understanding this trade-off guides appropriate step size selection.
