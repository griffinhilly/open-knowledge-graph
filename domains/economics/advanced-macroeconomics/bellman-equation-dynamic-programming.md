---
id: bellman-equation-dynamic-programming
title: Bellman Equation and Dynamic Programming
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: constrained-optimization
  type: hard
- id: differential-equations
  type: hard
- id: constrained-optimization-lagrange
  type: soft
- id: recursive-definitions
  type: soft
builds-toward:
- euler-equation-intertemporal-choice
- solow-growth-model
tags:
- dynamic-optimization
- recursive-methods
- foundations
stage: advanced
status: draft
---

# Bellman Equation and Dynamic Programming

## Core Idea
The Bellman equation decomposes a dynamic optimization problem into current period and future components: V(x) = max[u(c,x) + βV(x')]. This recursive formulation enables solving infinite-horizon problems and characterizing optimal consumption, investment, and labor supply decisions over time.
