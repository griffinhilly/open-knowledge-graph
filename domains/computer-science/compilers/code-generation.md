---
id: code-generation
title: Code Generation from IR
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: instruction-set-architecture
  type: hard
builds-toward:
- activation-records-runtime
- jit-compilation
tags:
- code-generation
- machine-code
- code-emission
stage: advanced
status: validated
---

# Code Generation from IR

## Core Idea
Code generation transforms optimized IR into executable machine code. For each IR instruction, emit corresponding assembly or bytecode. This involves instruction selection (choosing target instructions), operand allocation (assigning registers/memory), and instruction scheduling (reordering for performance). Modern code generators use pattern matching, templates, or dynamic programming to select instructions.

## Questions

```yaml
- question: "During instruction selection, what core challenge does a compiler face when mapping IR to machine instructions?"
  type: multiple-choice
  options:
    - "Determining whether the program terminates"
    - "Many IR instruction sequences can be covered by multiple machine instruction patterns with different execution costs"
    - "Converting floating-point values to integer types"
    - "Removing unused variables from the symbol table"
  answer: 1
  explanation: "Instruction selection is fundamentally a pattern-matching and covering problem: a sequence of IR instructions can often be covered by different combinations of machine instructions (e.g., one complex instruction vs. several simpler ones), each with different execution costs. Choosing the minimum-cost cover is NP-hard in general, so compilers use dynamic programming, greedy heuristics, or tree pattern matching to approximate the optimum."

- question: "Register allocation is expected to happen before instruction selection because the number of available physical registers constrains which machine instructions can be chosen."
  type: true-false
  answer: false
  explanation: "In most compiler architectures, instruction selection precedes register allocation. Instructions are first selected assuming an unlimited supply of virtual (temporary) registers; register allocation then maps virtual registers to physical ones, inserting spill code to memory when physical registers run out. Some compilers interleave the phases, but the standard pipeline — used by LLVM and GCC — selects instructions first, then allocates registers."

- question: "What is instruction scheduling, and why is it a distinct concern from instruction selection in modern processors?"
  type: short-answer
  answer: "Instruction scheduling reorders instructions — without changing program semantics — to avoid pipeline stalls and exploit instruction-level parallelism. It is separate from instruction selection because selection decides *which* instructions to emit, while scheduling decides *in what order* to emit them. Modern processors execute instructions out of order at runtime, but static compiler scheduling reduces hazards (such as memory load latencies) that hardware reordering cannot always resolve."
  explanation: "The separation reflects distinct optimization goals: instruction selection minimizes the number and cost of operations; instruction scheduling minimizes the wall-clock time those operations take by exploiting processor microarchitecture. Both phases require knowledge of the target machine, but they use different algorithms (covering/matching for selection; list scheduling or software pipelining for scheduling) and can be improved independently."
```

## Explainer

After the front end parses and analyzes source code and the middle end optimizes an intermediate representation (IR), the back end has one job: turn that IR into instructions the target machine can execute. This is code generation, and it is harder than it sounds because IR is designed for portability and ease of manipulation — it does not map one-to-one to any real instruction set. The code generator must bridge that gap while producing efficient output.

The first sub-problem is *instruction selection*: for each IR operation (or group of operations), choose which machine instruction(s) to emit. Many IR patterns can be matched by multiple sequences of machine instructions with different costs. For example, a multiply-and-add operation in the IR might be expressible as two instructions (MUL then ADD) or as a single fused multiply-add instruction if the target supports it. The compiler models this as a tree-pattern-matching problem — the IR is treated as a tree, and a library of patterns (each corresponding to a machine instruction) is applied greedily or via dynamic programming to find the lowest-cost cover.

The second sub-problem is *register allocation*: the IR assumes an unlimited supply of temporary variables, but real machines have a fixed, small set of registers. Register allocation assigns IR temporaries to physical registers, and when there are not enough registers, decides which values to *spill* — write to the stack and reload later. Spilling is expensive because memory accesses are slow, so minimizing spills is critical. Register allocation is modeled as a graph-coloring problem: temporaries that are "live" at the same time cannot share a register, and coloring the interference graph with K colors (where K is the number of registers) finds a valid assignment or identifies which temporaries must be spilled.

The third sub-problem is *instruction scheduling*: modern processors have pipelines and can execute multiple instructions simultaneously, but only if there are no data or resource hazards between them. The compiler reorders instructions (subject to data-flow dependencies) to keep the pipeline busy. A load from memory, for example, might stall the pipeline for many cycles waiting for the result — a scheduler can move other independent instructions into that gap. Scheduling after register allocation is common because the register assignment affects which instructions can be reordered.

The output of code generation is assembly or object code for a specific target architecture (x86, ARM, RISC-V, WebAssembly, etc.). This is why the back end is the component that must be rewritten when porting a compiler to a new target — the front end (parsing, type checking) and middle end (IR optimizations) remain the same. LLVM's success largely comes from providing a high-quality, target-independent IR and a shared code generation framework that handles much of this complexity, allowing front ends for many languages to benefit from one well-engineered back end.
