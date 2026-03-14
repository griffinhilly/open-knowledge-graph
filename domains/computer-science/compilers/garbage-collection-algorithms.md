---
id: garbage-collection-algorithms
title: Garbage Collection Algorithms
domain: computer-science
course: compilers
prerequisites:
- id: runtime-function-calls
  type: hard
- id: memory-management-basics
  type: hard
builds-toward:
- jit-compilation
tags:
- garbage-collection
- memory-management
- runtime-system
stage: advanced
status: draft
---

# Garbage Collection Algorithms

## Core Idea
Garbage collection automatically reclaims memory of unreachable objects, freeing programmers from manual deallocation. Reachability is determined from root references (stack, globals). Common algorithms include mark-and-sweep (mark reachable objects, sweep unreachable), generational (younger objects collected more often), and copying (move live objects to a new space). GC adds overhead but prevents memory leaks.
