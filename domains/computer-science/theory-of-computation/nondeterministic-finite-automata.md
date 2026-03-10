---
id: nondeterministic-finite-automata
title: Nondeterministic Finite Automata (NFA)
domain: computer-science
course: theory-of-computation
prerequisites:
- id: deterministic-finite-automata
  type: hard
- id: set-theory-basics
  type: soft
- id: set-operations
  type: soft
builds-toward:
- nfa-to-dfa-conversion
- kleene-theorem
- pushdown-automata
tags:
- automata
- nondeterminism
- NFA
- regular
stage: advanced
status: draft
---

# Nondeterministic Finite Automata (NFA)

## Core Idea
A nondeterministic finite automaton (NFA) extends the DFA by allowing transitions to zero, one, or multiple states on the same input symbol, as well as ε-transitions that consume no input. An NFA accepts a string if at least one possible computation path ends in an accept state. Nondeterminism is a mathematical convenience, not a physical model — every NFA can be converted to an equivalent DFA, so NFAs recognize the same class of languages. NFAs are often far smaller and easier to construct than equivalent DFAs.

## How It's Best Learned
Build NFAs for union and concatenation of two simpler languages to see why nondeterminism is natural for language operations. Then trace the parallel-execution intuition: imagine the NFA forking into multiple copies at each nondeterministic choice, accepting if any copy accepts.

## Common Misconceptions
- Thinking NFAs are strictly more powerful than DFAs — they are equivalent in expressiveness.
- Confusing acceptance semantics: an NFA accepts if *some* path accepts, not if *all* paths accept.
- Forgetting ε-closure: ε-transitions must be followed transitively before and after every symbol read.
