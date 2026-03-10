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
- binary-relations
- cardinality-and-countability
tags:
- union
- intersection
- complement
- set-difference
- symmetric-difference
stage: formal-systems
status: draft
---

# Set Operations

## Core Idea
The standard set operations are: union A ∪ B (elements in A or B or both), intersection A ∩ B (elements in both), set difference A \ B (elements in A but not B), and complement Aᶜ (elements in the universal set not in A). Set identities — such as De Morgan's laws (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ — mirror the logical equivalences for ∨ and ∧, making set algebra and propositional logic deeply connected.

## How It's Best Learned
Always draw Venn diagrams alongside symbolic manipulation. Prove set equalities by showing mutual containment (A ⊆ B and B ⊆ A implies A = B). This element-chasing technique is the standard proof method for set identities.

## Common Misconceptions
- Confusing A \ B with B \ A — set difference is not commutative.
- Assuming A ∩ B = ∅ means A and B have no relationship, rather than just no shared elements.
- Forgetting that the complement depends on the choice of universal set.
