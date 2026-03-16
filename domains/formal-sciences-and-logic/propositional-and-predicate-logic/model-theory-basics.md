---
id: model-theory-basics
title: Basic Model Theory
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-semantics
  type: hard
- id: fol-soundness-completeness
  type: soft
- id: set-theory-basics
  type: soft
- id: equivalence-relations
  type: soft
- id: fol-compactness
  type: soft
- id: propositional-compactness
  type: soft
- id: set-fundamentals
  type: hard
- id: functions-and-function-properties
  type: hard
builds-toward:
- lowenheim-skolem-theorem
tags:
- model-theory
- theory
- elementary-equivalence
- categorical
- complete-theory
stage: formal-systems
status: validated
---
# Basic Model Theory

## Core Idea
Model theory studies the relationship between formal theories and the structures that satisfy them. A theory T is a set of sentences closed under logical consequence; a model of T is a structure where every sentence in T is true. Two structures are elementarily equivalent if they satisfy exactly the same first-order sentences. A theory is complete if for every sentence φ, either φ or ¬φ is in the theory; it is categorical in cardinality κ if all its models of cardinality κ are isomorphic. These concepts help characterize what first-order logic can and cannot express.

## How It's Best Learned
Work through examples of complete theories (dense linear orders without endpoints, algebraically closed fields) and incomplete theories (the theory of groups). Verify elementary equivalence by constructing back-and-forth systems.

## Common Misconceptions
- Elementary equivalence is weaker than isomorphism: two non-isomorphic structures can satisfy exactly the same first-order sentences.
- A complete theory can still have multiple non-isomorphic models (of different cardinalities).

## Questions

```yaml
- question: "Two structures M and N are elementarily equivalent if and only if:"
  type: multiple-choice
  options:
    - "There exists an isomorphism between M and N"
    - "They satisfy exactly the same set of first-order sentences"
    - "Every quantifier-free sentence true in M is also true in N"
    - "They are both models of the same complete theory and have the same cardinality"
  answer: 1
  explanation: "Elementary equivalence (M ≡ N) means M and N agree on all first-order sentences — not just quantifier-free ones, and regardless of cardinality. Isomorphism (option A) implies elementary equivalence but is strictly stronger: non-isomorphic structures can be elementarily equivalent. Option C (only quantifier-free sentences) is too weak. Option D is close but cardinality alone is not sufficient — two structures of the same cardinality can be models of the same complete theory without being elementarily equivalent if the theory is not complete."

- question: "A complete theory can have multiple non-isomorphic models."
  type: true-false
  answer: true
  explanation: "Completeness means that for every sentence φ, either φ or ¬φ is a theorem of the theory — there is no sentence the theory leaves undecided. But this says nothing about isomorphism: different cardinalities yield different models. For example, the theory of dense linear orders without endpoints (DLO) is complete, yet it has countable models (like ℚ) and uncountable models (like ℝ) that are not isomorphic. Categoricity in a specific cardinality κ is the stronger property that all models of size κ are isomorphic."

- question: "What does it mean for a theory to be categorical in cardinality κ, and why does this not imply completeness in general?"
  type: short-answer
  answer: "A theory T is κ-categorical if all models of T of cardinality κ are isomorphic. This does not automatically imply completeness, but by the Łoś–Vaught test: if T is κ-categorical for some κ, has no finite models, and is consistent, then T is complete. Without those conditions, κ-categoricity alone does not force completeness."
  explanation: "The subtlety is that categoricity pins down the theory's models at one cardinality, but first-order logic cannot fix cardinality. A sentence true in all countable models might fail in an uncountable one unless completeness (every sentence decided) already holds. The Łoś–Vaught test is the bridge connecting these two properties."
```

## Explainer

From first-order semantics you know how to evaluate a first-order sentence in a given structure M: interpret each constant, function symbol, and relation symbol in M, then check whether the sentence comes out true. Model theory is the systematic study of the relationship between theories — sets of sentences — and the structures that satisfy them.

A theory T is formally a set of first-order sentences closed under logical consequence: whenever T ⊨ φ (every model of T satisfies φ), we require φ ∈ T. A structure M is a model of T if every sentence in T is true in M. The collection of all sentences true in M is its complete theory Th(M) — by definition, a complete theory. Two structures M and N are elementarily equivalent (M ≡ N) if Th(M) = Th(N): they agree on every first-order sentence, even though they may look quite different as structures. For example, the rationals ℚ and the reals ℝ, as ordered fields, are not isomorphic, but they are elementarily equivalent as dense linear orders without endpoints.

A critical distinction: elementary equivalence is much weaker than isomorphism. Isomorphic structures are always elementarily equivalent, but the converse fails dramatically. First-order logic simply cannot distinguish many non-isomorphic structures: for instance, any two algebraically closed fields of the same characteristic and the same uncountable cardinality are isomorphic, but two ACFs of different cardinalities satisfy the same sentences. This gap between "syntactically indistinguishable" and "structurally identical" is one of the central themes of model theory.

A theory T is complete if for every sentence φ, either φ ∈ T or ¬φ ∈ T — the theory has an opinion on every question expressible in the language. Note that completeness is about sentences, not about uniqueness of models: a complete theory can still have many non-isomorphic models, one for each infinite cardinality. The theory DLO (dense linear orders without endpoints) is complete, yet ℚ and ℝ are both models and are non-isomorphic. What completeness buys you is that any two models agree on all first-order sentences — they are elementarily equivalent — even if they are not isomorphic.

Categoricity in cardinality κ goes further: T is κ-categorical if all models of T of cardinality κ are isomorphic to each other. This pins down the structure at size κ completely. The Łoś–Vaught test is a powerful tool: if T is consistent with no finite models and is κ-categorical for some infinite κ, then T is complete. This is how we prove DLO is complete — it is ℵ₀-categorical (every countable dense linear order without endpoints is isomorphic to ℚ) and has no finite models.
