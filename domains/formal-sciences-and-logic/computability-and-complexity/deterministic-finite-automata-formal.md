---
id: deterministic-finite-automata-formal
title: Deterministic Finite Automata
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: soft
- id: set-fundamentals
  type: soft
- id: binary-relations
  type: soft
- id: set-operations-and-notation
  type: soft
builds-toward:
- nondeterministic-finite-automata-formal
- regular-expressions-and-languages
tags:
- automata
- regular-languages
- computation
stage: formal-systems
status: draft
---

# Deterministic Finite Automata

## Core Idea
A deterministic finite automaton (DFA) is the simplest model of computation: a finite set of states, an input alphabet, a transition function that maps each state-symbol pair to exactly one next state, a start state, and a set of accept states. A DFA reads an input string one symbol at a time, following transitions deterministically, and accepts if it ends in an accept state. The class of languages recognized by DFAs is exactly the regular languages — a proper subset of the context-free languages and far weaker than what Turing machines can decide.

## How It's Best Learned
Draw state diagrams for small DFAs that accept concrete languages — strings ending in "01", strings with an even number of 1s, binary multiples of 3. Trace inputs through the diagram by hand before formalizing the transition function as a table. This builds intuition for how finite memory constrains what can be recognized.

## Common Misconceptions
- A DFA does not have memory beyond its current state — it cannot count unboundedly, which is why it cannot recognize languages like {a^n b^n}.
- The transition function must be total: every state must have a transition for every symbol, even if that transition leads to a "dead" (non-accepting sink) state.
