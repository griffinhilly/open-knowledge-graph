---
id: fundamental-theorem-of-algebra
title: Fundamental Theorem of Algebra
domain: mathematics
course: algebra-2
prerequisites:
- id: complex-numbers-intro
  type: hard
- id: factor-theorem
  type: hard
- id: quadratic-formula-review
  type: soft
- id: graphing-polynomial-functions
  type: soft
- id: operations-with-complex-numbers
  type: soft
- id: rational-root-theorem
  type: soft
builds-toward:
- polynomial-division-review
tags:
- polynomials
- fundamental-theorem
- complex-roots
- degree
stage: abstract-reasoning
status: validated
---
# Fundamental Theorem of Algebra

## Core Idea
The Fundamental Theorem of Algebra states that every non-constant polynomial with complex coefficients has at least one complex root. A corollary: a degree-n polynomial has exactly n roots (counted with multiplicity) in the complex numbers. Complex roots of polynomials with real coefficients come in conjugate pairs: if a + bi is a root, so is a - bi. This theorem guarantees that the complex number system is "complete" for polynomial equations.

## How It's Best Learned
Start with examples: a degree-2 polynomial has 2 roots, a degree-3 has 3, etc. Show cases where some roots are complex (x^2 + 1 has roots i and -i). Emphasize the conjugate pairs property for real-coefficient polynomials. Practice writing polynomials given their roots (including complex ones). Do NOT attempt to prove the theorem; it requires analysis beyond Algebra 2.

## Common Misconceptions
- Thinking real roots and complex roots are separate categories (real numbers are complex numbers with imaginary part 0).
- Forgetting to count roots with multiplicity (x^2 = 0 has root x = 0 with multiplicity 2).
- Not recognizing the conjugate pairs requirement for real-coefficient polynomials.
- Thinking a degree-3 polynomial must have 3 real roots (it has 3 complex roots, of which 1 or 3 are real).

## Explainer

You've already studied complex numbers and the Factor Theorem. Now you have the tools to appreciate one of the most satisfying guarantees in all of mathematics. The **Fundamental Theorem of Algebra** says: every polynomial equation of degree n ≥ 1 has exactly n roots — but only if you allow complex numbers. Over the real numbers, polynomials can run out of roots (x² + 1 = 0 has no real solution). Over the complex numbers, they never do.

The Factor Theorem tells you that if r is a root of p(x), then (x - r) is a factor. The Fundamental Theorem guarantees the first root always exists, so you can always factor out at least one linear factor. Apply the theorem again to the remaining degree-(n-1) polynomial — it too has a root, so factor out another linear factor. Repeat until you've extracted all n factors. The conclusion: every degree-n polynomial factors completely as p(x) = a(x - r₁)(x - r₂)···(x - rₙ), where r₁, ..., rₙ are the n roots (counted with **multiplicity**) in ℂ. Multiplicity matters: x² = (x - 0)(x - 0) has root 0 with multiplicity 2, which still counts as 2 roots.

For polynomials with real coefficients, complex roots always come in **conjugate pairs**: if a + bi is a root, so is a - bi. This is because the coefficients are real, so taking the complex conjugate of the equation p(r) = 0 gives p(r̄) = 0. Practically: a degree-4 real polynomial with roots 2 and 3 + i must also have root 3 - i, accounting for 3 of its 4 roots. The fourth root must be real (since complex roots come in pairs). Similarly, a real polynomial of odd degree must have at least one real root — complex non-real roots pair up, and a single root is left over that must be real.

Think of the theorem as a completeness certificate. The real numbers are not **algebraically closed** — they leave x² + 1 = 0 unsolved. The complex numbers are algebraically closed: you never need to invent a new number system to solve polynomial equations. This is why complex numbers are not just useful in algebra, but central to it. In practice, the theorem guides every polynomial factoring problem: know the degree, know the exact count of roots, apply the conjugate pairs rule to constrain which roots are real.
