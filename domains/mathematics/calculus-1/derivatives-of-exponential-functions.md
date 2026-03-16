---
id: derivatives-of-exponential-functions
title: Derivatives of Exponential Functions
domain: mathematics
course: calculus-1
prerequisites:
  - id: chain-rule
    type: hard
  - id: exponential-functions-review
    type: hard
builds-toward:
  - derivatives-of-logarithmic-functions
  - differential-equations-intro-separable
tags: [derivatives, exponential]
stage: formal-systems
status: validated
---

# Derivatives of Exponential Functions

## Core Idea
The natural exponential function has the remarkable property that d/dx[e^x] = e^x: it is its own derivative. For a general base, d/dx[b^x] = b^x * ln(b). With the chain rule, d/dx[e^(g(x))] = e^(g(x)) * g'(x). This property makes e^x the most important function in calculus and differential equations, because exponential growth/decay is the solution to dy/dx = ky.

## How It's Best Learned
Motivate by showing that the limit definition yields e^x back. Compare with other bases to see why ln(b) appears. Practice with chain rule applications: e^(3x), e^(-x^2), 2^(sin(x)). Connect to growth/decay problems.

## Common Misconceptions
- Applying the power rule to e^x (it is not x * e^(x-1)).
- Forgetting the chain rule: d/dx[e^(2x)] = 2e^(2x), not e^(2x).
- Confusing d/dx[e^x] with d/dx[x^e] (the latter uses the power rule since e is a constant).

## Questions

```yaml
- question: "What is d/dx[e^(3x²)]?"
  type: multiple-choice
  options:
    - "e^(3x²)"
    - "3e^(3x²)"
    - "6x·e^(3x²)"
    - "3x²·e^(3x²)"
  answer: 2
  explanation: "By the chain rule, d/dx[e^(g(x))] = e^(g(x))·g'(x). Here g(x) = 3x², so g'(x) = 6x. Therefore d/dx[e^(3x²)] = 6x·e^(3x²). Forgetting the chain rule factor gives just e^(3x²) (option 0). Using 3 instead of 6 (from differentiating x² as x) gives option 1."

- question: "The derivative of 2^x is the same as the derivative of e^x because both are exponential functions."
  type: true-false
  answer: false
  explanation: "d/dx[e^x] = e^x, but d/dx[2^x] = 2^x·ln(2). Only the base e has the property that ln(e) = 1, making the correction factor disappear. For any other base b, the factor ln(b) appears. This is precisely what makes e the natural base for calculus."

- question: "Explain why the power rule cannot be used to differentiate e^x, and state the correct derivative."
  type: short-answer
  answer: "The power rule d/dx[x^n] = n·x^(n-1) applies when the variable is the base and the exponent is a constant. In e^x, the variable x is the exponent and e is the constant base — the roles are reversed. The correct derivative is d/dx[e^x] = e^x."
  explanation: "Applying the power rule incorrectly would give x·e^(x-1), which is wrong. The confusion often arises because x^e (power function, e is constant) and e^x (exponential function, x is exponent) look similar but behave differently. x^e differentiates to e·x^(e-1); e^x differentiates to itself."
```

## Explainer

The power rule d/dx[x^n] = n·x^(n-1) applies when the variable x is the base and the exponent n is a fixed constant. The exponential function e^x is the structural opposite: the base e is the constant and the variable x is the exponent. These are different kinds of functions, and they require different differentiation rules.

The natural exponential function has a defining property: its derivative is itself. That is, d/dx[e^x] = e^x. This is not a coincidence or a formula to memorize and accept on faith — it is almost the definition of e. The number e ≈ 2.71828... is the unique real number for which this holds. You can see why from the limit definition of the derivative: when you compute lim(h→0) (e^(x+h) − e^x)/h = e^x · lim(h→0) (e^h − 1)/h, the limit evaluates to exactly 1 only when the base is e. For any other base b, d/dx[b^x] = b^x · ln(b). When b = e, ln(e) = 1, so the factor vanishes — this is why e is called the natural base.

With the chain rule, the pattern extends cleanly: d/dx[e^(g(x))] = e^(g(x)) · g'(x). The outer e^(·) stays unchanged; multiply by the derivative of the inner function. This means the outer function "passes through" untouched while the chain rule factor accounts for the inner function's rate of change. For example, d/dx[e^(5x³)] = e^(5x³) · 15x². The most frequent error is omitting g'(x) entirely, treating the exponent as though it were a constant. Always ask: is my exponent a function of x? If yes, the chain rule applies.

This derivative rule is central to modeling. The differential equation dy/dx = ky — which describes any process where the rate of change is proportional to the current value — has y = Ce^(kx) as its solution. Exponential growth (populations, investments) corresponds to k > 0; exponential decay (radioactive substances, drug concentrations) corresponds to k < 0. Recognizing and differentiating exponential functions correctly is the gateway to all of these applications in differential equations.
