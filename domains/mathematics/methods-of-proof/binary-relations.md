---
id: binary-relations
title: Binary Relations
domain: mathematics
course: methods-of-proof
prerequisites:
- id: cartesian-product
  type: hard
- id: set-theory-basics
  type: hard
builds-toward:
- equivalence-relations
- partial-orders
- injective-surjective-bijective
tags:
- relations
- binary-relation
- reflexive
- symmetric
- transitive
- antisymmetric
stage: formal-systems
status: validated
---

# Binary Relations

## Core Idea
A binary relation R on a set A is a subset of A × A; we write aRb or (a, b) ∈ R. Key properties: R is reflexive if aRa for all a; symmetric if aRb implies bRa; antisymmetric if aRb and bRa implies a = b; and transitive if aRb and bRc implies aRc. These four properties form the building blocks for classifying the most important types of relations — equivalence relations and partial orders.

## How It's Best Learned
Work with concrete relations on small sets represented as directed graphs or matrices. For each relation, check all four properties systematically. Compare 'divides' (reflexive, antisymmetric, transitive) to 'less than' (irreflexive, antisymmetric, transitive) to 'same parity as' (reflexive, symmetric, transitive).

## Common Misconceptions
- Assuming all relations are either symmetric or antisymmetric — a relation can be neither.
- Confusing a relation with a function — a relation is any subset of A × A, with no restrictions.
- Checking transitivity only on a few pairs rather than verifying for all applicable triples.
