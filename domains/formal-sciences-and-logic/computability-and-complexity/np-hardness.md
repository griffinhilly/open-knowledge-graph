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
