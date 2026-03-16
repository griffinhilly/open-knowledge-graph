---
id: existential-closure-homomorphism
title: Existential Closure Under Homomorphisms
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: embedding-and-preservation-properties
  type: hard
- id: diagram-expansion-by-constants
  type: hard
- id: existential-formulas-embeddings
  type: soft
builds-toward:
- extension-lemma-embeddings
tags:
- existential
- closure
- preservation
- homomorphism
stage: abstract-reasoning
status: draft
---

# Existential Closure Under Homomorphisms

## Core Idea
If f: M → N is a homomorphism and φ(x) is an existential formula satisfied by some a in M, then φ(f(a)) is satisfied in N. This is the key property allowing us to push existential properties forward through homomorphisms, and it justifies why embeddings (injective homomorphisms reflecting existentials) are natural in model theory.

## Explainer

You already know that a homomorphism f: M → N between structures in the same language preserves atomic formulas: if M ⊨ R(a₁, …, aₙ), then N ⊨ R(f(a₁), …, f(aₙ)). Existential closure under homomorphisms extends this one step: homomorphisms also preserve **existential formulas** — formulas of the form ∃x₁ … ∃xₙ φ(x₁, …, xₙ, y) where φ is quantifier-free. The key insight is that an existential claim says "there exists something witnessing this property." If witnesses exist in M, their images under f exist in N and satisfy the same atomic conditions, because f preserves atomic truth.

To see why this works, trace through the logic. Suppose M ⊨ ∃x φ(x, a), witnessed by some element b ∈ M with M ⊨ φ(b, a). The formula φ is built from atoms using conjunctions, disjunctions, and negations — but not universal quantifiers. Since f preserves each atomic statement about b and a, and since existential-free Boolean combinations of preserved atomic facts remain preserved, we get N ⊨ φ(f(b), f(a)). Since f(b) exists in N, we get N ⊨ ∃x φ(x, f(a)). The existential witness is simply the image of the original witness.

Crucially, homomorphisms do *not* in general preserve **universal formulas** or **negated atomic formulas**. A homomorphism can collapse distinct elements (two elements of M may map to the same element of N), which can destroy universal claims and make false atoms true. For example, if M models "¬R(a,b)" and f(a) = f(b) in N, then N might model R(f(a), f(b)) anyway. This asymmetry explains why **embeddings** — injective homomorphisms — are more powerful: they reflect as well as preserve atomic facts, and thus preserve and reflect all quantifier-free formulas.

This property is not merely an abstract curiosity. It is the foundation for the diagram technique in model theory: the diagram of a structure M records all atomic facts about its elements, and the existence of a homomorphism from the diagram into N precisely corresponds to satisfying the existential consequences of M's theory. From your prerequisite work on diagram expansion, you know that adding constant symbols for each element of M allows you to state these facts as sentences — and a model of those sentences gives you a homomorphic image of M inside N. Existential closure under homomorphisms is what makes this technique work.
