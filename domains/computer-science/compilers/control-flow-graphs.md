---
id: control-flow-graphs
title: Control Flow Graphs
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: graph-theory-fundamentals
  type: soft
- id: directed-graphs-and-digraphs
  type: soft
builds-toward:
- dataflow-analysis
tags:
- cfg
- program-analysis
- graph-representation
stage: advanced
status: validated
---

# Control Flow Graphs

## Core Idea
A control flow graph (CFG) represents a program's control structure as a directed graph where nodes are basic blocks (straight-line code with one entry/exit) and edges represent jumps. CFGs are the foundation for program analysis: dominance, loops, and dataflow properties are computed on CFGs. Building and analyzing CFGs is essential for optimization and verification.

## Questions

```yaml
- question: "Which of the following best defines a basic block in a control flow graph?"
  type: multiple-choice
  options:
    - "Any single three-address instruction in the intermediate representation."
    - "A maximal sequence of consecutive instructions with exactly one entry point (no jumps into the middle) and one exit point (execution falls through or branches only at the end)."
    - "Any loop body identified by a back edge in the CFG."
    - "A set of instructions that all access the same variable."
  answer: 1
  explanation: "A basic block is defined by the absence of internal control flow: once execution enters the first instruction, every subsequent instruction in the block is guaranteed to execute before any branch. 'Maximal' means we extend the block as far as possible before hitting a branch or a branch target. This guarantee — that the whole block runs or none of it does — is exactly what enables optimizations like local dead-code elimination and constant folding within a block."

- question: "In a CFG, a conditional branch instruction (such as an if-else) always produces exactly two outgoing edges from the basic block that contains it."
  type: true-false
  answer: true
  explanation: "A conditional branch has two possible successor states: the taken branch (true branch) and the fall-through (false branch). Both must be represented as outgoing edges so the CFG accurately models all possible execution paths. An unconditional jump produces one outgoing edge, and a return instruction typically connects to a special EXIT node or has no outgoing edge (depending on the CFG model)."

- question: "A naive approach to optimization would operate instruction-by-instruction across the whole program. Why do compiler writers instead build a CFG and work with basic blocks as the unit of analysis?"
  type: short-answer
  answer: "Within a basic block, control flow is linear and predictable: every instruction executes in sequence whenever any instruction in the block executes. This lets optimizations like constant propagation, common subexpression elimination, and liveness analysis make guarantees that would require tracking branching for individual instructions. The CFG then lifts these per-block results to the whole program, connecting blocks via edges so inter-block (global) analyses like reaching definitions and dominator trees can be computed with standard graph algorithms."
  explanation: "Basic blocks partition the program into chunks where local reasoning is safe, and the CFG provides the graph structure for global reasoning. This two-level decomposition — local optimization within blocks, global analysis on the CFG — is the core architecture of almost every optimizing compiler, from GCC to LLVM. The alternative (working instruction-by-instruction across arbitrary control flow) would require re-analyzing every possible execution path at every step."
```

## Explainer

When a compiler translates source code into intermediate representation (IR), it produces a flat list of three-address instructions. But a flat list hides a crucial dimension: not every instruction always executes. Branches, loops, and function returns mean that execution can take many paths through the code. A control flow graph makes this structure explicit by turning the flat instruction list into a directed graph that mirrors all the ways the program can actually run.

The first step in building a CFG is identifying **basic blocks**. A basic block is a maximal run of instructions with a single entry point (no jumps land in the middle) and a single exit point (only the last instruction may be a branch). Within a basic block, control flow is perfectly sequential: if the first instruction executes, all of them do. This is a powerful guarantee for optimization — you can propagate constants, eliminate dead code, and allocate registers within a block using only local information, without worrying about branching.

The second step is adding **edges**. After each basic block, execution either falls through to the next block, jumps unconditionally to some target, or branches conditionally to one of two targets. Each possibility becomes a directed edge in the CFG. A conditional if-else creates two outgoing edges from the block containing the branch: one to the "then" block and one to the "else" block. Loops create **back edges** — edges that point backward to an earlier block — which are the graph-theoretic signature of a loop. Finding all back edges lets the compiler identify natural loops and apply loop-specific optimizations like loop-invariant code motion.

With the CFG in hand, the compiler can compute **global properties** across all blocks. Dominator analysis asks: for each basic block B, which blocks must every execution path pass through before reaching B? The dominator tree organizes this information and enables structured optimizations like partial redundancy elimination. Liveness analysis uses the CFG edges in reverse to determine which variables are still needed at each program point, enabling efficient register allocation. All of these analyses — which you will study in depth as dataflow analysis — are defined as fixed-point computations on the CFG structure.

The CFG is not just an internal compiler data structure; it is also the foundation for static analysis tools, test coverage measurement (branch coverage counts CFG edges), and program verification. When a security scanner checks for use-after-free errors or null-pointer dereferences, it is walking paths through the program's CFG. Understanding the CFG therefore unlocks not just compiler optimizations but the broader field of program analysis.
