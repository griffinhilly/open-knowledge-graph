---
id: tautologies-and-contradictions
title: Tautologies, Contradictions, and Satisfiability
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
- id: logical-equivalences
  type: soft
- id: truth-tables
  type: soft
builds-toward:
- normal-forms-cnf-dnf
- propositional-soundness-completeness
tags:
- tautology
- contradiction
- satisfiability
- validity
stage: formal-systems
status: validated
---

# Tautologies, Contradictions, and Satisfiability

## Core Idea
A tautology is a formula true under every possible valuation (e.g., p ∨ ¬p); a contradiction is false under every valuation (e.g., p ∧ ¬p); a contingency is neither. A formula is satisfiable if at least one valuation makes it true. These classifications partition the space of propositional formulas and are central to logic — proof systems aim to derive exactly the tautologies. The semantic notion of validity (⊨ φ) is the target that syntactic proof systems strive to match.

## How It's Best Learned
Classify a variety of formulas before and after applying De Morgan's laws. Practice converting the question 'is φ a tautology?' to 'is ¬φ a contradiction?' and verify the equivalence.

## Common Misconceptions
- A tautology is not just 'always probably true' — it must hold for literally every truth assignment.
- Satisfiable does not mean true; it means true in at least one scenario.

## Explainer

You know from propositional semantics that a formula's truth value depends on a **truth assignment** — a function mapping each propositional variable to true or false. A formula with n distinct variables has 2ⁿ possible truth assignments. The central classifications of propositional logic ask: what does a formula's truth value look like *across all* those assignments?

A **tautology** (also called a validity) is true under every possible truth assignment — not some, not most, but all of them. The classic example is p ∨ ¬p ("law of excluded middle"): no matter what truth value p takes, one of p and ¬p is true, so the disjunction is always true. A **contradiction** (also called an unsatisfiable formula) is false under every assignment. The example p ∧ ¬p assigns p a value, then requires it to be both true and false simultaneously — impossible. A **contingency** falls in between: true under some assignments, false under others. The formula p → q is contingent: it fails only when p is true and q is false.

The third classification, **satisfiability**, cuts differently: a formula is satisfiable if at least one truth assignment makes it true. Every tautology is satisfiable (all assignments work); every contradiction is unsatisfiable (no assignment works); contingencies are satisfiable but not tautologies. Satisfiability is the focus of SAT solvers and computational complexity — it is the question "can this formula ever be true?" rather than "is this formula always true?"

The most useful transformation here is one you can derive from the logical equivalences you know: φ is a tautology if and only if ¬φ is a contradiction if and only if ¬φ is unsatisfiable. This equivalence is practically powerful because it lets you convert a tautology-checking question into a satisfiability-checking question (and vice versa), which matters for proof systems and automated reasoning. In a proof system, the goal is to derive exactly the tautologies — the formulas whose negations are unsatisfiable, i.e., the ones no consistent assignment can falsify. The semantic target of proof theory is tautology; satisfiability is the complementary concept used to detect when a formula can coherently be false.
