---
id: static-single-assignment-form
title: Static Single Assignment (SSA) Form
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: control-flow-graphs
  type: hard
builds-toward:
- dataflow-analysis
- code-optimization
tags:
- ssa
- ir-form
- dataflow
stage: advanced
status: draft
---

# Static Single Assignment (SSA) Form

## Core Idea
SSA form ensures each variable is assigned exactly once. Use-def chains are explicit: each use links to a unique definition. Phi (φ) functions merge definitions at control flow joins. SSA simplifies dataflow analysis, enables sophisticated optimizations, and makes dependencies explicit. Most modern compilers (LLVM, GCC, Java JIT) use SSA as their primary IR.

## Explainer

In a conventional intermediate representation, a variable like `x` can be assigned multiple times across different points in the program. This creates a fundamental problem for analysis: when you see a use of `x`, which assignment does it refer to? Answering this requires reaching definitions analysis, which tracks all possible definitions flowing to each use. **Static Single Assignment (SSA) form** eliminates this ambiguity by renaming variables so that each assignment targets a unique name. If the original code assigns to `x` three times, SSA renames them to `x₁`, `x₂`, and `x₃`. Every use then refers to exactly one definition — the mapping is immediate and unambiguous.

The complication arises at **control flow joins** — points where two or more paths merge. Consider an if-else: one branch assigns `x₁ = 5`, the other assigns `x₂ = 10`, and then the paths converge. After the join, which version of `x` should subsequent code use? SSA introduces **phi (φ) functions** to handle this. A phi function `x₃ = φ(x₁, x₂)` is placed at the join point, meaning "x₃ takes the value x₁ if execution came from the left branch, or x₂ if it came from the right." Phi functions are not real instructions — they do not execute at runtime — but they maintain the SSA invariant that every use has exactly one reaching definition. The algorithm for placing phi functions uses the **dominance frontier**: a phi for variable `x` is needed at every block where the definition of `x` in one predecessor does not dominate all paths to that block.

The payoff of SSA is enormous for optimization. Because each name has exactly one definition, **use-def chains** are trivially available: follow the name back to its unique assignment. This makes constant propagation straightforward — if `x₃ = 5`, every use of `x₃` can be replaced with `5`, no reaching-definitions iteration required. **Dead code elimination** becomes simple: if no use references `x₃`, delete its definition. **Common subexpression elimination** and **strength reduction** also benefit because the explicit naming makes redundant computations immediately visible.

Converting to SSA and back is well-understood. Construction involves renaming variables during a traversal of the dominator tree, inserting phi functions at dominance frontiers. Converting out of SSA (for final code generation) replaces phi functions with copy instructions along the incoming edges — `x₃ = φ(x₁, x₂)` becomes a copy `x₃ = x₁` at the end of the left predecessor and `x₃ = x₂` at the end of the right predecessor. Register allocation then coalesces these copies where possible. LLVM's IR is natively in SSA form, which is why its optimization passes are so clean and composable — each pass can rely on the single-assignment property without rebuilding analysis information from scratch.
