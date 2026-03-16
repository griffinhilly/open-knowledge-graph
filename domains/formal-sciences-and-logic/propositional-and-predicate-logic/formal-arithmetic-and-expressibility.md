---
id: formal-arithmetic-and-expressibility
title: Formal Arithmetic and Expressibility
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: mathematical-induction
  type: soft
- id: natural-numbers-as-iterative-construction
  type: soft
- id: arithmetic-functions-and-multiplicativity
  type: soft
builds-toward:
- godels-incompleteness-theorems
- decidability-and-undecidability
tags:
- Peano-arithmetic
- formal-arithmetic
- representability
- primitive-recursion
stage: formal-systems
status: validated
---

# Formal Arithmetic and Expressibility

## Core Idea
Peano Arithmetic (PA) is a first-order theory with axioms for zero, successor, addition, and multiplication, plus an induction schema. PA is powerful enough to express and prove a vast range of arithmetic truths. A key concept is representability: a function f is representable in PA if there is a formula φ(x, y) such that PA proves φ(n, f(n)) for each numeral n and PA proves ∀y(φ(n, y) → y = f(n)). Gödel showed that all primitive recursive functions are representable in PA, which is the technical foundation for encoding proofs as numbers (Gödel numbering).

## How It's Best Learned
Write out the Peano axioms explicitly and verify small arithmetic facts from them. Trace Gödel numbering on a simple formula to see how syntax becomes arithmetic. The induction schema is an axiom scheme, not a single axiom.

## Common Misconceptions
- PA is not the same as 'all of mathematics' — it cannot prove the consistency of set theory or many combinatorial principles.
- The induction axiom schema has infinitely many instances (one per formula), not just one.

## Questions

```yaml
- question: "Which of the following best describes what it means for a function f to be 'representable' in Peano Arithmetic?"
  type: multiple-choice
  options: ["f is computable by a Turing machine", "There is a formula φ(x,y) such that PA proves φ(n, f(n)) for each n and PA proves f(n) is the unique value satisfying φ(n,y)", "f can be expressed using only the symbols +, ×, 0, and S", "f is provably total in PA"]
  answer: 1
  explanation: "Representability requires two things: PA must prove each specific instance φ(n, f(n)) (the formula is satisfied by the correct value), and PA must prove uniqueness — that f(n) is the *only* value satisfying φ(n, y). The uniqueness condition is critical; without it, the formula wouldn't pin down f as a function. Mere Turing computability or syntactic expressibility is not sufficient for representability."

- question: "The induction axiom of Peano Arithmetic is a single axiom."
  type: true-false
  answer: false
  explanation: "The induction 'axiom' is actually an axiom *schema* — an infinite family of axioms, one for each formula φ in the language of arithmetic. For each formula φ(n), PA includes: (φ(0) ∧ ∀n(φ(n) → φ(n+1))) → ∀n φ(n). Because there are infinitely many formulas, there are infinitely many induction axioms. This is why PA cannot be finitely axiomatized."

- question: "Why did Gödel need to develop Gödel numbering, and what does it accomplish?"
  type: short-answer
  answer: "Gödel numbering assigns a unique natural number to every formula and proof in PA's language, translating syntactic properties of proofs into arithmetic properties of numbers. This allows PA to express statements about its own provability as arithmetic formulas."
  explanation: "The incompleteness proof requires constructing a sentence that says 'I am not provable in PA.' For PA to 'talk about' provability, statements about proofs — a syntactic notion — must become arithmetic statements. Gödel numbering provides this translation. Once proofs are numbers, 'x is a proof of formula y' becomes a primitive recursive relation, which is representable in PA by the representability theorem."
```

## Explainer

Peano Arithmetic (PA) is the standard first-order formalization of the natural numbers. Its non-logical axioms assert that 0 is a number, that the successor function S is injective and never returns 0, and that addition and multiplication satisfy their standard recursive definitions. These constraints look simple, but together with the induction schema they generate an enormous body of mathematics. Most theorems of elementary number theory — divisibility, primality, the Chinese Remainder Theorem — are provable in PA.

The induction axiom schema is often misunderstood as a single axiom. It is not. It is a template generating infinitely many axioms, one for each formula φ in the language. For any formula φ(n), PA contains: "if φ holds at 0 and φ holding at n implies φ holds at n+1, then φ holds for all n." Because there are infinitely many formulas in first-order logic, there are infinitely many induction axioms. This is why PA cannot be finitely axiomatized — a deep result connected to Gödel's theorem itself.

The concept of *representability* is the technical bridge between arithmetic and metamathematics. A function f is representable in PA if there is a formula φ(x, y) such that PA proves φ(n, f(n)) for each concrete numeral n, and PA also proves that f(n) is the *unique* value satisfying φ(n, y). This two-part condition — existence and uniqueness — ensures that φ captures exactly the graph of f. Gödel's key lemma is that all primitive recursive functions (addition, multiplication, exponentiation, the coding functions used in Gödel numbering) are representable in PA.

Why does representability matter? Gödel's incompleteness proof requires PA to reason about its own syntax — about which formulas are provable. To enable this, Gödel invented a coding scheme: each symbol, formula, and finite sequence of formulas (i.e., proof) is assigned a unique natural number, its *Gödel number*. Syntactic operations on proofs then become arithmetic functions on these numbers. Since those functions are primitive recursive, they are representable in PA. This means PA can literally express statements like "the number g codes a valid proof of the formula coded by n" as an arithmetic formula — the foundation on which the incompleteness theorems are built.
