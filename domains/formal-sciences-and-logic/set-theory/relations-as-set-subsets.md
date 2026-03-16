---
id: relations-as-set-subsets
title: Relations as Subsets of Cartesian Products
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: cartesian-product-and-ordered-pairs
  type: hard
builds-toward:
- functions-and-mappings-formal
tags:
- relations
- binary-relations
- formal-definition
stage: formal-systems
status: draft
---

# Relations as Subsets of Cartesian Products

## Core Idea
A relation R from A to B is any subset of the Cartesian product A × B. This formalization treats all relational structures—ordering relations, equivalence relations, correspondence—as mathematical objects. Key properties include reflexivity, symmetry, transitivity, and totality, which characterize important relation types.

## Explainer

You already know that the **Cartesian product** A × B is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B. A relation is simply a selection from that pool — a subset R ⊆ A × B that picks exactly the pairs you want to declare "related." Writing (a, b) ∈ R is equivalent to saying "a is related to b under R," often written aRb. The key insight is that this definition requires nothing more than set membership: a relation is not a rule or a formula, just a collection of ordered pairs.

Consider the "less than" relation on the integers. Instead of defining it as a rule, we can think of it as the infinite set {(1,2), (1,3), (2,3), (1,4), (2,4), ...} — every pair (m, n) where m is less than n. Similarly, a family tree "is a parent of" relation is the set of ordered pairs (person, child) for every parent-child connection in the family. By reducing relations to sets of pairs, we can reason about them using the tools of set theory: union, intersection, complement, and composition.

Properties of relations are properties of these subsets relative to the underlying sets. **Reflexivity** means (a, a) ∈ R for every a in the domain — the relation includes all "self-pairs." **Symmetry** means if (a, b) ∈ R then (b, a) ∈ R — the relation looks the same in both directions. **Transitivity** means if (a, b) ∈ R and (b, c) ∈ R then (a, c) ∈ R — the relation chains through intermediate elements. An **equivalence relation** satisfies all three; it carves the set into disjoint classes of mutually related elements (called equivalence classes). A **partial order** is reflexive, antisymmetric, and transitive — it captures the structure of "no larger than" without requiring every pair to be comparable.

The payoff of this formalism is uniformity: functions, orderings, equivalences, and graphs are all special cases of the same structure. A **function** from A to B is a relation where every element of A appears as a left coordinate exactly once — adding a uniqueness constraint to the general relation definition. This builds directly toward the formal treatment of functions you will encounter next. Seeing functions as a subtype of relations, rather than a separate concept, lets you apply everything you know about sets to understand when functions exist, when they can be inverted, and how composition of relations generalizes function composition.

Mastering this definition means training yourself to think set-theoretically about structure. Whenever you encounter a relationship between objects — "divides," "is a subset of," "has the same remainder as" — the formal move is to ask: what are the two sets involved, what is A × B, and which ordered pairs belong to the relation? That translation from intuitive relationship to explicit subset is the foundation of all subsequent work in logic, algebra, and theoretical computer science.
