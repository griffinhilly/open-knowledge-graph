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
status: validated
---

# Graph Coloring Register Allocation

## Core Idea
Register allocation models the problem as a graph coloring problem: nodes are variables, edges connect variables that interfere (are live simultaneously), and colors are registers. Finding a k-coloring is NP-hard, so practical allocators use heuristics like spill-cost-driven node selection.

## How It's Best Learned
Implement graph-coloring register allocation including live variable analysis, interference graph construction, and spilling.

## Questions

```yaml
- question: "In Chaitin's simplification heuristic, when the algorithm finds no node with fewer than k neighbors in the interference graph, what happens next?"
  type: multiple-choice
  options:
    - "The algorithm restarts with a different initial state ordering"
    - "One variable is chosen to spill to memory, load/store instructions are inserted, and the interference graph is rebuilt"
    - "The compiler increases the number of available registers by saving some to the stack frame"
    - "The algorithm reports failure and prevents the function from compiling"
  answer: 1
  explanation: "When every node has at least k neighbors, no node is guaranteed to be colorable — a spill is necessary. The allocator selects a variable to live in memory instead of a register, inserts loads before each use and stores after each definition, and then repeats the entire analysis on the modified code. Spilling changes the interference graph, so multiple rounds may be needed."

- question: "A variable is live across 1,000 instructions inside a hot inner loop. The interference graph cannot be k-colored. Is this variable a good candidate to spill?"
  type: multiple-choice
  options:
    - "Yes — variables with long live ranges have many interfering edges and their removal most simplifies the graph"
    - "No — spilling it inserts load and store instructions inside the tight inner loop, causing high memory traffic on the most-executed code path"
    - "Yes — variables that interfere with many others cost the most registers and must be eliminated first"
    - "Neutral — spill cost depends only on register pressure at the spill point, not on loop execution frequency"
  answer: 1
  explanation: "Spill cost is highest for variables used frequently in hot code. A variable live through 1,000 iterations of an inner loop requires a load and store on every iteration — potentially millions of extra memory operations at runtime. Good allocators weight spill decisions by execution frequency (often from profiling), strongly preferring to spill variables in cold paths over those in inner loops."

- question: "Two variables must be assigned different physical registers (colors) in graph-coloring register allocation if and only if their live ranges overlap at some program point."
  type: true-false
  answer: true
  explanation: "This is the definition of interference. If two variables are simultaneously live — both holding values needed later — they cannot share a register without corrupting one another. The interference graph encodes exactly this: an edge between nodes means their live ranges overlap and they must receive different colors (registers)."

- question: "Graph-coloring register allocation always produces the minimum possible number of spills for a given program."
  type: true-false
  answer: false
  explanation: "Finding an optimal k-coloring is NP-hard in general. Practical allocators use polynomial-time heuristics (like Chaitin's simplification) that work well in practice but provide no optimality guarantee. The heuristic may spill a variable that a smarter (exponential-time) algorithm could have kept in a register."

- question: "What is an interference graph, and why does building it correctly require live variable analysis?"
  type: short-answer
  answer: "An interference graph has one node per virtual variable and an edge between any two variables whose live ranges overlap — meaning there is some program point where both hold values needed later. Live variable analysis is a backward dataflow pass that determines, at every program point, which variables are live. Without it, the compiler cannot know which pairs of variables are simultaneously alive and therefore cannot correctly identify which pairs must not share a register."
  explanation: "The interference graph is the key abstraction that converts register allocation into graph coloring. Edges represent conflicts. Live variable analysis is a prerequisite because liveness is a global property — a variable is live at a point if it is used on some future execution path, which requires reasoning backward through the control-flow graph."
```

## Explainer

From your study of register allocation, you know the fundamental problem: a program may use hundreds or thousands of virtual variables (temporaries), but the target machine has a fixed number of physical registers — typically 16 to 32 for general-purpose use. The compiler must map virtual variables to physical registers so that no two variables that are "alive" at the same time share a register. If you have studied graph coloring, you will immediately see the connection: this is exactly the problem of coloring the nodes of a graph with a limited number of colors so that no two adjacent nodes share a color.

The **interference graph** makes this mapping explicit. Each virtual variable becomes a node. Two nodes are connected by an edge if their **live ranges** overlap — meaning there exists some program point where both variables hold values that will be needed later. Building this graph requires **live variable analysis**, a backward dataflow problem that determines, at each point, which variables are live (will be used before being redefined). Once the interference graph is built, register allocation reduces to finding a **k-coloring**, where k is the number of available physical registers. If two variables interfere, they get different colors (registers); if they don't interfere, they *may* share a register.

The classic algorithm is **Chaitin's simplification heuristic**. It works by iterative simplification: find a node with fewer than k neighbors, remove it from the graph (pushing it onto a stack), and repeat. The intuition is that a node with fewer than k neighbors can always be colored regardless of its neighbors' colors — there is always a color left over. When the graph is empty, pop nodes off the stack and assign each one a color not used by its already-colored neighbors. If at some point no node has fewer than k neighbors, a **spill** is needed: one variable must be stored in memory rather than a register. The choice of which variable to spill is guided by **spill cost** heuristics — prefer variables that are used infrequently or live across many instructions, and avoid spilling variables inside tight loops.

Spilling is not free. A spilled variable requires inserting load and store instructions around every use and definition, which increases code size and introduces memory traffic. After spilling, the interference graph changes (new temporaries for loads/stores), so the allocator rebuilds and recolors — potentially requiring multiple rounds. Modern allocators refine this framework with **coalescing** (merging non-interfering variables connected by move instructions to eliminate copies), **live range splitting** (splitting a variable into segments so only part of it spills), and **priority-based coloring** that considers execution frequency. The graph coloring framework remains the dominant approach in production compilers because it produces high-quality allocations and has a clean theoretical foundation, even though optimal coloring is NP-hard and the heuristics do not always find the best solution.
