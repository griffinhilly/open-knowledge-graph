---
id: register-allocation
title: Register Allocation
domain: computer-science
course: compilers
prerequisites:
- id: live-variable-analysis
  type: hard
- id: instruction-set-architecture
  type: soft
- id: graph-coloring
  type: hard
builds-toward:
- code-generation
tags:
- register-allocation
- code-generation
- architecture
stage: advanced
status: draft
---

# Register Allocation

## Core Idea
Register allocation assigns variables to CPU registers and memory locations. A variable can use a register if its live ranges don't overlap with other variables' (no two live variables can share a register). This is modeled as a graph coloring problem: variables are nodes, edges connect interfering variables, and colors are registers. Spilling (moving to memory) is required when coloring exceeds available registers.

## Explainer

After the compiler generates intermediate code, every temporary variable and user variable needs a home in the machine. Registers are the fastest storage a CPU has — an operation on registers can complete in a single cycle, while a memory access may cost dozens of cycles or more. **Register allocation** is the compiler phase that decides which variables live in registers and which get demoted to slower memory (the stack), directly determining how fast the generated code will run.

The problem connects two concepts you already know. From **live variable analysis**, you can determine for each point in the program which variables are simultaneously "alive" — meaning their current values will be used before being overwritten. Two variables that are live at the same time **interfere**: they cannot share a register because both values must be accessible. The compiler builds an **interference graph** where each variable is a node and an edge connects every pair of variables that interfere. The question then becomes: can you assign one of *k* colors (registers) to each node such that no two adjacent nodes share a color? This is exactly the **graph coloring** problem.

Graph coloring with *k* colors is NP-complete in general, but compilers use a remarkably effective heuristic. The key insight is that any node with fewer than *k* neighbors can always be colored: no matter what colors its neighbors use, at least one color remains available. The algorithm repeatedly removes such low-degree nodes from the graph (pushing them onto a stack), simplifying the graph until it is empty or only high-degree nodes remain. Then it pops nodes off the stack and assigns colors — each node's neighbors are already colored, and by construction a valid color exists. When a node cannot be removed because all remaining nodes have *k* or more neighbors, the compiler must **spill** one variable to memory, inserting load and store instructions around its uses.

Choosing which variable to spill is a critical decision. A variable used inside a deeply nested loop is expensive to spill because every load and store happens on each iteration. A variable used once outside any loop is cheap to spill. Good allocators use cost heuristics that weigh use frequency, loop depth, and the number of interferences. Some allocators also **coalesce** — if a copy instruction `x = y` exists and `x` and `y` don't interfere, they can be assigned the same register, eliminating the copy entirely. The interplay between spilling, coalescing, and coloring makes register allocation one of the most studied and practically impactful optimizations in compiler design.
