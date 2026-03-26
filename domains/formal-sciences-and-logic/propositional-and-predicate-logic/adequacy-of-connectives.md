---
id: adequacy-of-connectives
title: Adequacy and Completeness of Connective Sets
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-equivalence-propositional
  type: hard
builds-toward:
- normal-forms-cnf-dnf
tags:
- semantics
- completeness
- propositional
stage: formal-systems
status: validated
---

# Adequacy and Completeness of Connective Sets

## Core Idea
A set of connectives is adequate if every truth function can be expressed using only those connectives. For example, {¬, ∧, ∨} is adequate, as is {¬, →}, but {∧, ∨} alone is not. Adequacy shows which minimal collections suffice to capture all logical structure.

## Questions

```yaml
- question: "Why is {∧, ∨} not an adequate set of connectives for propositional logic?"
  type: multiple-choice
  options:
    - "Because ∧ and ∨ cannot express conditional (→) statements"
    - "Because every formula built from only ∧ and ∨ is a monotone function, and negation is non-monotone so it cannot be expressed"
    - "Because {∧, ∨} requires too many connectives — only single connectives can be adequate"
    - "Because ∧ and ∨ share the same truth table when both inputs are true"
  answer: 1
  explanation: "The structural argument for non-adequacy of {∧, ∨} is monotonicity: every formula built using only ∧ and ∨ has the property that flipping any variable from F to T can never change the output from T to F. But negation is not monotone — ¬T = F, so flipping the input from F to T flips the output from T to F. Since monotonicity is preserved by ∧ and ∨ and negation violates it, negation cannot be expressed using only {∧, ∨}. This is not about expressibility of specific connectives (option A) but about a fundamental structural property the inadequate set cannot simulate."

- question: "Which of the following is a singly adequate connective — one that can express all truth functions by itself?"
  type: multiple-choice
  options:
    - "Disjunction (∨), because any formula can be written as a disjunction of cases"
    - "Conditional (→), because → combined with itself can simulate all other connectives"
    - "NAND (↑), because ¬p ≡ p ↑ p and p ∧ q ≡ (p ↑ q) ↑ (p ↑ q)"
    - "Exclusive-OR (⊕), because any two truth values can be combined with XOR"
  answer: 2
  explanation: "NAND (p ↑ q, true unless both are true) is singly adequate. You can derive: ¬p ≡ p ↑ p (NAND with itself = negation), and p ∧ q ≡ (p ↑ q) ↑ (p ↑ q) (negate the NAND). With negation and conjunction, {¬, ∧} is adequate, so NAND alone suffices. Disjunction (option A) is not adequate alone — it cannot express negation. Conditional (option B) cannot express constant-false or negation without a false constant. XOR (option D) is not adequate — it can only express parity functions and cannot simulate conjunction."

- question: "The set {¬, →} is an adequate set of connectives because negation and the conditional together can express all truth functions."
  type: true-false
  answer: true
  explanation: "This follows by showing {¬, →} can simulate all connectives in {¬, ∧, ∨}, which is already known adequate. The key step: p ∨ q ≡ ¬p → q (if not-p then q). Once you have ¬ and ∨, De Morgan's gives ∧. So {¬, →} can express ¬, ∧, and ∨, and since {¬, ∧, ∨} is adequate (any truth function can be written in DNF), {¬, →} inherits adequacy. This is why Hilbert-style proof systems for propositional logic often use only {¬, →} as primitive connectives."

- question: "A set of connectives is adequate if and primarily if it contains at least three connectives."
  type: true-false
  answer: false
  explanation: "This is wrong in both directions. NAND alone (a single connective) is adequate — so fewer than three suffices. Meanwhile, {∧, ∨, →} contains three connectives but is not adequate, because no combination of these can express negation: every formula using only ∧, ∨, → evaluates to T when all variables are T, so the constant-false function ⊥ and ¬p are both inexpressible. Adequacy depends on the logical structure of the connectives chosen, not merely their number."

- question: "Prove informally that {∧, ∨} is not an adequate set of connectives by identifying a structural property that all formulas built from only ∧ and ∨ share."
  type: short-answer
  answer: "Every formula built from only ∧ and ∨ is monotone: if you flip any variable's value from F to T, the output can only stay the same or change from F to T — it can never change from T to F. This is because ∧ and ∨ are each monotone operations (making an input 'more true' can only make the output 'more true'), and the composition of monotone functions is monotone. Negation violates monotonicity — when p = T, ¬p = F, so flipping p from F to T flips the output from T to F. Since monotonicity is preserved by {∧, ∨} but negation is not monotone, negation cannot be expressed."
  explanation: "This proof technique — finding a structural invariant that the target function violates — is the standard approach to proving non-adequacy. Rather than trying all possible formulas (infinitely many), you identify a property that every formula in the set must satisfy, then show the target truth function lacks that property. The same technique proves that {→} alone is not adequate (all tautologies map all-T inputs to T, so constant-false is inexpressible)."
```

## Explainer

A **truth function** for n variables is simply a function from {T, F}^n to {T, F} — a complete specification of an output for every combination of input truth values. For one variable there are 4 such functions (constant-T, constant-F, identity, negation); for two variables there are 16. The question of adequacy asks: which sets of logical connectives can express *all* such functions? From your prerequisite study of logical equivalence, you already know that ¬, ∧, and ∨ together are sufficient, because every truth function can be written in disjunctive normal form (DNF) — an OR of ANDs of possibly negated variables. This is the baseline: {¬, ∧, ∨} is adequate.

The interesting question is which *smaller* sets are adequate. {¬, ∧} is adequate because ∨ can be recovered: p ∨ q ≡ ¬(¬p ∧ ¬q) by De Morgan's law. {¬, ∨} is adequate by the symmetric argument. {¬, →} is adequate because p → q ≡ ¬p ∨ q, and negation lets you recover disjunction. But {∧, ∨} alone fails: every formula built from only ∧ and ∨ is a **monotone** function — flipping any input from F to T can never flip the output from T to F. Since negation is not monotone, it cannot be expressed in {∧, ∨}. This is an example of proving *non*-adequacy by identifying a structural invariant preserved by the inadequate set.

More surprisingly, even single connectives can be adequate. The **NAND** connective p ↑ q (true unless both p and q are true) is adequate alone: ¬p ≡ p ↑ p, and p ∧ q ≡ (p ↑ q) ↑ (p ↑ q). The **NOR** connective p ↓ q (true only when both are false) is also singly adequate: ¬p ≡ p ↓ p, and p ∨ q ≡ (p ↓ p) ↓ (q ↓ q). These are the only binary connectives that are singly adequate, a fact you can verify by checking all 16 two-variable connectives for the structural properties necessary to simulate negation and conjunction.

Adequacy matters beyond its own sake because it tells you how much expressible content a logic has. In digital circuit design, NAND and NOR gates are universal — any circuit can be built from one gate type alone, which is why hardware manufactures favor them. In proof theory, a Hilbert system using {¬, →} as primitive connectives is complete (adequate), meaning its axioms can express any tautology; proofs using only those connectives are sufficient. When you build a formal logic, choosing your primitive connectives determines what the language can say, and adequacy is the exact criterion for expressive completeness at the level of propositional truth functions.
