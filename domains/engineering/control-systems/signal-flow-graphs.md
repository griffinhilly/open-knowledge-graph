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
status: draft
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
