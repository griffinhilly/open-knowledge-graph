---
id: hamiltonian-path-cycle
title: Hamiltonian Path and Cycle Problems
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
builds-toward:
- approximation-algorithms-design
tags:
- np-complete
- graph-problems
- path-problems
stage: advanced
status: draft
---

# Hamiltonian Path and Cycle Problems

## Core Idea
The Hamiltonian cycle problem asks if a graph contains a cycle visiting each vertex exactly once; Hamiltonian path is the variant without returning to start. Both are NP-complete. Unlike shortest-cycle detection (solvable in polynomial time by DFS), finding a Hamiltonian path/cycle appears intrinsically hard, requiring potentially checking all permutations. The problems highlight the distinction between decision (NP) and optimization: verifying a Hamiltonian cycle is quick, but finding one seems impossible in polynomial time.
