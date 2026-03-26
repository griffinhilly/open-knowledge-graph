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
status: validated
---

# Register Allocation

## Core Idea
Register allocation assigns variables to CPU registers and memory locations. A variable can use a register if its live ranges don't overlap with other variables' (no two live variables can share a register). This is modeled as a graph coloring problem: variables are nodes, edges connect interfering variables, and colors are registers. Spilling (moving to memory) is required when coloring exceeds available registers.

## Questions

```yaml
- question: "Two variables x and y both appear in the same function. Variable x holds the result of a computation that is only used at line 5, and y is first assigned at line 8. Can they safely share a register?"
  type: multiple-choice
  options:
    - "No — two variables can never share a register in the same function"
    - "Yes — their live ranges don't overlap, so they don't interfere and can share a register"
    - "Only if they have the same data type"
    - "Only if the compiler can prove they hold the same value"
  answer: 1
  explanation: "Two variables can share a register whenever their live ranges don't overlap — that is, they are never simultaneously alive. x is live only up to line 5 (where its last use occurs); y only becomes live at line 8 (its assignment). Since there is no point where both are simultaneously alive, they don't interfere in the interference graph, so there is no edge between them, and they can receive the same color (register)."

- question: "The graph coloring heuristic for register allocation works by repeatedly removing nodes with fewer than k neighbors. Why does this guarantee those nodes can always be colored at assignment time?"
  type: multiple-choice
  options:
    - "Nodes with fewer neighbors interfere with fewer variables, so they are less important and can be spilled cheaply"
    - "A node with fewer than k neighbors will always have at least one color available no matter what colors its neighbors receive, since there are k colors and fewer than k constraints"
    - "Low-degree nodes are always assigned to callee-saved registers, which are always available"
    - "The heuristic does not guarantee colorability — it just provides an approximation"
  answer: 1
  explanation: "This is the key insight of the Chaitin-Briggs coloring heuristic. If a node has degree < k, then its neighbors can use at most (k–1) distinct colors, leaving at least one color free for this node regardless of how neighbors are colored. So when you pop this node off the stack after all its neighbors are colored, you are guaranteed a valid color exists. This is not just a heuristic — it is a provable guarantee for nodes that were removed during the simplification phase."

- question: "Spilling a variable that is used inside a deeply nested loop is more expensive than spilling a variable used once outside any loop."
  type: true-false
  answer: true
  explanation: "Spilling inserts a store before the variable's definition and a load before each of its uses, replacing register access with memory access. If the variable is inside a loop that executes N times, these loads and stores execute N times per loop iteration — potentially millions of times at runtime. A variable used once outside any loop incurs the memory access cost only once. Good allocators use loop depth and use frequency as part of their spill cost heuristic to minimize the runtime penalty of spilling."

- question: "Two variables that are seldom simultaneously live can still interfere and is expected to be given different registers if they are both used in the same basic block."
  type: true-false
  answer: false
  explanation: "Interference is defined entirely by live range overlap — two variables interfere if and only if they are simultaneously live at some program point. Being in the same basic block is irrelevant; what matters is whether both are alive at the same time. If x's live range ends before y's begins (even within the same block), they have no edge in the interference graph and can share a register. This is precisely why live variable analysis must be computed before building the interference graph."

- question: "Why is live variable analysis a required prerequisite for register allocation, and what would go wrong if you tried to allocate registers without it?"
  type: short-answer
  answer: "Live variable analysis determines, for every program point, which variables hold values that will be used in the future — their live ranges. Register allocation needs this to know which pairs of variables must not share a register (those that are simultaneously live). Without it, you cannot construct the interference graph. If you naively gave every variable its own register, you would need as many registers as variables — usually far more than the hardware has. Without live range information, you also cannot identify opportunities for register sharing between variables whose lifetimes don't overlap, leading to unnecessary and costly spills."
  explanation: "The entire graph coloring model depends on live ranges: nodes are variables, edges connect variables that are simultaneously live, and graph coloring assigns registers such that interfering variables get different ones. Live variable analysis is what makes this model possible. It reveals that many variables in a real program never coexist simultaneously, allowing the compiler to reuse registers far more aggressively than a naive one-variable-one-register approach — often keeping most variables in the small register file that modern CPUs provide."
```

## Explainer

After the compiler generates intermediate code, every temporary variable and user variable needs a home in the machine. Registers are the fastest storage a CPU has — an operation on registers can complete in a single cycle, while a memory access may cost dozens of cycles or more. **Register allocation** is the compiler phase that decides which variables live in registers and which get demoted to slower memory (the stack), directly determining how fast the generated code will run.

The problem connects two concepts you already know. From **live variable analysis**, you can determine for each point in the program which variables are simultaneously "alive" — meaning their current values will be used before being overwritten. Two variables that are live at the same time **interfere**: they cannot share a register because both values must be accessible. The compiler builds an **interference graph** where each variable is a node and an edge connects every pair of variables that interfere. The question then becomes: can you assign one of *k* colors (registers) to each node such that no two adjacent nodes share a color? This is exactly the **graph coloring** problem.

Graph coloring with *k* colors is NP-complete in general, but compilers use a remarkably effective heuristic. The key insight is that any node with fewer than *k* neighbors can always be colored: no matter what colors its neighbors use, at least one color remains available. The algorithm repeatedly removes such low-degree nodes from the graph (pushing them onto a stack), simplifying the graph until it is empty or only high-degree nodes remain. Then it pops nodes off the stack and assigns colors — each node's neighbors are already colored, and by construction a valid color exists. When a node cannot be removed because all remaining nodes have *k* or more neighbors, the compiler must **spill** one variable to memory, inserting load and store instructions around its uses.

Choosing which variable to spill is a critical decision. A variable used inside a deeply nested loop is expensive to spill because every load and store happens on each iteration. A variable used once outside any loop is cheap to spill. Good allocators use cost heuristics that weigh use frequency, loop depth, and the number of interferences. Some allocators also **coalesce** — if a copy instruction `x = y` exists and `x` and `y` don't interfere, they can be assigned the same register, eliminating the copy entirely. The interplay between spilling, coalescing, and coloring makes register allocation one of the most studied and practically impactful optimizations in compiler design.
