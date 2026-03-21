---
id: factoring-trinomials
title: Factoring Trinomials
domain: mathematics
course: algebra-1
prerequisites:
  - id: multiplying-binomials-foil
    type: hard
  - id: factoring-gcf
    type: hard
builds-toward:
  - factoring-completely
  - solving-quadratics-by-factoring
tags: [factoring, trinomials, quadratics, polynomials]
stage: abstract-reasoning
status: validated
---

# Factoring Trinomials

## Core Idea
Factoring a trinomial of the form x² + bx + c means finding two binomials (x + p)(x + q) whose product is the original trinomial. Since FOIL gives x² + (p+q)x + pq, we need p + q = b and p × q = c. For x² + 7x + 12, we need two numbers that add to 7 and multiply to 12: 3 and 4, giving (x + 3)(x + 4). When the leading coefficient is not 1 (ax² + bx + c with a > 1), techniques like the AC method or trial-and-error are used. Factoring trinomials is the reverse of FOIL and is the primary method for solving quadratic equations without the quadratic formula.

## How It's Best Learned
Start with simple trinomials (leading coefficient of 1) and practice finding the two numbers that satisfy the sum-and-product conditions. Use organized lists of factor pairs. Then introduce trinomials with leading coefficients greater than 1 using the AC method (multiply a × c, find factors that add to b, split the middle term, factor by grouping). Always check by FOILing the answer.

## Common Misconceptions
- Finding numbers that add to c instead of multiply to c (or vice versa).
- Not considering negative factors when b or c is negative.
- Struggling with the AC method — forgetting to split the middle term correctly or factor by grouping after splitting.

## Questions

```yaml
- question: "A student factoring x² + 8x + 15 reasons: 'I need two numbers that multiply to 8 and add to 15.' What is the error, and what is the correct factorization?"
  type: multiple-choice
  options:
    - "The student should use the AC method since the leading coefficient is not 1. The answer is (x + 3)(x + 5)."
    - "The student inverted the conditions. You need numbers that add to 8 and multiply to 15. The answer is (x + 3)(x + 5)."
    - "The student's approach is correct; since no integer pair works, the trinomial is irreducible over the integers."
    - "The student should use the quadratic formula instead of attempting to factor by inspection."
  answer: 1
  explanation: "In x² + bx + c, b comes from the sum of the two numbers and c comes from their product — because FOIL gives (x+p)(x+q) = x² + (p+q)x + pq. The most common error is reversing these roles. For x² + 8x + 15, we need p + q = 8 and p × q = 15. The pair (3, 5) satisfies both: 3 + 5 = 8 and 3 × 5 = 15, giving (x + 3)(x + 5)."

- question: "Which of the following is the correct factorization of x² − 3x − 10?"
  type: multiple-choice
  options:
    - "(x + 5)(x + 2)"
    - "(x − 5)(x − 2)"
    - "(x − 5)(x + 2)"
    - "(x + 5)(x − 2)"
  answer: 2
  explanation: "We need p + q = −3 and p × q = −10. Since c is negative, one factor must be positive and one negative. Testing: (−5) + 2 = −3 ✓ and (−5)(2) = −10 ✓. So (x − 5)(x + 2) is correct. Verify by FOILing: x² + 2x − 5x − 10 = x² − 3x − 10. Option D, (x + 5)(x − 2), gives x² + 3x − 10 — the sign of b is flipped, a common error when negatives are involved."

- question: "When factoring x² − 9x + 20, you should look for two negative numbers that add to −9 and multiply to 20."
  type: true-false
  answer: true
  explanation: "When c (the constant term) is positive and b (the middle coefficient) is negative, both numbers must be negative: a negative times a negative gives a positive product, and two negatives sum to a negative. For x² − 9x + 20, we need numbers that add to −9 and multiply to 20: that's −4 and −5, giving (x − 4)(x − 5). Forgetting to consider negative factors is one of the most common errors in factoring."

- question: "When the leading coefficient is greater than 1 (e.g., 2x² + 7x + 3), you can factor the trinomial by finding two numbers that add to 7 and multiply to 3."
  type: true-false
  answer: false
  explanation: "When a ≠ 1, you cannot simply find factors of c that add to b. The AC method is needed: multiply a × c (here, 2 × 3 = 6), then find factors of that product that add to b (here, 1 + 6 = 7). Use these to split the middle term: 2x² + x + 6x + 3, then factor by grouping: x(2x + 1) + 3(2x + 1) = (x + 3)(2x + 1). Applying the simpler method ignores the leading coefficient and produces incorrect results."

- question: "Explain why factoring a trinomial of the form x² + bx + c is described as 'reversing FOIL,' and what two conditions the two numbers must satisfy."
  type: short-answer
  answer: "Factoring reverses FOIL because FOIL-ing (x + p)(x + q) produces x² + (p+q)x + pq — so b equals the sum p+q and c equals the product p×q. To factor, we find p and q such that p + q = b and p × q = c."
  explanation: "This is why b and c play different roles: b comes from adding the two numbers while c comes from multiplying them. A student who searches for numbers that 'add to c' or 'multiply to b' has inverted the relationship. Always verify by FOILing the answer: if the result matches the original trinomial, the factors are correct."
```

## Explainer

Factoring trinomials is the reverse of the FOIL process you already know. When you multiplied (x + 3)(x + 4) using FOIL, you got x² + 7x + 12. Factoring runs that process backward: given x² + 7x + 12, find the two binomials. Because FOIL produces a coefficient of x equal to the sum of the two constants, and a constant term equal to their product, the problem reduces to: find two numbers p and q such that p + q = 7 and p × q = 12.

The most reliable approach is systematic: list factor pairs of 12 — (1, 12), (2, 6), (3, 4) — and check which pair sums to 7. The pair (3, 4) works: 3 + 4 = 7 and 3 × 4 = 12, so x² + 7x + 12 = (x + 3)(x + 4). Negative signs follow the same logic with signed numbers. For x² − x − 12, you need p + q = −1 and p × q = −12. The pair (3, −4) works: 3 + (−4) = −1 and 3 × (−4) = −12, giving (x + 3)(x − 4). When c is negative, one factor must be positive and one negative; when c is positive and b is negative, both factors are negative.

When the leading coefficient is not 1 — say 2x² + 7x + 3 — the **AC method** extends the same idea. Multiply the leading coefficient by the constant: 2 × 3 = 6. Find two numbers that multiply to 6 and add to 7: those are 1 and 6. Use these to split the middle term: 2x² + x + 6x + 3. Now factor by grouping — the GCF work you already know: x(2x + 1) + 3(2x + 1) = (x + 3)(2x + 1). The grouping step works precisely because both pairs share the binomial factor (2x + 1).

Always verify by FOILing your answer — this habit catches sign errors immediately. Factoring trinomials builds directly into solving quadratic equations: once you write ax² + bx + c as a product of two binomials, the **zero product property** lets you find roots by setting each factor to zero. A trinomial that doesn't factor over the integers is called **irreducible over ℤ** and requires the quadratic formula, which you'll encounter next.
