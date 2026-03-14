---
id: turing-machine-model-and-definition
title: Turing Machine Model and Formal Definition
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: pushdown-automata-and-equivalence
  type: soft
builds-toward:
- multi-tape-turing-machines
- universal-turing-machine
tags:
- turing-machine
- tape
- head
- control
- acceptance
- computation
stage: advanced
status: draft
---

# Turing Machine Model and Formal Definition

## Core Idea
A Turing machine has a finite control, infinite tape, and read-write head. Each step: read symbol, change state, write symbol, move head. TMs formalize algorithms without committing to specifics of implementation. A TM accepts if it halts in an accepting state; computes a function if halting output is well-defined. TMs embody the Church-Turing thesis about the limits of computation.
