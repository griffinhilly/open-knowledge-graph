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

## Questions

```yaml
- question: "You want to integrate (x³ + 2x) / (x² − 1). What is the correct first step?"
  type: multiple-choice
  options:
    - "Factor the denominator and set up A/(x−1) + B/(x+1) immediately"
    - "Perform polynomial long division, since the numerator degree exceeds the denominator degree"
    - "Complete the square in the denominator to identify irreducible factors"
    - "Apply u-substitution with u = x² − 1"
  answer: 1
  explanation: "Partial fraction decomposition only applies to proper fractions (numerator degree < denominator degree). Here the numerator has degree 3 and the denominator degree 2, so the fraction is improper. Long division must come first, producing a polynomial plus a proper remainder; only the remainder is then decomposed. Jumping straight to partial fractions (option A) leads to an inconsistent system of equations — there won't be enough unknowns to match all numerator coefficients."

- question: "Which integral form does the irreducible quadratic factor (x² + 9) in the denominator contribute?"
  type: multiple-choice
  options:
    - "A logarithm term A·ln|x² + 9|"
    - "A power-rule term −A/(x² + 9)"
    - "An arctan term (and possibly a logarithm term from the linear part of the numerator)"
    - "Two separate logarithm terms from the complex roots of x² + 9"
  answer: 2
  explanation: "Because x² + 9 has discriminant 0 − 36 < 0, it has no real roots and cannot be factored — it is irreducible. Its partial fraction form is (Ax + B)/(x² + 9). The Ax part produces A·ln|x² + 9| via u-substitution, and the B part produces (B/3)arctan(x/3) via the standard inverse-trig integral ∫1/(x²+k²) dx = (1/k)arctan(x/k). Option D is wrong: complex roots never appear in real partial fraction decomposition; irreducibility is precisely what prevents factoring into real linear terms."

- question: "Partial fraction decomposition can be applied directly to any rational function, regardless of the relative degrees of the numerator and denominator."
  type: true-false
  answer: false
  explanation: "Partial fractions require a proper fraction — one where the numerator degree is strictly less than the denominator degree. When the numerator degree is greater than or equal to the denominator degree, polynomial long division must be performed first, separating the expression into a polynomial (integrated directly by the power rule) plus a proper fractional remainder. Skipping this step produces an inconsistent coefficient system that cannot be solved."

- question: "A distinct linear factor (x − r) in the denominator always contributes a natural logarithm term to the antiderivative."
  type: true-false
  answer: true
  explanation: "The partial fraction form for a distinct linear factor is A/(x − r). Integrating via u-substitution (u = x − r) gives A·ln|x − r| + C, regardless of the value of r. This is the standard result and holds universally for distinct (non-repeated) linear factors. Repeated linear factors (x − r)² behave differently — their additional terms integrate by the power rule to −A/(x − r), not a logarithm."

- question: "Why must polynomial long division precede partial fraction decomposition when the numerator degree is greater than or equal to the denominator degree?"
  type: short-answer
  answer: "The partial fraction template assumes a proper fraction. If the fraction is improper, matching the coefficients of the partial fraction form requires more unknowns than the template provides — the system of equations is inconsistent and cannot be solved. Long division first extracts the polynomial part (which integrates term by term by the power rule) and leaves a proper remainder for decomposition."
  explanation: "Students who skip long division typically realize the mistake when their coefficient equations have no solution. The structural reason is that a degree-k numerator over a degree-k denominator includes a constant quotient term that doesn't fit any partial fraction form. Long division makes that term explicit, reducing the remaining problem to one the template can handle."
```

## Explainer

The core strategy is to work backwards from addition. You know how to add fractions: 1/(x−1) + 2/(x+3) = (3x+1)/((x−1)(x+3)). **Partial fraction decomposition** reverses this: given a rational function like (3x+1)/((x−1)(x+3)), break it back into simpler fractions. From your algebra prerequisite, you know how to do this decomposition. Now the payoff: each simple fraction is integrable by a method you already know, so a rational function that seemed hard to integrate becomes a sum of easy integrals.

The three cases and their integrals follow a consistent pattern. A **distinct linear factor** (x − r) contributes a term A/(x−r), which integrates to A·ln|x−r| + C via u-substitution. A **repeated linear factor** (x − r)² contributes A/(x−r) + B/(x−r)², where the second term integrates by the power rule to −B/(x−r) + C. An **irreducible quadratic factor** (ax²+bx+c with negative discriminant) requires completing the square and splitting the numerator, producing arctan terms — this is where your soft prerequisite (inverse trig derivatives) becomes essential, since ∫1/(x²+k²) dx = (1/k)arctan(x/k) + C.

The full procedure has four steps: (1) if the numerator degree ≥ denominator degree, do **polynomial long division first** to produce a proper fraction plus a polynomial; (2) factor the denominator completely into linear and irreducible quadratic factors; (3) set up the partial fraction form and solve for all coefficients (by substituting convenient values of x or expanding and matching coefficients); (4) integrate term by term. Skipping step 1 is the most common mistake — the decomposition template only applies to proper fractions (numerator degree strictly less than denominator degree). If you skip it, you'll find the algebra won't close.

This technique matters beyond its direct applications because it illustrates a broader mathematical strategy: transform a hard problem into multiple easy ones. A rational function that resists integration directly becomes a sum of logarithm, arctan, and power functions you've already mastered. The theoretical guarantee — that every rational function can be integrated in closed form — is precisely what partial fractions makes constructive.
