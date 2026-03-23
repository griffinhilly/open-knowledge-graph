---
id: dataflow-analysis
title: Dataflow Analysis
domain: computer-science
course: compilers
prerequisites:
- id: control-flow-graphs
  type: hard
- id: fixpoint-computation
  type: hard
- id: graph-theory-fundamentals
  type: soft
- id: graph-theory-intro
  type: soft
builds-toward:
- reaching-definitions-analysis
- live-variable-analysis
- code-optimization
tags:
- dataflow
- program-analysis
- optimization
stage: advanced
status: validated
---

# Dataflow Analysis

## Core Idea
Dataflow analysis computes information about how data flows through a program. It solves systems of constraints on basic blocks, iterating until a fixpoint is reached. Forward analyses (reaching definitions) track properties forward through the CFG; backward analyses (live variables) track them backward. Dataflow results enable optimizations like constant propagation and dead-code elimination.

## Questions

```yaml
- question: "Live variable analysis asks: at each program point, which variables might be used before being overwritten on some path from that point? Why is this a backward analysis rather than a forward one?"
  type: multiple-choice
  options: ["Because it only applies to loops, which must be traversed in reverse", "Because the information needed at a point depends on what happens later (at uses), not earlier (at definitions)", "Because CFG edges are reversed in all standard analyses", "Because backward analyses are faster to compute than forward ones"]
  answer: 1
  explanation: "A variable is live at point p if there is a path from p to some use of the variable with no intervening definition. That information flows from uses backward toward definitions — you learn that x is live at an earlier point because you see it used at a later point. Reaching definitions, by contrast, asks whether a definition made earlier 'reaches' a later point, which flows forward."

- question: "In a reaching definitions analysis, a definition of variable x at point d 'reaches' point p if there is a path from d to p along which x is not redefined."
  type: true-false
  answer: true
  explanation: "This is the standard definition. A definition is 'killed' when the same variable is assigned again on the path. Reaching definitions is a forward analysis: you propagate the set of definitions that reach the entry of each basic block forward through the CFG, generating new definitions and killing old ones at each assignment."

- question: "Why is fixpoint iteration in dataflow analysis guaranteed to terminate, and what property of the transfer functions ensures this?"
  type: short-answer
  answer: "The dataflow values live in a finite lattice, and the transfer functions are monotone — each iteration can only move values in one direction (toward greater or lesser information). Since the lattice has finite height, values cannot keep changing forever; they must stabilize."
  explanation: "At each iteration, the dataflow sets at each block can only grow (for may-analyses like reaching definitions) or shrink (for must-analyses). Because program variables and definitions are finite, the sets are bounded. Monotonicity means no iteration can reverse a prior change, so the sequence of iterates is monotonically increasing (or decreasing) and bounded — by the finite chain condition, it must reach a fixpoint."
```

## Explainer

Dataflow analysis is a family of techniques for computing facts about a program's runtime behavior using only the static structure of its code. Instead of executing the program, you reason about what *could* happen on any possible execution path — and you do this by working with the control-flow graph (CFG) you already know, propagating information from block to block until the solution stabilizes.

The framework works as follows. Each basic block has a **transfer function** that describes how that block transforms the dataflow information. For reaching definitions, for example, a block that assigns `x = 3` *generates* that definition and *kills* any earlier definition of `x`. The global solution must satisfy the **dataflow equations**: the information at the entry of each block equals the meet (union or intersection, depending on the analysis) of the information at the exit of all its predecessors. You initialize all blocks conservatively, then iterate — recomputing each block's entry and exit sets using the current values of its neighbors — until nothing changes. That stable state is the fixpoint.

The direction of propagation divides analyses into two classes. **Forward analyses** flow information in the same direction as execution: the facts at block B's entry depend on B's predecessors. Reaching definitions is the canonical example — you ask which assignments made earlier might still be "live" as you enter B. **Backward analyses** flow in reverse: the facts at B's entry depend on what happens in B's successors. Live variable analysis is the canonical example — a variable is live entering B if it might be used before being overwritten on some path *continuing from* B. Recognizing which direction an analysis flows is the key to setting up the equations correctly.

Termination is guaranteed because dataflow values inhabit a **finite lattice**, and the transfer functions are **monotone** — each iteration can only add information (for union-based analyses) or remove it (for intersection-based analyses), never reverse a prior change. Since the sets of definitions or variables are finite, this monotone sequence must eventually plateau. In practice, convergence is fast — often in just a few passes, with loops requiring at most as many iterations as the nesting depth.

Dataflow results directly power compiler optimizations. Reaching definitions enable **constant propagation**: if only one definition of `x` reaches a use and that definition assigns a constant, the use can be replaced with the constant. Live variable analysis enables **dead-code elimination**: if a variable is assigned but not live afterward (never used before being overwritten), the assignment can be removed. These are among the most impactful optimizations in production compilers, and both rest on the same algorithmic foundation of iterative fixpoint computation over the CFG.
