---
id: vectorization-and-simd
title: Vectorization and SIMD Code Generation
domain: computer-science
course: compilers
prerequisites:
- id: code-optimization
  type: hard
- id: dataflow-analysis
  type: hard
builds-toward:
- target-specific-code-generation
tags:
- optimization
- SIMD
- parallelism
stage: advanced
status: draft
---

# Vectorization and SIMD Code Generation

## Core Idea
Vectorization transforms scalar loops into SIMD code that processes multiple data elements in parallel using vector instructions. The compiler identifies data-parallel loops, verifies absence of cross-iteration dependencies via dependence analysis, and generates packed instructions exploiting modern CPU vector units.

## How It's Best Learned
Write a loop that processes array elements independently, run it through a modern compiler with vectorization enabled, and examine generated SIMD instructions.

## Questions

```yaml
- question: "A compiler refuses to vectorize the loop: `for (i=1; i<n; i++) A[i] = A[i-1] * 2;`. The most accurate explanation is:"
  type: multiple-choice
  options:
    - "The loop body is too complex for the SIMD vectorization pass to analyze"
    - "There is a loop-carried dependency: iteration i reads the value written by iteration i-1, so parallel execution would produce wrong results"
    - "The array is too small — vectorization is only beneficial for large arrays"
    - "The multiplication operation is not supported on this CPU's SIMD unit"
  answer: 1
  explanation: "This loop has a loop-carried dependency: A[i] depends on A[i-1], which was written by the previous iteration. If you executed iterations 1 and 2 simultaneously, iteration 2 might read the original (pre-loop) value of A[1] instead of the value just written by iteration 1, producing wrong results. The compiler's dependence analysis detects this and rightly refuses vectorization — correctness always overrides performance. A simple independent loop like `A[i] = B[i] * 2` (no cross-iteration dependencies) would vectorize freely."

- question: "A loop processes 1,007 elements using AVX (256-bit registers, 8 floats per register). How does the compiler handle the elements that don't fit evenly into the SIMD width?"
  type: multiple-choice
  options:
    - "It rounds down to 1,000 elements and skips the last 7 to keep the loop simple"
    - "It pads the array allocation to 1,008 elements so the count is a multiple of 8"
    - "It generates a scalar remainder loop that processes the last 7 elements after 125 full vector iterations"
    - "It refuses to vectorize because the element count must be a compile-time constant divisible by 8"
  answer: 2
  explanation: "The compiler generates a vectorized main loop covering ⌊1007/8⌋ = 125 iterations (processing elements 0–999), then a scalar remainder loop for the last 7 elements (1000–1006). This is a standard compiler strategy — the remainder loop is a simple scalar fallback, not a failure. Some compilers can also generate 'peeled' prologue iterations to align the main loop on memory boundaries before the vectorized portion. The compiler never silently skips elements or refuses on this basis."

- question: "Even when a loop has a loop-carried dependency (such as summing all elements of an array), a compiler may still be able to vectorize it by using multiple partial accumulators in separate vector lanes."
  type: true-false
  answer: true
  explanation: "A reduction like `sum += A[i]` has a loop-carried dependency on `sum`, but the compiler can break it by using multiple independent partial sums — say, 8 separate accumulators in one AVX register, each accumulating every 8th element. After the vectorized loop, a horizontal add combines the 8 partial sums into the final result. This transforms a loop-carried dependency on a scalar into a dependency only on the final reduction step, which can be done once outside the loop. The compiler must prove associativity (floating-point reductions require `-ffast-math` or equivalent)."

- question: "When a compiler cannot prove that two pointer arguments do not alias (point to overlapping memory), it will always refuse to vectorize any loop involving those pointers."
  type: true-false
  answer: false
  explanation: "Rather than refusing outright, the compiler can generate a runtime alias check: it emits code that compares the pointer ranges at runtime and branches to either the vectorized or scalar version depending on whether they overlap. This produces a function that is correct in all cases while still achieving speedup in the common non-aliasing case. The programmer can also help by annotating pointers with `restrict` (C99), explicitly asserting no aliasing and allowing the compiler to skip the runtime check and always use the vectorized path."

- question: "Why is proving absence of loop-carried dependencies the critical prerequisite for vectorization, and what can programmers do to help the compiler vectorize loops it would otherwise reject?"
  type: short-answer
  answer: "Vectorization executes multiple loop iterations simultaneously, so if iteration i writes a value that iteration i+k reads, the parallel execution produces wrong results — the read may see a stale or partially-updated value. Correctness is non-negotiable, so the compiler only vectorizes when it can prove no such cross-iteration dependencies exist. Programmers can help by: (1) using `restrict` on pointer parameters to assert non-aliasing; (2) avoiding writes to arrays that are also read with different indices in the same loop; (3) separating computations into independent loops the compiler can analyze more easily; (4) using `#pragma GCC ivdep` or similar to manually assert to the compiler that no dependencies exist when the programmer knows this to be true; and (5) using compiler reports (-fopt-info-vec on GCC) to understand why specific loops aren't vectorizing."
  explanation: "The key insight is that a loop fails to vectorize because the compiler couldn't prove safety, not necessarily because vectorization is impossible. Programmers who understand dependence analysis can provide the information the compiler lacks — either through annotations like `restrict`, through code restructuring, or through manual SIMD intrinsics as a last resort."
```

## Explainer

You know from your work on code optimization that compilers transform programs to run faster while preserving their meaning, and from dataflow analysis that compilers can track how values flow through a program to identify optimization opportunities. **Vectorization** applies both ideas to a specific goal: finding loops where each iteration does the same operation on different data, then replacing many scalar iterations with fewer vector instructions that process multiple data elements simultaneously.

Consider a loop that adds corresponding elements of two arrays: `for (i = 0; i < 1000; i++) C[i] = A[i] + B[i]`. A scalar processor executes 1,000 separate additions. But modern CPUs have **SIMD** (Single Instruction, Multiple Data) units — hardware that can load, say, 8 floats at once into a wide register and add all 8 pairs in a single instruction. If the compiler vectorizes this loop, it executes only 125 iterations, each processing 8 elements. The speedup is nearly 8x for this simple case, with no change to the source code.

The compiler's vectorization pass must answer a critical question: **is it safe to process multiple iterations simultaneously?** This is where dataflow and dependence analysis earn their keep. If iteration i writes to a location that iteration i+2 reads, executing them in parallel would produce wrong results — the read might see a stale value. The compiler builds a **dependence graph** across loop iterations and checks for cross-iteration dependencies that would prevent parallel execution. Independent iterations (no loop-carried dependencies) are safe to vectorize. Some dependencies can be worked around — for instance, a reduction like summing an array has a loop-carried dependency on the accumulator, but the compiler can use multiple partial sums in separate vector lanes and combine them at the end.

Practical vectorization involves several mechanical steps. The compiler determines the **vector width** (how many elements fit in one SIMD register — typically 4 for 32-bit floats on 128-bit SSE, 8 on 256-bit AVX). It checks that memory accesses are **aligned** and **contiguous** — loading scattered elements into a vector register is much slower than loading a consecutive block. It handles the **remainder loop** for when the trip count isn't a multiple of the vector width (the last few iterations run as scalar code). It also must ensure that no aliasing exists — if pointers A and C might point to overlapping memory, the compiler either proves they don't overlap or generates both vectorized and scalar versions with a runtime check. Understanding these constraints explains why seemingly simple loops sometimes fail to vectorize: the compiler couldn't prove safety, not that the optimization was impossible.
