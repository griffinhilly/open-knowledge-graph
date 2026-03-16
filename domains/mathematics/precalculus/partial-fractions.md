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

## Explainer

Partial fraction decomposition is the **reverse of adding fractions**. When you add 2/(x + 1) + 3/(x − 2), you find a common denominator and combine: [2(x − 2) + 3(x + 1)] / [(x + 1)(x − 2)] = (5x − 1) / [(x + 1)(x − 2)]. Partial fractions does this backward — given (5x − 1) / [(x + 1)(x − 2)], recover the simpler pieces 2/(x + 1) and 3/(x − 2). The technique works because every proper rational function with a factorable denominator can be decomposed this way, and the decomposition is unique.

The first step is always a check of degrees. If the degree of the numerator is greater than or equal to the degree of the denominator, perform **polynomial long division** first — exactly as your prerequisite covered. Long division produces a polynomial quotient plus a remainder fraction whose numerator degree is strictly less than its denominator degree. This "proper" fraction is what you decompose. For example, (x³ + 2x) / (x² − 1) is improper; long division gives x + (3x) / (x² − 1), and you decompose only the remainder.

Once you have a proper fraction, factor the denominator completely and set up the decomposition form. The rules are: a **distinct linear factor** (x − r) contributes A/(x − r); a **repeated linear factor** (x − r)^k contributes A/(x − r) + B/(x − r)² + ··· + K/(x − r)^k (one term for each power); an **irreducible quadratic factor** (x² + bx + c) contributes (Ax + B)/(x² + bx + c). A linear numerator is required for the quadratic case because there are two degrees of freedom — a constant numerator cannot match both the numerator and derivative constraints a degree-2 denominator creates.

To find the coefficients, multiply both sides of the decomposition by the full denominator to clear fractions. This yields a polynomial identity that holds for all x. **Strategic substitution** — plugging in the roots of each factor — is usually fastest: for x = 2 in A(x − 2) + B(x + 1) = 5x − 1, the A-term vanishes and you get 3B = 9, B = 3; at x = −1, the B-term vanishes and you get −3A = −6, A = 2. For repeated or quadratic factors where roots are complex or repeated, equating coefficients of each power of x is often cleaner. Always verify by recombining the result. This algebraic identity is the foundation for integrating rational functions in calculus — 2/(x + 1) and 3/(x − 2) each integrate immediately to natural logarithms, while the combined fraction is far harder to integrate directly.
