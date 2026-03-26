---
id: normal-forms-cnf-dnf
title: Conjunctive and Disjunctive Normal Forms
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: tautologies-and-contradictions
  type: hard
- id: boolean-algebra
  type: soft
- id: truth-tables
  type: soft
builds-toward:
- propositional-compactness
- sequent-calculus-intro
tags:
- CNF
- DNF
- normal-form
- clause
- literal
stage: formal-systems
status: validated
---

# Conjunctive and Disjunctive Normal Forms

## Core Idea
Every propositional formula can be converted to conjunctive normal form (CNF — a conjunction of disjunctions of literals) or disjunctive normal form (DNF — a disjunction of conjunctions of literals). CNF is fundamental to SAT solving and the resolution proof method; DNF makes satisfiability checking easy (a DNF is satisfiable iff any conjunct is consistent). The conversion uses De Morgan's laws, double negation elimination, and distribution. Normal forms provide canonical representations that simplify algorithmic reasoning about formulas.

## How It's Best Learned
Convert the same formula to both CNF and DNF by hand. Verify satisfiability directly from the DNF and check validity via the CNF. Use truth tables to confirm equivalence.

## Common Misconceptions
- CNF and DNF are not unique — a formula has many equivalent CNF/DNF representations.
- A CNF formula with an empty clause is always false; a DNF with an empty conjunct is always true.

## Questions

```yaml
- question: "You have a propositional formula in DNF. Which reasoning task can be checked most efficiently directly from the DNF structure?"
  type: multiple-choice
  options:
    - "Validity (is the formula true in all models?)"
    - "Satisfiability (is there any model that makes the formula true?)"
    - "Equivalence to another formula"
    - "Converting to CNF"
  answer: 1
  explanation: "DNF makes satisfiability trivially easy: a DNF formula is satisfiable if and only if at least one conjunct is consistent — contains no literal and its negation. Just scan each conjunct for a contradiction; if none has one, the formula is satisfiable. Validity, by contrast, is hard in DNF (every conjunct must be a tautology). CNF reverses this: satisfiability is hard (the NP-complete SAT problem), but checking whether the formula can be falsified is easy (does any clause have all literals simultaneously falsifiable?)."

- question: "What is the CNF of ¬(p ∧ ¬q)?"
  type: multiple-choice
  options:
    - "p ∧ ¬q"
    - "¬p ∧ q"
    - "¬p ∨ q"
    - "p ∨ ¬q"
  answer: 2
  explanation: "Apply De Morgan's law: ¬(p ∧ ¬q) = ¬p ∨ ¬(¬q) = ¬p ∨ q. This is already a single clause (a disjunction of literals), so it is in CNF. The result is ¬p ∨ q. Note that this is also in DNF (a single conjunct with two literals is degenerate — a single-literal DNF). The key step is recognizing that De Morgan's law converts ¬(A ∧ B) into ¬A ∨ ¬B, pushing the negation inward."

- question: "A DNF formula is satisfiable if and only if it contains at least one conjunct that does not contain both a literal and its negation."
  type: true-false
  answer: true
  explanation: "A DNF conjunct (like p ∧ ¬q ∧ r) is satisfiable exactly when it is internally consistent — no variable appears both positively and negated in the same conjunct. If such an assignment exists for one conjunct, the whole DNF is satisfiable (set variables to satisfy that conjunct; ignore other conjuncts). If every conjunct contains a complementary literal pair (p and ¬p), every conjunct is a contradiction, so the formula is unsatisfiable. This makes DNF satisfiability a linear-time check."

- question: "Nearly every propositional formula has a unique CNF representation."
  type: true-false
  answer: false
  explanation: "CNF and DNF representations are NOT unique. A formula can have many equivalent CNF representations. For example, (p ∨ q) and (p ∨ q) ∧ (p ∨ q) are logically equivalent CNFs of the same formula. The canonical CNF derived from a truth table (one clause per falsifying row) is unique, but general CNF conversion does not produce a canonical form. The misconception of uniqueness likely comes from conflating 'normal form' with 'canonical form' — normal forms impose structural constraints, not uniqueness."

- question: "Why is CNF, rather than DNF, the standard input format for modern SAT solvers, even though DNF makes satisfiability easy to check?"
  type: short-answer
  answer: "DNF makes satisfiability easy for a single formula, but converting an arbitrary formula to DNF can cause an exponential blowup in size. A formula with n variables may have a DNF with up to 2ⁿ conjuncts. SAT solvers instead work on CNF, where the resolution proof method operates efficiently: two clauses (A ∨ p) and (B ∨ ¬p) resolve to (A ∨ B), eliminating a variable. Resolution requires CNF structure. While CNF satisfiability is NP-complete in theory, modern DPLL/CDCL solvers exploit CNF's clause structure to prune the search space dramatically in practice."
  explanation: "The tradeoff is: DNF gives you an easy satisfiability check but blows up in size during conversion; CNF stays compact but makes satisfiability hard. For practical automated reasoning, the compactness of CNF and the tractability of resolution outweigh the theoretical ease of DNF satisfiability checking."
```

## Explainer

You know from truth tables and Boolean algebra that any propositional formula defines a truth function — a mapping from truth assignments to true/false. Normal forms are **canonical structural representations** of those truth functions. Instead of an arbitrary tangle of connectives, CNF and DNF impose a uniform two-level structure that makes certain reasoning tasks dramatically easier.

A **literal** is an atom or its negation: p, ¬p, q, ¬q, and so on. A **clause** in CNF is a disjunction of literals (p ∨ ¬q ∨ r), and a **CNF formula** is a conjunction of clauses — "AND of ORs." A **conjunct** in DNF is a conjunction of literals (p ∧ ¬q ∧ r), and a **DNF formula** is a disjunction of conjuncts — "OR of ANDs." The key insight is that these two structures trade off which reasoning task is easy. In DNF, **satisfiability** is trivial: a DNF is satisfiable if and only if at least one conjunct is internally consistent (contains no literal and its negation). In CNF, **falsifiability** is trivial: a CNF is falsifiable if and only if at least one clause can be made false. Correspondingly, checking DNF validity is hard (every conjunct must be a tautology), while checking CNF satisfiability is hard (the SAT problem).

The conversion procedure builds on De Morgan's laws and distribution. To reach CNF: push negations inward using De Morgan's (¬(A ∧ B) → ¬A ∨ ¬B, ¬(A ∨ B) → ¬A ∧ ¬B), eliminate double negations, then distribute ∨ over ∧ to "open up" each clause. To reach DNF: push negations inward, eliminate double negations, then distribute ∧ over ∨. A shortcut via truth tables: read off a DNF directly by writing one conjunct per row where the formula is true (the **canonical DNF** or **sum of minterms**), or a CNF by writing one clause per row where the formula is false.

CNF is ubiquitous in computational logic because the SAT problem — is this CNF formula satisfiable? — is the canonical NP-complete problem, and modern SAT solvers require CNF input. The **resolution proof method** (which you will encounter next) works exclusively on CNF: two clauses (A ∨ p) and (B ∨ ¬p) resolve to (A ∨ B) by eliminating the complementary literal pair. Understanding CNF as a data structure, not just a normal form, is the key to seeing why so much of automated reasoning is built on it.
