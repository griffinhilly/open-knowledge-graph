---
id: nondeterministic-finite-automata-formal
title: Nondeterministic Finite Automata
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: deterministic-finite-automata-formal
  type: hard
- id: relations-properties-and-types
  type: soft
builds-toward:
- regular-expressions-and-languages
- pushdown-automata-formal
tags:
- automata
- nondeterminism
- regular-languages
stage: formal-systems
status: draft
---

# Nondeterministic Finite Automata

## Core Idea
A nondeterministic finite automaton (NFA) generalizes the DFA by allowing multiple transitions from a single state on the same symbol, transitions on the empty string (epsilon-transitions), and missing transitions. An NFA accepts if there exists at least one computation path that reaches an accept state. The subset construction algorithm proves that every NFA can be converted to an equivalent DFA, establishing that NFAs recognize exactly the regular languages. The conversion may cause an exponential blowup in the number of states, but the language class remains the same.

## How It's Best Learned
Design an NFA for a language that would be awkward as a DFA — such as "strings whose third-from-last symbol is 1" — then apply the subset construction step by step. Seeing the DFA's state space explode makes the power-of-nondeterminism tradeoff concrete.

## Common Misconceptions
- Nondeterminism does not add computational power for finite automata — NFAs and DFAs accept exactly the same class of languages, unlike the TM/NTM distinction in complexity theory.
- An NFA does not "choose" the right path; it accepts if any path leads to acceptance, which is equivalent to exploring all paths simultaneously.
