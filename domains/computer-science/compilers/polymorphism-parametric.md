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

## Questions

```yaml
- question: "A function has type ∀α. α → α → α. Which of the following best describes what this function can do?"
  type: multiple-choice
  options:
    - "It could be any function, since the type variable α allows arbitrary behavior on any type"
    - "It must be the identity function, since it takes one value and returns one of the same type"
    - "It must return one of its two arguments unchanged — it cannot examine or transform them"
    - "It could sort its inputs if α happens to be a comparable type"
  answer: 2
  explanation: "A parametrically polymorphic function cannot inspect or branch on its type parameter — it must work identically for all types. A function of type ∀α. α → α → α receives two values of unknown type and must return one of them. Since it cannot construct new values of type α, compare them, or do anything type-specific, it can only return the first or the second argument unchanged. This is 'theorems for free': the type signature alone constrains the function's possible behaviors."

- question: "Rust uses monomorphization while OCaml uses uniform representation for parametric polymorphism. A program calls a polymorphic reverse function on [int], [string], and [bool] lists. How many compiled versions exist in each language?"
  type: multiple-choice
  options:
    - "Rust: 1 version; OCaml: 3 versions"
    - "Rust: 3 versions; OCaml: 1 version"
    - "Rust: 3 versions; OCaml: 3 versions"
    - "Rust: 1 version; OCaml: 1 version"
  answer: 1
  explanation: "Monomorphization (Rust) generates a specialized copy for each concrete type: reverse_int, reverse_string, reverse_bool — three versions. Uniform representation (OCaml) compiles one version that operates on boxed pointers, serving all three call sites. This is the core tradeoff: monomorphization eliminates boxing overhead but increases code size; uniform representation is compact but adds indirection."

- question: "Python's + operator performing integer addition for ints and string concatenation for strings is an example of parametric polymorphism."
  type: true-false
  answer: false
  explanation: "This is ad-hoc polymorphism (overloading). Parametric polymorphism requires that a single piece of code behaves identically regardless of the type — it cannot inspect the type or branch on it. Python's + runs different code for integers vs strings. A parametrically polymorphic function cannot even know what type it is operating on, which is why its behavior must be uniform."

- question: "A function of type ∀α. [α] → [α] could be a sorting function, since it works on lists of any type."
  type: true-false
  answer: false
  explanation: "Parametricity forbids this. The function cannot inspect or compare elements of type α — it has no knowledge of α's structure and no comparison operation. Sorting requires knowing the relative order of elements, which requires type-specific knowledge. The function can only rearrange, drop, or duplicate existing list elements. A sort function needs a constraint like (Ord α) ⇒ [α] → [α], which is a typeclass constraint — not pure parametric polymorphism."

- question: "Why can you deduce properties of a parametrically polymorphic function from its type signature alone, without seeing its implementation?"
  type: short-answer
  answer: "Because a parametrically polymorphic function cannot inspect, branch on, or construct values of its type parameter α, its behavior is fully determined by what it can legally do with values of an unknown type. The type signature tells you exactly what inputs are available and what output type is required, and since no type-specific operations are permitted, the space of possible implementations is tightly constrained. This principle — called parametricity or 'theorems for free' — means the type itself serves as a specification."
  explanation: "This contrasts sharply with ad-hoc polymorphism, where the type signature tells you almost nothing about behavior (the + operator's type gives no hint that it adds integers but concatenates strings). Parametricity is one of the most powerful properties of Hindley-Milner type systems: it gives you machine-checked behavioral guarantees from types alone."
```

## Explainer

From your study of Hindley-Milner type inference, you know that a type system can automatically assign types to expressions without explicit annotations. Parametric polymorphism is what makes that system powerful: it allows a single function definition to work uniformly over *all* types, not just one. The `length` function doesn't care whether it's counting integers, strings, or nested lists — it only inspects the list structure, never the elements. The type variable `α` in `length: ∀α. [α] → int` is a placeholder that can be instantiated to any concrete type, and the function's behavior is identical regardless of what `α` becomes.

The word **parametric** is key — it means the function's behavior is *parameterized* by a type it knows nothing about. This gives you a powerful reasoning tool called **parametricity** (or "theorems for free"): because a parametrically polymorphic function cannot inspect or branch on its type parameter, you can deduce properties of the function from its type signature alone. For example, a function with type `∀α. α → α` can only be the identity function — there is nothing else it could do with a value of an unknown type except return it unchanged. This is fundamentally different from **ad-hoc polymorphism** (overloading), where `+` might mean integer addition for `int` and concatenation for `string` — different code for different types.

From a compiler's perspective, parametric polymorphism raises a concrete implementation question: if `length` works on `[int]`, `[string]`, and `[bool]`, does the compiler generate one copy of the code or many? There are two main strategies. **Uniform representation** (used by OCaml, Haskell, Java's generics) compiles a single version of the function that operates on a universal representation — typically boxed pointers. This is simple but adds indirection overhead. **Monomorphization** (used by Rust, C++ templates) generates a specialized copy of the function for each concrete type it's used with — `length_int`, `length_string`, etc. This eliminates indirection but can increase code size. Both strategies produce correct results; the tradeoff is between runtime performance and compilation cost.

Understanding parametric polymorphism also clarifies the design space of type systems you'll encounter in compiler construction. Languages like ML and Haskell use **prenex polymorphism** (the `∀` quantifier appears only at the outermost level), which keeps type inference decidable. More expressive systems allow **higher-rank polymorphism**, where polymorphic types can appear inside function arguments — but this requires explicit annotations because inference becomes undecidable. The Hindley-Milner system you already know hits a sweet spot: it infers principal (most general) types for all expressions using only prenex polymorphism, giving programmers generics without annotation burden.
