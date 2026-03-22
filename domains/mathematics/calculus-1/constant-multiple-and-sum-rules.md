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

## Questions

```yaml
- question: "Find d/dx[4x³ − 7x + 3]."
  type: multiple-choice
  options:
    - "12x² − 7x"
    - "12x² − 7"
    - "4x² − 7"
    - "12x³ − 7"
  answer: 1
  explanation: "Apply the rules term by term: d/dx[4x³] = 4·3x² = 12x² (constant multiple + power rule); d/dx[−7x] = −7·1 = −7 (constant multiple + power rule, since x = x¹); d/dx[3] = 0 (derivative of a constant is zero). Assembled: 12x² − 7. Option A keeps the x in the −7x term, forgetting to differentiate it (leaving −7x instead of −7). Option C forgets to multiply by 3 when applying the power rule to x³. Option D retains the cubic exponent, not reducing it by 1."

- question: "A student differentiates h(x) = (3x²)(5x³) by writing h'(x) = (6x)(15x²) = 90x³. What error did they make?"
  type: multiple-choice
  options:
    - "They applied the wrong exponent rule when differentiating 3x²"
    - "They incorrectly assumed d/dx[f·g] = f'·g' — the derivative of a product is not the product of the derivatives"
    - "They forgot to apply the constant multiple rule to factor out the 15"
    - "They should have applied the chain rule here instead"
  answer: 1
  explanation: "The sum/difference rule (linearity of differentiation) applies to f + g, not f·g. d/dx[f·g] ≠ f'·g'. For products, the product rule gives d/dx[f·g] = f·g' + f'·g. The correct approach here is simpler: first simplify h(x) = 15x⁵, then differentiate to get h'(x) = 75x⁴. Alternatively, applying the product rule: (3x²)(15x²) + (6x)(5x³) = 45x⁴ + 30x⁴ = 75x⁴. The student's 90x³ is wrong because they distributed the derivative operation over multiplication, which is not permitted."

- question: "The derivative of f(x) = 5x⁴ − 3x² + 2x − 9 is f'(x) = 20x³ − 6x + 2."
  type: true-false
  answer: true
  explanation: "Apply constant multiple and sum/difference rules term by term: d/dx[5x⁴] = 5·4x³ = 20x³; d/dx[−3x²] = −3·2x = −6x; d/dx[2x] = 2·1 = 2; d/dx[−9] = 0 (constant). Result: 20x³ − 6x + 2. The constant −9 contributes zero — a common point of error is leaving it as −9 rather than 0. This example demonstrates all three aspects of linearity: constants factor out, derivatives distribute over all terms in the sum, and constant terms vanish."

- question: "Because differentiation distributes over addition — d/dx[f + g] = f' + g' — it also distributes over multiplication: d/dx[f·g] = f'·g'."
  type: true-false
  answer: false
  explanation: "Linearity of differentiation is a specific property of the addition operation, not a universal property of all binary operations. The product rule shows that d/dx[f·g] = f·g' + f'·g — cross terms appear, and the operation does not simply distribute. The distribution over sums follows from the algebraic property of limits (the limit of a sum is the sum of the limits), but no analogous property holds for products. Assuming linearity extends to products is one of the most common structural errors in early calculus — products need the product rule, compositions need the chain rule."

- question: "What does it mean to say that differentiation is a 'linear operator,' and what is the most important boundary of that linearity that students must not cross?"
  type: short-answer
  answer: "A linear operator satisfies two properties: scaling (d/dx[c·f] = c·f') and additivity (d/dx[f + g] = f' + g'). Together these mean you can break a sum into parts, differentiate each separately, and reassemble — the structure is fully preserved. The critical boundary is that linearity applies only to sums and differences, not to products or compositions. d/dx[f·g] ≠ f'·g' (the product rule is needed), and d/dx[f(g(x))] is not simply f'(x)·g'(x) (the chain rule is needed)."
  explanation: "Understanding linearity as a precise property — not just vague 'distribution' — tells you exactly when the simple rules apply and when they don't. The power to differentiate polynomials term by term comes entirely from linearity; the need for the product rule and chain rule marks where linearity ends. Linearity recurs throughout mathematics (linear algebra, differential equations, integration), so recognizing its structure and limits is a durable conceptual skill, not just a calculus technique."
```

## Explainer

You've learned the power rule: d/dx[xⁿ] = nxⁿ⁻¹. That handles individual power terms in isolation. But most functions you'll differentiate are *combinations* — a constant times a function, or several functions added together. Two additional rules handle these cases, and together they reveal something fundamental about the structure of differentiation itself.

The **constant multiple rule** states d/dx[c·f(x)] = c·f'(x): a constant factor pulls out of a derivative. The proof comes directly from the limit definition. The difference quotient for c·f(x) is [c·f(x+h) − c·f(x)]/h = c·[f(x+h) − f(x)]/h. Since c doesn't depend on h, it factors out before the limit is taken, giving c·f'(x). In practice: d/dx[5x³] = 5·d/dx[x³] = 5·3x² = 15x². The constant stays attached; only the power is differentiated.

The **sum/difference rule** states d/dx[f(x) ± g(x)] = f'(x) ± g'(x): derivatives distribute over addition and subtraction. Again from the limit definition: the limit of a sum is the sum of the limits (when both exist), so the combined difference quotient [f(x+h) + g(x+h) − f(x) − g(x)]/h separates into two independent difference quotients. In practice: d/dx[x³ + x²] = 3x² + 2x, one term at a time.

Together, these two rules express that differentiation is a **linear operator**: d/dx[a·f(x) + b·g(x)] = a·f'(x) + b·g'(x) for any constants a, b. Linearity means you can break a complicated expression into simple parts, differentiate each part, and reassemble — the structure is preserved. You'll encounter this same idea in integration, linear algebra (linear transformations), and differential equations. Any time an operation is linear, it becomes decomposable and predictable.

Combining linearity with the power rule, you can now differentiate any polynomial term by term: d/dx[5x³ − 2x + 7] = 5·3x² − 2·1x⁰ + 0 = 15x² − 2. Note that the constant 7 has derivative zero — it contributes 7·d/dx[x⁰] = 7·0 = 0. This term-by-term approach only works for sums and differences. Products require the product rule and compositions require the chain rule — neither distributes as simply as sums do. Keeping that boundary clear is the main conceptual task as you build your differentiation toolkit.
