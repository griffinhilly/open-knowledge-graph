---
id: constant-multiple-and-sum-rules
title: Constant Multiple and Sum/Difference Rules
domain: mathematics
course: calculus-1
prerequisites:
  - id: power-rule
    type: hard
builds-toward:
  - product-rule
  - antiderivatives
tags: [derivatives, rules, linearity]
stage: formal-systems
status: validated
---

# Constant Multiple and Sum/Difference Rules

## Core Idea
The constant multiple rule says d/dx[c*f(x)] = c*f'(x): constants factor out of derivatives. The sum/difference rule says d/dx[f(x) +/- g(x)] = f'(x) +/- g'(x): derivatives distribute over addition and subtraction. Together, these express the linearity of differentiation. Combined with the power rule, they allow you to differentiate any polynomial term by term.

## How It's Best Learned
Derive from the limit definition (constants factor out of limits, limit of a sum is sum of limits). Practice differentiating polynomials term by term. Emphasize that this only works for sums, not products or compositions (those need the product rule and chain rule).

## Common Misconceptions
- Trying to apply the sum rule to products: d/dx[f*g] is not f'*g'.
- Forgetting to differentiate constant terms (their derivative is zero, not the constant itself).
- Not recognizing that these rules together mean differentiation is a linear operation.

## Explainer

You've learned the power rule: d/dx[xⁿ] = nxⁿ⁻¹. That handles individual power terms in isolation. But most functions you'll differentiate are *combinations* — a constant times a function, or several functions added together. Two additional rules handle these cases, and together they reveal something fundamental about the structure of differentiation itself.

The **constant multiple rule** states d/dx[c·f(x)] = c·f'(x): a constant factor pulls out of a derivative. The proof comes directly from the limit definition. The difference quotient for c·f(x) is [c·f(x+h) − c·f(x)]/h = c·[f(x+h) − f(x)]/h. Since c doesn't depend on h, it factors out before the limit is taken, giving c·f'(x). In practice: d/dx[5x³] = 5·d/dx[x³] = 5·3x² = 15x². The constant stays attached; only the power is differentiated.

The **sum/difference rule** states d/dx[f(x) ± g(x)] = f'(x) ± g'(x): derivatives distribute over addition and subtraction. Again from the limit definition: the limit of a sum is the sum of the limits (when both exist), so the combined difference quotient [f(x+h) + g(x+h) − f(x) − g(x)]/h separates into two independent difference quotients. In practice: d/dx[x³ + x²] = 3x² + 2x, one term at a time.

Together, these two rules express that differentiation is a **linear operator**: d/dx[a·f(x) + b·g(x)] = a·f'(x) + b·g'(x) for any constants a, b. Linearity means you can break a complicated expression into simple parts, differentiate each part, and reassemble — the structure is preserved. You'll encounter this same idea in integration, linear algebra (linear transformations), and differential equations. Any time an operation is linear, it becomes decomposable and predictable.

Combining linearity with the power rule, you can now differentiate any polynomial term by term: d/dx[5x³ − 2x + 7] = 5·3x² − 2·1x⁰ + 0 = 15x² − 2. Note that the constant 7 has derivative zero — it contributes 7·d/dx[x⁰] = 7·0 = 0. This term-by-term approach only works for sums and differences. Products require the product rule and compositions require the chain rule — neither distributes as simply as sums do. Keeping that boundary clear is the main conceptual task as you build your differentiation toolkit.
