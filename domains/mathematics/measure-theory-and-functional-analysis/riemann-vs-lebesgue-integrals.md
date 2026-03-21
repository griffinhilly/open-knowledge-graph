---
id: riemann-vs-lebesgue-integrals
title: 'Comparison: Riemann and Lebesgue Integrals'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: riemann-integral-darboux-sums
  type: hard
- id: lebesgue-integral-general-definition
  type: hard
builds-toward:
- dominated-convergence-theorem
tags:
- integration
stage: advanced
status: draft
---

# Comparison: Riemann and Lebesgue Integrals

## Core Idea
If a bounded function on [a,b] is Riemann integrable, it is Lebesgue integrable with equal integrals. The Lebesgue integral applies to a much broader class of functions and has superior convergence theorems (e.g., dominated convergence).

## How It's Best Learned
Show that Dirichlet's function (1 on rationals, 0 on irrationals) is Lebesgue integrable but not Riemann integrable. Understand that Lebesgue slices 'horizontally' while Riemann slices 'vertically.'

## Common Misconceptions
Lebesgue integration is not strictly stronger in existence: every Riemann integrable function is Lebesgue integrable, but the reverse is false. The real advantage is better convergence theorems.

## Questions

```yaml
- question: "Dirichlet's function assigns 1 to every rational number and 0 to every irrational on [0,1]. What is its Lebesgue integral, and why does Riemann integration fail here?"
  type: multiple-choice
  options:
    - "Both integrals equal 1, because there are infinitely many rationals in [0,1]"
    - "The Lebesgue integral equals 0; Riemann fails because every subinterval contains both rationals and irrationals, so upper and lower sums never converge"
    - "Neither integral is defined, since the function has a discontinuity at every point"
    - "Both integrals equal 1/2, because rationals and irrationals are equally dense in [0,1]"
  answer: 1
  explanation: "The rationals have Lebesgue measure zero, so the integral is 1 × 0 + 0 × 1 = 0. Riemann fails because any subinterval [x, x+δ] contains both rationals (where f = 1) and irrationals (where f = 0), forcing the upper Darboux sum to always be 1 and the lower sum to always be 0 — they never converge. Lebesgue sidesteps this by partitioning the range instead of the domain."

- question: "A student argues that the main reason to prefer Lebesgue over Riemann integration is that Lebesgue can integrate Dirichlet-like functions that Riemann cannot. What is the more fundamental advantage?"
  type: multiple-choice
  options:
    - "Lebesgue integration is computationally faster for numerical approximations"
    - "The Lebesgue integral always equals the Riemann integral when both exist, making them interchangeable in practice"
    - "The Lebesgue framework has superior convergence theorems — such as the Dominated Convergence Theorem — that allow limits and integrals to be interchanged under mild conditions"
    - "Lebesgue integration avoids the need to define measure-zero sets"
  answer: 2
  explanation: "Extending the class of integrable functions is a real benefit, but the deeper payoff is convergence. The Dominated Convergence Theorem says that if fₙ → f pointwise a.e. and all fₙ are dominated by an integrable g, then ∫fₙ → ∫f. The Riemann framework offers no analogous general theorem — you can construct sequences of Riemann integrable functions converging to non-Riemann-integrable limits. This interchangeability of limits and integrals is what makes Lebesgue integration indispensable in analysis, probability, and PDEs."

- question: "Every bounded Riemann integrable function on [a,b] is also Lebesgue integrable, and the two integrals are equal."
  type: true-false
  answer: true
  explanation: "This is the precise inclusion relationship: Riemann integrable ⊆ Lebesgue integrable, with equal values. The containment is strict — there exist Lebesgue integrable functions (like Dirichlet's function) that are not Riemann integrable. The key word is 'bounded': for improper Riemann integrals of unbounded functions, the relationship is more nuanced."

- question: "The fundamental difference between Lebesgue and Riemann integration is that Lebesgue is more accurate — it gives more precise values for the same integrals."
  type: true-false
  answer: false
  explanation: "When both integrals exist, they give identical values. The difference is not accuracy but scope and theoretical power. Lebesgue partitions the range rather than the domain, which extends the class of integrable functions and — more importantly — enables the Dominated Convergence Theorem and related results. The advantage is structural: Lebesgue integration is designed so that limits and integrals commute under mild conditions, which is exactly what modern analysis requires."

- question: "Why does Lebesgue's 'horizontal slicing' approach succeed where Riemann's 'vertical slicing' fails for functions like Dirichlet's function?"
  type: short-answer
  answer: "Riemann partitions the domain into subintervals and asks: what values does f take here? For Dirichlet's function, every subinterval contains both rationals (f=1) and irrationals (f=0), so no partition ever produces approximations that converge. Lebesgue instead partitions the range and asks: for each output value, what is the measure of its preimage? The preimage of 1 (the rationals) has measure zero; the preimage of 0 (the irrationals) has measure 1. So the integral is simply 1×0 + 0×1 = 0. Range partitioning sidesteps the domain's complicated structure entirely."
  explanation: "Riemann's approach requires the function to be nearly constant on small subintervals — Dirichlet's function is maximally discontinuous everywhere. Lebesgue's approach bypasses this requirement by working directly with the distribution of output values and their associated measures, making the domain's pathological structure irrelevant."
```

## Explainer

Both the Riemann and Lebesgue integrals are trying to do the same thing — compute the "signed area" under a function's graph. The difference lies in *how* they carve up the problem, and that difference has profound consequences. You already know Riemann integration via Darboux sums: you partition the **domain** [a, b] into subintervals and approximate the integral by summing f(x) × (width of interval). Lebesgue's insight was to partition the **range** instead: divide the y-axis into bands, ask "what is the measure of the set of x-values where f(x) falls in this band?", and sum (band height) × (measure of preimage).

This range-partitioning is powerful because it decouples the behavior of the function from the structure of the domain. Consider **Dirichlet's function**: f(x) = 1 if x is rational, 0 if x is irrational. Riemann integration fails here — every subinterval of [0, 1] contains both rationals and irrationals, so upper and lower Darboux sums never converge. But Lebesgue handles it trivially: the preimage of the value 1 is the rationals (measure zero), and the preimage of the value 0 is the irrationals (measure 1). The integral is 1 × 0 + 0 × 1 = 0.

The **inclusion relationship** is clean but asymmetric: every bounded Riemann integrable function on [a, b] is also Lebesgue integrable, and the two integrals agree. But the Lebesgue integral applies to many functions that are not Riemann integrable — precisely those where the domain has complicated structure that defeats the Darboux partition approach. The reverse fails: a function like the unbounded 1/√x on (0, 1] requires an improper Riemann integral but is directly Lebesgue integrable; however, this is a technicality and not the main point of distinction.

The real payoff of Lebesgue integration is its **convergence theorems**. The Dominated Convergence Theorem, which you'll encounter next, says: if fₙ → f pointwise almost everywhere and all the fₙ are dominated by an integrable function g, then ∫fₙ → ∫f. This result is routinely used in analysis, probability, and PDEs. The Riemann framework offers no analogous general theorem — you can construct sequences of Riemann integrable functions converging to a non-Riemann-integrable limit. Lebesgue integration is designed precisely so that limits and integrals commute under mild conditions, which is why it has become the standard in modern analysis.
