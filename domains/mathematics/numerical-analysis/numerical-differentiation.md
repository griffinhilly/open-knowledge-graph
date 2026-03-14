---
id: numerical-differentiation
title: Numerical Differentiation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
builds-toward:
- richardsons-extrapolation
tags:
- numerical-derivatives
- finite-differences
- error-analysis
stage: advanced
status: draft
---

# Numerical Differentiation

## Core Idea
Numerical differentiation approximates derivatives using finite difference formulas like forward (f(x+h)-f(x))/h or central (f(x+h)-f(x-h))/(2h). There is a fundamental trade-off: smaller h reduces truncation error from Taylor approximation but increases rounding error from floating-point arithmetic. Optimal h balances these competing errors.
