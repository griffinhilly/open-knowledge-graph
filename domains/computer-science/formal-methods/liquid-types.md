---
id: liquid-types
title: Liquid Types
domain: computer-science
course: formal-methods
prerequisites:
- id: refinement-types
  type: hard
- id: smt-solving-theories
  type: hard
- id: predicate-logic-introduction
  type: soft
builds-toward: []
tags:
- liquid-haskell
- refinement-types
- smt-based-verification
- subtyping
- fluid-typing
- automatic-verification
stage: expert
status: validated
---

# Liquid Types

## Core Idea

Liquid types refine dependent types with **liquid type checking** — a technique that restricts refinements to a decidable subset of predicates (typically quantifier-free linear arithmetic), enabling fully automatic type checking via SMT solving. Rather than requiring users to manually prove type constraints (as in full dependent type theory), a liquid type checker automatically discharges proof obligations using an SMT solver. A liquid type for a list might be `[Int]<{v:Int | v > 0}>` (a list of positive integers). The type checker enforces this by verifying that all list-construction operations produce values satisfying the refinement, using SMT calls internally. **Liquid Haskell** is the most mature implementation, embedding liquid types into Haskell for practical verification without sacrificing automation or ease of use.

## Questions

```yaml
- question: "A function is declared with liquid type `incr :: x:{Int | x >= 0} -> {y:Int | y > x}`. What does the type checker verify when this function is called with argument 5?"
  type: short-answer
  answer: "The type checker verifies that: (1) the argument 5 satisfies the precondition {x:Int | x >= 0} (which it does: 5 >= 0), and (2) assuming the function is correctly implemented, the returned value satisfies the postcondition {y:Int | y > x} where x is bound to 5 (so the return value must be > 5). If the function actually returns an Int without additional constraints, the type checker would report an error unless the function is proven to satisfy the stronger output type. The SMT solver is used internally to check these logical constraints."
  explanation: "Liquid type checking turns type verification into SMT problems. Each function call generates constraints that the SMT solver discharges. For the call `incr(5)`, the solver checks: does 5 satisfy the precondition? (yes: 5 >= 0 is satisfiable). Does the function's implementation guarantee the postcondition? (type checker recursively checks the function body). The power is that the user writes types with logical refinements, and the checker automates the reasoning rather than requiring manual proofs."

- question: "Liquid types restrict refinement predicates to a decidable fragment (typically quantifier-free linear arithmetic). Why not allow arbitrary logic like full first-order logic?"
  type: short-answer
  answer: "Arbitrary first-order logic is undecidable — no algorithm can determine whether a formula is satisfiable. This would make type checking undecidable, requiring the user to provide manual proofs. By restricting to quantifier-free linear arithmetic (QF_LIA) or similar decidable theories, liquid type checking becomes a decision problem: the SMT solver always terminates with a yes/no answer. This enables fully automatic type checking without user-written proofs, though it limits the expressiveness of refinements to quantifier-free predicates."
  explanation: "The name 'liquid' captures the idea: types are 'liquid' (fluid, flexible) in their expressiveness — you can refine any type with any quantifier-free predicate. But they're not so expressive that checking becomes undecidable. This is a careful balance: dependent types (like Coq or Agda) have full expressiveness but require users to prove refinement properties; liquid types have restricted expressiveness but automatic checking. Research into more expressive logics (e.g., allowing some quantifiers in restricted forms) is ongoing."

- question: "Liquid Haskell verifies a function `divide :: x:Nat -> y:{Nat | y != 0} -> Nat`. When type-checking a call `divide(10, 0)`, what happens?"
  type: multiple-choice
  options:
    - "The function executes and raises a runtime error"
    - "The type checker rejects the program at compile time because the argument 0 does not satisfy the liquid type {y:Nat | y != 0}"
    - "The type checker warns but allows the code to compile"
    - "The type checker asks the user to provide a proof that 0 != 0"
  answer: 1
  explanation: "Liquid type checking is compile-time verification. The SMT solver checks whether the argument 0 satisfies the constraint y != 0. Since 0 = 0 is true (the constraint is unsatisfiable), the solver reports UNSAT and the type checker rejects the program. No runtime error occurs because the error is caught statically. This is the power of refinement types: division-by-zero is no longer a runtime error but a compile-time type error, caught before the program executes."

- question: "Consider a function `sum :: xs:[Int]<{v:Int | v > 0}> -> {n:Int | n > 0}` that sums a non-empty list of positive integers. How would a liquid type checker verify this?"
  type: short-answer
  answer: "The type checker would verify: (1) the input is a list of integers, each greater than 0; (2) the output is an integer greater than 0. For the function body (likely a recursion or fold), the checker generates proof obligations for each expression: if you sum positive integers, the result is positive. The SMT solver checks this arithmetic property automatically. If the function is correctly implemented, all obligations are discharged (the solver returns SAT); if not, the solver finds a counterexample (an input that violates the postcondition)."
  explanation: "This example shows liquid types in action: instead of manually proving 'sum of positive integers is positive,' you write the types with logical refinements and the checker verifies them. The SMT solver handles the arithmetic reasoning, making it practical for real code. This is the key advantage over full dependent types: you avoid writing explicit proofs while still getting strong correctness guarantees."
```

## Explainer

**Dependent types** (in languages like Coq or Agda) allow types to depend on values, enabling extremely expressive type systems that can express complex properties. A dependent type `Vec(n)` represents vectors of exactly length n; you can express "the result is a list of length equal to the input" as a type. But dependent types come at a cost: verifying that a function satisfies its dependent type requires manual proofs, and the proof process is interactive and labor-intensive.

**Liquid types** strike a pragmatic balance. They refine ordinary types with logical predicates (drawn from a decidable logic), enabling strong correctness guarantees without manual proofs. The refinement is expressed as a **liquid type annotation** — a predicate that values of that type must satisfy. A liquid type for a list of positive integers is `{xs : [Int] | all(xs, \x -> x > 0)}` (in Liquid Haskell: `[Int]<{v:Int | v > 0}>`). The type checker automatically verifies that list operations maintain this invariant using SMT solving.

The key innovation is the restriction to **decidable logics**, typically **quantifier-free linear arithmetic** (QF_LIA) over integers. This logic is expressive enough to reason about:
- Numeric bounds (x >= 0, x < 100)
- Arithmetic relationships (y = x + 1, n > sum)
- Logical combinations (x > 0 && y < 10)

But it excludes:
- Unrestricted quantification (∃x. P(x) for arbitrary P)
- Nonlinear arithmetic (x * y > 0, when x and y are variables)
- General recursion and induction

Restricting to this fragment makes the decision problem tractable: an SMT solver like Z3 can always determine whether a constraint is satisfiable in bounded time.

**Liquid Haskell** (developed at UC San Diego) is the most mature implementation. Users write Haskell code with liquid type annotations:

```haskell
-- A natural number (Int >= 0)
{-@ type Nat = {v:Int | v >= 0} @-}

-- A function that divides x by y, where y != 0
{-@ divide :: x:Int -> y:{Int | y != 0} -> Int @-}
divide x y = x `div` y
```

When this function is called with a non-zero divisor (e.g., `divide(10, 3)`), the type checker verifies the constraint is satisfied. If called with zero (e.g., `divide(10, 0)`), the checker rejects it at compile time — division by zero is a type error, not a runtime error. The user writes the type annotation once; the checker verifies it everywhere the function is called.

The checking process is fully automatic: the type checker generates SMT queries and delegates them to a solver (typically Z3). No user-written proofs, no interactive tactic languages, no expertise in formal logic required. This automation is the pragmatic breakthrough that makes liquid types practical for real code.

**Applications include:**

- **NASA/JPL verification**: Liquid Haskell has been applied to verify properties of spacecraft control software.
- **Industry adoption**: Used at companies like Google and others for code verification without the burden of interactive theorem proving.
- **Specification libraries**: Liquid Haskell includes libraries with refined types for standard data structures (lists, sets, maps) with properties like sortedness, disjointness, and size.

The limitations are inherent to the decidable logic restriction: you cannot express arbitrary mathematical properties or non-linear constraints. But for the common case of verifying safety and liveness properties (bounds, non-negativity, ordering, absence of errors), the automatic checking makes liquid types a practical and popular choice.

Current research extends liquid types to more expressive logics (nonlinear arithmetic with limited quantification, temporal properties) while maintaining decidability, and integrates them with other type system features (generics, polymorphism, modules) for real-world software verification.
