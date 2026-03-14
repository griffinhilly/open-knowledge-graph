---
id: nc-class-parallel-circuits
title: NC Class and Parallel Circuit Complexity
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: circuit-complexity
  type: hard
- id: time-complexity-classes-formal
  type: soft
tags:
- parallel-computation
- circuits
- depth-bounds
stage: advanced
status: draft
---

# NC Class and Parallel Circuit Complexity

## Core Idea
NC (Nick's Class) contains languages computable by circuits of polynomial size and logarithmic depth. These circuits model highly parallel computation: depth corresponds to parallel time while size represents total operations. NC ⊆ P, and whether NC = P remains open. NC-hierarchy captures degrees of parallelizability, with NC^1 (linear size, log depth) being particularly fundamental for understanding parallelism.
