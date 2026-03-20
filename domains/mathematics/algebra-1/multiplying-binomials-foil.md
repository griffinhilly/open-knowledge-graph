---
id: multiplying-binomials-foil
title: Multiplying Binomials (FOIL)
domain: mathematics
course: algebra-1
prerequisites:
  - id: multiplying-polynomials
    type: hard
builds-toward:
  - factoring-trinomials
  - factoring-difference-of-squares
  - solving-quadratics-by-factoring
tags: [FOIL, binomials, multiplication, polynomials]
stage: abstract-reasoning
status: validated
---

# Multiplying Binomials (FOIL)

## Core Idea
FOIL is a mnemonic for multiplying two binomials: First, Outer, Inner, Last. For (x + 3)(x − 5): First: x·x = x², Outer: x·(−5) = −5x, Inner: 3·x = 3x, Last: 3·(−5) = −15. Combine: x² − 5x + 3x − 15 = x² − 2x − 15. FOIL is simply the distributive property applied systematically — it ensures no product is missed. It is the most frequently used multiplication pattern in algebra because it produces the standard trinomials that students later learn to factor. Special products — perfect square trinomials and difference of squares — are FOIL applied to specific binomial pairs.

## How It's Best Learned
Practice FOIL as a procedure while emphasizing it is just organized distribution. Show the connection between FOIL and the area model (a 2×2 grid). Include special cases: (x + a)² = x² + 2ax + a² (perfect square trinomial) and (x + a)(x − a) = x² − a² (difference of squares). Have students recognize these patterns before formally naming them.

## Common Misconceptions
- Thinking (x + 3)² = x² + 9 (squaring each term instead of FOILing — missing the middle term 6x).
- Forgetting to combine the outer and inner terms.
- Trying to apply FOIL to non-binomial products (FOIL only works for binomial × binomial; use general distribution otherwise).

## Questions

```yaml
- question: "A student expands (x + 5)² and writes x² + 25. What error did they make, and what is the correct answer?"
  type: multiple-choice
  options:
    - "They forgot to square the constant — the correct answer is x² + 5²"
    - "They squared each term separately instead of applying FOIL — the correct answer is x² + 10x + 25"
    - "They only computed the First and Last terms of FOIL — the correct answer is x² + 5x + 25"
    - "They applied the difference of squares pattern incorrectly — the correct answer is x² − 25"
  answer: 1
  explanation: "The error is squaring each term separately: (x + 5)² ≠ x² + 5². FOIL gives four products: First (x·x = x²), Outer (x·5 = 5x), Inner (5·x = 5x), Last (5·5 = 25). Combining: x² + 5x + 5x + 25 = x² + 10x + 25. The middle term 10x comes from the outer and inner products — exactly the term that gets dropped when students incorrectly distribute the exponent. For (x + a)², the correct pattern is always x² + 2ax + a², and the middle coefficient is always twice the product of the two terms."

- question: "A student tries to use FOIL to multiply (x² + 3x + 2)(x + 1). What is the problem with this approach?"
  type: multiple-choice
  options:
    - "FOIL only works when the first factor has a leading coefficient of 1"
    - "FOIL only applies to binomial × binomial; one factor here is a trinomial, requiring full distribution"
    - "FOIL cannot be applied when the second factor contains a constant term"
    - "FOIL requires both factors to have the same degree"
  answer: 1
  explanation: "FOIL is a mnemonic for organizing the four products that arise when multiplying exactly two binomials (two-term expressions). When one factor is a trinomial (three terms), there are six products to compute (3 × 2), not four. The correct approach is full distribution: multiply each term in the trinomial by each term in the binomial. Thinking of FOIL as a special case of the distributive property — rather than a separate rule — makes it natural to extend distribution to any polynomial multiplication."

- question: "FOIL is a mathematical rule distinct from the distributive property, specifically designed for polynomial multiplication."
  type: true-false
  answer: false
  explanation: "FOIL is not a separate rule — it is a mnemonic for organizing the distributive property when both factors are binomials. The distributive property says: multiply each term in the first polynomial by each term in the second. For two binomials, this produces exactly four products, and FOIL names them in order (First, Outer, Inner, Last) to prevent any from being missed. Treating FOIL as an independent rule leads to confusion about when it applies and why it works."

- question: "When expanding (x + a)(x − a), the outer and inner terms cancel, leaving no middle term in the result."
  type: true-false
  answer: true
  explanation: "FOIL gives: First = x², Outer = −ax, Inner = +ax, Last = −a². The outer term is −ax and the inner term is +ax — they are equal in magnitude and opposite in sign, so they sum to zero. The result is x² − a², the difference of squares pattern. This cancellation happens whenever the two binomials differ only in the sign of their constant term. Recognizing this pattern before computing saves time and reveals algebraic structure."

- question: "Why does (x + 3)² equal x² + 6x + 9, not x² + 9? Explain where the middle term comes from."
  type: short-answer
  answer: "Squaring (x + 3) means multiplying (x + 3)(x + 3). FOIL produces four products: x·x = x², x·3 = 3x, 3·x = 3x, and 3·3 = 9. The two middle terms (3x + 3x = 6x) come from the outer and inner products. The error x² + 9 omits these entirely, as if (x + 3)² meant 'square each term separately,' which violates the distributive property."
  explanation: "The middle term 6x is the signature of a perfect square trinomial. For any (x + a)², the middle term is always 2ax — twice the product of the two terms in the binomial. This is because the outer and inner FOIL products are always identical for a perfect square, so they add rather than cancel. Understanding this pattern prevents the most common FOIL error and prepares students to recognize and factor perfect square trinomials later."
```

## Explainer

You already know how to multiply polynomials using the distributive property: multiply each term in the first polynomial by each term in the second, then collect like terms. FOIL is not a new rule — it's a memory trick for organizing that distribution when both polynomials happen to be **binomials** (exactly two terms each). The name labels the four products in the order you should compute them: First, Outer, Inner, Last.

Take (x + 3)(x − 5). The distributive property says: multiply x by everything in the second binomial, then multiply 3 by everything in the second. That gives four products: x·x (First), x·(−5) (Outer), 3·x (Inner), and 3·(−5) (Last). Result: x² − 5x + 3x − 15. The outer and inner terms are both linear (containing x), so they combine: −5x + 3x = −2x, giving the **trinomial** x² − 2x − 15. This shape — x² + bx + c — is what you will spend most of Algebra 2 learning to factor back apart.

An area model makes this visual. Draw a 2×2 rectangle with (x + 3) along the top and (x − 5) along the side. The four cells are exactly the four FOIL products. Each product occupies its region: x² in the top-left, −5x top-right, 3x bottom-left, −15 bottom-right. The total area is the sum of the four cells. This model explains why no product can be missed and why the middle terms add: they're both rectangular strips of the same type (length × number).

Two **special products** reward recognizing the pattern before computing. When both binomials are identical, (x + a)² = x² + 2ax + a² — a **perfect square trinomial**. The coefficient of the middle term is always twice the product of the two constants. Students frequently write (x + 3)² = x² + 9, which omits the middle term entirely; the correct expansion is x² + 6x + 9. The other special case is (x + a)(x − a) = x² − a², the **difference of squares** — the outer and inner terms are equal and opposite, so they cancel, leaving no middle term at all.

FOIL's limitation is worth naming: the mnemonic only applies to binomial × binomial. If you multiply a trinomial by a binomial, you need three distributions, not four. Thinking of the distributive property as the underlying rule — and FOIL as a convenient shortcut for the 2×2 case — keeps the method flexible and prevents confusion when the polynomials have more terms.
