---
id: loop-detection-analysis
title: Loop Detection and Analysis
domain: computer-science
course: compilers
prerequisites:
- id: data-dependence-analysis
  type: hard
- id: control-flow-graphs
  type: hard
builds-toward:
- array-subscript-optimization
- global-optimization-techniques
tags:
- analysis
- loops
- optimization
stage: advanced
status: draft
---

# Loop Detection and Analysis

## Core Idea
Loop detection identifies blocks forming loops and computes properties like nesting depth, headers, and latches. This information is essential for loop-specific optimizations like invariant code motion and vectorization. Loop analysis uses depth-first search on control-flow graphs.

## How It's Best Learned
Implement loop detection using DFS and build a loop nest tree. Identify irreducible loops and understand their challenges.

## Common Misconceptions
All loops have a single entry point (irreducible loops have multiple entries). Loop nesting depth determines optimization opportunity (depth is one factor; size and iteration count matter too).

## Explainer

You already know how to build a **control-flow graph** (CFG) where each node is a basic block and edges represent branches. You also understand data dependence — which statements read values produced by others. Loop detection takes these foundations and asks a structural question: which regions of the CFG execute repeatedly, and what are their properties?

The central concept is the **natural loop**. In a CFG, a natural loop is defined by a **back edge** — an edge from a node back to a node that dominates it. The target of the back edge is the **loop header** (the single entry point), and the source is the **latch** (where control flows back). To find all natural loops, you first compute the **dominator tree** of the CFG using depth-first search, then identify every back edge. For each back edge from latch L to header H, the loop body consists of H plus all nodes that can reach L without going through H. This is computed by a simple backward walk from L, collecting nodes until you hit H.

Consider a concrete example: a `while` loop in source code produces a CFG where the condition-check block dominates the loop body, and the body's exit edge leads back to the condition check. That back edge defines the loop. A nested `for` loop inside the `while` creates an inner loop whose header is dominated by the outer header, forming a **loop nest tree** — a hierarchy where inner loops are children of outer loops. This nesting structure is critical because optimizers treat inner loops differently: the innermost loop is where a program spends most of its time, so it receives the most aggressive optimization (unrolling, vectorization, software pipelining).

Not all loops are so well-behaved. An **irreducible loop** has multiple entry points — control can enter the loop body at more than one block. These arise from unstructured control flow like `goto` statements. Irreducible loops break the assumption that every loop has a single header, which complicates most loop optimizations. Compilers typically handle irreducible loops by either transforming them into reducible form (node splitting) or conservatively skipping optimizations on them. Recognizing irreducible loops is itself part of loop detection: if a back edge targets a node that does not dominate the source, the loop is irreducible.

Once loops are detected, **loop analysis** computes the properties optimizers need: iteration count (exact or estimated), induction variables (variables that change by a fixed amount each iteration), loop-invariant expressions (computations whose operands do not change within the loop), and memory access patterns. These properties feed directly into loop-invariant code motion, strength reduction, loop unrolling, and auto-vectorization. Without accurate loop detection, none of these transformations can be applied safely — the compiler would not know which code repeats or how to restructure it.
