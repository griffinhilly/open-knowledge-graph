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

## Questions

```yaml
- question: "Let A = {1, 2, 3} and B = {a, b}. What is |A × B|?"
  type: multiple-choice
  options:
    - "5, because |A| + |B| = 3 + 2 = 5"
    - "6, because |A| · |B| = 3 · 2 = 6"
    - "8, because A × B and B × A together have 12 pairs but we remove duplicates"
    - "9, because the product of the largest elements is 3 · 3 = 9"
  answer: 1
  explanation: "The size formula for Cartesian products is multiplicative: |A × B| = |A| · |B|. For each of the 3 elements in A, you form a pair with each of the 2 elements in B, giving 3 · 2 = 6 ordered pairs: {(1,a), (1,b), (2,a), (2,b), (3,a), (3,b)}. The additive answer (5) confuses union with product — union combines elements, product forms pairs. This multiplicative structure extends to more sets: |A × B × C| = |A| · |B| · |C|."

- question: "Which statement correctly distinguishes the set {a, b} from the ordered pair (a, b)?"
  type: multiple-choice
  options:
    - "They are the same object — sets and ordered pairs represent identical mathematical structures"
    - "In a set, {a, b} = {b, a}; in an ordered pair, (a, b) ≠ (b, a) unless a = b"
    - "Sets can only contain numbers, while ordered pairs can contain any objects"
    - "Ordered pairs are just sets with exactly two elements — the notation is different but the meaning is identical"
  answer: 1
  explanation: "The key distinction is that sets are unordered: {a, b} and {b, a} are the same set. Ordered pairs are ordered: (a, b) and (b, a) are different unless a = b. This distinction is what makes the Cartesian product useful. A × B and B × A contain the same element combinations but different ordered pairs: (a, b) ∈ A × B while (b, a) ∈ B × A. Order-sensitivity is essential for defining relations and functions, where which element 'maps to' which matters."

- question: "A binary relation from set A to set B is formally defined as a subset of the Cartesian product A × B."
  type: true-false
  answer: true
  explanation: "This is the formal set-theoretic definition of a relation. A × B is the set of all possible ordered pairs (a, b). Any subset R ⊆ A × B specifies exactly which pairs stand in the relation — (a, b) ∈ R means 'a is related to b.' For example, the 'less than' relation on {1, 2, 3} is the subset {(1,2), (1,3), (2,3)} ⊆ {1,2,3} × {1,2,3}. Functions are then defined as special relations: subsets of A × B where every element of A appears as a first coordinate exactly once."

- question: "For any two sets A and B, A × B = B × A."
  type: true-false
  answer: false
  explanation: "In general, A × B ≠ B × A. A × B consists of pairs (a, b) with a ∈ A and b ∈ B; B × A consists of pairs (b, a) with b ∈ B and a ∈ A. These are different ordered pairs unless a = b. For example, if A = {1} and B = {x}, then A × B = {(1,x)} while B × A = {(x,1)} — completely different sets. The only exceptions are when A = B (in which case A × A = A × A trivially) or when one of the sets is empty (both products are then empty)."

- question: "Why is the concept of an ordered pair — rather than just a set of two elements — necessary for defining functions and relations?"
  type: short-answer
  answer: "Functions and relations track which element is the input and which is the output (or which is related to which). A set {a, b} loses this directionality: {a, b} = {b, a}, so we cannot tell whether 'a maps to b' or 'b maps to a.' An ordered pair (a, b) preserves the distinction: (a, b) ≠ (b, a) unless a = b. For example, the function f(2) = 5 must be recorded as (2, 5) — a different relationship than f(5) = 2, which is (5, 2). If we used unordered sets, we would lose the ability to represent which value was the input. Order is what makes the formal definition of function — as a set of input-output pairs — meaningful."
  explanation: "The Cartesian product, by generating ordered pairs, provides the formal scaffolding that makes every downstream concept in mathematics (functions, relations, graphs, matrices, coordinate geometry) rigorously definable. The concept is deceptively simple, but it is the foundation on which most of formal mathematics is built."
```

## Explainer

You've already worked with set operations like union, intersection, and complement — all of which take sets and produce new sets of elements drawn from the same "universe." The Cartesian product does something structurally different: it combines two sets to create a set of *pairs*, where each pair records one element from each original set. If A = {1, 2} and B = {x, y}, then A × B = {(1, x), (1, y), (2, x), (2, y)}. Order matters: (1, x) and (x, 1) are different objects, and in general A × B ≠ B × A unless the sets are equal or empty.

The **ordered pair** is the key concept. Unlike a set {a, b} where order doesn't matter and {a, b} = {b, a}, the pair (a, b) records which element came from which set. This distinction is what makes relations and functions possible. A **binary relation** from A to B is just a subset R ⊆ A × B — a collection of pairs where some elements of A are "related to" elements of B. For example, the "less than" relation on {1, 2, 3} is {(1,2), (1,3), (2,3)} ⊆ {1,2,3} × {1,2,3}. Without the Cartesian product, we'd have no formal language for "a relates to b."

The size formula |A × B| = |A| · |B| follows directly from counting: for each of the |A| choices from A, there are |B| choices from B, giving |A| · |B| pairs total. This multiplicative structure is why Cartesian products extend naturally to more than two sets: A × B × C is the set of ordered triples, with |A × B × C| = |A| · |B| · |C|. The familiar coordinate plane ℝ² is exactly ℝ × ℝ — the Cartesian product of the real numbers with itself, named after Descartes who first used this idea to connect geometry and algebra.

The conceptual leap from sets to Cartesian products is a shift from thinking about collections of single objects to thinking about *relationships between* objects. Every function, every matrix, every graph, every relation you'll encounter in mathematics is formally a subset of some Cartesian product. Internalizing this — that "a function from A to B" is really just a special subset of A × B satisfying extra properties — will make abstract definitions throughout mathematics much more concrete and navigable.
