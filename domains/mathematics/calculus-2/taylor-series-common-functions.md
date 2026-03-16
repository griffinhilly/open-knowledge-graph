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
status: validated
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

## Explainer

You have learned how to construct a Maclaurin series by repeatedly differentiating a function and evaluating at zero. The standard series in this topic are the outputs of that process applied to the most important functions. Think of this list not as facts to memorize in isolation, but as a toolkit: once you have e^x, sin(x), cos(x), and 1/(1−x) committed to memory, you can derive dozens of other series without recomputing from scratch. The power comes from three manipulation techniques — **substitution**, **differentiation**, and **integration** — applied to series you already know.

Substitution is the fastest technique. To find the series for e^{−x²}, replace x with −x² in the series for e^x: e^{−x²} = Σ(−x²)^n/n! = Σ(−1)^n x^{2n}/n!. To find the series for cos(x²), substitute x² into the cosine series. The critical caution: the radius of convergence changes under substitution. The geometric series 1/(1−x) = Σx^n converges for |x| < 1. Substituting x² gives 1/(1−x²) = Σx^{2n}, valid for |x²| < 1, i.e., |x| < 1 — same condition here, but if you had substituted 2x you would get convergence for |2x| < 1, meaning |x| < 1/2. Always re-derive the convergence condition after substitution.

Differentiation and integration extend the toolkit further. Differentiating 1/(1−x) = Σx^n term by term gives 1/(1−x)² = Σnx^{n−1}. Integrating 1/(1−x) gives −ln(1−x) = Σx^{n+1}/(n+1), which rearranges to the series for ln(1+x) after substituting −x. The series for arctan(x) comes from integrating 1/(1+x²) = Σ(−1)^n x^{2n} term by term: arctan(x) = Σ(−1)^n x^{2n+1}/(2n+1). Notice that the known series for 1/(1−x) is the seed from which several other standard series grow.

The series also have a structural logic worth noticing. The series for e^x uses all non-negative powers with no sign changes and denominators n!. The sine series uses only odd powers with alternating signs; the cosine series uses only even powers with alternating signs. This reflects the fact that sin is odd and cos is even — odd functions have only odd-power terms, even functions have only even-power terms. The alternating signs come from the pattern of derivatives: sin, cos, −sin, −cos, sin, ... so every four steps the sign pattern repeats. Seeing the structural reason for each feature helps you reconstruct series quickly if you forget a detail, rather than relying purely on memorization.
