---
id: lhopitals-rule
title: "L'Hopital's Rule"
domain: mathematics
course: calculus-1
prerequisites:
  - id: limits-at-infinity
    type: hard
  - id: derivatives-of-trigonometric-functions
    type: soft
  - id: derivatives-of-exponential-functions
    type: soft
builds-toward:
  - improper-integrals-convergence
  - taylor-series
tags: [limits, indeterminate-forms, lhopital]
stage: formal-systems
status: draft
---

# L'Hopital's Rule

## Core Idea
L'Hopital's Rule states that if lim f(x)/g(x) produces an indeterminate form 0/0 or infinity/infinity, then the limit equals lim f'(x)/g'(x), provided this latter limit exists. The rule can be applied repeatedly for persistent indeterminate forms. Other indeterminate forms (0 * infinity, infinity - infinity, 0^0, 1^infinity, infinity^0) can be converted to 0/0 or infinity/infinity form first.

## How It's Best Learned
Verify indeterminate form before applying. Practice with 0/0 and infinity/infinity cases. Then learn to convert other indeterminate forms. Compare with algebraic techniques (factoring, rationalizing) which sometimes work better. Emphasize that L'Hopital's Rule applies to f'/g', not (f/g)'.

## Common Misconceptions
- Applying L'Hopital's Rule when the form is not indeterminate (e.g., 1/0 is not indeterminate).
- Using the quotient rule instead of differentiating numerator and denominator separately.
- Applying the rule in a circular loop without recognizing the limit can be computed directly.
