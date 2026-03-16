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
status: validated
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

## Explainer

The core strategy is to work backwards from addition. You know how to add fractions: 1/(x−1) + 2/(x+3) = (3x+1)/((x−1)(x+3)). **Partial fraction decomposition** reverses this: given a rational function like (3x+1)/((x−1)(x+3)), break it back into simpler fractions. From your algebra prerequisite, you know how to do this decomposition. Now the payoff: each simple fraction is integrable by a method you already know, so a rational function that seemed hard to integrate becomes a sum of easy integrals.

The three cases and their integrals follow a consistent pattern. A **distinct linear factor** (x − r) contributes a term A/(x−r), which integrates to A·ln|x−r| + C via u-substitution. A **repeated linear factor** (x − r)² contributes A/(x−r) + B/(x−r)², where the second term integrates by the power rule to −B/(x−r) + C. An **irreducible quadratic factor** (ax²+bx+c with negative discriminant) requires completing the square and splitting the numerator, producing arctan terms — this is where your soft prerequisite (inverse trig derivatives) becomes essential, since ∫1/(x²+k²) dx = (1/k)arctan(x/k) + C.

The full procedure has four steps: (1) if the numerator degree ≥ denominator degree, do **polynomial long division first** to produce a proper fraction plus a polynomial; (2) factor the denominator completely into linear and irreducible quadratic factors; (3) set up the partial fraction form and solve for all coefficients (by substituting convenient values of x or expanding and matching coefficients); (4) integrate term by term. Skipping step 1 is the most common mistake — the decomposition template only applies to proper fractions (numerator degree strictly less than denominator degree). If you skip it, you'll find the algebra won't close.

This technique matters beyond its direct applications because it illustrates a broader mathematical strategy: transform a hard problem into multiple easy ones. A rational function that resists integration directly becomes a sum of logarithm, arctan, and power functions you've already mastered. The theoretical guarantee — that every rational function can be integrated in closed form — is precisely what partial fractions makes constructive.
