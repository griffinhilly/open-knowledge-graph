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

## Questions

```yaml
- question: "You want to apply the Alternating Series Test to Σ (-1)ⁿ aₙ. You verify that lim aₙ = 0 as n → ∞. What else must you verify?"
  type: multiple-choice
  options:
    - "Nothing — lim aₙ = 0 is the only condition required for the test to apply"
    - "That the series of absolute values Σ aₙ diverges"
    - "That aₙ₊₁ ≤ aₙ for all sufficiently large n — the terms must be non-increasing"
    - "That the partial sums are bounded above by some constant M"
  answer: 2
  explanation: "The Alternating Series Test requires three conditions: alternating signs, terms approaching zero, AND terms being non-increasing (aₙ₊₁ ≤ aₙ). The most common error is checking only lim aₙ = 0 and assuming that's sufficient. A counterexample: if aₙ alternates between 1/n (for even n) and 2/n (for odd n), the limit is still 0 but the terms are not monotone — the test doesn't apply, and the series may diverge. Option B is irrelevant; the test is specifically designed for series that converge despite the absolute series diverging."

- question: "You use the first 5 terms of the alternating harmonic series Σ (-1)ⁿ⁺¹/n = ln(2) to estimate ln(2). S₅ = 1 − 1/2 + 1/3 − 1/4 + 1/5 = 47/60. By the alternating series estimation theorem, the error satisfies:"
  type: multiple-choice
  options:
    - "|ln(2) − S₅| ≤ 1/5, the magnitude of the last included term"
    - "|ln(2) − S₅| ≤ 1/6, the magnitude of the first omitted term"
    - "|ln(2) − S₅| ≤ 1/10, half the last term"
    - "|ln(2) − S₅| = 0, since ln(2) can be computed exactly"
  answer: 1
  explanation: "The alternating series estimation theorem states that the error from stopping at the Nth partial sum is bounded by the (N+1)th term — the first term you omitted. After S₅, the next term is a₆ = 1/6, so |ln(2) − S₅| ≤ 1/6. Option A is the most tempting mistake: using the last *included* term rather than the first *omitted* one. The bound comes from the bracketing property: the true sum is always sandwiched between two consecutive partial sums, so the error cannot exceed their difference, which is exactly the next term."

- question: "For the alternating harmonic series Σ (-1)ⁿ⁺¹/n, the odd partial sums S₁, S₃, S₅, ... form a decreasing sequence and the even partial sums S₂, S₄, S₆, ... form an increasing sequence, with the true sum trapped between them."
  type: true-false
  answer: true
  explanation: "This bracketing behavior is the geometric heart of the Alternating Series Test. S₁ = 1 overshoots the sum; adding −1/2 gives S₂ = 1/2, which undershoots; adding +1/3 gives S₃ = 5/6, which overshoots but less than S₁; and so on. The odd partial sums descend toward the limit from above; the even partial sums ascend from below. Since each correction is smaller than the last (decreasing terms), the two sequences close in on each other and must converge to the same value — the sum of the series."

- question: "The Alternating Series Test can be applied to any series with alternating signs whose terms approach zero, without any additional conditions."
  type: true-false
  answer: false
  explanation: "The decreasing condition (aₙ₊₁ ≤ aₙ) is a separate and necessary requirement. A series can have alternating signs and aₙ → 0 while still failing the test — if the terms do not decrease monotonically, the oscillating partial-sum argument breaks down. Without monotone decrease, the odd partial sums might not consistently overshoot (or consistently undershoot), and the bracketing argument fails. The common confusion stems from conflating this test with the divergence test: both check whether aₙ → 0, but for different purposes — divergence test checks a necessary condition for convergence, while the Alternating Series Test has two conditions that together are sufficient."

- question: "The harmonic series Σ 1/n diverges, but the alternating harmonic series Σ (-1)ⁿ⁺¹/n converges. Explain why the alternating signs make the difference."
  type: short-answer
  answer: "The harmonic series diverges because its partial sums grow without bound — even though each term is small, they accumulate faster than they shrink. The alternating version forces systematic cancellation: each positive term is immediately followed by a negative term of smaller magnitude, so the partial sums oscillate around the true value rather than drifting off to infinity. Formally, the odd partial sums decrease (each positive addition is followed by a subtraction of a slightly smaller amount) and the even partial sums increase, and since the terms shrink to zero, both sequences converge to the same limit. The alternating signs create a self-correcting structure absent from the all-positive series."
  explanation: "This is the essence of conditional convergence: the series converges, but only because of cancellation between positive and negative terms. Rearranging the terms can actually change the sum — a fact known as the Riemann rearrangement theorem — which is why conditional convergence is considered a weaker form of convergence than absolute convergence (where Σ |aₙ| converges on its own)."
```

## Explainer

You know from the divergence test that if the terms of a series don't approach zero, the series diverges — and from your study of sequences what it means for aₙ → 0. But the harmonic series Σ 1/n shows that aₙ → 0 is not sufficient for convergence; the partial sums grow without bound. What changes when signs alternate? The series 1 − 1/2 + 1/3 − 1/4 + ··· has the same magnitudes as the harmonic series but *converges*, to ln(2). Alternating signs create systematic cancellation that forces convergence even when the absolute values diverge.

The mechanism is clearest by watching the partial sums. S₁ = 1 overshoots the true sum. S₂ = 1 − 1/2 = 1/2 undershoots (we subtracted too much). S₃ = 5/6 overshoots again. The partial sums form two interlocking monotone sequences: odd partial sums decrease (S₁ > S₃ > S₅ > ···) and even partial sums increase (S₂ < S₄ < S₆ < ···), with every odd sum above every even sum. If the terms aₙ are decreasing and approach zero, the gap between consecutive partial sums shrinks to zero, and both sequences must converge to the same limit — trapped between them. This bracketing picture is exactly what the **Alternating Series Test** (Leibniz's test) formalizes.

The three conditions are each necessary for this argument. The **alternating signs** condition ensures partial sums swing back and forth rather than drifting in one direction. The **decreasing** condition aₙ₊₁ ≤ aₙ ensures that each correction is smaller than the previous one, so the oscillations shrink. The **limit condition** aₙ → 0 ensures the oscillations shrink all the way to zero. If aₙ doesn't approach zero, the series diverges by the divergence test you already know — the Alternating Series Test doesn't even apply. The most common error is checking only aₙ → 0 and forgetting to verify the decreasing condition; these are two separate requirements.

A bonus consequence is the **alternating series estimation theorem**: |S − Sₙ| ≤ aₙ₊₁. The error from stopping at the nth partial sum is bounded by the very next term — the first one you omitted. The true sum is always sandwiched between two consecutive partial sums, so the error cannot exceed their difference, which is aₙ₊₁. This makes alternating series useful for numerical approximation: to estimate ln(2) within 0.001, take enough terms so that aₙ₊₁ = 1/(n+1) < 0.001, meaning n ≥ 999. The next topic — absolute versus conditional convergence — classifies whether a series converges because of this cancellation (conditional) or whether the absolute values already converge on their own (absolute), which is a strictly stronger property.
