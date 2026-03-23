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
stage: expert
status: validated
---

# Spectrum of a Theory and Vaught's Conjecture

## Core Idea
The spectrum I(κ, T) of a theory T counts the number of non-isomorphic models of T of cardinality κ. Vaught's conjecture (still open) states that for countable theories, I(ℵ₀, T) is either countable or ℵ₁. The spectrum determines much about the theory: stable theories have controlled spectrum growing polynomially, while unstable theories can have wild spectra.

## How It's Best Learned
Compute spectrum for simple theories: the theory of dense linear orders has I(ℵ₀, T) = 1. Study how spectrum changes under theory extensions.

## Questions

```yaml
- question: "A complete countable theory T has infinitely many non-isomorphic countable models. What does Vaught's conjecture assert about I(ℵ₀, T)?"
  type: multiple-choice
  options:
    - "I(ℵ₀, T) must equal ℵ₁, the first uncountable cardinal"
    - "I(ℵ₀, T) cannot equal ℵ₁ — it must be either at most ℵ₀ or exactly 2^ℵ₀"
    - "I(ℵ₀, T) can be any cardinal between ℵ₀ and 2^ℵ₀"
    - "I(ℵ₀, T) must equal 2^ℵ₀ once it exceeds ℵ₀"
  answer: 1
  explanation: "Vaught's conjecture (1961, still open) asserts that for a complete countable theory, the number of countable models up to isomorphism cannot be exactly ℵ₁. It must be either countable (≤ ℵ₀) or maximal (2^ℵ₀). The conjecture is striking precisely because ℵ₁ is the 'obvious' intermediate value between ℵ₀ and 2^ℵ₀, and it is this natural candidate that is claimed to be forbidden."

- question: "For uncountable cardinals κ, which values can I(κ, T) take for a complete first-order theory T?"
  type: multiple-choice
  options:
    - "Any cardinal from 0 up to 2^κ, depending on the complexity of T"
    - "Only 0, 1, or 2^κ — no intermediate values are possible"
    - "Only ℵ₀ or 2^κ, since uncountable models are either few or many"
    - "Any infinite cardinal ≤ 2^κ, but never 0"
  answer: 1
  explanation: "At uncountable cardinals, the spectrum is severely constrained: I(κ, T) can only be 0 (no model of that size), 1 (categoricity — exactly one model up to isomorphism), or 2^κ (the maximum). There is no middle ground. This 'all or nothing' structure at uncountable cardinalities has no analogue at ℵ₀, where the countable spectrum is far richer and more mysterious."

- question: "Morley's theorem implies that if a complete countable theory is categorical in some uncountable cardinal, it is categorical in all uncountable cardinals."
  type: true-false
  answer: true
  explanation: "Morley's theorem (1965) is one of the landmark results in model theory and states exactly this. Uncountable categoricity is a robust global property: it cannot hold at some uncountable cardinals and fail at others. This is the 'all or nothing' behavior at uncountable cardinals — a stark contrast to the countable case, where the spectrum can vary in complex ways."

- question: "A stable theory can have spectrum I(κ, T) = 2^κ at many uncountable cardinals, just like an unstable theory."
  type: true-false
  answer: false
  explanation: "Stable theories have tightly controlled spectra. At uncountable cardinals, their model counts are bounded by a polynomial in the cofinality of the cardinal — far below the maximum 2^κ. Unstable theories, by contrast, can achieve I(κ, T) = 2^κ at many cardinals. Stability, which reflects deep combinatorial properties (order properties, type definability), is precisely what prevents the spectrum from exploding to its maximum value."

- question: "Why is ℵ₁ considered the 'obvious' intermediate value that Vaught's conjecture claims is forbidden, and why would its existence be surprising from the perspective of model theory?"
  type: short-answer
  answer: "ℵ₁ is the first uncountable cardinal and sits immediately between ℵ₀ and 2^ℵ₀ (assuming the continuum hypothesis fails, 2^ℵ₀ > ℵ₁). A theory with exactly ℵ₁ countable models would be neither 'tame' (finitely many or countably many models) nor 'wild' (as many as possible). Vaught's conjecture asserts this intermediate complexity is forbidden — there is no 'medium' regime for countable model counts. Its existence would suggest a kind of combinatorial structure in the models that doesn't fit either the controlled behavior of ω-stable theories or the maximal complexity of unstable ones."
  explanation: "The conjecture has deep connections to the descriptive set-theoretic complexity of the isomorphism relation on countable models. If I(ℵ₀, T) = ℵ₁, the set of countable models (up to isomorphism) would have a Borel-but-non-analytic character that current model-theoretic tools cannot produce. This is why the conjecture remains open after 60+ years — it requires combining model theory with descriptive set theory in ways that are not yet fully understood."
```

## Explainer

You know from the Löwenheim-Skolem theorems that a complete first-order theory with an infinite model has models of every infinite cardinality. This raises a finer question: how many non-isomorphic models does the theory have of each cardinality? The answer, encoded in the **spectrum** I(κ, T), turns out to be a remarkably sensitive invariant of the theory — a kind of fingerprint that reflects its logical complexity.

The spectrum function I(κ, T) counts non-isomorphic models of T of cardinality κ. For a given uncountable cardinal κ, the possible values of I(κ, T) are severely constrained: it must be 0 (no model of that size), 1 (exactly one up to isomorphism — **categoricity**), or 2^κ (the maximum). These are the only possibilities for uncountable cardinals — there is no middle ground. Morley's theorem (a landmark result in model theory) shows that if T is categorical in some uncountable cardinal, it is categorical in all uncountable cardinals. This "all or nothing" behavior at uncountable cardinals has no analogue at ℵ₀.

The countable case is far richer and more mysterious. I(ℵ₀, T) — the number of countable models up to isomorphism — can be 1, n (for small n), ℵ₀, or 2^ℵ₀. **Vaught's conjecture** (1961, still open) asserts it cannot be exactly ℵ₁ — the number of countable models of a complete countable theory is either at most ℵ₀ or exactly 2^ℵ₀. The conjecture has been verified for many special classes of theories (ω-stable theories, certain expansions of linear orders), but the general case remains one of the deepest open problems in mathematical logic. The conjecture is striking because ℵ₁ is the "obvious" intermediate value between ℵ₀ and 2^ℵ₀, and the conjecture says this obvious value is forbidden.

The spectrum connects to **stability theory**: a theory is **stable** if, roughly, its models do not have too many types. Stable theories have tightly controlled spectra — at uncountable cardinals the number of models is bounded by a polynomial in the cardinal's cofinality. **Unstable** theories can have spectrum I(κ, T) = 2^κ at many cardinals, the maximum. Stability is not just a counting statement — it reflects deep combinatorial properties of the models (order properties, definability of types, existence of prime models). The spectrum is thus the observable output of a much richer theory about how models of a theory can differ from one another.
