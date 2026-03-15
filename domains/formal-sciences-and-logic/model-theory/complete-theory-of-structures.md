---
id: complete-theory-of-structures
title: Complete Theory and Consequence Relations
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-instantiation-structures
  type: hard
- id: logical-consequence-and-entailment
  type: hard
- id: complete-first-order-theories
  type: hard
builds-toward:
- elementary-equivalence-and-logical-indistinguishability
- vaught-theorem-on-models
tags:
- complete-theory
- Th(M)
- consequence
- deduction
stage: abstract-reasoning
status: draft
---

# Complete Theory and Consequence Relations

## Core Idea
The complete theory Th(M) of a structure M is the set of all first-order sentences true in M. Every sentence is either in Th(M) or its negation is—this ensures completeness. Th(M) determines which other structures satisfy the same theory and provides a canonical object for studying M's first-order properties.

## How It's Best Learned
Compute Th(M) for concrete structures: what sentences are in Th(Q, <)? What about Th(Z, <)? Notice how different structures can have the same complete theory.
