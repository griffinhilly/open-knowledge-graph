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

## Explainer

In the type systems you have studied so far, types and values inhabit separate worlds. You can have a type `List<Int>` that describes "a list of integers," but the type says nothing about *how many* integers. The function `head` that returns the first element of a list can be given the type `List<T> → T`, but this is a lie — it crashes on an empty list. The type system cannot distinguish an empty list from a non-empty one because list length is a *value*, and values are invisible to types. **Dependent types** break down this wall: they allow types to contain and be parameterized by values, so `Vec<T, n>` means "a list of exactly n elements of type T," where n is a natural number known at compile time.

This idea connects to lambda calculus in a precise way. In the simply-typed lambda calculus, you have terms that depend on terms (ordinary functions), and types that depend on types (generic/parametric polymorphism). Dependent types add a third axis: **types that depend on terms**. The type `Vec<Int, 3>` depends on the value `3`. A function `append : Vec<T, m> → Vec<T, n> → Vec<T, m+n>` states in its type signature that appending a vector of length m to one of length n produces a vector of length m+n. The compiler *proves* this at type-checking time — if your implementation does not maintain this invariant, it will not compile. This is not testing; it is mathematical proof carried out by the type checker.

Consider what this buys you. A matrix multiplication function can have the type `Matrix<m, k> → Matrix<k, n> → Matrix<m, n>`, and the compiler will reject any attempt to multiply matrices with incompatible dimensions — not at runtime with an error message, but at compile time with a type error. An array index operation can require a proof that the index is within bounds, eliminating out-of-bounds errors entirely. A network protocol parser can encode the expected message format in the type, so a well-typed parser is guaranteed to handle all valid messages correctly.

The cost is significant. Type checking in dependent type systems is **undecidable** in general — the compiler may need to evaluate arbitrary computations to check whether two types are equal. Languages like Agda, Idris, and Coq manage this by requiring all functions used in types to be total (always terminating), which keeps type checking decidable at the expense of restricting what you can express. Writing dependently-typed programs also demands a different style of thinking: you are simultaneously writing code and constructing proofs, and the compiler is your proof assistant. The learning curve is steep, but the payoff is programs where entire categories of bugs — null pointer dereferences, buffer overflows, dimension mismatches, protocol violations — are ruled out by construction rather than caught by tests.
