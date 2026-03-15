---
id: turing-machines-formal
title: Turing Machines
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: formal-arithmetic-and-expressibility
  type: soft
- id: algorithm-complexity
  type: soft
- id: binary-relations
  type: soft
- id: mathematical-induction
  type: soft
- id: set-theory-basics
  type: soft
- id: algorithm-analysis-big-o
  type: soft
- id: set-fundamentals
  type: soft
builds-toward:
- church-turing-thesis-formal
- halting-problem-formal
- nondeterministic-turing-machines
- kolmogorov-complexity
- time-complexity-classes-formal
tags:
- computation
- automata
- models-of-computation
stage: advanced
status: validated
---

# Turing Machines

## Core Idea
A Turing machine is an abstract computational device consisting of an infinite tape, a read/write head, and a finite set of states with transition rules. It can simulate any algorithmic process and serves as the foundational formal model of computation. Despite its simplicity, no physically realizable computing device has been shown to exceed its computational power. The model precisely defines what it means for a function to be computable and for a language to be decidable or recognizable.

## How It's Best Learned
Start by tracing simple Turing machines by hand on concrete inputs — e.g., a machine that accepts palindromes or increments a binary number. Build familiarity with the state-transition diagram formalism before studying multi-tape variants and their polynomial-time equivalence to single-tape machines.

## Common Misconceptions
- Turing machines are not infinite in practice; the tape is potentially infinite but only a finite prefix is ever used on any terminating computation.
- A Turing machine that loops forever on an input does NOT accept it — acceptance requires halting in a designated accept state.
