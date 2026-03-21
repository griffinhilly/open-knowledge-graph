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

## Questions

```yaml
- question: "A type checker processes `let f x = x + 1` with no type annotations. It assigns type variable α to x. What constraint does the `+` operation generate?"
  type: multiple-choice
  options:
    - "α = float, because + in most languages operates on floating-point numbers by default"
    - "α = int, because + requires operands of the same type and 1 is an integer literal, so x must also be int"
    - "A type error, because x has no annotation and the checker cannot proceed without one"
    - "No constraint — type variables are left unresolved until the function is called with a concrete argument"
  answer: 1
  explanation: "Constraint-based type checking generates constraints from how values are used, not from annotations. The + operator requires both operands to have the same numeric type; since 1 is an integer literal with type int, the constraint α = int is generated. The solver then records this constraint and, when it processes the whole program, it knows f takes an int and returns an int — without any annotation from the programmer. This is precisely the power of constraint-based type inference."

- question: "What is the key architectural advantage of separating constraint generation from constraint solving in type checking?"
  type: multiple-choice
  options:
    - "It makes type checking faster because constraints can be checked in parallel during lexical analysis"
    - "It allows the type system to be extended with new constraint forms (subtyping, trait bounds, refinements) without rewriting the core solver"
    - "It eliminates the need for garbage collection because type variables are automatically freed after constraint solving"
    - "It ensures that programs without explicit type annotations are always rejected, which improves code documentation"
  answer: 1
  explanation: "Separation of concerns is the key benefit. The constraint generator is language-specific: it knows the syntax and what constraints each construct implies. The solver is language-agnostic: it just solves constraint systems. Adding a new type system feature — say, subtyping or a trait bound — means adding new constraint forms to the generator. The solver can often handle these without modification, or with local extensions. This modular design is why so many different languages (OCaml, Haskell, Rust, TypeScript) can use variations of the same underlying constraint-solving machinery."

- question: "Constraint-based type checking requires programmers to write explicit type annotations for every function parameter and variable in order to generate constraints."
  type: true-false
  answer: false
  explanation: "The whole point of constraint-based type checking is that it works without annotations. The compiler assigns fresh type variables to unannotated expressions and generates constraints from how those expressions are used. Unification then solves the constraints, inferring concrete types. Languages like OCaml and Haskell allow entire programs to be written without a single type annotation — the constraint solver infers everything. Annotations are permitted and can help both the programmer and the compiler, but they are not required."

- question: "In constraint-based type checking, unification finds the most general substitution that makes two type expressions equal, and reports a type error when no such substitution exists."
  type: true-false
  answer: true
  explanation: "Unification is the core solving mechanism. Given two type expressions (e.g., α → int and bool → β), unification finds the unique most-general unifier: α = bool, β = int. 'Most general' means it avoids unnecessary commitments — it never specializes a type variable beyond what is required. When unification fails (e.g., trying to unify int with bool), no substitution can reconcile them, which means the constraints are unsatisfiable — the program has a type error. The constraint that generated the conflict is tracked back to the source expression to produce the error message."

- question: "Why does constraint-based type checking enable type inference for unannotated code, while traditional syntax-directed type checking does not?"
  type: short-answer
  answer: "Traditional syntax-directed type checking checks each AST node locally and immediately — if the type of an expression is not yet known (because there is no annotation), it fails. Constraint-based checking instead assigns fresh type variables to unknown expressions and generates constraints describing what relationships those variables must satisfy. These constraints are collected across the entire program. The solver then has a global view and can propagate information bidirectionally: learning from how a variable is used in the body of a function what type the parameter must have, even though the parameter had no annotation. Unification solves all constraints simultaneously, yielding inferred types throughout."
  explanation: "The contrast is between local (node-by-node) and global (whole-program) reasoning. Syntax-directed checking cannot reason globally because it makes decisions immediately at each node. Constraint generation defers all decisions until the full constraint system is assembled, then solves once — allowing information from later parts of the code to influence earlier parts."
```

## Explainer

Traditional type checking walks the AST and directly verifies that types are consistent at each node — for instance, checking that both operands of `+` are numeric. This works well for simple type systems, but it breaks down when the types are not yet known. Consider a function `let f x = x + 1`. What is the type of `x`? You cannot determine it by looking at the parameter alone — you need to examine how `x` is used in the body. **Constraint-based type checking** handles this by separating the problem into two phases: first generate constraints, then solve them.

In the **constraint generation** phase, the compiler walks the AST and assigns a fresh **type variable** (like α, β, γ) to every expression whose type is not immediately known. At each AST node, it emits constraints describing the relationships these type variables must satisfy. For `x + 1`, the constraints might be: α = type(x), `int` = type(1), α = `int` (because `+` requires integer operands), and the result type is `int`. For a function application `f(a)`, if `f` has type β and `a` has type γ, the constraint is β = γ → δ, where δ is a fresh variable for the return type. Each syntactic construct contributes a few local constraints, and the full set of constraints captures all the type relationships in the program.

The **constraint solving** phase finds an assignment of concrete types to type variables that satisfies every constraint simultaneously, or reports which constraints are unsatisfiable. The most common solving technique is **unification**, which you may know from logic programming. Unification takes two type expressions and finds the most general substitution that makes them equal: unifying `α → int` with `bool → β` yields α = `bool`, β = `int`. The solver processes constraints one at a time, maintaining a substitution map and applying it to remaining constraints as it goes. When a contradiction arises — for example, trying to unify `int` with `bool` — the solver has found a type error, and because it has tracked which program expression generated each constraint, it can produce a meaningful error message pointing to the source of the conflict.

The power of this approach is its flexibility and modularity. Because constraint generation and solving are separate phases, you can extend the type system by adding new constraint forms without rewriting the solver — subtyping constraints, trait bounds, or refinement predicates each just add new kinds of constraints. Languages like OCaml, Haskell, Rust, and TypeScript all use variations of constraint-based type checking to support features like parametric polymorphism and type inference. The programmer writes `let f x = x + 1` without any type annotation, and the constraint solver infers that `f : int → int` — a level of convenience that direct, syntax-directed type checking cannot easily provide.
