---
id: intermediate-code-representation
title: Intermediate Code Representation
domain: computer-science
course: compilers
prerequisites:
- id: semantic-analysis
  type: hard
- id: abstract-syntax-trees
  type: hard
builds-toward:
- static-single-assignment-form
- code-optimization
tags:
- intermediate-representation
- ir
- compilation-phases
stage: advanced
status: validated
---

# Intermediate Code Representation

## Core Idea
Intermediate representation (IR) is an abstraction between source and target languages. Common forms include three-address code (TAC), register-transfer language (RTL), and bytecode. IR simplifies optimization and retargeting: optimize once on IR, then generate code for multiple targets. IR abstracts away source-language details and target-machine specifics, enabling machine-independent transformations.

## Questions

```yaml
- question: "A compiler team wants to support 5 source languages targeting 4 hardware architectures. Without IR, how many separate translators do they need? With a shared IR?"
  type: multiple-choice
  options:
    - "Without IR: 9 (5 + 4); with IR: 20 (5 × 4)"
    - "Without IR: 20 (5 × 4); with IR: 9 (5 + 4)"
    - "Without IR: 20 (5 × 4); with IR: 5 (one per source language)"
    - "The number is the same either way; IR only affects optimization quality, not translator count"
  answer: 1
  explanation: "Without IR, each source language needs a direct translator to each target — 5 × 4 = 20 translators. With IR, you need m frontends (source → IR) plus n backends (IR → machine code) = 5 + 4 = 9 components. This m+n vs. m×n tradeoff is the core strategic value of IR. It scales dramatically: at 10 languages and 10 targets, the difference is 20 vs. 100 components. This is why LLVM's IR has been so influential — any language that emits LLVM IR gets all LLVM backends for free."

- question: "Why is three-address code (TAC) better than an AST as a target for optimization passes like dead code elimination or constant folding?"
  type: multiple-choice
  options:
    - "TAC is closer to machine code, so optimization passes run faster"
    - "TAC eliminates all temporary variables before optimization, reducing state to track"
    - "TAC mirrors source language syntax, making it easier to preserve programmer intent"
    - "TAC flattens expressions into sequential instructions with named temporaries, making data flow and control flow explicit and easy to analyze"
  answer: 3
  explanation: "An AST mirrors the tree structure of the source syntax, which is awkward for optimization — you need recursive tree traversals, and data flow between expressions is implicit in the nesting. TAC decomposes every expression into at most one operation using named temporaries (t1 = b*c; t2 = a+t1), making every data dependency an explicit named reference. Control flow becomes explicit labels and gotos. This flat, explicit form is ideal for constructing data flow graphs, identifying dead assignments, finding common subexpressions, and all standard optimizations."

- question: "A single set of optimization passes (e.g., dead code elimination) written for an IR can be applied to programs from multiple source languages."
  type: true-false
  answer: true
  explanation: "Yes — this is a core benefit of IR. Optimizations are written once against the IR, not against individual source languages. Once Python, Rust, and C all compile to LLVM IR, LLVM's dead code elimination, constant folding, and inlining passes apply to all three without modification. The frontend translates source to IR; the optimizer works on IR; the backend generates machine code from IR. Each phase is independent."

- question: "Using an IR layer typically produces slower machine code than a direct source-to-machine translation, because the extra translation step introduces inefficiency."
  type: true-false
  answer: false
  explanation: "The opposite is generally true. IR enables machine-independent optimizations (constant folding, dead code elimination, common subexpression elimination, inlining) that operate before any target-specific code generation. A direct source-to-machine translation typically applies only simple, local optimizations. The IR-based approach, by exposing program structure in an analyzable form, enables deeper analysis and better code. SSA form in particular enables powerful optimizations that would be impractical on an AST or direct machine code."

- question: "Why is three-address code a better target for optimization than an abstract syntax tree, even though both represent the same program?"
  type: short-answer
  answer: "An AST mirrors source syntax: expressions are nested, data flow is implicit in tree structure, and control flow is buried inside if/while/for nodes. Optimization requires traversing the tree recursively and reasoning about implicit relationships. TAC explodes every expression into a flat sequence of single-operation instructions using named temporaries, making every data dependency an explicit reference and every control transfer an explicit goto. This means a compiler can extract data flow and control flow graphs directly, identify which definitions reach which uses, and apply standard analysis algorithms (liveness, reaching definitions, dominance) without first transforming the structure."
  explanation: "The transformation from AST to TAC trades tree structure for sequential explicitness. Optimizations that would require complex tree transformations become simple instruction-level substitutions on TAC. This is why SSA form (a restricted TAC where each temporary is assigned exactly once) simplifies optimization further — it makes data flow not just visible but unique, trivializing many analyses."
```

## Explainer

After semantic analysis, you have an AST annotated with types and scope information — a tree that faithfully represents the structure of the source program. But an AST is a poor target for optimization and code generation: its structure mirrors the source language's syntax, not the machine's execution model, and tree transformations are awkward for the linear, instruction-by-instruction reasoning that optimization requires. **Intermediate representation** is the bridge: a language-neutral, machine-neutral format that is low-level enough to reason about execution but high-level enough to support powerful transformations before committing to any specific target architecture.

The most common IR form is **three-address code (TAC)**, where every instruction has at most one operator and up to three operands: `t1 = a + b`, `t2 = t1 * c`, `if t2 > 0 goto L1`. Complex source expressions are decomposed into sequences of simple operations using **temporary variables**. The expression `a + b * c - d` becomes something like `t1 = b * c; t2 = a + t1; t3 = t2 - d`. This flat, explicit form makes data flow visible — you can see exactly which temporaries feed into which operations — and is easy to analyze for optimization. Control flow constructs like loops and conditionals become explicit labels and goto instructions, making the control flow graph straightforward to extract.

The strategic value of IR is the **m × n problem**. Without IR, supporting m source languages and n target machines requires m × n separate translators. With a common IR, you need only m frontends (source → IR) and n backends (IR → machine code), for m + n total components. This is why LLVM's IR is so influential: any language frontend that emits LLVM IR gets access to LLVM's entire suite of optimizations and all its target backends, from x86 to ARM to WebAssembly. The same principle applies at a smaller scale within a single compiler — machine-independent optimizations like constant folding, dead code elimination, and common subexpression elimination are written once on the IR and apply regardless of what source language produced it or what target will consume it.

Different compilers use IRs at different abstraction levels, and some use multiple IR levels. A high-level IR might preserve loop structure and array indexing; a low-level IR might expose individual memory loads, stores, and register-like temporaries. **Static Single Assignment (SSA) form** — where each variable is assigned exactly once — is a particularly powerful IR variant that simplifies many optimization analyses by making data flow explicit. Bytecode formats like the JVM's or Python's are also IRs, interpreted by a virtual machine rather than compiled to hardware. The choice of IR shapes what optimizations are easy to express: design the right intermediate language, and the optimizations almost write themselves.
