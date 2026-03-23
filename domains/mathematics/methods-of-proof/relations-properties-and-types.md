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
status: validated
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

## Questions

```yaml
- question: "Can a relation be both symmetric and antisymmetric simultaneously?"
  type: multiple-choice
  options:
    - "No — they are logical opposites and cannot both hold for the same relation"
    - "Yes — if the only pairs (x, y) in the relation satisfy x = y, both properties hold trivially"
    - "Yes, but only for relations on infinite sets"
    - "No — antisymmetry explicitly negates symmetry by requiring asymmetric behavior"
  answer: 1
  explanation: "Symmetric means: if (x,y) ∈ R then (y,x) ∈ R. Antisymmetric means: if (x,y) ∈ R and (y,x) ∈ R then x = y. These are not logical opposites. The equality relation {(x,x) : x ∈ A} satisfies both: it is symmetric (trivially — (x,x) reversed is (x,x)) and antisymmetric (the only mutual pairs are (x,x) pairs where x = x). A relation fails to be antisymmetric only if there exist distinct x ≠ y with both (x,y) and (y,x) in R."

- question: "Consider the 'divides' relation on positive integers: x divides y means y = kx for some positive integer k. Which combination of properties does this relation satisfy?"
  type: multiple-choice
  options:
    - "Reflexive, symmetric, and transitive — making it an equivalence relation"
    - "Reflexive, antisymmetric, and transitive — making it a partial order"
    - "Symmetric and transitive, but not reflexive"
    - "Reflexive and symmetric, but not transitive"
  answer: 1
  explanation: "Divisibility is reflexive (x divides x, since x = 1·x), antisymmetric (if x|y and y|x for positive integers then x = y), and transitive (if x|y and y|z then x|z). It is NOT symmetric: 2 divides 6, but 6 does not divide 2. These three properties — reflexive, antisymmetric, transitive — define a partial order. Divisibility on ℕ is the canonical example of a partial order that is not a total order (2 and 3 are incomparable: neither divides the other)."

- question: "The 'is equal to' relation on any set is simultaneously reflexive, symmetric, transitive, AND antisymmetric."
  type: true-false
  answer: true
  explanation: "Equality satisfies all four properties. Reflexive: x = x. Symmetric: if x = y then y = x. Transitive: if x = y and y = z then x = z. Antisymmetric: if x = y and y = x then x = y (trivially true). This means equality is both an equivalence relation (reflexive + symmetric + transitive) and satisfies antisymmetry. It is the only equivalence relation that is also a partial order."

- question: "Every transitive relation is also reflexive."
  type: true-false
  answer: false
  explanation: "Counterexample: the 'strictly less than' relation < on ℝ is transitive (if x < y and y < z then x < z) but not reflexive (no number is strictly less than itself). Another counterexample: the empty relation on any set is vacuously transitive but not reflexive. Transitivity says nothing about whether elements relate to themselves — it only constrains chains of distinct related pairs."

- question: "A student checks whether the 'is a parent of' relation on people is an equivalence relation. Identify which required properties it fails, and explain why for each."
  type: short-answer
  answer: "It fails all three properties required for equivalence. Not reflexive: no one is their own parent. Not symmetric: if A is a parent of B, then B is not a parent of A (they are a child of A). Not transitive: if A is a parent of B and B is a parent of C, then A is a grandparent of C — not a parent. So 'is a parent of' is neither reflexive, symmetric, nor transitive."
  explanation: "Checking properties systematically — rather than relying on intuition — is the core skill. 'Is a sibling of' is symmetric but not reflexive or transitive. 'Is an ancestor of' is transitive but not reflexive or symmetric. 'Is a parent of' fails all three. Each failure corresponds to a concrete counterexample, which is how you prove a relation lacks a property."
```

## Explainer

From your study of sets and Cartesian products, you know that A × A is the set of all ordered pairs (x, y) with x, y ∈ A. A **relation** on A is simply any subset R ⊆ A × A. Writing x ~ y (or xRy) means the pair (x, y) is in R. This is deceptively simple — almost anything can be a relation. "Is divisible by," "is a sibling of," "is greater than," and "is equal to" are all relations on appropriate sets. The interesting question is not what a relation is, but what structural properties it might have.

Four properties organize the landscape. **Reflexivity** says (x, x) ∈ R for every x in A — every element is related to itself. Equality is reflexive; "strictly less than" is not (no number is strictly less than itself). **Symmetry** says if (x, y) ∈ R then (y, x) ∈ R — the relation runs both ways. "Is a sibling of" is symmetric; "is a parent of" is not. **Transitivity** says if (x, y) ∈ R and (y, z) ∈ R then (x, z) ∈ R — the relation chains. "Is less than or equal to" is transitive; "is a direct flight from" need not be. **Antisymmetry** says if (x, y) ∈ R and (y, x) ∈ R then x = y — the only way two elements can be mutually related is if they're the same element.

These properties combine into named types. An **equivalence relation** is reflexive, symmetric, and transitive — it partitions the set into equivalence classes where all related elements cluster together. Equality, congruence mod n, and "has the same birthday as" are all equivalence relations. A **partial order** is reflexive, antisymmetric, and transitive — it lets you compare some pairs but not necessarily all. Divisibility on the positive integers, and the subset relation on sets, are partial orders. When every pair of elements is comparable (either x ~ y or y ~ x), the partial order becomes a **total order** or **linear order**, like ≤ on the integers.

Visualizing relations as directed graphs helps with checking properties. Draw a node for each element and a directed arrow from x to y whenever x ~ y. Reflexivity means every node has a self-loop. Symmetry means every arrow is paired with a reverse arrow. Transitivity means if there is a path from x to y to z, there is also a direct arrow from x to z. Antisymmetry means no two distinct nodes have arrows in both directions. Drawing small examples — say, relations on {1, 2, 3} — and checking properties directly is the most effective way to internalize these definitions before applying them in proofs.
