---
id: pushdown-automata-formal
title: Pushdown Automata
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: nondeterministic-finite-automata-formal
  type: hard
builds-toward:
- context-free-grammars-formal
- linear-bounded-automata
tags:
- automata
- context-free-languages
- stack
stage: formal-systems
status: draft
---

# Pushdown Automata

## Core Idea
A pushdown automaton (PDA) extends a finite automaton with an unbounded stack, enabling it to recognize context-free languages such as {a^n b^n}. Transitions can push symbols onto or pop symbols from the stack, giving the machine a form of unbounded memory organized in last-in-first-out order. Nondeterministic PDAs (NPDAs) recognize exactly the context-free languages, but deterministic PDAs (DPDAs) recognize a strictly smaller class. Acceptance can be defined by final state or by empty stack; the two modes are equivalent for nondeterministic PDAs.

## How It's Best Learned
Build a PDA for {a^n b^n} by pushing a marker for each 'a' and popping for each 'b', then extend to more complex languages like balanced parentheses or {ww^R}. Compare the DPDA and NPDA for specific languages to see where determinism falls short — e.g., palindromes require nondeterminism to guess the midpoint.

## Common Misconceptions
- Unlike finite automata, deterministic and nondeterministic PDAs are NOT equivalent — DPDAs recognize a proper subset of the context-free languages.
- A PDA can only access the top of its stack, not arbitrary positions — this restriction is what separates context-free from context-sensitive computation.
