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

## Questions

```yaml
- question: "You know Σ 1/n (the harmonic series) diverges. You find a series whose terms satisfy 0 ≤ aₙ ≤ 1/n for all n. What can the direct comparison test conclude about Σaₙ?"
  type: multiple-choice
  options:
    - "Σaₙ diverges, because it is bounded above by a divergent series"
    - "Σaₙ converges, because its terms are smaller than the harmonic series terms"
    - "Nothing — bounding a series above by a divergent series gives no information about convergence or divergence"
    - "Σaₙ diverges if its terms are positive; converges if some terms equal zero"
  answer: 2
  explanation: "Being bounded above by a divergent series is logically uninformative. The comparison test only works in two 'tight' directions: (1) if 0 ≤ aₙ ≤ bₙ and Σbₙ converges, then Σaₙ converges; (2) if 0 ≤ aₙ ≤ bₙ and Σaₙ diverges, then Σbₙ diverges. The condition here — bounded above by a divergent series — fits neither. As concrete evidence: aₙ = 1/n² satisfies aₙ ≤ 1/n but Σ 1/n² converges; aₙ = 1/(2n) also satisfies aₙ ≤ 1/n but Σ 1/(2n) diverges. The test cannot distinguish them."

- question: "To show that Σ 1/(n² + 5n) converges using the direct comparison test, which approach is valid?"
  type: multiple-choice
  options:
    - "Compare to Σ 1/n: since 1/(n² + 5n) < 1/n and Σ 1/n diverges, Σ 1/(n² + 5n) must converge"
    - "Compare to Σ 1/n²: since n² + 5n > n² we have 1/(n² + 5n) < 1/n², and Σ 1/n² converges (p-series, p = 2)"
    - "Compare to Σ 1/n³: since 1/(n² + 5n) > 1/n³, Σ 1/(n² + 5n) must diverge"
    - "Compare to Σ 1/(5n): since n² + 5n < 5n for small n, the terms are eventually bounded below by 1/(5n)"
  answer: 1
  explanation: "Since n² + 5n > n² for all n ≥ 1, we have 1/(n² + 5n) < 1/n², establishing 0 ≤ 1/(n² + 5n) ≤ 1/n². Since Σ 1/n² converges (p-series with p = 2 > 1), the comparison test concludes Σ 1/(n² + 5n) converges. Option A is the classic error: bounding above by a divergent series proves nothing. Option C has the inequality backwards and draws the wrong conclusion. The valid move is always: bounded above by something convergent → convergent."

- question: "If 0 ≤ aₙ ≤ bₙ for all n and Σaₙ diverges, then Σbₙ must also diverge."
  type: true-false
  answer: true
  explanation: "True. This is one of the two valid moves of the comparison test. If the smaller series Σaₙ diverges — its partial sums grow without bound — then Σbₙ, whose partial sums are always at least as large (since bₙ ≥ aₙ ≥ 0), must also grow without bound. Intuitively: if even the smaller quantity is infinite, the larger one certainly is too."

- question: "If 0 ≤ aₙ ≤ bₙ for all n and Σbₙ diverges, then Σaₙ must also diverge."
  type: true-false
  answer: false
  explanation: "False. This is the most common error with the comparison test. Being bounded above by a divergent series tells you nothing. The smaller series can converge or diverge. Counterexample: 0 ≤ 1/n² ≤ 1/n for all n ≥ 1, and Σ 1/n diverges, yet Σ 1/n² converges (p = 2 > 1). The only valid upper-bound move is: bounded above by a *convergent* series → convergence. The valid lower-bound move is: bounded below by a *divergent* series → divergence. The other two combinations are logically useless."

- question: "Explain in your own words why only two of the four possible comparison directions yield valid conclusions, and identify which two are useless."
  type: short-answer
  answer: "The valid directions are: (1) if 0 ≤ aₙ ≤ bₙ and Σbₙ converges, then Σaₙ converges — partial sums of aₙ are bounded above by those of bₙ, and a bounded increasing sequence converges; (2) if 0 ≤ aₙ ≤ bₙ and Σaₙ diverges, then Σbₙ diverges — partial sums of bₙ exceed those of aₙ, which blow up. The two useless directions are: bounded above by a divergent series (being smaller than something infinite doesn't prevent convergence), and bounded below by a convergent series (being larger than something finite doesn't prevent divergence)."
  explanation: "A useful analogy: if a small pile of rocks keeps growing forever, a larger pile certainly does too (valid). If a large pile is finite, the smaller one must be too (valid). But knowing the large pile grows forever tells you nothing about the small one, and knowing the small pile is finite tells you nothing about the large one. The comparison test encodes exactly these two monotone implications and nothing more."
```

## Explainer

You have built up a library of series whose convergence behavior you know exactly: **geometric series** Σ rⁿ converges when |r| < 1 and diverges otherwise; **p-series** Σ 1/nᵖ converges for p > 1 and diverges for p ≤ 1. The comparison test lets you leverage this library to analyze new, more complex series. The idea is simple: if you can trap a new series between two benchmarks whose behavior you know, you inherit their conclusions.

The logic runs in two directions. If every term satisfies 0 ≤ a_n ≤ b_n and if Σb_n converges, then Σa_n must also converge — your series is dominated term-by-term by a convergent one, so its partial sums are bounded above and increasing, which forces convergence. Conversely, if Σa_n diverges (and again 0 ≤ a_n ≤ b_n), then Σb_n also diverges — if the smaller series blows up, the larger one certainly does. The two moves that prove nothing are: bounding your series above by a divergent series (being smaller than something that diverges doesn't tell you whether you diverge), and bounding below by a convergent series (being larger than something that converges doesn't tell you whether you converge). Only the "tight" comparisons work.

To apply the test, you need to identify a comparison series and verify the inequality. For large n, the dominant terms in a_n reveal what benchmark to use. Consider Σ 1/(n² + 3): since n² + 3 > n² for all n, we have 1/(n² + 3) < 1/n². Since Σ 1/n² converges (p-series with p = 2 > 1), and since 0 ≤ 1/(n² + 3) ≤ 1/n², the comparison test confirms convergence. For a divergence example, consider Σ 1/(n - ln n): for large n, ln n < n/2 so n - ln n < n, meaning 1/(n - ln n) > 1/n. Since Σ 1/n diverges (p-series with p = 1), and our terms are larger, Σ 1/(n - ln n) also diverges.

The comparison test encodes the same logical principle as the comparison test for improper integrals you may have seen earlier — positivity plus a term-by-term domination relationship transfers convergence or divergence. It is often the first tool to try when a series resembles a benchmark but has a modified denominator. When the inequality is awkward to establish directly (for instance, when the terms are approximately equal to a benchmark rather than clearly larger or smaller), the **limit comparison test** offers an algebraic shortcut to the same conclusion: if lim(a_n/b_n) = L with 0 < L < ∞, then both series behave the same way.
