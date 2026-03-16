---
id: polynomial-long-division
title: Polynomial Long Division
domain: mathematics
course: algebra-2
prerequisites:
- id: polynomial-functions-degree-and-leading-coefficient
  type: hard
- id: multiplying-polynomials
  type: hard
- id: graphing-polynomial-functions
  type: soft
builds-toward:
- synthetic-division
- remainder-theorem
- rational-functions-and-asymptotes
tags:
- polynomials
- division
- long-division
- quotient-remainder
stage: abstract-reasoning
status: validated
---
# Polynomial Long Division

## Core Idea
Polynomial long division divides a polynomial by another polynomial, producing a quotient and remainder, analogous to integer long division. If f(x) = d(x)*q(x) + r(x), where deg(r) < deg(d). The process: divide leading terms, multiply, subtract, bring down, repeat. This is essential for simplifying rational expressions, finding oblique asymptotes, and applying the remainder and factor theorems.

## How It's Best Learned
Draw the explicit parallel to integer long division. Start with divisors of degree 1 (linear), then degree 2. Emphasize including placeholder terms for missing powers (e.g., 0x^2). Practice verifying answers by multiplying quotient by divisor and adding the remainder.

## Common Misconceptions
- Forgetting to include terms with zero coefficients as placeholders.
- Subtracting incorrectly (sign errors are the most common mistake).
- Stopping too early or too late in the division process.
- Not knowing when the process is complete (when the remainder's degree is less than the divisor's degree).

## Explainer

Polynomial long division is integer long division with variables instead of digits. When you divide 137 by 5, you ask: how many times does 5 fit into 13? You get 2, multiply to get 10, subtract to get 3, bring down the 7, and continue. Polynomial long division follows exactly this rhythm, but instead of asking "how many times does 5 fit into 13?", you ask "what do I multiply the leading term of the divisor by to match the leading term of what remains?"

Work through a concrete example: divide x³ − 2x² + 0x − 4 by x − 2. The leading term of the dividend is x³ and the leading term of the divisor is x. Ask: what times x gives x³? Answer: x². Write x² in the quotient. Multiply x²(x − 2) = x³ − 2x², subtract to get 0x² + 0x − 4. Notice the x² terms cancelled entirely. Bring down: you have −4 left. Now x doesn't fit into −4 (degree 0 is less than degree 1), so −4 is the remainder. Result: x³ − 2x² − 4 = (x − 2)(x²) + (−4). You can verify: multiply it out and you recover the original polynomial.

The critical bookkeeping step is **placeholder terms**: if your dividend is missing a power (say there's no x term), you must write 0x to hold its place. Without it, your columns fall out of alignment and every subsequent subtraction produces wrong results. This parallels writing a zero in the ones place when doing integer division of 2300 ÷ 4.

The result fits the **polynomial division algorithm**: f(x) = d(x) · q(x) + r(x), where deg(r) < deg(d). This mirrors the integer relationship 17 = 5 · 3 + 2. The remainder captures "what's left over." When the remainder is zero, d(x) divides f(x) evenly — meaning d(x) is a factor of f(x). The **remainder theorem** (your next topic) sharpens this: the value f(a) tells you the remainder when f is divided by (x − a), without doing the full division at all.
