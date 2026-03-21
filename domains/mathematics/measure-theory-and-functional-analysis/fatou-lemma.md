---
id: fatou-lemma
title: Fatou's Lemma
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-properties
  type: hard
builds-toward:
- dominated-convergence-theorem
tags:
- convergence-theorems
stage: advanced
status: draft
---

# Fatou's Lemma

## Core Idea
For any sequence of non-negative measurable functions, ∫liminf fₙ dμ ≤ liminf ∫fₙ dμ. Unlike the Monotone Convergence Theorem, Fatou's Lemma applies to non-monotone sequences without boundedness assumptions, making it more universally applicable.

## Questions

```yaml
- question: "Let fₙ = n · 1_{[0,1/n]} on [0,1] with Lebesgue measure (a spike of height n and width 1/n). Each ∫fₙ dμ = 1 and the pointwise lim inf of fₙ is 0 everywhere. What does Fatou's Lemma say about this sequence?"
  type: multiple-choice
  options:
    - "∫lim inf fₙ dμ = lim inf ∫fₙ dμ, so 0 = 1 — a contradiction showing the lemma fails here"
    - "∫lim inf fₙ dμ ≤ lim inf ∫fₙ dμ, so 0 ≤ 1 — the inequality holds with strict inequality"
    - "∫lim inf fₙ dμ ≥ lim inf ∫fₙ dμ, so 0 ≥ 1 — showing the functions are not admissible"
    - "Nothing — Fatou's Lemma only applies to monotone sequences"
  answer: 1
  explanation: "Fatou's Lemma guarantees ∫lim inf fₙ dμ ≤ lim inf ∫fₙ dμ. Here, lim inf fₙ = 0 pointwise (the spike concentrates in a region of width 1/n → 0), so ∫0 dμ = 0. And lim inf ∫fₙ = lim inf 1 = 1. We get 0 ≤ 1 — the inequality holds with strict inequality. This is the canonical example showing the inequality can be *strict*: mass has 'escaped to infinity' as the spikes narrow. Fatou does not claim equality; it only bounds the integral of the lim inf. Option D is wrong — Fatou requires only non-negativity and measurability, not monotonicity."

- question: "Fatou's Lemma applies more broadly than the Monotone Convergence Theorem. What is the key difference in assumptions between the two results?"
  type: multiple-choice
  options:
    - "The MCT requires Lebesgue integration; Fatou's Lemma works for Riemann integration as well"
    - "Fatou's Lemma requires only non-negative measurable functions; the MCT additionally requires the sequence to be non-decreasing"
    - "The MCT applies to any sequence; Fatou's Lemma requires the sequence to converge pointwise"
    - "Fatou's Lemma requires a dominating integrable function; the MCT does not"
  answer: 1
  explanation: "The MCT requires the sequence to be non-decreasing (fₙ ≤ fₙ₊₁ a.e.) as well as non-negative, and under these conditions delivers equality: ∫lim fₙ = lim ∫fₙ. Fatou's Lemma requires only non-negativity — no monotonicity, no boundedness, no pointwise convergence — and delivers only an inequality. This weaker conclusion from weaker assumptions is what makes Fatou applicable in far more general situations. The dominating function assumption belongs to the Dominated Convergence Theorem, not Fatou."

- question: "There exist sequences of non-negative measurable functions for which ∫lim inf fₙ dμ < lim inf ∫fₙ dμ strictly — Fatou's Lemma cannot be strengthened to an equality in general."
  type: true-false
  answer: true
  explanation: "The moving spike example (fₙ = n · 1_{[0,1/n]}) is the canonical counterexample: each ∫fₙ = 1, so lim inf ∫fₙ = 1, while the pointwise lim inf is 0 everywhere, giving ∫lim inf fₙ = 0. Strict inequality holds because mass 'escapes to infinity' — the functions concentrate their mass in vanishingly small regions where the limit function has no mass. This shows that without additional assumptions (like domination by an integrable function), the inequality in Fatou cannot be improved to equality."

- question: "Fatou's Lemma requires the sequence fₙ to converge pointwise to a function f before the inequality ∫lim inf fₙ dμ ≤ lim inf ∫fₙ dμ can be applied."
  type: true-false
  answer: false
  explanation: "Fatou's Lemma requires only that the functions fₙ are non-negative and measurable — no pointwise convergence is needed. The lim inf in the statement handles the non-convergent case: lim inf fₙ(x) is defined for every sequence of real numbers, even if the sequence does not converge. The function g(x) = lim inf fₙ(x) is always well-defined and measurable for measurable fₙ. This is what makes Fatou so broadly applicable: it handles oscillating, non-converging sequences that the MCT cannot. If fₙ happens to converge pointwise, then lim inf fₙ = lim fₙ = f, and Fatou reduces to ∫f ≤ lim inf ∫fₙ."

- question: "Explain why Fatou's Lemma cannot be upgraded to an equality in general — what phenomenon causes the strict inequality, and what additional assumption restores equality?"
  type: short-answer
  answer: "The strict inequality arises when 'mass escapes to infinity' — when the sequence concentrates positive integral mass in regions that shrink to zero measure, so the limiting function captures none of that mass. The moving spike fₙ = n · 1_{[0,1/n]} illustrates this: each function has integral 1, but the limit function is 0 everywhere, so the integral of the limit is 0 while the limit of the integrals is 1. The mass that each fₙ carries is in a region of width 1/n that collapses to a single point of measure zero. To restore equality — guaranteeing ∫lim fₙ = lim ∫fₙ — one needs to prevent this escape. The Dominated Convergence Theorem provides this by requiring |fₙ| ≤ g a.e. for some integrable dominating function g; the dominating function bounds where mass can concentrate and prevents it from escaping to zero-measure sets."
  explanation: "Fatou only controls the 'floor' — what mass must survive to the limit. It cannot control mass that escapes to sets where the limit is zero. The DCT solves this by imposing a ceiling (the dominating function) that keeps mass in regions where convergence can be tracked, allowing equality to be restored."
```

## Explainer

From your study of Lebesgue integral properties, you know that the integral is a "limit-friendly" operation in many situations — but not always. The core question in all convergence theorems is: when can you pass a limit through the integral sign, swapping ∫lim with lim∫? The Monotone Convergence Theorem answers this cleanly for increasing sequences. Fatou's Lemma gives a weaker but far more general answer for *any* sequence of non-negative functions: the integral of the limiting behavior is at most the limiting behavior of the integrals. The inequality goes one way, and that turns out to be enough.

The key concept to internalize is the **limit inferior** (lim inf). For a sequence of real numbers aₙ, the lim inf is the smallest accumulation point — the eventual floor below which the sequence stays infinitely often. For functions, lim inf fₙ(x) is defined pointwise: at each x, take the lim inf of the sequence of values fₙ(x). The function g(x) = lim inf fₙ(x) is measurable whenever the fₙ are, and Fatou's Lemma asserts ∫g dμ ≤ lim inf ∫fₙ dμ. Equality can fail: if fₙ "spikes" with a tall narrow bump that moves away to infinity, the integrals ∫fₙ might stay large while the pointwise lim inf is zero everywhere.

The proof strategy connects directly to the Monotone Convergence Theorem. Define gₙ(x) = inf{fₖ(x) : k ≥ n} — the running infimum. The sequence gₙ is non-decreasing and gₙ ≤ fₙ pointwise, so ∫gₙ dμ ≤ ∫fₙ dμ. Taking lim inf on the right: lim ∫gₙ dμ ≤ lim inf ∫fₙ dμ. But gₙ increases to lim inf fₙ pointwise, so by the Monotone Convergence Theorem, lim ∫gₙ dμ = ∫lim inf fₙ dμ. Chaining these inequalities gives the result. This proof pattern — constructing a monotone minorant and applying MCT — is one of the most reusable techniques in measure theory.

Fatou's Lemma is a workhorse for establishing the **Dominated Convergence Theorem**, which appears next in the curriculum. The DOM theorem needs Fatou applied twice (to fₙ and to 2g − fₙ for a dominating function g). More broadly, whenever you want to show that an integral is finite or bounded but cannot assume pointwise convergence, Fatou gives you a floor. The habit to build now: when you see ∫lim or lim∫ in a problem with non-negative functions, reach for Fatou's Lemma as the first tool to bound the integral of the limit.
