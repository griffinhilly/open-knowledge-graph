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
status: draft
---

# Intermediate Code Representation

## Core Idea
Intermediate representation (IR) is an abstraction between source and target languages. Common forms include three-address code (TAC), register-transfer language (RTL), and bytecode. IR simplifies optimization and retargeting: optimize once on IR, then generate code for multiple targets. IR abstracts away source-language details and target-machine specifics, enabling machine-independent transformations.

## Explainer

After semantic analysis, you have an AST annotated with types and scope information — a tree that faithfully represents the structure of the source program. But an AST is a poor target for optimization and code generation: its structure mirrors the source language's syntax, not the machine's execution model, and tree transformations are awkward for the linear, instruction-by-instruction reasoning that optimization requires. **Intermediate representation** is the bridge: a language-neutral, machine-neutral format that is low-level enough to reason about execution but high-level enough to support powerful transformations before committing to any specific target architecture.

The most common IR form is **three-address code (TAC)**, where every instruction has at most one operator and up to three operands: `t1 = a + b`, `t2 = t1 * c`, `if t2 > 0 goto L1`. Complex source expressions are decomposed into sequences of simple operations using **temporary variables**. The expression `a + b * c - d` becomes something like `t1 = b * c; t2 = a + t1; t3 = t2 - d`. This flat, explicit form makes data flow visible — you can see exactly which temporaries feed into which operations — and is easy to analyze for optimization. Control flow constructs like loops and conditionals become explicit labels and goto instructions, making the control flow graph straightforward to extract.

The strategic value of IR is the **m × n problem**. Without IR, supporting m source languages and n target machines requires m × n separate translators. With a common IR, you need only m frontends (source → IR) and n backends (IR → machine code), for m + n total components. This is why LLVM's IR is so influential: any language frontend that emits LLVM IR gets access to LLVM's entire suite of optimizations and all its target backends, from x86 to ARM to WebAssembly. The same principle applies at a smaller scale within a single compiler — machine-independent optimizations like constant folding, dead code elimination, and common subexpression elimination are written once on the IR and apply regardless of what source language produced it or what target will consume it.

Different compilers use IRs at different abstraction levels, and some use multiple IR levels. A high-level IR might preserve loop structure and array indexing; a low-level IR might expose individual memory loads, stores, and register-like temporaries. **Static Single Assignment (SSA) form** — where each variable is assigned exactly once — is a particularly powerful IR variant that simplifies many optimization analyses by making data flow explicit. Bytecode formats like the JVM's or Python's are also IRs, interpreted by a virtual machine rather than compiled to hardware. The choice of IR shapes what optimizations are easy to express: design the right intermediate language, and the optimizations almost write themselves.
