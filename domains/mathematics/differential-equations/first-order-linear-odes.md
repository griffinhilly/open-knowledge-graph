---
id: first-order-linear-odes
title: First-Order Linear Ordinary Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: integrating-factor-method
  type: hard
- id: antiderivatives
  type: hard
builds-toward:
- higher-order-linear-odes
- systems-first-order-linear-odes
tags:
- first-order
- linear
- fundamental
stage: advanced
status: draft
---

# First-Order Linear Ordinary Differential Equations

## Core Idea
A first-order linear ODE has the form dy/dx + P(x)y = Q(x). The general solution is y = c·e^(-∫P(x)dx) + e^(-∫P(x)dx)∫Q(x)e^(∫P(x)dx)dx, consisting of a homogeneous part and a particular solution. These equations are fundamental throughout applied mathematics and physics, modeling everything from radioactive decay to chemical reactions.
