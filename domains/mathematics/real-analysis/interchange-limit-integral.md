---
id: interchange-limit-integral
title: Interchange of Limit and Integral
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-convergence-preserves-continuity
  type: hard
- id: riemann-integral-properties
  type: hard
tags:
- limit-integral
- interchange
- uniform-convergence
stage: advanced
status: draft
---

# Interchange of Limit and Integral

## Core Idea
If (fₙ) converges uniformly to f on [a,b] and each fₙ is integrable, then lim ∫fₙ = ∫ lim fₙ. This allows passing limits through integral signs, essential for analyzing series of integrals and probability distributions. The result follows from uniform convergence preserving continuity and properties of the integral.

## Explainer

You know from your work on uniform convergence that pointwise convergence is not enough to preserve analytic structure — a sequence of functions can converge pointwise to a limit while their integrals diverge, or converge to the wrong value. The classic counterexample is a sequence of "spike" functions that each integrate to 1 but converge pointwise to the zero function, whose integral is 0. The problem is that with pointwise convergence, the spikes can move around and concentrate mass in arbitrarily small intervals while remaining bounded pointwise. This is why **uniform convergence** is the right hypothesis for interchange theorems.

Uniform convergence means that the error |fₙ(x) − f(x)| can be made smaller than any ε for all x simultaneously, not just at each fixed x. Once you have that, you can bound the difference between the two integrals directly: |∫fₙ − ∫f| = |∫(fₙ − f)| ≤ ∫|fₙ − f| ≤ ε·(b−a). Since b−a is a fixed constant and ε is arbitrary, the difference can be made as small as desired. The uniform bound over the whole interval is what makes the estimate work — the error in the integral is controlled by the sup-norm error multiplied by the length of the interval.

This theorem has immediate practical consequences. When you integrate a convergent power series term by term — writing ∫∑aₙxⁿ = ∑∫aₙxⁿ — you are swapping a limit (the series is a limit of partial sums) and an integral. The justification is exactly this theorem: power series converge uniformly on closed subintervals of their radius of convergence, so the interchange is valid there. Similarly, when a sequence of continuous functions converges uniformly, the limit is continuous, and you can exchange limit and integral freely.

The broader lesson is that mathematical operations — limits, integrals, derivatives, sums — do not automatically commute. Each interchange theorem states a precise condition under which the order can be reversed. Uniform convergence is the most useful such condition in real analysis. Later, in measure theory, the Dominated Convergence Theorem gives a weaker hypothesis (domination by an integrable function instead of uniform convergence) that covers many more cases, but the idea is the same: you need a condition that prevents mass from escaping to infinity or concentrating in shrinking sets.
