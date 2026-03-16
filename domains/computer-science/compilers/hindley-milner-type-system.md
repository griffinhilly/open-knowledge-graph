---
id: hindley-milner-type-system
title: Hindley-Milner Type System
domain: computer-science
course: compilers
prerequisites:
- id: type-inference-algorithms
  type: hard
- id: lambda-calculus-foundations
  type: hard
builds-toward:
- polymorphism-parametric
tags:
- type-inference
- polymorphism
- functional-languages
stage: advanced
status: draft
---

# Hindley-Milner Type System

## Core Idea
The Hindley-Milner (HM) type system is a polymorphic type system with implicit type inference. It assigns each expression a principal type (most general type satisfying constraints). Polymorphic functions are given rank-1 types: type variables are universally quantified at the top level. HM is used in languages like ML and Haskell; it balances expressiveness with decidable type inference.

## Explainer

From your work with type inference algorithms, you know that a compiler can often determine the type of an expression without explicit annotations — by examining how values are used, it generates constraints and solves them. And from lambda calculus, you know that functions are first-class values that can be passed around, returned, and composed. The **Hindley-Milner type system** combines these ideas into an elegant framework where the compiler can infer the types of *all* expressions in a program — including polymorphic functions — without a single type annotation from the programmer, and it is guaranteed to find the most general type possible.

Consider the identity function `fun x -> x`. What is its type? It takes an argument and returns it unchanged, so it works on integers, strings, lists — anything. HM assigns it the **principal type** `∀α. α → α`, meaning "for any type α, this function takes an α and returns an α." The key word is **principal**: this is the most general type that is consistent with the function's definition. Any valid use of the function — applying it to an integer, a string, a pair — is an instance of this principal type obtained by substituting a concrete type for α. The guarantee that a principal type always exists and can be found algorithmically is HM's central theorem, proved independently by Hindley (1969) and Milner (1978).

The inference algorithm — **Algorithm W** — works by assigning fresh type variables to unknown types, generating **constraints** from how expressions are used (if `f` is applied to an integer, then `f`'s argument type must unify with `int`), and solving constraints through **unification**. Unification asks: can two type expressions be made identical by substituting type variables? `α → int` and `bool → β` unify with the substitution {α = bool, β = int}, giving `bool → int`. If unification fails (e.g., `int` vs `bool`), the program has a type error. The algorithm processes the program in a single pass, threading a substitution that accumulates all discovered type equalities.

The "rank-1" restriction is what makes this decidable. In HM, type variables are universally quantified only at the **outermost level** of a type scheme — you can have `∀α. α → α` but not `(∀α. α → α) → int` (where the quantifier is nested inside an argument position). This restriction, called **prenex polymorphism**, means that polymorphic values are only generalized at `let` bindings, not at arbitrary expression boundaries. When you write `let id = fun x -> x in (id 5, id "hello")`, the `let` binding generalizes `id` to `∀α. α → α`, and each use instantiates α independently — once as `int`, once as `string`. Without the `let`, passing the same lambda to a function expecting it to work at two different types simultaneously would require higher-rank polymorphism, which makes inference undecidable. This careful scoping of generalization is why ML and Haskell can infer all types while System F (which allows arbitrary-rank polymorphism) cannot.
