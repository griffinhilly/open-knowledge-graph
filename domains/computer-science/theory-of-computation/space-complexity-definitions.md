---
id: space-complexity-definitions
title: 'Space Complexity: L, NL, and PSPACE'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: boolean-satisfiability-and-reductions
  type: soft
- id: space-complexity-and-savitch-theorem
  type: hard
builds-toward:
- savitch-theorem-and-implications
tags:
- space-complexity
- log-space
- pspace
- l
- nl
- definitions
stage: advanced
status: draft
---

# Space Complexity: L, NL, and PSPACE

## Core Idea
Space complexity measures memory usage: L is log-space (useful for streaming), NL is nondeterministic log-space (path finding), PSPACE is polynomial space. Unlike time, space is reusable, so space classes have different hierarchies. PSPACE-complete problems include QBF (quantified Boolean formulas)—intractable despite polynomial space sufficing theoretically.
