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
status: validated
---

# Type Inference Algorithms

## Core Idea
Type inference algorithms automatically determine types of expressions without explicit annotations. Constraint-based inference generates type equations from the program, then solves them. The unification algorithm finds a most general solution to these constraints. Modern languages use type inference to reduce annotation burden while retaining compile-time type safety.

## Questions

```yaml
- question: "When type inference infers that `fun x -> x` has type `α → α`, why doesn't it infer the more specific type `int → int`?"
  type: multiple-choice
  options:
    - "The inference algorithm only infers types for expressions applied to integer arguments it has already seen"
    - "The algorithm finds the most general unifier — if no constraint forces α to be int, it leaves α as a free type variable, yielding a polymorphic type"
    - "The algorithm cannot infer numeric types and defaults to generic type variables for all primitives"
    - "The identity function is a special case hard-coded as polymorphic in the type system"
  answer: 1
  explanation: "Type inference generates constraints from the program's structure and solves them via unification. For `fun x -> x`, the only constraint is that input and output must have the same type — nothing forces that type to be int. Unification finds the most general unifier: rather than specializing unnecessarily, it leaves α free, producing a polymorphic type α → α. If the function were instead `fun x -> x + 1`, the addition would constrain α = int and the inferred type would be int → int."

- question: "During constraint generation for a function application `f(a)`, what constraint does the compiler produce?"
  type: multiple-choice
  options:
    - "The types of f and a must be equal"
    - "The type of f must be a function type α → β, where α equals the type of a, and β is a fresh type variable for the result"
    - "The type of a must be a subtype of the domain type expected by f"
    - "f must have a concrete, fully-known function type at compile time"
  answer: 1
  explanation: "For a function application `f(a)`, the compiler generates a constraint that the type of `f` must be a function from the type of `a` to some result type. Since the result type is unknown, it is represented as a fresh type variable — a placeholder to be filled in later by unification. This constraint, combined with others, will determine whether `f` is applied correctly and what result type the application has."

- question: "Type inference eliminates compile-time type safety, because without explicit annotations the compiler cannot fully verify that types are used correctly."
  type: true-false
  answer: false
  explanation: "Type inference maintains full compile-time type safety — it does not skip type checking, it performs it automatically. The constraint-generation and unification process produces the same type information that explicit annotations would provide. If a type mismatch exists (e.g., passing a string to a function expecting an integer), unification finds contradictory constraints and the compiler reports a type error. Inference reduces programmer burden without weakening the type-safety guarantee."

- question: "The 'occurs check' in type inference catches situations where solving constraints would require a type variable to equal a type expression that contains that same variable."
  type: true-false
  answer: true
  explanation: "Without the occurs check, unification could attempt to satisfy a constraint like α = list(α), producing an infinite type with no finite representation. The occurs check adds a verification step: before substituting α ↦ T, it verifies that α does not appear in T. If it does, unification fails with a type error. Most practical type systems include this check; some (like certain Prolog implementations) omit it for performance, at the cost of allowing potentially unsound infinite types."

- question: "Describe the two main phases of type inference and explain what role unification plays in the second phase."
  type: short-answer
  answer: "Phase 1 is constraint generation: the compiler walks the abstract syntax tree and, for each construct, produces type equations relating the types of its parts using fresh type variables as placeholders for unknowns. Phase 2 is constraint solving: the unification algorithm takes the collected constraints and finds a most general unifier — a substitution mapping type variables to types that simultaneously satisfies all constraints. Unification detects type errors (contradictory constraints like α = int and α = string) and leaves variables free when constraints don't force them to a specific type, yielding polymorphic types automatically."
  explanation: "The key insight is that type inference transforms a typing problem into a constraint-satisfaction problem and solves it algebraically. Unification is not guessing — it finds the unique most general solution to the constraint system, explaining why polymorphism emerges naturally rather than requiring special-case rules."
```

## Explainer

You already know that type systems classify expressions to prevent certain classes of errors, and that the unification algorithm can find substitutions that make two symbolic expressions identical. Type inference connects these ideas: instead of requiring the programmer to annotate every variable and expression with a type, the compiler generates **type constraints** from the program's structure and then uses unification to solve them automatically.

The process begins with **constraint generation**. The compiler walks the abstract syntax tree and, for each node, produces equations relating the types of its parts. When it sees `x + y`, it generates constraints saying the types of `x` and `y` must both be numeric and the result type must also be numeric. When it sees a function application `f(a)`, it generates a constraint saying the type of `f` must be a function from the type of `a` to some fresh **type variable** representing the unknown result type. Type variables are placeholders — they stand for types the compiler hasn't determined yet, much like unknowns in a system of equations. A function definition `fun x -> x + 1` generates constraints that the parameter `x` must be an integer (because it's added to 1) and the return type must also be an integer.

Once all constraints are collected, the compiler feeds them to the **unification algorithm**. Unification takes pairs of type expressions and finds a **most general unifier** — a substitution mapping type variables to concrete types (or to other type variables) that satisfies every constraint simultaneously. If `α = int` and `β = α → int`, unification produces `{α ↦ int, β ↦ int → int}`. The "most general" part matters: the algorithm avoids over-specializing. If the constraints don't force `α` to be any specific type, unification leaves it as a type variable, which means the expression is **polymorphic** — it works for any type. This is how languages like ML and Haskell infer that `fun x -> x` has type `α → α` (the identity function works for all types) without the programmer writing a single annotation.

Inference can fail in two ways. A **type error** occurs when unification finds contradictory constraints — for instance, if one constraint says `α = int` and another says `α = string`. The compiler reports this as a type mismatch. The **occurs check** catches a subtler problem: if solving requires `α = list(α)`, the type would be infinitely recursive, which most type systems reject. Modern type inference algorithms handle these cases with clear error messages, but the core algorithm remains the same generate-then-unify pipeline. Understanding this pipeline demystifies the "magic" of languages where types seem to appear from nowhere — the compiler is simply solving a constraint system that the program's structure defines implicitly.
