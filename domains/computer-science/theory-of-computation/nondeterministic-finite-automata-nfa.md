---
id: nondeterministic-finite-automata-nfa
title: Nondeterministic Finite Automata
domain: computer-science
course: theory-of-computation
prerequisites:
- id: deterministic-finite-automata-dfa
  type: hard
builds-toward:
- nfa-dfa-equivalence-construction
- regular-expressions-to-automata
tags:
- finite-automata
- nfa
- nondeterminism
stage: abstract-reasoning
status: draft
---

# Nondeterministic Finite Automata

## Core Idea
An NFA extends a DFA by allowing zero, one, or multiple transitions for each (state, symbol) pair, and by permitting epsilon (ε) transitions that consume no input. An NFA accepts a string if any possible path of transitions consumes the string and ends in an accepting state.
