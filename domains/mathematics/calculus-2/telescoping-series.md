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

## Questions

```yaml
- question: "What is the sum of the infinite series ∑ 1/(n(n+1)) from n=1 to ∞?"
  type: multiple-choice
  options:
    - "1/2 — only the first term survives after cancellation"
    - "1 — the partial sum S_N = 1 - 1/(N+1), which approaches 1"
    - "The series diverges — partial fractions do not produce convergence"
    - "2 — the first and last terms both survive and each contributes 1"
  answer: 1
  explanation: "After decomposing 1/(n(n+1)) = 1/n - 1/(n+1), the partial sum collapses to S_N = 1 - 1/(N+1). As N → ∞, 1/(N+1) → 0, leaving the exact sum of 1. Option A is a common error from assuming only one term survives; in this case S_N simplifies cleanly to 1."

- question: "A series has general term aₙ = 1/n - 1/(n+2). After writing out the partial sum S_N, which terms survive the telescoping cancellation?"
  type: multiple-choice
  options:
    - "Only 1/1, the very first term"
    - "1/1 and 1/2 from the start, minus 1/(N+1) and 1/(N+2) from the end"
    - "Every other term — the odd-indexed ones survive"
    - "Only the final term 1/(N+2)"
  answer: 1
  explanation: "Writing out S_N = (1/1 - 1/3) + (1/2 - 1/4) + (1/3 - 1/5) + ... reveals that 1/3 is added and subtracted, as is 1/4, 1/5, and so on. Two terms survive at the beginning (1/1 and 1/2) and two at the end (−1/(N+1) and −1/(N+2)). The shift by 2, not 1, means two pairs remain. Always write out the partial sum explicitly rather than guessing which terms survive."

- question: "For any telescoping series where aₙ = f(n) − f(n+1), the sum equals f(1) − lim_{N→∞} f(N+1), provided that limit is finite."
  type: true-false
  answer: true
  explanation: "The N-th partial sum is S_N = [f(1)−f(2)] + [f(2)−f(3)] + ... + [f(N)−f(N+1)] = f(1) − f(N+1). The infinite sum is the limit of S_N as N → ∞, which equals f(1) − L whenever f(N+1) → L. This formula is the central result of the telescoping method."

- question: "Any series whose terms can be decomposed by partial fractions is a telescoping series."
  type: true-false
  answer: false
  explanation: "Partial fractions is a technique for rewriting terms, but the result is a telescoping series only if the decomposition produces a form like f(n) − f(n+1) so that adjacent terms cancel. For example, 1/((n+1)(n+3)) decomposes into (1/2)(1/(n+1) − 1/(n+3)), which does telescope (with a shift of 2). But not every partial fraction decomposition aligns terms to cancel — it depends entirely on the structure of the shift in the denominator."

- question: "Why is writing out the partial sum S_N term-by-term essential to evaluating a telescoping series, rather than just recognizing 'it telescopes' and applying the formula directly?"
  type: short-answer
  answer: "Writing out S_N explicitly reveals exactly which terms survive at each end of the sum. The number of surviving terms depends on the shift in the formula (a shift of 1 leaves one term at each end; a shift of 2 leaves two). Skipping this step leads to errors in identifying the boundary terms. The written-out sum also confirms the cancellation pattern and catches sign errors in the partial fraction decomposition."
  explanation: "Students who try to apply the formula mechanically without writing out terms often misidentify the surviving endpoint terms, especially when the telescoping involves a shift greater than 1. The physical act of writing the sum and crossing out matching pairs is not a shortcut to skip — it is the derivation itself."
```

## Explainer

You know from series that the sum of an infinite series is defined as the limit of its **partial sums** S_N = a₁ + a₂ + ... + a_N. For most series, partial sums are hard to write in closed form — we need tests to determine convergence, but we rarely find the actual value. Telescoping series are one of the rare exceptions: their partial sums simplify so dramatically that an exact sum falls out. The key mechanism is massive cancellation driven by the structure of each term.

The standard example is ∑ 1/(n(n+1)). You know from partial fractions that 1/(n(n+1)) = 1/n - 1/(n+1). Now write out the first few terms of the partial sum: S_N = (1/1 - 1/2) + (1/2 - 1/3) + (1/3 - 1/4) + ... + (1/N - 1/(N+1)). Look at what survives: every intermediate fraction appears once with a plus sign and once with a minus sign. The entire middle collapses, leaving S_N = 1 - 1/(N+1). Taking the limit as N → ∞: S = 1. This is the **telescoping** effect — like a collapsing telescope, the interior sections slide into each other and disappear.

The general structure is: if each term aₙ can be written as f(n) - f(n+1) for some function f, then S_N = f(1) - f(N+1). The series converges if and only if f(N+1) → L for some finite limit L as N → ∞, and in that case the sum is f(1) - L. The partial fractions step is not optional — it is usually what reveals the telescoping form. Without decomposing 1/(n(n+1)) into 1/n - 1/(n+1), the cancellation is invisible.

To apply this reliably, write out the N-th partial sum explicitly — do not try to track the cancellation in your head. Write S_N = term₁ + term₂ + term₃ + ... + term_N after substituting the partial fraction form, and physically cross out matching terms. What is left is your closed-form for S_N. This careful bookkeeping also tells you which terms survive at each end: sometimes it is the first two that survive, sometimes just the first one, depending on the shift in the formula. Recognizing when a series can telescope — and having the partial fractions skill to expose that structure — makes you one of the few students who can find exact infinite sums on demand.
