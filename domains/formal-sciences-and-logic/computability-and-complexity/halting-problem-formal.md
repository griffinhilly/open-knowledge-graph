---
id: halting-problem-formal
title: The Halting Problem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: cantor-diagonalization
  type: hard
- id: church-turing-thesis-formal
  type: soft
- id: decidability-and-undecidability
  type: soft
- id: uncountable-sets-and-cantor-diagonalization
  type: soft
- id: set-fundamentals
  type: soft
- id: functions-and-function-properties
  type: hard
builds-toward:
- rices-theorem
- re-and-co-re-languages
- computability-reductions
tags:
- undecidability
- diagonalization
- computability
stage: advanced
status: validated
---

# The Halting Problem

## Core Idea
The halting problem asks whether there exists a Turing machine that, given any program and input, correctly determines whether that program halts on that input. Turing proved in 1936 that no such machine can exist. The proof uses diagonalization: assume a halting oracle H exists and construct a machine D that runs H on itself then does the opposite — D's behavior contradicts H's prediction, yielding a contradiction. This is the paradigmatic undecidability result and the template for hundreds of subsequent proofs.

## How It's Best Learned
Carefully trace through the diagonalization argument to see exactly where the contradiction arises. Then practice reducing other problems to the halting problem — recognizing it as the canonical hard problem from which undecidability spreads.

## Common Misconceptions
- The proof does not say that no specific program's halting behavior can be determined — it says no *general* algorithm works for all programs.
- Undecidability is not about computational speed or resource limits; it is an absolute mathematical impossibility.
