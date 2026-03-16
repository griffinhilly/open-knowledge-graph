---
id: riemann-lebesgue-comparison
title: Comparison of Riemann and Lebesgue Integrals
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral
  type: hard
- id: riemann-integral-via-darboux-sums
  type: hard
tags:
- integration
stage: advanced
status: draft
---

# Comparison of Riemann and Lebesgue Integrals

## Core Idea
A bounded function on a finite interval is Riemann-integrable if and only if its discontinuity set has measure zero. The Lebesgue integral extends Riemann integration to unbounded functions and domains while preserving equality on Riemann-integrable functions.

## Explainer

You now have both integrals in hand: the Riemann integral, defined through Darboux sums that partition the x-axis into subintervals, and the Lebesgue integral, defined through simple function approximation and measure. The natural question is how they relate. The answer is precise: on a closed bounded interval [a, b], a bounded function f is Riemann-integrable if and only if its set of discontinuities has **Lebesgue measure zero**. A set has measure zero if it can be covered by open intervals of arbitrarily small total length — single points, finite collections of points, and even countable collections like the rationals all have measure zero.

This characterization — the **Lebesgue criterion for Riemann integrability** — explains at once why continuous functions are Riemann-integrable (no discontinuities), why monotone functions are Riemann-integrable (only countably many jump discontinuities, a measure-zero set), and why the Dirichlet function f(x) = 1 for x rational, 0 for x irrational is *not* Riemann-integrable (discontinuous everywhere, a full-measure set). The Lebesgue integral handles the Dirichlet function easily: its value on the rationals doesn't matter because the rationals have measure zero, so ∫f dλ = 0.

When a function is Riemann-integrable, both integrals agree exactly: (R)∫_a^b f dx = (L)∫_a^b f dλ. The Lebesgue integral is thus a strict generalization — it integrates everything Riemann can, plus much more. The expansion comes in two directions. First, Lebesgue handles functions with large discontinuity sets that Riemann cannot, like the Dirichlet function above. Second, Lebesgue handles improper integrals more cleanly: rather than taking limits of Riemann integrals over expanding intervals, you simply integrate over all of ℝ directly, provided the positive and negative parts are separately finite.

The practical significance is in the **convergence theorems**. The Riemann integral has weak pointwise convergence results — even uniformly converging sequences of Riemann-integrable functions only guarantee exchanging limit and integral under restrictive conditions. The Lebesgue integral comes equipped with the Dominated Convergence Theorem and the Monotone Convergence Theorem, which allow limit-integral interchange under much weaker hypotheses. This is why modern analysis, probability theory, and functional analysis all use Lebesgue integration as the default: it is not just a generalization but a framework with far more powerful tools for working with limiting processes.
