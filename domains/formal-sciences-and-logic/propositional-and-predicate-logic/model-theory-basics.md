---
id: model-theory-basics
title: Basic Model Theory
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-semantics
  type: hard
- id: fol-soundness-completeness
  type: soft
- id: set-theory-basics
  type: soft
- id: equivalence-relations
  type: soft
- id: fol-compactness
  type: soft
- id: propositional-compactness
  type: soft
- id: set-fundamentals
  type: hard
- id: functions-and-function-properties
  type: hard
builds-toward:
- lowenheim-skolem-theorem
tags:
- model-theory
- theory
- elementary-equivalence
- categorical
- complete-theory
stage: formal-systems
status: validated
---
# Basic Model Theory

## Core Idea
Model theory studies the relationship between formal theories and the structures that satisfy them. A theory T is a set of sentences closed under logical consequence; a model of T is a structure where every sentence in T is true. Two structures are elementarily equivalent if they satisfy exactly the same first-order sentences. A theory is complete if for every sentence φ, either φ or ¬φ is in the theory; it is categorical in cardinality κ if all its models of cardinality κ are isomorphic. These concepts help characterize what first-order logic can and cannot express.

## How It's Best Learned
Work through examples of complete theories (dense linear orders without endpoints, algebraically closed fields) and incomplete theories (the theory of groups). Verify elementary equivalence by constructing back-and-forth systems.

## Common Misconceptions
- Elementary equivalence is weaker than isomorphism: two non-isomorphic structures can satisfy exactly the same first-order sentences.
- A complete theory can still have multiple non-isomorphic models (of different cardinalities).
