---
id: limit-definition-of-derivative
title: Limit Definition of the Derivative
domain: mathematics
course: calculus-1
prerequisites:
- id: limit-definition-intuitive
  type: hard
- id: rates-of-change-preview
  type: hard
- id: continuity-definition
  type: soft
builds-toward:
- derivative-as-slope-of-tangent
- power-rule
tags:
- derivatives
- definition
- difference-quotient
stage: formal-systems
status: validated
---
# Limit Definition of the Derivative

## Core Idea
The derivative of f at x = a is defined as f'(a) = lim(h->0) (f(a + h) - f(a))/h, the limit of the difference quotient. This single formula captures the instantaneous rate of change by taking the average rate of change over a shrinking interval. When this limit exists, the function is said to be differentiable at a. Every derivative rule you will learn is a shortcut derived from this definition.

## How It's Best Learned
Compute derivatives from the definition for simple functions: f(x) = x^2, f(x) = 1/x, f(x) = sqrt(x). Show the algebra step by step, emphasizing how the h in the denominator cancels. Connect each computation to the slope of the tangent line. Then motivate the need for shortcut rules (the definition is correct but slow).

## Common Misconceptions
- Setting h = 0 instead of taking the limit as h approaches 0 (division by zero).
- Forgetting to expand (a + h)^n correctly.
- Believing the derivative exists everywhere just because the function is defined everywhere (absolute value at 0 is a counterexample).
