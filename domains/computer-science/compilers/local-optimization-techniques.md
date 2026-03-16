---
id: local-optimization-techniques
title: Local Optimization Techniques
domain: computer-science
course: compilers
prerequisites:
- id: basic-block-analysis
  type: hard
- id: code-optimization
  type: hard
builds-toward:
- global-optimization-techniques
tags:
- optimization
- local-opts
- peephole
stage: advanced
status: draft
---

# Local Optimization Techniques

## Core Idea
Local optimizations operate within a single basic block and include constant folding, constant propagation, dead code elimination, and algebraic simplification. These are the easiest optimizations to implement but have limited scope, serving as foundation for sophisticated global optimizations.

## How It's Best Learned
Implement several local optimizations and apply them to basic blocks. Measure improvements in code quality.

## Explainer

You already know that a basic block is a straight-line sequence of instructions with one entry and one exit — no branches in the middle, no jumps into the middle. This property is what makes local optimizations so tractable: because execution flows strictly top to bottom through a basic block, you can reason about every instruction's effect without worrying about alternate paths. Local optimizations exploit this simplicity to clean up inefficiencies that arise naturally from naive code generation.

The most fundamental local optimization is **constant folding**: if both operands of an arithmetic instruction are constants, the compiler computes the result at compile time and replaces the instruction with an assignment. For example, `t1 = 3 * 4` becomes `t1 = 12`. Closely related is **constant propagation**, which tracks when a variable holds a known constant and substitutes that constant into later uses. If `x = 5` and later `y = x + 2`, the compiler can rewrite the second instruction as `y = 5 + 2`, which constant folding then reduces to `y = 7`. These two optimizations feed each other in a cascade — one substitution enables the next simplification.

**Algebraic simplification** applies identities from arithmetic to eliminate redundant work: `x * 1` becomes `x`, `x + 0` becomes `x`, `x * 2` becomes `x + x` or a left shift. These transformations seem trivial individually, but naive code generators produce exactly these patterns, especially when expanding high-level constructs like array indexing or structure field access. **Dead code elimination** then removes instructions whose results are never used by any subsequent instruction in the block. If constant propagation replaces every use of `t1`, the instruction that computed `t1` is now dead and can be deleted, shrinking the block further.

The key insight about local optimizations is that they are cheap, safe, and composable. Each one is simple enough to implement in a single pass over the basic block, and applying them in combination often produces cascading improvements — constant propagation enables constant folding, which enables dead code elimination, which shortens the block for the next pass. However, their scope is inherently limited to one basic block. A variable defined in one block and used in another is invisible to local analysis. This limitation motivates the global optimization techniques that extend the same ideas across entire control-flow graphs using dataflow analysis, but the local versions remain the essential building blocks that every compiler implements first.
