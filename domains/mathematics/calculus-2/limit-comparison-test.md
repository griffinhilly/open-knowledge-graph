---
id: limit-comparison-test
title: Limit Comparison Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: comparison-test
    type: hard
builds-toward:
  - absolute-vs-conditional-convergence
tags: [series, convergence-tests, limit-comparison]
stage: formal-systems
status: validated
---

# Limit Comparison Test

## Core Idea
The Limit Comparison Test states: if a_n > 0 and b_n > 0, and lim(n->infinity) a_n/b_n = c where 0 < c < infinity, then sum of a_n and sum of b_n either both converge or both diverge. This test is more flexible than direct comparison because you only need to show the terms are proportional in the limit, not that one is always larger than the other.

## How It's Best Learned
Compare unfamiliar series with p-series or geometric series by computing the limit of their ratio. Practice identifying the dominant term in a_n to guess the right comparison series. Emphasize that the limit must be a positive finite number for the conclusion to hold.

## Common Misconceptions
- Drawing a conclusion when the limit is 0 or infinity (these cases require separate analysis).
- Choosing a comparison series b_n that does not match the growth rate of a_n.
- Confusing the limit comparison test with L'Hopital's rule (they serve different purposes, though L'Hopital's rule may be used within the limit comparison test).

## Explainer

The Direct Comparison Test — your prerequisite — lets you conclude that a series converges if its terms are always smaller than a convergent series, or diverges if its terms are always larger than a divergent series. This is powerful but demanding: you need a *termwise* inequality, which can be hard to establish, especially when terms involve sums or differences in the numerator. The Limit Comparison Test relaxes this requirement. Instead of demanding that aₙ ≤ bₙ for all n, it only requires that aₙ and bₙ have the same **asymptotic order** — that their ratio approaches a positive finite constant. If aₙ/bₙ → c with 0 < c < ∞, then aₙ ≈ c · bₙ for large n, so the two series are in a sense proportional, and they must converge or diverge together.

The practical skill is choosing the right comparison series bₙ. The strategy is to identify the **dominant terms** in the numerator and denominator of aₙ and construct bₙ from those terms alone. For example, if aₙ = (3n² + 5) / (n⁴ − 2n + 1), the dominant terms give bₙ = 3n²/n⁴ = 3/n², a convergent p-series (p = 2 > 1). You then verify: aₙ/bₙ = [(3n² + 5)/(n⁴ − 2n + 1)] / [3/n²] → 1 as n → ∞, so the limit is 1, a positive finite number, and the Limit Comparison Test confirms that Σaₙ converges. The constant 3 in bₙ was irrelevant for the conclusion — any positive constant multiple of a convergent series still converges.

When the limit equals 0 or infinity, the test is inconclusive for the comparison you chose; try a different bₙ. A limit of 0 means aₙ grows much slower than bₙ — your comparison series was too large and you should try a smaller one. A limit of ∞ means aₙ grows much faster than bₙ — try a larger comparison. These boundary cases are where the Limit Comparison Test and the Direct Comparison Test are often combined: you use the Limit Comparison Test to identify the right growth rate, and then fall back to direct comparison or a known test if the limit is degenerate.

The Limit Comparison Test is most useful when the Direct Comparison Test fails because the termwise inequality goes the wrong way. For example, if Σ1/n diverges but you cannot directly show your series has terms larger than 1/n (perhaps the inequality reverses for some small n), the Limit Comparison Test sidesteps the problem — the eventual proportionality is all that matters. This makes it one of the most versatile convergence tests for series with rational or algebraic terms.
