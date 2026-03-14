---
id: local-optimization-techniques
title: Local Optimization Techniques
domain: computer-science
course: compilers
prerequisites:
- id: basic-block-analysis
  type: hard
- id: code-optimization
  type: hard
builds-toward:
- global-optimization-techniques
tags:
- optimization
- local-opts
- peephole
stage: advanced
status: draft
---

# Local Optimization Techniques

## Core Idea
Local optimizations operate within a single basic block and include constant folding, constant propagation, dead code elimination, and algebraic simplification. These are the easiest optimizations to implement but have limited scope, serving as foundation for sophisticated global optimizations.

## How It's Best Learned
Implement several local optimizations and apply them to basic blocks. Measure improvements in code quality.
