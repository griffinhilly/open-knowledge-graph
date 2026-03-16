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

## Explainer

You already know the Chomsky hierarchy as a ladder of machine power: finite automata recognize regular languages, pushdown automata recognize context-free languages, and unrestricted Turing machines recognize recursively enumerable languages. A **linear bounded automaton (LBA)** sits on the rung between PDAs and full Turing machines. It is a nondeterministic Turing machine with one constraint: the read/write head can never move beyond the cells occupied by the original input. The tape is bounded by input length — hence "linear bounded."

This restriction might seem minor, but it carves out a precise class. LBAs recognize exactly the **context-sensitive languages** — languages describable by grammars where each production rule can only expand a string (never shrink it). The classic separating example is {a^n b^n c^n}: three equal-length groups of different symbols. A pushdown automaton can match two groups against each other using its stack, but it cannot track three simultaneously. An LBA handles it by scanning back and forth, using the bounded tape as scratch memory to count and cross-check all three groups.

Why is boundedness so powerful? Even though the tape is limited to n cells, the machine can be in many different states and head positions — up to n × |Q| × |Γ|^n distinct configurations, which grows exponentially in n. This is dramatically more than a PDA, which only keeps a polynomial count in its stack. The bound merely prevents the machine from allocating infinite scratch space; it still has enormous computational room within the input's footprint.

A deep result connects LBAs to the structure of complexity: the **Immerman-Szelepcsényi theorem** proves that nondeterministic linear space (equivalently, the context-sensitive languages) is closed under complement. This is non-obvious — knowing that a string is *in* a language and knowing it is *not* in a language are logically symmetric but computationally asymmetric for nondeterministic machines. The proof uses an inductive counting argument: by counting the reachable configurations carefully, you can build a nondeterministic verifier for non-membership. One unresolved question persists: whether deterministic LBAs can simulate nondeterministic ones. Unlike the finite-automaton case (where DFA = NFA) or the full Turing machine case, this remains open — a rare gap in an otherwise well-charted hierarchy.
