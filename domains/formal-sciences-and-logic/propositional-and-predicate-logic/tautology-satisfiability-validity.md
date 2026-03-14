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
