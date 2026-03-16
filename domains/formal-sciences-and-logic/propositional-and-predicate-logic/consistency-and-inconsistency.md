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

## Explainer

You already know that a formula is **satisfiable** if some interpretation makes it true, and **unsatisfiable** (a contradiction) if none does. **Consistency** extends this idea from single formulas to sets: a set Σ of formulas is consistent if there is at least one interpretation that satisfies every formula in Σ simultaneously. It is **inconsistent** if no such interpretation exists — the formulas collectively impose contradictory demands on the world.

The simplest inconsistency arises from a direct contradiction: the set {P, ¬P} is inconsistent because any interpretation that makes P true makes ¬P false, and vice versa. But inconsistency can be more subtle. Consider {P → Q, P, ¬Q}: any interpretation making P true and Q false satisfies ¬Q but falsifies P → Q; any interpretation making Q true satisfies P → Q but falsifies ¬Q; you cannot satisfy all three at once. The set is inconsistent even though no single formula in it is a contradiction.

Why does inconsistency matter so much? Because of **ex falso quodlibet** — the principle of explosion: from a contradiction, you can derive any formula whatsoever. If an axiomatic system contains an inconsistency, every formula is provable in it, including both a statement and its negation. The system says everything and therefore says nothing useful. This is why consistency is the *minimum* requirement for any formal theory to be meaningful. When mathematicians worried in the early 20th century about the foundations of mathematics — leading to Gödel's incompleteness theorems, Hilbert's program, and Russell's type theory — the central concern was whether their axiom systems were consistent.

Consistency and satisfiability are deeply linked: by the **completeness theorem** (which you will encounter later), a set of first-order sentences is consistent — meaning no contradiction is derivable — if and only if it is satisfiable — meaning some interpretation makes all of them true. This equivalence is non-trivial and connects the syntactic notion of derivability with the semantic notion of truth. For propositional logic, you can check consistency by truth tables: build the combined truth table for all formulas in Σ and see whether any row makes every formula true. For infinite sets, you need deeper tools — but the concept is the same: does a coherent picture of the world exist in which all the claims hold?
