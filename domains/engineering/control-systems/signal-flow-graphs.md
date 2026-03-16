---
id: signal-flow-graphs
title: Signal Flow Graphs and Mason's Gain Formula
domain: engineering
course: control-systems
prerequisites:
- id: block-diagram-algebra
  type: soft
- id: transfer-functions-control
  type: hard
tags:
- signal-flow-graph
- mason
- gain-formula
- forward-paths
- loop-gains
stage: advanced
status: validated
---

# Signal Flow Graphs and Mason's Gain Formula

## Core Idea
Signal flow graphs (SFGs) represent systems as directed graphs where nodes are signals and edges carry gain values (transfer functions). Mason's gain formula provides a systematic method for computing the overall transfer function: T = (Σ Pₖ Δₖ) / Δ, where Pₖ are forward-path gains, Δ is the graph determinant accounting for all loops and their non-touching combinations, and Δₖ is the determinant of the subgraph not touching path k. SFGs are mathematically equivalent to block diagrams but are often easier to construct directly from system equations and avoid the need for sequential reduction. They are especially useful for complex multi-loop systems.

## How It's Best Learned
Practice identifying all forward paths and loops systematically before applying Mason's formula — missing a loop is the most common error. Verify results against block diagram reduction on the same system to build confidence.

## Common Misconceptions
- Non-touching loops in the determinant Δ enter as products of their gains, not sums — the sign convention (alternating +/−) must be tracked carefully.
- Mason's formula applies to linear flow graphs only; nonlinear interconnections cannot be handled this way.
- The same system can be drawn as multiple different SFGs; all yield the same transfer function when Mason's formula is correctly applied.

## Explainer

A **signal flow graph** (SFG) is a directed graph that encodes the same information as a block diagram, but in a form that is easier to construct directly from a set of simultaneous linear equations. Each **node** represents a signal variable, and each directed **branch** carries a **gain** — the transfer function scaling one signal into another. Where a block diagram requires reduction rules applied to boxes and summing junctions, an SFG captures everything as a network of weighted edges, making the mathematical structure transparent.

The power of SFGs comes from **Mason's gain formula**, which computes the transfer function T = (Σ Pₖ Δₖ) / Δ in one pass without algebraic reduction. Before applying it, you must enumerate three things. First, identify every **forward path** — any path from input node to output node that visits no node more than once — and compute each path's gain Pₖ by multiplying its branch gains. Second, identify every **loop** — any closed path visiting no node more than once — and compute each loop gain Lᵢ as the product of the branch gains around that loop. Third, identify all sets of **non-touching loops** (loops that share no nodes), because these contribute product terms to the **graph determinant** Δ = 1 − ΣLᵢ + ΣLᵢLⱼ − ΣLᵢLⱼLₖ + ···, where the sums alternate in sign and run over all loops, all pairs of non-touching loops, all triples, and so on.

The term Δₖ, called the **cofactor** for forward path k, is computed by deleting from Δ all loops that touch path k. Intuitively, Δₖ captures the "independent dynamics" — the loops that are unaffected by and do not interact with path k. If all loops touch path k, then Δₖ = 1. This is why simple single-loop feedback systems yield the familiar T = G/(1 + GH) directly from Mason's formula: one forward path P₁ = G, one loop L₁ = −GH, Δ = 1 − (−GH) = 1 + GH, and Δ₁ = 1 since the loop touches the forward path.

The most important skill in applying Mason's formula is systematic bookkeeping. For complex multi-loop systems, missing a loop or a non-touching pair is the most common error. A structured approach helps: list all paths of increasing length from input to output, then list all loops, then check every pair of loops for node overlap to determine which are non-touching. Once you have verified your inventory, the arithmetic is straightforward. Comparing the SFG result against an independent block-diagram reduction on the same system builds confidence and catches errors — if the two methods disagree, the bookkeeping has a mistake.
