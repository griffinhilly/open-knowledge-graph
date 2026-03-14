---
id: exptime-expspace-classes
title: EXPTIME and EXPSPACE Complexity Classes
domain: computer-science
course: theory-of-computation
prerequisites:
- id: time-complexity-classes
  type: hard
- id: space-complexity-classes
  type: hard
tags:
- complexity-classes
- exponential-bounds
stage: advanced
status: draft
---

# EXPTIME and EXPSPACE Complexity Classes

## Core Idea
EXPTIME is the class of languages decidable in time 2^(p(n)) for polynomial p; EXPTIME strictly contains PSPACE by hierarchy theorems. EXPSPACE similarly bounds space exponentially. These classes represent problems solvable by explicit enumeration or exhaustive search but intractable for realistic instance sizes. Problems complete for EXPTIME include two-player game winner determination and deciding provability in certain formal systems—scenarios where checking all possibilities becomes unavoidable.
