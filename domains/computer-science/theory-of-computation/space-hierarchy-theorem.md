---
id: space-hierarchy-theorem
title: Space Hierarchy Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: space-complexity-classes
  type: hard
- id: turing-machines
  type: hard
builds-toward:
- pspace-complexity-class
tags:
- complexity-theory
- hierarchy
- provable-separation
stage: advanced
status: draft
---

# Space Hierarchy Theorem

## Core Idea
The space hierarchy theorem states that for space-constructible f(n) ≥ log n, DSPACE(f(n)) ⊂ DSPACE(f(n) log f(n)). Unlike time (which requires quadratic growth), space only needs logarithmic growth because space is 'reusable'—the machine can overwrite previous values. The theorem shows space classes strictly increase even with tighter bounds than time, but the proof technique differs fundamentally: verifying space usage requires tracking maximum usage, not cumulative cost.
