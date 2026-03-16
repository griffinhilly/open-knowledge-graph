---
id: procedure-inlining-optimization
title: Procedure Inlining Optimization
domain: computer-science
course: compilers
prerequisites:
- id: global-optimization-techniques
  type: hard
- id: control-flow-graphs
  type: hard
builds-toward:
- instruction-selection-techniques
tags:
- optimization
- inlining
- procedure-calls
stage: advanced
status: draft
---

# Procedure Inlining Optimization

## Core Idea
Procedure inlining replaces a function call with a copy of the function body, eliminating call overhead and enabling further optimizations. Inlining trades code size for speed and must be controlled via heuristics to avoid code bloat.

## How It's Best Learned
Implement function inlining with a simple heuristic (inline if function is small). Measure code size and speed impacts.

## Explainer

From your work on global optimization and control flow graphs, you know that many optimizations operate across basic blocks and depend on seeing enough code to find redundancies. **Procedure inlining** dramatically expands the optimizer's view by replacing a function call with a copy of the called function's body, spliced directly into the caller. Instead of a call instruction that jumps away and returns, the code just continues straight through, as if the function's logic had been written inline at the call site.

The immediate benefit is eliminating call overhead — saving the cost of pushing arguments onto the stack, jumping to the callee, saving and restoring registers, and returning. But this direct saving is often the smaller win. The larger benefit is that inlining exposes the function body to the caller's optimization context. Once inlined, constant arguments can be propagated into the function body, dead branches can be eliminated, and common subexpressions between the caller and the inlined code become visible. Consider a function `square(x)` that returns `x * x`. Called as `square(5)`, inlining produces `5 * 5`, which constant folding reduces to `25` — a chain of optimizations that would be impossible across a function call boundary.

The fundamental tension in inlining is the **code size tradeoff**. Every inlining decision copies the function body, increasing the total code size. If a function is called from 50 different sites and each call is inlined, the compiled binary contains 50 copies of that code. Larger code means more instruction cache pressure, which can actually slow down execution — the opposite of the intended effect. Compilers therefore use heuristics to decide what to inline: small functions (a few statements) are almost always inlined, functions called from a single site are inlined regardless of size (since no duplication occurs), and hot call sites identified by profiling data get priority. Recursive functions generally cannot be inlined (or are inlined only to a fixed depth), and functions with complex control flow may offer diminishing returns.

The implementation mechanics matter too. When inlining into a control flow graph, the compiler must rename local variables to avoid name collisions, map the caller's arguments onto the callee's parameters, and replace return statements with jumps to a continuation point in the caller. If the inlined function has multiple return paths, these must be merged. The compiler also needs to handle interactions with other optimizations — inlining can change loop structures, affect alias analysis, and create new opportunities for constant propagation that require additional optimization passes to exploit. This is why inlining is typically performed early in the optimization pipeline, so that downstream passes can capitalize on the newly exposed code.
