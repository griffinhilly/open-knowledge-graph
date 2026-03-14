---
id: code-optimization
title: Code Optimization Fundamentals
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
builds-toward:
- common-subexpression-elimination
- loop-invariant-code-motion
- constant-propagation
tags:
- optimization
- compiler-design
- performance
stage: advanced
status: draft
---

# Code Optimization Fundamentals

## Core Idea
Code optimization improves program performance (speed, memory, energy) without changing observable behavior (correctness). Optimizations are enabled by dataflow analysis: reaching definitions, liveness, availability. Machine-independent optimizations (constant propagation, CSE) are applied to IR; machine-dependent optimizations (instruction scheduling, register allocation) target specific architectures.
