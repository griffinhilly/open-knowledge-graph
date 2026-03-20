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
stage: advanced
status: draft
---

# Fatou's Lemma

## Core Idea
For non-negative measurable functions, ∫(liminf fₙ) ≤ liminf ∫fₙ. This weaker result than dominated convergence requires no dominating function. Fatou's lemma is essential for many existence proofs in functional analysis.

## Explainer

From your work with the Lebesgue integral for non-negative functions, you know that integration behaves well under limits in some cases — the Monotone Convergence Theorem says that if fₙ increases pointwise, the integrals converge in step. But what if the sequence oscillates? What if there's no monotonicity and no dominating function? Fatou's Lemma gives the answer in complete generality for non-negative measurable functions: ∫(liminf fₙ) ≤ liminf ∫fₙ. You can always integrate the eventual lower envelope, but the inequality only goes one way — you may lose mass, but you cannot gain it.

The **liminf** (limit inferior) of a sequence of functions fₙ is defined pointwise: (liminf fₙ)(x) = lim_{n→∞} inf_{k≥n} fₖ(x). It represents the "eventual lower envelope" — the largest function that is ≤ fₙ for all sufficiently large n. A canonical example illustrates why Fatou's inequality is strict: let fₙ = χ_{[n, n+1]} on ℝ with Lebesgue measure. Each fₙ has integral 1. But for any fixed x, fₙ(x) = 0 eventually (once n > x), so liminf fₙ = 0 everywhere, and ∫(liminf fₙ) = 0. The inequality reads 0 ≤ 1 — correct, but strict. The mass "escaped to +∞" and was never captured by the limit function.

Non-negativity is not optional. Without fₙ ≥ 0, the conclusion can fail in both directions. Consider gₙ = −χ_{[n,n+1]}: each integral is −1, but liminf gₙ = 0 everywhere, so ∫(liminf gₙ) = 0 > −1 = liminf ∫gₙ, and the inequality reverses. This is why Fatou's Lemma is stated for non-negative functions and why the Dominated Convergence Theorem — which restores equality — must impose a dominating function: the dominator prevents mass from escaping to infinity, converting the inequality into equality.

In practice, Fatou's Lemma is rarely used to compute integrals. Instead, it is a proof tool. The typical application pattern: you have a sequence of non-negative functions and know bounds on their integrals, but cannot control their pointwise limit directly. Fatou's Lemma gives you a bound on the integral of the limiting function for free, with no additional hypotheses beyond non-negativity. It appears in existence proofs — showing that a limit function is integrable — and in establishing lower semicontinuity of integral functionals. Think of it as the measure-theoretic principle of conservation: mass cannot appear from nowhere in the limit, but it can disappear.
