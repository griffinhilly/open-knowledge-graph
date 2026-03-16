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

## Explainer

You already know that a DFA processes input one symbol at a time, always in exactly one state, following exactly one transition per symbol. An NFA relaxes this rigid constraint in two ways. First, from a given state on a given input symbol, the machine may have **multiple possible transitions** — or none at all. Second, the machine may take **epsilon (ε) transitions**, moving between states without consuming any input. The result is a machine that, conceptually, explores many computational paths simultaneously rather than committing to a single deterministic route.

The key shift in thinking is about acceptance. A DFA accepts if its single path ends in an accept state. An NFA accepts if **any one** of its potentially many paths ends in an accept state — the others can crash, loop, or reject, and it does not matter. Think of the NFA as an optimist: it succeeds if success is possible along any branch. You can visualize this as a tree of possibilities that the machine explores in parallel, where a single accepting leaf is enough to accept the entire string.

Consider a concrete example: suppose you want to recognize strings over {0, 1} that contain the substring "01". A DFA needs to carefully track whether it has seen a 0 followed by a 1 using distinct states. An NFA can take a simpler approach — it nondeterministically "guesses" when the substring begins. It stays in a start state reading any symbol, and at any point it can branch into a path that reads '0' then '1' and accepts. The nondeterminism handles the guessing; you do not need to explicitly encode the tracking logic.

Epsilon transitions add further flexibility. An ε-transition lets the machine silently move between states, which is especially useful when combining smaller automata into larger ones — for instance, when converting a regular expression into an NFA. You can glue together sub-machines with ε-transitions to represent union, concatenation, or Kleene star without redesigning the entire automaton. Despite all this added flexibility, NFAs recognize exactly the same class of languages as DFAs — the regular languages. The power of nondeterminism here is not computational but descriptive: NFAs are often dramatically simpler to design and understand, even though a corresponding DFA always exists.
