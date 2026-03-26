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
- id: indiscernibles-and-morley-theorem
  type: soft
builds-toward:
- morleys-uncountable-categoricity
tags:
- Ryll-Nardzewski
- categoricity
- complete-type
- characterization
stage: expert
status: validated
---
# Ryll-Nardzewski Theorem: Syntactic Characterization of Categoricity

## Core Idea
A countably infinite complete theory T is κ-categorical (has exactly one model of cardinality κ) if and only if for every n, T has only finitely many complete n-types. This theorem provides a syntactic characterization of categoricity in terms of type spaces and is a precursor to Morley's more general categoricity theorem.

## Questions

```yaml
- question: "A complete theory T has infinitely many complete 2-types over the empty set. What does the Ryll-Nardzewski theorem immediately tell you?"
  type: multiple-choice
  options:
    - "T cannot be ω-categorical"
    - "T has no countable models"
    - "T is categorical in every uncountable cardinality"
    - "T has only finitely many 1-types"
  answer: 0
  explanation: "The Ryll-Nardzewski theorem says T is ω-categorical if and only if for each n, S_n(T) is finite. Infinitely many 2-types directly violates this condition for n=2, so T cannot be ω-categorical. The theorem does not say anything about uncountable cardinalities (that requires Morley's theorem), and infinitely many 2-types says nothing about 1-types."

- question: "The theory DLO (dense linear order without endpoints) is ω-categorical with unique countable model ℚ. For n=3, which best explains why finitely many 3-types exist?"
  type: multiple-choice
  options:
    - "Any 3-tuple of rationals is described, up to automorphism, entirely by the ordering of its elements — there are exactly 6 order types for 3 distinct elements"
    - "ℚ has only finitely many elements, so there are finitely many 3-tuples"
    - "DLO has no complete types because all its models are infinite"
    - "The Stone topology on S₃(DLO) is compact, so it has finitely many points"
  answer: 0
  explanation: "For any n-tuple of distinct rationals, the complete type is fully determined by the linear order among them — which of the n! orderings applies. For n=3 there are 6 permutations, giving at most 6 distinct 3-types (fewer if ties are allowed, but DLO excludes equality). This finite count is exactly why DLO satisfies the Ryll-Nardzewski condition. ℚ is infinite, compactness of the Stone space alone does not imply finiteness (an infinite compact space can still have infinitely many points), and 'no complete types' is wrong."

- question: "If a complete theory T is ω-categorical, then every complete n-type over ∅ is isolated — that is, there exists a single formula that uniquely determines the entire type."
  type: true-false
  answer: true
  explanation: "This is a key step in the Ryll-Nardzewski theorem. When S_n(T) is finite, the Stone topology on it is discrete, meaning every singleton {p} is open. In the Stone topology, open sets are unions of basic open sets of the form [φ] = {types containing φ}. A singleton being open means p = [φ] for some formula φ, i.e., φ isolates p. Isolated types are exactly those pinned by a single formula — so finite type count implies every type is isolated."

- question: "A theory that is ω-categorical is expected to also be categorical in nearly every uncountable cardinality, since having mainly finitely many n-types is a property of the theory regardless of cardinality."
  type: true-false
  answer: false
  explanation: "This is false. ω-categoricity is a property specifically about countable models, and the Ryll-Nardzewski theorem characterizes only ω-categoricity. Morley's theorem characterizes categoricity in uncountable cardinalities and requires a different condition (no Vaughtian pairs, totally transcendental). Many ω-categorical theories, including DLO itself, are not categorical in uncountable cardinalities — there are many non-isomorphic uncountable dense linear orders."

- question: "Why does having only finitely many complete n-types (for each n) force all countable models of T to be isomorphic? Explain the mechanism."
  type: short-answer
  answer: "When every type is isolated, the omitting types theorem's dual guarantees each type is realized in every model. With finitely many n-types, every countable model realizes exactly the same finite collection of types. A back-and-forth argument then constructs an isomorphism between any two countable models: at each stage, you can always extend a finite partial isomorphism because the type of any tuple is one of finitely many isolated types, all realized on both sides."
  explanation: "The key mechanism is: finite type count → every type isolated → every type realized in every model → back-and-forth succeeds. Isolated types are the bridge: a formula φ that isolates a type p means any model satisfying T contains a tuple realizing p (because T ⊨ ∃x φ(x)), and the type of that tuple is fully determined by φ. The back-and-forth argument exploits this to build an isomorphism step by step."
```

## Explainer

From your study of Vaught's theorem and type spaces, you know that a complete type over a theory T is a maximal consistent set of formulas in finitely many free variables — a complete description of how a tuple of elements could behave. The **Stone topology** makes the collection of all n-types into a compact, totally disconnected topological space, where the basic open sets are determined by individual formulas. When this space is finite, its topology is discrete and all types are **isolated** (each type is itself an open set, equivalent to being the unique type consistent with a single formula).

The Ryll-Nardzewski theorem says: a countably infinite complete theory T is **ω-categorical** (has exactly one countable model up to isomorphism) if and only if for each n ≥ 1, the space S_n(T) of complete n-types is finite. This is a striking equivalence between a structural property of models (uniqueness up to isomorphism) and a combinatorial property of formulas (finite type-count). The "only finitely many n-types" condition means there are only finitely many ways any n-tuple of elements can behave — the theory is combinatorially tame.

To see the intuition behind the forward direction: if T is ω-categorical, then the automorphism group of the unique countable model M acts on M^n with only finitely many orbits (by the Ryll-Nardzewski theorem's equivalent formulation in terms of oligomorphic groups). Two n-tuples with the same orbit realize the same complete type. Finitely many orbits implies finitely many types. Conversely, when T has only finitely many n-types, every type is isolated — there is a formula φ(x₁, …, xₙ) that uniquely determines the complete type of any tuple satisfying it. Isolated types are realized in every model by the omitting types theorem's dual, and with finitely many types to realize, all countable models end up with the same structure.

The prototype is the theory of the dense linear order without endpoints (DLO), whose unique countable model is the rationals ℚ. Every finite tuple of rationals is described (up to automorphism) entirely by the order type of its elements — there are finitely many such order types for each n, confirming finite type-count. The Ryll-Nardzewski theorem turns this example into a theorem: ω-categoricity is exactly the finite type-count condition, and theories satisfying it are the "most classifiable" in the countable setting. This sets the stage for Morley's deeper question about categoricity in uncountable cardinalities.
