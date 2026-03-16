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

## Explainer

From your study of control flow graphs, you know that a program's execution can follow many paths through branches, loops, and function calls. **Fixpoint computation** is the technique that lets a compiler reason about *all* those paths simultaneously, answering questions like "which variables are definitely initialized at this point?" or "which expressions have already been computed and can be reused?" The key insight is that these questions can be formulated as equations over the CFG, and solving those equations means iterating until the answers stop changing — reaching a **fixpoint**.

Here is the concrete picture. For each basic block in the CFG, you define a **transfer function** that describes how executing that block transforms the dataflow information. For reaching definitions analysis, the transfer function says: "this block kills definitions of variable x and generates a new definition of x at line 7." You also define **merge functions** at points where control flow joins (after an if-else, at loop headers): typically union ("a definition reaches here if it reaches along *any* incoming edge") or intersection ("a definition reaches here only if it reaches along *all* incoming edges"). You start with an initial approximation — often the most conservative assumption, like "nothing is known" — and then walk through the CFG, applying transfer functions and merge functions, updating the dataflow information at each block. When no block's information changes in a complete pass, you have reached the fixpoint: the solution.

Convergence is guaranteed by two mathematical properties. First, the dataflow values form a **lattice** — a partially ordered set where every pair of elements has a well-defined join (least upper bound) and meet (greatest lower bound), and the lattice has finite height. Second, the transfer functions are **monotonic**: they never move information "downward" in the lattice. Together, these properties guarantee that each iteration can only move values upward (or leave them unchanged), and since the lattice has finite height, the process must terminate. For a reaching definitions analysis on a program with *n* definitions, the lattice is the power set of definitions ordered by subset inclusion, with height *n* — so convergence takes at most *n* passes.

The order in which you process blocks matters for efficiency, not correctness. A naive approach processes every block on every pass. A **worklist algorithm** maintains a queue of blocks whose inputs have changed and only reprocesses those blocks, often converging in far fewer steps. For forward analyses (like reaching definitions), processing blocks in reverse postorder — roughly, processing predecessors before successors — minimizes redundant work. For backward analyses (like liveness), reverse postorder on the reversed CFG works best. These are practical optimizations; the fixpoint itself is the same regardless of iteration order, which is one of the elegant properties of the framework.
