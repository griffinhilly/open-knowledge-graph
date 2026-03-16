---
id: time-space-hierarchy-theorems
title: Time and Space Hierarchy Theorems
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: time-complexity-classes-formal
  type: hard
- id: space-complexity-classes-formal
  type: hard
builds-toward:
- polynomial-hierarchy-levels
tags:
- hierarchy
- lower-bounds
- separations
stage: advanced
status: draft
---

# Time and Space Hierarchy Theorems

## Core Idea
The time hierarchy theorem states that if f(n) log f(n) < g(n), then DTIME(f(n)) ⊊ DTIME(g(n)): more time provably allows computation of strictly harder problems. Space hierarchy is analogous. These theorems rigorously separate complexity classes and show that the complexity landscape has unbounded 'height'—no single complexity class contains all computable languages.

## Explainer

You already know complexity classes like P and EXPTIME, and that DTIME(f(n)) is the class of problems solvable in O(f(n)) time. A natural question is whether these classes are genuinely distinct — does having more time *actually* let you solve harder problems? The **time hierarchy theorem** answers yes, rigorously. If g(n) grows faster than f(n) log f(n), then DTIME(g(n)) strictly contains DTIME(f(n)): problems exist that require roughly g(n) steps but cannot be solved in f(n) steps. As a corollary, P ⊊ EXPTIME — exponential time is provably more powerful than polynomial time.

The proof uses **diagonalization**, the same technique behind the undecidability of the halting problem. Construct a machine D that, on input ⟨M, 1^n⟩, simulates M for g(n) steps and does the opposite of whatever M would do. If any machine M in DTIME(f(n)) could solve the same problem as D, we get a contradiction when we feed D its own description. The log factor in the condition f(n) log f(n) < g(n) is a technical overhead needed for the universal TM simulation. For the **space hierarchy theorem**, the condition is simpler — f(n) = o(g(n)) suffices — because space can be reused and the simulation overhead is smaller.

These theorems are foundational because without them, the complexity hierarchy could collapse. Perhaps P = EXPTIME, or every problem solvable in space n is also solvable in space log n. The hierarchy theorems rule this out: the complexity landscape is genuinely infinite, with strict containments at every level of increased resources. This gives complexity theory its structure — there is no "maximum" class of tractable problems, and no single resource bound captures all of computation.

An important subtlety is what the hierarchy theorems do *not* prove. They separate DTIME classes by time, but they cannot separate P from NP, or NP from PSPACE. Those separations require *lower bounds* — proofs that specific problems require a certain amount of resources — and such lower bounds remain largely elusive. The hierarchy theorems are unconditional separations achieved by the clever diagonalization construction, whereas most separations in complexity theory (like P ≠ NP) require reasoning about the structure of actual computational problems, a far harder task.
