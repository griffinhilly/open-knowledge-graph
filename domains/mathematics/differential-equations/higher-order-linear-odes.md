---
id: higher-order-linear-odes
title: Higher-Order Linear Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: undetermined-coefficients
  type: hard
- id: variation-of-parameters
  type: soft
builds-toward:
- systems-first-order-linear-odes
tags:
- higher-order
- linear
- nth-order
stage: advanced
status: draft
---

# Higher-Order Linear Differential Equations

## Core Idea
An nth-order linear ODE has the form y^(n) + a_{n-1}y^(n-1) + ... + a₁y' + a₀y = f(x). The same principles apply: combine n linearly independent homogeneous solutions and add a particular solution. For constant coefficients, the characteristic equation becomes a polynomial of degree n. Higher-order equations arise naturally when modeling complex mechanical and electrical systems.
