---
id: order-of-convergence
title: Order of Convergence
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
builds-toward:
- runge-kutta-methods-for-odes
tags:
- convergence-rate
- linear-convergence
- quadratic-convergence
stage: advanced
status: draft
---

# Order of Convergence

## Core Idea
The order of convergence p characterizes how fast an iterative sequence approaches its limit: |e_{n+1}| ≈ C|e_n|^p. Linear convergence (p=1) means a fixed number of digits gained per iteration; quadratic (p=2) means digits roughly double. Higher order convergence is desirable but often requires more computation per iteration.
