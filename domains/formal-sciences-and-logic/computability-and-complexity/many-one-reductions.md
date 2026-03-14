---
id: many-one-reductions
title: Many-One Reductions and Undecidability Proofs
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: undecidable-problems-examples
  type: hard
- id: computability-reductions
  type: hard
builds-toward:
- turing-degrees-equivalence
- np-hardness
tags:
- reductions
- undecidability
- proof-technique
stage: advanced
status: draft
---

# Many-One Reductions and Undecidability Proofs

## Core Idea
A many-one reduction from problem A to problem B is a total computable function that maps instances of A to instances of B, preserving the yes/no answer. If A is undecidable and there is a many-one reduction from A to B, then B is also undecidable. This technique systematically proves vast families of problems undecidable.
