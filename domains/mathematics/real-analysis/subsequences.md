---
id: subsequences
title: Subsequences
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
builds-toward:
- bolzano-weierstrass-theorem
- limit-superior-and-inferior
tags:
- subsequences
- convergence
- selections
stage: advanced
status: validated
---

# Subsequences

## Core Idea
A subsequence of (aₙ) is a sequence (aₙₖ) where n₁ < n₂ < n₃ < ... A key fact: if (aₙ) converges to L, then every subsequence converges to L. Conversely, existence of convergent subsequences is a weaker property that allows us to extract convergence from non-convergent sequences.

## How It's Best Learned
Given (-1)ⁿ, identify its convergent subsequences: a₂ₖ → 1 and a₂ₖ₊₁ → -1. Extract a convergent subsequence from sin(n): though sin(n) oscillates chaotically, Bolzano-Weierstrass guarantees a convergent sub-sequence exists.

## Common Misconceptions
- Thinking a subsequence must be 'regular' (e.g., every other term); any selection with increasing indices counts.
- Assuming if a sequence diverges, no subsequence converges.
- Confusing the order: convergence ⟹ all subsequences converge, but not vice versa.

## Questions

```yaml
- question: "The sequence (aₙ) = (−1)ⁿ does not converge. Which subsequence-based argument best demonstrates this?"
  type: multiple-choice
  options:
    - "The sequence is bounded, so by Bolzano-Weierstrass it cannot converge"
    - "The even-indexed subsequence a₂ₖ converges to 1 and the odd-indexed subsequence a₂ₖ₊₁ converges to −1; since these limits differ, the original sequence cannot converge"
    - "The sequence has no convergent subsequences, which is sufficient to prove divergence"
    - "The sequence is not eventually monotone, so it fails the criterion for convergence in ℝ"
  answer: 1
  explanation: "If a sequence converges to L, every subsequence must converge to L. So if two subsequences converge to different limits, no single L can satisfy the definition — the original sequence cannot converge. The even-indexed terms of (−1)ⁿ are all 1, converging to 1; the odd-indexed terms are all −1, converging to −1. These limits are different, which is a contradiction with any proposed limit L. This is the standard proof technique: find two subsequences with distinct limits to certify divergence."

- question: "Suppose every convergent subsequence of a bounded sequence (aₙ) converges to the same value L. Does (aₙ) necessarily converge to L?"
  type: multiple-choice
  options:
    - "No — a sequence can have all subsequences converge to L while the original sequence diverges, as long as some terms wander far from L"
    - "Yes — if every convergent subsequence converges to L, then (aₙ) itself converges to L"
    - "Only if the sequence is monotone in addition to being bounded"
    - "Only if L = 0, since non-zero limits require stronger conditions"
  answer: 1
  explanation: "If (aₙ) did not converge to L, there would exist an ε > 0 and infinitely many terms with |aₙ − L| ≥ ε. Those infinitely many terms form a subsequence that stays away from L. Since (aₙ) is bounded, Bolzano-Weierstrass guarantees this 'bad' subsequence has a convergent sub-subsequence — but that sub-subsequence converges to some limit other than L (since its terms are all at distance ≥ ε from L). This contradicts the assumption that every convergent subsequence converges to L. Therefore (aₙ) must converge to L."

- question: "If a sequence (aₙ) diverges, then no subsequence of (aₙ) can converge."
  type: true-false
  answer: false
  explanation: "This is a common and important misconception. A divergent sequence can have many convergent subsequences — it just cannot have all of them converge to the same limit (which would force convergence of the full sequence). The sequence (−1)ⁿ diverges, yet a₂ₖ → 1 and a₂ₖ₊₁ → −1 are both convergent subsequences. More dramatically, Bolzano-Weierstrass guarantees that every bounded sequence (whether convergent or not) has at least one convergent subsequence. Divergence means the whole sequence fails to settle on a limit, not that it has no structured parts."

- question: "If a sequence (aₙ) converges to L, then the subsequence formed by taking only the even-indexed terms (a₂, a₄, a₆, ...) must also converge to L."
  type: true-false
  answer: true
  explanation: "This is a direct application of the theorem that convergence implies every subsequence converges to the same limit. The even-indexed subsequence (a₂ₖ) has indices n₁=2 < n₂=4 < n₃=6 < ..., which is a valid strictly increasing sequence of indices. By definition, for any ε > 0, there exists N such that all n ≥ N satisfy |aₙ − L| < ε. Since nₖ = 2k → ∞, eventually every nₖ ≥ N, so |a₂ₖ − L| < ε for all sufficiently large k. The same argument applies to any subsequence, not just even-indexed ones."

- question: "Explain why the existence of two subsequences converging to different limits proves that the original sequence diverges."
  type: short-answer
  answer: "The theorem states: if aₙ → L, then every subsequence converges to L. Contrapositive: if some subsequence does NOT converge to L, then aₙ does not converge to L. If two subsequences converge to different values L₁ ≠ L₂, then no matter what value L is proposed as the limit of the original sequence, at least one subsequence (the one converging to the other value) fails to converge to L. Since the original sequence would require all subsequences to agree on L, and none can, the original sequence cannot converge to any limit."
  explanation: "This argument uses the contrapositive of a key theorem and is the standard technique for proving divergence via subsequences. It is more elegant than ε-N arguments for oscillating sequences because it reduces the problem to showing that two parts of the sequence settle near different values — often geometrically obvious. The method also reveals the structure of divergence: the sequence is not 'going to infinity' but is being pulled in multiple directions simultaneously, which is precisely what subsequences with different limits capture."
```

## Explainer

From your work on **ε-N convergence**, you know what it means for a sequence (aₙ) to converge to a limit L: for every ε > 0, all sufficiently far-out terms stay within ε of L. A **subsequence** is obtained by selecting an infinite subset of the original sequence's terms, preserving their original order. Formally, you choose a strictly increasing sequence of indices n₁ < n₂ < n₃ < ... and form the new sequence (aₙ₁, aₙ₂, aₙ₃, ...). The key word is *strictly increasing indices* — you can skip terms, but you cannot reorder them or repeat them.

The first major fact is that convergence is inherited by all subsequences: if aₙ → L, then every subsequence also converges to L. The ε-N proof is almost immediate — if all terms from index N onward are within ε of L, then in particular the subsequence terms with nₖ ≥ N are within ε of L, and since nₖ → ∞, eventually every nₖ ≥ N. The converse direction is more powerful and surprising: if you can find *two* subsequences that converge to *different* limits, the original sequence cannot converge. This is why (−1)ⁿ diverges — the even-indexed terms converge to 1 and the odd-indexed terms converge to −1, which is a contradiction with any single limit L.

The deeper use of subsequences is extracting convergence from sequences that do not themselves converge. A bounded sequence in ℝ need not converge — consider (sin n), which oscillates chaotically and never settles — but it cannot escape to infinity either. The **Bolzano-Weierstrass theorem**, which you will encounter next, guarantees that every bounded sequence in ℝ has at least one convergent subsequence. This means bounded sequences always contain "convergent pieces" even if the whole sequence misbehaves. Subsequences are the tool for identifying those pieces.

Think of it as a filtering operation. The original sequence might contain too much noise to see a limit. A subsequence is a principled act of selective attention — you choose the terms that exhibit the behavior you are studying and ignore the rest. The richness of a sequence's behavior can be read off from its convergent subsequences: their limit points are exactly the **limit superior** and **limit inferior**, which tell you the highest and lowest values the sequence accumulates near. Subsequences thus give you a vocabulary for describing not just whether a sequence converges, but *how* it fails to converge — and that vocabulary is essential throughout real analysis and topology.
