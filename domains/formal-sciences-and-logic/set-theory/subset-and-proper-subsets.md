---
id: subset-and-proper-subsets
title: Subsets and Proper Subsets
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: set-membership-and-notation
  type: hard
builds-toward:
- indexed-families-of-sets
- axiom-of-power-set
- finite-sets-and-finiteness-definition
tags:
- order
- containment
- relations
stage: formal-systems
status: draft
---

# Subsets and Proper Subsets

## Core Idea
Set A is a subset of set B (A ⊆ B) if every element of A is also in B. A proper subset (A ⊂ B) is a subset that is not equal to B. The subset relation forms a partial order on all sets, forming the basis for power sets and set hierarchies.

## How It's Best Learned
Practice determining when A ⊆ B by checking membership conditions, then identify proper subsets as those with strict containment.

## Explainer

From your work with set membership, you know that the symbol ∈ answers the question "does this element belong to this set?" The subset relation lifts that question to the set level: instead of asking whether a single element belongs to a set, you ask whether an entire set is "contained inside" another. Formally, **A is a subset of B** (written A ⊆ B) if and only if every element of A is also an element of B. There is no requirement that B has only those elements — B may contain much more. The direction matters: A ⊆ B does not imply B ⊆ A unless the two sets happen to be equal.

A **proper subset** (A ⊂ B, sometimes written A ⊊ B) adds one extra condition: A ⊆ B *and* A ≠ B. In other words, B contains at least one element that A does not. The word "proper" signals strict containment. For example, {1, 2} ⊂ {1, 2, 3} is a proper subset, but {1, 2, 3} ⊆ {1, 2, 3} is only a subset (and actually equality). This distinction matters in the same way that < and ≤ differ for numbers — both express an ordering, but only one permits equality.

Two special cases trip up beginners. First, the **empty set** (∅) is a subset of every set, including itself. This follows directly from the definition: the statement "every element of ∅ is in B" is vacuously true because there are no elements to violate it. Second, every set is a subset of itself (A ⊆ A), because every element of A is trivially in A. This reflexivity means the subset relation is not the same as the proper-subset relation — A ⊂ A is always false.

The subset relation has the structure of a **partial order**: it is reflexive (A ⊆ A), antisymmetric (if A ⊆ B and B ⊆ A, then A = B), and transitive (if A ⊆ B and B ⊆ C, then A ⊆ C). This partial-order structure is why subsets are the natural ingredient for building power sets and set hierarchies — topics you will encounter next. When you learn about the power set of a set S, it will be defined as exactly the collection of all subsets of S, and the subset relation will serve as the ordering that organizes that collection.
