---
id: loop-unrolling-optimization
title: Loop Unrolling
domain: computer-science
course: compilers
prerequisites:
- id: code-optimization
  type: hard
- id: control-flow-graphs
  type: hard
builds-toward:
- vectorization-and-simd
tags:
- optimization
- loops
- performance
stage: advanced
status: draft
---

# Loop Unrolling

## Core Idea
Loop unrolling duplicates the loop body multiple times per iteration, reducing branch overhead and enabling better instruction-level parallelism. It trades code size for speed and requires bounds checking to handle partial iterations, with heuristics to prevent code explosion.

## How It's Best Learned
Manually unroll a simple loop (e.g., summing an array), measure branch counts, and observe how unrolling factors affect the instruction mix.

## Explainer

Consider a loop that sums 1000 array elements. Each iteration performs one addition and one branch back to the loop header — so the processor executes 1000 branches, each requiring a comparison, a conditional jump, and potentially a pipeline flush if the branch predictor guesses wrong. **Loop unrolling** reduces this overhead by replicating the loop body multiple times within a single iteration. If you unroll by a factor of 4, each iteration now performs four additions before branching, cutting the branch count from 1000 to 250.

The benefit goes beyond just eliminating branches. From your work on control flow graphs and code optimization, you know that the compiler analyzes basic blocks — straight-line sequences of instructions with no branches. A loop body that executes one operation is a tiny basic block with limited optimization opportunity. Unrolling the body creates a larger basic block, giving the optimizer more instructions to schedule. It can now interleave independent operations, hide memory latency by issuing loads early, and exploit **instruction-level parallelism** — keeping multiple functional units in the processor busy simultaneously.

Unrolling is not free. The duplicated code increases the binary size, which can cause instruction cache pressure. If the loop body is already large, unrolling it further may evict other useful code from the cache, creating a net slowdown. Compilers use heuristics to choose an unrolling factor that balances the branch reduction and scheduling benefits against code bloat. Typical factors are 2, 4, or 8 for tight inner loops, with larger factors reserved for very small loop bodies.

There is also a bookkeeping cost: if the trip count is not evenly divisible by the unrolling factor, the compiler must generate a **remainder loop** (or **epilogue**) to handle the leftover iterations. For example, unrolling by 4 on a loop of 1000 iterations works cleanly, but a loop of 1003 iterations needs an extra pass of 3 single iterations. The compiler inserts this cleanup code automatically, but it adds complexity to the generated output. Despite these tradeoffs, loop unrolling is one of the most consistently profitable optimizations in practice and serves as a foundation for more advanced transformations like vectorization and software pipelining.
