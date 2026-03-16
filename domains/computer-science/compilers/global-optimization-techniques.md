---
id: global-optimization-techniques
title: Global Optimization Techniques
domain: computer-science
course: compilers
prerequisites:
- id: use-definition-chains
  type: hard
- id: code-optimization
  type: hard
builds-toward:
- procedure-inlining-optimization
- array-subscript-optimization
tags:
- optimization
- global-opts
- dataflow
stage: advanced
status: draft
---

# Global Optimization Techniques

## Core Idea
Global optimizations operate across basic block boundaries using data-flow information. Common global optimizations include code hoisting, common subexpression elimination, and copy propagation. These optimizations are more powerful but more complex than local optimizations.

## How It's Best Learned
Implement global common subexpression elimination or code hoisting using reaching definitions and data-flow analysis.

## Explainer

From your study of code optimization, you know that local optimizations work within a single basic block — a straight-line sequence of instructions with one entry and one exit. These are safe and straightforward because control flow within a block is linear. But real programs branch, loop, and merge, meaning most optimization opportunities span multiple basic blocks. **Global optimization** extends optimization across an entire function's control flow graph, using the dataflow information from use-definition chains to determine what transformations are safe at each point in the program.

Consider **global common subexpression elimination** (GCSE). If the expression `a + b` is computed in block B1 and again in block B3, and neither `a` nor `b` is redefined on any path from B1 to B3, then the second computation is redundant. A local optimizer would miss this because the two computations are in different blocks. GCSE uses **available expressions analysis** — a forward dataflow problem that tracks which expressions have been computed and not subsequently invalidated at each program point. If `a + b` is available at the entry to B3, the compiler replaces the redundant computation with a reference to the previously computed value, saving an arithmetic operation on every execution of that path.

**Code hoisting** (also called loop-invariant code motion when applied to loops) moves computations to earlier points in the program where they dominate later uses. If a computation inside a loop produces the same result on every iteration because its operands are not modified within the loop, the compiler can hoist it above the loop header so it executes once instead of thousands of times. The safety check requires that the computation's operands have the same reaching definitions at the hoist point as they do at the original location — this is exactly the information that use-definition chains provide. **Copy propagation** is another global optimization: after an assignment `x = y`, every subsequent use of `x` (where no intervening redefinition of `x` or `y` occurs) can be replaced with `y`, potentially enabling further optimizations like dead code elimination when `x` is no longer used.

The challenge of global optimization is that safety requires conservative reasoning about all possible execution paths. If a value is available on one path to a block but not another, the compiler cannot assume it is available — it must account for the worst case. This is why dataflow analysis computes meet-over-all-paths solutions: the intersection (for available expressions) or union (for reaching definitions) of information along every path to a given point. The result is that global optimizations are always sound but sometimes miss opportunities that a more aggressive analysis (like path-sensitive or speculative optimization) could catch. Despite this conservatism, global optimizations typically yield significant performance improvements — often 10–30% — because redundant computations and loop-invariant operations are pervasive in real programs.
