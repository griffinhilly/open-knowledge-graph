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

## Explainer

From stability theory, you know that stable theories have well-controlled type spaces — the number of types over any set is bounded. From type spaces and Stone topology, you have a precise picture of what a type is: a maximal consistent set of formulas. But stability alone doesn't give you a canonical way to extend types from one parameter set to a larger one while preserving "independence." **Forking** is the device that solves this problem — it defines a notion of when a type extension is "generic" (non-forking) versus "dependent" (forking).

The definition is technical but the intuition is algebraic: in a field, an element a is **algebraically independent** over a set A if a does not satisfy any polynomial equation with coefficients from A. Forking generalizes this to arbitrary stable structures. A type p(x) over a set B **forks over** A ⊆ B if it implies a disjunction of formulas φ₁(x, b₁) ∨ ... ∨ φₙ(x, bₙ) where each φᵢ is "algebraically constraining" in a precise sense (each has finitely many realizations in any model). Informally, p forks over A when B contains information that dramatically constrains where x can land — information that was not already present in A. A **non-forking extension** of a type over A to a larger set B is an extension that adds no such new constraints.

The key properties that forking satisfies in stable theories are what make it a genuine independence relation. **Symmetry**: a is independent from b over A iff b is independent from a over A. **Transitivity**: if a is independent from bc over A and independent from b over Ac, then a is independent from b over A. **Finite character**: a forks over A iff some finite subset of its type forks. **Extension**: any type over A has a non-forking extension over any larger set B. These four axioms are axioms of an **independence relation** in the abstract sense, and in stable theories they have a unique solution — forking is the *only* relation satisfying them.

In algebraically closed fields (ACF), non-forking independence coincides exactly with algebraic independence: the transcendence degree over A of a tuple a is preserved in non-forking extensions. This gives you concrete grounding. In general stable theories, forking plays the same structural role that linear independence plays in vector spaces or algebraic independence plays in fields — it defines a dimension theory. The **Morley rank** and the **forking geometry** of a strongly minimal set determine whether the structure "looks like" a vector space (modular geometry) or a projective space or something more complex. This geometric classification of stable theories — one of the deepest results of model theory — rests entirely on forking as its foundation.

