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

## Explainer

You already know how to multiply polynomials using the distributive property: multiply each term in the first polynomial by each term in the second, then collect like terms. FOIL is not a new rule — it's a memory trick for organizing that distribution when both polynomials happen to be **binomials** (exactly two terms each). The name labels the four products in the order you should compute them: First, Outer, Inner, Last.

Take (x + 3)(x − 5). The distributive property says: multiply x by everything in the second binomial, then multiply 3 by everything in the second. That gives four products: x·x (First), x·(−5) (Outer), 3·x (Inner), and 3·(−5) (Last). Result: x² − 5x + 3x − 15. The outer and inner terms are both linear (containing x), so they combine: −5x + 3x = −2x, giving the **trinomial** x² − 2x − 15. This shape — x² + bx + c — is what you will spend most of Algebra 2 learning to factor back apart.

An area model makes this visual. Draw a 2×2 rectangle with (x + 3) along the top and (x − 5) along the side. The four cells are exactly the four FOIL products. Each product occupies its region: x² in the top-left, −5x top-right, 3x bottom-left, −15 bottom-right. The total area is the sum of the four cells. This model explains why no product can be missed and why the middle terms add: they're both rectangular strips of the same type (length × number).

Two **special products** reward recognizing the pattern before computing. When both binomials are identical, (x + a)² = x² + 2ax + a² — a **perfect square trinomial**. The coefficient of the middle term is always twice the product of the two constants. Students frequently write (x + 3)² = x² + 9, which omits the middle term entirely; the correct expansion is x² + 6x + 9. The other special case is (x + a)(x − a) = x² − a², the **difference of squares** — the outer and inner terms are equal and opposite, so they cancel, leaving no middle term at all.

FOIL's limitation is worth naming: the mnemonic only applies to binomial × binomial. If you multiply a trinomial by a binomial, you need three distributions, not four. Thinking of the distributive property as the underlying rule — and FOIL as a convenient shortcut for the 2×2 case — keeps the method flexible and prevents confusion when the polynomials have more terms.
