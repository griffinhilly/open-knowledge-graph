---
id: fixpoint-computation
title: Fixpoint Computation and Iteration
domain: computer-science
course: compilers
prerequisites:
- id: control-flow-graphs
  type: hard
builds-toward:
- dataflow-analysis
tags:
- fixpoint
- iteration
- convergence
stage: advanced
status: draft
---

# Fixpoint Computation and Iteration

## Core Idea
Dataflow analysis problems are solved by iterating transfer functions until a fixpoint (no change in values) is reached. Values form a lattice-like structure with a partial order; transfer functions must be monotonic for convergence. Different iteration orders (forward, backward, worklist) affect convergence speed. Widening operators ensure termination on infinite lattices.
