---
id: data-dependence-analysis
title: Data Dependence Analysis
domain: computer-science
course: compilers
prerequisites:
- id: basic-block-analysis
  type: hard
- id: dataflow-analysis
  type: hard
builds-toward:
- use-definition-chains
- loop-detection-analysis
tags:
- analysis
- data-flow
- dependencies
stage: advanced
status: draft
---

# Data Dependence Analysis

## Core Idea
Data dependence analysis determines which instructions depend on results from earlier instructions. Dependencies include true dependencies (a use depends on a write), anti-dependencies (a write depends on an earlier read), and output dependencies. Understanding dependencies is essential for safe code motion and parallelization.

## How It's Best Learned
Compute data dependence sets for small programs and draw dependence graphs. Understand how dependences limit parallelization.

## Common Misconceptions
All dependencies must be respected (anti and output dependencies can often be eliminated through renaming). Dependence analysis only matters for parallelization (it affects all optimizations that move code).

## Explainer

From basic block analysis and dataflow analysis, you know how to trace values through a program's control flow graph. Data dependence analysis takes this further by asking a precise question: for any two instructions, does the order in which they execute matter? If instruction B reads a value that instruction A writes, then A must execute before B — reordering them would give B the wrong value. This relationship is called a **true dependence** (also called a flow dependence or read-after-write), and it represents a genuine constraint that no optimization can eliminate. If you compute `x = a + b` on line 3 and use `y = x * 2` on line 7, the multiplication truly depends on the addition.

Two other kinds of dependence are less fundamental but equally important to get right. An **anti-dependence** (write-after-read) occurs when instruction A reads a variable and later instruction B writes to it — B must not execute before A finishes reading the old value. An **output dependence** (write-after-write) occurs when two instructions write to the same variable — their order determines which value persists. Unlike true dependences, anti and output dependences are **name dependences**: they arise not from genuine data flow but from the reuse of variable names or storage locations. If you renamed the variable so that each write targets a distinct location, these dependences vanish. This insight is the basis of register renaming in hardware and SSA form in compilers.

The practical output of dependence analysis is a **dependence graph**, where nodes are instructions and directed edges represent dependences. An edge from A to B labeled with the dependence type means "A must execute before B." Any valid reordering of instructions must respect every edge in this graph — it must be a topological order. Instructions with no path between them in the dependence graph are independent and can safely execute in parallel or be reordered freely. This directly enables optimizations like instruction scheduling (reorder instructions to fill pipeline stalls), loop parallelization (execute independent iterations simultaneously), and code motion (move an instruction out of a loop if no dependence prevents it).

For loops, dependence analysis becomes especially powerful and subtle. A **loop-carried dependence** exists when an instruction in iteration i depends on a result from iteration i−1 (or earlier). The classic example is `a[i] = a[i-1] + 1` — each iteration reads the value written by the previous one, creating a chain that prevents parallel execution. In contrast, `a[i] = b[i] + 1` has no loop-carried dependence, so all iterations can run in parallel. Determining whether array accesses in a loop create dependences requires solving systems of integer constraints (like the GCD test or the Banerjee test), connecting dependence analysis to the integer arithmetic you encountered in earlier compiler topics.
