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

## Questions

```yaml
- question: "You want to verify that H = {even integers} is a subgroup of (ℤ, +). Which conditions do you actually need to check?"
  type: multiple-choice
  options:
    - "All four group axioms: closure, associativity, identity, and inverses"
    - "Nonemptiness, closure under addition, and closure under additive inverses"
    - "Only closure under addition, since identity and inverses follow automatically from it"
    - "Only that H is a nonempty subset of G"
  answer: 1
  explanation: "Associativity is inherited for free because H ⊆ G — any triple a, b, c ∈ H satisfies (a+b)+c = a+(b+c) in ℤ, hence in H. Identity is automatic once you have closure under operation and inverses: if a ∈ H then a⁻¹ ∈ H, and a + a⁻¹ = 0 ∈ H by closure. So the subgroup test reduces to exactly three conditions: nonemptiness, closure under the operation, and closure under inverses. Option C is wrong because closure under addition alone does not guarantee inverses (ℤ⁺ is closed under addition but is not a subgroup)."

- question: "Is the set of positive integers ℤ⁺ a subgroup of (ℝ, +)?"
  type: multiple-choice
  options:
    - "Yes — it is nonempty and closed under addition"
    - "No — it is not closed under addition (e.g., 3 + 5 ∉ ℤ⁺)"
    - "No — it does not contain the identity element 0"
    - "No — it fails closure under inverses (the additive inverse of 3 is −3, which is not in ℤ⁺)"
  answer: 3
  explanation: "ℤ⁺ is closed under addition (option A's premise is correct) — that's the tempting mistake. But the subgroup test also requires closure under inverses. For any n ∈ ℤ⁺, its additive inverse −n is negative, so −n ∉ ℤ⁺. The test fails here. Note that option C (no identity) is a consequence of the same failure: once you know inverses aren't present, the identity can't be in H either, but the root failure by the subgroup test is the inverse condition."

- question: "If H is a nonempty subset of a group G that is closed under the group operation and closed under taking inverses, then the identity element of G must also be in H."
  type: true-false
  answer: true
  explanation: "Take any element a ∈ H (possible since H is nonempty). By closure under inverses, a⁻¹ ∈ H. By closure under the operation, a · a⁻¹ = e ∈ H. So the identity is automatically present — you never need to check it separately. This is the elegance of the subgroup test: two conditions imply the third."

- question: "To confirm that a subset H of a group G is a subgroup, you must verify all four group axioms — closure, associativity, identity, and inverses — because H might not inherit properties from G."
  type: true-false
  answer: false
  explanation: "Associativity is always inherited for free. Since H ⊆ G uses the same operation as G, and associativity holds for all elements of G, it holds in particular for all elements of H. There is no way for associativity to fail in a subset of an associative group. The subgroup test requires only nonemptiness, closure under the operation, and closure under inverses — three conditions, not four."

- question: "Why does the subgroup test not require checking associativity, even though associativity is one of the four group axioms?"
  type: short-answer
  answer: "Associativity is inherited from the ambient group G. Since H ⊆ G and H uses the same binary operation, for any a, b, c ∈ H we also have a, b, c ∈ G, where (ab)c = a(bc) already holds. The same equation therefore holds in H. Associativity cannot fail in a subset of a group because it depends on the operation, not on which elements are present."
  explanation: "This insight is what makes the subgroup test economical. Rather than re-verifying all axioms, you exploit the fact that H 'borrows' associativity from G. Only the conditions that depend on which elements are in H — closure under the operation and closure under inverses — need to be checked. Identity then follows as a consequence of those two."
```

## Explainer

To verify that H is a subgroup of G, you might think you need to check all four group axioms: closure, associativity, identity, inverses. But three of those are essentially free — and understanding why reveals the elegant economy of the subgroup test.

**Associativity is inherited for free.** Since H ⊆ G and elements of H are also elements of G, associativity holds in H simply because it holds in G. You never need to check it separately. This is the key insight that reduces the subgroup verification from four conditions to two: closure under the operation, and closure under taking inverses. And once you have both of those (plus nonemptiness), the identity is automatic — if a ∈ H, then a⁻¹ ∈ H by closure under inverses, and then a·a⁻¹ = e, so e ∈ H by closure under the operation.

Concretely: the integers ℤ form a subgroup of (ℝ, +). Is this obvious? Check the test: ℤ is nonempty (contains 0, or 1, or any integer), the sum of two integers is an integer (closed under +), and the negative of an integer is an integer (closed under taking additive inverses). Done — no need to verify associativity of addition, which you already knew from ℝ. Now compare: the positive integers ℤ⁺ fail the test because ℤ⁺ is not closed under inverses (the additive inverse of 3 is −3, which is not positive). So ℤ⁺ is not a subgroup of (ℝ, +), even though it is closed under addition.

A useful variant is the **two-step subgroup test**: H is a subgroup if and only if (1) H is nonempty, (2) H is closed under the group operation, and (3) H is closed under taking inverses — stated as two separate conditions rather than one combined condition. Both formulations are equivalent. There is also a one-line version combining them: H ≤ G if and only if H ≠ ∅ and for all a, b ∈ H, ab⁻¹ ∈ H. This single condition packages closure and inverses together: setting a = b gives aa⁻¹ = e ∈ H (identity); setting a = e gives b⁻¹ ∈ H (inverses); and then ab⁻¹ using an inverse gives closure.

Subgroups are the building blocks of group theory. Every group homomorphism has a kernel that is a subgroup. Cosets are built from subgroups. Normal subgroups — subgroups whose left and right cosets coincide — are exactly the subgroups you can quotient by to form a new group. All of this begins with the simple question: which subsets of a group are themselves groups? The subgroup test gives you the fastest answer.
