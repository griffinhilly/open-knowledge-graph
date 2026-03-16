---
id: ir-intermediate-representation-design
title: Intermediate Representation Design and Tradeoffs
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: compiler-phases-and-organization
  type: hard
tags:
- IR
- design
- architecture
stage: advanced
status: draft
---

# Intermediate Representation Design and Tradeoffs

## Core Idea
Choosing an IR shape profoundly affects compiler modularity and performance: high-level IRs (close to source syntax) simplify semantic analysis but complicate code generation; low-level IRs (close to machine code) simplify backend work but require careful lowering. The choice shapes the entire compiler architecture.

## Explainer

From your work on compiler phases and intermediate code representation, you know that a compiler does not translate source code directly into machine instructions. Instead, it lowers the program through one or more **intermediate representations** — internal data structures that sit between the source language and the target machine. The design question is not whether to use an IR, but which shape of IR best serves the compiler's goals, and how many levels of IR the compiler should maintain.

Think of IR design as choosing a language for the compiler to talk to itself. A **high-level IR** preserves source-language structure — loops, conditionals, typed variables, function calls — much like an abstract syntax tree with annotations. This makes it easy to perform type checking, inlining decisions, and source-level optimizations, but the IR is far from the machine and must eventually be "lowered" through multiple transformation passes. A **low-level IR**, by contrast, looks closer to assembly: explicit registers or virtual registers, flat control flow with branches, and simple three-address instructions. Low-level IRs simplify instruction selection and register allocation but lose the structural information that high-level optimizations need.

Most production compilers solve this tension by using **multiple IR levels**. LLVM, for instance, accepts high-level input from language frontends (Clang emits LLVM IR), performs optimization passes on its SSA-based mid-level IR, and then lowers to a machine-specific IR before final code emission. Each level of IR is designed for the transformations that happen at that stage. The high-level IR preserves semantic richness; the mid-level IR enables general-purpose optimization; the low-level IR enables target-specific tuning. This layered approach is what makes LLVM usable across dozens of source languages and target architectures — the IR boundaries define clean interfaces between compiler components.

The key tradeoffs to internalize are these: **expressiveness versus analyzability**. A tree-based IR is expressive and maps naturally to source constructs, but analyzing control flow across branches requires flattening it. A flat, three-address-code IR makes control flow explicit and is easy to analyze with dataflow techniques, but reconstructing high-level loop structure for vectorization requires extra analysis. **Graph-based IRs** like SSA (Static Single Assignment) form occupy a middle ground — they make data flow explicit through use-def chains while keeping control flow as a graph of basic blocks. SSA is dominant in modern compilers precisely because it balances these concerns, making many optimizations (constant propagation, dead code elimination, register allocation) both simpler to implement and more effective.

When evaluating an IR design, ask three questions: What transformations will this IR undergo? What information must be preserved versus what can be discarded? And how many lowering steps separate this IR from the final output? The answers determine whether you need a tree, a graph, a linear sequence, or some hybrid — and whether a single IR suffices or a multi-level pipeline is warranted.
