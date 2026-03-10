---
id: axiom-of-separation
title: Axiom Schema of Separation
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: zfc-axioms-overview
  type: hard
- id: first-order-logic-syntax
  type: soft
builds-toward:
- axiom-of-replacement
- von-neumann-ordinals
tags:
- ZFC
- separation
- comprehension
- specification
stage: formal-systems
status: draft
---

# Axiom Schema of Separation

## Core Idea
The axiom schema of separation (also called restricted comprehension or specification) states: for any set A and any first-order formula φ(x), the collection {x ∈ A : φ(x)} is a set. By requiring that new sets be carved out of an already-existing set A, separation avoids Russell's paradox: the paradoxical 'R' would require A to be the universal set, which ZFC never asserts exists. Separation is technically a schema — one axiom for each first-order formula φ — and is one of the primary tools for constructing subsets within ZFC.

## How It's Best Learned
Practice applying separation to construct specific sets: intersections A ∩ B = {x ∈ A : x ∈ B}, the set of even numbers within ℕ, and relative complements. Verify that each construction starts from an existing set. Then revisit Russell's paradox and identify exactly why separation prevents it.

## Common Misconceptions
- Separation does not let you form {x : P(x)} for arbitrary P — you must always start from an existing set A.
- The schema of separation does not assert that a universal set exists; in fact ZFC proves no universal set exists.
