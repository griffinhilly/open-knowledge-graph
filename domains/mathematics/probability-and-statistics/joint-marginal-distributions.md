---
id: joint-marginal-distributions
title: Joint and Marginal Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-definition-types
  type: hard
builds-toward:
- conditional-distributions-of-random-variables
- covariance-between-random-variables
tags:
- joint-distribution
- marginal
stage: formal-systems
status: draft
---

# Joint and Marginal Distributions

## Core Idea
Joint PMF/PDF p(x,y) or f(x,y) specifies the probability of pairs. Marginal distributions sum or integrate out the other variable: p_X(x)=∑_y p(x,y). Two variables are independent iff joint factors into marginals: p(x,y)=p_X(x)p_Y(y).
