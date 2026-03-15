---
id: alternating-turing-machines-computability-and-complexity
title: Alternating Turing Machines
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: nondeterministic-turing-machines
  type: hard
- id: turing-machines-formal
  type: hard
builds-toward:
- pspace-and-complexity-hierarchy
tags:
- computation-models
- quantifiers
- complexity
stage: advanced
status: draft
---

# Alternating Turing Machines

## Core Idea
An alternating Turing machine is a nondeterministic Turing machine whose states are classified as existential (∃) or universal (∀). Computation branches existentially at ∃-states (seeking a 'yes' path) and universally at ∀-states (requiring all paths to lead to acceptance). The time and space complexity of ATMs characterize the polynomial hierarchy and PSPACE, respectively.
