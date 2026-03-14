---
id: union-axiom
title: Axiom of Union
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: zfc-axioms-overview
  type: hard
- id: axiom-of-separation
  type: soft
builds-toward:
- ordinal-numbers-and-order
tags:
- union
- axiom
- ZFC
- set construction
stage: formal-systems
status: draft
---

# Axiom of Union

## Core Idea
The axiom of union states that for any set X, there exists a set ∪X whose members are exactly the elements of the elements of X: ∪X = {y : ∃z ∈ X, y ∈ z}. Applied to {A, B}, it yields the familiar A ∪ B. The axiom is essential for flattening nested set structures — it peels away one layer of braces. Combined with pairing (to form {A, B}) and separation (to carve out intersections and differences), it provides the full suite of Boolean set operations within ZFC.

## How It's Best Learned
Compute ∪X by hand for small examples: ∪{{1,2},{2,3}} = {1,2,3}, ∪{∅} = ∅, ∪∅ = ∅. Then verify that binary union A ∪ B = ∪{A, B} by tracing the definition. Practice distinguishing ∪X (the union axiom applied to a set of sets) from A ∪ B (the binary operation derived from it). Work through why arbitrary unions require an axiom rather than following from separation alone.

## Common Misconceptions
- The union axiom does not take two sets and combine them — it takes a single set of sets and flattens it by one level. Binary union is a derived operation.
- ∪∅ = ∅ is valid and follows directly from the definition, since no element has any member of ∅ as a witness.
