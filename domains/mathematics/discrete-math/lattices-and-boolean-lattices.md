---
id: lattices-and-boolean-lattices
title: Lattices and Boolean Lattices
domain: mathematics
course: discrete-math
prerequisites:
- id: posets-and-hasse-diagrams
  type: hard
- id: boolean-algebra
  type: soft
tags:
- discrete-structures
- lattices
- boolean-algebra
stage: formal-systems
status: draft
---

# Lattices and Boolean Lattices

## Core Idea
A lattice is a poset where every two elements have a unique least upper bound (join) and greatest lower bound (meet). Boolean lattices are lattices of all subsets of a set under inclusion. Lattices provide a unified framework for order-theoretic and algebraic structures.

## Explainer

You've already worked with **posets** (partially ordered sets) and their Hasse diagrams — structures where elements are related by a partial order ≤ that is reflexive, antisymmetric, and transitive. A lattice adds one more requirement: every pair of elements must have both a well-defined "best common upper bound" and a "best common lower bound." Not every poset satisfies this; lattices are the better-behaved ones.

Given two elements a and b in a lattice, the **join** a ∨ b is the least upper bound — the smallest element that is ≥ both a and b. The **meet** a ∧ b is the greatest lower bound — the largest element that is ≤ both. In the divisibility poset on positive integers (where a ≤ b means a | b), the join of 4 and 6 is lcm(4, 6) = 12, and the meet is gcd(4, 6) = 2. This poset is a lattice, and you already know the operations — you've just been calling them lcm and gcd rather than join and meet.

**Boolean lattices** are the cleanest example: take all subsets of a fixed set S = {1, 2, …, n}, ordered by inclusion ⊆. The join of two subsets is their union (∪), the meet is their intersection (∩), and the Hasse diagram for n = 3 forms a cube-like structure with ∅ at the bottom and S at the top. Every Boolean lattice satisfies the **distributive law**: a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c). This mirrors the Boolean algebra you may know from logic — where AND distributes over OR — because Boolean algebra is precisely the algebra of Boolean lattices.

Lattices appear throughout mathematics and computer science: in logic (formulas ordered by implication form a lattice), in algebra (subgroups of a group form a lattice under inclusion), in type systems (where types are partially ordered and joins represent least common supertypes), and in static analysis (where program facts are propagated through lattice operations). The language of joins and meets gives you a unified vocabulary for all these structures, letting you transfer intuitions across domains.
