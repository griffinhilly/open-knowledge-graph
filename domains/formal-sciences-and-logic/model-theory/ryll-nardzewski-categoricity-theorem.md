---
id: ryll-nardzewski-categoricity-theorem
title: 'Ryll-Nardzewski Theorem: Syntactic Characterization of Categoricity'
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: vaught-theorem-on-models
  type: hard
- id: type-spaces-and-stone-topology
  type: hard
builds-toward:
- morleys-uncountable-categoricity
tags:
- Ryll-Nardzewski
- categoricity
- complete-type
- characterization
stage: advanced
status: draft
---

# Ryll-Nardzewski Theorem: Syntactic Characterization of Categoricity

## Core Idea
A countably infinite complete theory T is κ-categorical (has exactly one model of cardinality κ) if and only if for every n, T has only finitely many complete n-types. This theorem provides a syntactic characterization of categoricity in terms of type spaces and is a precursor to Morley's more general categoricity theorem.

## Explainer

From your study of Vaught's theorem and type spaces, you know that a complete type over a theory T is a maximal consistent set of formulas in finitely many free variables — a complete description of how a tuple of elements could behave. The **Stone topology** makes the collection of all n-types into a compact, totally disconnected topological space, where the basic open sets are determined by individual formulas. When this space is finite, its topology is discrete and all types are **isolated** (each type is itself an open set, equivalent to being the unique type consistent with a single formula).

The Ryll-Nardzewski theorem says: a countably infinite complete theory T is **ω-categorical** (has exactly one countable model up to isomorphism) if and only if for each n ≥ 1, the space S_n(T) of complete n-types is finite. This is a striking equivalence between a structural property of models (uniqueness up to isomorphism) and a combinatorial property of formulas (finite type-count). The "only finitely many n-types" condition means there are only finitely many ways any n-tuple of elements can behave — the theory is combinatorially tame.

To see the intuition behind the forward direction: if T is ω-categorical, then the automorphism group of the unique countable model M acts on M^n with only finitely many orbits (by the Ryll-Nardzewski theorem's equivalent formulation in terms of oligomorphic groups). Two n-tuples with the same orbit realize the same complete type. Finitely many orbits implies finitely many types. Conversely, when T has only finitely many n-types, every type is isolated — there is a formula φ(x₁, …, xₙ) that uniquely determines the complete type of any tuple satisfying it. Isolated types are realized in every model by the omitting types theorem's dual, and with finitely many types to realize, all countable models end up with the same structure.

The prototype is the theory of the dense linear order without endpoints (DLO), whose unique countable model is the rationals ℚ. Every finite tuple of rationals is described (up to automorphism) entirely by the order type of its elements — there are finitely many such order types for each n, confirming finite type-count. The Ryll-Nardzewski theorem turns this example into a theorem: ω-categoricity is exactly the finite type-count condition, and theories satisfying it are the "most classifiable" in the countable setting. This sets the stage for Morley's deeper question about categoricity in uncountable cardinalities.
