---
id: derivatives-of-logarithmic-functions
title: Derivatives of Logarithmic Functions
domain: mathematics
course: calculus-1
prerequisites:
  - id: derivatives-of-exponential-functions
    type: hard
  - id: logarithmic-functions-review
    type: hard
  - id: chain-rule
    type: hard
builds-toward:
  - implicit-differentiation
tags: [derivatives, logarithmic]
stage: formal-systems
status: validated
---

# Derivatives of Logarithmic Functions

## Core Idea
The derivative of the natural logarithm is d/dx[ln(x)] = 1/x. For a general base, d/dx[log_b(x)] = 1/(x * ln(b)). With the chain rule, d/dx[ln(g(x))] = g'(x)/g(x). Logarithmic differentiation is a technique where you take ln of both sides before differentiating, which simplifies products, quotients, and variable exponents. The result d/dx[ln(x)] = 1/x is also why the integral of 1/x is ln|x| + C.

## How It's Best Learned
Derive d/dx[ln(x)] using inverse function differentiation: if y = ln(x), then e^y = x, differentiate implicitly. Practice chain rule applications: ln(x^2 + 1), ln(sin(x)). Introduce logarithmic differentiation for expressions like x^x or (x^2 + 1)^(sin(x)).

## Common Misconceptions
- Forgetting the chain rule: d/dx[ln(2x)] = 1/x (the 2 cancels), but d/dx[ln(x^2)] = 2/x.
- Confusing d/dx[ln(x)] = 1/x with d/dx[e^x] = e^x.
- Not recognizing when logarithmic differentiation simplifies a problem.

## Explainer

You know that d/dx[eˣ] = eˣ — the exponential function is its own derivative. The natural logarithm ln(x) is the **inverse function** of eˣ, and that relationship lets you derive its derivative without memorizing anything new. Set y = ln(x), so eʸ = x. Differentiate both sides with respect to x (using the chain rule on the left): eʸ · (dy/dx) = 1. Solve for dy/dx: dy/dx = 1/eʸ = 1/x. That's it — **d/dx[ln(x)] = 1/x**. This result is geometrically sensible: the slope of y = ln(x) is large and positive near x = 0 (the curve rises steeply) and approaches 0 as x grows (the curve flattens). The function 1/x captures exactly that behavior.

The **chain rule** upgrades this to composite functions. If u = g(x) is a differentiable function, then d/dx[ln(g(x))] = g'(x)/g(x). The derivative of the argument appears in the numerator; the argument itself stays in the denominator. Examples: d/dx[ln(x² + 1)] = 2x/(x² + 1), and d/dx[ln(sin(x))] = cos(x)/sin(x) = cot(x). For general bases, d/dx[log_b(x)] = 1/(x · ln(b)), which follows from rewriting log_b(x) = ln(x)/ln(b) and differentiating. The ln(b) factor in the denominator explains why natural logarithms (base e) are "natural" for calculus — the ln(e) = 1 makes the formula simplest.

**Logarithmic differentiation** is the technique that makes d/dx[ln(x)] = 1/x genuinely powerful beyond its own derivative. When you need to differentiate a complicated product, quotient, or function with a variable in the exponent — like f(x) = xˣ or f(x) = (x²+1)^(sin x) — take the natural log of both sides first: ln(f) = sin(x)·ln(x²+1). Now differentiate both sides (using the chain rule on the left: f'/f) and solve for f'. This technique converts exponential, product, and power relationships into additions and subtractions, which are far easier to handle. The result f'/f is called the **logarithmic derivative**, and it appears throughout calculus and beyond — in probability, physics, and the study of functions with multiplicative structure.
