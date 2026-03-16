---
id: set-operations-union-intersection-complement
title: 'Set Operations: Union, Intersection, and Complement'
domain: mathematics
course: methods-of-proof
prerequisites:
- id: set-fundamentals
  type: hard
- id: logical-equivalences-intro
  type: soft
builds-toward:
- cartesian-products-relations
- proof-by-cases-exhaustion
tags:
- sets
- operations
- union
- intersection
- complement
stage: formal-systems
status: draft
---

# Set Operations: Union, Intersection, and Complement

## Core Idea
Union (A ∪ B) combines all elements from two sets; intersection (A ∩ B) contains only common elements; complement (A^c) contains all elements not in A (relative to a universal set). These operations correspond to OR, AND, and NOT in logic. Their algebraic properties, including De Morgan's laws, are essential for set-based reasoning.

## Explainer

You already know what a set is and how membership works. The three operations — union, intersection, and complement — are the basic algebra of sets, and they mirror the logical connectives you've seen: ∪ corresponds to OR, ∩ corresponds to AND, and complement corresponds to NOT. This correspondence is not accidental. The statement "x ∈ A ∪ B" is literally the logical claim "x ∈ A or x ∈ B," and proving things about sets is often just applying logical rules to membership statements.

To sharpen the intuitions: **union** A ∪ B is the most permissive operation — it includes everything from either set. **Intersection** A ∩ B is the most restrictive — only what both sets share. **Complement** Aᶜ (relative to a universal set U) contains everything in U not in A. Venn diagrams capture these visually, but precise membership-condition definitions are what enable proofs. The standard method for proving a set equality A = B is to show A ⊆ B and B ⊆ A: take an arbitrary element of one side and prove it belongs to the other by chasing through the logical definitions.

The most important algebraic identities are **De Morgan's laws**: (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ and (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ. These say that complementing a union flips it to an intersection, and vice versa. The logical reading makes this immediate: "not (P or Q)" means "not P, and not Q." Sets also satisfy distributive laws — A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) — exactly mirroring AND distributing over OR. These identities let you rewrite complex set expressions into simpler equivalent forms, a skill that recurs in probability theory, topology, and formal logic.

When you encounter **proof by cases** (your next topic), set operations structure the argument directly: partition a set A into disjoint pieces A₁ ∪ A₂ = A with A₁ ∩ A₂ = ∅, then prove the desired property on each piece separately. In this sense, set operations are not just definitional machinery — they are the grammar of mathematical reasoning about collections, and fluency with them is a prerequisite for almost everything in pure mathematics.
