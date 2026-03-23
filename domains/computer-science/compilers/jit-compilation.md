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
status: validated
---

# Just-In-Time (JIT) Compilation

## Core Idea
Just-in-time compilation compiles code at runtime during program execution, enabling adaptive optimization. A JIT monitors runtime behavior (hot paths, type information) and generates specialized code based on observed patterns. JIT can outperform ahead-of-time compilation by exploiting runtime information and code specialization, though with compilation overhead. Languages like Java and JavaScript use JIT extensively.

## Questions

```yaml
- question: "A JIT compiler observes that a function is always called with integer arguments and generates a specialized integer-only version. What must the JIT include to handle the case when the function is later called with a float?"
  type: multiple-choice
  options:
    - "A compile-time type checker that prevents the float call"
    - "A guard that checks the type assumption at runtime and falls back if violated"
    - "A second pass of the AOT compiler to handle edge cases"
    - "Nothing — the specialized version will automatically handle floats correctly"
  answer: 1
  explanation: "Speculative optimization requires guards — runtime checks that verify the assumed conditions still hold. If a float is passed (violating the integer assumption), the guard triggers and the JIT falls back to a slower generic path or recompiles. Without guards, specialization would produce incorrect results. A JIT cannot use compile-time type checking (option A) because type information only exists at runtime, and AOT is not invoked at runtime (option C)."

- question: "Why can a JIT-compiled language sometimes outperform ahead-of-time compiled C code for specific workloads?"
  type: multiple-choice
  options:
    - "JIT compilers use faster hardware than AOT compilers"
    - "JIT compilers skip register allocation to save compilation time"
    - "JIT can generate code specialized to the actual runtime types and hot paths, which AOT cannot know in advance"
    - "JIT-compiled languages are always more efficient because they eliminate all dead code"
  answer: 2
  explanation: "AOT compilers must generate conservative code that handles all possible inputs and paths — they cannot assume any runtime conditions. A JIT observes which paths are actually taken and what types are actually used, then generates code optimized for exactly those cases. This specialization can outperform AOT-compiled code for specific workloads. However, this advantage disappears when speculative assumptions are violated, and JITs pay overhead for profiling and compilation — so JIT does not uniformly outperform AOT."

- question: "A JIT compiler starts by executing code in an interpreter before compiling anything, which makes programs initially slower than AOT-compiled equivalents."
  type: true-false
  answer: true
  explanation: "This is a real tradeoff — interpretation is slower than compiled execution. Tiered JIT systems accept this startup penalty: code runs interpreted first (zero compilation cost), gets baseline-compiled when it warms up, and receives full optimization only when identified as hot. For long-running programs, the eventual compiled code more than compensates for the startup overhead. For short-running programs, JIT-compiled code may be slower overall than AOT-compiled code."

- question: "JIT compilation is essentially the same as ahead-of-time compilation, just performed later in the process."
  type: true-false
  answer: false
  explanation: "JIT compilation is fundamentally different from AOT because it has access to runtime information that AOT never has: profiling data on which code is hot, actual runtime types, observed branching patterns, and memory layout information. This allows JIT to perform speculative optimizations (inlining, type specialization) that are unsound for AOT. AOT must generate code correct for all possible inputs; JIT can speculate on observed behavior and add guards to catch violations. The timing difference is secondary — the information advantage is what makes JIT qualitatively different."

- question: "Explain why a JIT compiler needs to interact with the garbage collector, and what could go wrong if it did not."
  type: short-answer
  answer: "JIT-compiled code generates machine instructions that access object fields at specific byte offsets based on observed object structure. A compacting garbage collector may move objects in memory. If the GC does not inform the JIT about these moves, the compiled code will access stale memory addresses, causing crashes or incorrect results. The GC must know which memory locations in compiled code contain object references (via stack maps at safe points) so it can update them when objects are relocated."
  explanation: "This GC-JIT cooperation is a major source of architectural complexity in JIT systems. Safe points in compiled code mark places where the GC can pause execution, and the JIT must emit stack maps identifying which registers and stack slots hold live object references. This tight coupling between runtime compilation and memory management is part of what makes JIT systems architecturally complex compared to simple AOT compilers."
```

## Explainer

In a traditional ahead-of-time (AOT) compiler, the code generation phase you already know produces machine code once, before the program ever runs. The compiler must make conservative assumptions — it cannot know which functions will be called millions of times or what types a variable will actually hold. **Just-in-time compilation** flips this model: it defers code generation to runtime, where it can observe the program's actual behavior and generate code tailored to what is really happening.

A JIT system typically starts by interpreting bytecode or running lightly compiled code, profiling as it goes. It tracks **hot paths** — functions or loops that execute frequently — and identifies them as candidates for compilation. When a hot path is detected, the JIT compiler kicks in and generates optimized machine code specifically for that path. This is where the connection to code generation becomes concrete: the JIT performs the same instruction selection, register allocation, and scheduling you studied in code generation, but it does so at runtime with additional information the AOT compiler never had.

The key advantage is **specialization**. Consider a function that accepts arguments of any type. An AOT compiler must generate code that handles every possible type. A JIT can observe that the function is always called with integers, generate a fast integer-only version, and insert a **guard** — a lightweight check that the assumption still holds. If the guard fails (the function is suddenly called with a string), the JIT falls back to a slower generic path or recompiles. This speculative optimization is why JIT-compiled languages like Java and JavaScript can approach and sometimes exceed the performance of statically compiled C code for specific workloads.

The tradeoff is **compilation overhead at runtime**. Every moment spent compiling is a moment not spent executing the program. JIT systems manage this with tiered compilation: code starts interpreted (zero compilation cost), gets baseline-compiled when warm, and receives full optimization only when truly hot. The garbage collector — which you may know from its role in memory management — interacts closely with the JIT, since compiled code contains assumptions about object layouts that the GC must respect when moving objects in memory. This interplay between runtime compilation, profiling, and memory management is what makes JIT systems both powerful and architecturally complex.
