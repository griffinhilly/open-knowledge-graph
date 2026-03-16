---
id: embedding-and-preservation-properties
title: Embeddings and Preservation of Formulas
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-instantiation-structures
  type: hard
- id: structure-homomorphisms-embeddings
  type: hard
builds-toward:
- isomorphism-and-structural-equivalence
- existential-closure-homomorphism
tags:
- embedding
- preservation
- homomorphism
- formula-classes
stage: abstract-reasoning
status: draft
---

# Embeddings and Preservation of Formulas

## Core Idea
An embedding f: M → N is an injective homomorphism that preserves and reflects atomic formulas. Crucially, different formula classes are preserved under different morphism types: universal formulas survive under substructures, existential formulas survive under embeddings, and positive formulas survive under homomorphisms.

## How It's Best Learned
Prove that universal formulas are preserved under substructures by showing how a satisfying assignment in a substructure extends. Contrast with existential formulas, which can be false in a substructure despite being true in the parent.

## Explainer

You already know that a structure M consists of a domain together with interpretations of the symbols in a signature, and that a homomorphism f: M → N preserves the truth of atomic formulas — if R(a₁,...,aₙ) holds in M, then R(f(a₁),...,f(aₙ)) holds in N. An **embedding** strengthens this: it is an injective homomorphism that also *reflects* atomic formulas — R(f(a₁),...,f(aₙ)) holds in N only if R(a₁,...,aₙ) held in M. Intuitively, N "looks like" M near the image of f, with no accidental extra relationships. Embeddings make M isomorphic to a substructure of N.

The central result is the **preservation theorem**: different morphism types preserve different classes of formulas. **Universal sentences** (∀x φ(x) where φ is quantifier-free) are preserved under *substructures*. If ∀x φ(x) holds in N and M is a substructure of N, then ∀x φ(x) holds in M too — because every element of M is also in N, so the universal claim cannot fail. **Existential sentences** (∃x φ(x) with quantifier-free φ) go in the opposite direction: they are preserved under *extensions*. If ∃x φ(x) holds in M and M embeds into N, the witness still exists in N. But an existential sentence true in N need not hold in M: the witness might have been removed.

A concrete example clarifies the asymmetry. The sentence "every element has a multiplicative inverse" is universal-existential (∀x ∃y xy = 1), not purely universal. It holds in ℝ (the reals) but fails in ℤ (the integers), which is a substructure of ℝ. This shows that mixed quantifier sentences are *not* preserved downward into substructures — only purely universal sentences enjoy that guarantee. Similarly, "there exists an element of order 2" is existential, preserved upward from ℤ/2ℤ to any group extending it, but a subgroup might lack such an element entirely.

**Positive formulas** — built from atomic formulas using ∧, ∨, ∃, and ∀ with no negation — are preserved under *homomorphisms*, the weakest morphism type. This is the most general preservation result and underpins the model-theoretic analysis of constraint satisfaction: if a structure satisfies a set of positive constraints, any homomorphic image of it satisfies them too. Together, these three preservation results form a fundamental dictionary between syntactic formula classes and semantic morphism properties, and they are essential tools for understanding what structural operations can and cannot destroy about a theory.
