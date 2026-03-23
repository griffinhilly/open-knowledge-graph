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
status: validated
---

# Type Reconstruction and Inference

## Core Idea
Type reconstruction determines types for expressions where types aren't explicitly written. It generates constraints (variable must equal int, type-a must unify with type-b) and solves them via unification, producing a consistent type assignment that respects the language's type rules.

## Questions

```yaml
- question: "Algorithm W encounters the expression `let id x = x`. What type does it infer for `id`, and how does it arrive at that type?"
  type: multiple-choice
  options:
    - "id : int → int, because `x` is most likely an integer"
    - "id : α → α for a fixed but unknown type α — a single concrete type must be chosen"
    - "id : ∀α. α → α, because the type variable is unconstrained and is universally quantified at the let-binding"
    - "Algorithm W fails here because no type annotation is provided"
  answer: 2
  explanation: "When Algorithm W processes `let id x = x`, it assigns a fresh type variable α to `x`. The body is also `x`, so the result type is α too — the function has type α → α. No constraint forces α to equal any concrete type. At the let-binding, unconstrained type variables are universally quantified, yielding ∀α. α → α. This polymorphic type means `id` can be applied to values of any type — `id 42` is int, `id true` is bool, etc. Option B is wrong because Hindley-Milner uses let-polymorphism to generalize, not monomorphic type variables."

- question: "A student believes type reconstruction works by trying all possible type assignments until finding one that passes the type checker. What does Algorithm W actually do instead?"
  type: multiple-choice
  options:
    - "It uses a SAT solver to search over all possible type combinations efficiently"
    - "It traverses the syntax tree, generates type constraints from each syntactic construct, then uses unification to solve all constraints simultaneously"
    - "It runs the program symbolically and observes what types emerge at runtime"
    - "It asks the programmer for hints by flagging ambiguous expressions"
  answer: 1
  explanation: "Algorithm W is a deterministic, constraint-based algorithm, not a search. It walks the abstract syntax tree and generates type constraints mechanically: literals get concrete types, variables get fresh type variables, function applications generate constraints relating argument and result types. The resulting constraint set is solved by unification — finding a substitution that maps type variables to types in a way that satisfies all constraints simultaneously. If no solution exists, the program has a type error. The algorithm never 'tries' types; it derives them algebraically."

- question: "Algorithm W requires at least some type annotations from the programmer to reconstruct types — it cannot determine types for a completely unannotated program."
  type: true-false
  answer: false
  explanation: "This is a common misconception about type inference. The Hindley-Milner algorithm (Algorithm W) is specifically designed to reconstruct types for fully unannotated programs. The programmer writes `let f x = x + 1` with no type declarations, and the algorithm deduces `f : int → int` entirely from the structure of the expression. This is why languages like ML and Haskell require so few explicit type annotations — the type system infers types automatically from expression structure and the constraints imposed by primitive operations."

- question: "The occurs check in Algorithm W rejects the constraint α = list(α) because accepting it would require α to have an infinite type."
  type: true-false
  answer: true
  explanation: "The occurs check verifies that when solving a constraint of the form α = T, the type variable α does not appear inside T. If α does appear in T (as in α = list(α)), then the substitution would produce α ↦ list(list(list(...))) — an infinitely deep type. Most implementations of Algorithm W reject such constraints as type errors. Some systems (like those with iso-recursive types) allow controlled forms of recursive types, but standard Hindley-Milner rejects them. The occurs check is also a performance concern, as skipping it can cause unification to loop."

- question: "What is a 'principal type,' and why does it matter that Algorithm W is guaranteed to find one rather than just any valid type?"
  type: short-answer
  answer: "A principal type is the most general type valid for an expression — all other valid types are specializations (instances) of it. For `let id x = x`, the principal type is ∀α. α → α. The type `int → int` is also valid for `id`, but it is less general. Algorithm W is guaranteed to find the principal type, meaning the inferred type is never more restrictive than necessary. This matters because a more restrictive type would prevent valid uses of the function — if `id` were inferred as `int → int`, you could not apply it to booleans, even though the definition works for any type."
  explanation: "The principal type property is what makes Hindley-Milner practically useful: type inference never 'overconstrain' the programmer's code. The inferred type is exactly as polymorphic as the code warrants. Languages without principal types (like some with overloading or subtyping) may require type annotations to disambiguate, or may produce surprising results when the inferred type is more specific than intended."
```

## Explainer

From your work with type inference and unification, you know the basic pieces: type inference assigns types to expressions without explicit annotations, and unification finds substitutions that make two type expressions equal. **Type reconstruction** combines these into a complete algorithm that takes an unannotated program and either produces a valid typing for every expression or reports that no consistent typing exists.

The classic algorithm is **Algorithm W**, introduced by Damas and Milner for the Hindley-Milner type system used in ML and Haskell. It works by walking the syntax tree and generating **type constraints** at each node. When it encounters a literal like `42`, it assigns the type `int`. When it encounters a variable, it looks up its type in the environment (or assigns a fresh **type variable** like `α` if the type is unknown). When it encounters a function application `f(x)`, it generates the constraint that `f`'s type must be `typeof(x) → β` for some fresh type variable `β`, and the result type is `β`. Each syntactic construct produces constraints that relate the types of its subexpressions.

After constraint generation, the algorithm solves the constraint set using **unification**. Each constraint says two type expressions must be equal — for example, `α = int → β` or `β = bool`. Unification finds a **substitution** (a mapping from type variables to concrete types) that satisfies all constraints simultaneously. If `α` must equal `int → β` and `β` must equal `bool`, unification produces `{α ↦ int → bool, β ↦ bool}`. If constraints are contradictory — say `α = int` and `α = bool` — unification fails, and the algorithm reports a type error. The **occurs check** prevents nonsensical infinite types: if solving `α = list(α)`, the algorithm rejects it because `α` would need to be `list(list(list(...)))` infinitely.

The power of type reconstruction is that programmers write code like `let f x = x + 1` without any type annotations, and the algorithm deduces that `f : int → int`. The Hindley-Milner system guarantees a **principal type** — the most general type that is valid — and Algorithm W finds it. This means the inferred type is never less general than what the programmer intended. Polymorphic functions like `let id x = x` receive the type `∀α. α → α`, meaning `id` works for any type. The algorithm achieves this through **let-polymorphism**: at `let` bindings, type variables that are not constrained by the surrounding context are universally quantified, allowing the bound name to be used at different types in different places.
