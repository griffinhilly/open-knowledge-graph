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

## Explainer

The **power rule** is the first great shortcut of differential calculus, and it follows directly from the limit definition of the derivative you already know. Recall that f'(x) = lim[h→0] (f(x+h) − f(x))/h. For f(x) = x², expanding (x+h)² = x² + 2xh + h² gives (2xh + h²)/h = 2x + h, which approaches 2x as h→0. For x³ you get 3x². The pattern is clear: bring the exponent down as a coefficient, reduce the exponent by one. The power rule states this for all real exponents n: if f(x) = xⁿ, then **f'(x) = n·xⁿ⁻¹**. You no longer need the limit machinery for any power function.

The rule extends well beyond positive integers, and this is where it becomes genuinely powerful. For f(x) = x⁻¹ = 1/x, rewrite it as x⁻¹ and apply the rule: f'(x) = −1·x⁻² = −1/x². For f(x) = √x = x^(1/2), the rule gives f'(x) = (1/2)x^(−1/2) = 1/(2√x). The key habit is **rewriting before differentiating**: any root or reciprocal must be expressed as a fractional or negative exponent first. The rule handles the rest automatically. This rewriting step is where most errors occur — not in the rule itself.

The one trap to avoid is confusing a power function with an **exponential function**. In xⁿ the variable is the base and n is constant — the power rule applies. In aˣ (like 2ˣ or eˣ) the variable is in the exponent and a is constant — the power rule does not apply. These look superficially similar but are fundamentally different types of functions with different derivative formulas. If you see the variable in the exponent, stop and recall the exponential derivative rules instead.

Combined with the constant multiple and sum rules (your next topic), the power rule makes differentiating any polynomial a mechanical one-pass process. For p(x) = 4x³ − 7x² + 2x − 5, you differentiate term by term: 12x² − 14x + 2. This speed and reliability is why the power rule is the backbone of early calculus — virtually every application in physics, economics, and engineering that involves rates of change starts with polynomial models, and the power rule is how you find their derivatives instantly.
