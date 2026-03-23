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
stage: expert
status: validated
---

# Comparison of Riemann and Lebesgue Integrals

## Core Idea
A bounded function on a finite interval is Riemann-integrable if and only if its discontinuity set has measure zero. The Lebesgue integral extends Riemann integration to unbounded functions and domains while preserving equality on Riemann-integrable functions.

## Questions

```yaml
- question: "The Dirichlet function — defined as 1 for rational x and 0 for irrational x on [0,1] — is bounded and defined everywhere on the interval. Why is it not Riemann-integrable?"
  type: multiple-choice
  options:
    - "It oscillates too rapidly for Darboux sums to converge"
    - "Its discontinuity set is the rationals, which have positive Lebesgue measure"
    - "Its discontinuity set is all of [0,1] — it is discontinuous everywhere — which has positive measure"
    - "Bounded functions on finite intervals are always Riemann-integrable"
  answer: 2
  explanation: "The Dirichlet function is discontinuous at every point of [0,1]: every neighborhood of every point contains both rationals and irrationals, so the function cannot be continuous anywhere. Its discontinuity set is therefore all of [0,1], which has Lebesgue measure 1 (not zero). By the Lebesgue criterion, a bounded function on [a,b] is Riemann-integrable if and only if its discontinuities form a measure-zero set — so the Dirichlet function fails this test. Option D is the common false assumption: boundedness alone is not enough for Riemann integrability."

- question: "A student claims: 'The Lebesgue integral is more powerful than the Riemann integral because it gives different, more accurate values for functions that Riemann can handle.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — Lebesgue integrals do assign different values to the same functions"
    - "The real advantage is that Lebesgue handles functions Riemann cannot, and the real power lies in its convergence theorems — when both apply, they give identical values"
    - "The claim is wrong because Riemann integrals are actually more general than Lebesgue integrals"
    - "The claim is right, but only for functions with infinitely many discontinuities"
  answer: 1
  explanation: "On any interval where a function is Riemann-integrable, both integrals agree exactly: (R)∫f dx = (L)∫f dλ. The Lebesgue integral is a strict generalization — it does everything Riemann does, plus more — but it does not revise Riemann's values. The deeper advantage is twofold: it handles a wider class of functions (those with large discontinuity sets), and it comes with far more powerful convergence theorems (Dominated Convergence, Monotone Convergence) that allow limit-integral interchange under much weaker conditions than Riemann integration permits."

- question: "A monotone function on [a,b] may have jump discontinuities, but it is still Riemann-integrable."
  type: true-false
  answer: true
  explanation: "A monotone function can have at most countably many jump discontinuities (since each jump has positive size and the total variation is finite). Any countable set has Lebesgue measure zero. By the Lebesgue criterion for Riemann integrability, a bounded function is Riemann-integrable if and only if its discontinuity set has measure zero — so a monotone function, whose discontinuities form a countable (hence measure-zero) set, is always Riemann-integrable."

- question: "If a function is Lebesgue-integrable on [0,1], then it is also Riemann-integrable on [0,1]."
  type: true-false
  answer: false
  explanation: "The Lebesgue integral strictly extends the Riemann integral — not the other way around. The Dirichlet function is Lebesgue-integrable (its Lebesgue integral equals 0, since the rationals have measure zero) but is not Riemann-integrable. The Lebesgue criterion shows that Riemann integrability requires the discontinuity set to have measure zero, a condition the Dirichlet function fails. Every Riemann-integrable function is Lebesgue-integrable, but not conversely."

- question: "Why does modern probability theory, functional analysis, and measure theory use the Lebesgue integral as the default framework rather than the Riemann integral, even for functions that Riemann could handle?"
  type: short-answer
  answer: "The Lebesgue integral is preferred not primarily because it handles more functions, but because it supports far more powerful convergence theorems. The Dominated Convergence Theorem and the Monotone Convergence Theorem allow one to interchange limits and integrals under conditions much weaker than those Riemann integration requires. Since virtually all advanced analysis involves limit processes — uniform limits of functions, convergence of probability measures, infinite series of functions — these theorems are indispensable. The Riemann integral's convergence results are too restrictive to carry the weight that modern analysis demands."
  explanation: "The key insight is that the Lebesgue integral's practical superiority is not mainly about handling pathological functions like the Dirichlet function — that would rarely matter in applications. The real reason is the convergence theorem package. In probability theory, for instance, taking expectations of limits of random variables requires exactly the kind of limit-integral interchange that the Dominated Convergence Theorem provides. Building this theory on Riemann integration would require imposing uniform convergence conditions everywhere, making it unworkable. Lebesgue integration is the foundation that makes modern analysis tractable."
```

## Explainer

You now have both integrals in hand: the Riemann integral, defined through Darboux sums that partition the x-axis into subintervals, and the Lebesgue integral, defined through simple function approximation and measure. The natural question is how they relate. The answer is precise: on a closed bounded interval [a, b], a bounded function f is Riemann-integrable if and only if its set of discontinuities has **Lebesgue measure zero**. A set has measure zero if it can be covered by open intervals of arbitrarily small total length — single points, finite collections of points, and even countable collections like the rationals all have measure zero.

This characterization — the **Lebesgue criterion for Riemann integrability** — explains at once why continuous functions are Riemann-integrable (no discontinuities), why monotone functions are Riemann-integrable (only countably many jump discontinuities, a measure-zero set), and why the Dirichlet function f(x) = 1 for x rational, 0 for x irrational is *not* Riemann-integrable (discontinuous everywhere, a full-measure set). The Lebesgue integral handles the Dirichlet function easily: its value on the rationals doesn't matter because the rationals have measure zero, so ∫f dλ = 0.

When a function is Riemann-integrable, both integrals agree exactly: (R)∫_a^b f dx = (L)∫_a^b f dλ. The Lebesgue integral is thus a strict generalization — it integrates everything Riemann can, plus much more. The expansion comes in two directions. First, Lebesgue handles functions with large discontinuity sets that Riemann cannot, like the Dirichlet function above. Second, Lebesgue handles improper integrals more cleanly: rather than taking limits of Riemann integrals over expanding intervals, you simply integrate over all of ℝ directly, provided the positive and negative parts are separately finite.

The practical significance is in the **convergence theorems**. The Riemann integral has weak pointwise convergence results — even uniformly converging sequences of Riemann-integrable functions only guarantee exchanging limit and integral under restrictive conditions. The Lebesgue integral comes equipped with the Dominated Convergence Theorem and the Monotone Convergence Theorem, which allow limit-integral interchange under much weaker hypotheses. This is why modern analysis, probability theory, and functional analysis all use Lebesgue integration as the default: it is not just a generalization but a framework with far more powerful tools for working with limiting processes.
