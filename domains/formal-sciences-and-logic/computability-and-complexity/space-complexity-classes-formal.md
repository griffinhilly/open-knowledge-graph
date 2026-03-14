---
id: space-complexity-classes-formal
title: 'Space Complexity: PSPACE, L, and NL'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: time-complexity-classes-formal
  type: hard
- id: nondeterministic-turing-machines
  type: soft
- id: big-o-notation
  type: soft
- id: algorithm-complexity
  type: soft
builds-toward:
- pspace-and-complexity-hierarchy
tags:
- complexity
- space-complexity
- PSPACE
- logarithmic-space
stage: advanced
status: validated
---

# Space Complexity: PSPACE, L, and NL

## Core Idea
Space complexity measures the number of tape cells a TM uses on an input of length n. PSPACE is the class of problems solvable in polynomial space; it contains both P and NP and is known to contain problems harder than any fixed polynomial. L and NL are the classes solvable in O(log n) space deterministically and nondeterministically; NL contains graph reachability (STCON). Savitch's theorem shows that nondeterministic space S(n) ≥ log n can be simulated deterministically in S(n)² space, so NPSPACE = PSPACE — a striking contrast to the unresolved P vs. NP question.

## How It's Best Learned
Contrast space with time: space can be reused across computation steps but time cannot. Work through Savitch's theorem to see why nondeterministic and deterministic space are polynomially related, while the analogous time question (NP ⊆ P?) remains open. Study QBF satisfiability as the canonical PSPACE-complete problem.

## Common Misconceptions
- Polynomial space does not imply polynomial time — PSPACE problems may require exponential time to solve.
- Logarithmic space is very restrictive: the working tape holds only O(log n) bits, enough for pointers into the input, while the input itself is read-only.
