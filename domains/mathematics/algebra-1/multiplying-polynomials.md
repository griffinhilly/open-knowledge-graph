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

## Questions

```yaml
- question: "Expand (x + 3)(x² − 2x + 1). Which result is correct?"
  type: multiple-choice
  options:
    - "x³ − 2x² + x + 3 (distributing only the x-term and then adding 3)"
    - "x³ + x² − 5x + 3"
    - "x³ + x² + x + 3"
    - "x³ − 2x² + 3x² + 1"
  answer: 1
  explanation: "Distributing fully: x·x² = x³, x·(−2x) = −2x², x·1 = x; then 3·x² = 3x², 3·(−2x) = −6x, 3·1 = 3. Combining like terms: x³ + (−2+3)x² + (1−6)x + 3 = x³ + x² − 5x + 3. Option A is the classic error — the 3 is only added once rather than distributed across all three terms of the trinomial."

- question: "When you multiply a binomial by a trinomial using the 'each by each' approach, how many individual products are generated before combining like terms?"
  type: multiple-choice
  options:
    - "3 — one for each term in the trinomial"
    - "4 — like the FOIL method"
    - "5 — the sum of the number of terms in both polynomials"
    - "6 — the product of the number of terms in each polynomial"
  answer: 3
  explanation: "Each of the 2 terms in the binomial multiplies each of the 3 terms in the trinomial: 2 × 3 = 6 products total. This generalizes: an m-term polynomial times an n-term polynomial always produces m × n products before combining. FOIL's four products are simply the 2 × 2 case."

- question: "When computing 3x · 2x², the exponents 1 and 2 are added to give x³."
  type: true-false
  answer: true
  explanation: "The product rule for exponents states x^a · x^b = x^(a+b). Here, x¹ · x² = x^(1+2) = x³, and the coefficients 3 and 2 multiply separately to give 6, yielding 6x³. This exponent rule applies at every individual multiplication step in polynomial multiplication."

- question: "FOIL is a reliable method for multiplying any two polynomials."
  type: true-false
  answer: false
  explanation: "FOIL (First, Outer, Inner, Last) only works for binomial × binomial — the 2 × 2 case. It breaks down the moment either polynomial has more than two terms. For a binomial times a trinomial (2 × 3), you need 6 products, but FOIL only produces 4. The general 'each by each' approach or grid model works for any polynomial sizes."

- question: "Why does the grid (area) model prevent the most common error in polynomial multiplication?"
  type: short-answer
  answer: "The grid assigns exactly one cell to each pair of terms — one row per term in the first polynomial, one column per term in the second. Every cell must be filled, making it structurally impossible to skip a term. You cannot accidentally 'forget' to multiply 3 by −2x because that cell exists in the grid and must be computed."
  explanation: "The most common error is partial distribution — distributing one term to all others, but missing some combinations for another term. The grid makes every combination explicit and visible, turning a procedural task (distribute everything) into a spatial one (fill every cell). This is also why the grid reveals the structural parallel to multi-digit integer multiplication."
```

## Explainer

You already know the distributive property: a(b + c) = ab + ac. Multiplying polynomials is nothing more than applying the distributive property repeatedly — once for every term in the first polynomial. The key rule is: **every term in the first polynomial must be multiplied by every term in the second polynomial**. No term gets skipped, no pair gets counted twice. If the first polynomial has m terms and the second has n terms, you will produce exactly m × n individual products before combining like terms.

Start with the simplest case: a monomial times a polynomial. When you compute 3x(2x² − 4x + 1), distribute the 3x to each term: 3x · 2x² = 6x³, 3x · (−4x) = −12x², and 3x · 1 = 3x. The exponent rule you already know — x^a · x^b = x^(a+b) — handles the variable part automatically at each step. The result is 6x³ − 12x² + 3x. Because a monomial times a trinomial gives three products (1 × 3 = 3), and none are like terms here, no combining is needed. The exponents 3, 2, and 1 are all distinct.

Now extend to binomial times trinomial: (x + 3)(x² − 2x + 1). Each of the two terms in (x + 3) distributes across all three terms of the trinomial, giving 2 × 3 = 6 products. The x-terms produce x · x² = x³, x · (−2x) = −2x², x · 1 = x. The 3-terms produce 3 · x² = 3x², 3 · (−2x) = −6x, 3 · 1 = 3. Now collect **like terms** — terms with identical variable-and-exponent combinations: x³ + (−2x² + 3x²) + (x − 6x) + 3 = x³ + x² − 5x + 3. The combining step is where errors pile up, so be systematic: sort by degree before adding.

A useful organizational tool is the **grid (area) model**: draw a rectangle with the terms of one polynomial labeling the rows and the other labeling the columns. Each cell holds one product — no term can be missed. This model also makes visible why polynomial multiplication parallels multi-digit multiplication. (x + 3)(x + 7) has the same structure as 13 × 17: the place-value columns are just carried symbolically rather than numerically. Mastering the general grid approach makes FOIL unnecessary — FOIL is simply the shorthand name for the 2 × 2 grid case, and it breaks down the moment either polynomial has more than two terms.
