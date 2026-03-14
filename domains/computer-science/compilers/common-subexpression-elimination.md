---
id: common-subexpression-elimination
title: Common Subexpression Elimination (CSE)
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
- id: reaching-definitions-analysis
  type: hard
tags:
- optimization
- cse
- expression-reuse
stage: advanced
status: draft
---

# Common Subexpression Elimination (CSE)

## Core Idea
Common subexpression elimination detects and removes redundant computations. If the same expression is computed multiple times with unchanged operands, compute it once and reuse the result. CSE requires tracking when expressions are available (all operands have definitions reaching the current point) and when they are not killed (operands not reassigned).
