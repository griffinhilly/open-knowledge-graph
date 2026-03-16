---
id: type-checking-bidirectional
title: Bidirectional Type Checking
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: hindley-milner-type-system
  type: soft
builds-toward:
- polymorphism-and-type-variables
tags:
- type-checking
- type-inference
stage: advanced
status: draft
---

# Bidirectional Type Checking

## Core Idea
Bidirectional type checking works in two modes: checking (verifying an expression has an expected type) and inference (discovering a term's type). This approach is more efficient than pure inference and handles more complex type systems. Many modern languages use bidirectional checking.

## How It's Best Learned
Implement a bidirectional type checker for a language with polymorphism. Compare performance and error messages with unidirectional approaches.

## Common Misconceptions
Type checking and inference are opposite processes (they are complementary modes). Bidirectional checking is only for functional languages (many imperative and systems languages use it).

## Explainer

If you have studied type systems, you know the basic question: given an expression and a type environment, does this expression have a valid type? Pure **type inference** (as in Hindley-Milner) answers this by discovering the type from scratch — it examines the expression, generates constraints, and solves them. Pure **type checking** goes the other direction: you are given a type and verify that the expression conforms. **Bidirectional type checking** combines both modes, switching between them strategically to get the best of each.

The two modes are called **synthesis** (inference) and **checking**. In synthesis mode, the algorithm examines an expression and produces its type — information flows *out* of the expression. Variables synthesize their type from the environment, and function application synthesizes a return type from the function's known type. In checking mode, the algorithm receives an expected type and verifies the expression against it — information flows *into* the expression. Lambda abstractions are the classic example: `λx. x + 1` cannot synthesize a type on its own (what type is `x`?), but if you *check* it against `Int → Int`, the parameter type `Int` is pushed inward, and the body `x + 1` can then be verified.

The key insight is that type annotations at strategic points create "seeds" of type information that propagate through the program. When you write `let f: Int → Int = λx. x + 1`, the annotation `Int → Int` lets the checker switch into checking mode for the lambda body. Without bidirectional checking, a pure inference system would need to either require annotations everywhere (tedious) or solve complex constraint systems globally (expensive, with poor error messages). Bidirectional checking finds a practical middle ground: annotate function signatures, and the rest flows naturally.

This design also produces dramatically better error messages. In pure Hindley-Milner inference, a type mismatch might be reported far from its actual cause, because the unification engine only discovers the conflict when two distant constraints collide. In bidirectional checking, errors are localized: if you check `"hello"` against `Int`, the error points directly at `"hello"` and says it is not an `Int`. Modern languages including Rust, Swift, Kotlin, and recent versions of TypeScript all use bidirectional type checking. The pattern scales naturally to advanced features like generics, dependent types, and type-level computation, which is why it has become the dominant approach in practical type system implementation.
