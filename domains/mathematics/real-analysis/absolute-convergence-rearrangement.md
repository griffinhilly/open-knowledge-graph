---
id: absolute-convergence-rearrangement
title: Absolute Convergence and Rearrangement
domain: mathematics
course: real-analysis
prerequisites:
- id: rigorous-series-convergence
  type: hard
tags:
- absolute-convergence
- rearrangement
- conditional-convergence
stage: advanced
status: validated
---

# Absolute Convergence and Rearrangement

## Core Idea
A series ∑aₙ converges absolutely if ∑|aₙ| converges. Absolute convergence implies convergence, but not vice versa (∑(-1)ⁿ/n converges conditionally but not absolutely). A key theorem: absolutely convergent series remain convergent after any rearrangement (to the same sum), while conditionally convergent series can be rearranged to converge to any value or diverge entirely.

## How It's Best Learned
Compare 1 - 1/2 + 1/3 - 1/4 + ... (converges conditionally to ln 2) with its rearrangement 1 + 1/3 - 1/2 + 1/5 + 1/7 - 1/4 + ... (converges to 3ln 2/2). Show why ∑1/n converges absolutely only after grouping.

## Common Misconceptions
- Thinking conditional convergence means the series barely converges; ∑(-1)ⁿ/n is robustly conditionally convergent.
- Confusing rearrangement with reindexing; we're permuting terms, not reordering indices.
- Assuming rearrangement can only change the sum slightly; it can change it arbitrarily or destroy convergence.

## Explainer

From your study of rigorous series convergence, you know that a series ∑aₙ converges when its partial sums settle to a finite limit. But there is a deeper question: does the series converge because of genuine summability, or only because of delicate cancellation between positive and negative terms? **Absolute convergence** — the condition that ∑|aₙ| converges — distinguishes these two cases. When the absolute values form a convergent series, the original series is "robustly" convergent; when only the original series converges (while ∑|aₙ| diverges), the convergence is "fragile," depending critically on the arrangement of terms.

The alternating harmonic series ∑(−1)ⁿ⁺¹/n = 1 − 1/2 + 1/3 − 1/4 + ⋯ converges to ln 2 by the alternating series test. But ∑1/n = 1 + 1/2 + 1/3 + 1/4 + ⋯ is the harmonic series, which diverges. So the alternating harmonic series converges **conditionally** — its convergence depends entirely on the alternating signs creating enough cancellation. By contrast, ∑(−1)ⁿ/n² converges absolutely because ∑1/n² = π²/6 < ∞. Here the terms are summable on their own merits, and the signs are irrelevant to convergence.

The deepest consequence of this distinction is the **Riemann rearrangement theorem**: a conditionally convergent series can be rearranged to converge to any real number whatsoever, or to diverge. This is not a technical curiosity — it means the "sum" of a conditionally convergent series is an artifact of the particular ordering. The mechanism is constructive: the positive terms alone diverge to +∞ and the negative terms alone diverge to −∞ (both diverge because the absolute series diverges). To hit a target T, take positive terms until the partial sum exceeds T, then negative terms until it dips below T, and repeat. The oscillations shrink to zero because aₙ → 0, so the rearranged series converges to T. You can aim at any T, or arrange for divergence.

Absolutely convergent series are immune to this pathology. If ∑|aₙ| converges, both the positive part ∑aₙ⁺ and the negative part ∑aₙ⁻ converge independently to finite values. The sum is then the difference of two finite quantities, and rearranging terms cannot change either sub-sum. Every rearrangement converges to the same value. This is why absolute convergence is the "safe" mode of convergence: it guarantees that the sum is a genuine, order-independent quantity. In applications — Fourier series, power series, numerical computation — absolute convergence is almost always the relevant condition, because rearrangement-sensitivity would make the "sum" meaningless in any context where the order of summation might vary.

## Questions

```yaml
- question: "The alternating harmonic series 1 − 1/2 + 1/3 − 1/4 + ⋯ converges to ln 2. If the terms are rearranged so that two positive terms always precede one negative term (e.g., 1 + 1/3 − 1/2 + 1/5 + 1/7 − 1/4 + ⋯), what can we conclude about the rearranged series?"
  type: multiple-choice
  options:
    - "It still converges to ln 2, because the same terms are present"
    - "It diverges, because the terms are out of order"
    - "It converges to a different value, approximately (3/2) ln 2"
    - "It cannot converge because rearranging an infinite series always destroys convergence"
  answer: 2
  explanation: "This is an instance of the Riemann rearrangement theorem: a conditionally convergent series can be rearranged to converge to any real value. The alternating harmonic series is conditionally convergent (∑1/n diverges, so it is not absolutely convergent), so rearrangements can produce different sums. The two-positive-one-negative rearrangement converges to (3/2) ln 2 ≈ 1.04 rather than ln 2 ≈ 0.69. Option A is the most tempting error — the naive intuition that 'same terms = same sum' fails for infinite series when convergence is only conditional."

- question: "Which of the following series can safely be rearranged into any order without changing its sum?"
  type: multiple-choice
  options:
    - "∑(−1)ⁿ/n (the alternating harmonic series)"
    - "∑(−1)ⁿ/n² (an alternating series whose absolute value also converges)"
    - "∑(−1)ⁿ (the alternating series of ±1, which diverges)"
    - "∑1/n (the harmonic series, which diverges to infinity)"
  answer: 1
  explanation: "Only absolutely convergent series are guaranteed to be rearrangement-invariant. ∑(−1)ⁿ/n² is absolutely convergent because ∑1/n² = π²/6 < ∞. Rearranging its terms always produces the same sum. By contrast, ∑(−1)ⁿ/n is only conditionally convergent (∑1/n diverges), so by Riemann's theorem it can be rearranged to any target value. The other two options diverge outright, so the question of rearrangement-invariance doesn't apply in the usual sense."

- question: "If ∑aₙ converges absolutely, then ∑aₙ also converges in the ordinary sense."
  type: true-false
  answer: true
  explanation: "Absolute convergence implies convergence. The proof uses the Cauchy criterion: since ∑|aₙ| converges, for any ε > 0 the tail sum ∑_{k=m}^{n} |aₖ| → 0, and since |∑aₖ| ≤ ∑|aₖ|, the partial sums of ∑aₙ form a Cauchy sequence and therefore converge. The converse is false — the alternating harmonic series converges but not absolutely."

- question: "If ∑aₙ converges, then ∑|aₙ| also converges."
  type: true-false
  answer: false
  explanation: "This is the classic false converse. The alternating harmonic series ∑(−1)ⁿ/n converges (to ln 2, by the alternating series test), but ∑|(−1)ⁿ/n| = ∑1/n is the harmonic series, which diverges. Convergence of ∑aₙ only implies absolute convergence when there is no cancellation structure exploiting the sign pattern — in general, alternating signs can carry a series to a finite limit even when the terms are too large for absolute convergence."

- question: "Why does absolute convergence protect a series from the effects of rearrangement, while conditional convergence does not?"
  type: short-answer
  answer: "In an absolutely convergent series, the positive and negative parts each converge independently to finite values. Rearranging terms cannot change the total because both sub-sums are locked in. In a conditionally convergent series, the positive terms alone diverge to +∞ and the negative terms alone diverge to −∞; the finite sum arises entirely from the balance between these two diverging components. By choosing a rearrangement that front-loads more positive (or more negative) terms, one can tip this balance arbitrarily, driving partial sums toward any target value or to infinity."
  explanation: "The Riemann rearrangement theorem is constructive: to rearrange ∑(−1)ⁿ/n toward a target T, take positive terms until the partial sum exceeds T, then take negative terms until it dips below T, and repeat. Since both the positive and negative sub-series diverge, this process never runs out of terms, and the oscillations shrink to zero because individual terms aₙ → 0. The key mechanism — inexhaustible supplies of both positive and negative terms — is exactly what absolute convergence rules out."
```
