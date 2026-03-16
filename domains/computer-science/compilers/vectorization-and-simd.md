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

## Explainer

You know from your work on code optimization that compilers transform programs to run faster while preserving their meaning, and from dataflow analysis that compilers can track how values flow through a program to identify optimization opportunities. **Vectorization** applies both ideas to a specific goal: finding loops where each iteration does the same operation on different data, then replacing many scalar iterations with fewer vector instructions that process multiple data elements simultaneously.

Consider a loop that adds corresponding elements of two arrays: `for (i = 0; i < 1000; i++) C[i] = A[i] + B[i]`. A scalar processor executes 1,000 separate additions. But modern CPUs have **SIMD** (Single Instruction, Multiple Data) units — hardware that can load, say, 8 floats at once into a wide register and add all 8 pairs in a single instruction. If the compiler vectorizes this loop, it executes only 125 iterations, each processing 8 elements. The speedup is nearly 8x for this simple case, with no change to the source code.

The compiler's vectorization pass must answer a critical question: **is it safe to process multiple iterations simultaneously?** This is where dataflow and dependence analysis earn their keep. If iteration i writes to a location that iteration i+2 reads, executing them in parallel would produce wrong results — the read might see a stale value. The compiler builds a **dependence graph** across loop iterations and checks for cross-iteration dependencies that would prevent parallel execution. Independent iterations (no loop-carried dependencies) are safe to vectorize. Some dependencies can be worked around — for instance, a reduction like summing an array has a loop-carried dependency on the accumulator, but the compiler can use multiple partial sums in separate vector lanes and combine them at the end.

Practical vectorization involves several mechanical steps. The compiler determines the **vector width** (how many elements fit in one SIMD register — typically 4 for 32-bit floats on 128-bit SSE, 8 on 256-bit AVX). It checks that memory accesses are **aligned** and **contiguous** — loading scattered elements into a vector register is much slower than loading a consecutive block. It handles the **remainder loop** for when the trip count isn't a multiple of the vector width (the last few iterations run as scalar code). It also must ensure that no aliasing exists — if pointers A and C might point to overlapping memory, the compiler either proves they don't overlap or generates both vectorized and scalar versions with a runtime check. Understanding these constraints explains why seemingly simple loops sometimes fail to vectorize: the compiler couldn't prove safety, not that the optimization was impossible.
