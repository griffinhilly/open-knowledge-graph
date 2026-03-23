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
stage: expert
status: validated
---

# Embeddings and Preservation of Formulas

## Core Idea
An embedding f: M → N is an injective homomorphism that preserves and reflects atomic formulas. Crucially, different formula classes are preserved under different morphism types: universal formulas survive under substructures, existential formulas survive under embeddings, and positive formulas survive under homomorphisms.

## How It's Best Learned
Prove that universal formulas are preserved under substructures by showing how a satisfying assignment in a substructure extends. Contrast with existential formulas, which can be false in a substructure despite being true in the parent.

## Questions

```yaml
- question: "The sentence 'every element has a multiplicative inverse' (∀x ∃y xy = 1) holds in ℝ (the reals). Does it hold in ℤ (the integers), which is a substructure of ℝ?"
  type: multiple-choice
  options:
    - "Yes — universal sentences are always preserved downward into substructures"
    - "No — this sentence is not purely universal (it contains an embedded existential), so preservation under substructures is not guaranteed"
    - "Yes — existential sentences are preserved upward, so any substructure inheriting ℝ will satisfy them"
    - "No — ℤ is not a legitimate substructure of ℝ because multiplication behaves differently"
  answer: 1
  explanation: "The sentence ∀x ∃y xy = 1 is universally-existentially quantified (∀∃), not purely universal. The preservation theorem guarantees that *purely universal* sentences (∀x φ(x) with quantifier-free φ) are preserved downward into substructures — but this guarantee does not extend to mixed quantifier sentences. And indeed it fails here: in ℤ, the integer 2 has no multiplicative inverse (1/2 ∉ ℤ). The witness y = 1/x exists in ℝ but was removed when we restricted to ℤ."

- question: "Structure M satisfies the existential sentence ∃x R(x,x), and M embeds injectively into structure N. Which conclusion is guaranteed by the preservation theorem?"
  type: multiple-choice
  options:
    - "N also satisfies ∃x R(x,x) — the witness from M is still present in the image of M in N"
    - "Every substructure of M also satisfies ∃x R(x,x)"
    - "M and N satisfy exactly the same sentences"
    - "M is isomorphic to N"
  answer: 0
  explanation: "Existential sentences are preserved under embeddings (extensions). If ∃x R(x,x) holds in M — say element a witnesses R(a,a) — then after embedding f: M → N, the element f(a) still exists in N and R(f(a),f(a)) holds (because embeddings preserve atomic formulas). So N inherits the existential witness. Option B is wrong: existential sentences go *upward* under extensions, not downward; a substructure of M might lack the witness. Option C is much stronger than what the preservation theorem guarantees."

- question: "If a purely universal sentence holds in a substructure M of N, then it must also hold in the larger structure N."
  type: true-false
  answer: false
  explanation: "False — the direction is reversed. Universal sentences are preserved *downward*: if ∀x φ(x) holds in N, then it holds in every substructure M of N (because M has fewer elements and each one is already in N where φ holds). But the reverse is not guaranteed. A purely universal sentence might hold in M simply because M lacks the counterexample elements — those elements might exist in N. For example, 'every element squared is non-negative' holds in ℝ (as a substructure of ℂ), but ℂ contains elements like i where i² = −1 < 0, violating it."

- question: "Positive formulas — built from atomic formulas using conjunction, disjunction, and quantifiers, but without any negation — are preserved under homomorphisms, even non-injective ones."
  type: true-false
  answer: true
  explanation: "True. This is the most general of the three preservation results. A homomorphism f: M → N preserves the truth of atomic formulas (by definition). Since positive formulas are built only from operations that respect this — ∧ (and), ∨ (or), ∃ (existential), ∀ (universal) without negation — their truth is inherited by the homomorphic image. Negation would break this: if ¬R(a) holds in M but f is not injective, R(f(a)) might hold in N. The absence of negation is exactly what makes positive formulas preserved under the weakest morphism type."

- question: "Explain the key directional asymmetry between universal and existential sentences in the preservation theorem, and why the asymmetry goes in opposite directions."
  type: short-answer
  answer: "Universal sentences are preserved *downward* into substructures: if ∀x φ(x) holds in N, it holds in every substructure M — M has fewer elements, so nothing new can violate the universal claim. Existential sentences are preserved *upward* under extensions: if ∃x φ(x) holds in M, any N that extends M retains the witness. But a substructure might have lost the existential witness, and a superstructure might introduce new elements that violate the universal claim. The asymmetry reflects what gets added versus removed when moving between structures."
  explanation: "Intuition: a universal claim is a constraint — 'nothing violates φ.' Removing elements (going to a substructure) cannot create a violation, but adding elements can. An existential claim is an existence assertion — 'something satisfies φ.' Adding elements cannot destroy a witness, but removing them can. This neat duality is why the preservation theorem is stated in terms of direction: ∀-sentences go down (to substructures), ∃-sentences go up (to extensions), and ∀∃-sentences (like most interesting mathematical statements) are preserved in neither direction unconditionally."
```

## Explainer

You already know that a structure M consists of a domain together with interpretations of the symbols in a signature, and that a homomorphism f: M → N preserves the truth of atomic formulas — if R(a₁,...,aₙ) holds in M, then R(f(a₁),...,f(aₙ)) holds in N. An **embedding** strengthens this: it is an injective homomorphism that also *reflects* atomic formulas — R(f(a₁),...,f(aₙ)) holds in N only if R(a₁,...,aₙ) held in M. Intuitively, N "looks like" M near the image of f, with no accidental extra relationships. Embeddings make M isomorphic to a substructure of N.

The central result is the **preservation theorem**: different morphism types preserve different classes of formulas. **Universal sentences** (∀x φ(x) where φ is quantifier-free) are preserved under *substructures*. If ∀x φ(x) holds in N and M is a substructure of N, then ∀x φ(x) holds in M too — because every element of M is also in N, so the universal claim cannot fail. **Existential sentences** (∃x φ(x) with quantifier-free φ) go in the opposite direction: they are preserved under *extensions*. If ∃x φ(x) holds in M and M embeds into N, the witness still exists in N. But an existential sentence true in N need not hold in M: the witness might have been removed.

A concrete example clarifies the asymmetry. The sentence "every element has a multiplicative inverse" is universal-existential (∀x ∃y xy = 1), not purely universal. It holds in ℝ (the reals) but fails in ℤ (the integers), which is a substructure of ℝ. This shows that mixed quantifier sentences are *not* preserved downward into substructures — only purely universal sentences enjoy that guarantee. Similarly, "there exists an element of order 2" is existential, preserved upward from ℤ/2ℤ to any group extending it, but a subgroup might lack such an element entirely.

**Positive formulas** — built from atomic formulas using ∧, ∨, ∃, and ∀ with no negation — are preserved under *homomorphisms*, the weakest morphism type. This is the most general preservation result and underpins the model-theoretic analysis of constraint satisfaction: if a structure satisfies a set of positive constraints, any homomorphic image of it satisfies them too. Together, these three preservation results form a fundamental dictionary between syntactic formula classes and semantic morphism properties, and they are essential tools for understanding what structural operations can and cannot destroy about a theory.
