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
