---
id: divergence-test
title: Divergence Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: sequences-convergence
    type: hard
  - id: series-definition-and-partial-sums
    type: hard
builds-toward:
  - integral-test
  - comparison-test
tags: [series, convergence-tests, divergence]
stage: formal-systems
status: validated
---

# Divergence Test

## Core Idea
The Divergence Test (nth-term test) states: if lim(n->infinity) a_n is not zero (or does not exist), then the series sum of a_n diverges. This is the first and simplest convergence test. However, it is one-directional: if a_n -> 0, the test is inconclusive (the series may converge or diverge). The harmonic series is the classic example of a_n -> 0 but the series diverging.

## How It's Best Learned
Apply as the first check for any series: if the terms do not approach zero, stop immediately and declare divergence. Practice with series like sum of n/(2n + 1), sum of (-1)^n, sum of cos(n). Emphasize the critical limitation: the converse is false.

## Common Misconceptions
- Concluding convergence because a_n -> 0 (the test cannot prove convergence, only divergence).
- Skipping this test and jumping to more complex tests when a simple limit would show divergence.
- Confusing this test with the comparison test or limit comparison test.

## Questions

```yaml
- question: "A student evaluates a series and finds that the terms a_n approach 0 as n → ∞. What can they conclude using the Divergence Test?"
  type: multiple-choice
  options:
    - "The series converges, since the terms go to zero"
    - "The series diverges, since vanishing terms cause partial sums to stabilize"
    - "Nothing — the Divergence Test is inconclusive when a_n → 0; further analysis is required"
    - "The series converges absolutely"
  answer: 2
  explanation: "This is the central trap of the Divergence Test. a_n → 0 is NECESSARY but not sufficient for convergence. The harmonic series Σ 1/n has terms going to zero yet diverges. The Divergence Test can only prove divergence (when a_n does not approach 0); it cannot prove convergence. When a_n → 0, you must use another test."

- question: "What does the Divergence Test conclude about the series Σ n/(2n + 1)?"
  type: multiple-choice
  options:
    - "The series converges because n/(2n+1) < 1 for all n"
    - "The series diverges because lim n/(2n+1) = 1/2 ≠ 0"
    - "The series diverges because 1/2 < 1"
    - "The test is inconclusive because the terms are bounded"
  answer: 1
  explanation: "As n → ∞, n/(2n+1) → 1/2 ≠ 0. Since the terms do not approach zero, the Divergence Test immediately confirms divergence — no further analysis needed. Option A confuses boundedness of terms with convergence of the series. Option D is wrong for the same reason: being bounded does not make the Divergence Test inconclusive; it is inconclusive only when a_n → 0."

- question: "The Divergence Test can be used to confirm that a series converges."
  type: true-false
  answer: false
  explanation: "The Divergence Test is strictly one-directional: it can only prove divergence. If a_n does not approach 0, the series diverges. If a_n → 0, the test says nothing — you cannot conclude convergence. To prove convergence, you need a different test (integral test, comparison test, ratio test, etc.)."

- question: "The harmonic series Σ 1/n diverges even though its terms approach zero."
  type: true-false
  answer: true
  explanation: "This is the definitive counterexample to the misconception that a_n → 0 implies convergence. The harmonic series Σ 1/n diverges (shown by the integral test or Cauchy condensation), yet 1/n → 0. It is famous precisely because it violates naive intuition — terms can vanish without the sum stabilizing."

- question: "Why is it not enough for a series to have terms approaching zero in order to conclude that the series converges? Give an example that illustrates your answer."
  type: short-answer
  answer: "Terms approaching zero is necessary but not sufficient for convergence. The partial sums must stabilize, which requires the terms to decrease fast enough — and a_n → 0 alone does not guarantee this. The harmonic series Σ 1/n is the classic example: 1/n → 0, yet the series diverges because the terms shrink too slowly. Terms like 1/n² decrease fast enough (series converges); terms like 1/n do not."
  explanation: "The Divergence Test tells you only what is ruled out (divergence is certain when a_n ↛ 0), not what is established. Convergence requires a separate positive argument. Keeping the harmonic series in mind as the standard counterexample helps prevent the 'vanishing terms ⟹ convergence' fallacy."
```

## Explainer

Before testing whether a series converges, ask the simplest possible question: are the terms even going to zero? If they aren't, there is no hope of the series converging — you can't add up infinitely many chunks of positive size and get a finite total. This is the **Divergence Test** (also called the nth-term test): if lim(n→∞) aₙ ≠ 0, the series diverges. Full stop. No further analysis needed.

The reasoning is intuitive but worth making precise. Recall from your study of sequences that for a series to have any chance of converging, its partial sums must stabilize. Partial sums stabilize only if the new terms being added become negligible — that is, if aₙ → 0. If aₙ is heading toward, say, 2, then each new partial sum grows by roughly 2, so the series diverges. For example, consider Σ n/(2n + 1). As n → ∞, n/(2n + 1) → 1/2 ≠ 0. The terms never become small, so the partial sums grow without bound — divergence confirmed immediately.

The critical limitation — and the most common source of error — is that the test is **one-directional**. It can only prove divergence; it can never prove convergence. The converse is false: aₙ → 0 does NOT guarantee convergence. The harmonic series Σ 1/n is the definitive counterexample — its terms go to zero, yet the series diverges. (This is why the harmonic series is famous: it violates the naive intuition that "small enough terms → convergence.") When the Divergence Test is inconclusive (aₙ → 0), you must reach for a different tool: the integral test, comparison test, ratio test, and so on.

Think of the Divergence Test as a quick triage step at the start of every series problem. Check it first, always. If the terms don't vanish, the series is dead on arrival. If they do vanish, you know only that the test has nothing to say — the series could converge or diverge, and you need more information. This habit of applying the cheapest, fastest test first before escalating to more powerful tools is a core strategy in series analysis.
