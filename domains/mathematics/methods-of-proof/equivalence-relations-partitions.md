---
id: equivalence-relations-partitions
title: Equivalence Relations and Partitions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: cartesian-products-relations
  type: hard
tags:
- relations
- equivalence
- partitions
stage: formal-systems
status: draft
---

# Equivalence Relations and Partitions

## Core Idea
An equivalence relation is reflexive (x ~ x), symmetric (x ~ y implies y ~ x), and transitive (x ~ y and y ~ z imply x ~ z). Equivalence relations partition a set into disjoint equivalence classes, where elements in the same class are equivalent. This correspondence between equivalence relations and partitions is fundamental to classification and quotient structures.

## Explainer

From your study of Cartesian products and relations, you know that a **relation** on a set A is a subset R ⊆ A × A — a collection of ordered pairs (x, y) that we write as x ~ y when (x, y) ∈ R. Not every relation is useful or well-behaved. An **equivalence relation** is a relation that behaves like equality: it is reflexive (every element is related to itself), symmetric (if x is related to y then y is related to x), and transitive (relatedness chains through intermediate elements). The classic example is equality itself, but the idea is far more general: "has the same birthday as," "leaves the same remainder when divided by 3," and "is geometrically congruent to" are all equivalence relations.

The central theorem is that equivalence relations and **partitions** are in perfect correspondence. Given an equivalence relation ~, the **equivalence class** of an element x is [x] = {y ∈ A : y ~ x} — the set of everything equivalent to x. These classes are non-empty (reflexivity guarantees x ∈ [x]), they cover the entire set (every element belongs to its own class), and they are mutually disjoint (if [x] and [y] share even one element, then x ~ y and the two classes are identical). The classes thus carve A into non-overlapping, exhaustive chunks — a partition. Conversely, given any partition, you can define an equivalence relation by declaring x ~ y iff x and y belong to the same piece. The correspondence is exact and bijective.

The power of this idea is that it lets you **classify objects by their properties** rather than their identity. Two integers are congruent mod n if their difference is divisible by n. The equivalence classes are {0, n, 2n, ...}, {1, n+1, 2n+1, ...}, and so on — and arithmetic on these classes (modular arithmetic) is well-defined precisely because the class of a sum depends only on the classes of the summands, not on the specific representatives chosen. This is the key step in constructing **quotient structures**: you replace the original set with its equivalence classes and check that operations on classes are independent of representative choice (called "well-definedness").

You will see this pattern throughout mathematics: the integers ℤ are a quotient of the natural numbers; the rationals ℚ are equivalence classes of pairs (a, b) under (a, b) ~ (c, d) iff ad = bc; topological spaces can be glued together by declaring boundary points equivalent. The three axioms — reflexive, symmetric, transitive — are the minimal conditions that ensure the quotient construction is coherent. Any weaker set of conditions breaks the disjointness of classes and the well-definedness of operations on them.
