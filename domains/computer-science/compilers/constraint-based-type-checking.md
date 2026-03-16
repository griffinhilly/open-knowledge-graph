---
id: constraint-based-type-checking
title: Constraint-Based Type Checking
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: type-checking-bidirectional
  type: soft
builds-toward:
- dependent-types-programming
tags:
- type-systems
- constraints
- checking
stage: advanced
status: draft
---

# Constraint-Based Type Checking

## Core Idea
Constraint-based type checking generates constraints between type variables instead of checking types directly. A solver finds an assignment satisfying all constraints, enabling more flexible type systems (optional types, refinement types) and clearer error messages from constraint violations.

## Explainer

Traditional type checking walks the AST and directly verifies that types are consistent at each node — for instance, checking that both operands of `+` are numeric. This works well for simple type systems, but it breaks down when the types are not yet known. Consider a function `let f x = x + 1`. What is the type of `x`? You cannot determine it by looking at the parameter alone — you need to examine how `x` is used in the body. **Constraint-based type checking** handles this by separating the problem into two phases: first generate constraints, then solve them.

In the **constraint generation** phase, the compiler walks the AST and assigns a fresh **type variable** (like α, β, γ) to every expression whose type is not immediately known. At each AST node, it emits constraints describing the relationships these type variables must satisfy. For `x + 1`, the constraints might be: α = type(x), `int` = type(1), α = `int` (because `+` requires integer operands), and the result type is `int`. For a function application `f(a)`, if `f` has type β and `a` has type γ, the constraint is β = γ → δ, where δ is a fresh variable for the return type. Each syntactic construct contributes a few local constraints, and the full set of constraints captures all the type relationships in the program.

The **constraint solving** phase finds an assignment of concrete types to type variables that satisfies every constraint simultaneously, or reports which constraints are unsatisfiable. The most common solving technique is **unification**, which you may know from logic programming. Unification takes two type expressions and finds the most general substitution that makes them equal: unifying `α → int` with `bool → β` yields α = `bool`, β = `int`. The solver processes constraints one at a time, maintaining a substitution map and applying it to remaining constraints as it goes. When a contradiction arises — for example, trying to unify `int` with `bool` — the solver has found a type error, and because it has tracked which program expression generated each constraint, it can produce a meaningful error message pointing to the source of the conflict.

The power of this approach is its flexibility and modularity. Because constraint generation and solving are separate phases, you can extend the type system by adding new constraint forms without rewriting the solver — subtyping constraints, trait bounds, or refinement predicates each just add new kinds of constraints. Languages like OCaml, Haskell, Rust, and TypeScript all use variations of constraint-based type checking to support features like parametric polymorphism and type inference. The programmer writes `let f x = x + 1` without any type annotation, and the constraint solver infers that `f : int → int` — a level of convenience that direct, syntax-directed type checking cannot easily provide.
