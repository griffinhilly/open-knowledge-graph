---
id: generics-and-specialization
title: Generics and Template Specialization
domain: computer-science
course: compilers
prerequisites:
- id: polymorphism-parametric
  type: hard
tags:
- generics
- templates
- code-generation
stage: advanced
status: draft
---

# Generics and Template Specialization

## Core Idea
Generic types and functions are parameterized by type variables and must be monomorphized (specialized) to concrete types for execution. Template instantiation generates type-specific code for each use; monomorphization creates multiple copies, increasing code size but enabling optimization. Languages like C++ use templates; languages like Java use erasure (runtime type information is discarded).

## Explainer

You already understand parametric polymorphism — the idea that a function or type can be written once and work with any type that satisfies its constraints. `fn swap<T>(a: T, b: T)` works for integers, strings, or custom structs. But source code generality must eventually become machine code specificity: the CPU executes concrete instructions on concrete data. The compiler must decide how to translate that single generic definition into executable code, and this decision has profound consequences for performance, code size, and runtime behavior.

**Monomorphization** is the most straightforward strategy. The compiler generates a separate, fully specialized copy of the generic function or type for each concrete type it is used with. If your code calls `swap<i32>` and `swap<String>`, the compiler emits two distinct functions — one operating on 32-bit integers, one on heap-allocated strings — each with its own optimized machine code. This is how C++ templates and Rust generics work. The advantage is zero-cost abstraction: the specialized code is identical to what you would have written by hand for each type, and the optimizer can inline, vectorize, and constant-fold with full type knowledge. The cost is **code bloat** — if a generic is instantiated with 20 different types, you get 20 copies of the code, which can inflate binary size and pressure instruction caches.

**Type erasure** takes the opposite approach. Instead of generating specialized copies, the compiler produces a single version of the generic code that operates on a uniform representation — typically object references or pointers. Java generics work this way: `List<Integer>` and `List<String>` share the same bytecode at runtime, with the generic type parameter erased to `Object`. The compiler inserts type casts at boundaries to maintain type safety. This keeps code size small and compilation fast, but sacrifices performance: every operation goes through indirection, primitive types must be boxed into objects, and the optimizer cannot exploit type-specific knowledge.

Modern language implementations explore a spectrum between these extremes. Some compilers monomorphize "hot" instantiations that benefit from specialization while sharing code for less performance-critical ones. Others use **dictionary passing**, where a generic function receives a table of type-specific operations as an extra argument at runtime — this avoids code duplication while keeping type information available. The compiler's choice of strategy shapes the trade-off triangle between runtime performance, binary size, and compilation speed, and understanding these strategies is essential for both language designers choosing a generics model and systems programmers reasoning about the cost of abstraction.
