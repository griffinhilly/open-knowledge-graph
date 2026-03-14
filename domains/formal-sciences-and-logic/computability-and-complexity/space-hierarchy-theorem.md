---
id: space-hierarchy-theorem
title: Space Hierarchy Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: space-complexity-classes-formal
  type: hard
- id: time-hierarchy-theorem
  type: soft
tags:
- separations
- space-complexity
- resource-bounded
stage: advanced
status: draft
---

# Space Hierarchy Theorem

## Core Idea
The space hierarchy theorem states that for space-constructible functions f and g with f = o(g), we have DSPACE(f) ⊊ DSPACE(g). Unlike the time hierarchy, the theorem is unconditional and requires no logarithmic factor. This implies strict hierarchy among space classes: L ⊂ PSPACE ⊂ EXPSPACE, guaranteeing more languages become decidable with more space.
