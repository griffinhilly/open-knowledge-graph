---
id: decidability-of-theories
title: Decidability of Theories
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: decidability-and-undecidability
  type: hard
- id: formal-arithmetic-and-expressibility
  type: hard
builds-toward:
- godels-incompleteness-theorems
tags:
- decidable-theories
- monadic-logic
- Presburger-arithmetic
- decision-procedures
- undecidable-theories
stage: advanced
status: draft
---

# Decidability of Theories

## Core Idea
A first-order theory is decidable if there exists an algorithm that, given any sentence in the theory's language, determines whether the theory entails it. Some fragments of first-order logic are decidable: monadic predicate logic (only unary predicates, no functions), Presburger arithmetic (natural numbers with addition but no multiplication), and the theory of real closed fields (Tarski's quantifier elimination). However, full first-order arithmetic (with both addition and multiplication) is undecidable, as shown by Church and Turing. Understanding which theories are decidable and which are not reveals the boundary between mechanizable and non-mechanizable reasoning.

## How It's Best Learned
Compare Presburger arithmetic (decidable) with Peano arithmetic (undecidable) to see how adding multiplication crosses the decidability boundary. Work through a simple quantifier-elimination example in Presburger arithmetic to see a decision procedure in action.

## Common Misconceptions
- Undecidability of a theory does not mean no sentences can be proved — it means no single algorithm can decide all sentences. Many individual theorems are easily provable.
- Decidability of a fragment does not extend to the full theory — monadic logic is decidable, but adding a single binary predicate makes it undecidable.
- Quantifier elimination is a powerful technique but applies only to specific theories — it is not a general method for first-order logic.

## Explainer

You already know that some problems are undecidable — no Turing machine can solve them for all inputs. You also know that formal theories express facts about mathematical structures in first-order logic. **Decidability of a theory** asks a specific algorithmic question: given an arbitrary sentence in the theory's language, is there a procedure that always halts and says "yes, this follows from the theory" or "no, this does not"? This is a question about the theory as a whole, not about any individual sentence.

The key technique for proving a theory *decidable* is **quantifier elimination**: show that every formula in the language is logically equivalent to a quantifier-free formula within the theory. If this holds, then to decide any sentence (a closed formula with no free variables), you need only evaluate a quantifier-free formula on the relevant constants — and quantifier-free evaluation is typically straightforward. **Presburger arithmetic** — the theory of natural numbers with addition but no multiplication — admits quantifier elimination: any statement about sums of numbers can be reduced to checking a finite combination of linear inequalities and congruence conditions. This gives a decision procedure, albeit one that runs in at least doubly exponential time.

The contrast with **Peano arithmetic** (addition and multiplication both present) is sharp. Gödel's incompleteness theorems and Turing/Church's work on undecidability both show that full first-order arithmetic is undecidable: no algorithm can determine all arithmetical truths. The culprit is multiplication, which lets you encode arbitrary computations and diagonalization arguments inside arithmetic. Presburger arithmetic avoids this by stripping out multiplication — it can express linear arithmetic but cannot define the notion of "x is a prime" or "x divides y" in full generality.

**Tarski's theorem on real closed fields** is another striking decidable theory: all of first-order geometry and real algebra (involving + , ×, <, and real-valued constants) is decidable. This means questions like "does this system of polynomial inequalities have a real solution?" are algorithmically decidable. The proof again uses quantifier elimination — every first-order statement about the real numbers is equivalent to a quantifier-free statement — via the Cylindrical Algebraic Decomposition or related methods. This result implies that Euclidean geometry is decidable, which is remarkable given how rich geometry seems.

The meta-lesson is that decidability is highly sensitive to expressive power. Monadic second-order logic over strings is decidable (Büchi's theorem), but adding a single binary relation that isn't definable from the linear order makes it undecidable. The boundary between decidable and undecidable often lies at whether a theory can encode the natural numbers with multiplication — once it can, Gödel-style arguments kick in and undecidability follows. Locating this boundary for a given theory is one of the central projects of mathematical logic.
