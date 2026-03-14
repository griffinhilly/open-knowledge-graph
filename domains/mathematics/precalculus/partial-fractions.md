---
id: partial-fractions
title: Partial Fraction Decomposition
domain: mathematics
course: precalculus
prerequisites:
  - id: polynomial-division-review
    type: hard
  - id: rational-functions-asymptotes-review
    type: soft
builds-toward:
  - partial-fraction-decomposition-integration
tags: [algebra, partial-fractions, rational-expressions]
stage: formal-systems
status: validated
---

# Partial Fraction Decomposition

## Core Idea
Partial fraction decomposition reverses the process of adding fractions: it breaks a complicated rational expression into a sum of simpler fractions whose denominators are the factors of the original denominator. For example, (2x + 3)/((x + 1)(x - 2)) = A/(x + 1) + B/(x - 2). This algebraic technique is essential preparation for integration of rational functions in Calculus 2.

## How It's Best Learned
Start with distinct linear factors (easiest case), then progress to repeated linear factors and irreducible quadratic factors. Practice setting up the decomposition form, clearing denominators, and solving for coefficients by strategic substitution or by equating coefficients. Always verify by recombining.

## Common Misconceptions
- Forgetting to perform polynomial long division first when the degree of the numerator is greater than or equal to the degree of the denominator.
- Missing repeated factor terms: (x - 1)^2 requires both A/(x - 1) and B/(x - 1)^2.
- Using A/(x^2 + 1) instead of (Ax + B)/(x^2 + 1) for irreducible quadratic factors.
