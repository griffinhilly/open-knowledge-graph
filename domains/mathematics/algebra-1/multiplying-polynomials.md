---
id: multiplying-polynomials
title: Multiplying Polynomials
domain: mathematics
course: algebra-1
prerequisites:
- id: polynomials-intro
  type: hard
- id: distributive-property
  type: hard
- id: exponent-rules-product-power-quotient
  type: hard
- id: adding-subtracting-polynomials
  type: soft
builds-toward:
- multiplying-binomials-foil
- factoring-trinomials
- factoring-difference-of-squares
tags:
- polynomials
- multiplication
- distributive-property
stage: abstract-reasoning
status: validated
---
# Multiplying Polynomials

## Core Idea
Multiplying polynomials extends the distributive property: every term in the first polynomial must be multiplied by every term in the second polynomial, and then like terms are combined. For a monomial times a polynomial, distribute the monomial: 3x(2x² − 4x + 1) = 6x³ − 12x² + 3x. For a binomial times a trinomial, each of the two terms distributes across all three terms, giving six products to combine. The exponent rules apply at each step (x^a × x^b = x^(a+b)). This is the foundation for FOIL, factoring, and polynomial division.

## How It's Best Learned
Start with monomial × polynomial (single distribution). Move to binomial × binomial (four products) before FOIL is introduced as a shortcut. Then practice binomial × trinomial and beyond using the "each by each" approach or a grid/area model. Emphasize combining like terms after multiplying. Use the area model for visual learners.

## Common Misconceptions
- Not distributing every term (e.g., in (x + 3)(x² − 2x + 1), forgetting to multiply 3 by all three terms).
- Adding exponents of unlike bases or within a single term incorrectly.
- Forgetting to combine like terms after distribution.

## Explainer

You already know the distributive property: a(b + c) = ab + ac. Multiplying polynomials is nothing more than applying the distributive property repeatedly — once for every term in the first polynomial. The key rule is: **every term in the first polynomial must be multiplied by every term in the second polynomial**. No term gets skipped, no pair gets counted twice. If the first polynomial has m terms and the second has n terms, you will produce exactly m × n individual products before combining like terms.

Start with the simplest case: a monomial times a polynomial. When you compute 3x(2x² − 4x + 1), distribute the 3x to each term: 3x · 2x² = 6x³, 3x · (−4x) = −12x², and 3x · 1 = 3x. The exponent rule you already know — x^a · x^b = x^(a+b) — handles the variable part automatically at each step. The result is 6x³ − 12x² + 3x. Because a monomial times a trinomial gives three products (1 × 3 = 3), and none are like terms here, no combining is needed. The exponents 3, 2, and 1 are all distinct.

Now extend to binomial times trinomial: (x + 3)(x² − 2x + 1). Each of the two terms in (x + 3) distributes across all three terms of the trinomial, giving 2 × 3 = 6 products. The x-terms produce x · x² = x³, x · (−2x) = −2x², x · 1 = x. The 3-terms produce 3 · x² = 3x², 3 · (−2x) = −6x, 3 · 1 = 3. Now collect **like terms** — terms with identical variable-and-exponent combinations: x³ + (−2x² + 3x²) + (x − 6x) + 3 = x³ + x² − 5x + 3. The combining step is where errors pile up, so be systematic: sort by degree before adding.

A useful organizational tool is the **grid (area) model**: draw a rectangle with the terms of one polynomial labeling the rows and the other labeling the columns. Each cell holds one product — no term can be missed. This model also makes visible why polynomial multiplication parallels multi-digit multiplication. (x + 3)(x + 7) has the same structure as 13 × 17: the place-value columns are just carried symbolically rather than numerically. Mastering the general grid approach makes FOIL unnecessary — FOIL is simply the shorthand name for the 2 × 2 grid case, and it breaks down the moment either polynomial has more than two terms.
