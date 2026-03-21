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

## Questions

```yaml
- question: "A type checker encounters the expression `λx. x + 1` in isolation. A pure type inference system cannot assign it a type. Under bidirectional type checking, what makes it possible to type this expression?"
  type: multiple-choice
  options:
    - "The checker automatically infers the most general polymorphic type for the lambda"
    - "An expected type propagated from surrounding context switches the checker to checking mode, pushing the parameter type inward"
    - "The checker decomposes the lambda and infers each subexpression's type independently"
    - "The compiler inserts a default type annotation when the programmer omits one"
  answer: 1
  explanation: "In synthesis (inference) mode, `λx. x + 1` cannot assign a type to `x` — the inference gets stuck. But if surrounding context provides an expected type like `Int → Int`, the checker switches to checking mode: the expected input type `Int` is pushed inward and assigned to `x`, then the body `x + 1` is verified against the output type `Int`. This direction-switching is the core mechanism of bidirectional checking — type information from annotations flows inward via checking mode to resolve expressions that synthesis mode cannot type alone."

- question: "Bidirectional type checking produces better error messages than pure Hindley-Milner type inference primarily because:"
  type: multiple-choice
  options:
    - "It uses a more powerful constraint solver that catches more errors"
    - "It always requires explicit annotations, so errors are always at annotated sites"
    - "Errors are reported at the exact subexpression where the actual type conflicts with the locally expected type, rather than where two distant constraints collide during unification"
    - "It checks each expression twice — once in each direction — catching errors earlier in compilation"
  answer: 2
  explanation: "In pure Hindley-Milner, the unification engine accumulates constraints globally and may only discover a conflict far from its source — reporting an error in a function call when the real mistake was in a type annotation several scopes up. Bidirectional checking localizes errors because it always carries an expected type into checking mode: if you check `\"hello\"` against `Int`, the error points directly at `\"hello\"` and says it is not an `Int`. The expected type flows inward and catches mismatches at the exact subexpression, not at a distant indirect consequence."

- question: "In bidirectional type checking, synthesis mode and checking mode are mutually exclusive — a given type checker uses one or the other throughout a program, not both."
  type: true-false
  answer: false
  explanation: "False. Bidirectional type checking works by dynamically switching between synthesis and checking modes during a single pass over the program. A function application might synthesize the function's type, then switch to checking mode for each argument. A let-binding with an annotation switches to checking mode for the bound expression. The two modes are complementary and interdependent — this is the 'bidirectional' in the name. Forcing everything into one mode either loses information (pure checking with insufficient annotations) or becomes computationally expensive (pure inference with constraint solving)."

- question: "A lambda expression like `λx. x + 1` can be successfully type-checked in checking mode if the surrounding context provides an expected function type, even without an explicit annotation on the parameter `x`."
  type: true-false
  answer: true
  explanation: "True. This is the canonical use case for checking mode. When an expected type like `Int → Int` is pushed into the lambda, the checker extracts the input type `Int` and adds `x : Int` to the local type environment. The body `x + 1` can then be verified against the output type `Int`. No explicit annotation on `x` is needed — the type information flows inward from the context. This is the practical value of bidirectional checking: reducing annotation burden while still typing expressions that pure inference cannot handle."

- question: "Explain the difference between synthesis mode and checking mode in bidirectional type checking, and give an example of why each mode is needed."
  type: short-answer
  answer: "Synthesis mode produces a type from an expression — information flows out. It is used when the expression determines its own type, such as a variable (look up in context) or an integer literal. Checking mode verifies an expression against a supplied expected type — information flows in. It is used when the expression's structure does not determine a unique type, such as a lambda whose parameter type is unknown until the expected function type is provided. Both modes are necessary because different language constructs have different information-flow directions."
  explanation: "Pure inference (synthesis-only) tries to discover every type from scratch. For complex type systems this requires solving constraint systems globally, which is expensive and yields poor error messages. Pure checking (annotations everywhere) is correct but tedious. Bidirectional checking exploits each construct's natural information flow: function type annotations and let-binding signatures seed type information that flows inward through checking mode, while simple terms like variables, literals, and applications generate types upward through synthesis mode. The interaction propagates types efficiently and localizes errors naturally."
```

## Explainer

If you have studied type systems, you know the basic question: given an expression and a type environment, does this expression have a valid type? Pure **type inference** (as in Hindley-Milner) answers this by discovering the type from scratch — it examines the expression, generates constraints, and solves them. Pure **type checking** goes the other direction: you are given a type and verify that the expression conforms. **Bidirectional type checking** combines both modes, switching between them strategically to get the best of each.

The two modes are called **synthesis** (inference) and **checking**. In synthesis mode, the algorithm examines an expression and produces its type — information flows *out* of the expression. Variables synthesize their type from the environment, and function application synthesizes a return type from the function's known type. In checking mode, the algorithm receives an expected type and verifies the expression against it — information flows *into* the expression. Lambda abstractions are the classic example: `λx. x + 1` cannot synthesize a type on its own (what type is `x`?), but if you *check* it against `Int → Int`, the parameter type `Int` is pushed inward, and the body `x + 1` can then be verified.

The key insight is that type annotations at strategic points create "seeds" of type information that propagate through the program. When you write `let f: Int → Int = λx. x + 1`, the annotation `Int → Int` lets the checker switch into checking mode for the lambda body. Without bidirectional checking, a pure inference system would need to either require annotations everywhere (tedious) or solve complex constraint systems globally (expensive, with poor error messages). Bidirectional checking finds a practical middle ground: annotate function signatures, and the rest flows naturally.

This design also produces dramatically better error messages. In pure Hindley-Milner inference, a type mismatch might be reported far from its actual cause, because the unification engine only discovers the conflict when two distant constraints collide. In bidirectional checking, errors are localized: if you check `"hello"` against `Int`, the error points directly at `"hello"` and says it is not an `Int`. Modern languages including Rust, Swift, Kotlin, and recent versions of TypeScript all use bidirectional type checking. The pattern scales naturally to advanced features like generics, dependent types, and type-level computation, which is why it has become the dominant approach in practical type system implementation.
