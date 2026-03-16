---
id: type-inference-algorithms
title: Type Inference Algorithms
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: unification-algorithm
  type: hard
builds-toward:
- hindley-milner-type-system
tags:
- type-inference
- constraint-solving
- algorithm
stage: advanced
status: draft
---

# Type Inference Algorithms

## Core Idea
Type inference algorithms automatically determine types of expressions without explicit annotations. Constraint-based inference generates type equations from the program, then solves them. The unification algorithm finds a most general solution to these constraints. Modern languages use type inference to reduce annotation burden while retaining compile-time type safety.

## Explainer

You already know that type systems classify expressions to prevent certain classes of errors, and that the unification algorithm can find substitutions that make two symbolic expressions identical. Type inference connects these ideas: instead of requiring the programmer to annotate every variable and expression with a type, the compiler generates **type constraints** from the program's structure and then uses unification to solve them automatically.

The process begins with **constraint generation**. The compiler walks the abstract syntax tree and, for each node, produces equations relating the types of its parts. When it sees `x + y`, it generates constraints saying the types of `x` and `y` must both be numeric and the result type must also be numeric. When it sees a function application `f(a)`, it generates a constraint saying the type of `f` must be a function from the type of `a` to some fresh **type variable** representing the unknown result type. Type variables are placeholders — they stand for types the compiler hasn't determined yet, much like unknowns in a system of equations. A function definition `fun x -> x + 1` generates constraints that the parameter `x` must be an integer (because it's added to 1) and the return type must also be an integer.

Once all constraints are collected, the compiler feeds them to the **unification algorithm**. Unification takes pairs of type expressions and finds a **most general unifier** — a substitution mapping type variables to concrete types (or to other type variables) that satisfies every constraint simultaneously. If `α = int` and `β = α → int`, unification produces `{α ↦ int, β ↦ int → int}`. The "most general" part matters: the algorithm avoids over-specializing. If the constraints don't force `α` to be any specific type, unification leaves it as a type variable, which means the expression is **polymorphic** — it works for any type. This is how languages like ML and Haskell infer that `fun x -> x` has type `α → α` (the identity function works for all types) without the programmer writing a single annotation.

Inference can fail in two ways. A **type error** occurs when unification finds contradictory constraints — for instance, if one constraint says `α = int` and another says `α = string`. The compiler reports this as a type mismatch. The **occurs check** catches a subtler problem: if solving requires `α = list(α)`, the type would be infinitely recursive, which most type systems reject. Modern type inference algorithms handle these cases with clear error messages, but the core algorithm remains the same generate-then-unify pipeline. Understanding this pipeline demystifies the "magic" of languages where types seem to appear from nowhere — the compiler is simply solving a constraint system that the program's structure defines implicitly.
