---
id: inlining-heuristics
title: Inlining Heuristics and Decision Making
domain: computer-science
course: compilers
prerequisites:
- id: procedure-inlining-optimization
  type: hard
- id: local-optimization-techniques
  type: hard
tags:
- optimization
- inlining
- heuristics
stage: advanced
status: draft
---

# Inlining Heuristics and Decision Making

## Core Idea
Inlining replaces function calls with function bodies, eliminating call overhead but risking code explosion. Heuristics estimate call frequency, function size, and cascading benefit to decide when inlining improves net performance, often using profiling data to guide decisions.

## How It's Best Learned
Examine compiler inlining decisions via -fopt-info in GCC or llvm-opt-report; compare code size and performance with and without inlining enabled.
