---
id: relations-properties-and-types
title: Relations and Their Properties
domain: mathematics
course: methods-of-proof
prerequisites:
- id: set-operations-and-notation
  type: hard
builds-toward:
- equivalence-relations-and-partitions
tags:
- relations
- reflexive
- symmetric
- transitive
stage: formal-systems
status: draft
---

# Relations and Their Properties

## Core Idea
A relation on a set is a subset of the Cartesian product. Relations can be reflexive (x ~ x for all x), symmetric (if x ~ y then y ~ x), transitive (if x ~ y and y ~ z then x ~ z), or antisymmetric. These properties characterize different types of relations (equivalence, partial order, etc.) and are essential for organizing and understanding mathematical structures.

## How It's Best Learned
Check whether specific relations satisfy given properties using definitions. Visualize relations using diagrams or matrices.

## Common Misconceptions
- Confusing symmetric with antisymmetric (a relation can be both).
- Assuming transitivity holds for all relations.
- Thinking reflexivity requires the relation to hold for only some elements.

## Explainer

From your study of sets and Cartesian products, you know that A × A is the set of all ordered pairs (x, y) with x, y ∈ A. A **relation** on A is simply any subset R ⊆ A × A. Writing x ~ y (or xRy) means the pair (x, y) is in R. This is deceptively simple — almost anything can be a relation. "Is divisible by," "is a sibling of," "is greater than," and "is equal to" are all relations on appropriate sets. The interesting question is not what a relation is, but what structural properties it might have.

Four properties organize the landscape. **Reflexivity** says (x, x) ∈ R for every x in A — every element is related to itself. Equality is reflexive; "strictly less than" is not (no number is strictly less than itself). **Symmetry** says if (x, y) ∈ R then (y, x) ∈ R — the relation runs both ways. "Is a sibling of" is symmetric; "is a parent of" is not. **Transitivity** says if (x, y) ∈ R and (y, z) ∈ R then (x, z) ∈ R — the relation chains. "Is less than or equal to" is transitive; "is a direct flight from" need not be. **Antisymmetry** says if (x, y) ∈ R and (y, x) ∈ R then x = y — the only way two elements can be mutually related is if they're the same element.

These properties combine into named types. An **equivalence relation** is reflexive, symmetric, and transitive — it partitions the set into equivalence classes where all related elements cluster together. Equality, congruence mod n, and "has the same birthday as" are all equivalence relations. A **partial order** is reflexive, antisymmetric, and transitive — it lets you compare some pairs but not necessarily all. Divisibility on the positive integers, and the subset relation on sets, are partial orders. When every pair of elements is comparable (either x ~ y or y ~ x), the partial order becomes a **total order** or **linear order**, like ≤ on the integers.

Visualizing relations as directed graphs helps with checking properties. Draw a node for each element and a directed arrow from x to y whenever x ~ y. Reflexivity means every node has a self-loop. Symmetry means every arrow is paired with a reverse arrow. Transitivity means if there is a path from x to y to z, there is also a direct arrow from x to z. Antisymmetry means no two distinct nodes have arrows in both directions. Drawing small examples — say, relations on {1, 2, 3} — and checking properties directly is the most effective way to internalize these definitions before applying them in proofs.
