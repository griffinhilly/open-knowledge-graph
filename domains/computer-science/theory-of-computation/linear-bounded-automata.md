---
id: linear-bounded-automata
title: Linear Bounded Automata
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machine-model-and-definition
  type: hard
- id: context-sensitive-languages
  type: hard
builds-toward:
- pspace-complexity-class
tags:
- automata
- resource-bounds
- complexity
stage: advanced
status: draft
---

# Linear Bounded Automata

## Core Idea
A linear bounded automaton (LBA) is a Turing machine whose read-write head cannot move beyond O(n) cells, bounding working memory linearly in input size. LBAs recognize exactly context-sensitive languages. Unlike Turing machines, it is unknown whether deterministic and nondeterministic LBAs recognize the same classes—a fundamental open problem. This contrasts with finite automata (where DFA = NFA) and suggests LBAs occupy an intermediate level of computational universality.
