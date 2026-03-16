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

## Explainer

You already know how to combine like terms: 3x + 5x = 8x because both terms contain the same variable to the same power. Adding and subtracting polynomials is exactly this skill applied to expressions with multiple types of terms at once. A polynomial like 3x² + 2x − 5 contains three types: an x²-term, an x-term, and a constant. Each type is its own "species," and species can only combine with their own kind.

When adding two polynomials, line them up so matching species are in the same column — this visual alignment makes it nearly impossible to accidentally combine unlike terms. For (3x² + 2x − 5) + (x² − 4x + 7): the x²-column gives 3x² + x² = 4x², the x-column gives 2x + (−4x) = −2x, and the constant column gives −5 + 7 = 2. Result: 4x² − 2x + 2. Notice that you never touch the exponents — they are labels that identify the species, not numbers to be added.

Subtraction introduces the single most important rule in this topic: **distribute the negative sign to every term** of the polynomial being subtracted. When you write A − B, you must mentally expand this to A + (−B), which means flipping the sign of every term in B before combining. For (3x² + 2x − 5) − (x² − 4x + 7), rewrite as (3x² + 2x − 5) + (−x² + 4x − 7). Note that −(−4x) became +4x — this sign flip is where most errors occur. Now combine columns normally: 2x² + 6x − 12.

A polynomial like x³ + 5 has "missing" terms — it has no x² or x component. Missing terms contribute zero to their column; treat them as 0x² + 0x and write placeholders if it helps. Subtraction of such a sparse polynomial is especially dangerous: every term in the sparse polynomial needs a sign flip, including invisible zero terms. Keeping columns aligned protects against gaps that disguise missing terms and makes verification easy.
