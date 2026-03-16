---
id: unification-algorithm
title: Unification Algorithm
domain: computer-science
course: compilers
prerequisites:
- id: type-systems-overview
  type: hard
- id: dynamic-programming-intro
  type: soft
builds-toward:
- type-inference-algorithms
tags:
- unification
- constraint-solving
- algorithm
stage: advanced
status: draft
---

# Unification Algorithm

## Core Idea
Unification finds a substitution that makes two terms syntactically identical. In type inference, it solves type constraints by finding variable substitutions. The algorithm recursively decomposes terms and detects occurs-check violations (a variable cannot appear in a term it must equal). Unification is fundamental to type systems and logic programming.

## Explainer

From your study of type systems, you know that a type checker must verify that types are consistent across a program — that the type of an argument matches the type a function expects, that both branches of an `if` return the same type, and so on. When types are explicitly annotated, checking is straightforward comparison. But when types must be **inferred**, the compiler generates **type variables** (unknowns) and **constraints** (equations between type expressions), then solves those constraints. **Unification** is the algorithm that solves them.

The core idea is simple: given two type expressions that may contain variables, find a **substitution** — a mapping from variables to types — that makes the two expressions identical. For example, unifying the type `List<α>` with `List<Int>` yields the substitution `{α → Int}`. Unifying `α → β` with `Int → Bool` yields `{α → Int, β → Bool}`. Unifying `Int` with `Bool` fails — no substitution can make them equal. Each successful unification tells the compiler something concrete about a previously unknown type.

The algorithm works by **recursive decomposition**. To unify two terms: if both are the same constant (like `Int`), succeed with no substitution. If one is a variable, bind that variable to the other term (after the occurs check — see below). If both are compound types with the same constructor (like `List<_>` or `_ → _`), recursively unify their corresponding components. If the constructors differ (`List` vs `Pair`, or `Int` vs `Bool`), fail — the types are incompatible. Each recursive step either produces a variable binding, confirms a match, or reports an error.

The **occurs check** prevents a subtle but critical error: a variable cannot be unified with a term that contains itself. If you try to unify `α` with `List<α>`, the substitution `{α → List<α>}` would create an infinite type — `List<List<List<...>>>`. The occurs check detects this and reports a type error. Without it, the algorithm could loop infinitely or produce unsound results. In practice, occurs-check violations often signal genuine programming errors, like a function that accidentally returns a container of its own return type.

When a type inference engine processes a program, it generates many constraints and applies unification repeatedly. Each unification may bind variables that appear in other constraints, so bindings must be propagated — this is where the connection to your knowledge of dynamic programming is relevant, as efficient unification uses a **union-find** data structure to track variable equivalences without repeatedly copying substitutions. The classic Robinson unification algorithm runs in near-linear time with union-find, making it practical for compilers that must type-check millions of lines of code. Unification is also the computational heart of logic programming languages like Prolog, where it serves as both pattern matching and variable binding in a single operation.
