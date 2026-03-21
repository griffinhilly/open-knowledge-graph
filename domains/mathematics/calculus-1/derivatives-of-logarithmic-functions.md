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

## Questions

```yaml
- question: "What is d/dx[ln(x²)]?"
  type: multiple-choice
  options:
    - "1/x²"
    - "2/x"
    - "1/(2x)"
    - "2x · ln(x)"
  answer: 1
  explanation: "Apply the chain rule: d/dx[ln(g(x))] = g'(x)/g(x). Here g(x) = x², so g'(x) = 2x. Therefore d/dx[ln(x²)] = 2x/x² = 2/x. The common error is forgetting the chain rule and writing 1/x². Note that ln(x²) = 2·ln(x), so you can also differentiate directly: d/dx[2·ln(x)] = 2·(1/x) = 2/x. Both approaches confirm the same answer."

- question: "You need to differentiate f(x) = x^(sin x). A classmate says to use the power rule: f'(x) = sin(x) · x^(sin x - 1). Why is this wrong, and what is the correct approach?"
  type: multiple-choice
  options:
    - "The power rule applies here — the classmate's answer is correct"
    - "The power rule requires a constant exponent. Since sin(x) varies with x, you must use logarithmic differentiation: take ln of both sides, giving ln(f) = sin(x)·ln(x), then differentiate implicitly"
    - "Use the chain rule directly: f'(x) = sin(x)·x^(sin x - 1) + x^(sin x)·cos(x)"
    - "The derivative doesn't exist because the exponent is not a polynomial"
  answer: 1
  explanation: "The power rule d/dx[x^n] = n·x^(n-1) requires n to be a constant. When the exponent itself is a function of x, the power rule fails. Logarithmic differentiation handles this: set y = x^(sin x), take ln of both sides: ln(y) = sin(x)·ln(x). Differentiate: (1/y)·y' = cos(x)·ln(x) + sin(x)/x. Solve: y' = x^(sin x)·[cos(x)·ln(x) + sin(x)/x]. The classmate only accounted for the base varying, not the exponent."

- question: "The derivative of ln(2x) is 1/x, not 1/(2x)."
  type: true-false
  answer: true
  explanation: "By the chain rule: d/dx[ln(2x)] = (d/dx[2x])/(2x) = 2/(2x) = 1/x. Equivalently, ln(2x) = ln(2) + ln(x), and since ln(2) is a constant its derivative is 0, leaving d/dx[ln(x)] = 1/x. This is a common trap: students expect the 2 to appear in the derivative, but the chain rule's numerator and denominator both contain the factor 2, which cancels."

- question: "The formula d/dx[log_b(x)] = 1/(x·ln(b)) shows that natural log (base e) is the 'natural' base for calculus because ln(e) = 1 simplifies the formula to 1/x."
  type: true-false
  answer: true
  explanation: "Yes — for any base b, d/dx[log_b(x)] = 1/(x·ln(b)) because log_b(x) = ln(x)/ln(b) by change of base, and ln(b) is a constant. When b = e, ln(e) = 1, so the formula reduces to 1/x with no extra constant. This is one of several reasons e is the natural base for calculus: it produces the cleanest derivatives and integrals. For base 10: d/dx[log₁₀(x)] = 1/(x·ln(10)) ≈ 1/(2.303x)."

- question: "Explain how d/dx[ln(x)] = 1/x is derived from the relationship between ln and e^x — without looking it up."
  type: short-answer
  answer: "Set y = ln(x), which means e^y = x. Differentiate both sides with respect to x using the chain rule on the left: e^y · (dy/dx) = 1. Solve for dy/dx: dy/dx = 1/e^y = 1/x (substituting back e^y = x)."
  explanation: "This derivation uses only two facts: the definition of ln as the inverse of e^x, and the chain rule. It illustrates why inverse function differentiation is powerful — you derive new results from known ones without memorizing additional formulas. The same technique derives d/dx[arcsin(x)], d/dx[arctan(x)], and other inverse function derivatives."
```

## Explainer

You know that d/dx[eˣ] = eˣ — the exponential function is its own derivative. The natural logarithm ln(x) is the **inverse function** of eˣ, and that relationship lets you derive its derivative without memorizing anything new. Set y = ln(x), so eʸ = x. Differentiate both sides with respect to x (using the chain rule on the left): eʸ · (dy/dx) = 1. Solve for dy/dx: dy/dx = 1/eʸ = 1/x. That's it — **d/dx[ln(x)] = 1/x**. This result is geometrically sensible: the slope of y = ln(x) is large and positive near x = 0 (the curve rises steeply) and approaches 0 as x grows (the curve flattens). The function 1/x captures exactly that behavior.

The **chain rule** upgrades this to composite functions. If u = g(x) is a differentiable function, then d/dx[ln(g(x))] = g'(x)/g(x). The derivative of the argument appears in the numerator; the argument itself stays in the denominator. Examples: d/dx[ln(x² + 1)] = 2x/(x² + 1), and d/dx[ln(sin(x))] = cos(x)/sin(x) = cot(x). For general bases, d/dx[log_b(x)] = 1/(x · ln(b)), which follows from rewriting log_b(x) = ln(x)/ln(b) and differentiating. The ln(b) factor in the denominator explains why natural logarithms (base e) are "natural" for calculus — the ln(e) = 1 makes the formula simplest.

**Logarithmic differentiation** is the technique that makes d/dx[ln(x)] = 1/x genuinely powerful beyond its own derivative. When you need to differentiate a complicated product, quotient, or function with a variable in the exponent — like f(x) = xˣ or f(x) = (x²+1)^(sin x) — take the natural log of both sides first: ln(f) = sin(x)·ln(x²+1). Now differentiate both sides (using the chain rule on the left: f'/f) and solve for f'. This technique converts exponential, product, and power relationships into additions and subtractions, which are far easier to handle. The result f'/f is called the **logarithmic derivative**, and it appears throughout calculus and beyond — in probability, physics, and the study of functions with multiplicative structure.
