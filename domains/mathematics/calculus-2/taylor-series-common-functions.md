---
id: taylor-series-common-functions
title: Taylor Series for Common Functions
domain: mathematics
course: calculus-2
prerequisites:
  - id: maclaurin-series
    type: hard
builds-toward: []
tags: [series, Taylor, reference, common-functions]
stage: formal-systems
status: draft
---

# Taylor Series for Common Functions

## Core Idea
The essential Taylor/Maclaurin series to know are: e^x = sum x^n/n! (all x), sin(x) = sum (-1)^n x^(2n+1)/(2n+1)! (all x), cos(x) = sum (-1)^n x^(2n)/(2n)! (all x), 1/(1-x) = sum x^n (|x| < 1), ln(1+x) = sum (-1)^(n+1) x^n/n (|x| <= 1, x not equal to -1), arctan(x) = sum (-1)^n x^(2n+1)/(2n+1) (|x| <= 1), and (1+x)^k = sum C(k,n) x^n (binomial series, |x| < 1). These serve as building blocks for constructing series of more complex functions.

## How It's Best Learned
Memorize these series and their intervals of convergence. Practice generating new series by substitution (e.g., e^(-x^2)), multiplication, differentiation (e.g., 1/(1-x)^2 from 1/(1-x)), and integration (e.g., ln(1+x) from 1/(1+x)). Use these to evaluate limits, compute integrals without closed forms, and approximate values.

## Common Misconceptions
- Mixing up which series have alternating signs and which do not.
- Forgetting whether a series uses all powers of x or only odd/even powers.
- Not adjusting the radius of convergence after substitution.
