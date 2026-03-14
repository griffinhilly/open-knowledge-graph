---
id: newtons-method-convergence-analysis
title: Newton's Method for Root-Finding (Convergence Analysis)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
builds-toward:
- order-of-convergence
tags:
- newtons-method
- root-finding
- quadratic-convergence
stage: advanced
status: draft
---

# Newton's Method for Root-Finding (Convergence Analysis)

## Core Idea
Newton's method approximates roots using x_{n+1} = x_n - f(x_n)/f'(x_n), derived by linearizing f around x_n via Taylor expansion. Near a simple root, the method exhibits quadratic convergence, roughly doubling the number of correct digits with each iteration. However, it requires derivative evaluation and convergence depends on the initial guess.
