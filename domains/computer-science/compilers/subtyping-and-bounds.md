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
status: validated
---

# Subtyping and Type Bounds

## Core Idea
Subtyping introduces a type ordering where subtypes are usable wherever supertypes are expected (Liskov substitution). Type bounds on generics (e.g., 'T extends Comparable') restrict which types can instantiate parameters, enabling safe polymorphic operations while maintaining type safety.

## Questions

```yaml
- question: "A function type `(Animal) → Dog` and a function type `(Dog) → Animal` are both in scope. Under correct subtyping rules with contravariant parameters and covariant returns, which is a subtype of which?"
  type: multiple-choice
  options:
    - "`(Dog) → Animal` is a subtype of `(Animal) → Dog`, because it accepts a narrower input and returns a broader output"
    - "`(Animal) → Dog` is a subtype of `(Dog) → Animal`, because it accepts a broader input and returns a narrower output"
    - "Neither is a subtype of the other; function types are invariant"
    - "Both are subtypes of each other, since they accept the same types in different directions"
  answer: 1
  explanation: "Function subtyping is contravariant in parameters and covariant in returns. `(Animal) → Dog` <: `(Dog) → Animal` because: (1) its parameter type `Animal` is a supertype of `Dog` — a caller passing a `Dog` is safe since the function accepts any `Animal`; (2) its return type `Dog` is a subtype of `Animal` — a caller expecting an `Animal` result is safe since the function always returns a `Dog`. The tempting wrong answer (option A) reverses this logic: a function that *only* accepts `Dog` is more restrictive, not less, from the caller's perspective."

- question: "What does an upper bound `T extends Comparable<T>` on a generic type parameter primarily enable?"
  type: multiple-choice
  options:
    - "It prevents T from being instantiated with primitive types, improving runtime performance"
    - "It allows the compiler to guarantee that values of type T have a compareTo method, enabling type-safe generic operations like sorting"
    - "It restricts T to exactly the Comparable type, removing the benefit of generics"
    - "It forces callers to provide explicit type annotations rather than relying on inference"
  answer: 1
  explanation: "An upper bound tells the type checker: 'T must be a subtype of Comparable<T>.' By the Liskov Substitution Principle, anything T can do, Comparable<T> can do — so the compiler knows values of type T have a compareTo method. This enables writing generic algorithms (sorting, priority queues) that work with any comparable type while remaining fully type-safe. Without the bound, T is completely opaque: you cannot call any methods on it. The bound adds capability knowledge, not restriction — it's what makes the generic useful."

- question: "If `Dog` is a subclass of `Animal`, then `List<Dog>` is a subtype of `List<Animal>` in a type-safe generic system."
  type: true-false
  answer: false
  explanation: "Generic collections are typically invariant in type-safe systems precisely because covariance would allow unsafe operations. If `List<Dog>` were a subtype of `List<Animal>`, you could write code like: `List<Animal> animals = new List<Dog>(); animals.add(new Cat());` — which would insert a Cat into a list that holds only Dogs, causing a runtime type error. Java's generic collections (unlike arrays) are invariant to prevent this. Covariance is only safe for read-only (producer) contexts, which is why Java uses wildcards like `? extends Animal` for that use case."

- question: "In a structural type system, a type can be a subtype of another type even without any explicit declaration of inheritance or interface implementation."
  type: true-false
  answer: true
  explanation: "Structural subtyping is based on shape (what fields and methods a type has) rather than declared relationships. TypeScript is the canonical example: if type A has all the properties that type B requires, A is structurally a subtype of B, even if A never mentions B. This is sometimes called 'duck typing' at the type-system level. Nominal type systems (like Java or C#) require explicit declaration (`implements`, `extends`). Both approaches enforce the core subtyping guarantee — a subtype can do everything a supertype can — but through different mechanisms."

- question: "Why must function types be contravariant in their parameter types? Give a concrete example showing what goes wrong if parameter types were covariant instead."
  type: short-answer
  answer: "If function parameters were covariant, a function expecting a subtype (e.g., Dog) could be substituted where a function expecting the supertype (Animal) is needed. A caller might then pass a Cat (which is an Animal but not a Dog), causing a type error at runtime. Example: if `(Dog → void) <: (Animal → void)` under covariance, you could pass a `(Dog → void)` function to code that calls it with any `Animal`. When that code passes a `Cat`, the function tries to use Dog-specific methods on a Cat — a type violation. Contravariance ensures the substituted function accepts at least as broad an input as the original."
  explanation: "Contravariance in parameters is the direction required for safe substitution. A subtype function must be at least as accepting as the supertype function. If a caller is prepared to pass an Animal, the function it calls must be able to handle any Animal — so the function's parameter type must be Animal or a supertype of Animal, not a subtype like Dog."
```

## Explainer

From your study of type systems, you know that types classify values and that a type checker ensures operations are applied to compatible values. **Subtyping** extends this idea by introducing a relationship *between* types: if type S is a subtype of type T (written S <: T), then any value of type S can safely be used wherever a value of type T is expected. This is the **Liskov Substitution Principle** — a subtype must honor all the guarantees of its supertype.

The most familiar example is class inheritance in object-oriented languages. If `Dog` extends `Animal`, then `Dog <: Animal` — you can pass a `Dog` to any function expecting an `Animal`, because a `Dog` has every method and field that `Animal` has (and possibly more). But subtyping is broader than inheritance. In structural type systems (like TypeScript's), subtyping is determined by shape rather than declared hierarchy: if type A has all the fields that type B requires, A is a subtype of B regardless of whether A explicitly extends B. The key insight is that subtyping is about *capability guarantees* — a subtype can do everything the supertype can do.

Where subtyping gets subtle is with **compound types**, especially function types. If a function expects an `Animal` parameter and returns a `Dog`, what is the subtyping relationship between function types? Function types are **contravariant** in their parameters and **covariant** in their return types. This means a function `(Animal) → Dog` is a subtype of `(Dog) → Animal` — not the other way around. The logic is: a caller providing a `Dog` is safe if the function accepts any `Animal` (a broader input), and a caller expecting an `Animal` result is safe if the function always returns a `Dog` (a narrower output). Getting variance wrong is a common source of type-system unsoundness, and understanding it is essential for working with generic types.

**Type bounds** bring subtyping into the world of generics (parametric polymorphism). An unbounded generic type parameter `T` can be instantiated with any type, but then you cannot call any methods on values of type `T` — the type checker knows nothing about `T`'s capabilities. An **upper bound** like `T extends Comparable` constrains `T` to be a subtype of `Comparable`, so the compiler knows that values of type `T` have a `compareTo` method. This enables writing generic sorting functions, priority queues, and similar data structures that work with any comparable type while remaining fully type-safe. A **lower bound** like `T super Dog` constrains `T` to be a supertype of `Dog` — this is less common but important for safe write operations into generic collections.

If you have encountered the Hindley-Milner type system, you will notice that it achieves polymorphism through type variables and unification rather than subtyping. Adding subtyping to Hindley-Milner-style inference is notoriously difficult because subtyping introduces inequality constraints (S <: T) rather than equality constraints (S = T), making inference undecidable in the general case. This is why languages like Java and C# require explicit type annotations on class declarations and bounds on generics — they combine subtyping with limited inference rather than attempting full inference with subtyping. Understanding this tension between subtyping and inference is key to appreciating the design tradeoffs in real type systems.
