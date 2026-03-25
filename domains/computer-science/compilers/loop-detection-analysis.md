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
- id: loop-unrolling-optimization
  type: soft
- id: use-definition-chains
  type: soft
- id: loop-invariant-code-motion
  type: soft
builds-toward:
- array-subscript-optimization
- code-optimization
tags:
- analysis
- loops
- optimization
stage: advanced
status: validated
---
# Loop Detection and Analysis

## Core Idea
Loop detection identifies blocks forming loops and computes properties like nesting depth, headers, and latches. This information is essential for loop-specific optimizations like invariant code motion and vectorization. Loop analysis uses depth-first search on control-flow graphs.

## How It's Best Learned
Implement loop detection using DFS and build a loop nest tree. Identify irreducible loops and understand their challenges.

## Common Misconceptions
All loops have a single entry point (irreducible loops have multiple entries). Loop nesting depth determines optimization opportunity (depth is one factor; size and iteration count matter too).

## Questions

```yaml
- question: "In a control-flow graph, a back edge runs from node L to node H. What structural condition on H and L makes this a natural loop back edge?"
  type: multiple-choice
  options:
    - "L must dominate H — control must always flow through L before H"
    - "H must dominate L — control must always flow through H before L"
    - "H and L must be in the same strongly connected component with no other entries"
    - "L must be the only predecessor of H in the CFG"
  answer: 1
  explanation: "A back edge is defined as an edge from L to H where H dominates L — meaning every path from the CFG entry to L passes through H. H is the loop header: it is the single required entry point. The dominance requirement is what makes it a 'natural' loop; without it, the loop would be irreducible (multiple entries). Option A has the relationship reversed: it is H that dominates L, not the other way around."

- question: "A nested loop has an outer loop running 100 iterations and an inner loop running 10 iterations per outer iteration. Which loop should be the primary target for optimization, and why?"
  type: multiple-choice
  options:
    - "The outer loop, because it controls when the inner loop executes"
    - "The inner loop, because a single operation moved out of it saves 1,000 executions, not just 100"
    - "Both equally — nesting depth alone determines optimization priority"
    - "Neither — compilers optimize loops based only on instruction count, not iteration count"
  answer: 1
  explanation: "The inner loop executes 100 × 10 = 1,000 times total, while the outer loop header executes only 100 times. Moving a loop-invariant computation out of the inner loop saves 999 redundant executions; moving it out of only the outer loop saves 99. This is why compilers prioritize innermost loops: they represent the highest iteration density, and any savings there multiplies across all outer iterations. Nesting depth is a proxy, but iteration count and operation cost are the real drivers."

- question: "Every loop in a well-formed program has exactly one entry point (header), making all loops natural loops."
  type: true-false
  answer: false
  explanation: "Irreducible loops, which arise from unstructured control flow such as 'goto' statements or certain hand-written assembly patterns, have multiple entry points. Control can reach the loop body through more than one block, so no single header dominates all loop nodes. These are not natural loops. Compilers handle irreducible loops by either transforming them via node splitting or conservatively skipping optimizations on them."

- question: "Loop-invariant code motion — moving computations whose operands don't change within a loop to just before the loop — can only be safely applied after loop detection has identified the loop's header and body."
  type: true-false
  answer: true
  explanation: "To hoist an expression out of a loop, the compiler must know (1) what constitutes the loop body, (2) that the expression is computed on every execution path through the body, and (3) that it is safe to execute it earlier. All three require knowing the loop structure: its header, back edges, and body nodes. Without loop detection, the compiler cannot identify which code is 'inside' the loop or where to place the hoisted computation."

- question: "What makes an irreducible loop challenging for compiler optimization, and how do compilers typically handle it?"
  type: short-answer
  answer: "An irreducible loop has multiple entry points — no single header dominates all nodes in the loop. This breaks the assumption underlying most loop analyses: that there is one place to check loop-invariant properties and one 'pre-header' where hoisted code can be placed. Without a unique entry, induction variable detection, invariant code motion, and vectorization all become unsafe or ambiguous. Compilers typically respond either by converting the irreducible loop into a reducible one via node splitting (duplicating a shared node to give each entry path its own copy) or by skipping loop-specific optimizations on those regions entirely."
  explanation: "Irreducibility is rare in code generated from structured high-level languages, which is why most programmers never encounter it directly. But it matters at the compiler level because even a single irreducible region can block optimization of surrounding code."
```

## Explainer

You already know how to build a **control-flow graph** (CFG) where each node is a basic block and edges represent branches. You also understand data dependence — which statements read values produced by others. Loop detection takes these foundations and asks a structural question: which regions of the CFG execute repeatedly, and what are their properties?

The central concept is the **natural loop**. In a CFG, a natural loop is defined by a **back edge** — an edge from a node back to a node that dominates it. The target of the back edge is the **loop header** (the single entry point), and the source is the **latch** (where control flows back). To find all natural loops, you first compute the **dominator tree** of the CFG using depth-first search, then identify every back edge. For each back edge from latch L to header H, the loop body consists of H plus all nodes that can reach L without going through H. This is computed by a simple backward walk from L, collecting nodes until you hit H.

Consider a concrete example: a `while` loop in source code produces a CFG where the condition-check block dominates the loop body, and the body's exit edge leads back to the condition check. That back edge defines the loop. A nested `for` loop inside the `while` creates an inner loop whose header is dominated by the outer header, forming a **loop nest tree** — a hierarchy where inner loops are children of outer loops. This nesting structure is critical because optimizers treat inner loops differently: the innermost loop is where a program spends most of its time, so it receives the most aggressive optimization (unrolling, vectorization, software pipelining).

Not all loops are so well-behaved. An **irreducible loop** has multiple entry points — control can enter the loop body at more than one block. These arise from unstructured control flow like `goto` statements. Irreducible loops break the assumption that every loop has a single header, which complicates most loop optimizations. Compilers typically handle irreducible loops by either transforming them into reducible form (node splitting) or conservatively skipping optimizations on them. Recognizing irreducible loops is itself part of loop detection: if a back edge targets a node that does not dominate the source, the loop is irreducible.

Once loops are detected, **loop analysis** computes the properties optimizers need: iteration count (exact or estimated), induction variables (variables that change by a fixed amount each iteration), loop-invariant expressions (computations whose operands do not change within the loop), and memory access patterns. These properties feed directly into loop-invariant code motion, strength reduction, loop unrolling, and auto-vectorization. Without accurate loop detection, none of these transformations can be applied safely — the compiler would not know which code repeats or how to restructure it.
