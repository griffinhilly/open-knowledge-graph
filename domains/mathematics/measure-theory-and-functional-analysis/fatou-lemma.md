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

## Explainer

From your study of Lebesgue integral properties, you know that the integral is a "limit-friendly" operation in many situations — but not always. The core question in all convergence theorems is: when can you pass a limit through the integral sign, swapping ∫lim with lim∫? The Monotone Convergence Theorem answers this cleanly for increasing sequences. Fatou's Lemma gives a weaker but far more general answer for *any* sequence of non-negative functions: the integral of the limiting behavior is at most the limiting behavior of the integrals. The inequality goes one way, and that turns out to be enough.

The key concept to internalize is the **limit inferior** (lim inf). For a sequence of real numbers aₙ, the lim inf is the smallest accumulation point — the eventual floor below which the sequence stays infinitely often. For functions, lim inf fₙ(x) is defined pointwise: at each x, take the lim inf of the sequence of values fₙ(x). The function g(x) = lim inf fₙ(x) is measurable whenever the fₙ are, and Fatou's Lemma asserts ∫g dμ ≤ lim inf ∫fₙ dμ. Equality can fail: if fₙ "spikes" with a tall narrow bump that moves away to infinity, the integrals ∫fₙ might stay large while the pointwise lim inf is zero everywhere.

The proof strategy connects directly to the Monotone Convergence Theorem. Define gₙ(x) = inf{fₖ(x) : k ≥ n} — the running infimum. The sequence gₙ is non-decreasing and gₙ ≤ fₙ pointwise, so ∫gₙ dμ ≤ ∫fₙ dμ. Taking lim inf on the right: lim ∫gₙ dμ ≤ lim inf ∫fₙ dμ. But gₙ increases to lim inf fₙ pointwise, so by the Monotone Convergence Theorem, lim ∫gₙ dμ = ∫lim inf fₙ dμ. Chaining these inequalities gives the result. This proof pattern — constructing a monotone minorant and applying MCT — is one of the most reusable techniques in measure theory.

Fatou's Lemma is a workhorse for establishing the **Dominated Convergence Theorem**, which appears next in the curriculum. The DOM theorem needs Fatou applied twice (to fₙ and to 2g − fₙ for a dominating function g). More broadly, whenever you want to show that an integral is finite or bounded but cannot assume pointwise convergence, Fatou gives you a floor. The habit to build now: when you see ∫lim or lim∫ in a problem with non-negative functions, reach for Fatou's Lemma as the first tool to bound the integral of the limit.
