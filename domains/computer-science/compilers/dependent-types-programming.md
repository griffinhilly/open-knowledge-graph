---
id: dependent-types-programming
title: Dependent Types and Value-Level Type Constraints
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: lambda-calculus-foundations
  type: hard
tags:
- type-systems
- dependent-types
- advanced
stage: advanced
status: draft
---

# Dependent Types and Value-Level Type Constraints

## Core Idea
In dependent type systems, types can depend on values—not just other types. This enables properties like 'list of length n' or 'vector indexed from 1 to n' to be encoded in types, allowing type-checking to verify invariants that traditional type systems cannot, eliminating entire classes of runtime errors.

## Questions

```yaml
- question: "A dependently-typed language defines a function with signature: `matMul : Matrix<m, k> → Matrix<k, n> → Matrix<m, n>`. A programmer calls `matMul A B` where A has type `Matrix<3, 4>` and B has type `Matrix<5, 2>`. What happens?"
  type: multiple-choice
  options:
    - "The program compiles but throws a dimension mismatch exception at runtime"
    - "The program fails to type-check at compile time, because 4 ≠ 5 (the inner dimensions don't match)"
    - "The program compiles; the type system cannot track numeric values like matrix dimensions"
    - "The behavior depends on whether the compiler performs value inference"
  answer: 1
  explanation: "This is the core payoff of dependent types. In a conventional type system, `Matrix` is typed with only element type, and dimension mismatches cause runtime exceptions. In a dependent type system, `Matrix<m, k>` encodes both dimensions as type-level values. When calling `matMul A B`, the compiler unifies the shared dimension: A's second dimension `k` must equal B's first dimension. Since 4 ≠ 5, the types are incompatible and the program is rejected at compile time — before any execution, before any test. The bug is impossible to ship, not just caught after the fact."

- question: "Why do dependently typed languages like Agda and Idris require all functions used in types to be provably terminating (total functions)?"
  type: multiple-choice
  options:
    - "Totality is a convenience requirement to make programs easier to read, not a formal requirement"
    - "Without guaranteed termination, type checking could loop forever trying to evaluate type-level computations"
    - "Partial functions cannot be expressed in dependent type systems due to syntactic restrictions"
    - "Totality is required only for standard library functions, not user-defined functions"
  answer: 1
  explanation: "Type checking in dependent type systems requires evaluating type-level expressions to determine if two types are equal. For example, to verify that `Vec<T, 2+3>` and `Vec<T, 5>` are the same type, the compiler must evaluate `2+3`. If functions used in types can loop infinitely, type checking can loop infinitely — making type checking undecidable. Requiring totality (all functions terminate on all inputs) guarantees that type-level evaluation always terminates, keeping type checking decidable. This is the mathematical prerequisite for a sound type system, not a convenience choice."

- question: "A function with type `safeHead : Vec<T, S n> → T` in a dependently-typed language provides a compile-time guarantee that the input list is non-empty."
  type: true-false
  answer: true
  explanation: "True. `Vec<T, S n>` (where `S n` means 'successor of n,' i.e., n+1) is the type of vectors with at least one element — an empty vector has type `Vec<T, 0>` and cannot unify with `Vec<T, S n>`. Any caller of `safeHead` must provide a vector whose length type unifies with `S n` for some n. Passing an empty vector causes a type error at compile time, not a runtime crash. The type signature encodes the precondition, and the type checker enforces it automatically — no runtime guard or documentation needed."

- question: "Dependent types are a generalization of generic types (parametric polymorphism): instead of parameterizing types over other types, you parameterize them over values."
  type: true-false
  answer: false
  explanation: "False — this description conflates two different dimensions of the lambda cube. Parametric polymorphism (generics like `List<T>`) allows types to depend on *other types*. Dependent types allow types to depend on *values*. These are distinct axes of expressiveness: generics capture 'a list of any element type,' while dependent types capture 'a list of exactly n elements.' A fully dependently-typed system supports types depending on values, types depending on types, terms depending on types, and terms depending on terms. Dependent types are not a generalization of generics — they occupy a different dimension of the type theory design space."

- question: "In dependent type theory, it is said that 'writing a well-typed program is the same as constructing a proof.' What does this mean concretely, and why does it eliminate certain categories of bugs?"
  type: short-answer
  answer: "By the Curry-Howard correspondence, types are propositions and programs inhabiting those types are proofs. A function `append : Vec<T, m> → Vec<T, n> → Vec<T, m+n>` is not just code — it is a proof that appending an m-element vector to an n-element vector yields an (m+n)-element vector. If the implementation doesn't maintain this invariant, the program fails to type-check (the proof is invalid). Bugs involving invariant violations become type errors caught at compile time rather than runtime failures discoverable only during execution or testing."
  explanation: "The Curry-Howard isomorphism establishes a correspondence between logic and programming: propositions correspond to types, proofs correspond to programs, and proof verification corresponds to type checking. If you can write a well-typed dependently-typed program, you have simultaneously proven the properties encoded in its type signature. Errors like 'I appended two lists and got the wrong length' become logically impossible — they would require an invalid proof, which the type checker rejects. The compiler acts as a proof assistant, verifying invariants mechanically on every compilation."
```

## Explainer

In the type systems you have studied so far, types and values inhabit separate worlds. You can have a type `List<Int>` that describes "a list of integers," but the type says nothing about *how many* integers. The function `head` that returns the first element of a list can be given the type `List<T> → T`, but this is a lie — it crashes on an empty list. The type system cannot distinguish an empty list from a non-empty one because list length is a *value*, and values are invisible to types. **Dependent types** break down this wall: they allow types to contain and be parameterized by values, so `Vec<T, n>` means "a list of exactly n elements of type T," where n is a natural number known at compile time.

This idea connects to lambda calculus in a precise way. In the simply-typed lambda calculus, you have terms that depend on terms (ordinary functions), and types that depend on types (generic/parametric polymorphism). Dependent types add a third axis: **types that depend on terms**. The type `Vec<Int, 3>` depends on the value `3`. A function `append : Vec<T, m> → Vec<T, n> → Vec<T, m+n>` states in its type signature that appending a vector of length m to one of length n produces a vector of length m+n. The compiler *proves* this at type-checking time — if your implementation does not maintain this invariant, it will not compile. This is not testing; it is mathematical proof carried out by the type checker.

Consider what this buys you. A matrix multiplication function can have the type `Matrix<m, k> → Matrix<k, n> → Matrix<m, n>`, and the compiler will reject any attempt to multiply matrices with incompatible dimensions — not at runtime with an error message, but at compile time with a type error. An array index operation can require a proof that the index is within bounds, eliminating out-of-bounds errors entirely. A network protocol parser can encode the expected message format in the type, so a well-typed parser is guaranteed to handle all valid messages correctly.

The cost is significant. Type checking in dependent type systems is **undecidable** in general — the compiler may need to evaluate arbitrary computations to check whether two types are equal. Languages like Agda, Idris, and Coq manage this by requiring all functions used in types to be total (always terminating), which keeps type checking decidable at the expense of restricting what you can express. Writing dependently-typed programs also demands a different style of thinking: you are simultaneously writing code and constructing proofs, and the compiler is your proof assistant. The learning curve is steep, but the payoff is programs where entire categories of bugs — null pointer dereferences, buffer overflows, dimension mismatches, protocol violations — are ruled out by construction rather than caught by tests.
