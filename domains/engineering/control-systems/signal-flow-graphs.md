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
stage: expert
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

## Questions

```yaml
- question: "A signal flow graph has three loops: L₁, L₂, and L₃. Loops L₁ and L₂ share a node; L₂ and L₃ share a node; but L₁ and L₃ share no nodes. How do L₁ and L₃ appear in the graph determinant Δ?"
  type: multiple-choice
  options:
    - "They appear as a sum: −(L₁ + L₃), added with a negative sign like all individual loops"
    - "They appear as a product: +L₁·L₃, added with a positive sign as a non-touching pair"
    - "They are ignored because they are not directly connected to each other"
    - "They appear only in the cofactor Δₖ for paths that touch L₂"
  answer: 1
  explanation: "In Δ = 1 − ΣLᵢ + ΣLᵢLⱼ − ···, pairs of non-touching loops enter as *products* with a positive sign. Since L₁ and L₃ share no nodes, they contribute the term +L₁·L₃. Individual loops contribute −ΣLᵢ; non-touching pairs contribute +ΣLᵢLⱼ; non-touching triples contribute −ΣLᵢLⱼLₖ; and so on in alternation. Option A is the most common misconception — students add rather than multiply non-touching loops. L₁ and L₂ touching (and L₂ and L₃ touching) means those pairs do NOT contribute product terms."

- question: "A simple negative feedback system has forward path gain G and feedback loop gain L₁ = −GH (negative sign from the summing junction). Applying Mason's formula, what is the transfer function?"
  type: multiple-choice
  options:
    - "T = G / (1 − GH)"
    - "T = G / (1 + GH)"
    - "T = GH / (1 + G)"
    - "T = G·GH"
  answer: 1
  explanation: "Applying Mason's formula: Δ = 1 − L₁ = 1 − (−GH) = 1 + GH. The single forward path P₁ = G touches the loop (they share nodes), so the cofactor Δ₁ = 1 (no untouched loops remain). Therefore T = P₁Δ₁/Δ = G·1/(1+GH) = G/(1+GH). This recovers the familiar negative feedback formula directly. If the feedback were positive (L₁ = +GH), Δ = 1−GH and T = G/(1−GH). The sign of the loop gain is critical and must be computed carefully."

- question: "If all loops in a signal flow graph touch a particular forward path k, then the cofactor Δₖ equals 1."
  type: true-false
  answer: true
  explanation: "The cofactor Δₖ is computed by removing from Δ all loops (and their non-touching combinations) that touch forward path k. If every loop touches path k, nothing remains after deletion: Δₖ = 1. This is why the simple feedback system T = G/(1+GH) has Δ₁ = 1 — the single loop touches the single forward path, so no independent loop dynamics remain. When some loops are untouched by path k, Δₖ captures those independent dynamics as a sub-determinant."

- question: "Different valid signal flow graph representations of the same linear system can yield different transfer functions when Mason's gain formula is correctly applied."
  type: true-false
  answer: false
  explanation: "While the same system can be drawn as multiple different SFGs (different node placement, different intermediate signals), they all encode the same set of linear equations. Mason's formula, when correctly applied to any valid representation, extracts the same input-output transfer function. If two correct SFGs of the same system give different transfer functions, there is a bookkeeping error — a missed loop, wrong loop gain, or incorrect non-touching pair identification. This consistency is why comparing against block diagram reduction serves as a useful check."

- question: "What is the graph determinant Δ in Mason's formula, and why do non-touching loops contribute as products rather than sums?"
  type: short-answer
  answer: "Δ = 1 − ΣLᵢ + ΣLᵢLⱼ − ΣLᵢLⱼLₖ + ···, where sums alternate in sign over all loops, all pairs of non-touching loops, all non-touching triples, etc. Non-touching loops contribute as products because their gains multiply independently — two loops sharing no nodes create compounded feedback that is neither captured by summing them nor by treating them as a single loop. The product term ΣLᵢLⱼ represents second-order interactions between independent feedback paths, and the alternating signs follow an inclusion-exclusion structure to prevent double-counting."
  explanation: "Non-touching loops are independent subsystems, and their combined gain contribution to the denominator is multiplicative, analogous to how independent probabilities multiply. Summing them would undercount the feedback from independent loops operating simultaneously; the correct accounting requires their product."
```

## Explainer

A **signal flow graph** (SFG) is a directed graph that encodes the same information as a block diagram, but in a form that is easier to construct directly from a set of simultaneous linear equations. Each **node** represents a signal variable, and each directed **branch** carries a **gain** — the transfer function scaling one signal into another. Where a block diagram requires reduction rules applied to boxes and summing junctions, an SFG captures everything as a network of weighted edges, making the mathematical structure transparent.

The power of SFGs comes from **Mason's gain formula**, which computes the transfer function T = (Σ Pₖ Δₖ) / Δ in one pass without algebraic reduction. Before applying it, you must enumerate three things. First, identify every **forward path** — any path from input node to output node that visits no node more than once — and compute each path's gain Pₖ by multiplying its branch gains. Second, identify every **loop** — any closed path visiting no node more than once — and compute each loop gain Lᵢ as the product of the branch gains around that loop. Third, identify all sets of **non-touching loops** (loops that share no nodes), because these contribute product terms to the **graph determinant** Δ = 1 − ΣLᵢ + ΣLᵢLⱼ − ΣLᵢLⱼLₖ + ···, where the sums alternate in sign and run over all loops, all pairs of non-touching loops, all triples, and so on.

The term Δₖ, called the **cofactor** for forward path k, is computed by deleting from Δ all loops that touch path k. Intuitively, Δₖ captures the "independent dynamics" — the loops that are unaffected by and do not interact with path k. If all loops touch path k, then Δₖ = 1. This is why simple single-loop feedback systems yield the familiar T = G/(1 + GH) directly from Mason's formula: one forward path P₁ = G, one loop L₁ = −GH, Δ = 1 − (−GH) = 1 + GH, and Δ₁ = 1 since the loop touches the forward path.

The most important skill in applying Mason's formula is systematic bookkeeping. For complex multi-loop systems, missing a loop or a non-touching pair is the most common error. A structured approach helps: list all paths of increasing length from input to output, then list all loops, then check every pair of loops for node overlap to determine which are non-touching. Once you have verified your inventory, the arithmetic is straightforward. Comparing the SFG result against an independent block-diagram reduction on the same system builds confidence and catches errors — if the two methods disagree, the bookkeeping has a mistake.
