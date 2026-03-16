---
id: code-optimization
title: Code Optimization Fundamentals
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
builds-toward:
- common-subexpression-elimination
- loop-invariant-code-motion
- constant-propagation
tags:
- optimization
- compiler-design
- performance
stage: advanced
status: draft
---

# Code Optimization Fundamentals

## Core Idea
Code optimization improves program performance (speed, memory, energy) without changing observable behavior (correctness). Optimizations are enabled by dataflow analysis: reaching definitions, liveness, availability. Machine-independent optimizations (constant propagation, CSE) are applied to IR; machine-dependent optimizations (instruction scheduling, register allocation) target specific architectures.

## Explainer

Once a compiler has parsed source code into an intermediate representation and analyzed its dataflow properties, it can begin **code optimization** — transforming the program to run faster, use less memory, or consume less energy, all while producing exactly the same observable results. This correctness constraint is paramount: an optimization that makes a program faster but changes its output is a bug, not an improvement. The dataflow analyses you studied — reaching definitions, live variables, available expressions — are what make safe optimization possible, because they tell the compiler precisely what it can and cannot change.

**Machine-independent optimizations** work on the IR and apply regardless of the target hardware. **Constant propagation** replaces variables with their known constant values — if `x = 5` at every point where `x` is used, replace every use of `x` with `5` and eliminate the variable entirely. **Common subexpression elimination (CSE)** detects when the same expression is computed multiple times with the same operands and reuses the first result instead of recomputing. **Dead code elimination** removes computations whose results are never used, identified through liveness analysis. **Loop-invariant code motion** moves computations that produce the same result on every loop iteration to before the loop, executing them once instead of thousands of times. Each of these transformations is enabled by a specific dataflow analysis that proves the transformation is safe.

**Machine-dependent optimizations** target specific hardware characteristics. **Register allocation** assigns frequently used variables to fast CPU registers instead of slow memory, guided by liveness and interference information. **Instruction scheduling** reorders instructions to avoid pipeline stalls on a specific processor, filling delay slots and maximizing instruction-level parallelism. **Peephole optimization** scans small windows of generated instructions and replaces inefficient patterns with better ones — replacing a multiply by a power of 2 with a left shift, for example. These optimizations require detailed knowledge of the target architecture and are applied after or during code generation.

An important concept is that optimizations **interact**: performing one optimization may enable or disable others. Constant propagation may reveal that a branch condition is always true, enabling dead code elimination of the false branch. That dead code elimination may in turn make a variable's definition unreachable, enabling further simplification. Because of these interactions, compilers typically run optimization passes in carefully ordered sequences, sometimes repeating passes until no further improvements are found. Understanding this phase-ordering problem — that the best sequence of optimizations depends on the specific program — is part of what makes compiler optimization as much an engineering discipline as a theoretical one.
