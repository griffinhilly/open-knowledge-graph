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

## Questions

```yaml
- question: "A student divides x³ + 5x − 3 by x² − 1. She writes the dividend as x³ + 5x − 3 without accounting for missing powers. What problem is most likely to follow?"
  type: multiple-choice
  options:
    - "She will get a quotient of higher degree than possible"
    - "The subtraction step will produce misaligned results because there is no x² term to subtract from"
    - "She will stop the division process one step too early"
    - "Nothing — missing terms can safely be ignored in polynomial long division"
  answer: 1
  explanation: "x³ + 5x − 3 is missing an x² term. Written correctly with the placeholder, it is x³ + 0x² + 5x − 3. When the first step produces a term in x², there is nothing to subtract it from if the placeholder was omitted — the columns fall out of alignment, corrupting every subsequent step. The placeholder 0x² is essential bookkeeping, not optional."

- question: "When should you stop the polynomial long division process?"
  type: multiple-choice
  options:
    - "After performing as many steps as the degree of the dividend"
    - "When the quotient has the same degree as the divisor"
    - "When the degree of the remainder is less than the degree of the divisor"
    - "Only when the remainder is exactly zero"
  answer: 2
  explanation: "The process stops when the remaining expression (the current remainder) has degree strictly less than the divisor's degree — because the divisor can no longer 'fit into' it, just as 5 doesn't fit into 4 in integer division. You stop even if the remainder is nonzero. Stopping only when the remainder is zero would be incorrect; many divisions produce a nonzero remainder."

- question: "If dividing f(x) by (x − a) produces a remainder of zero, then (x − a) is a factor of f(x)."
  type: true-false
  answer: true
  explanation: "By the polynomial division algorithm, f(x) = (x − a)·q(x) + r. If r = 0, then f(x) = (x − a)·q(x), which means (x − a) divides f(x) evenly — it is a factor. This connection is what the factor theorem formalizes and is one of the key reasons polynomial long division matters for factoring."

- question: "In polynomial long division, you compare the degree of the remainder to the degree of the dividend to decide when to stop."
  type: true-false
  answer: false
  explanation: "You compare the remainder's degree to the degree of the DIVISOR, not the dividend. The rule is: stop when deg(remainder) < deg(divisor). The dividend's degree is irrelevant to the stopping condition. Confusing divisor and dividend is a common source of errors in knowing when to halt the process."

- question: "How does the equation f(x) = d(x)·q(x) + r(x) let you verify that a polynomial long division was performed correctly?"
  type: short-answer
  answer: "Multiply the quotient q(x) by the divisor d(x), then add the remainder r(x). If the result equals the original dividend f(x), the division is correct. For example, if dividing x³ − 2x² − 4 by x − 2 gives quotient x² and remainder −4, verify by computing (x − 2)(x²) + (−4) = x³ − 2x² − 4, which matches the original."
  explanation: "This verification mirrors integer division: if 17 ÷ 5 gives quotient 3 and remainder 2, you check that 5·3 + 2 = 17. The same structure applies to polynomials. Multiplication is easier to perform than division and provides an independent check on the entire computation, catching sign errors, missed terms, and incorrect combining."
```

## Explainer

Polynomial long division is integer long division with variables instead of digits. When you divide 137 by 5, you ask: how many times does 5 fit into 13? You get 2, multiply to get 10, subtract to get 3, bring down the 7, and continue. Polynomial long division follows exactly this rhythm, but instead of asking "how many times does 5 fit into 13?", you ask "what do I multiply the leading term of the divisor by to match the leading term of what remains?"

Work through a concrete example: divide x³ − 2x² + 0x − 4 by x − 2. The leading term of the dividend is x³ and the leading term of the divisor is x. Ask: what times x gives x³? Answer: x². Write x² in the quotient. Multiply x²(x − 2) = x³ − 2x², subtract to get 0x² + 0x − 4. Notice the x² terms cancelled entirely. Bring down: you have −4 left. Now x doesn't fit into −4 (degree 0 is less than degree 1), so −4 is the remainder. Result: x³ − 2x² − 4 = (x − 2)(x²) + (−4). You can verify: multiply it out and you recover the original polynomial.

The critical bookkeeping step is **placeholder terms**: if your dividend is missing a power (say there's no x term), you must write 0x to hold its place. Without it, your columns fall out of alignment and every subsequent subtraction produces wrong results. This parallels writing a zero in the ones place when doing integer division of 2300 ÷ 4.

The result fits the **polynomial division algorithm**: f(x) = d(x) · q(x) + r(x), where deg(r) < deg(d). This mirrors the integer relationship 17 = 5 · 3 + 2. The remainder captures "what's left over." When the remainder is zero, d(x) divides f(x) evenly — meaning d(x) is a factor of f(x). The **remainder theorem** (your next topic) sharpens this: the value f(a) tells you the remainder when f is divided by (x − a), without doing the full division at all.
