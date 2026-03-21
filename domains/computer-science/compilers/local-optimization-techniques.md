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

## Questions

```yaml
- question: "A compiler encounters this sequence in a single basic block: `a = 4 * 3; b = a + 0; c = b * 1;`. After applying constant folding, constant propagation, and algebraic simplification, what does the block reduce to (assuming c is used later)?"
  type: multiple-choice
  options:
    - "`a = 12; b = 12; c = 12;`"
    - "`a = 12; b = a; c = b;`"
    - "`c = 12;`"
    - "`a = 4 * 3; b = a; c = b;`"
  answer: 2
  explanation: "Constant folding reduces `4 * 3` to `12`, giving `a = 12`. Constant propagation substitutes a = 12 into `b = a + 0`, which algebraic simplification reduces to `b = 12` (since x + 0 = x, then constant folding gives 12). Constant propagation then substitutes b = 12 into `c = b * 1`, which algebraic simplification reduces to `c = 12` (since x * 1 = x). The intermediate assignments to `a` and `b` are now dead code — their values are never used by any later instruction (c = 12 doesn't reference them). Dead code elimination removes them, leaving only `c = 12`. This illustrates the cascade: each optimization creates opportunities for the next."

- question: "Variable x is assigned the value 7 at the end of basic block B1. Basic block B2 immediately follows and begins with `y = x * 2`. Can the local optimizer for B2 apply constant propagation to substitute x = 7 and fold this to `y = 14`?"
  type: multiple-choice
  options:
    - "Yes — if B1 always precedes B2, the constant value of x carries over automatically"
    - "No — local optimization is confined to a single basic block; the optimizer for B2 cannot access the constant value established in B1 without global dataflow analysis"
    - "Yes — constant propagation is a global property of variables, not a property of blocks"
    - "No — because x could be a pointer and dereferencing pointers prevents constant folding"
  answer: 1
  explanation: "This is the fundamental limitation of local optimization. The local optimizer for B2 can only analyze instructions within B2; it has no mechanism to observe that x = 7 was established in B1. From B2's perspective, x is an unknown variable. Crossing basic block boundaries requires global dataflow analysis — specifically, reaching definitions analysis — which is what global optimization techniques provide. Option A represents the common misconception: even if B1 always precedes B2 in the control flow graph, local analysis cannot exploit this without global information."

- question: "Local optimizations like constant folding and dead code elimination are called 'local' because they only work on variables with local (non-global) scope."
  type: true-false
  answer: false
  explanation: "The term 'local' refers to the scope of analysis: a basic block, not the scope of variables. Local optimizations operate within a single basic block — a straight-line sequence of instructions with one entry and one exit. The variable itself can have any scope; what matters is whether the optimization needs information from outside the block. Variables with global scope can still be constant-folded or dead-code-eliminated within a block, as long as the analysis stays within that block's boundaries."

- question: "Constant propagation and constant folding tend to produce larger improvements than either technique applied alone, because successfully applying one creates new opportunities for the other."
  type: true-false
  answer: true
  explanation: "This cascading effect is a key property of local optimizations. Constant propagation substitutes known constant values into expressions, which may then have all-constant operands — creating new opportunities for constant folding to compute them at compile time. The newly folded constants may eliminate all uses of intermediate variables, creating opportunities for dead code elimination, which shortens the block and may expose further optimization opportunities. The optimizations are most effective when applied together in a pass-by-pass loop until no further changes occur."

- question: "Why is the single-basic-block scope of local optimizations both their greatest strength and their fundamental limitation?"
  type: short-answer
  answer: "Within a basic block, control flow is simple: instructions execute in sequence with no branches, so the compiler can safely reason about every instruction's effect. This simplicity makes local optimizations easy to implement, provably safe, and applicable to every basic block in the program. The limitation is the inverse: any optimization requiring knowledge of values or control flow from outside the block is impossible locally. A constant defined in one block and used in another is invisible to local analysis. This motivates global optimizations, which use dataflow analysis to propagate information across blocks — but these are more complex and expensive to implement."
  explanation: "The same property — guaranteed sequential execution — that makes local analysis tractable also limits it. Real programs contain variables that live across block boundaries, loop induction variables, and function calls that local analysis cannot reason about. Global optimization techniques (available expressions, reaching definitions, live variable analysis) extend the same basic ideas to entire control-flow graphs, but they depend on the local optimizations as a foundation — cleaning up the obvious inefficiencies before the more expensive global passes run."
```

## Explainer

You already know that a basic block is a straight-line sequence of instructions with one entry and one exit — no branches in the middle, no jumps into the middle. This property is what makes local optimizations so tractable: because execution flows strictly top to bottom through a basic block, you can reason about every instruction's effect without worrying about alternate paths. Local optimizations exploit this simplicity to clean up inefficiencies that arise naturally from naive code generation.

The most fundamental local optimization is **constant folding**: if both operands of an arithmetic instruction are constants, the compiler computes the result at compile time and replaces the instruction with an assignment. For example, `t1 = 3 * 4` becomes `t1 = 12`. Closely related is **constant propagation**, which tracks when a variable holds a known constant and substitutes that constant into later uses. If `x = 5` and later `y = x + 2`, the compiler can rewrite the second instruction as `y = 5 + 2`, which constant folding then reduces to `y = 7`. These two optimizations feed each other in a cascade — one substitution enables the next simplification.

**Algebraic simplification** applies identities from arithmetic to eliminate redundant work: `x * 1` becomes `x`, `x + 0` becomes `x`, `x * 2` becomes `x + x` or a left shift. These transformations seem trivial individually, but naive code generators produce exactly these patterns, especially when expanding high-level constructs like array indexing or structure field access. **Dead code elimination** then removes instructions whose results are never used by any subsequent instruction in the block. If constant propagation replaces every use of `t1`, the instruction that computed `t1` is now dead and can be deleted, shrinking the block further.

The key insight about local optimizations is that they are cheap, safe, and composable. Each one is simple enough to implement in a single pass over the basic block, and applying them in combination often produces cascading improvements — constant propagation enables constant folding, which enables dead code elimination, which shortens the block for the next pass. However, their scope is inherently limited to one basic block. A variable defined in one block and used in another is invisible to local analysis. This limitation motivates the global optimization techniques that extend the same ideas across entire control-flow graphs using dataflow analysis, but the local versions remain the essential building blocks that every compiler implements first.
