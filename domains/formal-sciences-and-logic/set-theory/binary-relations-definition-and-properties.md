---
id: binary-relations-definition-and-properties
title: Binary Relations and Their Properties
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: ordered-pairs-and-tuples
  type: hard
- id: indexed-families-of-sets
  type: soft
builds-toward:
- equivalence-relations-and-equivalence-classes
- well-founded-relations-and-recursion
- functions-and-function-properties
tags:
- relations
- properties
- structures
stage: formal-systems
status: draft
---

# Binary Relations and Their Properties

## Core Idea
A binary relation R on a set S is a subset R ⊆ S × S. Relations exhibit properties including reflexivity (aRa for all a), symmetry (aRb ⟹ bRa), and transitivity (aRb ∧ bRc ⟹ aRc). Different combinations of these properties define important relation classes: equivalence relations, orderings, and more.

## Explainer

From your work with ordered pairs, you know that S × S is the set of all pairs (a, b) where a and b come from S. A **binary relation** R on S is simply a subset of this Cartesian product: a collection of pairs. When (a, b) ∈ R, we write aRb and say "a is related to b." This set-theoretic definition is completely general — any collection of pairs is a valid relation. The interesting structure comes from which properties that collection happens to satisfy.

Three properties appear most often. **Reflexivity** says every element is related to itself: for all a ∈ S, aRa. The equality relation on any set is reflexive; so is "less than or equal to" on the integers. **Symmetry** says the relation runs in both directions: if aRb then bRa. "Is a sibling of" is symmetric; "is a parent of" is not. **Transitivity** says the relation chains: if aRb and bRc then aRc. "Is an ancestor of" is transitive; "is a neighbor of" (in a graph) typically is not. A fourth property appears in orderings: **antisymmetry** says that if aRb and bRa, then a = b — the relation can go both ways only when the two elements are the same.

These properties combine to define the most important relation types in mathematics. **Equivalence relations** satisfy reflexivity, symmetry, and transitivity — they partition S into equivalence classes where all related elements are grouped together. "Has the same remainder when divided by 3" is an equivalence relation on the integers, grouping them into classes {0, 3, 6, ...}, {1, 4, 7, ...}, {2, 5, 8, ...}. **Partial orders** satisfy reflexivity, antisymmetry, and transitivity — they give a notion of "at most as large as" without requiring all elements to be comparable. The subset relation on a collection of sets is a partial order. **Total orders** add comparability: for any two elements, either aRb or bRa (or both, in which case a = b). The usual ≤ on the integers is a total order.

Learning to identify which properties a relation has — and which it lacks — is the first step toward classifying it. The strategy is to test each property directly with concrete examples and counterexamples. For a finite set, you can draw the relation as a directed graph (a → b whenever aRb) and read off reflexivity (every node has a self-loop), symmetry (every edge runs in both directions), and transitivity (if a → b → c then a → c). This visual representation builds intuition rapidly and makes the abstract definitions concrete.
