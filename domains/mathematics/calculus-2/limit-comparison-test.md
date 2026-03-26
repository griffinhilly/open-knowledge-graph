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

## Questions

```yaml
- question: "To test convergence of Σ (3n² + 7)/(n⁴ − n + 2), a student chooses bₙ = 1/n² and computes lim(aₙ/bₙ) = 3. What conclusion follows?"
  type: multiple-choice
  options:
    - "The test is inconclusive — the limit must equal exactly 1 for the Limit Comparison Test to apply"
    - "The series diverges because the limit 3 is greater than 1"
    - "Since lim(aₙ/bₙ) = 3 (positive and finite) and Σ 1/n² converges (p-series, p = 2), the series Σaₙ also converges"
    - "The series converges, but only after dividing by 3 to normalize the limit to 1"
  answer: 2
  explanation: "The Limit Comparison Test requires lim(aₙ/bₙ) = c where 0 < c < ∞ — any positive finite value works, not only c = 1. If the limit is 3, then aₙ ≈ 3bₙ for large n, meaning the two series are proportional and must behave identically (both converge or both diverge). Since Σ1/n² converges (p = 2 > 1), so does Σaₙ. Option A is the most common misconception about the test."

- question: "A student applies the Limit Comparison Test to a series Σaₙ using comparison series Σbₙ and finds lim(aₙ/bₙ) = 0. What does this tell them?"
  type: multiple-choice
  options:
    - "Σaₙ converges, because its terms are smaller than bₙ in the limit"
    - "Σaₙ diverges, because a limit of 0 indicates the ratio collapses"
    - "The test is inconclusive for this choice of bₙ — the student should try a comparison series that grows more slowly (matches aₙ's rate better)"
    - "Σaₙ and Σbₙ converge and diverge oppositely"
  answer: 2
  explanation: "When lim(aₙ/bₙ) = 0, the terms aₙ grow much more slowly than bₙ — the comparison series is too large. The Limit Comparison Test only gives a conclusion when the limit is a positive finite number. A limit of 0 or ∞ is inconclusive: you cannot infer convergence or divergence directly. The student should choose a smaller bₙ that more closely matches the growth rate of aₙ. Option A is tempting but wrong — even if aₙ < bₙ, a smaller divergent series can still diverge (e.g., aₙ = 1/n and bₙ = 1)."

- question: "The Limit Comparison Test is more flexible than the Direct Comparison Test because it only requires the ratio aₙ/bₙ to approach a positive finite constant, rather than a termwise inequality aₙ ≤ bₙ."
  type: true-false
  answer: true
  explanation: "True. The Direct Comparison Test needs aₙ ≤ bₙ (or aₙ ≥ bₙ) for all n — a pointwise condition that can be difficult or impossible to establish, especially when the numerator or denominator involves differences. The Limit Comparison Test only needs eventual proportionality: if aₙ/bₙ → c > 0, then for large n, aₙ ≈ c·bₙ, and the two series necessarily share convergence behavior. This avoids the need for any termwise inequality."

- question: "If lim(aₙ/bₙ) = 0 and Σbₙ diverges, then Σaₙ is expected to also diverge."
  type: true-false
  answer: false
  explanation: "False. A limit of 0 means aₙ grows much slower than bₙ — the series Σaₙ could converge even though Σbₙ diverges. For example, aₙ = 1/n² and bₙ = 1/n: lim(aₙ/bₙ) = lim(n/n²) = lim(1/n) = 0, Σ1/n diverges, but Σ1/n² converges. The Limit Comparison Test only provides a conclusion when the limit is strictly between 0 and ∞. At the boundary values 0 and ∞, no conclusion can be drawn about the original series from the chosen comparison alone."

- question: "Explain why the Limit Comparison Test fails to give a conclusion when lim(aₙ/bₙ) = ∞, and describe what this tells you about your choice of comparison series bₙ."
  type: short-answer
  answer: "When lim(aₙ/bₙ) = ∞, the terms aₙ grow much faster than bₙ — the comparison series bₙ is too small. The test cannot conclude convergence or divergence because: a series growing faster than a convergent series could still converge (e.g., faster than 1/n³ but still summable), and a series growing faster than a divergent series clearly diverges — but we don't know which case we're in without more information. The fix is to choose a larger bₙ that grows at the same asymptotic rate as aₙ (by identifying the dominant terms in the numerator and denominator of aₙ). The goal is a bₙ such that lim(aₙ/bₙ) = c for some 0 < c < ∞."
  explanation: "The skill in applying the test is matching growth rates. For rational sequences, extract the leading-term ratio: if aₙ = (5n³ + 2n)/(n⁵ + 7), the dominant terms give 5n³/n⁵ = 5/n², so try bₙ = 1/n². The constant 5 doesn't affect the convergence conclusion. A limit of ∞ with bₙ = 1/n² means you need a larger comparison, perhaps 1/n. A limit of 0 means you need a smaller comparison, perhaps 1/n³."
```

## Explainer

The Direct Comparison Test — your prerequisite — lets you conclude that a series converges if its terms are always smaller than a convergent series, or diverges if its terms are always larger than a divergent series. This is powerful but demanding: you need a *termwise* inequality, which can be hard to establish, especially when terms involve sums or differences in the numerator. The Limit Comparison Test relaxes this requirement. Instead of demanding that aₙ ≤ bₙ for all n, it only requires that aₙ and bₙ have the same **asymptotic order** — that their ratio approaches a positive finite constant. If aₙ/bₙ → c with 0 < c < ∞, then aₙ ≈ c · bₙ for large n, so the two series are in a sense proportional, and they must converge or diverge together.

The practical skill is choosing the right comparison series bₙ. The strategy is to identify the **dominant terms** in the numerator and denominator of aₙ and construct bₙ from those terms alone. For example, if aₙ = (3n² + 5) / (n⁴ − 2n + 1), the dominant terms give bₙ = 3n²/n⁴ = 3/n², a convergent p-series (p = 2 > 1). You then verify: aₙ/bₙ = [(3n² + 5)/(n⁴ − 2n + 1)] / [3/n²] → 1 as n → ∞, so the limit is 1, a positive finite number, and the Limit Comparison Test confirms that Σaₙ converges. The constant 3 in bₙ was irrelevant for the conclusion — any positive constant multiple of a convergent series still converges.

When the limit equals 0 or infinity, the test is inconclusive for the comparison you chose; try a different bₙ. A limit of 0 means aₙ grows much slower than bₙ — your comparison series was too large and you should try a smaller one. A limit of ∞ means aₙ grows much faster than bₙ — try a larger comparison. These boundary cases are where the Limit Comparison Test and the Direct Comparison Test are often combined: you use the Limit Comparison Test to identify the right growth rate, and then fall back to direct comparison or a known test if the limit is degenerate.

The Limit Comparison Test is most useful when the Direct Comparison Test fails because the termwise inequality goes the wrong way. For example, if Σ1/n diverges but you cannot directly show your series has terms larger than 1/n (perhaps the inequality reverses for some small n), the Limit Comparison Test sidesteps the problem — the eventual proportionality is all that matters. This makes it one of the most versatile convergence tests for series with rational or algebraic terms.
