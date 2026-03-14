---
id: equivalence-relations
title: Equivalence Relations and Partitions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: binary-relations
  type: hard
builds-toward:
- partial-orders
tags:
- equivalence-relation
- equivalence-class
- partition
- modular-arithmetic
- quotient-set
stage: formal-systems
status: validated
---

# Equivalence Relations and Partitions

## Core Idea
An equivalence relation is a relation that is reflexive, symmetric, and transitive. Every equivalence relation on a set A partitions A into disjoint equivalence classes [a] = {b ∈ A | aRb}, and conversely every partition determines an equivalence relation. The canonical example is congruence modulo n: integers are equivalent if they have the same remainder when divided by n. Equivalence relations formalize the notion of 'sameness up to some criterion.'

## How It's Best Learned
Use congruence modulo n as the running example: verify all three properties, list the equivalence classes (ℤ₃ has classes [0], [1], [2]), and show how the classes partition ℤ. Then abstract to a general equivalence relation and prove the partition theorem.

## Common Misconceptions
- Forgetting that equivalence classes are always non-empty, pairwise disjoint, and cover the whole set.
- Thinking any two elements of an equivalence class must be 'literally equal' rather than just related by R.
- Conflating a partial order (antisymmetric) with an equivalence relation (symmetric).
