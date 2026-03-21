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

## Questions

```yaml
- question: "A student computes d/dx[sin(x)/cos(x)] using the quotient rule and gets −sec²(x) instead of sec²(x). What mistake did they make?"
  type: multiple-choice
  options:
    - "They forgot to square the denominator"
    - "They reversed the order in the numerator, computing fg′ − f′g instead of f′g − fg′"
    - "They differentiated cos(x) as +sin(x) instead of −sin(x)"
    - "They should have used the product rule instead of the quotient rule"
  answer: 1
  explanation: "With f = sin x and g = cos x, the correct numerator is f′g − fg′ = (cos x)(cos x) − (sin x)(−sin x) = cos²x + sin²x = 1. Reversing the order gives fg′ − f′g = (sin x)(−sin x) − (cos x)(cos x) = −sin²x − cos²x = −1, producing −sec²x. The order f′g − fg′ is non-negotiable — swapping it flips the sign of the entire result."

- question: "Which of the following does NOT require the quotient rule to differentiate?"
  type: multiple-choice
  options:
    - "d/dx[sin(x)/cos(x)]"
    - "d/dx[(x³ + 1)/(x² − 1)]"
    - "d/dx[5x²/3]"
    - "d/dx[eˣ/(x + 1)]"
  answer: 2
  explanation: "When the denominator is a constant, simply factor it out: d/dx[5x²/3] = (5/3) · d/dx[x²] = (10/3)x. No quotient rule needed. The quotient rule is reserved for expressions where both numerator and denominator are genuine functions of x. Applying it unnecessarily to constant denominators is a common inefficiency. Options A, B, and D all have x-dependent denominators that require the rule."

- question: "The quotient rule formula d/dx[f/g] = (f′g − fg′)/g² can be derived directly from the product rule applied to f(x) · [g(x)]⁻¹."
  type: true-false
  answer: true
  explanation: "This derivation is the cleanest way to understand the quotient rule. Writing f/g as f · g⁻¹ and applying the product rule gives f′ · g⁻¹ + f · (−g′g⁻²). Simplifying: f′/g − fg′/g² = (f′g − fg′)/g². Knowing this derivation means you never need to memorize the formula blindly — you can reconstruct it from the product rule in under a minute."

- question: "The numerator of the quotient rule result is f(x)g′(x) − f′(x)g(x) — 'hi d-lo minus lo d-hi.'"
  type: true-false
  answer: false
  explanation: "This is exactly backwards. The correct numerator is f′(x)g(x) − f(x)g′(x) — 'lo d-hi minus hi d-lo,' where 'hi' is the numerator f and 'lo' is the denominator g. The minus sign means order matters: reversing the two terms changes the sign of the entire result. Many students flip this and wonder why their answer is off by a sign."

- question: "Explain why the quotient rule produces f′g − fg′ in the numerator and not fg′ − f′g. Where does this asymmetry come from?"
  type: short-answer
  answer: "The asymmetry comes from the product rule applied to f · g⁻¹. The first term differentiates f (leaving g⁻¹ alone): f′/g. The second term differentiates g⁻¹ using the chain rule: f · (−g′/g²) = −fg′/g². Combining over a common denominator gives (f′g − fg′)/g². The minus sign is inherited from the chain rule applied to g⁻¹, and the order f′g first is fixed by which factor is differentiated first."
  explanation: "The non-commutativity is the key: f′g − fg′ ≠ fg′ − f′g (they differ by a sign). Because the formula comes from a minus sign in the chain rule, swapping the terms is not a cosmetic rearrangement — it produces the wrong sign entirely. This is why the mnemonic 'lo d-hi minus hi d-lo' specifies the order: d(hi) comes first, d(lo) is subtracted."
```

## Explainer

You already know the product rule: d/dx[f·g] = f'g + fg'. The quotient rule is not a separate idea — it is the product rule applied to f(x) · [g(x)]⁻¹. Seeing this derivation once makes the formula much easier to reconstruct if you ever forget it. Let h(x) = f(x)/g(x) = f(x) · [g(x)]⁻¹. By the product rule, h'(x) = f'(x) · [g(x)]⁻¹ + f(x) · d/dx[g(x)]⁻¹. Using the chain rule, d/dx[g⁻¹] = -g'(x)/[g(x)]². Substituting: h'(x) = f'/g - fg'/g² = (f'g - fg')/g². That is the quotient rule, derived directly from the product rule.

The formula d/dx[f/g] = (f'g - fg')/g² has an asymmetry worth noting: the numerator is **f'g minus fg'**, in that order. The first term differentiates the numerator while leaving the denominator alone; the second term differentiates the denominator while leaving the numerator alone. Then everything sits over g squared. The mnemonic "lo d-hi minus hi d-lo over lo-lo" names g as "lo" (the bottom) and f as "hi" (the top): (lo · d(hi) - hi · d(lo)) / (lo · lo).

The quotient rule's most important application is deriving the derivatives of trigonometric functions you don't already know. Since tan(x) = sin(x)/cos(x), apply the rule with f = sin x and g = cos x: (cos x · cos x - sin x · (-sin x)) / cos²x = (cos²x + sin²x) / cos²x = 1/cos²x = sec²x. So d/dx[tan x] = sec²x. Similarly you can derive d/dx[cot x], d/dx[sec x], and d/dx[csc x] — all from sin and cos using the quotient rule. These are not formulas to memorize blindly; they are results you can re-derive in thirty seconds.

One practical judgment: the quotient rule is not always necessary for fractions. If the denominator is a constant (like 5x²/3), just factor it out — no quotient rule needed. If the denominator is a simple power of x (like 1/x³ = x⁻³), rewrite with a negative exponent and use the power rule. Save the quotient rule for cases where both numerator and denominator genuinely depend on x in ways you cannot simplify first. Reaching for it prematurely on simple expressions is the most common inefficiency students have with this rule.
