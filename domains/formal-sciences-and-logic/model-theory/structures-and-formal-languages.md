---
id: structures-and-formal-languages
title: Structures and Formal Languages
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: set-fundamentals
  type: soft
- id: binary-relations
  type: soft
- id: functions-and-function-properties
  type: soft
- id: functions-and-mappings-formal
  type: hard
- id: ordered-pairs-and-tuples
  type: soft
builds-toward:
- model-interpretation-and-satisfaction
- structure-homomorphisms-embeddings
tags:
- signature
- structure
- interpretation
- domain
- arity
stage: advanced
status: draft
---

# Structures and Formal Languages

## Core Idea
A signature specifies the vocabulary of a formal language by listing constant symbols, function symbols with specified arities, and relation symbols with specified arities. A structure over a signature assigns concrete meaning by providing a non-empty domain and interpretations of all symbols in the language. This separation of abstract syntax from concrete semantics is foundational to model-theoretic analysis.
