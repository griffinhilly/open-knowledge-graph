---
id: gradual-typing-systems
title: Gradual Typing and Mixed Static-Dynamic Types
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: type-inference-algorithms
  type: soft
tags:
- type-systems
- static
- dynamic
stage: advanced
status: draft
---

# Gradual Typing and Mixed Static-Dynamic Types

## Core Idea
Gradual typing blends static and dynamic typing, allowing programmers to omit type annotations where inference fails or dynamic behavior is needed. The compiler inserts runtime type checks where static types transition to 'any' or 'dynamic', enabling flexible development without abandoning static safety entirely.

## Explainer

From your study of type systems, you know the fundamental tradeoff: static typing catches errors at compile time and enables optimizations, while dynamic typing offers flexibility and faster prototyping. Historically, languages chose one side — Java and Haskell are statically typed, Python and Ruby are dynamically typed. **Gradual typing** rejects this binary choice by allowing both styles to coexist in the same program. A programmer can write fully annotated, statically checked code in critical modules and leave types unspecified in exploratory or rapidly changing code. TypeScript adding types to JavaScript, Python's type hints with mypy, and Typed Racket are all manifestations of this idea.

The mechanism that makes gradual typing work is the **dynamic type**, often written as `any` or `Dynamic`. This type is compatible with every other type — you can assign an `any` value to a `string` variable, or pass an `any` value where an `int` is expected, and the type checker will not complain. This is the escape hatch that preserves the flexibility of dynamic typing. But compatibility at compile time does not mean correctness at runtime. When a value flows from `any` into a statically typed context, the compiler (or runtime) inserts a **runtime type check** — a cast that verifies the value actually has the expected type. If you assigned a string to an `any` variable and then pass it where an integer is expected, the runtime check fails and raises a type error. These inserted checks are the **boundaries** between the static and dynamic worlds.

The theoretical foundation is the **consistency** relation, introduced by Jeremy Siek and Walid Taha. In a conventional static type system, types must be *equal* or in a *subtype* relationship to be compatible. Gradual typing relaxes this: two types are **consistent** if they are equal on all parts where they are both specified, and the `any` type is consistent with everything. `int` is consistent with `any`, and `any` is consistent with `string`, but `int` is not consistent with `string` — the dynamic type acts as a wildcard that matches anything, but two concrete types still must match each other. This ensures that fully annotated code gets the same static guarantees as a conventional statically typed language, while partially annotated code degrades gracefully.

A key challenge in gradual typing is the **blame problem**: when a runtime type check fails, which part of the code is at fault? If a function declared as `f(x: int) -> string` is called with an `any` value that turns out to be a float, the blame should fall on the caller who supplied the wrong type, not on the function definition. Gradual typing systems track blame across boundaries using **contracts** or **casts** that remember which side of the typed/untyped boundary introduced the value. This is not just an academic concern — clear blame tracking produces error messages that point to the actual source of the type mismatch rather than the symptom, which is critical for usability in large codebases where typed and untyped code are deeply interleaved.
