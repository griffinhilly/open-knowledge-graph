---
id: skolem-functions-and-witnesses
title: Skolem Functions and Witness Functions
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: lowenheim-skolem-downward
  type: hard
builds-toward:
- saturated-models-and-realization
- ultraproducts-of-structures
tags:
- Skolem function
- witness
- existential elimination
- Herbrand
stage: advanced
status: draft
---

# Skolem Functions and Witness Functions

## Core Idea
For each existential quantification ∃x φ(x, y), a Skolem function f(y) assigns a witness such that f(y) satisfies φ(f(y), y) whenever such a witness exists. Skolem functions systematically convert existential statements into functional dependencies, eliminating quantifiers constructively. They are central to proofs of Löwenheim-Skolem and compactness.
