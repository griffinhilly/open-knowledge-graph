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
