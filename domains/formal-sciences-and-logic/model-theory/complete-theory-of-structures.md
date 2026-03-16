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
stage: abstract-reasoning
status: draft
---

# Complete Theory and Consequence Relations

## Core Idea
The complete theory Th(M) of a structure M is the set of all first-order sentences true in M. Every sentence is either in Th(M) or its negation is—this ensures completeness. Th(M) determines which other structures satisfy the same theory and provides a canonical object for studying M's first-order properties.

## How It's Best Learned
Compute Th(M) for concrete structures: what sentences are in Th(Q, <)? What about Th(Z, <)? Notice how different structures can have the same complete theory.

## Explainer

From your study of model instantiation and logical consequence, you know that a **structure** M assigns interpretations to the symbols of a language — domains, relations, functions, constants — and that a sentence φ is true or false in M according to these interpretations. The **complete theory** Th(M) of a structure M is simply the set of all sentences true in M: Th(M) = {φ : M ⊨ φ}. Every sentence is either in Th(M) (it is true in M) or its negation is (φ is false in M, so ¬φ is true). This totality — no sentence left undecided — is exactly what "complete" means.

Think of Th(M) as the complete first-order portrait of M. The integers (ℤ, <) satisfy "every element has a successor" and "there is no least element"; the rationals (ℚ, <) satisfy both of these and also "between any two elements there is another." These are different sentences with different truth values in ℤ and ℚ, so Th(ℤ, <) ≠ Th(ℚ, <). In contrast, any two **dense linear orders without endpoints** — like ℚ and the irrational numbers — satisfy exactly the same first-order sentences, so they have the same complete theory. This is not obvious from the structures themselves (ℚ and the irrationals look very different) but follows from Cantor's back-and-forth argument, which shows any two countable dense linear orders without endpoints are isomorphic.

The consequence relation connects to Th(M) in a precise way. A sentence φ is a **logical consequence** of Th(M) — written Th(M) ⊨ φ — if and only if φ is already in Th(M). Since Th(M) is complete, there is no ambiguity: every sentence is settled. For a weaker theory T (a set of axioms not derived from a single structure), T is called complete if no sentence is left undecided by T — that is, if T ⊨ φ or T ⊨ ¬φ for every sentence φ. An axiom system that happens to pin down a single structure up to elementary equivalence will have Th(M) as its unique complete extension, which is the goal of axiomatizing a structure.

The key application is **elementary equivalence**: two structures M and N are elementarily equivalent if Th(M) = Th(N) — they satisfy exactly the same first-order sentences. Elementary equivalence is coarser than isomorphism (isomorphic structures are always elementarily equivalent, but not vice versa). The rationals and a non-standard dense linear order without endpoints are elementarily equivalent but not isomorphic. Th(M) thus partitions all structures into equivalence classes, and model theory studies what first-order logic can and cannot distinguish. Understanding Th(M) as an object — what axioms generate it, how it behaves under extensions, whether it is decidable — is the foundation for all deeper model-theoretic investigation.

