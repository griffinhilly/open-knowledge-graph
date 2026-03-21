---
id: consistency-and-inconsistency
title: Consistency and Inconsistency of Theories
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: satisfiability-and-unsatisfiability
  type: hard
- id: tautologies-and-contradictions
  type: soft
tags:
- propositional-logic
- consistency
- logic-systems
stage: formal-systems
status: draft
---

# Consistency and Inconsistency of Theories

## Core Idea
A set of formulas is consistent if there exists an interpretation satisfying all of them simultaneously; it is inconsistent if no such interpretation exists. Consistency is essential for logical systems—an inconsistent set of axioms allows deriving any formula, making the system useless for sound reasoning.

## Questions

```yaml
- question: "A new formal axiomatic theory is shown to be inconsistent. What follows about the theorems provable in that system?"
  type: multiple-choice
  options:
    - "Some theorems are unprovable — the system has gaps"
    - "The system is incomplete but may still be useful for some purposes"
    - "Every formula is provable in the system, including both a statement and its negation"
    - "The system proves no theorems, because the axioms cancel each other out"
  answer: 2
  explanation: "By the principle of explosion (ex falso quodlibet), from any contradiction you can derive any formula whatsoever. An inconsistent system does not prove nothing — it proves everything. Both P and ¬P are theorems. This makes the system useless for distinguishing truth from falsehood. Option A describes incompleteness, which is a different property entirely."

- question: "Is the set {P → Q, ¬Q, P} consistent?"
  type: multiple-choice
  options:
    - "Yes — no individual formula in the set is itself a contradiction"
    - "No — there is no interpretation that satisfies all three formulas simultaneously"
    - "Yes — interpretations where P → Q is false satisfy the remaining formulas"
    - "It depends on whether P and Q are logically independent"
  answer: 1
  explanation: "If P is true and ¬Q is true (Q false), then P → Q is false (a true antecedent with a false consequent). If P is false, P is not satisfied. No row in the combined truth table makes all three formulas true — the set is inconsistent. Option A is the key misconception: inconsistency is a property of the set as a whole, not of any individual member."

- question: "A set of formulas can be inconsistent even if none of the individual formulas in the set is itself a contradiction."
  type: true-false
  answer: true
  explanation: "Inconsistency is a collective property: the formulas together impose contradictory demands on an interpretation, even though each individual formula is satisfiable. {P → Q, P, ¬Q} is inconsistent, yet P → Q is satisfiable (make P false), P is satisfiable (make P true), and ¬Q is satisfiable (make Q false). The incompatibility only emerges when you try to satisfy all three simultaneously."

- question: "An inconsistent theory is useless because it can prove no theorems."
  type: true-false
  answer: false
  explanation: "The opposite is true: an inconsistent theory proves too MANY theorems — in fact, every formula is provable from a contradiction (the principle of explosion). The theory is useless because it proves everything, including contradictions, making it impossible to rely on for sound reasoning. A theory that says everything says nothing meaningful."

- question: "Why is consistency considered the minimum requirement for a formal theory, rather than merely a desirable property?"
  type: short-answer
  answer: "Because of explosion (ex falso quodlibet): from any inconsistency, every formula is derivable — including both a statement and its negation. A theory that proves everything cannot distinguish true claims from false ones. Consistency is therefore not a bonus feature — it is the precondition for the theory to make any meaningful claims at all. An inconsistent axiom system is not a weak theory; it is no theory."
  explanation: "This is why foundational crises in mathematics (Russell's paradox, Hilbert's program) centered on consistency: if the axioms of arithmetic or set theory were inconsistent, all mathematical reasoning built on them would be worthless. Gödel's incompleteness theorems showed that consistency of a sufficiently powerful system cannot be proved within that system itself — but consistency remains the first requirement, even if unprovable internally."
```

## Explainer

You already know that a formula is **satisfiable** if some interpretation makes it true, and **unsatisfiable** (a contradiction) if none does. **Consistency** extends this idea from single formulas to sets: a set Σ of formulas is consistent if there is at least one interpretation that satisfies every formula in Σ simultaneously. It is **inconsistent** if no such interpretation exists — the formulas collectively impose contradictory demands on the world.

The simplest inconsistency arises from a direct contradiction: the set {P, ¬P} is inconsistent because any interpretation that makes P true makes ¬P false, and vice versa. But inconsistency can be more subtle. Consider {P → Q, P, ¬Q}: any interpretation making P true and Q false satisfies ¬Q but falsifies P → Q; any interpretation making Q true satisfies P → Q but falsifies ¬Q; you cannot satisfy all three at once. The set is inconsistent even though no single formula in it is a contradiction.

Why does inconsistency matter so much? Because of **ex falso quodlibet** — the principle of explosion: from a contradiction, you can derive any formula whatsoever. If an axiomatic system contains an inconsistency, every formula is provable in it, including both a statement and its negation. The system says everything and therefore says nothing useful. This is why consistency is the *minimum* requirement for any formal theory to be meaningful. When mathematicians worried in the early 20th century about the foundations of mathematics — leading to Gödel's incompleteness theorems, Hilbert's program, and Russell's type theory — the central concern was whether their axiom systems were consistent.

Consistency and satisfiability are deeply linked: by the **completeness theorem** (which you will encounter later), a set of first-order sentences is consistent — meaning no contradiction is derivable — if and only if it is satisfiable — meaning some interpretation makes all of them true. This equivalence is non-trivial and connects the syntactic notion of derivability with the semantic notion of truth. For propositional logic, you can check consistency by truth tables: build the combined truth table for all formulas in Σ and see whether any row makes every formula true. For infinite sets, you need deeper tools — but the concept is the same: does a coherent picture of the world exist in which all the claims hold?
