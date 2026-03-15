---
id: nondeterministic-polynomial-time-computability-and-complexity
title: Nondeterministic Polynomial Time and NP
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-and-polynomial-time
  type: hard
- id: nondeterministic-turing-machines
  type: hard
builds-toward:
- sat-and-np-complete-problems
- np-complete-problems-standard
tags:
- NP
- nondeterminism
- complexity-classes
stage: advanced
status: draft
---

# Nondeterministic Polynomial Time and NP

## Core Idea
NP is the class of languages recognized by nondeterministic Turing machines in polynomial time, or equivalently, languages with polynomial-time verifiers: for membership x ∈ L, a short certificate exists that can be verified in polynomial time. This characterization makes NP capture optimization and constraint-satisfaction problems; P ⊆ NP, and whether they are equal is the P vs NP problem.
