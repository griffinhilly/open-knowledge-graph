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
status: validated
---

# Generics and Template Specialization

## Core Idea
Generic types and functions are parameterized by type variables and must be monomorphized (specialized) to concrete types for execution. Template instantiation generates type-specific code for each use; monomorphization creates multiple copies, increasing code size but enabling optimization. Languages like C++ use templates; languages like Java use erasure (runtime type information is discarded).

## Questions

```yaml
- question: "A Rust program calls a generic sort function with 15 different concrete types. A Java program calls a generic sort function with the same 15 types. How do the compiled outputs differ?"
  type: multiple-choice
  options:
    - "Both produce 15 specialized copies — Rust and Java both use monomorphization"
    - "Rust produces 15 specialized copies; Java produces one shared version using type erasure"
    - "Java produces 15 specialized copies; Rust produces one shared version via dictionary passing"
    - "Both produce a single shared version — modern compilers always prefer smaller binaries"
  answer: 1
  explanation: "Rust uses monomorphization: the compiler generates a distinct, fully specialized function for each concrete type, so calling sort with 15 types produces 15 copies of the function in the binary, each optimized for its specific type. Java uses type erasure: the generic sort method compiles to a single bytecode implementation operating on Object references, with type casts inserted at boundaries. The Rust binary will be larger but faster (no boxing, no virtual dispatch); the Java binary will be smaller but pays the cost of indirection and boxing for primitive types."

- question: "What is the core performance advantage of monomorphization over type erasure?"
  type: multiple-choice
  options:
    - "Monomorphization allows faster compilation because types are resolved earlier"
    - "Monomorphization produces type-specific code that the optimizer can inline, vectorize, and constant-fold without indirection"
    - "Monomorphization eliminates the need for garbage collection, reducing runtime overhead"
    - "Monomorphization shares code between instantiations, reducing instruction cache pressure"
  answer: 1
  explanation: "When a generic function is monomorphized for a specific type, the resulting code is identical to what you would have written by hand for that type. The optimizer has full knowledge of the concrete types involved and can eliminate virtual dispatch, inline function calls, vectorize loops over known-size data, and constant-fold type-specific computations. Type erasure sacrifices all of this: every operation goes through object references, primitives must be boxed into heap objects, and the optimizer cannot specialize based on type. The tradeoff is that monomorphization can inflate binary size when a generic is used with many types."

- question: "Type erasure is always slower than monomorphization because it discards all type information, leaving the runtime unable to perform any type-specific optimizations."
  type: true-false
  answer: false
  explanation: "Type erasure discards generic type *parameters* at runtime, but compilers using erasure still perform type-checking at compile time and insert explicit type casts. The performance cost of erasure comes from indirection (operating on object references rather than direct values) and boxing (wrapping primitives in heap objects), not from total loss of optimization opportunity. JIT compilers (like the JVM's HotSpot) can still perform runtime optimizations such as method inlining based on observed types. The claim that 'all type information is lost' conflates the erasure of generic parameters with the loss of all type knowledge."

- question: "In a language that uses type erasure for generics, a List<Integer> and a List<String> share the same compiled bytecode at runtime."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of type erasure. In Java, `List<Integer>` and `List<String>` are identical at the bytecode level — both are just `List` operating on `Object` references. The generic type parameter exists only in the source code for compile-time type checking; by the time the code runs on the JVM, the type parameter has been erased. This is why you cannot, for example, write `new T()` in a Java generic method — the runtime doesn't know what T is."

- question: "Explain the core tradeoff between monomorphization and type erasure in terms of runtime performance and binary size."
  type: short-answer
  answer: "Monomorphization generates a separate, fully specialized copy of the generic code for each concrete type used. This enables zero-cost abstraction — the compiler can optimize each copy as if it were hand-written for that type — but multiplies code size with every new type instantiation, potentially bloating the binary and pressuring instruction caches. Type erasure produces a single shared implementation operating on a uniform representation (typically object references), keeping binary size small regardless of how many types are used, but at the cost of indirection, boxing of primitives, and loss of type-specific optimization opportunities. The choice encodes a tradeoff between 'fast at runtime' and 'small in memory.'"
  explanation: "Neither approach is universally better — the right choice depends on the language's goals and typical use cases. Systems languages (Rust, C++) favor monomorphization because performance is paramount and generics are often used with a small, fixed set of types. Application languages (Java, C#) favor erasure or hybrid approaches because developer productivity, binary size, and startup time matter more than peak throughput. Modern languages like Swift and C# explore intermediate strategies (specialization for critical types, sharing for others) to capture benefits of both."
```

## Explainer

You already understand parametric polymorphism — the idea that a function or type can be written once and work with any type that satisfies its constraints. `fn swap<T>(a: T, b: T)` works for integers, strings, or custom structs. But source code generality must eventually become machine code specificity: the CPU executes concrete instructions on concrete data. The compiler must decide how to translate that single generic definition into executable code, and this decision has profound consequences for performance, code size, and runtime behavior.

**Monomorphization** is the most straightforward strategy. The compiler generates a separate, fully specialized copy of the generic function or type for each concrete type it is used with. If your code calls `swap<i32>` and `swap<String>`, the compiler emits two distinct functions — one operating on 32-bit integers, one on heap-allocated strings — each with its own optimized machine code. This is how C++ templates and Rust generics work. The advantage is zero-cost abstraction: the specialized code is identical to what you would have written by hand for each type, and the optimizer can inline, vectorize, and constant-fold with full type knowledge. The cost is **code bloat** — if a generic is instantiated with 20 different types, you get 20 copies of the code, which can inflate binary size and pressure instruction caches.

**Type erasure** takes the opposite approach. Instead of generating specialized copies, the compiler produces a single version of the generic code that operates on a uniform representation — typically object references or pointers. Java generics work this way: `List<Integer>` and `List<String>` share the same bytecode at runtime, with the generic type parameter erased to `Object`. The compiler inserts type casts at boundaries to maintain type safety. This keeps code size small and compilation fast, but sacrifices performance: every operation goes through indirection, primitive types must be boxed into objects, and the optimizer cannot exploit type-specific knowledge.

Modern language implementations explore a spectrum between these extremes. Some compilers monomorphize "hot" instantiations that benefit from specialization while sharing code for less performance-critical ones. Others use **dictionary passing**, where a generic function receives a table of type-specific operations as an extra argument at runtime — this avoids code duplication while keeping type information available. The compiler's choice of strategy shapes the trade-off triangle between runtime performance, binary size, and compilation speed, and understanding these strategies is essential for both language designers choosing a generics model and systems programmers reasoning about the cost of abstraction.
