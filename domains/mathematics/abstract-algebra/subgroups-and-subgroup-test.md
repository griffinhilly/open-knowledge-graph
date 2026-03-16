---
id: subgroups-and-subgroup-test
title: Subgroups and Subgroup Test
domain: mathematics
course: abstract-algebra
prerequisites:
- id: basic-group-properties
  type: hard
builds-toward:
- cyclic-groups
- cosets-and-lagrange-theorem
- normal-subgroups
tags:
- subgroups
- tests
- structure
stage: advanced
status: draft
---

# Subgroups and Subgroup Test

## Core Idea
A subgroup H of G is a subset forming a group under the same operation. The subgroup test: H is nonempty, closed under the operation, and contains inverses. One-step and two-step tests provide efficient verification methods.

## How It's Best Learned
Identify subgroups of Z and S_3. Apply both the standard definition and subgroup tests to see which is most convenient for different cases.

## Common Misconceptions
- Forgetting to check closure; a subset with inverses is not necessarily a subgroup.
- Assuming every subset containing the identity is a subgroup without checking closure.

## Explainer

You've built up the group axioms — closure, associativity, identity, inverses — and seen them satisfied by groups like ℤ under addition and S_n under composition. A **subgroup** asks a natural question: when does a *subset* of a group form a group in its own right, under the same operation? This is the first tool for understanding the internal structure of a group, and the subgroup tests make verification efficient.

Start with a familiar example. The integers ℤ under addition form a group. The set 2ℤ = {…, −4, −2, 0, 2, 4, …} is a subset: the sum of two even integers is even (closure), 0 is even (identity), and the additive inverse of an even integer is even (inverses). Associativity is inherited from ℤ. So 2ℤ is a subgroup of ℤ. More generally, nℤ is a subgroup for any positive integer n. Subgroups can also fail: in S₃, the set {e, (12), (13), (23)} is *not* a subgroup because closure fails — (12)∘(13) = (132), which is not in the set.

The **one-step subgroup test** packages all the axioms into a single condition: a nonempty subset H is a subgroup of G if and only if for every a, b ∈ H, the element ab⁻¹ ∈ H. Setting a = b shows e = aa⁻¹ ∈ H (identity). Setting a = e (now known to be in H) shows b⁻¹ ∈ H (inverses exist). Replacing b by b⁻¹ and applying the condition gives a(b⁻¹)⁻¹ = ab ∈ H (closure). One condition, three axioms. The **two-step test** — verify closure directly and verify that inverses exist — is often more explicit for finite groups where you can check element by element.

The significance of subgroups extends well beyond verification. Subgroups *partition* the parent group into equal-sized cosets, which is the content of Lagrange's theorem: the order of a subgroup divides the order of the group. This immediately constrains what subgroups can exist — a group of order 12 can have subgroups of order 1, 2, 3, 4, 6, or 12, but not 5. Normal subgroups (subgroups closed under conjugation) go further: they let you construct quotient groups by collapsing the subgroup to a single identity element. All of that structure begins with the basic question you're studying now: which subsets close up into groups?
