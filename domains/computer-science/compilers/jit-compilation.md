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
