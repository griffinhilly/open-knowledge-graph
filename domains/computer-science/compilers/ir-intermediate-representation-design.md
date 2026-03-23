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
status: validated
---

# Intermediate Representation Design and Tradeoffs

## Core Idea
Choosing an IR shape profoundly affects compiler modularity and performance: high-level IRs (close to source syntax) simplify semantic analysis but complicate code generation; low-level IRs (close to machine code) simplify backend work but require careful lowering. The choice shapes the entire compiler architecture.

## Questions

```yaml
- question: "A compiler team is implementing a loop vectorization pass and must choose between a tree-based high-level IR and a flat three-address-code IR. Which is better suited for this pass, and why?"
  type: multiple-choice
  options:
    - "Flat three-address-code, because its linear structure makes all instructions directly accessible without recursive traversal"
    - "Tree-based IR, because loop constructs (loop body, induction variables, iteration bounds) are preserved naturally, making vectorizable loops easier to identify without extra analysis"
    - "Either works equally well — vectorization depends only on the target architecture, not the IR structure"
    - "SSA form, because SSA automatically eliminates loop-carried dependencies that prevent vectorization"
  answer: 1
  explanation: "Loop vectorization requires identifying high-level loop structures — the body, induction variables, and trip count — that are naturally preserved in a tree-based or high-level IR. In flat three-address code, loop structure has been linearized into branches and jumps; recovering it requires additional loop detection and induction variable analysis passes. This is the core tradeoff: high-level IRs simplify source-level optimizations that depend on structural information, while low-level IRs simplify backend tasks. SSA helps with data-flow but does not inherently preserve loop structure."

- question: "What is the key optimization advantage of SSA (Static Single Assignment) form over ordinary three-address code?"
  type: multiple-choice
  options:
    - "SSA uses fewer total instructions, reducing compilation time"
    - "SSA makes data-flow relationships explicit through use-def chains, simplifying analyses like constant propagation and dead code elimination without requiring separate reaching-definitions computation"
    - "SSA eliminates all phi functions at control-flow join points, making control flow analysis trivial"
    - "SSA is a higher-level IR than three-address code and therefore preserves more source-language structure"
  answer: 1
  explanation: "In SSA form, every variable is defined exactly once, so each use unambiguously refers to a single definition. This makes use-def chains direct and explicit — no dataflow analysis is needed to determine what value a variable holds at a given point. Optimizations like constant propagation, dead code elimination, and value numbering become dramatically simpler. SSA introduces phi functions (not eliminates them — option C is backwards) at join points to merge definitions from different control-flow paths. SSA is a property of assignment structure, not IR level; it can be applied to any flat IR (option D is incorrect)."

- question: "Using multiple IR levels in a compiler (e.g., high-level frontend IR → mid-level optimizer IR → machine IR) always adds unnecessary complexity, since each lowering step is a potential source of bugs."
  type: true-false
  answer: false
  explanation: "Multiple IR levels allow each compiler phase to work with an IR tailored to its tasks. The frontend IR preserves semantic richness for type checking and high-level optimizations; the mid-level IR enables target-independent optimization passes; the machine IR enables target-specific instruction selection and register allocation. This creates clean boundaries between compiler components, making the compiler modular — language frontends and machine backends can be developed independently. The complexity cost is real but the benefit — modularity and reuse across languages and targets — is why LLVM, GCC, and most production compilers use this approach."

- question: "A high-level IR that preserves source-language structure (loops, typed variables, function calls) is better suited for register allocation than a low-level IR close to machine code."
  type: true-false
  answer: false
  explanation: "Register allocation requires knowledge of actual machine registers, calling conventions, and hardware constraints — information that high-level IRs deliberately abstract away. It must be performed on a low-level IR where variables have been mapped to virtual registers, instruction selection is complete, and the correspondence to hardware operations is clear. A high-level IR that abstracts over register counts and classes cannot meaningfully perform register allocation. This is a classic example of the tradeoff: high-level IRs enable semantic analysis and source-level optimizations; low-level IRs enable backend tasks."

- question: "What three questions should guide the design of an IR for a specific compiler phase, and what does each reveal about the appropriate IR choice?"
  type: short-answer
  answer: "1. What transformations will this IR undergo? This determines required structural properties — dataflow analysis needs explicit use-def chains (favoring SSA or linear code over trees); loop optimizations need preserved loop structure (favoring high-level IR). 2. What information must be preserved versus discarded? High-level semantic information needed for optimization must be retained; irrelevant details should be lowered to reduce complexity. 3. How many lowering steps separate this IR from the final output? Deep in the pipeline, IRs should be close to machine code to enable target-specific optimizations like register allocation."
  explanation: "These questions prevent the mistake of designing one IR for everything. No single IR can simultaneously preserve loop structure for vectorization, provide precise use-def chains for dataflow optimization, and be close enough to machine code for register allocation. Production compilers use multiple IR levels because each answers a specific subset of these questions. The expressiveness-vs-analyzability tradeoff is real: a tree IR is expressive but hard to analyze; a linear SSA IR is highly analyzable but loses structural information. Identifying which tradeoff matters for each compilation phase is the core skill in IR design."
```

## Explainer

From your work on compiler phases and intermediate code representation, you know that a compiler does not translate source code directly into machine instructions. Instead, it lowers the program through one or more **intermediate representations** — internal data structures that sit between the source language and the target machine. The design question is not whether to use an IR, but which shape of IR best serves the compiler's goals, and how many levels of IR the compiler should maintain.

Think of IR design as choosing a language for the compiler to talk to itself. A **high-level IR** preserves source-language structure — loops, conditionals, typed variables, function calls — much like an abstract syntax tree with annotations. This makes it easy to perform type checking, inlining decisions, and source-level optimizations, but the IR is far from the machine and must eventually be "lowered" through multiple transformation passes. A **low-level IR**, by contrast, looks closer to assembly: explicit registers or virtual registers, flat control flow with branches, and simple three-address instructions. Low-level IRs simplify instruction selection and register allocation but lose the structural information that high-level optimizations need.

Most production compilers solve this tension by using **multiple IR levels**. LLVM, for instance, accepts high-level input from language frontends (Clang emits LLVM IR), performs optimization passes on its SSA-based mid-level IR, and then lowers to a machine-specific IR before final code emission. Each level of IR is designed for the transformations that happen at that stage. The high-level IR preserves semantic richness; the mid-level IR enables general-purpose optimization; the low-level IR enables target-specific tuning. This layered approach is what makes LLVM usable across dozens of source languages and target architectures — the IR boundaries define clean interfaces between compiler components.

The key tradeoffs to internalize are these: **expressiveness versus analyzability**. A tree-based IR is expressive and maps naturally to source constructs, but analyzing control flow across branches requires flattening it. A flat, three-address-code IR makes control flow explicit and is easy to analyze with dataflow techniques, but reconstructing high-level loop structure for vectorization requires extra analysis. **Graph-based IRs** like SSA (Static Single Assignment) form occupy a middle ground — they make data flow explicit through use-def chains while keeping control flow as a graph of basic blocks. SSA is dominant in modern compilers precisely because it balances these concerns, making many optimizations (constant propagation, dead code elimination, register allocation) both simpler to implement and more effective.

When evaluating an IR design, ask three questions: What transformations will this IR undergo? What information must be preserved versus what can be discarded? And how many lowering steps separate this IR from the final output? The answers determine whether you need a tree, a graph, a linear sequence, or some hybrid — and whether a single IR suffices or a multi-level pipeline is warranted.
