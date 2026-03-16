---
id: polymorphism-and-type-variables
title: Polymorphism and Type Variables
domain: computer-science
course: compilers
prerequisites:
- id: type-checking-bidirectional
  type: hard
- id: hindley-milner-type-system
  type: soft
builds-toward:
- three-address-intermediate-code
tags:
- type-systems
- generics
- polymorphism
stage: advanced
status: draft
---

# Polymorphism and Type Variables

## Core Idea
Parametric polymorphism allows functions and data structures to work with multiple types. This is more general than ad-hoc polymorphism (overloading). Implementing polymorphism requires careful handling of type variables, instantiation, and specialization.

## How It's Best Learned
Implement parametric polymorphism using type variables and instantiation. Study how Java generics and C++ templates compile differently.

## Common Misconceptions
Type variables are just placeholders (they are constraints on valid operations). Polymorphism requires runtime type checking (parametric polymorphism can be fully static).

## Explainer

From your work with type checking, you know that a type checker walks the AST and ensures that every operation receives operands of the correct type. But what happens when you write a function like `identity(x) = x` that works for any type? Without polymorphism, you would need to write a separate version for integers, strings, booleans, and every other type — or abandon type safety entirely by using a universal "any" type. **Parametric polymorphism** solves this by introducing **type variables** — placeholders like `α` or `T` that stand for "some type, to be determined later" — allowing a single function definition to be type-safe across all types.

The key insight is that a type variable is not a concrete type but a **universally quantified** constraint. When you write `identity : ∀α. α → α`, you are saying: "for any type `α` you choose, this function takes an `α` and returns an `α`." The type checker enforces this contract: inside `identity`, the only thing you can do with `x` is treat it as an opaque value of type `α`. You cannot add to it, print it, or call methods on it — because those operations are not defined for all possible types. This restriction is what makes parametric polymorphism safe. If you could inspect or operate on `x` based on its runtime type, you would have **ad-hoc polymorphism** (overloading or type classes), which is a different mechanism with different implementation requirements.

When a polymorphic function is actually called — say `identity(42)` — the type checker performs **instantiation**: it substitutes the type variable `α` with the concrete type `int`, producing the specialized type `int → int` for this particular call. If you also call `identity("hello")`, a separate instantiation yields `string → string`. The Hindley-Milner system you have encountered automates this process through **type inference**: the compiler deduces both the polymorphic type of the definition and the instantiation at each call site, without requiring explicit type annotations from the programmer.

How this plays out in compiled code varies significantly across languages. In **type erasure** implementations (like Java generics and most ML compilers), the compiler verifies type safety at compile time and then generates a single version of the code that works with a uniform representation — typically pointers or boxed values. The type variables vanish entirely from the runtime code. In **monomorphization** implementations (like C++ templates and Rust generics), the compiler generates a separate specialized copy of the function for each concrete type it is called with — `identity_int`, `identity_string`, and so on. Monomorphization produces faster code (no boxing overhead) at the cost of larger binaries and longer compile times. Understanding this distinction matters when you move to intermediate code generation, because the IR must either represent polymorphic operations abstractly or the polymorphism must be resolved before IR generation.
