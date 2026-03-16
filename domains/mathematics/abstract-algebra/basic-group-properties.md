---
id: basic-group-properties
title: Basic Group Properties
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-definition-and-examples
  type: hard
builds-toward:
- subgroups-and-subgroup-test
- cosets-and-lagrange-theorem
tags:
- groups
- properties
- proofs
stage: advanced
status: draft
---

# Basic Group Properties

## Core Idea
Basic group properties include uniqueness of identity and inverses, cancellation laws, and (ab)^{-1} = b^{-1}a^{-1}. These follow directly from axioms and are used throughout group theory. Proofs are brief but build essential intuition.

## Explainer

You already know the four group axioms: closure, associativity, existence of an identity, and existence of inverses. What you may not yet realize is that the axioms leave open a silent question — what if a group has *two* different identities? Or what if an element has *two* different inverses? Basic group properties are the proofs that rule this out, and they follow from the axioms alone through surprisingly short arguments.

**Uniqueness of the identity** is proved by assuming e and e' are both identities and watching them collapse: e = e · e' = e'. The first equality holds because e' is an identity (so anything times e' equals that thing), and the second holds because e is an identity. Two identities are forced to be the same element. **Uniqueness of inverses** follows the same logic: if b and c are both inverses of a, then b = b·e = b·(a·c) = (b·a)·c = e·c = c. The associativity axiom is the key engine driving both proofs.

The **cancellation laws** say that if ab = ac then b = c (left cancellation), and if ba = ca then b = c (right cancellation). The proof is immediate: multiply both sides on the left by a⁻¹. These feel obvious because you're used to real number arithmetic, but they are not trivial — they require the existence of inverses guaranteed by the axioms. Note that in a group, left and right cancellation both hold, but in weaker algebraic structures (like monoids, which lack guaranteed inverses) they may not.

The **socks-and-shoes rule** (ab)⁻¹ = b⁻¹a⁻¹ captures the order-reversal that happens when inverting a product. To undo the act of putting on socks *then* shoes, you must remove the shoes *first*, then the socks — the reversal is forced. Algebraically, you verify this by checking that (ab)(b⁻¹a⁻¹) = a(bb⁻¹)a⁻¹ = a·e·a⁻¹ = e. The pattern generalizes: (a₁a₂···aₙ)⁻¹ = aₙ⁻¹···a₂⁻¹a₁⁻¹. These properties are used so constantly in group theory that they quickly become automatic, but the first time you write out each proof you see the full logical weight the axioms are bearing.
