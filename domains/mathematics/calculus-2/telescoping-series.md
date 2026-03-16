---
id: telescoping-series
title: Telescoping Series
domain: mathematics
course: calculus-2
prerequisites:
  - id: series-definition-and-partial-sums
    type: hard
  - id: partial-fractions
    type: hard
builds-toward:
  - convergence-test-strategy
tags: [series, telescoping, partial-sums]
stage: formal-systems
status: validated
---

# Telescoping Series

## Core Idea
A telescoping series is one whose partial sums collapse through cancellation, leaving only a few surviving terms. After partial fraction decomposition, the general term has the form f(n) - f(n+1) (or similar), so when you sum, most terms cancel: S_N = f(1) - f(N+1). Taking the limit as N -> infinity gives the exact sum. Telescoping is one of the few methods that yields exact sums for infinite series.

## How It's Best Learned
Decompose 1/(n(n+1)) by partial fractions, write out several terms of the partial sum, observe the cancellation pattern, and find the sum. Practice recognizing series that telescope after algebraic manipulation. Verify by computing partial sums.

## Common Misconceptions
- Not recognizing when a series telescopes (partial fractions are the key step).
- Making errors tracking which terms survive after cancellation.
- Assuming all series with partial fractions telescope (they do not).

## Explainer

You know from series that the sum of an infinite series is defined as the limit of its **partial sums** S_N = a₁ + a₂ + ... + a_N. For most series, partial sums are hard to write in closed form — we need tests to determine convergence, but we rarely find the actual value. Telescoping series are one of the rare exceptions: their partial sums simplify so dramatically that an exact sum falls out. The key mechanism is massive cancellation driven by the structure of each term.

The standard example is ∑ 1/(n(n+1)). You know from partial fractions that 1/(n(n+1)) = 1/n - 1/(n+1). Now write out the first few terms of the partial sum: S_N = (1/1 - 1/2) + (1/2 - 1/3) + (1/3 - 1/4) + ... + (1/N - 1/(N+1)). Look at what survives: every intermediate fraction appears once with a plus sign and once with a minus sign. The entire middle collapses, leaving S_N = 1 - 1/(N+1). Taking the limit as N → ∞: S = 1. This is the **telescoping** effect — like a collapsing telescope, the interior sections slide into each other and disappear.

The general structure is: if each term aₙ can be written as f(n) - f(n+1) for some function f, then S_N = f(1) - f(N+1). The series converges if and only if f(N+1) → L for some finite limit L as N → ∞, and in that case the sum is f(1) - L. The partial fractions step is not optional — it is usually what reveals the telescoping form. Without decomposing 1/(n(n+1)) into 1/n - 1/(n+1), the cancellation is invisible.

To apply this reliably, write out the N-th partial sum explicitly — do not try to track the cancellation in your head. Write S_N = term₁ + term₂ + term₃ + ... + term_N after substituting the partial fraction form, and physically cross out matching terms. What is left is your closed-form for S_N. This careful bookkeeping also tells you which terms survive at each end: sometimes it is the first two that survive, sometimes just the first one, depending on the shift in the formula. Recognizing when a series can telescope — and having the partial fractions skill to expose that structure — makes you one of the few students who can find exact infinite sums on demand.
