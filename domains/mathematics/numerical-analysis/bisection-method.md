---
id: bisection-method
title: Bisection Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: mean-value-theorem
  type: hard
builds-toward:
- order-of-convergence
tags:
- root-finding
- bracketing
- convergence
stage: advanced
status: draft
---

# Bisection Method

## Core Idea
The bisection method finds a root of a continuous function by repeatedly halving an interval where the function changes sign, guaranteed by the Intermediate Value Theorem. At each iteration, the function is evaluated at the midpoint and the appropriate half-interval is retained. The method is slow but guaranteed to converge for continuous functions and is extremely robust.
