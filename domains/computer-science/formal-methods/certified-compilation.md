---
id: certified-compilation
title: Certified Compilation
domain: computer-science
course: formal-methods
prerequisites:
- id: operational-semantics
  type: hard
- id: interactive-theorem-proving
  type: hard
- id: program-synthesis
  type: soft
builds-toward: []
tags:
- verified-compiler
- compcert
- semantics-preservation
- bisimulation
- compiler-correctness
- proof-assistant
stage: expert
status: validated
---

# Certified Compilation

## Core Idea

Certified compilation produces a compiler whose behavior is proven correct by a machine-checked formal proof. A certified compiler guarantees that the compiled code behaves identically to the source program — miscompilation bugs are impossible by mathematical proof, not by testing. **CompCert** (the foundational example) is a certified C compiler where every optimization pass is formally verified in Coq to preserve program semantics. The proof demonstrates a **simulation** or **bisimulation** between source and compiled code: any observable behavior (input/output, termination, failure) of the source is faithfully reproduced by the compiled code. This provides absolute assurance that the compiler will not introduce subtle bugs that testing might miss.

## Questions

```yaml
- question: "A compiler is 'certified' if its output is proven to preserve program semantics. What does 'preserve semantics' formally mean?"
  type: short-answer
  answer: "Semantic preservation means: for any source program P and any input I, if P produces output O (or diverges, or crashes), then the compiled code produces the same output O (or diverges, or crashes identically). Formally, this is expressed as a **simulation** or **bisimulation** relation: the compiled code's execution trace matches the source code's trace up to irrelevant differences (like variable names or intermediate machine states). The proof establishes that no behavior of the source program is changed by compilation."
  explanation: "This is a theorem of the form: ∀ source, compiled. compile(source) = compiled → ∀ input. semantics(source, input) ~ semantics(compiled, input), where ~ is a simulation or bisimulation relation. The proof is done in a proof assistant (Coq, Isabelle, Agda), making it machine-checkable. The key is that semantic preservation is stronger than 'the compiler doesn't crash' — it says the compiler's output has the exact same behavior as the input."

- question: "CompCert is verified in Coq and handles a subset of C. Why not verify a compiler for the full C language?"
  type: short-answer
  answer: "Verifying a compiler requires: (1) a formal semantics of the source language (every rule, every edge case), (2) a formal semantics of the target language (the machine/virtual machine), (3) proof that every transformation preserves semantics. Full C has thousands of pages of specification, undefined behavior in many contexts, and complex interactions between features (pointer arithmetic, type casting, volatile access). Verifying all of this is infeasible within reasonable effort. CompCert handles a safe subset of C (excluding undefined behaviors, dangerous casts, etc.), which is suitable for many real applications. Full verification of realistic languages remains an active research area."
  explanation: "This is a fundamental tension in certified compilation: completeness vs. tractability. A complete compiler for full C would be incredibly difficult to verify because the semantics is complex and sometimes underspecified. CompCert made a strategic choice: verify a safe subset thoroughly rather than attempt a fragile claim about the full language. In practice, many critical systems don't use the dangerous corners of C anyway, so CompCert's scope is reasonable. As proof assistant tooling and proof techniques improve, the scope of certified compilers expands."

- question: "A certified compiler must prove a simulation relation between source and compiled code. Which of the following can be assumed as part of the proof, and which must be verified?"
  type: multiple-choice
  options:
    - "The source language semantics and the target language semantics are both assumed; only the transformation is verified"
    - "All of these are assumed — the compiler is certified by testing"
    - "The source language semantics must be verified, but the target language (hardware) semantics is assumed"
    - "The source language semantics is given; the target language semantics is given; the transformation (each optimization pass) is verified to establish a simulation"
  answer: 3
  explanation: "In certified compilation, the source and target language semantics are **given** (formalized in the proof assistant, not proven). These are the inputs to the certification effort. The **transformation** — the actual compiler code and its optimization passes — is what is verified. Each pass (constant propagation, dead code elimination, register allocation, etc.) is verified to preserve semantics: given any source program satisfying the source semantics, the output of this pass satisfies the target semantics. CompCert formalizes C semantics and x86 (or PowerPC) semantics, then verifies each pass."

- question: "If a certified compiler has a bug in its output, what does that imply?"
  type: short-answer
  answer: "Either: (1) the formal semantics of the source or target language is incorrect (doesn't accurately model the language), or (2) the proof itself has a bug (which is rare but possible if the proof assistant has a soundness bug). It does NOT imply a bug in the verified compiler transformation, because the transformation is machine-checked by the proof assistant. The power of certified compilation is that bugs in the transformation are impossible — the machine-checked proof provides absolute assurance of the compiler's correctness (modulo the semantics and the proof assistant)."
  explanation: "This illustrates the scope of certification: the proof is only as good as its inputs (the semantics) and the tool that checks it (the proof assistant's kernel). In practice, the semantics of C and x86 used in CompCert are carefully validated against the official specifications, and the Coq kernel is extensively tested. The result is compiler correctness with extremely high confidence — far higher than any compiler verified by testing alone."
```

## Explainer

Every programmer knows the frustration: a compiler bug sneaks a miscompilation into production code. The program works correctly in isolation but fails in specific contexts because the compiler incorrectly optimized or transformed it. Compiler bugs are rare but devastating because they strike at a level of abstraction the programmer trusts completely. **Certified compilation** solves this problem at its root: prove mathematically that the compiler is correct.

**CompCert**, developed by Xavier Leroy and colleagues, demonstrated that certified compilation is practical. CompCert is a compiler from a subset of C to multiple target architectures (x86, PowerPC, ARM), with every transformation pass proven correct in Coq. The proof is machine-checked, meaning no argument is accepted unless the Coq kernel formally verifies it. The result is a compiler with an absolute guarantee: any observable behavior (input/output, termination, failure) of a C program compiled by CompCert will be identical to the behavior if that program were executed by a reference interpreter of C semantics.

The approach has two main components:

1. **Formal semantics**: Both the source language (C) and target language (assembly) are formalized mathematically. This is not a vague description but a precise definition of every operation, rule, and edge case. For C, this includes pointer operations, type conversions, memory layout, and undefined behavior boundaries. For the target assembly, it includes instruction execution, memory access, register semantics.

2. **Verified transformations**: Each compiler pass (parsing, type checking, optimization, code generation, register allocation) is implemented and proven to preserve semantics. A proof of semantic preservation for a pass P says: given a source program S that satisfies source semantics, the output P(S) satisfies target semantics and exhibits identical observable behavior.

The key insight is the **simulation relation** (or **bisimulation**): a formal notion of "same behavior." A backward simulation says that for every step of the target program (compiled), there is a corresponding step (or sequence of steps) of the source program, and the states remain "equivalent" throughout execution. This equivalence is carefully defined to ignore irrelevant differences (variable names, intermediate machine states) while preserving observable behaviors.

**Practical implications:**

- **No miscompilation bugs**: Unlike conventional compilers tested on large benchmark suites, CompCert's correctness is absolute. A bug in the verified transformation is mathematically impossible; any failure must lie outside the verified scope (e.g., in the un-verified parts like preprocessing or linking).

- **Scope tradeoff**: CompCert doesn't support every C feature (some undefined behaviors, dangerous casts, volatile access are excluded) and doesn't target every architecture. But the subset it covers is suitable for systems programming and critical applications.

- **Performance**: CompCert includes optimizations (constant propagation, dead code elimination, common subexpression elimination, instruction scheduling). The compiler is 80-90% as fast as GCC on many benchmarks, demonstrating that certified compilation doesn't require sacrificing performance.

- **Widespread applicability**: CompCert has been applied to verify embedded systems, aerospace software, and critical infrastructure. The guarantee that no compiler-introduced bugs can appear provides enormous value in high-assurance contexts.

**Beyond CompCert:**

- **Sel4 microkernel**: The seL4 operating system kernel (a microkernel used in military/critical systems) was verified in Isabelle/HOL, including compilation to executable code.
- **Cryptol**: A domain-specific language for cryptographic specifications, with a certified compiler to C.
- **CakeML**: A dialect of Standard ML with a fully certified compiler from source to machine code, verified in HOL4.

The cost of certified compilation is development effort: CompCert took many years and extensive formalization effort. But as proof automation improves and certified compiler frameworks are reused, the cost is decreasing. The benefit — absolute assurance of compiler correctness — is increasingly valuable for critical systems where a single bug can have catastrophic consequences.

The fundamental question certified compilation raises is: how much can we trust automation? The answer CompCert provides is: we can trust compilers completely if we formalize their behavior and mechanically verify it. This is not a rejection of testing or engineering rigor but a complement: formal proof for the parts we can formalize, testing and review for the parts we cannot.
