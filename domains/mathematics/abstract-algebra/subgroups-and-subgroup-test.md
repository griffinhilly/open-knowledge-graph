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

## Questions

```yaml
- question: "Consider H = {e, (12), (13), (23)} in S₃ — all transpositions plus the identity. Every element is its own inverse, so H is closed under inverses, and e ∈ H. Is H a subgroup of S₃?"
  type: multiple-choice
  options:
    - "Yes, because it contains the identity and all its own inverses"
    - "No, because it fails closure: (12)∘(13) = (132) ∉ H"
    - "No, because associativity doesn't hold inside H"
    - "Yes, because |H| = 4 divides |S₃| = 6"
  answer: 1
  explanation: "H fails the closure axiom. Even though every element is self-inverse and the identity is present, (12)∘(13) = (132) ∉ H, so H is not a subgroup. This is the classic trap: inverses + identity does not imply closure."

- question: "In the one-step subgroup test, what does substituting a = b into the condition 'ab⁻¹ ∈ H for all a, b ∈ H' establish?"
  type: multiple-choice
  options:
    - "That the group operation is associative within H"
    - "That H is closed under the group operation"
    - "That the identity element e = aa⁻¹ belongs to H"
    - "That H is a normal subgroup of G"
  answer: 2
  explanation: "Setting a = b gives aa⁻¹ = e ∈ H, establishing that H contains the identity. From there, setting a = e (now known to be in H) shows b⁻¹ ∈ H (inverses), and replacing b with b⁻¹ recovers closure. One condition encodes all three axioms."

- question: "If H is a nonempty subset of a group G satisfying ab⁻¹ ∈ H for all a, b ∈ H, then the identity element of G must belong to H."
  type: true-false
  answer: true
  explanation: "Since H is nonempty, pick any a ∈ H. The condition with a = b gives aa⁻¹ = e ∈ H. The identity membership follows directly from the one-step test — you don't need to assume it separately."

- question: "Any nonempty subset of a group that contains the identity element and is closed under taking inverses is a subgroup."
  type: true-false
  answer: false
  explanation: "Closure under inverses and containing e are necessary but not sufficient. Closure under the group operation must also hold. The set {e, (12), (13), (23)} in S₃ has both properties yet is not a subgroup because it fails closure."

- question: "Explain how the single condition 'ab⁻¹ ∈ H for all a, b ∈ H' in the one-step subgroup test encodes all three subgroup axioms: identity, inverses, and closure."
  type: short-answer
  answer: "Setting a = b gives e = aa⁻¹ ∈ H (identity). With e ∈ H, setting a = e gives b⁻¹ = eb⁻¹ ∈ H (inverses). Finally, replacing b with b⁻¹ in the original condition gives a(b⁻¹)⁻¹ = ab ∈ H (closure). Three axioms are recovered from one condition by strategic substitution."
  explanation: "The key is that the condition is assumed to hold for ALL pairs a, b ∈ H — so particular choices of a and b extract each axiom in turn. Understanding this shows why the test is logically equivalent to the full definition, not a shortcut that misses something."
```

## Explainer

You've built up the group axioms — closure, associativity, identity, inverses — and seen them satisfied by groups like ℤ under addition and S_n under composition. A **subgroup** asks a natural question: when does a *subset* of a group form a group in its own right, under the same operation? This is the first tool for understanding the internal structure of a group, and the subgroup tests make verification efficient.

Start with a familiar example. The integers ℤ under addition form a group. The set 2ℤ = {…, −4, −2, 0, 2, 4, …} is a subset: the sum of two even integers is even (closure), 0 is even (identity), and the additive inverse of an even integer is even (inverses). Associativity is inherited from ℤ. So 2ℤ is a subgroup of ℤ. More generally, nℤ is a subgroup for any positive integer n. Subgroups can also fail: in S₃, the set {e, (12), (13), (23)} is *not* a subgroup because closure fails — (12)∘(13) = (132), which is not in the set.

The **one-step subgroup test** packages all the axioms into a single condition: a nonempty subset H is a subgroup of G if and only if for every a, b ∈ H, the element ab⁻¹ ∈ H. Setting a = b shows e = aa⁻¹ ∈ H (identity). Setting a = e (now known to be in H) shows b⁻¹ ∈ H (inverses exist). Replacing b by b⁻¹ and applying the condition gives a(b⁻¹)⁻¹ = ab ∈ H (closure). One condition, three axioms. The **two-step test** — verify closure directly and verify that inverses exist — is often more explicit for finite groups where you can check element by element.

The significance of subgroups extends well beyond verification. Subgroups *partition* the parent group into equal-sized cosets, which is the content of Lagrange's theorem: the order of a subgroup divides the order of the group. This immediately constrains what subgroups can exist — a group of order 12 can have subgroups of order 1, 2, 3, 4, 6, or 12, but not 5. Normal subgroups (subgroups closed under conjugation) go further: they let you construct quotient groups by collapsing the subgroup to a single identity element. All of that structure begins with the basic question you're studying now: which subsets close up into groups?
