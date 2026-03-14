---
id: array-subscript-optimization
title: Array Subscript Optimization
domain: computer-science
course: compilers
prerequisites:
- id: loop-detection-analysis
  type: hard
- id: data-dependence-analysis
  type: hard
builds-toward:
- instruction-selection-techniques
tags:
- optimization
- loops
- memory
stage: advanced
status: draft
---

# Array Subscript Optimization

## Core Idea
Array subscript expressions often involve expensive multiplication and addition operations in loops. Strength reduction optimizes subscripts by detecting linear patterns (common in loops) and substituting cheaper operations. This optimization is particularly important for dense linear algebra code.

## How It's Best Learned
Implement strength reduction for induction variables in loops. Manually optimize nested loop array accesses.
