---
id: radon-nikodym-theorem
title: Radon-Nikodym Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: measure-spaces
  type: hard
- id: lp-spaces
  type: soft
builds-toward:
- signed-measures-hahn-jordan
tags:
- measure-theory
stage: advanced
status: draft
---

# Radon-Nikodym Theorem

## Core Idea
If ν is σ-finite and absolutely continuous with respect to μ, then ∃h measurable: ν(A) = ∫_A h dμ. The Radon-Nikodym derivative dν/dμ = h formalizes differentiation of measures.

## Explainer

You have been working with measure spaces — sets X equipped with a σ-algebra and a measure μ that assigns sizes to measurable sets. Now suppose you have *two* measures on the same space: μ and ν. A natural question arises: when can ν be expressed in terms of μ? When can we write ν as "μ with a weight function"?

The key condition is **absolute continuity**: ν is absolutely continuous with respect to μ, written ν ≪ μ, if every μ-null set is also ν-null. That is, whenever μ(A) = 0, we also have ν(A) = 0. This says: ν cannot see anything that μ considers negligible. In probabilistic terms, if an event has probability zero under μ, it also has probability zero under ν. Absolute continuity is the precise condition under which ν is "dominated by" μ.

The **Radon-Nikodym theorem** says: if ν ≪ μ and both measures are σ-finite, then there exists a non-negative measurable function h such that ν(A) = ∫_A h dμ for every measurable set A. This function h is unique μ-almost everywhere, and we write it as dν/dμ — the **Radon-Nikodym derivative**. The name is deliberate: this is literally a derivative of one measure with respect to another. Just as the ordinary derivative df/dx tells you how f changes relative to x, the Radon-Nikodym derivative tells you how ν is distributed relative to μ.

A concrete example anchors the abstraction. In classical probability, if X has probability density function f(x) and we take μ to be Lebesgue measure, then P(A) = ∫_A f(x) dx for every measurable set A. In Radon-Nikodym language, P ≪ λ (Lebesgue) and dP/dλ = f. The density function you learned in probability theory is a Radon-Nikodym derivative! The theorem generalizes this: any absolutely continuous probability measure on Rⁿ has a density, and conversely. This also underlies conditional expectation in advanced probability: E[X | G] is the Radon-Nikodym derivative of a signed measure with respect to a restricted measure — a perspective that makes its properties (linearity, tower property) transparent.
