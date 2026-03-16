---
id: alternating-series-test
title: Alternating Series Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: divergence-test
    type: hard
  - id: sequences-convergence
    type: hard
builds-toward:
  - absolute-vs-conditional-convergence
tags: [series, convergence-tests, alternating]
stage: formal-systems
status: validated
---

# Alternating Series Test

## Core Idea
The Alternating Series Test (Leibniz's test) states: if a_n > 0, a_n is decreasing, and lim a_n = 0, then the alternating series sum of (-1)^n * a_n converges. Furthermore, the error from using the Nth partial sum is bounded by the (N+1)th term: |S - S_N| <= a_(N+1). This test handles series that converge because of cancellation between positive and negative terms, even when the series of absolute values diverges.

## How It's Best Learned
Verify the three conditions: alternating signs, decreasing absolute values, limit zero. Visualize partial sums bouncing back and forth, converging to the sum. Apply the alternating series estimation theorem for error bounds. Classic example: the alternating harmonic series sum of (-1)^(n+1)/n = ln(2).

## Common Misconceptions
- Forgetting to check that a_n is decreasing (not just that a_n -> 0).
- Applying the test to non-alternating series.
- Confusing the alternating series test with the divergence test (both check if a_n -> 0, but for different conclusions).

## Explainer

You know from the divergence test that if the terms of a series don't approach zero, the series diverges — and from your study of sequences what it means for aₙ → 0. But the harmonic series Σ 1/n shows that aₙ → 0 is not sufficient for convergence; the partial sums grow without bound. What changes when signs alternate? The series 1 − 1/2 + 1/3 − 1/4 + ··· has the same magnitudes as the harmonic series but *converges*, to ln(2). Alternating signs create systematic cancellation that forces convergence even when the absolute values diverge.

The mechanism is clearest by watching the partial sums. S₁ = 1 overshoots the true sum. S₂ = 1 − 1/2 = 1/2 undershoots (we subtracted too much). S₃ = 5/6 overshoots again. The partial sums form two interlocking monotone sequences: odd partial sums decrease (S₁ > S₃ > S₅ > ···) and even partial sums increase (S₂ < S₄ < S₆ < ···), with every odd sum above every even sum. If the terms aₙ are decreasing and approach zero, the gap between consecutive partial sums shrinks to zero, and both sequences must converge to the same limit — trapped between them. This bracketing picture is exactly what the **Alternating Series Test** (Leibniz's test) formalizes.

The three conditions are each necessary for this argument. The **alternating signs** condition ensures partial sums swing back and forth rather than drifting in one direction. The **decreasing** condition aₙ₊₁ ≤ aₙ ensures that each correction is smaller than the previous one, so the oscillations shrink. The **limit condition** aₙ → 0 ensures the oscillations shrink all the way to zero. If aₙ doesn't approach zero, the series diverges by the divergence test you already know — the Alternating Series Test doesn't even apply. The most common error is checking only aₙ → 0 and forgetting to verify the decreasing condition; these are two separate requirements.

A bonus consequence is the **alternating series estimation theorem**: |S − Sₙ| ≤ aₙ₊₁. The error from stopping at the nth partial sum is bounded by the very next term — the first one you omitted. The true sum is always sandwiched between two consecutive partial sums, so the error cannot exceed their difference, which is aₙ₊₁. This makes alternating series useful for numerical approximation: to estimate ln(2) within 0.001, take enough terms so that aₙ₊₁ = 1/(n+1) < 0.001, meaning n ≥ 999. The next topic — absolute versus conditional convergence — classifies whether a series converges because of this cancellation (conditional) or whether the absolute values already converge on their own (absolute), which is a strictly stronger property.
