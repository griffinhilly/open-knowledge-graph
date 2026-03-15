---
id: model-instantiation-structures
title: Model Instantiation and Structure Realization
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: signature-and-vocabulary-model-theory
  type: hard
- id: model-interpretation-and-satisfaction
  type: hard
- id: set-fundamentals
  type: hard
- id: equivalence-relations-and-equivalence-classes
  type: soft
builds-toward:
- embedding-and-preservation-properties
- complete-theory-of-structures
tags:
- instantiation
- realization
- semantic-interpretation
- universe
stage: abstract-reasoning
status: draft
---

# Model Instantiation and Structure Realization

## Core Idea
A structure M (or model) in a signature σ assigns to each symbol in σ a concrete mathematical object: constants become elements, function symbols become operations, and relation symbols become sets of tuples. The universe (domain) of M is the non-empty set over which these interpretations are defined.

## How It's Best Learned
Work through explicit examples: the group (Z, +) as a model of the group signature, or (R, 0, 1, +, ·, <) as a model of the ordered field signature. Verify satisfaction of key axioms.

## Common Misconceptions
A structure is not an abstract syntax tree—it is a concrete assignment. Distinct structures can satisfy the same theory but differ in their interpretations of function/relation symbols.
