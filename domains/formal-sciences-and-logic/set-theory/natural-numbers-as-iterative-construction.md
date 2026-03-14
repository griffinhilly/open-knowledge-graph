---
id: natural-numbers-as-iterative-construction
title: 'Natural Numbers in Set Theory: Iterative Construction'
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: finite-sets-and-finiteness-definition
  type: hard
- id: recursion-on-finite-structures
  type: soft
builds-toward:
- ordinal-numbers-and-order
- von-neumann-ordinals
- axiom-of-infinity
tags:
- natural-numbers
- iterative
- von-neumann
stage: formal-systems
status: draft
---

# Natural Numbers in Set Theory: Iterative Construction

## Core Idea
Natural numbers are constructed set-theoretically: 0 = ∅, n+1 = n ∪ {n}, yielding ℕ = {0, 1, 2, 3, ...} = {∅, {∅}, {∅,{∅}}, ...}. This von Neumann construction embeds ℕ into the set-theoretic universe and allows ordinal numbers to generalize the concept of 'counting' to infinite cases.
