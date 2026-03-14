---
id: least-squares-approximation
title: Least Squares Approximation and Normal Equations
domain: mathematics
course: linear-algebra
prerequisites:
- id: gram-schmidt-process
  type: hard
- id: systems-of-linear-equations
  type: hard
tags:
- least squares
- approximation
- normal equations
stage: formal-systems
status: draft
---

# Least Squares Approximation and Normal Equations

## Core Idea
For an inconsistent system Ax = b, the least squares solution minimizes ||Ax − b||². The solution satisfies A^T Ax = A^T b (the normal equations), giving x̂ = (A^T A)^{-1} A^T b when A has full column rank. Least squares finds the best approximation when exact solutions don't exist, essential in statistics and data fitting.
