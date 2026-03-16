---
id: cartesian-product
title: Cartesian Product
domain: mathematics
course: methods-of-proof
prerequisites:
- id: set-operations
  type: hard
builds-toward:
- binary-relations
tags:
- sets
- product
- pairs
stage: formal-systems
status: draft
---

# Cartesian Product

## Core Idea
The Cartesian product A × B is the set of all ordered pairs (a, b) with a ∈ A and b ∈ B. It provides the foundation for defining relations and functions, and |A × B| = |A| · |B|.

## Explainer

You've already worked with set operations like union, intersection, and complement — all of which take sets and produce new sets of elements drawn from the same "universe." The Cartesian product does something structurally different: it combines two sets to create a set of *pairs*, where each pair records one element from each original set. If A = {1, 2} and B = {x, y}, then A × B = {(1, x), (1, y), (2, x), (2, y)}. Order matters: (1, x) and (x, 1) are different objects, and in general A × B ≠ B × A unless the sets are equal or empty.

The **ordered pair** is the key concept. Unlike a set {a, b} where order doesn't matter and {a, b} = {b, a}, the pair (a, b) records which element came from which set. This distinction is what makes relations and functions possible. A **binary relation** from A to B is just a subset R ⊆ A × B — a collection of pairs where some elements of A are "related to" elements of B. For example, the "less than" relation on {1, 2, 3} is {(1,2), (1,3), (2,3)} ⊆ {1,2,3} × {1,2,3}. Without the Cartesian product, we'd have no formal language for "a relates to b."

The size formula |A × B| = |A| · |B| follows directly from counting: for each of the |A| choices from A, there are |B| choices from B, giving |A| · |B| pairs total. This multiplicative structure is why Cartesian products extend naturally to more than two sets: A × B × C is the set of ordered triples, with |A × B × C| = |A| · |B| · |C|. The familiar coordinate plane ℝ² is exactly ℝ × ℝ — the Cartesian product of the real numbers with itself, named after Descartes who first used this idea to connect geometry and algebra.

The conceptual leap from sets to Cartesian products is a shift from thinking about collections of single objects to thinking about *relationships between* objects. Every function, every matrix, every graph, every relation you'll encounter in mathematics is formally a subset of some Cartesian product. Internalizing this — that "a function from A to B" is really just a special subset of A × B satisfying extra properties — will make abstract definitions throughout mathematics much more concrete and navigable.
