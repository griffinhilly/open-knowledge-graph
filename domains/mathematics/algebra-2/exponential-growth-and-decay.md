---
id: exponential-growth-and-decay
title: Exponential Growth and Decay
domain: mathematics
course: algebra-2
prerequisites:
  - id: exponential-functions-and-graphs
    type: hard
builds-toward:
  - solving-exponential-equations
  - natural-logarithm-and-e
tags: [exponential, growth, decay, applications, half-life, doubling-time]
stage: abstract-reasoning
status: validated
---

# Exponential Growth and Decay

## Core Idea
Exponential growth and decay model situations where a quantity changes by a constant percentage per unit time. The general model is A(t) = A_0 * (1 + r)^t for growth (r > 0) or A(t) = A_0 * (1 - r)^t for decay (0 < r < 1). For continuous compounding: A(t) = A_0 * e^(kt). Key concepts include doubling time, half-life, and the distinction between rate and growth factor. Applications span finance, biology, physics, and pharmacology.

## How It's Best Learned
Start with concrete examples: compound interest, population growth, radioactive decay. Practice writing models from word problems (identify A_0, r, and t). Compute future values and solve for time (requiring logarithms, previewing the next unit). Distinguish between growth rate (percentage) and growth factor (1 + rate).

## Common Misconceptions
- Confusing growth rate r with growth factor (1 + r).
- Using linear models for exponential situations (adding instead of multiplying).
- Thinking half-life means the quantity reaches zero after two half-lives.
- Not converting percentage rates to decimal form before using the formula.

## Questions

```yaml
- question: "A population of bacteria doubles every 3 hours. Starting with 500 bacteria, which expression gives the population after t hours?"
  type: multiple-choice
  options:
    - "500 + 2t"
    - "500 · 2^t"
    - "500 · 2^(t/3)"
    - "500 · (2/3)^t"
  answer: 2
  explanation: "Every 3 hours, the population doubles — so after t hours it has doubled t/3 times. The base is 2 (the growth factor), and the exponent is t/3. Option A is a linear model (adding instead of multiplying). Option B would double every 1 hour, not every 3. Option D uses 2/3 as a decay factor, which would produce decreasing values."

- question: "After two half-lives have passed, a radioactive substance has completely decayed to zero."
  type: true-false
  answer: false
  explanation: "After each half-life, half of the *remaining* substance decays — not half of the original. After one half-life: 50% remains. After two: 25% remains. After three: 12.5%. The quantity follows A(t) = A_0 · (1/2)^(t/h) and approaches zero asymptotically but never reaches it."

- question: "A savings account earns 6% annual interest compounded annually. Explain the difference between the growth rate and the growth factor in this context, and identify each."
  type: short-answer
  answer: "The growth rate is 6% (or 0.06 as a decimal) — the percentage increase per period. The growth factor is 1.06 — the number you multiply by each year to get the new balance. Growth factor = 1 + growth rate."
  explanation: "Confusing rate and factor is a persistent error. The rate describes how much is added; the factor describes the multiplier. In A(t) = A_0 · (1 + r)^t, the r is the rate (0.06) and (1 + r) = 1.06 is the factor. Using r = 6 instead of 0.06 is a classic mistake that produces wildly wrong answers."
```

## Explainer

Exponential growth and decay arise whenever a quantity changes by a *constant proportion* per unit time rather than a constant amount. The distinction is subtle but important: a population that grows by 100 individuals per year is growing linearly; a population that grows by 10% per year is growing exponentially. The percentage rule means the absolute number of new individuals keeps increasing as the population gets larger, which is why exponential growth accelerates so dramatically over time.

The standard model is A(t) = A₀ · (1 + r)^t, where A₀ is the initial amount, r is the growth rate per period (as a decimal), and t is the number of periods. For decay, r is negative — or equivalently, you write A(t) = A₀ · (1 − r)^t with r > 0 representing the fraction lost each period. The base (1 + r) is called the growth factor: it is the multiplier applied each period. A growth factor greater than 1 means growth; less than 1 means decay. Notice that the growth factor and the growth rate carry different information — 6% annual interest means rate = 0.06 and factor = 1.06.

Half-life and doubling time are the most intuitive measures of how fast a quantity changes. The doubling time is the period required for a quantity to double; the half-life is the period required for it to halve. Both are constant for a given exponential model, which is what makes them so useful: a radioactive isotope with a 5-hour half-life will always lose half its remaining mass every 5 hours, regardless of how much is left. This constancy is what distinguishes exponential decay from linear decay (where a constant *amount* is lost each period until the quantity reaches zero).

A common misconception is that after two half-lives, a substance reaches zero. It does not. After one half-life, half the original amount remains. After the second, half of *that* remains — one quarter of the original. The quantity follows A(t) = A₀ · (1/2)^(t/h) where h is the half-life, an equation that approaches zero asymptotically but never touches it. The same structure appears in drug pharmacology, carbon-14 dating, and the discharge of capacitors.

For problems involving continuous processes — continuously compounded interest, continuous population growth — the natural base e arises: A(t) = A₀ · e^(kt). Here k is the continuous growth rate, which is related to but not equal to the per-period rate r. You will explore this connection when you study the natural logarithm and Euler's number e in the next unit; for now, it is enough to recognize that e^(kt) is the continuous analog of (1 + r)^t.
