---
id: inlining-heuristics
title: Inlining Heuristics and Decision Making
domain: computer-science
course: compilers
prerequisites:
- id: procedure-inlining-optimization
  type: hard
- id: local-optimization-techniques
  type: hard
tags:
- optimization
- inlining
- heuristics
stage: advanced
status: draft
---

# Inlining Heuristics and Decision Making

## Core Idea
Inlining replaces function calls with function bodies, eliminating call overhead but risking code explosion. Heuristics estimate call frequency, function size, and cascading benefit to decide when inlining improves net performance, often using profiling data to guide decisions.

## How It's Best Learned
Examine compiler inlining decisions via -fopt-info in GCC or llvm-opt-report; compare code size and performance with and without inlining enabled.

## Explainer

From your study of procedure inlining and local optimization, you know that replacing a function call with the function's body eliminates call overhead (saving the return address, setting up a stack frame, jumping) and exposes the inlined code to further optimizations — constant folding, dead code elimination, and register allocation can now operate across what was previously an opaque call boundary. But inlining every call is disastrous: a function called from 50 sites would be duplicated 50 times, bloating the binary, overwhelming the instruction cache, and potentially making the program *slower*. **Inlining heuristics** are the decision rules that determine which calls to inline and which to leave as calls.

The simplest heuristic is a **size threshold**: inline functions smaller than *N* instructions. Tiny functions — getters, setters, wrappers that add one argument and delegate — are almost always worth inlining because the call overhead exceeds the code they contain, and the duplicated code is negligible. But a size threshold alone misses the point. A medium-sized function called once in a hot loop is an excellent inlining candidate, while a tiny function called from a thousand cold paths may not be worth the code bloat. Good heuristics combine multiple signals: function size, estimated call frequency (from static analysis or profiling data), the depth of the call chain (to avoid recursive blowup), and whether the call site passes constants that would enable further optimization after inlining.

**Profile-guided optimization** (PGO) transforms inlining from guesswork into measurement. The compiler first instruments the program to record how often each call site executes during a representative run. On the second compilation, it uses that profile data to focus inlining on the hot paths — the 5% of call sites that account for 95% of execution time. A function called millions of times per second in an inner loop gets inlined; the same function called once during startup does not. PGO-driven inlining routinely produces 10-30% speedups in large applications because it concentrates optimization effort exactly where it matters.

The subtlest aspect is **cascading benefit**: inlining one function may expose a constant argument that, after constant propagation, makes a second function trivially small and worth inlining in turn. Compilers handle this through iterative inlining passes, but each round risks further code growth. Production compilers like LLVM and GCC use elaborate cost models that estimate the net effect of inlining — weighing the saved call overhead and the optimization opportunities against the code size increase and its impact on instruction cache pressure. The heuristic is never perfect, which is why compiler flags like `-finline-limit` and `__attribute__((always_inline))` exist: they let developers override the heuristic when they know something the compiler does not.
