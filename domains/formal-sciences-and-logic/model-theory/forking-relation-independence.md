---
id: forking-relation-independence
title: Forking and Independence in Stability Theory
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: stability-theory-introduction
  type: hard
- id: type-spaces-and-stone-topology
  type: hard
builds-toward:
- strongly-minimal-and-geometry
- o-minimality-and-tame-geometry
tags:
- forking
- independence
- stability
stage: advanced
status: draft
---

# Forking and Independence in Stability Theory

## Core Idea
In stable theories, forking is a notion of dependence: a type p forks over a set A if it extends to two contradictory types over a larger set. Non-forking extension provides a notion of algebraic independence in arbitrary structures, generalizing the concept from field theory. Forking satisfies symmetry and transitivity, making it a fundamental concept in stability theory.

## How It's Best Learned
Study forking in algebraically closed fields (ACF), where non-forking corresponds to algebraic independence. Verify the forking axioms: symmetry, transitivity, and finite character.

## Questions

```yaml
- question: "In a stable theory, what does it mean for a type p(x) over B to fork over A ⊆ B?"
  type: multiple-choice
  options:
    - "p has more realizations in the model than expected given A"
    - "p implies a finite disjunction of formulas, each with only finitely many realizations, using parameters from B that are not in A"
    - "p is inconsistent with the complete theory when parameters from B are added"
    - "p has no non-forking extensions to any set larger than B"
  answer: 1
  explanation: "Forking captures the idea that B contains new information that dramatically constrains where x can land — information absent from A. Technically, p forks over A if it implies φ₁(x,b₁) ∨ ... ∨ φₙ(x,bₙ) where each φᵢ has only finitely many realizations (is 'algebraically constraining'). A forking type is still consistent — it just has become dependent on the new parameters. Options A and C describe different phenomena entirely."

- question: "In an algebraically closed field (ACF), you are given a type of a single element a over a set A. Under what condition does this type fork over A?"
  type: multiple-choice
  options:
    - "When a is transcendental over A — that is, a satisfies no polynomial over A"
    - "When a is algebraically dependent over A — it satisfies a polynomial equation with coefficients in A"
    - "When a is contained in the algebraic closure of A but not literally in A itself"
    - "When A is uncountable, causing the type space to be too large"
  answer: 1
  explanation: "In ACF, non-forking corresponds exactly to algebraic independence. Forking therefore corresponds to algebraic dependence: a forks over A when it satisfies a polynomial with coefficients in A, meaning B has 'algebraically constrained' a beyond what A already determined. Option A describes the non-forking case — transcendental elements are the independent ones. Option C is incorrect because an element in the algebraic closure (but not A) can still be in a forking or non-forking extension depending on the type."

- question: "Forking independence in stable theories is symmetric: if a is independent from b over A, then b is independent from a over A."
  type: true-false
  answer: true
  explanation: "Symmetry is one of the four key axioms that forking satisfies in stable theories. This is genuinely non-obvious — 'a is independent from b over A' and 'b is independent from a over A' are logically different statements about different types, yet in stable theories they are equivalent. Symmetry is what makes forking a true independence relation rather than a one-directional dependence notion."

- question: "In algebraically closed fields, forking independence is determined solely by the cardinality of the tuple: any two tuples of the same length over A either both fork or both do not fork over A."
  type: true-false
  answer: false
  explanation: "Cardinality is irrelevant to whether a tuple forks over A. Two tuples of the same length can behave completely differently: one may be algebraically independent over A (non-forking) while the other satisfies polynomial relations over A (forking). Forking depends on the specific algebraic relationships between the elements and A, not on how many elements there are."

- question: "What role does forking play in stable theories that is analogous to the role linear independence plays in vector spaces?"
  type: short-answer
  answer: "Forking defines a dimension theory for stable structures. Just as linear independence measures how many vectors contribute genuinely new 'directions' and yields the dimension of a vector space, non-forking independence measures how many elements are 'genuinely new' over a base set and yields a dimension (Morley rank) for stable structures. The forking geometry of a strongly minimal set then classifies the structure geometrically — modular (vector-space-like), projective, or more complex."
  explanation: "The analogy is deep: both linear independence and forking independence satisfy the exchange property (in appropriate forms), which is what makes a dimension theory possible. In ACF, non-forking corresponds to algebraic independence and the dimension is transcendence degree. The classification of stable theories by their forking geometry — one of the deepest results of model theory — rests entirely on this analogy."
```

## Explainer

From stability theory, you know that stable theories have well-controlled type spaces — the number of types over any set is bounded. From type spaces and Stone topology, you have a precise picture of what a type is: a maximal consistent set of formulas. But stability alone doesn't give you a canonical way to extend types from one parameter set to a larger one while preserving "independence." **Forking** is the device that solves this problem — it defines a notion of when a type extension is "generic" (non-forking) versus "dependent" (forking).

The definition is technical but the intuition is algebraic: in a field, an element a is **algebraically independent** over a set A if a does not satisfy any polynomial equation with coefficients from A. Forking generalizes this to arbitrary stable structures. A type p(x) over a set B **forks over** A ⊆ B if it implies a disjunction of formulas φ₁(x, b₁) ∨ ... ∨ φₙ(x, bₙ) where each φᵢ is "algebraically constraining" in a precise sense (each has finitely many realizations in any model). Informally, p forks over A when B contains information that dramatically constrains where x can land — information that was not already present in A. A **non-forking extension** of a type over A to a larger set B is an extension that adds no such new constraints.

The key properties that forking satisfies in stable theories are what make it a genuine independence relation. **Symmetry**: a is independent from b over A iff b is independent from a over A. **Transitivity**: if a is independent from bc over A and independent from b over Ac, then a is independent from b over A. **Finite character**: a forks over A iff some finite subset of its type forks. **Extension**: any type over A has a non-forking extension over any larger set B. These four axioms are axioms of an **independence relation** in the abstract sense, and in stable theories they have a unique solution — forking is the *only* relation satisfying them.

In algebraically closed fields (ACF), non-forking independence coincides exactly with algebraic independence: the transcendence degree over A of a tuple a is preserved in non-forking extensions. This gives you concrete grounding. In general stable theories, forking plays the same structural role that linear independence plays in vector spaces or algebraic independence plays in fields — it defines a dimension theory. The **Morley rank** and the **forking geometry** of a strongly minimal set determine whether the structure "looks like" a vector space (modular geometry) or a projective space or something more complex. This geometric classification of stable theories — one of the deepest results of model theory — rests entirely on forking as its foundation.

