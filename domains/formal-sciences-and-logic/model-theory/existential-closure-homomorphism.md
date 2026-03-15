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
