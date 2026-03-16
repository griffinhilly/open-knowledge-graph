---
id: nc-class-parallel-circuits
title: NC Class and Parallel Circuit Complexity
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: circuit-complexity
  type: hard
- id: time-complexity-classes-formal
  type: soft
tags:
- parallel-computation
- circuits
- depth-bounds
stage: advanced
status: draft
---

# NC Class and Parallel Circuit Complexity

## Core Idea
NC (Nick's Class) contains languages computable by circuits of polynomial size and logarithmic depth. These circuits model highly parallel computation: depth corresponds to parallel time while size represents total operations. NC ⊆ P, and whether NC = P remains open. NC-hierarchy captures degrees of parallelizability, with NC^1 (linear size, log depth) being particularly fundamental for understanding parallelism.

## Explainer

From your study of circuit complexity, you know that Boolean circuits measure two distinct resources: **size** (total gates, corresponding to work) and **depth** (longest path from input to output, corresponding to time if gates can compute in parallel). NC exploits this separation: it defines the class of problems solvable with polynomial total work but only logarithmic parallel time.

The key intuition is that depth measures how many sequential steps you need if you have unlimited processors. Consider adding two n-bit numbers: naively done left to right, you have n sequential carries — depth Θ(n). But with a carry-lookahead tree, you can compute carries in O(log n) depth using O(n) gates. This is why integer addition is in NC^1 (circuits of O(n) size and O(log n) depth). More generally, NC^i consists of problems solvable by polynomial-size circuits of depth O(log^i n). The full class NC = ∪_i NC^i is what you can solve in polylogarithmic parallel time.

NC ⊆ P follows directly: a polynomial-size, polylogarithmic-depth circuit can be evaluated in polynomial time sequentially (just evaluate gate by gate in topological order). The reverse containment NC = P is open — it asks whether every polynomial-time algorithm can be efficiently parallelized down to polylogarithmic depth. The intuition for why P ≠ NC is plausible: some problems seem inherently sequential, where each step depends critically on the previous result.

The NC hierarchy refines parallelizability: NC^1 captures the most aggressively parallelizable problems (formula evaluation, regular languages), while NC^2 captures linear algebra over finite fields (matrix multiplication). Between NC and P lies an important class called **P-complete**: problems that are in P but believed not to be in NC because they capture sequential computation. The canonical P-complete problem is circuit value problem (CVP) — evaluating a given circuit on a given input — with all the irony that the very model used to define NC turns out to characterize its complement.
