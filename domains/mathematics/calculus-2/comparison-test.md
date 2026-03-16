---
id: comparison-test
title: Comparison Test
domain: mathematics
course: calculus-2
prerequisites:
- id: geometric-series
  type: hard
- id: p-series
  type: hard
- id: divergence-test
  type: soft
- id: improper-integrals-divergence
  type: soft
- id: integral-test
  type: soft
builds-toward:
- limit-comparison-test
tags:
- series
- convergence-tests
- comparison
stage: formal-systems
status: validated
---
# Comparison Test

## Core Idea
The Direct Comparison Test states: if 0 <= a_n <= b_n for all n, then if sum of b_n converges, sum of a_n converges (smaller than convergent = convergent); if sum of a_n diverges, sum of b_n diverges (bigger than divergent = divergent). The test requires finding a suitable comparison series, typically a geometric or p-series. It is the series analogue of the comparison test for improper integrals.

## How It's Best Learned
Build a library of benchmark series (geometric, p-series). Practice bounding series terms above by convergent benchmarks or below by divergent benchmarks. Emphasize that the comparison must go the right direction: you cannot conclude convergence by bounding above by a divergent series.

## Common Misconceptions
- Comparing in the wrong direction (bounding below by a convergent series proves nothing).
- Forgetting that both series must have non-negative terms.
- Choosing a comparison series that is not actually larger or smaller as needed.

## Explainer

You have built up a library of series whose convergence behavior you know exactly: **geometric series** Σ rⁿ converges when |r| < 1 and diverges otherwise; **p-series** Σ 1/nᵖ converges for p > 1 and diverges for p ≤ 1. The comparison test lets you leverage this library to analyze new, more complex series. The idea is simple: if you can trap a new series between two benchmarks whose behavior you know, you inherit their conclusions.

The logic runs in two directions. If every term satisfies 0 ≤ a_n ≤ b_n and if Σb_n converges, then Σa_n must also converge — your series is dominated term-by-term by a convergent one, so its partial sums are bounded above and increasing, which forces convergence. Conversely, if Σa_n diverges (and again 0 ≤ a_n ≤ b_n), then Σb_n also diverges — if the smaller series blows up, the larger one certainly does. The two moves that prove nothing are: bounding your series above by a divergent series (being smaller than something that diverges doesn't tell you whether you diverge), and bounding below by a convergent series (being larger than something that converges doesn't tell you whether you converge). Only the "tight" comparisons work.

To apply the test, you need to identify a comparison series and verify the inequality. For large n, the dominant terms in a_n reveal what benchmark to use. Consider Σ 1/(n² + 3): since n² + 3 > n² for all n, we have 1/(n² + 3) < 1/n². Since Σ 1/n² converges (p-series with p = 2 > 1), and since 0 ≤ 1/(n² + 3) ≤ 1/n², the comparison test confirms convergence. For a divergence example, consider Σ 1/(n - ln n): for large n, ln n < n/2 so n - ln n < n, meaning 1/(n - ln n) > 1/n. Since Σ 1/n diverges (p-series with p = 1), and our terms are larger, Σ 1/(n - ln n) also diverges.

The comparison test encodes the same logical principle as the comparison test for improper integrals you may have seen earlier — positivity plus a term-by-term domination relationship transfers convergence or divergence. It is often the first tool to try when a series resembles a benchmark but has a modified denominator. When the inequality is awkward to establish directly (for instance, when the terms are approximately equal to a benchmark rather than clearly larger or smaller), the **limit comparison test** offers an algebraic shortcut to the same conclusion: if lim(a_n/b_n) = L with 0 < L < ∞, then both series behave the same way.
