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

## Explainer

Before testing whether a series converges, ask the simplest possible question: are the terms even going to zero? If they aren't, there is no hope of the series converging — you can't add up infinitely many chunks of positive size and get a finite total. This is the **Divergence Test** (also called the nth-term test): if lim(n→∞) aₙ ≠ 0, the series diverges. Full stop. No further analysis needed.

The reasoning is intuitive but worth making precise. Recall from your study of sequences that for a series to have any chance of converging, its partial sums must stabilize. Partial sums stabilize only if the new terms being added become negligible — that is, if aₙ → 0. If aₙ is heading toward, say, 2, then each new partial sum grows by roughly 2, so the series diverges. For example, consider Σ n/(2n + 1). As n → ∞, n/(2n + 1) → 1/2 ≠ 0. The terms never become small, so the partial sums grow without bound — divergence confirmed immediately.

The critical limitation — and the most common source of error — is that the test is **one-directional**. It can only prove divergence; it can never prove convergence. The converse is false: aₙ → 0 does NOT guarantee convergence. The harmonic series Σ 1/n is the definitive counterexample — its terms go to zero, yet the series diverges. (This is why the harmonic series is famous: it violates the naive intuition that "small enough terms → convergence.") When the Divergence Test is inconclusive (aₙ → 0), you must reach for a different tool: the integral test, comparison test, ratio test, and so on.

Think of the Divergence Test as a quick triage step at the start of every series problem. Check it first, always. If the terms don't vanish, the series is dead on arrival. If they do vanish, you know only that the test has nothing to say — the series could converge or diverge, and you need more information. This habit of applying the cheapest, fastest test first before escalating to more powerful tools is a core strategy in series analysis.
