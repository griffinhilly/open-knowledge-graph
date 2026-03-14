---
id: pspace-completeness
title: PSPACE and PSPACE-Completeness
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: pspace-and-complexity-hierarchy
  type: hard
- id: polynomial-hierarchy
  type: hard
builds-toward:
- alternating-machines-hierarchy
tags:
- pspace
- space-complexity
- qbf
- pspace-complete
stage: advanced
status: draft
---

# PSPACE and PSPACE-Completeness

## Core Idea
PSPACE is the class of problems solvable in polynomial space (regardless of time). PSPACE contains the polynomial hierarchy and includes problems like quantified Boolean formulas (QBF) that are PSPACE-complete. The relationship between time and space complexity is subtle: PSPACE-completeness reveals problems harder than NP (under standard assumptions) yet solvable with modest space.

## How It's Best Learned
Understand the connection between polynomial space and polynomial alternation via Savitch's theorem. Study TQBF as the canonical PSPACE-complete problem.
