---
id: chain-rule
title: Chain Rule
domain: mathematics
course: calculus-1
prerequisites:
- id: product-rule
  type: soft
- id: composition-of-functions
  type: hard
- id: composition-of-functions-advanced
  type: soft
builds-toward:
- implicit-differentiation
- related-rates
- u-substitution
tags:
- derivatives
- rules
- chain-rule
- composition
stage: formal-systems
status: validated
---
# Chain Rule

## Core Idea
The chain rule states that if y = f(g(x)), then dy/dx = f'(g(x)) * g'(x). In Leibniz notation: if y = f(u) and u = g(x), then dy/dx = (dy/du)(du/dx). You differentiate the outer function evaluated at the inner function, then multiply by the derivative of the inner function. The chain rule is arguably the most important derivative rule because composite functions appear everywhere.

## How It's Best Learned
Start with clear identification of the "outer" and "inner" functions. Practice with simple compositions like (3x + 1)^5, sin(x^2), e^(2x). Build up to multi-layer compositions (chain rule applied multiple times). Connect to u-substitution in integration (the chain rule in reverse).

## Common Misconceptions
- Forgetting to multiply by the derivative of the inner function (the most common chain rule error).
- Difficulty identifying the inner and outer functions in complex expressions.
- Not recognizing when the chain rule is needed (any composite function requires it).

## Questions

```yaml
- question: "What is the derivative of f(x) = sin(3x²)?"
  type: multiple-choice
  options: ["cos(3x²)", "6x · cos(6x)", "-cos(3x²) · 6x", "6x · cos(3x²)"]
  answer: 3
  explanation: "Identify outer = sin(u) and inner = 3x². Differentiate outer: cos(u) = cos(3x²). Differentiate inner: 6x. Multiply: 6x · cos(3x²). Option A forgets to multiply by the inner derivative. Option B applies the inner derivative inside the trig function — a common error of 'differentiating inside the argument' instead of multiplying outside. Option C has the wrong sign (sin differentiates to +cos, not -cos)."

- question: "The chain rule is mainly needed when a function is raised to a power, like (3x + 1)⁵."
  type: true-false
  answer: false
  explanation: "The chain rule applies to any composite function — whenever one function is nested inside another. sin(x²), e^(3x), ln(x² + 1), and √(x + 1) all require the chain rule even though none of them is a polynomial raised to a power. The trigger is composition, not exponents specifically."

- question: "Identify the outer and inner functions in h(x) = e^(x² + 1), then find h'(x)."
  type: short-answer
  answer: "Outer: f(u) = eᵘ; Inner: g(x) = x² + 1. h'(x) = e^(x² + 1) · 2x"
  explanation: "The inner function is what gets evaluated first: x² + 1. The outer function is applied to that result: e raised to whatever the inner gives. By the chain rule, h'(x) = f'(g(x)) · g'(x) = e^(x²+1) · 2x. Note that the derivative of eᵘ is eᵘ — the exponential function is its own derivative — so only the inner derivative 2x is new."
```

## Explainer

The chain rule solves one specific problem: how do you differentiate a function that is nested inside another function? You already know how to differentiate sin(x), and you know how to differentiate x². But what about sin(x²)? That is a composite function — x² goes in first, then sin is applied to the result — and it requires the chain rule.

The key step is identifying which function is the "outer" (applied last) and which is the "inner" (applied first). In sin(x²), the outer function is sin(·) and the inner is x². In e^(3x+1), the outer is e^(·) and the inner is 3x+1. In (x² + 4)⁵, the outer is (·)⁵ and the inner is x² + 4. Once you have these, the chain rule says: differentiate the outer function (treating the inner as a single variable), evaluate it at the inner function, and multiply by the derivative of the inner function. Written as a formula: if h(x) = f(g(x)), then h'(x) = f'(g(x)) · g'(x).

The most common error is differentiating the outer and forgetting to multiply by the inner derivative. For (3x + 1)⁵, the outer derivative gives 5(3x + 1)⁴ — but without the inner derivative (3), the answer is incomplete. Every composite function "costs" a factor of the inner derivative. If the inner function is just x, its derivative is 1 and that factor is invisible, which is why you didn't need the chain rule for sin(x) — the "inner function" is x, g'(x) = 1.

The Leibniz notation dy/dx = (dy/du)(du/dx) makes the chain rule feel almost like fraction cancellation: the "du" terms appear to cancel, leaving dy/dx. This is not exactly why it works (du is not literally a number you can cancel), but the notation is designed to make the structure intuitive. If y depends on u and u depends on x, the rate of change of y with respect to x is the product of the rates.

Recognizing when the chain rule is needed takes practice. The trigger is composition: any time you can describe a function as "do this to the result of that," you need the chain rule. As you encounter integration, you will find that u-substitution is the chain rule in reverse — you are "undoing" a chain rule structure to simplify an integral. Building a clear mental model of composite functions now will make u-substitution much more intuitive when you reach it.
