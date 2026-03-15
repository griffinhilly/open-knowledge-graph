---
id: extension-lemma-embeddings
title: Extension Lemma for Embeddings
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: existential-closure-homomorphism
  type: hard
- id: diagram-expansion-by-constants
  type: hard
- id: compactness-theorem-model-theory
  type: soft
builds-toward:
- universal-homogeneous-models
- amalgamation-construction-extensions
tags:
- extension
- embedding
- homomorphism-extension
- partial-map
stage: abstract-reasoning
status: draft
---

# Extension Lemma for Embeddings

## Core Idea
The extension lemma states that a partial embedding f: A → M (where A ⊂ M) can be extended to an embedding of a larger set into a sufficiently large structure. This is proved using the compactness theorem applied to the diagram of M with constants for elements of A. Extension lemmas are foundational for all amalgamation constructions.

## How It's Best Learned
Prove the extension lemma from compactness for a specific example: extending an embedding of Q into itself to an embedding of an algebraic extension.
