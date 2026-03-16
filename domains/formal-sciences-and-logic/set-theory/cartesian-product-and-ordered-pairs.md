---
id: cartesian-product-and-ordered-pairs
title: Cartesian Product and Ordered Pairs
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: set-membership-and-notation
  type: hard
builds-toward:
- relations-as-set-subsets
- functions-and-mappings-formal
tags:
- cartesian-product
- ordered-pairs
- relations
stage: formal-systems
status: draft
---

# Cartesian Product and Ordered Pairs

## Core Idea
The Cartesian product A × B is the set of all ordered pairs (a,b) where a ∈ A and b ∈ B. Two ordered pairs are equal iff (a,b) = (c,d) means a = c and b = d. This construction provides the formal foundation for relations, functions, and multi-dimensional structures in set theory.

## Explainer

Start from something you already know: a set is an unordered collection of distinct elements. The set {1, 2} is exactly the same as {2, 1}. But many mathematical objects are inherently ordered — the point (3, 5) in a coordinate plane is not the same as the point (5, 3). To talk about ordered structure within set theory, we need a new construction, and that is what the **ordered pair** provides.

The formal definition of an ordered pair is (a, b) = {{a}, {a, b}}. This encoding (due to Kuratowski) looks strange at first, but it achieves precisely one thing: it forces the two components to be distinguishable. You can verify that (a, b) = (c, d) if and only if a = c and b = d, while unordered sets {a, b} = {c, d} whenever the elements match in any order. The set-theoretic encoding is mostly scaffolding — what matters is the equality rule. Once you have ordered pairs, everything else follows from your prerequisite concept of **set membership**: you already know how to test whether something belongs to a set, and that is all you need to build the Cartesian product.

The **Cartesian product** A × B is defined as the set of all ordered pairs (a, b) where a ∈ A and b ∈ B. If A = {1, 2} and B = {x, y}, then A × B = {(1,x), (1,y), (2,x), (2,y)} — every element of A paired with every element of B, in that order. The name honors René Descartes, whose coordinate geometry pairs real numbers exactly this way: ℝ × ℝ is the Cartesian plane, where every point is an ordered pair of real numbers. The size of A × B is |A| · |B|, since each of |A| choices from A independently combines with each of |B| choices from B.

The payoff of this construction is that it makes **relations** and **functions** set-theoretic objects. A binary relation between A and B is simply a subset of A × B — a collection of ordered pairs. The relation "less than" on ℕ is the set {(0,1), (0,2), (1,2), (0,3), ...}. A function f: A → B is a special kind of relation — a subset of A × B where every element of A appears as a first component exactly once. This means everything you want to say about functions and relations can be reduced to membership questions about sets of ordered pairs, giving set theory its remarkable expressive power.

The construction extends naturally: the **n-fold Cartesian product** A₁ × A₂ × ... × Aₙ is the set of ordered n-tuples, and A × A × A can be written A³. Sequences, vectors, databases rows — all of these are instances of Cartesian products. Once you understand that ordered pairs are just a device for encoding position into a set, the entire tower of relational mathematics becomes accessible: relations build on ordered pairs, functions build on relations, and virtually every mathematical structure you will study is, at bottom, a set with some distinguished relations and functions on it.

