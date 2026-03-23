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
status: validated
---

# Static Single Assignment (SSA) Form

## Core Idea
SSA form ensures each variable is assigned exactly once. Use-def chains are explicit: each use links to a unique definition. Phi (φ) functions merge definitions at control flow joins. SSA simplifies dataflow analysis, enables sophisticated optimizations, and makes dependencies explicit. Most modern compilers (LLVM, GCC, Java JIT) use SSA as their primary IR.

## Questions

```yaml
- question: "Why does constant propagation become dramatically simpler when the IR is in SSA form?"
  type: multiple-choice
  options:
    - "SSA restricts programs to integer types, so all values are known statically at compile time"
    - "Each use has exactly one reaching definition, so if x₃ = 5, every use of x₃ can immediately be replaced with 5 without any iterative dataflow analysis"
    - "Phi functions pre-compute all possible values at control flow joins, making constants visible in a single pass"
    - "SSA eliminates all conditional branches, so values are always statically determined"
  answer: 1
  explanation: "In conventional IR, determining which definition reaches a given use requires reaching-definitions dataflow analysis — an iterative algorithm that propagates sets of definitions through the control flow graph. In SSA, this is unnecessary: each variable name uniquely identifies its one and only definition. If x₃ = 5, every use of x₃ is definitively reached by that one assignment. Constant propagation reduces to a single lookup rather than a fixpoint computation. This is the core payoff of the SSA invariant — use-def chains are free."

- question: "A program contains: if (cond) { x = 1; } else { x = 2; } followed by: y = x + 3. After converting to SSA form, what appears at the join point after the if-else?"
  type: multiple-choice
  options:
    - "Two separate assignments x = 1 and x = 2 are duplicated at the join point and resolved by runtime branching"
    - "A phi function x₃ = φ(x₁, x₂) is placed at the join point, which resolves to x₁ or x₂ depending on which branch was taken"
    - "A merged assignment x₃ = (x₁ + x₂) / 2 representing the average of both branches"
    - "The variable x is left undefined at the join point; SSA requires the programmer to initialize it before use"
  answer: 1
  explanation: "Control flow joins are exactly where SSA's phi functions are needed. After the if-branch assigns x₁ = 1 and the else-branch assigns x₂ = 2, subsequent code needs a way to refer to 'the value of x, whichever branch was taken.' The phi function x₃ = φ(x₁, x₂) is SSA's solution: it is a definitional device that takes the value of whichever argument corresponds to the actual execution path. The subsequent use y = x₃ + 3 then has exactly one reaching definition. Phi functions are not runtime instructions — they encode the join semantics in the IR structure."

- question: "Phi functions in SSA form are real instructions that execute at runtime to select between multiple possible values."
  type: true-false
  answer: false
  explanation: "Phi functions are a conceptual device in the IR — they exist only during compilation, not at runtime. During final code generation, SSA destruction replaces each phi function with copy instructions inserted at the ends of predecessor blocks: x₃ = φ(x₁, x₂) becomes 'copy x₁ into x₃' at the end of the left predecessor and 'copy x₂ into x₃' at the end of the right predecessor. Register allocation then coalesces these copies where possible. Treating phi functions as runtime instructions is a misconception; they are analysis artifacts that make the dataflow structure explicit."

- question: "In SSA form, any given variable name may appear on the left-hand side of at most one assignment anywhere in the entire function."
  type: true-false
  answer: true
  explanation: "This is the defining invariant of SSA — 'static single assignment.' Each original variable x is renamed into a family of versioned names x₁, x₂, x₃, ... where each version is assigned exactly once. A definition site for x₃ appears exactly once in the program; every use of x₃ refers to that one definition. This unique-definition property is what makes use-def chains trivially available (follow the name back to its one assignment site) and what enables the optimization benefits."

- question: "Explain why phi functions are necessary in SSA form and how the dominance frontier determines where they are placed."
  type: short-answer
  answer: "Phi functions are needed wherever two control flow paths merge and bring different versions of the same variable. Without them, a join point would have ambiguous reaching definitions — violating SSA's invariant. A phi function x₃ = φ(x₁, x₂) resolves the ambiguity by explicitly merging the two versions. Phi functions are placed at dominance frontiers: a block B is in the dominance frontier of block D if D dominates a predecessor of B but does not strictly dominate B itself. Intuitively, the dominance frontier of a definition site is the set of blocks where that definition first 'competes' with other reaching definitions — precisely where merging is needed."
  explanation: "The dominance frontier placement ensures phi functions are inserted neither too early (wasting memory and computation) nor too late (leaving ambiguous uses). A definition at block D dominates all blocks it reaches exclusively; the moment another path brings a different definition to the same block, a phi function is required there. Algorithms like Cytron's efficient SSA construction algorithm use the dominance tree and iterated dominance frontiers to insert exactly the right phi functions — no more, no less."
```

## Explainer

In a conventional intermediate representation, a variable like `x` can be assigned multiple times across different points in the program. This creates a fundamental problem for analysis: when you see a use of `x`, which assignment does it refer to? Answering this requires reaching definitions analysis, which tracks all possible definitions flowing to each use. **Static Single Assignment (SSA) form** eliminates this ambiguity by renaming variables so that each assignment targets a unique name. If the original code assigns to `x` three times, SSA renames them to `x₁`, `x₂`, and `x₃`. Every use then refers to exactly one definition — the mapping is immediate and unambiguous.

The complication arises at **control flow joins** — points where two or more paths merge. Consider an if-else: one branch assigns `x₁ = 5`, the other assigns `x₂ = 10`, and then the paths converge. After the join, which version of `x` should subsequent code use? SSA introduces **phi (φ) functions** to handle this. A phi function `x₃ = φ(x₁, x₂)` is placed at the join point, meaning "x₃ takes the value x₁ if execution came from the left branch, or x₂ if it came from the right." Phi functions are not real instructions — they do not execute at runtime — but they maintain the SSA invariant that every use has exactly one reaching definition. The algorithm for placing phi functions uses the **dominance frontier**: a phi for variable `x` is needed at every block where the definition of `x` in one predecessor does not dominate all paths to that block.

The payoff of SSA is enormous for optimization. Because each name has exactly one definition, **use-def chains** are trivially available: follow the name back to its unique assignment. This makes constant propagation straightforward — if `x₃ = 5`, every use of `x₃` can be replaced with `5`, no reaching-definitions iteration required. **Dead code elimination** becomes simple: if no use references `x₃`, delete its definition. **Common subexpression elimination** and **strength reduction** also benefit because the explicit naming makes redundant computations immediately visible.

Converting to SSA and back is well-understood. Construction involves renaming variables during a traversal of the dominator tree, inserting phi functions at dominance frontiers. Converting out of SSA (for final code generation) replaces phi functions with copy instructions along the incoming edges — `x₃ = φ(x₁, x₂)` becomes a copy `x₃ = x₁` at the end of the left predecessor and `x₃ = x₂` at the end of the right predecessor. Register allocation then coalesces these copies where possible. LLVM's IR is natively in SSA form, which is why its optimization passes are so clean and composable — each pass can rely on the single-assignment property without rebuilding analysis information from scratch.
