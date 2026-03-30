---
id: refinement-types
title: Refinement Types
domain: computer-science
course: formal-methods
prerequisites:
- id: type-systems-type-checking
  type: hard
- id: dependent-type-theory
  type: soft
- id: predicate-logic
  type: soft
builds-toward: []
tags:
- liquid-types
- liquid-haskell
- smt
- predicate-refinement
- subtyping
stage: expert
status: validated
---
# Refinement Types

## Core Idea
Refinement types augment base types with logical predicates that constrain the set of values. Instead of just Int, you write {v : Int | v > 0} — the type of positive integers. A function div : Int -> {v : Int | v != 0} -> Int statically guarantees the divisor is nonzero. Unlike full dependent types, refinement predicates are restricted to decidable logics (typically quantifier-free theories handled by SMT solvers), enabling fully automatic type checking without manual proofs. Liquid types, the most successful refinement type system, infer refinement predicates automatically using abstract interpretation over types, combining the expressiveness of dependent-types-lite with the automation of type inference.

## Questions

```yaml
- question: "How does the refinement type {v : Int | v > 0 && v < 100} differ from a runtime assertion assert(v > 0 && v < 100)?"
  type: multiple-choice
  options:
    - "They check the same property but at different times: the refinement type checks statically at compile time, while the assertion checks at runtime. The refinement type guarantees the property holds on ALL executions, while the assertion only catches violations on executions that are actually run"
    - "The refinement type is less precise than the assertion"
    - "The assertion provides a formal proof while the refinement type does not"
    - "There is no meaningful difference; they are equivalent"
  answer: 0
  explanation: "This is the fundamental value proposition of refinement types: they move runtime checks to compile time. If the program type-checks, the property is guaranteed to hold in all executions without any runtime cost. If the type checker cannot prove the property, it reports a type error before the program runs. Assertions catch bugs only in executions that are actually tested. Refinement types catch all possible violations statically."

- question: "Liquid types achieve automatic type checking by restricting refinement predicates to decidable logics that SMT solvers can handle."
  type: true-false
  answer: true
  explanation: "Full dependent types allow arbitrary computations in types, making type checking undecidable and requiring manual proof effort. Liquid types restrict refinements to quantifier-free formulas over SMT-decidable theories (linear arithmetic, arrays, uninterpreted functions). This restriction means subtype checking reduces to SMT validity queries, which Z3 or CVC5 can decide automatically. The user writes type annotations (or they are inferred); the tool generates SMT queries; no manual proofs are needed. This is the key tradeoff: less expressive than full dependent types, but fully automatic."

- question: "Explain how refinement type checking reduces to SMT queries, using the example of checking that a function call div(x, y) is safe where div expects {v : Int | v != 0} as its second argument."
  type: short-answer
  answer: "At the call site div(x, y), the type checker must verify that y has type {v : Int | v != 0}. It collects the path conditions (e.g., from an enclosing 'if y != 0' branch) and the refinements of y's declared type, forming the context. It then asks the SMT solver: given the context, is y != 0 valid? If the solver says yes (valid), the call type-checks. If the solver says no (with a counterexample), the type checker reports an error showing a concrete scenario where y could be zero."
  explanation: "This reduction is what makes refinement types practical. Every subtyping check {v : T | P} <: {v : T | Q} reduces to the implication P => Q, which is an SMT query. Path-sensitivity comes from collecting predicates from conditional branches: inside 'if y != 0 then div(x, y)', the path condition y != 0 is added to the context, making the SMT query trivially valid. The programmer writes normal code with type annotations; the tool handles the rest."
```

## Explainer

Full dependent types (as in Coq or Agda) let types express arbitrarily precise specifications, but at a cost: type checking is undecidable and requires the programmer to construct proofs manually. At the other extreme, simple type systems (as in Java or Python) are fully automatic but cannot express properties like "this integer is positive" or "this list is sorted." **Refinement types** occupy a sweet spot: they extend base types with logical predicates, gaining significant expressive power while retaining automatic type checking.

A refinement type has the form {v : T | P(v)}, where T is a base type and P is a logical predicate. The type {v : Int | v > 0} contains exactly the positive integers. A function can declare `div : (x : Int) -> (y : {v : Int | v != 0}) -> Int`, making division by zero a static type error. Array access can use `get : (a : Array T) -> (i : {v : Int | 0 <= v && v < len(a)}) -> T`, making out-of-bounds access a type error. These specifications live in the type system, are checked at compile time, and carry zero runtime cost.

The key to automation is restricting predicates to **decidable theories** that SMT solvers can handle. **Liquid types**, developed by Rondon, Kawaguchi, and Jhala, restrict refinements to conjunctions of qualifiers — simple predicates from a fixed set — and use abstract interpretation to infer which qualifiers apply at each program point. Subtype checking reduces to SMT validity: {v : T | P} is a subtype of {v : T | Q} if and only if P implies Q, which the solver decides automatically. **LiquidHaskell** applies this to Haskell, enabling programmers to verify memory safety, termination, functional correctness, and information flow properties with minimal annotation burden. The tool infers most refinements automatically; the programmer adds annotations only where inference needs guidance.

Path sensitivity is crucial for practical refinement typing. Inside `if x > 0 then f(x) else g(x)`, the type of x in the then-branch is refined to {v : Int | v > 0} by the branch condition. The type checker tracks these path conditions and includes them in SMT queries. This means that idiomatic null checks, bounds checks, and error handling are automatically recognized by the type system. The programmer does not need to add explicit annotations for code that already checks its preconditions — the type system extracts the information from the control flow.

Refinement types are less expressive than full dependent types — they cannot express properties requiring quantifiers (like "for all elements in this list, P holds") without extensions. But for a large class of safety and correctness properties — array bounds, division by zero, resource protocol compliance, numeric invariants — they provide strong static guarantees with an experience closer to ordinary type checking than to theorem proving. Tools like LiquidHaskell, Flux (for Rust), and F* (which combines refinement and dependent types) demonstrate that refinement types can scale to substantial codebases while catching real bugs that conventional type systems miss.
