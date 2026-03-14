---
id: axiom-of-replacement
title: Axiom Schema of Replacement
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: zfc-axioms-overview
  type: hard
- id: first-order-logic-syntax
  type: soft
- id: axiom-of-separation
  type: soft
builds-toward:
- transfinite-recursion
- von-neumann-ordinals
tags:
- ZFC
- replacement
- image
- class function
- schema
stage: formal-systems
status: validated
---

# Axiom Schema of Replacement

## Core Idea
The axiom schema of replacement asserts that if φ(x, y) defines a class function (for each x in a set A, there is exactly one y with φ(x, y)), then the image {y : ∃x ∈ A, φ(x, y)} is a set. Replacement strictly extends separation: it permits constructing sets like {ω, P(ω), P(P(ω)), ...} that lie beyond any single level of the hierarchy reachable by separation alone. It is indispensable for defining the ordinal hierarchy via transfinite recursion and for proving key results about cardinal arithmetic.

## How It's Best Learned
Compare what can be built using only separation versus using replacement. Key example: define the sequence ω, ω+1, ω+2, ... and show that separation alone cannot guarantee this image is a set. Work through the formal statement of the schema carefully and see why the 'exactly one y' (functionality) condition is necessary.

## Common Misconceptions
- Replacement requires φ to be functional — for each x there is a unique y. If φ is merely a relation, the image need not be a set.
- Replacement does not follow from separation and the other basic axioms; it is genuinely stronger and essential for transfinite mathematics.
