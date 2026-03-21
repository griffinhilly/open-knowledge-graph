---
id: complete-theory-of-structures
title: Complete Theory and Consequence Relations
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-instantiation-structures
  type: hard
- id: logical-consequence-and-entailment
  type: hard
- id: complete-first-order-theories
  type: hard
builds-toward:
- elementary-equivalence-and-logical-indistinguishability
- vaught-theorem-on-models
tags:
- complete-theory
- Th(M)
- consequence
- deduction
stage: advanced
status: draft
---

# Complete Theory and Consequence Relations

## Core Idea
The complete theory Th(M) of a structure M is the set of all first-order sentences true in M. Every sentence is either in Th(M) or its negation is—this ensures completeness. Th(M) determines which other structures satisfy the same theory and provides a canonical object for studying M's first-order properties.

## How It's Best Learned
Compute Th(M) for concrete structures: what sentences are in Th(Q, <)? What about Th(Z, <)? Notice how different structures can have the same complete theory.

## Questions

```yaml
- question: "Structures M and N satisfy exactly the same first-order sentences. Which of the following must be true?"
  type: multiple-choice
  options:
    - "M and N are isomorphic, since identical first-order behavior implies identical structure"
    - "M and N are elementarily equivalent, but need not be isomorphic"
    - "Th(M) and Th(N) are different, since distinct structures have distinct theories"
    - "M and N share some but not all first-order sentences, since complete theories can overlap"
  answer: 1
  explanation: "Two structures satisfying the same first-order sentences are elementarily equivalent by definition (Th(M) = Th(N)). But elementary equivalence does not imply isomorphism — ℚ and any non-standard dense linear order without endpoints are elementarily equivalent but not isomorphic. The key point is that first-order logic cannot always distinguish non-isomorphic structures; elementary equivalence is a strictly coarser relation."

- question: "The Euclidean algorithm shows that ℤ and ℚ, both ordered under <, have properties in common. A student claims Th(ℤ, <) = Th(ℚ, <) since both are linear orders without greatest element. What is wrong?"
  type: multiple-choice
  options:
    - "The claim is correct — both structures have the same complete theory"
    - "The claim is wrong because ℤ lacks an ordering relation"
    - "The claim is wrong because ℚ satisfies 'between any two elements there is another,' which ℤ does not — so their complete theories differ"
    - "The claim is wrong because Th(M) can only be defined for finite structures"
  answer: 2
  explanation: "ℚ is a dense linear order: between any two rationals there is another. ℤ does not have this property — there is nothing between 1 and 2. This is a first-order sentence that is true in ℚ but false in ℤ, so it belongs to Th(ℚ, <) but not Th(ℤ, <). Finding a single sentence with different truth values in two structures is all it takes to prove their complete theories differ."

- question: "The complete theory Th(M) of any structure M is a complete theory, meaning for every sentence φ, either φ ∈ Th(M) or ¬φ ∈ Th(M)."
  type: true-false
  answer: true
  explanation: "Every first-order sentence is either true or false in M — there is no third option. If φ is true in M, then φ ∈ Th(M). If φ is false in M, then ¬φ is true in M, so ¬φ ∈ Th(M). This totality is exactly what makes Th(M) complete: no sentence is left undecided."

- question: "If two structures are isomorphic, they may have different complete theories depending on how the isomorphism is defined."
  type: true-false
  answer: false
  explanation: "Isomorphic structures always have the same complete theory. An isomorphism is a bijection that preserves all the structure (relations, functions, constants), so any sentence true in one structure is true in the other. Th(M) = Th(N) is a consequence of isomorphism. The reverse does not hold — Th(M) = Th(N) does not imply isomorphism — but the forward direction is a basic theorem."

- question: "Why is elementary equivalence a strictly coarser relation than isomorphism, and what does this tell us about the expressive power of first-order logic?"
  type: short-answer
  answer: "Elementary equivalence (same complete theory) is coarser because non-isomorphic structures can satisfy exactly the same first-order sentences. Isomorphism implies elementary equivalence, but not vice versa. This shows that first-order logic is expressively limited: it cannot always distinguish structures that differ in ways first-order sentences cannot capture, such as cardinality differences between countable dense linear orders."
  explanation: "The classic example is Cantor's theorem that all countable dense linear orders without endpoints are isomorphic — so ℚ and the set of irrationals as ordered sets have the same complete theory even though they are structurally different as sets. First-order logic cannot say 'there are uncountably many elements' in a single sentence, so it cannot distinguish structures that differ only in cardinality beyond what can be captured finitely."
```

## Explainer

From your study of model instantiation and logical consequence, you know that a **structure** M assigns interpretations to the symbols of a language — domains, relations, functions, constants — and that a sentence φ is true or false in M according to these interpretations. The **complete theory** Th(M) of a structure M is simply the set of all sentences true in M: Th(M) = {φ : M ⊨ φ}. Every sentence is either in Th(M) (it is true in M) or its negation is (φ is false in M, so ¬φ is true). This totality — no sentence left undecided — is exactly what "complete" means.

Think of Th(M) as the complete first-order portrait of M. The integers (ℤ, <) satisfy "every element has a successor" and "there is no least element"; the rationals (ℚ, <) satisfy both of these and also "between any two elements there is another." These are different sentences with different truth values in ℤ and ℚ, so Th(ℤ, <) ≠ Th(ℚ, <). In contrast, any two **dense linear orders without endpoints** — like ℚ and the irrational numbers — satisfy exactly the same first-order sentences, so they have the same complete theory. This is not obvious from the structures themselves (ℚ and the irrationals look very different) but follows from Cantor's back-and-forth argument, which shows any two countable dense linear orders without endpoints are isomorphic.

The consequence relation connects to Th(M) in a precise way. A sentence φ is a **logical consequence** of Th(M) — written Th(M) ⊨ φ — if and only if φ is already in Th(M). Since Th(M) is complete, there is no ambiguity: every sentence is settled. For a weaker theory T (a set of axioms not derived from a single structure), T is called complete if no sentence is left undecided by T — that is, if T ⊨ φ or T ⊨ ¬φ for every sentence φ. An axiom system that happens to pin down a single structure up to elementary equivalence will have Th(M) as its unique complete extension, which is the goal of axiomatizing a structure.

The key application is **elementary equivalence**: two structures M and N are elementarily equivalent if Th(M) = Th(N) — they satisfy exactly the same first-order sentences. Elementary equivalence is coarser than isomorphism (isomorphic structures are always elementarily equivalent, but not vice versa). The rationals and a non-standard dense linear order without endpoints are elementarily equivalent but not isomorphic. Th(M) thus partitions all structures into equivalence classes, and model theory studies what first-order logic can and cannot distinguish. Understanding Th(M) as an object — what axioms generate it, how it behaves under extensions, whether it is decidable — is the foundation for all deeper model-theoretic investigation.

