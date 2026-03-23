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
status: validated
---

# Unification Algorithm

## Core Idea
Unification finds a substitution that makes two terms syntactically identical. In type inference, it solves type constraints by finding variable substitutions. The algorithm recursively decomposes terms and detects occurs-check violations (a variable cannot appear in a term it must equal). Unification is fundamental to type systems and logic programming.

## Questions

```yaml
- question: "A type inference engine tries to unify the type expression `α → β` with `Int → Bool`. What is the result?"
  type: multiple-choice
  options:
    - "Failure — the arrow type constructor cannot be unified with other constructors"
    - "The substitution {α → Int, β → Bool}, making both expressions identical"
    - "The substitution {α → Bool, β → Int}, since type variables are symmetric"
    - "Success with no substitution — arrow types are always compatible"
  answer: 1
  explanation: "Unification succeeds when two compound types share the same constructor. Both expressions use `→`, so the algorithm decomposes them: unify the left components (α with Int → yields {α → Int}) and the right components (β with Bool → yields {β → Bool}). The combined substitution {α → Int, β → Bool} makes both expressions identical: Int → Bool. Option C reverses the bindings incorrectly — the algorithm matches components positionally, not arbitrarily. Option D is wrong because the substitution is necessary, not vacuous."

- question: "A programmer writes a function where, accidentally, the return type depends on itself — the function returns a list of its own return type. What does the unification algorithm do when it encounters the constraint unifying `α` with `List<α>`?"
  type: multiple-choice
  options:
    - "Succeeds and infers the type `List<List<List<...>>>` as the return type"
    - "Fails immediately with a type error, because no finite substitution can satisfy this constraint"
    - "Succeeds only if the list is empty, since an empty list has no elements to cause the cycle"
    - "Skips the constraint and continues with remaining constraints in the program"
  answer: 1
  explanation: "The occurs check detects this case and reports a type error. When the algorithm tries to bind α to List<α>, it first checks whether α appears *inside* List<α> — it does. Binding α → List<α> would create an infinite type (List<List<List<...>>>), which is unsound. The occurs check catches this before the binding is made and reports failure. Without the occurs check, the algorithm might loop infinitely trying to expand the infinite substitution, or produce an unsound result. This is why the occurs check is not optional: it prevents a class of genuine programming errors."

- question: "The occurs check in unification is an optional optimization — skipping it makes unification faster, and in practice, recursive types rarely arise in real programs."
  type: true-false
  answer: false
  explanation: "The occurs check is not optional — it is a correctness requirement. Without it, unification of a variable with a term containing that variable would succeed, creating an infinite type that represents a cyclic, unbounded data structure. This leads to either infinite loops during substitution propagation or unsound type inference. While some languages deliberately omit the occurs check to allow explicitly recursive types (with special syntax), removing it silently from a standard type system produces incorrect behavior. The distinction is not about performance optimization but about soundness."

- question: "Unifying two compound types with different constructors — for example, `List<Int>` with `Pair<Int, Bool>` — always fails, even if their component types are compatible."
  type: true-false
  answer: true
  explanation: "Constructor mismatch is an immediate and irrecoverable failure in unification. The algorithm requires both terms to have the same top-level constructor before it can recursively unify their components. `List` and `Pair` are different type constructors — they represent structurally different types — so no substitution can make `List<Int>` identical to `Pair<Int, Bool>`. The component types (Int and Bool) are irrelevant once the constructors differ. This reflects the type system's guarantee: a list and a pair are categorically different even if they contain the same element types."

- question: "Explain why the occurs check is necessary in unification and what specific error it prevents."
  type: short-answer
  answer: "The occurs check ensures that when binding a type variable α to a type term T, α does not appear anywhere inside T. Without this check, the algorithm could create the substitution {α → List<α>}, which represents an infinite type List<List<List<...>>> with no finite base. This infinite type is unsound: the type system cannot represent or reason about it correctly. The occurs check detects this by scanning T for any occurrence of α before making the binding; if found, it reports a type error. In practice, occurs-check violations usually signal real programming errors — a function that recursively wraps its own return type without a proper base case."
  explanation: "The occurs check adds a linear scan over the term being bound, which can slow unification in pathological cases. Some systems (like standard Prolog) omit it for performance, explicitly allowing infinite terms. But for type systems that must be sound, the occurs check is non-negotiable — it is the mechanism that keeps the type language finite and decidable."
```

## Explainer

From your study of type systems, you know that a type checker must verify that types are consistent across a program — that the type of an argument matches the type a function expects, that both branches of an `if` return the same type, and so on. When types are explicitly annotated, checking is straightforward comparison. But when types must be **inferred**, the compiler generates **type variables** (unknowns) and **constraints** (equations between type expressions), then solves those constraints. **Unification** is the algorithm that solves them.

The core idea is simple: given two type expressions that may contain variables, find a **substitution** — a mapping from variables to types — that makes the two expressions identical. For example, unifying the type `List<α>` with `List<Int>` yields the substitution `{α → Int}`. Unifying `α → β` with `Int → Bool` yields `{α → Int, β → Bool}`. Unifying `Int` with `Bool` fails — no substitution can make them equal. Each successful unification tells the compiler something concrete about a previously unknown type.

The algorithm works by **recursive decomposition**. To unify two terms: if both are the same constant (like `Int`), succeed with no substitution. If one is a variable, bind that variable to the other term (after the occurs check — see below). If both are compound types with the same constructor (like `List<_>` or `_ → _`), recursively unify their corresponding components. If the constructors differ (`List` vs `Pair`, or `Int` vs `Bool`), fail — the types are incompatible. Each recursive step either produces a variable binding, confirms a match, or reports an error.

The **occurs check** prevents a subtle but critical error: a variable cannot be unified with a term that contains itself. If you try to unify `α` with `List<α>`, the substitution `{α → List<α>}` would create an infinite type — `List<List<List<...>>>`. The occurs check detects this and reports a type error. Without it, the algorithm could loop infinitely or produce unsound results. In practice, occurs-check violations often signal genuine programming errors, like a function that accidentally returns a container of its own return type.

When a type inference engine processes a program, it generates many constraints and applies unification repeatedly. Each unification may bind variables that appear in other constraints, so bindings must be propagated — this is where the connection to your knowledge of dynamic programming is relevant, as efficient unification uses a **union-find** data structure to track variable equivalences without repeatedly copying substitutions. The classic Robinson unification algorithm runs in near-linear time with union-find, making it practical for compilers that must type-check millions of lines of code. Unification is also the computational heart of logic programming languages like Prolog, where it serves as both pattern matching and variable binding in a single operation.
