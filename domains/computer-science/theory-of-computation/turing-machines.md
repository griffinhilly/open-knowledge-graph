---
id: turing-machines
title: Turing Machines
domain: computer-science
course: theory-of-computation
prerequisites:
- id: pushdown-automata
  type: hard
- id: recursion-basics
  type: soft
- id: cfg-pda-equivalence
  type: soft
- id: pumping-lemma-cfl
  type: soft
builds-toward:
- turing-machine-variants
- church-turing-thesis
- decidability
- time-complexity-classes
tags:
- Turing-machine
- computation
- model
- tape
- decidability
stage: advanced
status: validated
---
# Turing Machines

## Core Idea
A Turing machine (TM) is a finite-state control with an infinite read-write tape. At each step it reads the current tape symbol, writes a new symbol, moves left or right, and transitions to a new state. TMs can accept by entering an accept state, reject by entering a reject state, or loop forever. TMs are the formal model of computation underlying modern computer science — a language is computable if and only if some TM decides it (halting on all inputs). Compared to PDAs, the key power boost is the ability to read and rewrite the tape arbitrarily, not just use a stack.

## How It's Best Learned
Design TMs for simple tasks: copy a string, test if a string is of the form aⁿbⁿ, or increment a binary number. Trace execution on concrete inputs to build intuition for how the tape replaces both the stack and the program's working memory.

## Common Misconceptions
- Thinking a TM is a modern computer — it is an idealized, infinitely-taped mathematical model.
- Confusing a TM that *accepts* (halts in accept state) with one that *decides* (halts on all inputs in either accept or reject state).
- Assuming TMs can only move one direction — the standard model moves left or right, and this bidirectionality is what makes them more powerful than PDAs.
