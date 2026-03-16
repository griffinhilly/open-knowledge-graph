---
id: turing-machine-model
title: Turing Machine Model and Formal Definition
domain: computer-science
course: theory-of-computation
prerequisites:
- id: limitations-of-context-free
  type: hard
builds-toward:
- turing-machine-variants
- universal-turing-machine
- church-turing-thesis
tags:
- turing-machines
- model
- computation
stage: abstract-reasoning
status: draft
---

# Turing Machine Model and Formal Definition

## Core Idea
A Turing machine is a theoretical computational device with a finite control, an infinite tape divided into cells, and a tape head that reads and writes symbols. At each step, based on the current state and symbol, it writes a new symbol, moves the head left or right, and enters a new state. This simple model captures the essence of algorithmic computation.

## How It's Best Learned
Implement a Turing machine simulator. Design machines for simple tasks (incrementing, palindrome checking). Understand the tape as unbounded memory and how it enables complex computations.

## Explainer

You have seen that finite automata and pushdown automata each have fundamental limitations — finite automata cannot count unboundedly, and pushdown automata cannot compare two independent counts. The **Turing machine** removes these limitations by providing an infinite tape that serves as both input and unlimited read-write memory, making it the most powerful standard model of computation.

Formally, a Turing machine consists of a finite set of states, a tape alphabet (including a blank symbol), a transition function, a start state, and accept/reject states. At each step, the machine reads the symbol under its **tape head**, then based on the current state and that symbol, it (1) writes a new symbol to the current cell, (2) moves the head one cell left or right, and (3) transitions to a new state. Computation proceeds until the machine enters the accept or reject state, or it may run forever — unlike DFAs, Turing machines are not guaranteed to halt on every input.

Consider how you would design a Turing machine to recognize the language {aⁿbⁿcⁿ | n ≥ 0}, which is beyond the reach of both finite automata and pushdown automata. One approach: scan right to find the first unmarked 'a', mark it with 'X', continue right to find the first unmarked 'b', mark it with 'Y', continue right to find the first unmarked 'c', mark it with 'Z', then return the head to the beginning and repeat. When all a's are marked, verify that no unmarked b's or c's remain. The tape serves as a scratchpad where the machine leaves marks to track its progress — something no automaton with only a stack or no memory at all could do.

The remarkable claim, formalized by the **Church-Turing thesis**, is that this simple model captures *everything* that is algorithmically computable. Any computation performed by any programming language, any computer architecture, or any other reasonable model of computation can be carried out by a Turing machine. The machine may be slow — spectacularly slow — but it can always simulate the other model. This is why Turing machines are the foundation for the theory of computability: when we say a problem is "decidable" or "undecidable," we mean with respect to this model, and the Church-Turing thesis assures us the answer would be the same for any other reasonable definition of computation.
