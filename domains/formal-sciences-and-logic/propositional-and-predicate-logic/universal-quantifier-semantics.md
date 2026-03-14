---
id: universal-quantifier-semantics
title: 'Universal Quantification: Meaning and Scope'
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: quantifier-notation-and-basics
  type: hard
builds-toward:
- free-variables-and-bound-variables
- substitution-and-instantiation
tags:
- semantics
- quantifiers
- first-order-logic
stage: formal-systems
status: draft
---

# Universal Quantification: Meaning and Scope

## Core Idea
∀x φ(x) is true in a structure iff φ(a) is true for every object a in the domain. The universal quantifier is the logical analog of conjunction over all objects. Scope interactions (∀x ∃y vs. ∃y ∀x) are crucial: different quantifier orderings yield different truth conditions.

## How It's Best Learned
Work with small finite domains and verify universal statements. Observe how changing domain size affects truth values.
