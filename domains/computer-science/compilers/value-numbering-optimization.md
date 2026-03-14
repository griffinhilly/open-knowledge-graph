---
id: value-numbering-optimization
title: Value Numbering and Redundancy Elimination
domain: computer-science
course: compilers
prerequisites:
- id: code-optimization
  type: hard
- id: dataflow-analysis
  type: soft
tags:
- optimization
- redundancy
- CSE
stage: advanced
status: draft
---

# Value Numbering and Redundancy Elimination

## Core Idea
Value numbering assigns numbers to expressions based on their semantic value; identical expressions receive the same number. Redundant computations are then replaced with the first computation's result, achieving both common subexpression elimination and constant folding in a single, efficient pass.
