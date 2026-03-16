---
id: quotient-rule
title: Quotient Rule
domain: mathematics
course: calculus-1
prerequisites:
  - id: product-rule
    type: hard
builds-toward:
  - implicit-differentiation
tags: [derivatives, rules, quotient-rule]
stage: formal-systems
status: validated
---

# Quotient Rule

## Core Idea
The quotient rule states that d/dx[f(x)/g(x)] = (f'(x)*g(x) - f(x)*g'(x)) / [g(x)]^2. It handles derivatives of fractions where both numerator and denominator are functions of x. The mnemonic "lo d-hi minus hi d-lo over lo-lo" helps with the formula. Alternatively, the quotient rule can be derived from the product rule with g^(-1), but the formula is used directly in practice.

## How It's Best Learned
Derive from the product rule applied to f * g^(-1). Practice with simple rational functions first, then with trig functions (this is how you derive d/dx[tan(x)] = sec^2(x)). Emphasize keeping the denominator squared and the minus sign in the correct position.

## Common Misconceptions
- Swapping the order in the numerator: it is f'g - fg', not fg' - f'g.
- Forgetting to square the denominator.
- Using the quotient rule when simpler alternatives exist (e.g., rewrite 1/x^3 as x^(-3) and use power rule).

## Explainer

You already know the product rule: d/dx[f·g] = f'g + fg'. The quotient rule is not a separate idea — it is the product rule applied to f(x) · [g(x)]⁻¹. Seeing this derivation once makes the formula much easier to reconstruct if you ever forget it. Let h(x) = f(x)/g(x) = f(x) · [g(x)]⁻¹. By the product rule, h'(x) = f'(x) · [g(x)]⁻¹ + f(x) · d/dx[g(x)]⁻¹. Using the chain rule, d/dx[g⁻¹] = -g'(x)/[g(x)]². Substituting: h'(x) = f'/g - fg'/g² = (f'g - fg')/g². That is the quotient rule, derived directly from the product rule.

The formula d/dx[f/g] = (f'g - fg')/g² has an asymmetry worth noting: the numerator is **f'g minus fg'**, in that order. The first term differentiates the numerator while leaving the denominator alone; the second term differentiates the denominator while leaving the numerator alone. Then everything sits over g squared. The mnemonic "lo d-hi minus hi d-lo over lo-lo" names g as "lo" (the bottom) and f as "hi" (the top): (lo · d(hi) - hi · d(lo)) / (lo · lo).

The quotient rule's most important application is deriving the derivatives of trigonometric functions you don't already know. Since tan(x) = sin(x)/cos(x), apply the rule with f = sin x and g = cos x: (cos x · cos x - sin x · (-sin x)) / cos²x = (cos²x + sin²x) / cos²x = 1/cos²x = sec²x. So d/dx[tan x] = sec²x. Similarly you can derive d/dx[cot x], d/dx[sec x], and d/dx[csc x] — all from sin and cos using the quotient rule. These are not formulas to memorize blindly; they are results you can re-derive in thirty seconds.

One practical judgment: the quotient rule is not always necessary for fractions. If the denominator is a constant (like 5x²/3), just factor it out — no quotient rule needed. If the denominator is a simple power of x (like 1/x³ = x⁻³), rewrite with a negative exponent and use the power rule. Save the quotient rule for cases where both numerator and denominator genuinely depend on x in ways you cannot simplify first. Reaching for it prematurely on simple expressions is the most common inefficiency students have with this rule.
