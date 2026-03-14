---
id: dead-code-elimination
title: Dead Code Elimination
domain: computer-science
course: compilers
prerequisites:
- id: live-variable-analysis
  type: hard
tags:
- optimization
- code-quality
- dead-code
stage: advanced
status: draft
---

# Dead Code Elimination

## Core Idea
Dead code elimination removes statements whose results are never used. An assignment to a non-live variable is dead: the value is computed but never observed. Unreachable code (after return, throw, or unconditional jump) is also dead. This optimization reduces code size and can expose further optimization opportunities. Aggressive dead-code elimination requires interprocedural analysis.
