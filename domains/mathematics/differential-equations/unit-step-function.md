---
id: unit-step-function
title: Unit Step Function and Piecewise-Defined Forcing
domain: mathematics
course: differential-equations
prerequisites:
- id: laplace-transform-definition-and-properties
  type: hard
- id: piecewise-functions
  type: soft
builds-toward:
- convolution-theorem
tags:
- laplace-transform
- piecewise
- step-function
stage: formal-systems
status: draft
---

# Unit Step Function and Piecewise-Defined Forcing

## Core Idea
The unit step function u(t - a) is 0 for t < a and 1 for t ≥ a. Its Laplace transform L{u(t - a)} = e^{-as}/s handles piecewise-defined forcing terms. The shifting property L{f(t - a)u(t - a)} = e^{-as}F(s) simplifies solving ODEs with discontinuous inputs.
