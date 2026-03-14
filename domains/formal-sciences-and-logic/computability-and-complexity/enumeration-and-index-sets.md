---
id: enumeration-and-index-sets
title: Enumeration of Turing Machines and Index Sets
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: cantor-pairing-and-enumerations
  type: soft
builds-toward:
- rices-theorem-applications
tags:
- enumeration
- index-sets
- godel-numbering
stage: advanced
status: draft
---

# Enumeration of Turing Machines and Index Sets

## Core Idea
Turing machines can be effectively enumerated (e.g., by lexicographic order of their descriptions), yielding a universal Turing machine. An index set is a set of indices W ⊆ ℕ where W = {i : the i-th machine has property P}. Rice's theorem asserts that all non-trivial index sets are non-recursive, formalizing the intuition that enumerating machines with a semantic property is fundamentally undecidable.
