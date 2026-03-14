---
id: oracle-turing-machines
title: Oracle Turing Machines
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: decidability
  type: soft
builds-toward:
- polynomial-hierarchy
- pspace-complexity-class
tags:
- complexity
- oracles
- relativization
stage: advanced
status: draft
---

# Oracle Turing Machines

## Core Idea
An oracle Turing machine augments a standard TM with a special oracle tape: given set A (the oracle), the machine queries membership in A in a single step. Oracle machines formalize 'if we could solve A instantly, what else becomes tractable?' They are crucial for proving that P vs NP cannot be settled by relativistic methods—any technique must be non-relativizing—and for studying the polynomial hierarchy via iterative oracle calls.
