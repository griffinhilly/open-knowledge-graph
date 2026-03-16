---
id: type-reconstruction-algorithms
title: Type Reconstruction and Inference
domain: computer-science
course: compilers
prerequisites:
- id: type-inference-algorithms
  type: hard
- id: unification-algorithm
  type: hard
builds-toward:
- constraint-based-type-checking
tags:
- type-systems
- inference
- algorithms
stage: advanced
status: draft
---

# Type Reconstruction and Inference

## Core Idea
Type reconstruction determines types for expressions where types aren't explicitly written. It generates constraints (variable must equal int, type-a must unify with type-b) and solves them via unification, producing a consistent type assignment that respects the language's type rules.

## Explainer

From your work with type inference and unification, you know the basic pieces: type inference assigns types to expressions without explicit annotations, and unification finds substitutions that make two type expressions equal. **Type reconstruction** combines these into a complete algorithm that takes an unannotated program and either produces a valid typing for every expression or reports that no consistent typing exists.

The classic algorithm is **Algorithm W**, introduced by Damas and Milner for the Hindley-Milner type system used in ML and Haskell. It works by walking the syntax tree and generating **type constraints** at each node. When it encounters a literal like `42`, it assigns the type `int`. When it encounters a variable, it looks up its type in the environment (or assigns a fresh **type variable** like `α` if the type is unknown). When it encounters a function application `f(x)`, it generates the constraint that `f`'s type must be `typeof(x) → β` for some fresh type variable `β`, and the result type is `β`. Each syntactic construct produces constraints that relate the types of its subexpressions.

After constraint generation, the algorithm solves the constraint set using **unification**. Each constraint says two type expressions must be equal — for example, `α = int → β` or `β = bool`. Unification finds a **substitution** (a mapping from type variables to concrete types) that satisfies all constraints simultaneously. If `α` must equal `int → β` and `β` must equal `bool`, unification produces `{α ↦ int → bool, β ↦ bool}`. If constraints are contradictory — say `α = int` and `α = bool` — unification fails, and the algorithm reports a type error. The **occurs check** prevents nonsensical infinite types: if solving `α = list(α)`, the algorithm rejects it because `α` would need to be `list(list(list(...)))` infinitely.

The power of type reconstruction is that programmers write code like `let f x = x + 1` without any type annotations, and the algorithm deduces that `f : int → int`. The Hindley-Milner system guarantees a **principal type** — the most general type that is valid — and Algorithm W finds it. This means the inferred type is never less general than what the programmer intended. Polymorphic functions like `let id x = x` receive the type `∀α. α → α`, meaning `id` works for any type. The algorithm achieves this through **let-polymorphism**: at `let` bindings, type variables that are not constrained by the surrounding context are universally quantified, allowing the bound name to be used at different types in different places.
