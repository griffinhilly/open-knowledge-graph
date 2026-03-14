---
id: many-one-and-turing-reductions
title: Many-One and Turing Reducibility
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: computability-reductions
  type: hard
- id: polynomial-time-reductions
  type: soft
tags:
- reductions
- hardness
- decidability
stage: advanced
status: draft
---

# Many-One and Turing Reducibility

## Core Idea
Many-one reducibility (A ≤_m B) transforms instances of A to instances of B via a single function and preserves hardness notions while defining degree structures. Turing reducibility (A ≤_T B) allows using a B-oracle adaptively during computation, classifying problems by computational power more finely. While many-one reducibility is standard for NP-completeness, Turing reducibility is more fundamental in computability theory and degree theory.
