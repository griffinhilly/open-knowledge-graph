---
id: subgroups-subgroup-test
title: Subgroups and Subgroup Test
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-basic-properties
  type: hard
builds-toward:
- cyclic-groups
- normal-subgroups
- cosets-lagrange-theorem
tags:
- subgroups
- subset
- closure
- inverses
stage: advanced
status: draft
---

# Subgroups and Subgroup Test

## Core Idea
A subgroup H of a group G is a subset of G that is itself a group under the same operation. The one-step subgroup test states that H is a subgroup if and only if it is nonempty and closed under the operation and taking inverses.

## Explainer

To verify that H is a subgroup of G, you might think you need to check all four group axioms: closure, associativity, identity, inverses. But three of those are essentially free — and understanding why reveals the elegant economy of the subgroup test.

**Associativity is inherited for free.** Since H ⊆ G and elements of H are also elements of G, associativity holds in H simply because it holds in G. You never need to check it separately. This is the key insight that reduces the subgroup verification from four conditions to two: closure under the operation, and closure under taking inverses. And once you have both of those (plus nonemptiness), the identity is automatic — if a ∈ H, then a⁻¹ ∈ H by closure under inverses, and then a·a⁻¹ = e, so e ∈ H by closure under the operation.

Concretely: the integers ℤ form a subgroup of (ℝ, +). Is this obvious? Check the test: ℤ is nonempty (contains 0, or 1, or any integer), the sum of two integers is an integer (closed under +), and the negative of an integer is an integer (closed under taking additive inverses). Done — no need to verify associativity of addition, which you already knew from ℝ. Now compare: the positive integers ℤ⁺ fail the test because ℤ⁺ is not closed under inverses (the additive inverse of 3 is −3, which is not positive). So ℤ⁺ is not a subgroup of (ℝ, +), even though it is closed under addition.

A useful variant is the **two-step subgroup test**: H is a subgroup if and only if (1) H is nonempty, (2) H is closed under the group operation, and (3) H is closed under taking inverses — stated as two separate conditions rather than one combined condition. Both formulations are equivalent. There is also a one-line version combining them: H ≤ G if and only if H ≠ ∅ and for all a, b ∈ H, ab⁻¹ ∈ H. This single condition packages closure and inverses together: setting a = b gives aa⁻¹ = e ∈ H (identity); setting a = e gives b⁻¹ ∈ H (inverses); and then ab⁻¹ using an inverse gives closure.

Subgroups are the building blocks of group theory. Every group homomorphism has a kernel that is a subgroup. Cosets are built from subgroups. Normal subgroups — subgroups whose left and right cosets coincide — are exactly the subgroups you can quotient by to form a new group. All of this begins with the simple question: which subsets of a group are themselves groups? The subgroup test gives you the fastest answer.
