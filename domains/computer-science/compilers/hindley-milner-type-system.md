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
- polymorphism-and-type-variables
tags:
- type-inference
- polymorphism
- functional-languages
stage: advanced
status: validated
---

# Hindley-Milner Type System

## Core Idea
The Hindley-Milner (HM) type system is a polymorphic type system with implicit type inference. It assigns each expression a principal type (most general type satisfying constraints). Polymorphic functions are given rank-1 types: type variables are universally quantified at the top level. HM is used in languages like ML and Haskell; it balances expressiveness with decidable type inference.

## Questions

```yaml
- question: "A programmer writes `let f = fun x -> x in (f 5, f \"hello\")`. Which best explains why this typechecks in HM?"
  type: multiple-choice
  options:
    - "f has type int when applied to 5 and type string when applied to 'hello', showing HM supports runtime type dispatch"
    - "The let binding generalizes f to ∀α. α → α, so each use independently instantiates α as int or string"
    - "HM generates two separate monomorphic copies of f at compile time for each use site"
    - "Type inference fails here and the programmer must add an explicit type annotation"
  answer: 1
  explanation: "The let binding is HM's generalization point. When `let f = fun x -> x` is processed, the type variable α is universally quantified, yielding ∀α. α → α. Each subsequent use site independently instantiates α — once as int, once as string. Without the let (e.g., passing the same lambda directly to a function expecting it at two types), you'd need higher-rank polymorphism, which HM cannot infer."

- question: "Why can HM infer all types in a program while System F (arbitrary-rank polymorphism) cannot?"
  type: multiple-choice
  options:
    - "System F allows side effects that interact with types in ways the inference algorithm cannot predict"
    - "HM restricts universal quantifiers to the outermost level (prenex polymorphism), keeping inference decidable"
    - "System F uses a larger set of type variables that causes the unification algorithm to loop indefinitely"
    - "HM only supports type inference for programs without recursive functions"
  answer: 1
  explanation: "HM's rank-1 restriction confines ∀ to the outermost level — you can have ∀α. α → α but not (∀α. α → α) → int. This prenex restriction means the algorithm only needs to instantiate quantifiers at let-binding call sites, which is decidable. System F allows ∀ nested inside argument positions, which requires the programmer to guide instantiation — inference becomes undecidable because the algorithm cannot search the infinite space of possible type instantiations."

- question: "In Hindley-Milner, a let-bound identifier can be used at different types in different parts of the program."
  type: true-false
  answer: true
  explanation: "This is the defining feature of HM parametric polymorphism. When `let id = fun x -> x` is bound, its type is generalized to ∀α. α → α. Every use site instantiates α independently — id can be applied to an int in one expression and a string in another. This is possible because the let binding creates a type scheme (a quantified type), not a monotype."

- question: "Adding explicit type annotations to every function in an HM-typed program allows the type checker to accept programs that inference alone would reject."
  type: true-false
  answer: false
  explanation: "HM inference is complete: it always finds the principal type — the most general type consistent with the program. Annotations can only narrow a type to something less general or document what inference already knows. They cannot discover more general types than Algorithm W would infer, and overly restrictive annotations can actually prevent valid programs from type-checking. Annotations are documentation aids, not correctness requirements."

- question: "Explain why the `let` binding plays a special role in HM generalization, and what would go wrong if HM tried to generalize type variables inside every lambda abstraction instead."
  type: short-answer
  answer: "The let binding is HM's designated generalization point: only here are type variables universally quantified to form a polymorphic type scheme. If HM attempted to generalize inside lambda arguments — allowing a single function parameter to be used at multiple types within one function body — it would require the parameter's type to be a higher-rank polymorphic type (e.g., a function expecting an argument that works at both int and string simultaneously). Inference for such types is undecidable. By restricting generalization to let bindings and keeping quantifiers at the top level (rank 1), HM guarantees that every well-typed program has a unique principal type that Algorithm W can find."
```

## Explainer

From your work with type inference algorithms, you know that a compiler can often determine the type of an expression without explicit annotations — by examining how values are used, it generates constraints and solves them. And from lambda calculus, you know that functions are first-class values that can be passed around, returned, and composed. The **Hindley-Milner type system** combines these ideas into an elegant framework where the compiler can infer the types of *all* expressions in a program — including polymorphic functions — without a single type annotation from the programmer, and it is guaranteed to find the most general type possible.

Consider the identity function `fun x -> x`. What is its type? It takes an argument and returns it unchanged, so it works on integers, strings, lists — anything. HM assigns it the **principal type** `∀α. α → α`, meaning "for any type α, this function takes an α and returns an α." The key word is **principal**: this is the most general type that is consistent with the function's definition. Any valid use of the function — applying it to an integer, a string, a pair — is an instance of this principal type obtained by substituting a concrete type for α. The guarantee that a principal type always exists and can be found algorithmically is HM's central theorem, proved independently by Hindley (1969) and Milner (1978).

The inference algorithm — **Algorithm W** — works by assigning fresh type variables to unknown types, generating **constraints** from how expressions are used (if `f` is applied to an integer, then `f`'s argument type must unify with `int`), and solving constraints through **unification**. Unification asks: can two type expressions be made identical by substituting type variables? `α → int` and `bool → β` unify with the substitution {α = bool, β = int}, giving `bool → int`. If unification fails (e.g., `int` vs `bool`), the program has a type error. The algorithm processes the program in a single pass, threading a substitution that accumulates all discovered type equalities.

The "rank-1" restriction is what makes this decidable. In HM, type variables are universally quantified only at the **outermost level** of a type scheme — you can have `∀α. α → α` but not `(∀α. α → α) → int` (where the quantifier is nested inside an argument position). This restriction, called **prenex polymorphism**, means that polymorphic values are only generalized at `let` bindings, not at arbitrary expression boundaries. When you write `let id = fun x -> x in (id 5, id "hello")`, the `let` binding generalizes `id` to `∀α. α → α`, and each use instantiates α independently — once as `int`, once as `string`. Without the `let`, passing the same lambda to a function expecting it to work at two different types simultaneously would require higher-rank polymorphism, which makes inference undecidable. This careful scoping of generalization is why ML and Haskell can infer all types while System F (which allows arbitrary-rank polymorphism) cannot.
