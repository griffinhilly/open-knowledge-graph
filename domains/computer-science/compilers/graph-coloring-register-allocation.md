---
id: graph-coloring-register-allocation
title: Graph Coloring Register Allocation
domain: computer-science
course: compilers
prerequisites:
- id: instruction-selection-techniques
  type: hard
- id: register-allocation
  type: hard
- id: graph-coloring
  type: soft
builds-toward:
- code-emission-target-generation
tags:
- register-allocation
- graph-coloring
- backend
stage: advanced
status: draft
---

# Graph Coloring Register Allocation

## Core Idea
Register allocation models the problem as a graph coloring problem: nodes are variables, edges connect variables that interfere (are live simultaneously), and colors are registers. Finding a k-coloring is NP-hard, so practical allocators use heuristics like spill-cost-driven node selection.

## How It's Best Learned
Implement graph-coloring register allocation including live variable analysis, interference graph construction, and spilling.

## Explainer

From your study of register allocation, you know the fundamental problem: a program may use hundreds or thousands of virtual variables (temporaries), but the target machine has a fixed number of physical registers — typically 16 to 32 for general-purpose use. The compiler must map virtual variables to physical registers so that no two variables that are "alive" at the same time share a register. If you have studied graph coloring, you will immediately see the connection: this is exactly the problem of coloring the nodes of a graph with a limited number of colors so that no two adjacent nodes share a color.

The **interference graph** makes this mapping explicit. Each virtual variable becomes a node. Two nodes are connected by an edge if their **live ranges** overlap — meaning there exists some program point where both variables hold values that will be needed later. Building this graph requires **live variable analysis**, a backward dataflow problem that determines, at each point, which variables are live (will be used before being redefined). Once the interference graph is built, register allocation reduces to finding a **k-coloring**, where k is the number of available physical registers. If two variables interfere, they get different colors (registers); if they don't interfere, they *may* share a register.

The classic algorithm is **Chaitin's simplification heuristic**. It works by iterative simplification: find a node with fewer than k neighbors, remove it from the graph (pushing it onto a stack), and repeat. The intuition is that a node with fewer than k neighbors can always be colored regardless of its neighbors' colors — there is always a color left over. When the graph is empty, pop nodes off the stack and assign each one a color not used by its already-colored neighbors. If at some point no node has fewer than k neighbors, a **spill** is needed: one variable must be stored in memory rather than a register. The choice of which variable to spill is guided by **spill cost** heuristics — prefer variables that are used infrequently or live across many instructions, and avoid spilling variables inside tight loops.

Spilling is not free. A spilled variable requires inserting load and store instructions around every use and definition, which increases code size and introduces memory traffic. After spilling, the interference graph changes (new temporaries for loads/stores), so the allocator rebuilds and recolors — potentially requiring multiple rounds. Modern allocators refine this framework with **coalescing** (merging non-interfering variables connected by move instructions to eliminate copies), **live range splitting** (splitting a variable into segments so only part of it spills), and **priority-based coloring** that considers execution frequency. The graph coloring framework remains the dominant approach in production compilers because it produces high-quality allocations and has a clean theoretical foundation, even though optimal coloring is NP-hard and the heuristics do not always find the best solution.
