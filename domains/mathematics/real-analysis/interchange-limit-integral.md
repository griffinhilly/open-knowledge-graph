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
- id: interchange-limit-derivative
  type: soft
- id: pointwise-convergence-function-sequences
  type: soft
- id: uniform-convergence
  type: hard
tags:
- limit-integral
- interchange
- uniform-convergence
stage: advanced
status: validated
---
# Interchange of Limit and Integral

## Core Idea
If (fₙ) converges uniformly to f on [a,b] and each fₙ is integrable, then lim ∫fₙ = ∫ lim fₙ. This allows passing limits through integral signs, essential for analyzing series of integrals and probability distributions. The result follows from uniform convergence preserving continuity and properties of the integral.

## Questions

```yaml
- question: "Consider a sequence of functions fₙ on [0,1] where fₙ = n on [0, 1/n] and fₙ = 0 elsewhere. Each fₙ converges pointwise to f = 0. What is lim(n→∞) ∫₀¹ fₙ dx?"
  type: multiple-choice
  options:
    - "0, because fₙ → 0 pointwise and the limit of a continuous function is integrable"
    - "1, because each ∫fₙ = 1 regardless of the pointwise limit"
    - "∞, because the spikes grow without bound"
    - "Undefined, because the integral does not exist for each fₙ"
  answer: 1
  explanation: "Each fₙ has integral exactly 1 (height n times width 1/n). Yet fₙ(x) → 0 for every fixed x in [0,1], because for any x > 0, fₙ(x) = 0 once n > 1/x. So ∫f = ∫0 = 0, but lim ∫fₙ = 1 ≠ 0 = ∫ lim fₙ. This is the canonical counterexample: pointwise convergence allows the integral mass to 'escape' into a shrinking spike, so the interchange fails. Uniform convergence would prevent this by requiring the error to shrink simultaneously everywhere."

- question: "Under which condition is it guaranteed that lim(n→∞) ∫ₐᵇ fₙ dx = ∫ₐᵇ (lim fₙ) dx on a bounded interval [a,b]?"
  type: multiple-choice
  options:
    - "Each fₙ is continuous and the sequence is monotone increasing"
    - "fₙ converges pointwise to f and each fₙ is bounded by the same constant M"
    - "fₙ converges uniformly to f on [a,b] and each fₙ is integrable"
    - "The sequence is Cauchy in the sup-norm at every rational point of [a,b]"
  answer: 2
  explanation: "Uniform convergence on [a,b] is the key hypothesis in the classical interchange theorem. It allows a single ε to work for all x simultaneously, so |∫fₙ − ∫f| ≤ ∫|fₙ − f| ≤ ε·(b−a). Option A (monotone) is the hypothesis for the Monotone Convergence Theorem, which applies to Lebesgue integrals in a different setting. Option B (uniform bound) is the hypothesis for the Dominated Convergence Theorem, not the classical Riemann-based result. Option D has a real-analysis flavor but is not a standard sufficient condition."

- question: "If (fₙ) converges uniformly to f on [a,b] and each fₙ is Riemann integrable, then lim ∫ₐᵇ fₙ dx = ∫ₐᵇ f dx."
  type: true-false
  answer: true
  explanation: "True. This is the uniform convergence interchange theorem. The proof is direct: |∫fₙ − ∫f| = |∫(fₙ − f)| ≤ ∫|fₙ − f| ≤ sup_x|fₙ(x) − f(x)| · (b−a). Since fₙ → f uniformly, the sup-norm goes to 0, so the difference between the integrals goes to 0. Note that uniform convergence also implies f is integrable (as a uniform limit of integrable functions on a bounded interval is itself integrable)."

- question: "Pointwise convergence of (fₙ) to f on [a,b] is sufficient to conclude that lim ∫ₐᵇ fₙ dx = ∫ₐᵇ f dx."
  type: true-false
  answer: false
  explanation: "False. The 'spike' counterexample (fₙ = n on [0,1/n], 0 elsewhere) shows pointwise convergence is not enough: fₙ → 0 pointwise everywhere, yet each integral equals 1. With pointwise convergence, the error |fₙ(x) − f(x)| need not shrink simultaneously across all x — it can concentrate in ever-smaller sets that still contribute finite area. Uniform convergence prevents this by requiring the error to be controlled everywhere at once."

- question: "Explain in your own words why uniform convergence is the 'right' condition for interchanging limit and integral, when pointwise convergence is not."
  type: short-answer
  answer: "With pointwise convergence, the error |fₙ(x) − f(x)| can be small at each individual x but large somewhere on the interval — 'moving' the mass around as n grows. This lets the integral of fₙ differ from the integral of f. Uniform convergence requires the error to be small everywhere simultaneously: once n is large enough, |fₙ(x) − f(x)| < ε for all x at once. Then the integral error is at most ε times the interval length, which can be made arbitrarily small."
  explanation: "The intuition is that integration is a global operation — it sums contributions from the whole interval. Pointwise convergence only gives local control (at each fixed point), which is too weak to control the global sum. Uniform convergence gives the global control needed. In more advanced analysis, the Dominated Convergence Theorem gives a weaker condition (domination by an integrable function) that covers more cases while still maintaining enough global control."
```

## Explainer

You know from your work on uniform convergence that pointwise convergence is not enough to preserve analytic structure — a sequence of functions can converge pointwise to a limit while their integrals diverge, or converge to the wrong value. The classic counterexample is a sequence of "spike" functions that each integrate to 1 but converge pointwise to the zero function, whose integral is 0. The problem is that with pointwise convergence, the spikes can move around and concentrate mass in arbitrarily small intervals while remaining bounded pointwise. This is why **uniform convergence** is the right hypothesis for interchange theorems.

Uniform convergence means that the error |fₙ(x) − f(x)| can be made smaller than any ε for all x simultaneously, not just at each fixed x. Once you have that, you can bound the difference between the two integrals directly: |∫fₙ − ∫f| = |∫(fₙ − f)| ≤ ∫|fₙ − f| ≤ ε·(b−a). Since b−a is a fixed constant and ε is arbitrary, the difference can be made as small as desired. The uniform bound over the whole interval is what makes the estimate work — the error in the integral is controlled by the sup-norm error multiplied by the length of the interval.

This theorem has immediate practical consequences. When you integrate a convergent power series term by term — writing ∫∑aₙxⁿ = ∑∫aₙxⁿ — you are swapping a limit (the series is a limit of partial sums) and an integral. The justification is exactly this theorem: power series converge uniformly on closed subintervals of their radius of convergence, so the interchange is valid there. Similarly, when a sequence of continuous functions converges uniformly, the limit is continuous, and you can exchange limit and integral freely.

The broader lesson is that mathematical operations — limits, integrals, derivatives, sums — do not automatically commute. Each interchange theorem states a precise condition under which the order can be reversed. Uniform convergence is the most useful such condition in real analysis. Later, in measure theory, the Dominated Convergence Theorem gives a weaker hypothesis (domination by an integrable function instead of uniform convergence) that covers many more cases, but the idea is the same: you need a condition that prevents mass from escaping to infinity or concentrating in shrinking sets.
