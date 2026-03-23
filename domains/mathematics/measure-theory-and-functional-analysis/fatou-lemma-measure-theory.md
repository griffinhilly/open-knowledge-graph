---
id: fatou-lemma-measure-theory
title: Fatou's Lemma
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-non-negative
  type: hard
builds-toward:
- dominated-convergence-theorem
tags:
- convergence-theorems
stage: expert
status: validated
---

# Fatou's Lemma

## Core Idea
For non-negative measurable functions, ∫(liminf fₙ) ≤ liminf ∫fₙ. This weaker result than dominated convergence requires no dominating function. Fatou's lemma is essential for many existence proofs in functional analysis.

## Questions

```yaml
- question: "Let fₙ = χ_{[n, n+1]} (the indicator function of the interval [n, n+1]) on ℝ with Lebesgue measure. Each fₙ has integral 1. What is ∫(liminf fₙ)?"
  type: multiple-choice
  options:
    - "1, because every fₙ integrates to 1 and the liminf should preserve this"
    - "∞, because infinitely many fₙ each contribute integral 1"
    - "0, because for any fixed x the value fₙ(x) = 0 eventually, so liminf fₙ = 0 everywhere"
    - "1/2, because the liminf averages the long-run behavior of the sequence"
  answer: 2
  explanation: "For any fixed x ∈ ℝ, once n > x we have x ∉ [n, n+1], so fₙ(x) = 0. Thus liminf fₙ(x) = 0 for every x, and the liminf function is identically zero. Its integral is 0. This is the canonical example of Fatou's strict inequality: ∫(liminf fₙ) = 0 ≤ 1 = liminf ∫fₙ. The mass did not disappear from the functions — it escaped to +∞, swept rightward out of every bounded region and therefore lost from the limiting function."

- question: "Fatou's Lemma states ∫(liminf fₙ) ≤ liminf ∫fₙ. Why can the inequality be strict rather than an equality?"
  type: multiple-choice
  options:
    - "Because liminf is a strictly weaker operation than lim for sequences"
    - "Because mass can escape to infinity in the limit — the integral of the limiting function can be less than the limiting value of the integrals when mass 'runs away' to remote regions"
    - "Because the Lebesgue integral is not countably additive for infinite sequences of functions"
    - "Because non-negative functions do not have well-defined liminfs pointwise"
  answer: 1
  explanation: "The canonical example (indicator functions sweeping rightward) shows what strict inequality means: the functions always have integral 1, but in the limit no mass is captured — it has escaped to +∞. The liminf function is identically 0. This 'loss of mass' is real: the sequence of integrals stays at 1, but the integral of the limit function drops to 0. Fatou guarantees you can't gain mass in the limit; it cannot prevent you from losing it. The Dominated Convergence Theorem restores equality by imposing a dominating function that prevents this escape."

- question: "Fatou's Lemma holds for any sequence of measurable functions, as long as the functions are measurable."
  type: true-false
  answer: false
  explanation: "Non-negativity is an essential hypothesis, not a technical convenience. For functions taking negative values, the conclusion can fail dramatically. Consider gₙ = −χ_{[n,n+1]}: each integral is −1, but liminf gₙ = 0 everywhere (same reasoning as the positive case), giving ∫(liminf gₙ) = 0 > −1 = liminf ∫gₙ. The inequality reverses — the wrong direction entirely. Non-negativity is what prevents mass from escaping to −∞, where the lower-bound reasoning of Fatou's proof breaks down."

- question: "Fatou's Lemma is primarily useful as a tool for directly computing integrals of limit functions."
  type: true-false
  answer: false
  explanation: "Fatou's Lemma is a proof tool, not a computational one. It produces an inequality — ∫(liminf fₙ) ≤ liminf ∫fₙ — not an equality, so it cannot directly compute a limit integral. In practice, it appears in existence proofs (showing a limit function has a finite integral given bounds on the sequence's integrals) and in establishing lower semicontinuity of integral functionals. For actual computation of ∫(lim fₙ), you need Monotone Convergence or Dominated Convergence, which impose stronger conditions in exchange for an equality."

- question: "State Fatou's Lemma informally and explain the intuitive reason why the inequality only goes one direction — why mass can be lost but not gained in the limit."
  type: short-answer
  answer: "For a sequence of non-negative measurable functions, the integral of the eventual lower envelope is at most the eventual lower limit of the integrals: ∫(liminf fₙ) ≤ liminf ∫fₙ. The inequality goes one way because mass can escape to infinity — as in functions that sweep rightward, carrying their mass to regions that no fixed point ever reaches — but mass cannot appear from nowhere in the limit. The limit function can only 'see' mass that stays in bounded regions; mass that runs to infinity is genuinely lost. Conservation holds in one direction: you cannot create mass in the limit. But you can lose it."
  explanation: "Think of it as a measure-theoretic conservation principle: the eventual lower envelope is the most mass the limit function can carry, and that is bounded above by how much mass was present in the sequence. The asymmetry (can lose, cannot gain) is why the inequality is ≤ rather than ≥ or =."
```

## Explainer

From your work with the Lebesgue integral for non-negative functions, you know that integration behaves well under limits in some cases — the Monotone Convergence Theorem says that if fₙ increases pointwise, the integrals converge in step. But what if the sequence oscillates? What if there's no monotonicity and no dominating function? Fatou's Lemma gives the answer in complete generality for non-negative measurable functions: ∫(liminf fₙ) ≤ liminf ∫fₙ. You can always integrate the eventual lower envelope, but the inequality only goes one way — you may lose mass, but you cannot gain it.

The **liminf** (limit inferior) of a sequence of functions fₙ is defined pointwise: (liminf fₙ)(x) = lim_{n→∞} inf_{k≥n} fₖ(x). It represents the "eventual lower envelope" — the largest function that is ≤ fₙ for all sufficiently large n. A canonical example illustrates why Fatou's inequality is strict: let fₙ = χ_{[n, n+1]} on ℝ with Lebesgue measure. Each fₙ has integral 1. But for any fixed x, fₙ(x) = 0 eventually (once n > x), so liminf fₙ = 0 everywhere, and ∫(liminf fₙ) = 0. The inequality reads 0 ≤ 1 — correct, but strict. The mass "escaped to +∞" and was never captured by the limit function.

Non-negativity is not optional. Without fₙ ≥ 0, the conclusion can fail in both directions. Consider gₙ = −χ_{[n,n+1]}: each integral is −1, but liminf gₙ = 0 everywhere, so ∫(liminf gₙ) = 0 > −1 = liminf ∫gₙ, and the inequality reverses. This is why Fatou's Lemma is stated for non-negative functions and why the Dominated Convergence Theorem — which restores equality — must impose a dominating function: the dominator prevents mass from escaping to infinity, converting the inequality into equality.

In practice, Fatou's Lemma is rarely used to compute integrals. Instead, it is a proof tool. The typical application pattern: you have a sequence of non-negative functions and know bounds on their integrals, but cannot control their pointwise limit directly. Fatou's Lemma gives you a bound on the integral of the limiting function for free, with no additional hypotheses beyond non-negativity. It appears in existence proofs — showing that a limit function is integrable — and in establishing lower semicontinuity of integral functionals. Think of it as the measure-theoretic principle of conservation: mass cannot appear from nowhere in the limit, but it can disappear.
