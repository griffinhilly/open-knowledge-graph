---
id: power-rule
title: Power Rule
domain: mathematics
course: calculus-1
prerequisites:
  - id: limit-definition-of-derivative
    type: hard
builds-toward:
  - constant-multiple-and-sum-rules
  - antiderivatives
tags: [derivatives, rules, power-rule]
stage: formal-systems
status: validated
---

# Power Rule

## Core Idea
The power rule states that if f(x) = x^n, then f'(x) = n*x^(n-1). It works for any real exponent n: positive integers, negative integers, and fractions. This is the first and most frequently used derivative shortcut. Combined with the constant multiple and sum rules, it handles all polynomial derivatives instantly.

## How It's Best Learned
Derive the power rule from the limit definition for n = 2 and n = 3 to see the pattern, then state the general rule. Practice with positive integer exponents, then extend to negative exponents (f(x) = 1/x^n = x^(-n)) and fractional exponents (f(x) = sqrt(x) = x^(1/2)). Emphasize rewriting roots and reciprocals as powers before differentiating.

## Common Misconceptions
- Forgetting to subtract 1 from the exponent.
- Not rewriting roots and fractions as powers: d/dx[sqrt(x)] requires writing it as x^(1/2) first.
- Applying the power rule to exponential functions like 2^x (the variable is in the exponent, not the base).

## Questions

```yaml
- question: "What is the derivative of f(x) = √x?"
  type: multiple-choice
  options:
    - "f'(x) = √x / 2"
    - "f'(x) = 1 / (2√x)"
    - "f'(x) = x^(1/2)"
    - "f'(x) = 2x^(1/2)"
  answer: 1
  explanation: "Rewrite √x as x^(1/2) before differentiating. Applying the power rule: bring down the exponent (1/2) as a coefficient and subtract 1 from the exponent: f'(x) = (1/2)x^(1/2 − 1) = (1/2)x^(−1/2) = 1/(2√x). The critical first step is the rewrite — trying to differentiate √x without converting it to a fractional exponent has no clear path. This rewriting habit is the main skill the power rule requires beyond the rule itself."

- question: "A student attempts to find d/dx[3^x] by applying the power rule, reasoning that the exponent x should be brought down as a coefficient. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "The student should apply the chain rule before the power rule"
    - "The power rule applies only to integer exponents, so x in the exponent requires a different approach"
    - "The power rule requires the variable to be the base with a constant exponent; here the variable is in the exponent, making 3^x an exponential function with a different derivative rule"
    - "The coefficient 3 should be moved to the exponent position first"
  answer: 2
  explanation: "The power rule d/dx[x^n] = n·x^(n−1) requires the variable to be in the *base* with a *constant* exponent. In 3^x, the base is the constant 3 and the variable x is in the exponent — this is an exponential function, which has a completely different derivative: d/dx[a^x] = a^x · ln(a). Confusing x^n (power function) with a^x (exponential function) is one of the most common errors in early calculus. They look superficially similar but are fundamentally different objects."

- question: "The power rule d/dx[x^n] = n·x^(n−1) is valid for n = −3."
  type: true-false
  answer: true
  explanation: "The power rule holds for all real exponents n, including negative integers, fractions, and irrational numbers. For n = −3: d/dx[x^(−3)] = −3·x^(−4) = −3/x^4. You can verify this by rewriting x^(−3) = 1/x^3 and using the quotient rule or limit definition — the result is the same. The extension to negative and fractional exponents is exactly what makes the power rule more powerful than it might first appear."

- question: "The derivative of f(x) = x^(1/2) is f'(x) = x^(−1/2)."
  type: true-false
  answer: false
  explanation: "Applying the power rule correctly: f'(x) = (1/2)·x^(1/2 − 1) = (1/2)·x^(−1/2). The missing coefficient of 1/2 is the error — the exponent must be brought *down as a multiplier* before the exponent is reduced. The result x^(−1/2) without the factor of 1/2 is wrong. Always write the result as (original exponent) × x^(original exponent − 1)."

- question: "Why can't the power rule be applied to d/dx[2^x], and what does the correct derivative look like?"
  type: short-answer
  answer: "The power rule applies only when the variable is the base and the exponent is a constant: f(x) = x^n. In 2^x, the base is the constant 2 and the variable x is the exponent. This makes it an exponential function, not a power function. The correct derivative is d/dx[2^x] = 2^x · ln(2), from the general rule d/dx[a^x] = a^x · ln(a)."
  explanation: "The fundamental distinction is which quantity varies. In x^n, the base grows with x while the exponent stays fixed — polynomial-type growth. In a^x, the exponent grows with x while the base stays fixed — exponential growth. The ln(a) factor in the exponential derivative arises from the identity a^x = e^(x ln a): differentiating the exponent x·ln(a) with respect to x gives ln(a), and e^(x ln a) = a^x remains as the factor. If a = e, then ln(e) = 1 and d/dx[e^x] = e^x — the one exponential function that is its own derivative."
```

## Explainer

The **power rule** is the first great shortcut of differential calculus, and it follows directly from the limit definition of the derivative you already know. Recall that f'(x) = lim[h→0] (f(x+h) − f(x))/h. For f(x) = x², expanding (x+h)² = x² + 2xh + h² gives (2xh + h²)/h = 2x + h, which approaches 2x as h→0. For x³ you get 3x². The pattern is clear: bring the exponent down as a coefficient, reduce the exponent by one. The power rule states this for all real exponents n: if f(x) = xⁿ, then **f'(x) = n·xⁿ⁻¹**. You no longer need the limit machinery for any power function.

The rule extends well beyond positive integers, and this is where it becomes genuinely powerful. For f(x) = x⁻¹ = 1/x, rewrite it as x⁻¹ and apply the rule: f'(x) = −1·x⁻² = −1/x². For f(x) = √x = x^(1/2), the rule gives f'(x) = (1/2)x^(−1/2) = 1/(2√x). The key habit is **rewriting before differentiating**: any root or reciprocal must be expressed as a fractional or negative exponent first. The rule handles the rest automatically. This rewriting step is where most errors occur — not in the rule itself.

The one trap to avoid is confusing a power function with an **exponential function**. In xⁿ the variable is the base and n is constant — the power rule applies. In aˣ (like 2ˣ or eˣ) the variable is in the exponent and a is constant — the power rule does not apply. These look superficially similar but are fundamentally different types of functions with different derivative formulas. If you see the variable in the exponent, stop and recall the exponential derivative rules instead.

Combined with the constant multiple and sum rules (your next topic), the power rule makes differentiating any polynomial a mechanical one-pass process. For p(x) = 4x³ − 7x² + 2x − 5, you differentiate term by term: 12x² − 14x + 2. This speed and reliability is why the power rule is the backbone of early calculus — virtually every application in physics, economics, and engineering that involves rates of change starts with polynomial models, and the power rule is how you find their derivatives instantly.
