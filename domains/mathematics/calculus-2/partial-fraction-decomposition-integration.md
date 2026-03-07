---
id: partial-fraction-decomposition-integration
title: Partial Fraction Decomposition for Integration
domain: mathematics
course: calculus-2
prerequisites:
  - id: partial-fractions
    type: hard
  - id: u-substitution
    type: hard
  - id: derivatives-of-inverse-trig-functions
    type: soft
builds-toward:
  - improper-integrals-convergence
tags: [integration, techniques, partial-fractions]
stage: formal-systems
status: draft
---

# Partial Fraction Decomposition for Integration

## Core Idea
Partial fraction decomposition breaks a rational function into a sum of simpler fractions that can each be integrated individually. Linear factors produce ln terms, repeated linear factors produce power-rule terms, and irreducible quadratic factors produce arctan and ln terms (via completing the square). This technique, combined with polynomial long division for improper fractions, allows you to integrate any rational function.

## How It's Best Learned
Review the algebraic decomposition from precalculus, then integrate each term. Practice all cases: distinct linear, repeated linear, irreducible quadratic, and combinations. Emphasize the strategy: long division first if needed, then factor, decompose, and integrate term by term.

## Common Misconceptions
- Forgetting to do long division when the degree of the numerator is greater than or equal to the denominator.
- Not recognizing irreducible quadratic factors (try to factor first, then use the discriminant test).
- Making algebraic errors when solving for the coefficients A, B, C.
