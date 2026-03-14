---
id: time-hierarchy-theorem
title: Time Hierarchy Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: time-complexity-classes
  type: hard
- id: turing-machines
  type: hard
builds-toward:
- exptime-expspace-classes
tags:
- complexity-theory
- hierarchy
- provable-separation
stage: advanced
status: draft
---

# Time Hierarchy Theorem

## Core Idea
The time hierarchy theorem states that for time-constructible f(n) > n log n, DTIME(f(n)) ⊂ DTIME(f(n) log f(n))—more time strictly enables computing harder problems. Using diagonal arguments with universal Turing machines, the theorem guarantees languages exist computable in quadratic but not linear time, providing rare provable separations in complexity theory. The log factor stems from the overhead of simulating one machine by another while verifying time bounds.
