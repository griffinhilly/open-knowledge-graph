---
id: jit-compilation
title: Just-In-Time (JIT) Compilation
domain: computer-science
course: compilers
prerequisites:
- id: code-generation
  type: hard
- id: garbage-collection-algorithms
  type: soft
tags:
- jit
- runtime-compilation
- dynamic-compilation
stage: advanced
status: draft
---

# Just-In-Time (JIT) Compilation

## Core Idea
Just-in-time compilation compiles code at runtime during program execution, enabling adaptive optimization. A JIT monitors runtime behavior (hot paths, type information) and generates specialized code based on observed patterns. JIT can outperform ahead-of-time compilation by exploiting runtime information and code specialization, though with compilation overhead. Languages like Java and JavaScript use JIT extensively.

## Explainer

In a traditional ahead-of-time (AOT) compiler, the code generation phase you already know produces machine code once, before the program ever runs. The compiler must make conservative assumptions — it cannot know which functions will be called millions of times or what types a variable will actually hold. **Just-in-time compilation** flips this model: it defers code generation to runtime, where it can observe the program's actual behavior and generate code tailored to what is really happening.

A JIT system typically starts by interpreting bytecode or running lightly compiled code, profiling as it goes. It tracks **hot paths** — functions or loops that execute frequently — and identifies them as candidates for compilation. When a hot path is detected, the JIT compiler kicks in and generates optimized machine code specifically for that path. This is where the connection to code generation becomes concrete: the JIT performs the same instruction selection, register allocation, and scheduling you studied in code generation, but it does so at runtime with additional information the AOT compiler never had.

The key advantage is **specialization**. Consider a function that accepts arguments of any type. An AOT compiler must generate code that handles every possible type. A JIT can observe that the function is always called with integers, generate a fast integer-only version, and insert a **guard** — a lightweight check that the assumption still holds. If the guard fails (the function is suddenly called with a string), the JIT falls back to a slower generic path or recompiles. This speculative optimization is why JIT-compiled languages like Java and JavaScript can approach and sometimes exceed the performance of statically compiled C code for specific workloads.

The tradeoff is **compilation overhead at runtime**. Every moment spent compiling is a moment not spent executing the program. JIT systems manage this with tiered compilation: code starts interpreted (zero compilation cost), gets baseline-compiled when warm, and receives full optimization only when truly hot. The garbage collector — which you may know from its role in memory management — interacts closely with the JIT, since compiled code contains assumptions about object layouts that the GC must respect when moving objects in memory. This interplay between runtime compilation, profiling, and memory management is what makes JIT systems both powerful and architecturally complex.
