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
status: validated
---

# Cartesian Products and Relations

## Core Idea
The Cartesian product A × B is the set of all ordered pairs (a, b) with a ∈ A and b ∈ B. A relation from A to B is any subset of A × B, formalizing correspondence between elements. Relations are the foundation for functions, equivalence, and order, making them central to mathematical structure.

## Questions

```yaml
- question: "Let A = {1, 2} and B = {a, b}. Which of the following is a valid relation from A to B?"
  type: multiple-choice
  options:
    - "{(1, a, b), (2, a)} — ordered triples formed from A and B"
    - "{(a, 1), (b, 2)} — pairs with B-elements first"
    - "{(1, a), (2, b), (2, a)} — a proper subset of A × B"
    - "{(1, a), (2, b)} only — a relation must pair every element of A with exactly one element of B"
  answer: 2
  explanation: "A relation from A to B is any subset of A × B — there is no additional requirement. A × B = {(1,a),(1,b),(2,a),(2,b)}, and {(1,a),(2,b),(2,a)} is a valid subset. Option D describes a function (the additional constraint that every element of A has exactly one partner), which is the most important special case of a relation but not the only valid one. Options A and B fail because they misplace the ordering or form triples rather than pairs."

- question: "Which of the following best describes the relationship between the concepts of 'function' and 'relation'?"
  type: multiple-choice
  options:
    - "Functions and relations are completely separate concepts with no formal connection"
    - "Every function is a relation, but not every relation is a function"
    - "Every relation is a function — they are different names for the same thing"
    - "Functions are more general than relations because functions can be defined by formulas"
  answer: 1
  explanation: "A function f: A → B is a relation from A to B with the extra constraint that every element of A appears as a first coordinate in exactly one pair. So functions are a special case of relations — a subset of A × B that satisfies the vertical-line-test condition. Not every relation is a function: the relation {(1,a),(1,b),(2,a)} has 1 paired with two elements, violating the single-output requirement. Framing functions as relations is one of the unifying moves of set-theoretic foundations."

- question: "The less-than relationship on real numbers can be formally expressed as a subset of ℝ × ℝ."
  type: true-false
  answer: true
  explanation: "The less-than relation on ℝ is formally the set {(x, y) ∈ ℝ × ℝ : x < y}. Writing 'x < y' is just informal shorthand for saying the pair (x, y) belongs to this set. This is a key point: what we think of as a 'comparison' or 'connection' between two numbers is formalized as a collection of ordered pairs. Every relation — divisibility, 'is a parent of', 'is congruent to mod n' — admits the same treatment."

- question: "The Cartesian product A × B and the Cartesian product B × A contain exactly the same ordered pairs."
  type: true-false
  answer: false
  explanation: "Ordered pairs are sensitive to order: (a, b) and (b, a) are different elements unless a = b. So A × B = {(a, b) : a ∈ A, b ∈ B} and B × A = {(b, a) : b ∈ B, a ∈ A} are different sets whenever A ≠ B. For example, if A = {1} and B = {x}, then A × B = {(1, x)} but B × A = {(x, 1)}. The word 'ordered' in 'ordered pair' is doing real mathematical work here."

- question: "Why does defining a relation as a subset of a Cartesian product unify concepts like 'less than,' 'divides,' and 'is a function of' under a single mathematical framework?"
  type: short-answer
  answer: "All three are ways of associating elements from one set with elements of another (or the same) set. By defining a relation as simply any subset of A × B, we capture the common structure: a pair (a, b) is in the relation if and only if a 'stands in the relation to' b. This means divisibility, ordering, and functional assignment all become instances of the same object — a set of ordered pairs — and any theorem proved about relations in general applies to all of them. It also lets us state precisely what properties (reflexivity, symmetry, transitivity) each type of relation has."
  explanation: "This unification is one of the main payoffs of set-theoretic foundations. Instead of treating 'functions,' 'orderings,' and 'equivalences' as conceptually separate kinds of things, we recognize them as subsets of Cartesian products satisfying different combinations of properties. Equivalence relations are reflexive, symmetric, and transitive; partial orders are reflexive, antisymmetric, and transitive; functions add the single-valued condition. The Cartesian product framework is the common language that makes these distinctions precise and comparable."
```

## Explainer

You already know how to form unions, intersections, and complements of sets. The **Cartesian product** A × B is the next construction: it builds a new set whose elements are ordered pairs (a, b) where a ∈ A and b ∈ B. If A = {1, 2} and B = {x, y}, then A × B = {(1, x), (1, y), (2, x), (2, y)}. A good way to picture this is a grid: rows indexed by A, columns by B, and each cell is one ordered pair. Notice that (1, x) and (x, 1) are different ordered pairs — order matters, which is the whole point of calling them "ordered."

A **relation** from A to B is any subset R ⊆ A × B. This is more general than it sounds. When we write "a is related to b" we mean the pair (a, b) is in R. For example, the less-than relation on ℝ is the set {(x, y) ∈ ℝ × ℝ : x < y} — an infinite subset of ℝ × ℝ. Divisibility on the positive integers is the relation {(m, n) ∈ ℤ⁺ × ℤ⁺ : m divides n}. In each case, what you thought of as a "comparison" or "connection" between two elements is formalized as a collection of ordered pairs.

A **relation on A** (from A to itself) is a subset of A × A. This case is especially rich because the same set appears on both sides, allowing self-referential structure. You can ask whether a relation is **reflexive** (every element is related to itself), **symmetric** (if a R b then b R a), **transitive** (if a R b and b R c then a R c), or **antisymmetric** (if a R b and b R a then a = b). Different combinations of these properties define the major types of relations you will study: equivalence relations are reflexive, symmetric, and transitive; partial orders are reflexive, antisymmetric, and transitive.

The most important special case of a relation from A to B is a **function**: a relation where every element of A is paired with exactly one element of B. In other words, a function f : A → B is a subset of A × B satisfying the vertical line test for ordered pairs. By framing functions as sets of pairs, you can state precisely what it means for two functions to be equal, what the domain and codomain are, and how composition works — all in the single language of set theory. The Cartesian product and relation framework thus unifies functions, orderings, and equivalence under one roof.
