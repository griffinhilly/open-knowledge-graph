---
id: chain-rule-multivariable
title: Chain Rule for Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: chain-rule
  type: hard
builds-toward:
- implicit-differentiation
- directional-derivatives-gradient
tags:
- chain-rule
- composition
- derivatives
stage: formal-systems
status: draft
---

# Chain Rule for Multivariable Functions

## Core Idea
If f(x, y) has continuous partials and x = x(t), y = y(t), then df/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt). For compositions like f(g(x, y), h(x, y)), the chain rule tracks how changes propagate through each layer.
