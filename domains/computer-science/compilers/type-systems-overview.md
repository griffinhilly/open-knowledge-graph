---
id: type-systems-overview
title: Type Systems Overview
domain: computer-science
course: compilers
prerequisites:
- id: semantic-analysis
  type: hard
- id: primitive-data-types
  type: soft
builds-toward:
- type-inference-algorithms
- hindley-milner-type-system
- polymorphism-and-type-variables
tags:
- type-systems
- type-checking
- language-design
stage: advanced
status: validated
---

# Type Systems Overview

## Core Idea
A type system assigns types to expressions and enforces type compatibility. Static type systems check types at compile-time, preventing type errors before runtime. Strongly-typed languages reject invalid operations; weakly-typed languages attempt coercions. Type systems vary in expressiveness: simple (int, float, bool), composite (structs, classes), and advanced (generics, dependent types).

## Questions

```yaml
- question: "Which of the following correctly describes the relationship between static/dynamic typing and strong/weak typing?"
  type: multiple-choice
  options:
    - "Static typing always implies strong typing; dynamic typing always implies weak typing."
    - "They are orthogonal dimensions — a language can be any combination of the two."
    - "Strongly-typed languages must check types at compile time."
    - "Dynamic typing means the language does not have types at all."
  answer: 1
  explanation: "Static/dynamic describes *when* types are checked (compile-time vs. runtime). Strong/weak describes *how strictly* type mismatches are handled (rejection vs. coercion). Python is dynamically but strongly typed — it checks at runtime and refuses `'hello' + 5`. C is statically but weakly typed — it checks at compile time but permits many implicit pointer/integer coercions."

- question: "A statically-typed language guarantees there will be no type errors at runtime."
  type: true-false
  answer: false
  explanation: "Static typing eliminates many type errors at compile time, but not all. Downcasts, null pointer dereferences, and unchecked array accesses are type-related runtime failures that slip past static checkers. A sound type system (like Haskell's) gives stronger guarantees, but most mainstream static type systems are intentionally unsound to allow useful patterns."

- question: "Why is a type system described as improving program correctness rather than just documentation?"
  type: short-answer
  answer: "A type system actively enforces constraints — the compiler or runtime rejects programs that violate them. Unlike comments or annotations, types are checked mechanically, so they catch real bugs (e.g., passing a string where an integer is expected) before the code runs. They serve as machine-verified specifications."
  explanation: "Types are often presented as documentation, but their real value is enforcement. When semantic analysis (the prerequisite) resolves names and scopes, the type checker then verifies that every operation is applied to compatible types. This catches a whole class of logical bugs at the earliest possible stage."
```

## Explainer

After semantic analysis assigns meaning to identifiers and scopes, a compiler's type checker asks the next question: does every operation make sense for the kinds of values involved? This is what a type system formalizes. A type is a set of values with associated operations — `int` is a set of integers you can add and multiply; `string` is a sequence of characters you can concatenate. The type system's job is to ensure you never accidentally mix them up.

The most important distinction to internalize is that static vs. dynamic typing and strong vs. weak typing are two separate axes, not a single spectrum. **Static typing** means the type of every expression is known at compile time; the compiler rejects the program if types are incompatible. **Dynamic typing** means types are attached to values at runtime and checked when operations execute. These are independent of whether the language is **strongly typed** (refuses to coerce mismatched types, like Python rejecting `1 + "hello"`) or **weakly typed** (attempts implicit conversion, like JavaScript silently computing `1 + "hello"` as `"1hello"`). Java is static and strong. Python is dynamic and strong. C is static and weak. JavaScript is dynamic and weak.

Type systems also vary in what they can express. Simple types — `int`, `float`, `bool` — let you describe basic values. Composite types — structs, classes, tuples — let you bundle values together. Polymorphic or generic types (like `List<T>`) let you write code that works for any type T without sacrificing type safety. More advanced systems (dependent types, linear types) can encode program invariants like "this array has exactly n elements" directly in the type, letting the compiler verify properties that would otherwise require runtime checks or manual proof.

From the compiler's perspective, the type system operates during semantic analysis. After parsing produces an AST and name resolution links identifiers to their declarations, the type checker annotates each AST node with a type, then verifies that every operator's arguments match its expected types. When a type error is found, the compiler reports it with a source location rather than crashing at runtime. This is why type errors are considered a *compile-time* benefit of static languages.

Understanding type systems is the foundation for more advanced topics: type inference (having the compiler deduce types you didn't write), parametric polymorphism (generic functions that remain type-safe), and eventually dependent or refinement types. Each of these extends the basic idea — that a type is a formal constraint on what values an expression can hold — into more expressive territory.

## Notes

- The static/dynamic and strong/weak axes come from Benjamin Pierce's taxonomy in *Types and Programming Languages*.
- "Soundness" is the formal property that well-typed programs don't produce type errors at runtime; most real-world type systems are intentionally unsound (e.g., Java's array covariance, TypeScript's `any`).
