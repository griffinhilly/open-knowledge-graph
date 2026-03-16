---
id: tautology-satisfiability-validity
title: Tautology, Satisfiability, and Validity
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
- id: tautologies-and-contradictions
  type: hard
builds-toward:
- propositional-soundness-completeness
- propositional-compactness
tags:
- tautology
- satisfiability
- validity
- contradiction
- decision-procedure
stage: formal-systems
status: draft
---

# Tautology, Satisfiability, and Validity

## Core Idea
A formula is a tautology (valid) if it is true under every interpretation, satisfiable if true under at least one interpretation, and a contradiction (unsatisfiable) if true under none. These three categories partition the logical landscape and are deeply interrelated: a formula is a tautology iff its negation is unsatisfiable, and satisfiable iff its negation is not a tautology. In propositional logic, truth tables provide a mechanical decision procedure for classifying any formula, though the procedure is exponential in the number of variables.

## How It's Best Learned
Classify a batch of formulas using truth tables, then verify the duality: check that negating a tautology always yields a contradiction and vice versa. Explore why satisfiability-checking (SAT) is the central computational problem of propositional logic.

## Common Misconceptions
- "Valid" and "true" are not synonyms — validity means true under all interpretations, while a formula can be true under a specific interpretation without being valid.
- Satisfiability is not the same as truth — a satisfiable formula might be false under the interpretation you happen to care about.
- The exponential blowup of truth tables is inherent: SAT is NP-complete, so no known polynomial-time decision procedure exists.

## Explainer

You already know what **propositional semantics** means: an interpretation assigns truth values to atomic propositions, and the truth of compound formulas is determined compositionally. You also know that some formulas are tautologies — true under every assignment — and some are contradictions — false under every assignment. This topic organizes the logical landscape into three exhaustive and mutually exclusive categories and reveals the algebraic relationships between them.

A **tautology** (also called **valid**) is a formula true under every possible interpretation. The canonical examples are p ∨ ¬p (the law of excluded middle) and p → p. These require no specific information to evaluate — their truth is guaranteed purely by their logical structure. In natural language, "it will either rain or not rain tomorrow" is a tautology; it contains no actual information about tomorrow's weather. **Contradiction** (unsatisfiable) is the opposite: a formula false under every interpretation, like p ∧ ¬p. A **satisfiable** formula is true under at least one interpretation — most ordinary formulas are satisfiable, including p, p → q, and p ∧ q.

The three categories are connected by clean **duality laws** that are worth internalizing as a reflex: φ is a tautology if and only if ¬φ is a contradiction. φ is satisfiable if and only if ¬φ is not a tautology. This means you only need one checking procedure: if you can test tautology, you can test contradiction by negating the formula; if you can test satisfiability, you can test tautology by testing the negation for unsatisfiability. This duality is what lets SAT solvers (satisfiability checkers) double as tautology checkers: "is φ a tautology?" becomes "is ¬φ unsatisfiable?"

The decision procedure in propositional logic is the **truth table**: enumerate all 2ⁿ assignments to n propositional variables and check the formula under each. If every row gives true, the formula is a tautology; if some row gives true, it is satisfiable; if no row gives true, it is a contradiction. The exponential cost is not a quirk of the method but a reflection of hardness: SAT (deciding satisfiability) is NP-complete, and co-SAT (deciding tautology) is co-NP-complete. No polynomial-time procedure for either is known, and finding one would resolve P vs. NP.

These three categories become more subtle in predicate logic. There, **validity** still means true under all interpretations (of function and relation symbols over any domain), but truth tables no longer apply — the set of interpretations is infinite. Checking validity in predicate logic is not decidable in general (Church-Turing theorem), though valid formulas are semi-decidable: if φ is valid, a proof procedure will eventually find a proof. The satisfiability/validity/contradiction trichotomy remains structurally the same, but the difficulty of classification jumps from NP/co-NP to undecidable. Understanding the propositional case first gives you clean intuition for the richer — and harder — predicate case.
