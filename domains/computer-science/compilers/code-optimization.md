---
id: code-optimization
title: Code Optimization Fundamentals
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
- id: peephole-optimization
  type: soft
- id: dead-code-elimination
  type: soft
builds-toward:
- common-subexpression-elimination
- loop-invariant-code-motion
- constant-propagation
tags:
- optimization
- compiler-design
- performance
stage: advanced
status: validated
---
# Code Optimization Fundamentals

## Core Idea
Code optimization improves program performance (speed, memory, energy) without changing observable behavior (correctness). Optimizations are enabled by dataflow analysis: reaching definitions, liveness, availability. Machine-independent optimizations (constant propagation, CSE) are applied to IR; machine-dependent optimizations (instruction scheduling, register allocation) target specific architectures.

## Questions

```yaml
- question: "A compiler's reaching definitions analysis determines that variable x is assigned the constant value 5 on every path reaching a loop body, and x is not modified inside the loop. Which optimization applies, and what dataflow analysis enables it?"
  type: multiple-choice
  options:
    - "Dead code elimination, enabled by liveness analysis showing x is never used after the loop"
    - "Constant propagation, enabled by reaching definitions analysis proving x always holds the value 5 at each use"
    - "Loop-invariant code motion, enabled by dominator analysis showing the assignment dominates the loop header"
    - "Register allocation, enabled by an interference graph showing x has a short live range"
  answer: 1
  explanation: "Reaching definitions analysis tracks which variable definitions reach each program point. If only one definition of x — the assignment x = 5 — reaches every use inside the loop, the compiler can safely replace every use of x with the literal 5, eliminating the variable. This is constant propagation. Reaching definitions is exactly the dataflow analysis that proves the substitution is safe (no other value reaches those use sites). Loop-invariant code motion would apply to expressions computed inside the loop whose operands don't change; here x is already a known constant, so its uses are simply replaced."

- question: "After optimization, a compiled program runs 15% faster but produces slightly different output on certain inputs compared to the unoptimized version. How should this be classified?"
  type: multiple-choice
  options:
    - "A valid optimization — performance gain justifies small deviations in output"
    - "A valid optimization for floating-point operations, which have inherent imprecision"
    - "A compiler bug — preserving observable behavior is an absolute constraint on all optimizations"
    - "Acceptable for machine-dependent optimizations but a bug in machine-independent ones"
  answer: 2
  explanation: "The fundamental invariant of code optimization is that observable behavior must be preserved — no exceptions. An optimization that changes program output is definitionally a compiler bug, not a performance-correctness tradeoff. Observable behavior includes outputs, side effects, and for concurrent programs, certain operation orderings. Options A, B, and D all treat correctness as negotiable — this is the key misconception to reject. The correctness constraint is what distinguishes a safe transformation from a program-corrupting bug."

- question: "Machine-independent optimizations like constant propagation and dead code elimination are applied during target-specific code generation to the instruction sequences of the target architecture."
  type: true-false
  answer: false
  explanation: "Machine-independent optimizations are applied to the intermediate representation (IR) — before any target-specific code generation. They operate on an abstract, architecture-neutral program representation and produce improvements that apply regardless of the target hardware. Machine-dependent optimizations (register allocation, instruction scheduling, peephole optimization) are what target specific hardware, applied during or after code generation. The distinction reflects the compiler pipeline: IR-level transformations first, then architecture-specific optimizations."

- question: "Applying constant propagation to a program may create opportunities for dead code elimination that would not have been detectable before constant propagation ran."
  type: true-false
  answer: true
  explanation: "Optimizations interact: the output of one creates conditions for another. Constant propagation replaces variables with their known constant values. If a branch condition becomes a known constant (effectively 'if (false)'), the unreachable branch is now detectable as dead code — but before constant propagation, the branch condition appeared to depend on a variable, making that branch appear live. Dead code elimination can then remove it. This chaining is why compilers run optimization passes in sequences and repeat them until no further improvements are found."

- question: "Why must every compiler optimization be justified by a dataflow analysis that proves the transformation is safe to apply?"
  type: short-answer
  answer: "Optimizations eliminate, reorder, or replace computations. Doing this incorrectly changes the program's observable behavior — making it a bug rather than an optimization. Dataflow analysis provides the formal proof that a transformation is safe: reaching definitions proves a constant substitution is valid (no other value reaches the use site); liveness analysis proves a computation is dead (its result is never subsequently used); available expressions analysis proves a reused value is still current (no intervening modification of its operands). Without this proof, an 'optimization' might eliminate a live computation, reuse a stale value, or hoist a non-invariant expression — corrupting the program."
  explanation: "Consider common subexpression elimination: replacing a second computation of (a + b) with the first result is only safe if neither a nor b has been modified between the two computations. Available expressions analysis tracks exactly this — an expression is 'available' at a point if it was computed on every reaching path and its operands were not subsequently modified. Without this analysis, CSE might reuse a stale result after a was reassigned, producing wrong output while appearing to be a legitimate optimization. The correctness constraint requires formal proof, and dataflow analysis provides that proof."
```

## Explainer

Once a compiler has parsed source code into an intermediate representation and analyzed its dataflow properties, it can begin **code optimization** — transforming the program to run faster, use less memory, or consume less energy, all while producing exactly the same observable results. This correctness constraint is paramount: an optimization that makes a program faster but changes its output is a bug, not an improvement. The dataflow analyses you studied — reaching definitions, live variables, available expressions — are what make safe optimization possible, because they tell the compiler precisely what it can and cannot change.

**Machine-independent optimizations** work on the IR and apply regardless of the target hardware. **Constant propagation** replaces variables with their known constant values — if `x = 5` at every point where `x` is used, replace every use of `x` with `5` and eliminate the variable entirely. **Common subexpression elimination (CSE)** detects when the same expression is computed multiple times with the same operands and reuses the first result instead of recomputing. **Dead code elimination** removes computations whose results are never used, identified through liveness analysis. **Loop-invariant code motion** moves computations that produce the same result on every loop iteration to before the loop, executing them once instead of thousands of times. Each of these transformations is enabled by a specific dataflow analysis that proves the transformation is safe.

**Machine-dependent optimizations** target specific hardware characteristics. **Register allocation** assigns frequently used variables to fast CPU registers instead of slow memory, guided by liveness and interference information. **Instruction scheduling** reorders instructions to avoid pipeline stalls on a specific processor, filling delay slots and maximizing instruction-level parallelism. **Peephole optimization** scans small windows of generated instructions and replaces inefficient patterns with better ones — replacing a multiply by a power of 2 with a left shift, for example. These optimizations require detailed knowledge of the target architecture and are applied after or during code generation.

An important concept is that optimizations **interact**: performing one optimization may enable or disable others. Constant propagation may reveal that a branch condition is always true, enabling dead code elimination of the false branch. That dead code elimination may in turn make a variable's definition unreachable, enabling further simplification. Because of these interactions, compilers typically run optimization passes in carefully ordered sequences, sometimes repeating passes until no further improvements are found. Understanding this phase-ordering problem — that the best sequence of optimizations depends on the specific program — is part of what makes compiler optimization as much an engineering discipline as a theoretical one.
