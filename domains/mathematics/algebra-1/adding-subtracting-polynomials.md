---
id: adding-subtracting-polynomials
title: Adding and Subtracting Polynomials
domain: mathematics
course: algebra-1
prerequisites:
  - id: polynomials-intro
    type: hard
  - id: combining-like-terms
    type: hard
builds-toward:
  - multiplying-polynomials
  - factoring-gcf
tags: [polynomials, addition, subtraction, like-terms]
stage: abstract-reasoning
status: validated
---

# Adding and Subtracting Polynomials

## Core Idea
Adding polynomials means combining like terms — terms with the same variable and exponent. (3x² + 2x − 5) + (x² − 4x + 7) = 4x² − 2x + 2. Subtracting polynomials requires distributing the negative sign across all terms of the second polynomial first, then combining like terms: (3x² + 2x − 5) − (x² − 4x + 7) = 3x² + 2x − 5 − x² + 4x − 7 = 2x² + 6x − 12. This skill extends the combining-like-terms concept from prealgebra to multi-term expressions with higher powers.

## How It's Best Learned
Use vertical alignment (stacking polynomials with like terms in columns) as a visual aid. Emphasize that subtraction means distributing the negative to every term — practice this step in isolation before combining. Use algebra tiles for concrete representation. Practice with polynomials of varying degrees and missing terms (e.g., x³ + 5 has no x² or x terms).

## Common Misconceptions
- When subtracting, only negating the first term of the second polynomial (forgetting to distribute the negative).
- Combining unlike terms (adding x² and x to get 2x² or 2x).
- Dropping terms that have no like term to combine with (the term just stays as-is).

## Questions

```yaml
- question: "Compute (3x² + 2x − 5) − (x² − 4x + 7)."
  type: multiple-choice
  options:
    - "2x² − 2x − 12 — only the first term of the second polynomial is negated"
    - "2x² + 6x − 12 — the negative is distributed to every term of the second polynomial"
    - "4x² − 2x + 2 — the polynomials are added instead of subtracted"
    - "2x² − 6x + 2 — the sign of the x-term is negated twice"
  answer: 1
  explanation: "The key step: distribute the negative to every term of (x² − 4x + 7), giving (−x² + 4x − 7). Note that −(−4x) = +4x, which is the step most commonly missed. Then combine like terms column by column: (3x² − x²) = 2x², (2x + 4x) = 6x, (−5 − 7) = −12. Result: 2x² + 6x − 12. Answer A is the classic error — only negating the first term (getting −x² but leaving −4x unchanged), which gives 2x² − 2x − 12."

- question: "Which of the following is a valid step when adding 5x³ + 2x to 3x² + x?"
  type: multiple-choice
  options:
    - "Combine 5x³ and 3x² to get 8x⁵, since both terms contain x"
    - "Combine 2x and x to get 3x, since both terms are x-terms with the same exponent"
    - "Combine 5x³ and x to get 5x⁴, multiplying the exponents"
    - "Combine all four terms into one expression since they all involve x"
  answer: 1
  explanation: "Only like terms — same variable AND same exponent — can be combined. 2x and x both have variable x to the first power, so they combine: 2x + x = 3x. The terms 5x³ and 3x² cannot be combined because their exponents differ (3 vs. 2): they belong to different 'species.' Exponents are labels that identify the species, not numbers to add. The result is 5x³ + 3x² + 3x — four terms become three because only one pair of like terms existed."

- question: "When subtracting one polynomial from another, you only need to change the sign of the first term of the polynomial being subtracted."
  type: true-false
  answer: false
  explanation: "This is the most common error in polynomial subtraction. The subtraction sign applies to the entire polynomial — every term within it — because the expression A − (B + C + D) must be rewritten as A + (−B) + (−C) + (−D). Changing only the first term's sign leaves the remaining terms with incorrect signs, producing a wrong answer. Every term inside the parentheses must be negated before combining like terms."

- question: "When adding or subtracting polynomials, the exponents of like terms are added together along with their coefficients."
  type: true-false
  answer: false
  explanation: "Exponents are never added when combining like terms — they remain unchanged. When you combine 3x² + x², the exponents stay at 2: the result is 4x², not 4x⁴. Exponents serve as labels identifying which 'species' of term you are dealing with (the x²-species, the x-species, the constant-species). Only coefficients are added. Exponent addition belongs to multiplication, not addition — this is a critical distinction to keep clear."

- question: "Why must the negative sign be distributed to every term when subtracting a polynomial, rather than just the first term?"
  type: short-answer
  answer: "Because subtraction means adding the opposite of the entire polynomial, not just its first term. The expression A − (B + C) is equivalent to A + (−1)(B + C) = A − B − C. The negative one multiplies every term inside the parentheses by the distributive property. Negating only the first term treats the parentheses as if they weren't there, which changes the mathematical meaning of the expression."
  explanation: "The parentheses in polynomial subtraction are not decorative — they indicate that the negative sign applies to the whole group. This is the same distributive property students use when expanding −2(x + 3) = −2x − 6. Polynomial subtraction is just a special case where the coefficient is −1. Keeping this principle clear prevents the most common error in this topic."
```

## Explainer

You already know how to combine like terms: 3x + 5x = 8x because both terms contain the same variable to the same power. Adding and subtracting polynomials is exactly this skill applied to expressions with multiple types of terms at once. A polynomial like 3x² + 2x − 5 contains three types: an x²-term, an x-term, and a constant. Each type is its own "species," and species can only combine with their own kind.

When adding two polynomials, line them up so matching species are in the same column — this visual alignment makes it nearly impossible to accidentally combine unlike terms. For (3x² + 2x − 5) + (x² − 4x + 7): the x²-column gives 3x² + x² = 4x², the x-column gives 2x + (−4x) = −2x, and the constant column gives −5 + 7 = 2. Result: 4x² − 2x + 2. Notice that you never touch the exponents — they are labels that identify the species, not numbers to be added.

Subtraction introduces the single most important rule in this topic: **distribute the negative sign to every term** of the polynomial being subtracted. When you write A − B, you must mentally expand this to A + (−B), which means flipping the sign of every term in B before combining. For (3x² + 2x − 5) − (x² − 4x + 7), rewrite as (3x² + 2x − 5) + (−x² + 4x − 7). Note that −(−4x) became +4x — this sign flip is where most errors occur. Now combine columns normally: 2x² + 6x − 12.

A polynomial like x³ + 5 has "missing" terms — it has no x² or x component. Missing terms contribute zero to their column; treat them as 0x² + 0x and write placeholders if it helps. Subtraction of such a sparse polynomial is especially dangerous: every term in the sparse polynomial needs a sign flip, including invisible zero terms. Keeping columns aligned protects against gaps that disguise missing terms and makes verification easy.
