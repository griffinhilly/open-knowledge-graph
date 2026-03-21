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

## Questions

```yaml
- question: "A compiler is evaluating whether to inline a tiny 3-instruction getter function that is called from 800 different locations, most of them in initialization code that runs once at startup. What should the heuristic decide?"
  type: multiple-choice
  options:
    - "Inline it everywhere — tiny functions should always be inlined to eliminate call overhead"
    - "Do not inline — duplicating the function body 800 times bloats the binary without meaningful performance gain"
    - "Inline only the calls inside hot loops; leave the cold startup calls as-is"
    - "Inline it and then apply dead code elimination to remove the duplicates"
  answer: 2
  explanation: "A good heuristic considers both size and call frequency. This tiny function seems like a perfect inline candidate by size alone, but 800 cold call sites means 800 copies of the code in the binary — significant code bloat with almost no performance benefit, since initialization code runs once. Instruction cache pressure may actually worsen performance. A size-threshold-only heuristic would naively inline this; a frequency-aware heuristic would correctly decline. Option C (inline only hot loops) is actually the right approach in practice, but only option B correctly diagnoses the problem with naive blanket inlining."

- question: "What is the primary reason that inlining every function call in a program could make it run *slower* than selective inlining?"
  type: multiple-choice
  options:
    - "Inlined code cannot be optimized by the compiler since it loses its function structure"
    - "Code size explosion overwhelms the instruction cache, causing more cache misses"
    - "Inlining prevents the CPU from using branch prediction on the call sites"
    - "Inlined functions cannot be shared between threads, creating synchronization overhead"
  answer: 1
  explanation: "When every call is inlined, the binary grows massively — a function called from 50 sites gets duplicated 50 times. This bloated code no longer fits efficiently in the L1 instruction cache. The CPU must constantly fetch new instructions from slower memory, and the cache miss penalties dominate any savings from eliminated call overhead. This is the central tension in inlining: the optimization that eliminates overhead at one level can create worse overhead at another. Compilers must estimate the net effect, not just the call overhead eliminated."

- question: "A function that is very small (below the compiler's size threshold) should always be inlined, regardless of how frequently it is called."
  type: true-false
  answer: false
  explanation: "Size is only one signal. Call frequency matters equally — a tiny function called from 1,000 cold paths still creates 1,000 copies in the binary with minimal performance benefit. Good heuristics weight both size and call frequency (ideally from profiling data). Some compilers also consider whether inlining exposes constant arguments that would enable further optimizations. The `__attribute__((always_inline))` directive exists precisely because the compiler's size-based default sometimes gets it wrong — the compiler needs developer knowledge to override."

- question: "Profile-guided optimization (PGO) improves inlining decisions by revealing which call sites execute most frequently during representative program runs."
  type: true-false
  answer: true
  explanation: "PGO transforms inlining from static estimation to measurement. The compiler instruments the binary, a representative workload runs to collect call frequency data, and the second compilation uses that data to inline aggressively at hot call sites while leaving cold sites uninlined. This concentration of optimization effort on the 5% of call sites that account for 95% of execution time routinely produces 10–30% speedups in large applications. Static heuristics must guess at frequency; PGO measures it directly."

- question: "Why do production compilers use elaborate cost models rather than a simple size threshold when deciding whether to inline a function, and what factors beyond size matter most?"
  type: short-answer
  answer: "A size threshold alone ignores call frequency (a hot function is worth inlining even if medium-sized), cascading optimization benefit (inlining may expose constant arguments that enable further simplification), and code size impact on instruction cache. Production cost models weigh: the saved call overhead, the inlining-enabled optimization opportunities (constant propagation, dead code elimination), the code size increase, the instruction cache pressure from that growth, and whether profiling data identifies the call site as hot. The net benefit — not just the direct call savings — drives the decision."
  explanation: "The core insight is that inlining is a tradeoff, not a simple win. It trades call overhead for code size, and code size affects instruction cache performance which can be the dominant factor. A function that fits in 5 instructions when called normally becomes 50 instructions in 10 call sites after inlining — and if those 10 sites scatter across the code, the instruction cache locality degrades. Cascading benefit (inlining enabling further passes) can make a medium function worth inlining; lack of benefit makes even a tiny function potentially not worth the bloat."
```

## Explainer

From your study of procedure inlining and local optimization, you know that replacing a function call with the function's body eliminates call overhead (saving the return address, setting up a stack frame, jumping) and exposes the inlined code to further optimizations — constant folding, dead code elimination, and register allocation can now operate across what was previously an opaque call boundary. But inlining every call is disastrous: a function called from 50 sites would be duplicated 50 times, bloating the binary, overwhelming the instruction cache, and potentially making the program *slower*. **Inlining heuristics** are the decision rules that determine which calls to inline and which to leave as calls.

The simplest heuristic is a **size threshold**: inline functions smaller than *N* instructions. Tiny functions — getters, setters, wrappers that add one argument and delegate — are almost always worth inlining because the call overhead exceeds the code they contain, and the duplicated code is negligible. But a size threshold alone misses the point. A medium-sized function called once in a hot loop is an excellent inlining candidate, while a tiny function called from a thousand cold paths may not be worth the code bloat. Good heuristics combine multiple signals: function size, estimated call frequency (from static analysis or profiling data), the depth of the call chain (to avoid recursive blowup), and whether the call site passes constants that would enable further optimization after inlining.

**Profile-guided optimization** (PGO) transforms inlining from guesswork into measurement. The compiler first instruments the program to record how often each call site executes during a representative run. On the second compilation, it uses that profile data to focus inlining on the hot paths — the 5% of call sites that account for 95% of execution time. A function called millions of times per second in an inner loop gets inlined; the same function called once during startup does not. PGO-driven inlining routinely produces 10-30% speedups in large applications because it concentrates optimization effort exactly where it matters.

The subtlest aspect is **cascading benefit**: inlining one function may expose a constant argument that, after constant propagation, makes a second function trivially small and worth inlining in turn. Compilers handle this through iterative inlining passes, but each round risks further code growth. Production compilers like LLVM and GCC use elaborate cost models that estimate the net effect of inlining — weighing the saved call overhead and the optimization opportunities against the code size increase and its impact on instruction cache pressure. The heuristic is never perfect, which is why compiler flags like `-finline-limit` and `__attribute__((always_inline))` exist: they let developers override the heuristic when they know something the compiler does not.
