---
id: systems-of-first-order-linear-odes
title: Systems of First-Order Linear Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: first-order-linear-odes
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- matrix-exponential-method
- eigenvalue-method-for-systems
- higher-order-linear-odes
tags:
- systems
- linear
- matrix-form
stage: formal-systems
status: draft
---

# Systems of First-Order Linear Differential Equations

## Core Idea
A system of first-order linear ODEs can be written in matrix form: y' = Ay + b(t), where y is a vector, A is a matrix, and b(t) is a forcing vector. This unified framework handles coupled equations and higher-order ODEs (converted to systems) via eigenvalue analysis.
