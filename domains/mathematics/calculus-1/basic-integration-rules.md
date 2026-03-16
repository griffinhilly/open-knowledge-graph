---
id: basic-integration-rules
title: Basic Integration Rules
domain: mathematics
course: calculus-1
prerequisites:
  - id: indefinite-integrals
    type: hard
  - id: constant-multiple-and-sum-rules
    type: hard
builds-toward:
  - u-substitution
  - riemann-sums
tags: [integration, rules, power-rule-integration]
stage: formal-systems
status: validated
---

# Basic Integration Rules

## Core Idea
The basic integration rules are the reverses of the basic derivative rules: the integral of x^n dx = x^(n+1)/(n+1) + C (for n not equal to -1), the integral of 1/x dx = ln|x| + C, the integral of e^x dx = e^x + C, the integral of sin(x) dx = -cos(x) + C, the integral of cos(x) dx = sin(x) + C, and so on. The constant multiple and sum rules apply to integrals just as they do to derivatives: integration is linear.

## How It's Best Learned
Build a reference table of basic integrals alongside the corresponding derivative rules. Practice until the correspondence is automatic. Emphasize the special case n = -1 (integral of 1/x is ln|x|, not the power rule). Verify every integral by differentiating.

## Common Misconceptions
- Applying the power rule for integration when n = -1 (division by zero).
- Forgetting sign changes: the integral of sin(x) is -cos(x), not +cos(x).
- Assuming there is a product rule or quotient rule for integration (there is not directly).

## Explainer

You already know that an indefinite integral asks: "what function, when differentiated, gives this?" Basic integration rules are just that question answered systematically for the most common functions. Every rule in this table is simply the corresponding derivative rule run in reverse.

The most important rule is the **power rule for integration**: ∫x^n dx = x^(n+1)/(n+1) + C. Compare this to the derivative rule d/dx[x^n] = nx^(n-1). Differentiation lowers the exponent by 1 and multiplies by the old exponent. Integration does the reverse: raise the exponent by 1 and divide by the new exponent. For example, ∫x³ dx = x⁴/4 + C — you can verify this by differentiating x⁴/4 to get x³. The linearity rules you learned for derivatives carry over unchanged: constants pull out of integrals (∫5x² dx = 5∫x² dx), and the integral of a sum is the sum of integrals.

The **exception at n = −1** deserves its own sentence. The power rule formula would give x⁰/0 + C, which is undefined. But the actual answer is well-defined: ∫(1/x) dx = ln|x| + C. This follows because d/dx[ln|x|] = 1/x — a derivative rule you know — so 1/x has an antiderivative, just not one the power rule formula produces. The absolute value matters: ln is only defined for positive inputs, but 1/x is defined for all x ≠ 0, and the antiderivative ln|x| handles both positive and negative x correctly.

For trigonometric functions, the sign changes are the trickiest part. You know that d/dx[sin x] = cos x and d/dx[cos x] = −sin x. Running these backwards gives ∫cos x dx = sin x + C and ∫sin x dx = −cos x + C. The minus sign in the second integral is not an error — it reflects the minus sign in the derivative of cosine. A reliable check: differentiate your answer and confirm you get back the integrand. This verification habit catches sign errors immediately and reinforces the derivative–integral inverse relationship at every step.
