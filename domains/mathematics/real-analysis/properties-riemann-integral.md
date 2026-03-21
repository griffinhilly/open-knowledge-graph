---
id: properties-riemann-integral
title: Properties of the Riemann Integral
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-integrability-criteria
  type: hard
builds-toward:
- fundamental-theorem-calculus-rigorous
- improper-integrals-rigorous
tags:
- riemann-integral
- properties
- linearity
stage: advanced
status: draft
---

# Properties of the Riemann Integral

## Core Idea
The Riemann integral satisfies linearity (∫(af+bg) = a∫f + b∫g), order properties (if f ≤ g then ∫f ≤ ∫g), additivity over intervals (∫[a,c] = ∫[a,b] + ∫[b,c]), and bounds (|∫f| ≤ ∫|f|). These properties make the integral a powerful tool for analysis and follow naturally from the definition via Darboux sums.

## Questions

```yaml
- question: "You want to show that |∫[0,1] sin(x²) dx| ≤ 1. Which property of the Riemann integral justifies the key step?"
  type: multiple-choice
  options:
    - "Linearity: ∫(af + bg) = a∫f + b∫g"
    - "Additivity: ∫[0,1] = ∫[0,c] + ∫[c,1] for any c ∈ (0,1)"
    - "Triangle inequality: |∫f| ≤ ∫|f|"
    - "Monotonicity: f ≤ g implies ∫f ≤ ∫g"
  answer: 2
  explanation: "The triangle inequality for integrals, |∫[a,b] f| ≤ ∫[a,b] |f|, is precisely the tool for bounding the absolute value of an integral. Here |∫[0,1] sin(x²) dx| ≤ ∫[0,1] |sin(x²)| dx ≤ ∫[0,1] 1 dx = 1. Monotonicity alone (option D) wouldn't let you move the absolute value inside the integral — it compares two integrals of different functions, not an absolute value of an integral to an integral of an absolute value."

- question: "A function f has a single jump discontinuity at x = c ∈ (a, b) but is otherwise continuous and bounded. You want to integrate f over [a, b]. Which property is most directly useful?"
  type: multiple-choice
  options:
    - "Linearity, because f can be written as a sum of simpler functions"
    - "Monotonicity, because f is bounded above by a continuous function"
    - "Additivity over subintervals: ∫[a,b] f = ∫[a,c] f + ∫[c,b] f"
    - "The triangle inequality, to handle the absolute value at the discontinuity"
  answer: 2
  explanation: "Additivity over subintervals lets you split [a,b] at the discontinuity, dealing with [a,c] and [c,b] separately — on each subinterval f is continuous and therefore Riemann integrable. This is the standard strategy for handling isolated discontinuities: isolate them at endpoints of subintervals, where integrability is unaffected. Linearity (option A) applies to sums of functions, not to splitting domains."

- question: "If f and g are Riemann integrable on [a, b] and f(x) ≤ g(x) for all x ∈ [a, b], then ∫[a,b] f ≤ ∫[a,b] g."
  type: true-false
  answer: true
  explanation: "This is the monotonicity (order) property of the Riemann integral. It follows directly from the Darboux sum definition: if f(x) ≤ g(x) everywhere, then for any partition, every lower Darboux sum of f is ≤ the corresponding lower sum of g, and similarly for upper sums. Taking the limit gives ∫f ≤ ∫g. This property is used constantly to bound integrals by replacing a complicated integrand with a simpler upper bound."

- question: "For any Riemann integrable function f on [a, b], the equality |∫[a,b] f| = ∫[a,b] |f| holds."
  type: true-false
  answer: false
  explanation: "This confuses the triangle inequality with an equality. The correct statement is |∫[a,b] f| ≤ ∫[a,b] |f|, which is an inequality, not generally an equality. Equality holds only when f does not change sign on [a, b] — for instance, if f ≥ 0 everywhere, then |∫f| = ∫f = ∫|f|. But if f takes both positive and negative values, the integral ∫f involves cancellation, making it strictly smaller in absolute value than ∫|f|. For example, ∫[0, 2π] sin(x) dx = 0, but ∫[0, 2π] |sin(x)| dx = 4."

- question: "Why does the linearity property ∫(af + bg) = a∫f + b∫g hold for Riemann integrals, and why is it useful?"
  type: short-answer
  answer: "Linearity holds because the Riemann integral is a limit of Darboux sums, and sums are linear: the sum of af(xᵢ)Δxᵢ + bg(xᵢ)Δxᵢ equals a·(sum of f terms) + b·(sum of g terms). This additivity over summands carries through to the limit. It is useful because it lets you break a complicated integrand into simpler pieces — integrating each separately and combining results — without returning to the definition each time."
  explanation: "The key is that the integral inherits linearity from summation, since it is defined as a limit of sums. This is why polynomial integrals can be done term-by-term, why scaling a function scales its integral, and why subtraction of integrals corresponds to the integral of a difference. Linearity is the algebraic backbone that makes the Fundamental Theorem of Calculus and most integration techniques possible."
```

## Explainer

From your study of Riemann integrability criteria, you know that a bounded function f on [a, b] is Riemann integrable when the gap between its upper and lower Darboux sums can be made arbitrarily small. That definition gives you the integral's existence conditions. What you build on top of it are the **properties** — algebraic and order-theoretic rules that let you compute and bound integrals without returning to the Darboux sum definition every time.

**Linearity** is the most frequently used property: ∫(af + bg) = a∫f + b∫g for real constants a, b and integrable functions f, g. This mirrors the linearity of summation — the integral is essentially a limit of sums, so it inherits sum's additive and scalar behavior. The proof follows by controlling the Darboux sums for af + bg in terms of those for f and g separately. Linearity is what allows you to integrate polynomial terms one at a time, or to split an integral of a sum into a sum of integrals.

**Monotonicity** says: if f(x) ≤ g(x) for all x in [a, b], then ∫f ≤ ∫g. Geometrically, if one function lies below another, its area is smaller. The proof is immediate: the lower Darboux sums for f are bounded above by those for g on any partition. A closely related result is the **triangle inequality for integrals**: |∫f| ≤ ∫|f|. This is the continuous analogue of |Σaᵢ| ≤ Σ|aᵢ|. It is used throughout analysis to bound error terms — you replace an absolute value of an integral with an integral of an absolute value, which is easier to estimate.

**Additivity over subintervals** states that if c ∈ [a, b], then ∫[a,b] f = ∫[a,c] f + ∫[b,c] f. This lets you split a complicated domain into manageable pieces, handle discontinuities by isolating them in a small sub-interval, and build up results about improper integrals by passing to limits. Combined with linearity, these properties form the algebraic backbone that makes the Fundamental Theorem of Calculus both meaningful and provable: when you differentiate ∫[a,x] f(t) dt with respect to x, it is the additivity property that allows you to isolate the increment [x, x+h] and let h → 0.
