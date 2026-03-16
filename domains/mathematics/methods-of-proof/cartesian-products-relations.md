---
id: cartesian-products-relations
title: Cartesian Products and Relations
domain: mathematics
course: methods-of-proof
prerequisites:
- id: set-operations-union-intersection-complement
  type: hard
builds-toward:
- functions-domain-codomain-range
- equivalence-relations-partitions
tags:
- sets
- relations
- cartesian-product
stage: formal-systems
status: draft
---

# Cartesian Products and Relations

## Core Idea
The Cartesian product A × B is the set of all ordered pairs (a, b) with a ∈ A and b ∈ B. A relation from A to B is any subset of A × B, formalizing correspondence between elements. Relations are the foundation for functions, equivalence, and order, making them central to mathematical structure.

## Explainer

You already know how to form unions, intersections, and complements of sets. The **Cartesian product** A × B is the next construction: it builds a new set whose elements are ordered pairs (a, b) where a ∈ A and b ∈ B. If A = {1, 2} and B = {x, y}, then A × B = {(1, x), (1, y), (2, x), (2, y)}. A good way to picture this is a grid: rows indexed by A, columns by B, and each cell is one ordered pair. Notice that (1, x) and (x, 1) are different ordered pairs — order matters, which is the whole point of calling them "ordered."

A **relation** from A to B is any subset R ⊆ A × B. This is more general than it sounds. When we write "a is related to b" we mean the pair (a, b) is in R. For example, the less-than relation on ℝ is the set {(x, y) ∈ ℝ × ℝ : x < y} — an infinite subset of ℝ × ℝ. Divisibility on the positive integers is the relation {(m, n) ∈ ℤ⁺ × ℤ⁺ : m divides n}. In each case, what you thought of as a "comparison" or "connection" between two elements is formalized as a collection of ordered pairs.

A **relation on A** (from A to itself) is a subset of A × A. This case is especially rich because the same set appears on both sides, allowing self-referential structure. You can ask whether a relation is **reflexive** (every element is related to itself), **symmetric** (if a R b then b R a), **transitive** (if a R b and b R c then a R c), or **antisymmetric** (if a R b and b R a then a = b). Different combinations of these properties define the major types of relations you will study: equivalence relations are reflexive, symmetric, and transitive; partial orders are reflexive, antisymmetric, and transitive.

The most important special case of a relation from A to B is a **function**: a relation where every element of A is paired with exactly one element of B. In other words, a function f : A → B is a subset of A × B satisfying the vertical line test for ordered pairs. By framing functions as sets of pairs, you can state precisely what it means for two functions to be equal, what the domain and codomain are, and how composition works — all in the single language of set theory. The Cartesian product and relation framework thus unifies functions, orderings, and equivalence under one roof.
