---
id: set-operations
title: Set Operations
domain: mathematics
course: methods-of-proof
prerequisites:
- id: set-theory-basics
  type: hard
builds-toward:
- cartesian-product
- equivalence-relations
tags:
- sets
- union
- intersection
stage: formal-systems
status: validated
---

# Set Operations

## Core Idea
Basic set operations are union (A ∪ B, elements in either set), intersection (A ∩ B, elements in both), and complement (A^c, elements not in A). These follow algebraic laws and are essential for working with relations and partitions.

## Questions

```yaml
- question: "If A = {1, 2, 3, 4} and B = {3, 4, 5, 6}, what is A ∩ B?"
  type: multiple-choice
  options:
    - "{1, 2, 3, 4, 5, 6}"
    - "{3, 4}"
    - "{1, 2, 5, 6}"
    - "{}"
  answer: 1
  explanation: "A ∩ B contains elements in both A and B simultaneously. Only 3 and 4 appear in both sets. Option A is A ∪ B (elements in either set). Option C is the symmetric difference (elements in one but not both). Option D would be the case if the sets shared no elements."

- question: "For any sets A and B, the union A ∪ B always contains strictly more elements than the intersection A ∩ B."
  type: true-false
  answer: false
  explanation: "If A = B, then A ∪ B = A ∩ B = A — they are identical and have the same number of elements. More generally, A ∪ B = A ∩ B if and only if A = B. The union is always at least as large as the intersection, but equality is possible."

- question: "Describe in words what the set (A ∪ B)^c represents, relative to a universal set U. Then name the equivalent expression given by De Morgan's law."
  type: short-answer
  answer: "It is the set of all elements in U that belong to neither A nor B. By De Morgan's law, (A ∪ B)^c = A^c ∩ B^c."
  explanation: "De Morgan's laws link complement with union and intersection: the complement of a union is the intersection of the complements, and vice versa. Intuitively, to be outside (A ∪ B) means to be outside A AND outside B simultaneously — which is exactly A^c ∩ B^c. These laws are frequently used to simplify set expressions and to rewrite logical conditions."
```

## Explainer

You already know what a set is — an unordered collection of distinct elements — and you know how to test membership. Set operations let you build new sets from existing ones, and together they form an algebra that mirrors the logic of AND, OR, and NOT.

The three fundamental operations are union, intersection, and complement. The **union** A ∪ B collects everything in A or B (or both) — it is the "at least one" operation, corresponding to logical OR. The **intersection** A ∩ B collects only what is in both A and B simultaneously — the "both" operation, corresponding to AND. The **complement** A^c (relative to a universal set U) collects everything in U that is *not* in A — the "negation" operation, corresponding to NOT. Every element in U is either in A or in A^c, never both.

These operations satisfy algebraic laws that parallel ordinary arithmetic. Union and intersection are both commutative (A ∪ B = B ∪ A) and associative. They are also distributive over each other: A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C), a fact that surprises students used to multiplication distributing over addition but not the other way around. The most important laws involving complement are **De Morgan's laws**: (A ∪ B)^c = A^c ∩ B^c, and (A ∩ B)^c = A^c ∪ B^c. Read the first one aloud: "the complement of a union is the intersection of the complements." To be outside A ∪ B, you must be outside A and outside B simultaneously — that is exactly A^c ∩ B^c.

A useful tool for checking set identities is the **Venn diagram**: two overlapping circles inside a rectangle (the universal set). Union is both circles; intersection is the overlap; complement is everything outside the circle. Before trying to prove an identity algebraically, sketch the Venn diagram — if the shaded regions match, the identity is plausible; if they don't, the identity is false and you have saved yourself a failed proof.

Set operations appear throughout mathematics because they formalize the underlying logic of conditions. A relation on A × B is a set of ordered pairs; a function is a relation satisfying an additional condition. A partition of a set A divides A into disjoint subsets (pairwise intersections are empty; their union is all of A). When you encounter equivalence relations and Cartesian products in the next topics, you will see how union, intersection, and complement provide the vocabulary for describing those structures precisely.
