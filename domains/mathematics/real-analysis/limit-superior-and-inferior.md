---
id: limit-superior-and-inferior
title: Limit Superior and Inferior
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
- id: subsequences
  type: hard
builds-toward:
- uniform-convergence-functions
tags:
- limsup
- liminf
- convergence
- oscillation
stage: advanced
status: draft
---

# Limit Superior and Inferior

## Core Idea
The limit superior (limsup) and limit inferior (liminf) of a sequence are the largest and smallest limit points of its subsequences, respectively. For any bounded sequence, liminf ≤ limsup, and equality holds if and only if the sequence converges. These tools allow precise analysis of oscillating sequences without traditional limits.

## Questions

```yaml
- question: "Consider the sequence aₙ = (−1)ⁿ + 1/n. What is lim sup aₙ?"
  type: multiple-choice
  options:
    - "+∞, because the sequence is unbounded"
    - "0, because 1/n → 0 and that is the only term that changes"
    - "1, because along even-indexed terms aₙ = 1 + 1/n → 1, and this is the largest value approached infinitely often"
    - "The limit superior does not exist for oscillating sequences"
  answer: 2
  explanation: "For even n, aₙ = 1 + 1/n, which approaches 1 from above. For odd n, aₙ = −1 + 1/n → −1. The tail supremum sup_{k≥n} aₖ is approximately 1 + 1/n (the even-indexed terms dominate), and this approaches 1 as n → ∞. So lim sup aₙ = 1. The key: lim sup is the largest value the sequence approaches infinitely often — not the largest value ever achieved. The lim inf = −1."

- question: "A student claims 'lim sup aₙ is just the supremum of the sequence — the largest value aₙ ever takes.' Which sequence disproves this?"
  type: multiple-choice
  options:
    - "aₙ = (−1)ⁿ — here sup = 1 and lim sup = 1, so they agree"
    - "aₙ = 1/n — here sup = 1 (the first term) but lim sup = 0, since 1 appears only finitely often and the sequence converges to 0"
    - "aₙ = n — here both sup and lim sup equal +∞, so they agree"
    - "aₙ = sin(n) — here both sup and lim sup equal 1"
  answer: 1
  explanation: "For aₙ = 1/n, the supremum is a₁ = 1, but lim sup aₙ = 0. The tail supremum sup_{k≥n} aₖ = 1/n → 0. The value 1 appears only once (at n=1) — lim sup ignores finitely-occurring values. It captures only the largest value the sequence approaches infinitely often — the largest limit point of any subsequence. This is fundamentally different from supremum, which is a one-time-maximum."

- question: "A sequence (aₙ) converges to L if and only if lim sup aₙ = lim inf aₙ = L."
  type: true-false
  answer: true
  explanation: "This is the fundamental characterization that makes lim sup and lim inf strictly more general than ordinary limits. If (aₙ) converges to L, every tail supremum and infimum approaches L, so limsup = liminf = L. Conversely, if limsup = liminf = L, the sequence is squeezed: for large n, all subsequent terms lie in an arbitrarily small interval around L, which is exactly ε-N convergence. Ordinary limits are the special case where the two extremes coincide."

- question: "For a bounded sequence, lim sup aₙ equals the supremum of all values the sequence takes."
  type: true-false
  answer: false
  explanation: "The lim sup is the largest LIMIT POINT (subsequential limit) — the largest value the sequence approaches infinitely often. The overall supremum may be achieved at just finitely many terms and then never approached again. For example, aₙ = 1/n has sup = 1 (attained at n=1) but lim sup = 0 (the only limit point). The lim sup effectively ignores transient large values and tracks only persistent accumulation points."

- question: "Why do the limit superior and inferior always exist for bounded sequences, even when the ordinary limit does not?"
  type: short-answer
  answer: "Define Mₙ = sup_{k≥n} aₖ (the tail supremum). As n increases, we're taking sup over a smaller set, so Mₙ is non-increasing. Since the sequence is bounded below, the non-increasing sequence (Mₙ) is also bounded below — by the monotone convergence theorem, it converges. This limit is the lim sup. Symmetrically, the tail infima mₙ = inf_{k≥n} aₖ form a non-decreasing bounded sequence that converges; this is the lim inf. The ordinary limit fails when these two limits are different (the sequence oscillates between multiple accumulation points), but each individually always converges."
  explanation: "This is why lim sup and lim inf are defined via tail operations and limits, not directly as 'largest value approached.' The construction via monotone sequences guarantees existence. The ordinary limit is just the special case where Mₙ and mₙ converge to the same value — a coincidence that fails for oscillating sequences."
```

## Explainer

From your work on ε-N convergence and subsequences, you know that a sequence (aₙ) converges to L if and only if every subsequence also converges to L. But what tools do you have when a sequence does not converge — when it oscillates or accumulates near multiple values? The **limit superior** and **limit inferior** are precisely the tools built for this situation.

The formal definition: lim sup aₙ = lim_{n→∞} sup_{k≥n} aₖ. In words, look at the "tail" of the sequence starting at index n, take the supremum of that tail, then let n grow. Each tail is a subset of the previous one, so the suprema form a non-increasing sequence — it always has a limit (possibly +∞ or −∞). This limit is the limsup. Symmetrically, lim inf aₙ = lim_{n→∞} inf_{k≥n} aₙ, and the infima form a non-decreasing sequence. The limsup captures the largest value the sequence "approaches arbitrarily closely, infinitely often"; the liminf captures the smallest such value.

The canonical example is aₙ = (−1)ⁿ. The sequence alternates between +1 and −1, never converging. Yet lim sup aₙ = 1: the tail sup is always 1 (since +1 appears in every tail), and lim inf aₙ = −1 (since −1 also appears in every tail). These are the two accumulation points of the sequence, and the limsup and liminf identify them exactly. Now recall your subsequence work: a value L is a limit point of (aₙ) if some subsequence converges to L. The limsup is the largest such L, and the liminf is the smallest. This is why the Core Idea's characterization holds: limsup = liminf if and only if every subsequence has the same limit, which is exactly convergence.

The power of these tools becomes clear in applications. The limsup appears naturally in the **ratio test** and **root test** for series convergence: you replace lim|aₙ₊₁/aₙ| with lim sup|aₙ₊₁/aₙ| to handle sequences where the ratio doesn't converge but is still bounded. In the theory of **uniform convergence** (which you'll encounter next), you'll use lim sup across a domain to define the sup-norm, the right measure of how close two functions are. Any time a classical limit fails to exist but you still need to make a quantitative statement about limiting behavior, lim sup and lim inf give you the language to do it. They are not a workaround for convergence — they are a strictly more general notion that reduces to the ordinary limit as a special case.
