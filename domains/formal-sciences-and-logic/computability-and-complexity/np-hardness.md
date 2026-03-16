---
id: np-hardness
title: 'NP-Hardness: Definition and Properties'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: p-versus-np
  type: hard
- id: polynomial-time-reductions
  type: hard
builds-toward:
- np-completeness-theorem
- sat-canonical-problem
tags:
- np-hardness
- reductions
- hardness
- complexity-classification
stage: advanced
status: draft
---

# NP-Hardness: Definition and Properties

## Core Idea
A problem is NP-hard if every NP problem polynomial-time reduces to it; solving an NP-hard problem in polynomial time would imply P = NP. NP-hard problems may or may not be in NP; those that are in NP are called NP-complete. NP-hardness measures the 'difficulty relative to NP' rather than solvability within NP.

## How It's Best Learned
Study the definition formally: a problem is NP-hard iff all NP problems reduce to it. Distinguish hardness (relative to NP) from membership in NP itself.

## Explainer

You already know about **polynomial-time reductions**: if problem A reduces to problem B in polynomial time, then a fast algorithm for B would give a fast algorithm for A. Reductions define a "difficulty ordering" on problems — B is at least as hard as A. NP-hardness is the extreme version of this: a problem H is **NP-hard** if *every* problem in NP reduces to H in polynomial time. Solving H quickly would collapse the entire class NP into P.

The definition has an important asymmetry to absorb. NP-hardness says H is at least as hard as everything in NP, but it says nothing about whether H is *in* NP itself. An NP-hard problem may be harder than NP — it might live in EXPTIME, or it might not even be decidable. The halting problem, for instance, is NP-hard (every NP problem reduces to it) but is also undecidable — far outside NP. NP-hardness is a *lower bound* on difficulty, not a classification of where the problem lives.

The problems you are likely most familiar with — SAT, 3-coloring, Hamiltonian cycle, TSP — are not just NP-hard but **NP-complete**: they are NP-hard *and* they belong to NP. Being in NP means a proposed solution can be verified in polynomial time. NP-completeness is the intersection: hard as anything in NP, but still checkable. NP-hardness without NP membership describes problems that are strictly harder — optimization variants, counting versions, or problems outside the decision hierarchy entirely.

A useful mental image: picture NP as a set of problems arranged by hardness. The NP-complete problems sit at the "ceiling" of NP, the hardest problems inside the class. NP-hard problems include those ceiling problems and everything above them. A reduction from an NP-complete problem to a new problem H proves H is NP-hard: since that NP-complete problem already sat at NP's ceiling, H must sit at least that high. This is why establishing NP-hardness in practice almost always involves reducing from a known NP-complete problem like SAT or 3-SAT rather than directly invoking the universal definition.

The P vs. NP question reframes in this language: if any NP-hard problem in NP (i.e., any NP-complete problem) is solvable in polynomial time, then P = NP. Conversely, if P ≠ NP, then no NP-hard problem admits a polynomial-time algorithm. NP-hardness is thus the correct notion for expressing "we have no efficient algorithm and here is the structural reason why."
