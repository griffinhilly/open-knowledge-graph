---
id: spectrum-and-number-of-models
title: Spectrum of a Theory and Vaught's Conjecture
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: complete-first-order-theories
  type: hard
- id: lowenheim-skolem-theorems-overview
  type: hard
builds-toward:
- morleys-uncountable-categoricity
- finite-axiomatization-and-completeness
tags:
- spectrum
- model-count
- vaught-conjecture
stage: advanced
status: draft
---

# Spectrum of a Theory and Vaught's Conjecture

## Core Idea
The spectrum I(κ, T) of a theory T counts the number of non-isomorphic models of T of cardinality κ. Vaught's conjecture (still open) states that for countable theories, I(ℵ₀, T) is either countable or ℵ₁. The spectrum determines much about the theory: stable theories have controlled spectrum growing polynomially, while unstable theories can have wild spectra.

## How It's Best Learned
Compute spectrum for simple theories: the theory of dense linear orders has I(ℵ₀, T) = 1. Study how spectrum changes under theory extensions.

## Explainer

You know from the Löwenheim-Skolem theorems that a complete first-order theory with an infinite model has models of every infinite cardinality. This raises a finer question: how many non-isomorphic models does the theory have of each cardinality? The answer, encoded in the **spectrum** I(κ, T), turns out to be a remarkably sensitive invariant of the theory — a kind of fingerprint that reflects its logical complexity.

The spectrum function I(κ, T) counts non-isomorphic models of T of cardinality κ. For a given uncountable cardinal κ, the possible values of I(κ, T) are severely constrained: it must be 0 (no model of that size), 1 (exactly one up to isomorphism — **categoricity**), or 2^κ (the maximum). These are the only possibilities for uncountable cardinals — there is no middle ground. Morley's theorem (a landmark result in model theory) shows that if T is categorical in some uncountable cardinal, it is categorical in all uncountable cardinals. This "all or nothing" behavior at uncountable cardinals has no analogue at ℵ₀.

The countable case is far richer and more mysterious. I(ℵ₀, T) — the number of countable models up to isomorphism — can be 1, n (for small n), ℵ₀, or 2^ℵ₀. **Vaught's conjecture** (1961, still open) asserts it cannot be exactly ℵ₁ — the number of countable models of a complete countable theory is either at most ℵ₀ or exactly 2^ℵ₀. The conjecture has been verified for many special classes of theories (ω-stable theories, certain expansions of linear orders), but the general case remains one of the deepest open problems in mathematical logic. The conjecture is striking because ℵ₁ is the "obvious" intermediate value between ℵ₀ and 2^ℵ₀, and the conjecture says this obvious value is forbidden.

The spectrum connects to **stability theory**: a theory is **stable** if, roughly, its models do not have too many types. Stable theories have tightly controlled spectra — at uncountable cardinals the number of models is bounded by a polynomial in the cardinal's cofinality. **Unstable** theories can have spectrum I(κ, T) = 2^κ at many cardinals, the maximum. Stability is not just a counting statement — it reflects deep combinatorial properties of the models (order properties, definability of types, existence of prime models). The spectrum is thus the observable output of a much richer theory about how models of a theory can differ from one another.
