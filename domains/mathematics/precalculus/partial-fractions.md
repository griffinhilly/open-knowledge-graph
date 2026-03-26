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

## Questions

```yaml
- question: "You need to decompose (3x + 1) / ((x + 2)(x² + 9)) into partial fractions. What is the correct form to set up?"
  type: multiple-choice
  options:
    - "A/(x + 2) + B/(x² + 9)"
    - "A/(x + 2) + (Bx + C)/(x² + 9)"
    - "A/(x + 2) + B/(x² + 9) + C/(x² + 9)²"
    - "A/(x + 2) + B/x + C/9"
  answer: 1
  explanation: "An irreducible quadratic factor (x² + 9) requires a linear numerator (Bx + C), not a constant. This is because there are two degrees of freedom — the factor is degree 2, so a constant numerator cannot match both the coefficient and derivative constraints. Option A is the most common error: using A/(x² + 9) with a constant numerator. Options C and D are structurally wrong — C treats the quadratic as a repeated factor, D factors the constant incorrectly."

- question: "Before decomposing (x³ + 5x) / (x² − 4) into partial fractions, what must you do first — and why?"
  type: multiple-choice
  options:
    - "Factor the denominator as (x − 2)(x + 2) and immediately set up A/(x − 2) + B/(x + 2)"
    - "Perform polynomial long division, because the numerator degree (3) is not less than the denominator degree (2)"
    - "Cancel common factors between numerator and denominator"
    - "Set the denominator equal to zero to find the roots"
  answer: 1
  explanation: "Partial fraction decomposition only works on *proper* rational functions — those where the numerator degree is strictly less than the denominator degree. Here, degree 3 ≥ degree 2, so the fraction is improper. Long division produces a polynomial quotient plus a proper remainder fraction; you then decompose only the remainder. Skipping this step and jumping to A/(x−2) + B/(x+2) is the most common error and produces an incorrect decomposition."

- question: "The factor (x − 3)² in the denominator requires primarily one partial fraction term: B/(x − 3)²."
  type: true-false
  answer: false
  explanation: "A repeated linear factor (x − 3)² requires *two* terms: A/(x − 3) + B/(x − 3)². One term for each power up to the multiplicity. Using only B/(x − 3)² cannot account for the full structure of the original numerator — you'd be missing a degree of freedom. The general rule: (x − r)^k contributes k separate terms, from power 1 up through power k."

- question: "Partial fraction decomposition can only be applied after the rational expression has been converted into a proper fraction (numerator degree < denominator degree)."
  type: true-false
  answer: true
  explanation: "This is a prerequisite that is often overlooked. Partial fractions require the fraction to be proper because the decomposition is based on the denominator's factors — and those factors only account for a polynomial of the same degree as the denominator. If the numerator is larger, there is a polynomial portion that no sum of proper partial fractions can represent. Long division extracts that polynomial first, leaving a proper remainder to decompose."

- question: "Why does an irreducible quadratic factor like (x² + 4) require a linear numerator (Ax + B) in its partial fraction term, rather than a constant A?"
  type: short-answer
  answer: "Because a degree-2 denominator factor introduces two independent degrees of freedom that the numerator must match. A constant numerator has only one free parameter, which is insufficient to satisfy the polynomial identity that results from clearing denominators. A linear numerator Ax + B provides two parameters (A and B), giving enough flexibility to correctly match both the even and odd coefficient constraints across the entire identity."
  explanation: "Think of it this way: when you clear the denominator and equate coefficients, a quadratic factor generates two equations (one for each power of x up to degree 1 in the numerator). One free parameter (constant) can only satisfy one equation; two free parameters (linear) can satisfy two. This is why the technique is consistent: the number of unknowns always matches the number of equations when you set up the form correctly."
```

## Explainer

Partial fraction decomposition is the **reverse of adding fractions**. When you add 2/(x + 1) + 3/(x − 2), you find a common denominator and combine: [2(x − 2) + 3(x + 1)] / [(x + 1)(x − 2)] = (5x − 1) / [(x + 1)(x − 2)]. Partial fractions does this backward — given (5x − 1) / [(x + 1)(x − 2)], recover the simpler pieces 2/(x + 1) and 3/(x − 2). The technique works because every proper rational function with a factorable denominator can be decomposed this way, and the decomposition is unique.

The first step is always a check of degrees. If the degree of the numerator is greater than or equal to the degree of the denominator, perform **polynomial long division** first — exactly as your prerequisite covered. Long division produces a polynomial quotient plus a remainder fraction whose numerator degree is strictly less than its denominator degree. This "proper" fraction is what you decompose. For example, (x³ + 2x) / (x² − 1) is improper; long division gives x + (3x) / (x² − 1), and you decompose only the remainder.

Once you have a proper fraction, factor the denominator completely and set up the decomposition form. The rules are: a **distinct linear factor** (x − r) contributes A/(x − r); a **repeated linear factor** (x − r)^k contributes A/(x − r) + B/(x − r)² + ··· + K/(x − r)^k (one term for each power); an **irreducible quadratic factor** (x² + bx + c) contributes (Ax + B)/(x² + bx + c). A linear numerator is required for the quadratic case because there are two degrees of freedom — a constant numerator cannot match both the numerator and derivative constraints a degree-2 denominator creates.

To find the coefficients, multiply both sides of the decomposition by the full denominator to clear fractions. This yields a polynomial identity that holds for all x. **Strategic substitution** — plugging in the roots of each factor — is usually fastest: for x = 2 in A(x − 2) + B(x + 1) = 5x − 1, the A-term vanishes and you get 3B = 9, B = 3; at x = −1, the B-term vanishes and you get −3A = −6, A = 2. For repeated or quadratic factors where roots are complex or repeated, equating coefficients of each power of x is often cleaner. Always verify by recombining the result. This algebraic identity is the foundation for integrating rational functions in calculus — 2/(x + 1) and 3/(x − 2) each integrate immediately to natural logarithms, while the combined fraction is far harder to integrate directly.
