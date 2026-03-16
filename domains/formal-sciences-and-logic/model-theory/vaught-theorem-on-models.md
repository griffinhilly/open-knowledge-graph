---
id: vaught-theorem-on-models
title: Vaught's Theorem on Number of Countable Models
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: countable-model-existence
  type: hard
- id: spectrum-and-number-of-models
  type: soft
builds-toward:
- ryll-nardzewski-categoricity-theorem
tags:
- Vaught
- countable-models
- spectrum
- cardinality-bound
stage: abstract-reasoning
status: draft
---

# Vaught's Theorem on Number of Countable Models

## Core Idea
Vaught's theorem establishes an upper bound on the number of countable models of a complete theory: the number is either 1 (categorical) or ≥ ℵ₀. There is no complete theory with exactly 2 countable models. This surprising rigidity reflects the discreteness of first-order logic and is a key result in counting models.

## Explainer

From your study of countable models, you know that a complete first-order theory always has at least one countable model (by the downward Löwenheim-Skolem theorem). From the spectrum of a theory, you may have studied how many non-isomorphic models a theory can have at a given cardinality. **Vaught's theorem** is a striking constraint on this count at the countable level: the number of non-isomorphic countable models of a complete theory can never equal exactly 2.

The result is counterintuitive. You might expect that by tuning a theory's axioms you could produce exactly 2 distinct countable structures. Vaught's theorem says no: the count is either 1 (the theory is **ℵ₀-categorical**, all countable models are isomorphic to each other), or it is at least ℵ₀. The argument proceeds through **types** — maximal consistent sets of formulas in one free variable that describe the possible "behavior" of a single element in a model. Two countable models are non-isomorphic exactly when they realize different collections of types. The key insight is that if a type is not isolated (not implied by a single formula of the theory), then omitting or realizing it generates further choices, each spawning more non-isomorphic models — and this cascade cannot stop at exactly 2.

To see the intuition more concretely: suppose a theory has two non-isomorphic countable models M and N. The difference between them is witnessed by some non-isolated type p that is realized in one but not the other. But the theory's combinatorial structure means there are infinitely many "variants" of p — partial types extending it in incompatible directions, each realizable in some countable model. The **Omitting Types Theorem** guarantees that any non-isolated type can be omitted in a countable model; conversely, isolated types must be realized. The interaction between isolated and non-isolated types therefore generates infinitely many distinct realizations, ruling out a count of exactly 2.

Vaught's theorem motivates **Vaught's conjecture**, one of the most important open problems in model theory: must the number of countable models of a complete theory be either at most ℵ₀ or exactly 2^ℵ₀? (Under the continuum hypothesis these are the only options anyway; the question is non-trivial when CH fails.) The conjecture has been proved for special classes of theories (ω-stable theories, theories without the independence property) but remains open in general. Vaught's theorem is thus the opening move in a deep classification project for first-order structures, revealing that the spectrum of countable models obeys unexpectedly rigid constraints.
