---
id: nl-completeness
title: NL-Completeness and Space-Bounded Reductions
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: logarithmic-space-classes
  type: hard
- id: computability-reductions
  type: soft
tags:
- space-complexity
- completeness
- reductions
stage: advanced
status: draft
---

# NL-Completeness and Space-Bounded Reductions

## Core Idea
A problem is NL-complete if it lies in NL and every language in NL reduces to it via a log-space reduction. The most canonical NL-complete problem is REACHABILITY: given a directed graph and two vertices, does a path exist between them? NL-completeness demonstrates that even space-constrained computation has meaningful completeness notions and hardness hierarchy.
