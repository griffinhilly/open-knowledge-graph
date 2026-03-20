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
stage: advanced
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

## Explainer

You already know that a **nondeterministic finite automaton** (NFA) processes input using only a finite internal state — its memory is exactly the state it is currently in. That severe restriction means NFAs cannot count: they cannot recognize {a^n b^n} because they would need to remember the exact count of a's seen, which requires unbounded storage. A **pushdown automaton** (PDA) solves this by attaching an unbounded **stack** to a finite automaton. The stack gives the machine a memory that can grow without limit, but with one strict constraint: you can only push and pop at the top. This last-in-first-out discipline is precisely the right structure for counting matching pairs, parentheses, or nested structures.

The canonical example is {a^n b^n | n ≥ 0}. The PDA pushes a marker onto the stack for every 'a' it reads, then pops one marker for every 'b'. If the stack is empty exactly when the input ends, the string is accepted. This is impossible for any NFA or DFA, but trivial for a PDA. The stack's power generalizes naturally: balanced parentheses, {ww^R} (palindromes), and the syntax of most programming languages are all context-free and recognizable by PDAs. Indeed, **nondeterministic PDAs recognize exactly the context-free languages** — the correspondence between PDAs and context-free grammars is the central theorem of this topic.

Nondeterminism plays a bigger role for PDAs than it does for finite automata. For DFAs and NFAs, you learned that nondeterminism does not add power — every NFA has an equivalent DFA. For PDAs, **determinism strictly reduces power**. The language {ww^R} requires a PDA to guess where the midpoint of the palindrome is, which it can do nondeterministically but not deterministically. Deterministic PDAs (DPDAs) define a proper subclass — the deterministic context-free languages — which includes most practical programming language grammars but excludes inherently ambiguous or center-guess-required languages.

Acceptance in a PDA can be defined in two ways: by **final state** (the machine enters an accepting state after consuming the full input) or by **empty stack** (the machine empties its stack after consuming the full input). For nondeterministic PDAs, these two modes are equivalent — any language accepted one way can be accepted the other. This equivalence does not hold for deterministic PDAs, which is another asymmetry compared to finite automata. Understanding which acceptance mode you are using matters when constructing PDAs or proving correctness, so always check the definition in use.
