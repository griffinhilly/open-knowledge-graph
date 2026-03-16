---
id: polymorphism-parametric
title: Parametric Polymorphism
domain: computer-science
course: compilers
prerequisites:
- id: hindley-milner-type-system
  type: hard
builds-toward:
- generics-and-specialization
tags:
- polymorphism
- generics
- type-parameters
stage: advanced
status: draft
---

# Parametric Polymorphism

## Core Idea
Parametric polymorphism allows functions and data types to be generic over type variables. A polymorphic function like `length: ∀α. [α] → int` works on lists of any element type, and a single compiled function serves all instantiations (via code generation or runtime dispatch). This contrasts with ad-hoc polymorphism (overloading), where different code handles different types.

## Explainer

From your study of Hindley-Milner type inference, you know that a type system can automatically assign types to expressions without explicit annotations. Parametric polymorphism is what makes that system powerful: it allows a single function definition to work uniformly over *all* types, not just one. The `length` function doesn't care whether it's counting integers, strings, or nested lists — it only inspects the list structure, never the elements. The type variable `α` in `length: ∀α. [α] → int` is a placeholder that can be instantiated to any concrete type, and the function's behavior is identical regardless of what `α` becomes.

The word **parametric** is key — it means the function's behavior is *parameterized* by a type it knows nothing about. This gives you a powerful reasoning tool called **parametricity** (or "theorems for free"): because a parametrically polymorphic function cannot inspect or branch on its type parameter, you can deduce properties of the function from its type signature alone. For example, a function with type `∀α. α → α` can only be the identity function — there is nothing else it could do with a value of an unknown type except return it unchanged. This is fundamentally different from **ad-hoc polymorphism** (overloading), where `+` might mean integer addition for `int` and concatenation for `string` — different code for different types.

From a compiler's perspective, parametric polymorphism raises a concrete implementation question: if `length` works on `[int]`, `[string]`, and `[bool]`, does the compiler generate one copy of the code or many? There are two main strategies. **Uniform representation** (used by OCaml, Haskell, Java's generics) compiles a single version of the function that operates on a universal representation — typically boxed pointers. This is simple but adds indirection overhead. **Monomorphization** (used by Rust, C++ templates) generates a specialized copy of the function for each concrete type it's used with — `length_int`, `length_string`, etc. This eliminates indirection but can increase code size. Both strategies produce correct results; the tradeoff is between runtime performance and compilation cost.

Understanding parametric polymorphism also clarifies the design space of type systems you'll encounter in compiler construction. Languages like ML and Haskell use **prenex polymorphism** (the `∀` quantifier appears only at the outermost level), which keeps type inference decidable. More expressive systems allow **higher-rank polymorphism**, where polymorphic types can appear inside function arguments — but this requires explicit annotations because inference becomes undecidable. The Hindley-Milner system you already know hits a sweet spot: it infers principal (most general) types for all expressions using only prenex polymorphism, giving programmers generics without annotation burden.
