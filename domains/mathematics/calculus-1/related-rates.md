---
id: related-rates
title: Related Rates
domain: mathematics
course: calculus-1
prerequisites:
  - id: implicit-differentiation
    type: hard
  - id: chain-rule
    type: hard
builds-toward:
  - optimization-problems
tags: [derivatives, applications, related-rates]
stage: formal-systems
status: validated
---

# Related Rates

## Core Idea
Related rates problems involve two or more quantities that change with respect to time, connected by an equation. You differentiate the equation with respect to time (using implicit differentiation and the chain rule) to relate the rates of change. For example, if a balloon's volume V and radius r are related by V = (4/3)*pi*r^3, then dV/dt = 4*pi*r^2 * dr/dt. This is one of the most important applications of the derivative.

## How It's Best Learned
Follow a systematic process: draw a diagram, identify variables and rates, write the relating equation, differentiate with respect to time, substitute known values, and solve for the unknown rate. Work many examples: ladders, cones filling with water, shadows, expanding circles.

## Common Misconceptions
- Substituting known values before differentiating (this destroys the variable relationships).
- Forgetting that all variables are functions of time t.
- Not correctly identifying what rate is given vs. what rate is asked for.
