---
id: set-theory-basics
title: Set Theory Basics
domain: mathematics
course: methods-of-proof
prerequisites: []
builds-toward:
- set-operations
- cartesian-product
tags:
- sets
- foundations
stage: formal-systems
status: draft
---

# Set Theory Basics

## Core Idea
A set is a collection of distinct elements. Sets can be finite or infinite, described by membership rules. Set theory provides foundational language for mathematics using notation for membership (∈), equality, and containment (⊆).

## Questions

```yaml
- question: "The set A = {1, 2, 3} and the set B = {3, 1, 2}. Which of the following is true?"
  type: multiple-choice
  options: ["A ≠ B, because the elements are listed in a different order", "A = B, because sets are equal when they contain exactly the same elements regardless of order", "A ⊂ B, because A was defined before B", "A ≠ B, because sets must be defined in the same way to be equal"]
  answer: 1
  explanation: "Set equality depends only on membership, not on the order elements are listed or how the set was defined. Since A and B contain exactly the same elements — 1, 2, and 3 — they are equal. Order is irrelevant in sets (unlike ordered tuples)."

- question: "The set {1, 2, 2, 3} contains four elements, since the number 2 appears twice."
  type: true-false
  answer: false
  explanation: "By definition, a set contains only distinct elements. Repetitions are ignored — {1, 2, 2, 3} is identical to {1, 2, 3}, a three-element set. This is one of the key differences between sets and multisets (bags), which do allow duplicate elements."

- question: "What is the difference between A ⊆ B and A ⊂ B?"
  type: short-answer
  answer: "A ⊆ B means A is a subset of B (every element of A is in B, and A may equal B). A ⊂ B means A is a proper subset of B (every element of A is in B, but A ≠ B — B has at least one element A does not)."
  explanation: "The distinction mirrors ≤ vs. < for numbers. A ⊆ B allows the possibility A = B, while A ⊂ B requires A to be strictly smaller. Every set is a subset of itself (A ⊆ A), but no set is a proper subset of itself."
```

## Explainer

A set is one of the most primitive ideas in mathematics: it is simply a collection of distinct objects, called elements, treated as a single thing. The elements can be anything — numbers, letters, people, other sets. What matters is only whether something is in the collection or not. We write this with curly braces: {2, 4, 6} is the set containing 2, 4, and 6. The symbol ∈ means "is an element of," so 4 ∈ {2, 4, 6} is true, while 5 ∈ {2, 4, 6} is false. Its negation, ∉, means "is not an element of."

Two features of sets are worth internalizing early. First, sets are unordered: {1, 2, 3} and {3, 1, 2} are the same set, because they contain exactly the same elements. Second, sets have no duplicates: if you write {1, 2, 2, 3}, the extra 2 is ignored — the set is just {1, 2, 3}. Both properties follow from the fact that membership is a yes-or-no question: either an element belongs to the set or it does not, and listing it twice does not change that answer.

Sets can be described in two ways. Roster notation lists the elements explicitly: {2, 4, 6, 8}. Set-builder notation describes them by a rule: {x | x is an even positive integer less than 10}, read "the set of all x such that x is an even positive integer less than 10." Set-builder notation is essential for infinite sets, which cannot be listed in full.

Containment between sets is captured by the subset relation. We say A ⊆ B (A is a subset of B) if every element of A also belongs to B. The empty set ∅ — the set with no elements — is a subset of every set, because there are no elements in it that could fail to be in B. A proper subset, written A ⊂ B, requires additionally that A ≠ B: B has at least one element that A lacks. These relations are the building blocks for comparing and relating sets, and they will appear throughout mathematics wherever structure is described in terms of membership.
