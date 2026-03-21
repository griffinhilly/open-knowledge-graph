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

## Questions

```yaml
- question: "Presburger arithmetic (natural numbers with addition only) is decidable. Adding multiplication to obtain full Peano arithmetic makes it undecidable. What is the key reason multiplication crosses this boundary?"
  type: multiple-choice
  options:
    - "Multiplication produces larger numbers that overflow the decision procedure's memory"
    - "Multiplication allows the theory to encode arbitrary computations, enabling diagonalization arguments that show no algorithm can decide all sentences"
    - "Multiplication is simply too slow to compute within a bounded time for arbitrary sentences"
    - "Adding multiplication violates the quantifier-elimination property that Presburger arithmetic satisfies"
  answer: 1
  explanation: "Multiplication enables the theory to express arbitrarily complex computational processes — including the very computations that Gödel and Turing used to prove incompleteness and undecidability. Once a theory can encode the natural numbers with multiplication, you can represent Turing machine computations inside the theory, and then diagonalization arguments show that no algorithm can decide all sentences. Presburger arithmetic avoids this by being restricted to linear arithmetic, which cannot define notions like 'x is prime' or simulate arbitrary computations."

- question: "A logician claims she has a decision procedure for a new first-order theory T. What must her procedure guarantee?"
  type: multiple-choice
  options:
    - "For every sentence φ, the procedure eventually proves φ or finds a counterexample, but may run forever on some inputs"
    - "For every sentence φ in T's language, the procedure always halts and correctly outputs whether T entails φ"
    - "The procedure can decide any sentence provable from T in fewer than one million proof steps"
    - "The procedure works for all quantifier-free sentences but may loop on quantified formulas"
  answer: 1
  explanation: "A decision procedure for a theory T is an algorithm that, given any sentence φ in T's language, always halts and outputs 'yes' (T entails φ) or 'no' (T does not entail φ). The key requirements are: (1) it must handle ALL sentences in the language, not just some; (2) it must always halt — it cannot run forever on any input. A procedure that sometimes loops or only handles a fragment of the language does not qualify. This is what separates decidable theories from merely consistent or complete ones."

- question: "Tarski proved that the theory of real closed fields (first-order geometry and real algebra with + , ×, <) is decidable — meaning questions like 'does this system of polynomial inequalities have a real solution?' are algorithmically answerable."
  type: true-false
  answer: true
  explanation: "Tarski's decidability result for real closed fields is remarkable: despite involving both addition and multiplication (which makes integer arithmetic undecidable), the theory of the real numbers is decidable. The key is that real multiplication does not enable the same diagonalization tricks as integer multiplication. Tarski proved this via quantifier elimination: every first-order statement about the reals is equivalent to a quantifier-free statement. This implies all of Euclidean geometry is decidable, since geometric statements can be encoded in real algebra."

- question: "An undecidable theory has no provable theorems — no individual sentence in the theory can be proved."
  type: true-false
  answer: false
  explanation: "This is a critical misconception. Undecidability means no single algorithm can decide ALL sentences — but many individual sentences are easily proved (or disproved). Peano arithmetic is undecidable, yet mathematicians prove theorems about arithmetic constantly. Undecidability means the algorithmic decision problem has no solution as a whole: there is no uniform procedure that works for every sentence. Individual proofs can still be found; we just cannot automate proof discovery for the entire theory."

- question: "Why does multiplication create undecidability in arithmetic when addition alone (Presburger arithmetic) does not, and what technique is used to prove decidability for fragments like Presburger?"
  type: short-answer
  answer: "Multiplication enables a theory to encode arbitrary computations: Gödel numbering and the representation of Turing machine executions inside arithmetic both rely on multiplication's power to express exponential growth and primality. Once you can simulate computations, undecidability follows by diagonalization — any algorithm claiming to decide all sentences can be given a sentence that asks whether that very algorithm halts, producing a contradiction. Presburger arithmetic lacks this expressive power: it can only express linear constraints and cannot define primality or divisibility in full generality. Decidability of Presburger arithmetic is proved by quantifier elimination: every formula is shown equivalent to a quantifier-free formula, reducing decision to finite checking of linear inequalities and congruences."
  explanation: "The contrast between Presburger and Peano arithmetic illustrates a general principle: decidability is exquisitely sensitive to expressive power. Adding a single operation (multiplication) crosses from decidable to undecidable. Quantifier elimination is the main constructive technique for proving decidability — it shows not just that a decision procedure exists but gives one, even if the resulting algorithm may be extremely slow (doubly exponential for Presburger). Understanding where the decidability boundary lies for a theory is one of the central problems of mathematical logic."
```

## Explainer

You already know that some problems are undecidable — no Turing machine can solve them for all inputs. You also know that formal theories express facts about mathematical structures in first-order logic. **Decidability of a theory** asks a specific algorithmic question: given an arbitrary sentence in the theory's language, is there a procedure that always halts and says "yes, this follows from the theory" or "no, this does not"? This is a question about the theory as a whole, not about any individual sentence.

The key technique for proving a theory *decidable* is **quantifier elimination**: show that every formula in the language is logically equivalent to a quantifier-free formula within the theory. If this holds, then to decide any sentence (a closed formula with no free variables), you need only evaluate a quantifier-free formula on the relevant constants — and quantifier-free evaluation is typically straightforward. **Presburger arithmetic** — the theory of natural numbers with addition but no multiplication — admits quantifier elimination: any statement about sums of numbers can be reduced to checking a finite combination of linear inequalities and congruence conditions. This gives a decision procedure, albeit one that runs in at least doubly exponential time.

The contrast with **Peano arithmetic** (addition and multiplication both present) is sharp. Gödel's incompleteness theorems and Turing/Church's work on undecidability both show that full first-order arithmetic is undecidable: no algorithm can determine all arithmetical truths. The culprit is multiplication, which lets you encode arbitrary computations and diagonalization arguments inside arithmetic. Presburger arithmetic avoids this by stripping out multiplication — it can express linear arithmetic but cannot define the notion of "x is a prime" or "x divides y" in full generality.

**Tarski's theorem on real closed fields** is another striking decidable theory: all of first-order geometry and real algebra (involving + , ×, <, and real-valued constants) is decidable. This means questions like "does this system of polynomial inequalities have a real solution?" are algorithmically decidable. The proof again uses quantifier elimination — every first-order statement about the real numbers is equivalent to a quantifier-free statement — via the Cylindrical Algebraic Decomposition or related methods. This result implies that Euclidean geometry is decidable, which is remarkable given how rich geometry seems.

The meta-lesson is that decidability is highly sensitive to expressive power. Monadic second-order logic over strings is decidable (Büchi's theorem), but adding a single binary relation that isn't definable from the linear order makes it undecidable. The boundary between decidable and undecidable often lies at whether a theory can encode the natural numbers with multiplication — once it can, Gödel-style arguments kick in and undecidability follows. Locating this boundary for a given theory is one of the central projects of mathematical logic.
