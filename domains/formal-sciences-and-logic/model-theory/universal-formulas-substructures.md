---
id: universal-formulas-substructures
title: Universal Formulas and Preservation under Substructures
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: model-interpretation-and-satisfaction
  type: hard
builds-toward:
- model-completeness-theorems
- quantifier-elimination-decidability
tags:
- universal-formulas
- preservation
- homomorphisms
stage: expert
status: validated
---

# Universal Formulas and Preservation under Substructures

## Core Idea
A universal formula (of the form ∀x φ where φ is quantifier-free) is preserved under substructures: if a universal formula holds in a substructure, it holds in the parent. This preservation property characterizes which sentences describe properties that propagate upward through the substructure ordering and is fundamental to understanding model-completeness.

## Questions

```yaml
- question: "Suppose B is a structure satisfying ∀x ∀y (x + y = y + x) (commutativity). If A is a substructure of B, which statement is correct?"
  type: multiple-choice
  options:
    - "A also satisfies commutativity, because the universal formula is preserved going to substructures"
    - "A may or may not satisfy commutativity — substructures can violate properties of the parent"
    - "A satisfies commutativity only if A has the same cardinality as B"
    - "Whether A satisfies commutativity depends on the specific operation, not on the logical form of the formula"
  answer: 0
  explanation: "Commutativity ∀x ∀y (x + y = y + x) is a universal sentence (universal quantifiers over a quantifier-free matrix). The preservation theorem says: if a universal sentence holds in B and A is a substructure of B, then it holds in A. The argument is direct: every element of A is also in B, and for any a₁, a₂ ∈ A, commutativity holds for a₁ and a₂ in B (since they are also elements of B), and since A inherits the same operation, it holds in A. Option B would be correct for existential sentences, not universal ones."

- question: "A group G satisfies the identity axiom: ∃e ∀x (e·x = x·e = x). A substructure A ⊆ G is closed under the group operation. Which claim about the identity axiom in A is best supported?"
  type: multiple-choice
  options:
    - "A necessarily satisfies the identity axiom, because universal formulas are preserved under substructures"
    - "The identity axiom is existential, so it is preserved upward from substructures to superstructures, not downward — A is not guaranteed to satisfy it from logic alone"
    - "A satisfies the identity axiom if and only if A has finite cardinality"
    - "The identity axiom is universal and therefore automatically satisfied by A"
  answer: 1
  explanation: "The identity axiom begins with ∃e — it is an existential sentence. Existential sentences are preserved going UPWARD (from substructures to superstructures), not downward. Logic alone does not guarantee that A contains the identity element or any identity at all. In practice, subgroups of a group do contain the group identity (by the subgroup definition), but this is an additional structural requirement, not a consequence of the logical form. Option A is wrong because the identity axiom is existential, not universal. Option D misidentifies the quantifier form."

- question: "If an existential sentence ∃x φ(x) holds in a structure A and B is a superstructure of A (A ⊆ B), then ∃x φ(x) also holds in B."
  type: true-false
  answer: true
  explanation: "Existential sentences are preserved going upward: if some element a ∈ A satisfies φ(a), and A ⊆ B so a ∈ B as well, then B also contains a witness for ∃x φ(x). The quantifier-free φ is satisfied by a in A because A and B agree on all relations and functions restricted to elements of A (this is what 'substructure' means). So the existential witness carries forward. This is the dual of universal preservation: ∀-sentences go down (to substructures); ∃-sentences go up (to superstructures)."

- question: "If a universal sentence holds in a substructure A, it is expected to also hold in any superstructure B containing A."
  type: true-false
  answer: false
  explanation: "This reverses the direction of preservation. Universal sentences are preserved going DOWNWARD — from B to A — not upward. If ∀x φ(x) holds in B, then it holds in A (any element of A is in B and satisfies φ). But the converse fails: B might contain elements outside A that violate φ, even if all elements of A satisfy it. For example, the sentence ∀x (x = 0) holds in the substructure {0} of the integers, but obviously fails in the integers themselves. Universal preservation is strictly one-directional."

- question: "Explain why universal formulas are preserved under substructures (going from a larger structure to a smaller one) but existential formulas are not. Use the definition of substructure in your answer."
  type: short-answer
  answer: "A substructure A of B has A's domain ⊆ B's domain, and all relations and functions on A are restrictions of those on B. For a universal sentence ∀x φ(x): if it holds in B, then for every element b ∈ B, φ(b) holds. Since every a ∈ A is also in B, φ(a) holds, and since φ is quantifier-free (checked only using relations/functions that A inherits from B), it holds in A too. For an existential sentence ∃x φ(x): even if it holds in B via some witness b ∈ B, that witness might be in B but not in A. A has fewer elements, so it may simply not contain the witness. There is no guarantee φ holds for any element of A."
  explanation: "The proof direction matters: the key move for universal sentences is 'every element of A is an element of B, so the universal claim still applies.' For existential sentences, the failure direction is 'B's witness might not be in A.' Students who understand this asymmetry — and why it follows from the definition of substructure — have grasped the core of preservation theory."
```

## Explainer

From first-order logic syntax, you know that formulas are built from atomic predicates using logical connectives (¬, ∧, ∨, →) and quantifiers (∀, ∃). A **quantifier-free formula** uses only connectives — no quantifiers at all. A **universal formula** (also written Π₁) prefixes a block of universal quantifiers in front of a quantifier-free matrix: ∀x₁ ∀x₂ … ∀xₙ φ(x₁,…,xₙ). The name comes from the fact that all variables are universally bounded. Universal formulas contrast with **existential formulas** (Σ₁), which prefix a block of existential quantifiers: ∃x₁…∃xₙ φ.

The core preservation fact is straightforward to prove once you think about it carefully. Suppose A is a substructure of B — meaning A is a structure with the same signature, A's domain is a subset of B's domain, and all relations and functions on A are restrictions of those on B. Now suppose the universal sentence ∀x φ(x) holds in A. Does it hold in B? Not necessarily: B might contain elements not in A that violate φ. But the reverse direction is what's true: if ∀x φ(x) holds in B, it holds in A. Because A ⊆ B, every element of A is also an element of B, and the quantifier-free formula φ is checked on those specific elements — and quantifier-free formulas are preserved under substructures since they only involve checking relations and functions, which A inherits from B. So ∀x φ holds in B ⇒ it holds in A. In other words, universal sentences are **preserved going to substructures** (from B down to A), while existential sentences are **preserved going to superstructures** (from A up to B).

A concrete example: the group axiom ∀x ∀y ∀z (x·(y·z) = (x·y)·z) is universal. If a set B with an operation is an associative structure, then any substructure A inherits associativity — you are just restricting which elements you check, and they still satisfy the universal claim. By contrast, the axiom ∃e ∀x (e·x = x) — the existence of an identity — is existential. A subgroup inherits the identity from the parent group, but not because universal-formulas force it; rather, this is an additional property that happens to be preserved for groups because the identity of the parent group lies in every subgroup (by definition). If you dropped that definition requirement, you could have a sub-semigroup without an identity.

The **Łoś–Tarski theorem** (preservation theorem) states the converse: a sentence is preserved under substructures if and only if it is logically equivalent to a universal sentence. This gives a semantic characterization of the universal fragment — preservation is not just a proof trick but the defining property. The connection to model-completeness is direct: a theory T is model-complete if and only if every formula is T-equivalent to a universal formula. Preservation under substructures thus becomes the bridge between the syntactic definition of universal formulas and the semantic notion of model-completeness, linking formula structure to structural behavior in models.

