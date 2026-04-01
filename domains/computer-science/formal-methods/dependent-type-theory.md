---
id: dependent-type-theory
title: Dependent Type Theory
domain: computer-science
course: formal-methods
prerequisites:
- id: type-systems-overview
  type: hard
- id: curry-howard-correspondence
  type: hard
- id: predicate-logic-introduction
  type: soft
builds-toward:
- refinement-types
tags:
- dependent-types
- pi-type
- sigma-type
- coq
- lean
- agda
- martin-lof
stage: expert
status: validated
---
# Dependent Type Theory

## Core Idea
Dependent type theory extends simple type systems by allowing types to depend on values. A dependent function type (Pi type) (x : A) -> B(x) represents functions whose return type varies with their input — enabling types like "a vector of exactly n elements" or "a proof that n is prime." A dependent pair type (Sigma type) (x : A, B(x)) pairs a value with a proof about that value. Through the Curry-Howard correspondence, dependent types unify programming and theorem proving: types express arbitrarily precise specifications, and well-typed programs are proofs of those specifications. Martin-Lof type theory is the foundational framework; Coq, Lean, and Agda implement variants of it.

## Questions

```yaml
- question: "What can dependent types express that simple types (like those in Haskell or Java) cannot?"
  type: multiple-choice
  options:
    - "Dependent types can express recursive data structures"
    - "Dependent types can express properties that relate values to types, such as 'a list of length n' or 'a sorted array,' embedding specifications into the type itself so that type-checking enforces correctness"
    - "Dependent types can express higher-order functions"
    - "Dependent types can express polymorphism"
  answer: 1
  explanation: "Simple type systems can express 'this is a list of integers' but not 'this is a list of exactly 5 integers' or 'this is a sorted list.' Dependent types allow types to mention values: Vec(Int, 5) is a type that depends on the value 5. A function append : Vec(A, n) -> Vec(A, m) -> Vec(A, n+m) has a return type that computes from the input lengths, making it a type error to return a vector of the wrong length. This moves invariants from runtime checks or comments into the type system where they are enforced at compile time."

- question: "In dependent type theory, the type Vec(A, 0) (a vector of zero elements) has exactly one inhabitant: the empty vector nil."
  type: true-false
  answer: true
  explanation: "Vec(A, n) is typically defined as an inductive type with two constructors: nil : Vec(A, 0) and cons : A -> Vec(A, n) -> Vec(A, n+1). Since only nil produces a Vec(A, 0), the type has exactly one inhabitant. This illustrates how dependent types encode precise invariants: the type determines the shape of the data. A function receiving Vec(A, 0) knows statically that it is the empty vector — no runtime check is needed."

- question: "Explain the Pi type (x : A) -> B(x) and how it generalizes both ordinary function types and universal quantification."
  type: short-answer
  answer: "The Pi type (x : A) -> B(x) is a function type where the return type B(x) can depend on the input value x. When B does not actually depend on x, it reduces to the ordinary function type A -> B. Under Curry-Howard, it corresponds to universal quantification: 'for all x : A, B(x).' A value of this type is a function that, given any x of type A, produces a value of type B(x) — simultaneously a program (a function) and a proof (of the universal statement)."
  explanation: "This generalization is what makes dependent type theory so powerful. Ordinary polymorphism (forall a. a -> a) is a special case where the type parameter is a type, not a value. Dependent types allow the parameter to be any value: a natural number, a list, a proof. The function head : (n : Nat) -> Vec(A, n+1) -> A takes a natural number n (which it may not even use computationally) and a non-empty vector, returning an element. The type-level computation n+1 guarantees the vector is non-empty, making a runtime bounds check unnecessary."
```

## Explainer

In simple type systems, types and values occupy separate universes: you can have a function from integers to integers (Int -> Int), but the type cannot mention a specific integer value. **Dependent type theory** breaks this barrier: types can contain and compute with values. The type Vec(Int, 5) — a vector of exactly five integers — depends on the value 5. The type Matrix(m, n) depends on dimension values. The type EqualProof(x, y) — a proof that x equals y — depends on the specific values x and y. This allows types to express arbitrarily precise specifications about the values they classify.

The two fundamental type formers are the **Pi type** and the **Sigma type**. The Pi type (x : A) -> B(x) is a dependent function type: the return type B(x) may depend on the input value x. When B does not depend on x, this is just the ordinary function type A -> B. Under Curry-Howard, Pi types correspond to universal quantification (for all x, B(x)). A function `safeDiv : (n : Int) -> (d : Int) -> (d != 0) -> Int` takes two integers and a *proof* that the divisor is nonzero, making division-by-zero a type error. The **Sigma type** (x : A, B(x)) is a dependent pair: a value x of type A together with a value of type B(x). It corresponds to existential quantification (there exists x such that B(x)). The pair `(7, proof_that_7_is_prime)` has type (x : Nat, IsPrime(x)).

The practical power of dependent types is **moving invariants from comments and tests into the type system**. A function `sort : List(A) -> SortedList(A)` that returns a type `SortedList(A)` (defined to contain a list plus a proof of sortedness) cannot return an unsorted list — type-checking would fail. The function `matmul : Matrix(m, k) -> Matrix(k, n) -> Matrix(m, n)` cannot be called with incompatible dimensions because the type checker verifies that the inner dimensions match. These constraints, which in conventional languages are checked at runtime (with crashes) or by convention (with bugs), become compile-time guarantees.

**Martin-Lof type theory** (1970s) is the foundational framework, providing the rules for constructing types, values, and judgments (type formation, introduction, elimination, computation). Modern proof assistants implement variants: Coq uses the **Calculus of Inductive Constructions** (CIC), extending Martin-Lof type theory with inductive types, universe polymorphism, and a hierarchy of type universes. Lean uses a similar foundation with added emphasis on automation and ergonomics. Agda stays closest to the Martin-Lof tradition, emphasizing direct term construction over tactic-based proof.

The main challenge with dependent types is that type-checking requires evaluating terms (since types contain values), making the type checker a partial evaluator. This is why dependent type theory requires all functions to be total (terminating): non-terminating computation in a type would make type-checking loop forever. The restriction to total functions also preserves logical consistency (via Curry-Howard, a non-terminating proof would prove anything). This constraint means that general recursion must be justified by well-founded arguments — a connection to termination analysis and well-founded orderings that practitioners must master to use dependent type theory effectively.
