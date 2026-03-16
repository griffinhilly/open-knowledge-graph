---
id: subtyping-and-bounds
title: Subtyping and Type Bounds
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: hindley-milner-type-system
  type: soft
builds-toward:
- gradual-typing-systems
tags:
- type-systems
- subtyping
- generics
stage: advanced
status: draft
---

# Subtyping and Type Bounds

## Core Idea
Subtyping introduces a type ordering where subtypes are usable wherever supertypes are expected (Liskov substitution). Type bounds on generics (e.g., 'T extends Comparable') restrict which types can instantiate parameters, enabling safe polymorphic operations while maintaining type safety.

## Explainer

From your study of type systems, you know that types classify values and that a type checker ensures operations are applied to compatible values. **Subtyping** extends this idea by introducing a relationship *between* types: if type S is a subtype of type T (written S <: T), then any value of type S can safely be used wherever a value of type T is expected. This is the **Liskov Substitution Principle** — a subtype must honor all the guarantees of its supertype.

The most familiar example is class inheritance in object-oriented languages. If `Dog` extends `Animal`, then `Dog <: Animal` — you can pass a `Dog` to any function expecting an `Animal`, because a `Dog` has every method and field that `Animal` has (and possibly more). But subtyping is broader than inheritance. In structural type systems (like TypeScript's), subtyping is determined by shape rather than declared hierarchy: if type A has all the fields that type B requires, A is a subtype of B regardless of whether A explicitly extends B. The key insight is that subtyping is about *capability guarantees* — a subtype can do everything the supertype can do.

Where subtyping gets subtle is with **compound types**, especially function types. If a function expects an `Animal` parameter and returns a `Dog`, what is the subtyping relationship between function types? Function types are **contravariant** in their parameters and **covariant** in their return types. This means a function `(Animal) → Dog` is a subtype of `(Dog) → Animal` — not the other way around. The logic is: a caller providing a `Dog` is safe if the function accepts any `Animal` (a broader input), and a caller expecting an `Animal` result is safe if the function always returns a `Dog` (a narrower output). Getting variance wrong is a common source of type-system unsoundness, and understanding it is essential for working with generic types.

**Type bounds** bring subtyping into the world of generics (parametric polymorphism). An unbounded generic type parameter `T` can be instantiated with any type, but then you cannot call any methods on values of type `T` — the type checker knows nothing about `T`'s capabilities. An **upper bound** like `T extends Comparable` constrains `T` to be a subtype of `Comparable`, so the compiler knows that values of type `T` have a `compareTo` method. This enables writing generic sorting functions, priority queues, and similar data structures that work with any comparable type while remaining fully type-safe. A **lower bound** like `T super Dog` constrains `T` to be a supertype of `Dog` — this is less common but important for safe write operations into generic collections.

If you have encountered the Hindley-Milner type system, you will notice that it achieves polymorphism through type variables and unification rather than subtyping. Adding subtyping to Hindley-Milner-style inference is notoriously difficult because subtyping introduces inequality constraints (S <: T) rather than equality constraints (S = T), making inference undecidable in the general case. This is why languages like Java and C# require explicit type annotations on class declarations and bounds on generics — they combine subtyping with limited inference rather than attempting full inference with subtyping. Understanding this tension between subtyping and inference is key to appreciating the design tradeoffs in real type systems.
