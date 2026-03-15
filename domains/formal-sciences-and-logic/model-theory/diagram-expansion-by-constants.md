---
id: diagram-expansion-by-constants
title: Diagram and Expansion by Constants
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-instantiation-structures
  type: hard
- id: signature-and-vocabulary-model-theory
  type: hard
builds-toward:
- existential-closure-homomorphism
- extension-lemma-embeddings
tags:
- diagram
- expansion
- constants
- language-extension
stage: abstract-reasoning
status: draft
---

# Diagram and Expansion by Constants

## Core Idea
The diagram of a structure M is formed by expanding the signature with a constant symbol for each element of M, then taking all atomic sentences true in M. The expanded theory allows explicit reference to elements and is crucial for proving extension lemmas and building homomorphism extensions.

## How It's Best Learned
Write out the diagram of a small structure like Z_3 (integers mod 3) with constants for each element, then extend embeddings using the diagram.
