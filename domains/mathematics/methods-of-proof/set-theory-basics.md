---
id: set-theory-basics
title: Set Theory Basics
domain: mathematics
course: methods-of-proof
prerequisites:
- id: variable-expressions
  type: soft
- id: factors-and-multiples
  type: soft
builds-toward:
- set-operations
- cartesian-product
- binary-relations
tags:
- sets
- elements
- subsets
- empty-set
- set-builder-notation
stage: formal-systems
status: validated
---

# Set Theory Basics

## Core Idea
A set is an unordered collection of distinct objects called elements. Sets are described by roster notation {1, 2, 3}, set-builder notation {x ∈ ℤ | x > 0}, or by name (ℕ, ℤ, ℚ, ℝ). The fundamental relation is membership: a ∈ A. A set B is a subset of A (B ⊆ A) if every element of B is also in A. The empty set ∅ is a subset of every set, and every set is a subset of itself.

## How It's Best Learned
Use Venn diagrams to build intuition. Work through subset vs. element membership carefully — {1} ∈ {{1}, 2} but {1} ⊆ {1, 2}. Have students write the power set of small sets to internalize subsets.

## Common Misconceptions
- Confusing ∈ (membership) and ⊆ (subset): {1} ⊆ {1,2,3} but 1 ∈ {1,2,3}.
- Thinking the empty set has no subsets — it has one, itself.
- Assuming sets can contain duplicate elements (they cannot; use multisets for that).
