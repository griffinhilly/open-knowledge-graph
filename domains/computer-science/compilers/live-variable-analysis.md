---
id: live-variable-analysis
title: Live Variable Analysis
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
builds-toward:
- register-allocation
- dead-code-elimination
tags:
- liveness
- dataflow
- code-quality
stage: advanced
status: draft
---

# Live Variable Analysis

## Core Idea
Live variable analysis determines which variables may be used in the future from a given program point. A variable is live if its value is reachable from the program point and may be used before being overwritten. Live variables guide register allocation (live variables cannot share a register) and dead-code elimination (assignments to non-live variables are removable).

## Explainer

From your work on dataflow analysis, you know how to propagate facts through a control flow graph by iterating over basic blocks until a fixed point is reached. Live variable analysis applies that same framework to answer one specific question: at any given point in the program, which variables might still be needed later? A variable is **live** at a program point if there exists some path from that point to a use of the variable along which the variable is not redefined. If no such path exists, the variable is **dead** — its current value will never be read again.

What makes liveness unusual among dataflow problems is that it flows backward. Most analyses you have seen propagate information forward, from definitions to uses. Liveness works in reverse: you start at the end of the program (or the exit of a function) and propagate information upward through the control flow graph. The **gen set** for a statement contains the variables it uses, and the **kill set** contains the variables it defines. At each program point, the live-out set is the union of the live-in sets of all successor blocks, and the live-in set is computed as (live-out minus kill) union gen. You iterate this backward pass until no sets change — the standard fixed-point approach from dataflow analysis, just running in the opposite direction.

The practical payoff of liveness information is direct. Consider register allocation: if two variables are both live at the same program point, they might both be needed simultaneously, so they cannot share a register. This creates an **interference graph** where each variable is a node and edges connect simultaneously live variables. Graph coloring on this interference graph is the foundation of modern register allocation. Without accurate liveness data, the allocator would either spill too many variables to memory (wasting performance) or incorrectly reuse a register while its value is still needed (producing wrong results).

Liveness also powers dead code elimination. If a statement assigns to a variable that is not live after that statement — meaning nothing downstream will ever read the assigned value — the entire assignment can be safely removed. This is surprisingly common after other optimizations have run. For example, inlining a function might introduce temporary variables that are used once and then overwritten; liveness analysis reveals them as dead, and the compiler strips them out. The beauty of liveness is its composability: it produces a simple, well-defined set at every program point that other compiler passes can query cheaply, making it one of the most reused analyses in a modern optimizing compiler.
