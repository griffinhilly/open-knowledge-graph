---
id: satisfiability-and-unsatisfiability
title: Satisfiability and Unsatisfiability
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-consequence-and-entailment
  type: hard
builds-toward:
- consistency-and-inconsistency
tags:
- propositional-logic
- satisfiability
- sat-problem
stage: formal-systems
status: draft
---

# Satisfiability and Unsatisfiability

## Core Idea
A formula (or set of formulas) is satisfiable if there exists at least one interpretation making it true; it is unsatisfiable if no such interpretation exists. The satisfiability problem (SAT) is computationally fundamental: checking whether a propositional formula is satisfiable is NP-complete, making it one of the most important problems in computational logic.

## Questions

```yaml
- question: "A logician wants to prove that from premises P₁ and P₂, conclusion C necessarily follows. She assumes ¬C alongside P₁ and P₂ and derives a contradiction. This refutation approach works because:"
  type: multiple-choice
  options:
    - "Deriving a contradiction from ¬C proves that C is a tautology independently of any premises"
    - "The contradiction shows P₁ ∧ P₂ ∧ ¬C is unsatisfiable, which is equivalent to P₁ ∧ P₂ ⊨ C"
    - "Refutation proofs are valid only in propositional logic and do not extend to first-order logic"
    - "Deriving a contradiction from any set of assumptions proves that those assumptions are all true"
  answer: 1
  explanation: "Logical consequence (φ ⊨ ψ) holds if and only if φ ∧ ¬ψ is unsatisfiable — there is no interpretation making the premises true and the conclusion false. Refutation proofs exploit this equivalence directly: assume the negation of the conclusion, add it to the premises, and derive ⊥. If you succeed, you have shown the negated conclusion is incompatible with the premises, proving the original consequence."

- question: "A propositional formula contains 20 distinct atomic variables. Checking its satisfiability by brute-force truth table requires how many rows?"
  type: multiple-choice
  options:
    - "20 × 2 = 40 rows"
    - "20² = 400 rows"
    - "2²⁰ = 1,048,576 rows"
    - "20! rows (factorial of 20)"
  answer: 2
  explanation: "Each atomic variable can independently be assigned true or false, giving 2 options per variable. For n independent variables, the number of distinct truth assignments is 2ⁿ. With 20 variables, that is 2²⁰ = 1,048,576 rows. This exponential blowup is precisely why SAT is computationally difficult in general — truth table enumeration is not a scalable algorithm."

- question: "A formula is unsatisfiable if and only if its negation is a tautology."
  type: true-false
  answer: true
  explanation: "If φ is unsatisfiable, it is false under every interpretation. Therefore ¬φ is true under every interpretation — a tautology. Conversely, if ¬φ is a tautology (true everywhere), then φ must be false everywhere — unsatisfiable. The duality between satisfiability and tautology mirrors the duality between ∃ and ∀: satisfiability says ∃ an interpretation making φ true; being a tautology says ∀ interpretations make φ true."

- question: "Because SAT is NP-complete, modern SAT solvers cannot efficiently handle any practical satisfiability problem."
  type: true-false
  answer: false
  explanation: "NP-completeness characterizes worst-case behavior, not typical behavior. Modern SAT solvers based on CDCL (conflict-driven clause learning) exploit the structure of practical problem instances — learned clauses, propagation, heuristic branching — to solve formulas with millions of variables in seconds. Industrial applications in hardware verification, planning, and cryptanalysis rely on this practical efficiency. Worst-case hardness and practical hardness are not the same thing."

- question: "Explain the duality between satisfiability and logical consequence: how does proving that a formula is unsatisfiable allow you to establish that a consequence relationship holds?"
  type: short-answer
  answer: "φ ⊨ ψ holds if and only if φ ∧ ¬ψ is unsatisfiable. If there is no interpretation making φ true while ψ is false, then every interpretation making φ true must also make ψ true — the definition of consequence. So to prove φ ⊨ ψ, it suffices to show φ ∧ ¬ψ has no model. This is why refutation-complete proof systems (like resolution) work by negating the conclusion and deriving a contradiction."
  explanation: "The duality runs deep: semantic consequence (a model-theoretic concept) and syntactic provability (a proof-theoretic concept) are connected through satisfiability. The completeness theorem for first-order logic says these two notions coincide: φ ⊨ ψ iff φ ⊢ ψ. Both sides can be reduced to unsatisfiability checks, which is why automated theorem provers almost universally work via refutation."
```

## Explainer

From your study of logical consequence and entailment, you know that φ ⊨ ψ means every interpretation making φ true also makes ψ true. **Satisfiability** is the other fundamental semantic concept: it asks not about consequence between formulas, but about *possibility* — is there any interpretation that makes this formula true at all?

A formula φ is **satisfiable** if there exists at least one interpretation (an assignment of truth values to atomic sentences in propositional logic, or a domain and interpretation function in first-order logic) under which φ evaluates to true. It is **unsatisfiable** — also called a **contradiction** — if no such interpretation exists. These concepts connect directly to consequence: φ ⊨ ψ if and only if φ ∧ ¬ψ is unsatisfiable. Proving logical consequence and proving unsatisfiability are two sides of the same coin, which is why many automated theorem provers work by negating the conclusion and seeking a contradiction — a method called **refutation**.

In propositional logic, satisfiability is decidable by truth tables (check all 2^n assignments for n atomic variables), but this brute-force approach is exponential. The **SAT problem** — given a propositional formula, is it satisfiable? — is **NP-complete**, the landmark result of Cook's theorem (1971). Being NP-complete means SAT is at least as hard as any problem whose solution can be verified in polynomial time, and a polynomial-time algorithm for SAT would yield polynomial-time algorithms for all of NP. Despite this worst-case hardness, modern SAT solvers (based on DPLL and conflict-driven clause learning, CDCL) exploit the structure of practical instances to solve formulas with millions of variables efficiently.

**Unsatisfiability** is central to proof systems. A **refutation-complete** proof system — such as resolution — works by taking the negation of a target claim and deriving a contradiction (the empty clause). If the negation is unsatisfiable, the refutation will eventually be found; if it is satisfiable, no refutation exists. The completeness theorem for first-order logic connects these two sides: a sentence φ is unsatisfiable if and only if ⊥ is provable from φ in a complete proof system. Grasping this duality between semantic satisfiability and syntactic provability is essential for understanding both automated reasoning and the theoretical limits of what logic can decide.
