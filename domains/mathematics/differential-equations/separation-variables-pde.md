---
id: separation-variables-pde
title: Separation of Variables for Partial Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: heat-equation-pde
  type: hard
- id: systems-first-order-linear-odes
  type: soft
builds-toward:
- wave-equation-pde
tags:
- separation-variables
- pde
- method
stage: advanced
status: draft
---

# Separation of Variables for Partial Differential Equations

## Core Idea
Separation of variables assumes u(x,t) = X(x)T(t) as a product. Substituting into a PDE yields an equation where one side depends only on x and the other only on t; both must equal a constant. This reduces the PDE into ODEs for X and T solvable separately. Superposing solutions for multiple separation constants yields the general solution.
