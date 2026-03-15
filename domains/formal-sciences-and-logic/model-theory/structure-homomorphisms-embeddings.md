---
id: structure-homomorphisms-embeddings
title: Structure Homomorphisms and Embeddings
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: structures-and-formal-languages
  type: hard
- id: functions-and-mappings-formal
  type: soft
- id: binary-relations-definition-and-properties
  type: soft
builds-toward:
- elementary-equivalence-indistinguishability
tags:
- homomorphism
- embedding
- morphism
- isomorphism
- preservation
stage: advanced
status: draft
---

# Structure Homomorphisms and Embeddings

## Core Idea
A homomorphism between two structures is a map that respects the interpretation: constants map to constants, functions commute (f(φ(a)) = φ(f(a))), and positive relations are preserved. Embeddings are injective homomorphisms that also preserve all relations, not just positive ones. These maps generalize familiar group and ring homomorphisms to arbitrary relational structures.
