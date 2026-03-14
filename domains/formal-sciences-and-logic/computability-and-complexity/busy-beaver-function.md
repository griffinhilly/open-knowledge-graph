---
id: busy-beaver-function
title: Busy Beaver Function and Non-Computability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: halting-problem-formal
  type: hard
- id: undecidability-and-gödel
  type: soft
tags:
- non-computability
- undecidability
- functions
stage: advanced
status: draft
---

# Busy Beaver Function and Non-Computability

## Core Idea
The busy beaver function BB(n) is the maximum number of steps a halting n-state Turing machine can take on a blank tape. BB is non-computable: no Turing machine can compute BB(n) for all n. Because computing BB would require solving the halting problem, busy beavers demonstrate that even well-defined integer sequences can be uncomputable, illustrating fundamental limits of computation.
