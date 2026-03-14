---
id: loop-invariant-code-motion
title: Loop Invariant Code Motion (LICM)
domain: computer-science
course: compilers
prerequisites:
- id: code-optimization
  type: hard
- id: control-flow-graphs
  type: hard
tags:
- optimization
- loop-optimization
- code-motion
stage: advanced
status: draft
---

# Loop Invariant Code Motion (LICM)

## Core Idea
Loop invariant code motion hoists expressions that do not depend on loop iterations outside the loop. If an expression's operands are not modified in the loop, it computes the same value in each iteration and can be moved before the loop. This reduces redundant computation. Safety requires ensuring the expression is always executed before the loop's first iteration.
