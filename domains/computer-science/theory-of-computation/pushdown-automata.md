---
id: pushdown-automata
title: Pushdown Automata (PDA)
domain: computer-science
course: theory-of-computation
prerequisites:
- id: deterministic-finite-automata
  type: hard
- id: stacks-data-structure
  type: hard
- id: nondeterministic-finite-automata
  type: soft
- id: context-free-grammars
  type: soft
builds-toward:
- cfg-pda-equivalence
- turing-machines
tags:
- PDA
- pushdown
- stack
- context-free
- nondeterminism
stage: advanced
status: validated
---
# Pushdown Automata (PDA)

## Core Idea
A pushdown automaton (PDA) extends an NFA with an unbounded stack. At each step, a PDA reads an input symbol (or ε), pops a symbol from the stack, transitions to a new state, and pushes a (possibly different) string onto the stack. PDAs recognize exactly the context-free languages. Nondeterministic PDAs are strictly more powerful than deterministic PDAs — unlike the DFA/NFA equivalence, adding nondeterminism gives PDAs additional expressive power. The stack is what allows PDAs to track nested structure that finite automata cannot.

## How It's Best Learned
Design a PDA for {aⁿbⁿ : n ≥ 0} by hand: push an 'a' for each a read, then pop for each b. Verify acceptance by both empty stack and final state. Then try {wwᴿ : w ∈ {a,b}*} to see why nondeterminism is needed.

## Common Misconceptions
- Assuming deterministic and nondeterministic PDAs are equivalent — unlike DFAs/NFAs, det-PDAs are strictly weaker (e.g., they cannot recognize {wwᴿ}).
- Forgetting that the stack must be initialized with a bottom-of-stack marker to test for empty stack.
- Thinking any CFL has a deterministic PDA — only DCFL languages (a proper subset of CFLs) do.
