---
id: linear-bounded-automata-computability-and-complexity
title: Linear Bounded Automata
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: pushdown-automata-formal
  type: hard
- id: turing-machines-formal
  type: hard
tags:
- automata
- context-sensitive-languages
- Chomsky-hierarchy
stage: formal-systems
status: draft
---

# Linear Bounded Automata

## Core Idea
A linear bounded automaton (LBA) is a nondeterministic Turing machine whose tape is restricted to the cells occupied by the input — it cannot use more space than the input length. LBAs recognize exactly the context-sensitive languages, placing them strictly between context-free languages and recursively enumerable languages in the Chomsky hierarchy. The Immerman-Szelepcsényi theorem shows that nondeterministic space classes are closed under complement, proving that the complement of every context-sensitive language is also context-sensitive.

## How It's Best Learned
Start from the Chomsky hierarchy and position the LBA as the machine model for level 1 (context-sensitive). Work through an example of an LBA recognizing {a^n b^n c^n} — a language that PDAs cannot handle — to see how bounded tape still permits counting across multiple groups. Contrast with unrestricted Turing machines to understand what bounded space buys and costs.

## Common Misconceptions
- Whether deterministic LBAs are equivalent to nondeterministic LBAs remains an open problem — unlike finite automata (DFA = NFA) and Turing machines (where nondeterminism doesn't change RE), the LBA question is unresolved.
- An LBA is not simply a Turing machine with a short tape — the tape is bounded by input length, which still allows exponentially many configurations.
