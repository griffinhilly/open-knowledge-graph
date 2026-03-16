---
id: literals-and-clauses-cnf
title: Literals and Clauses in Conjunctive Normal Form
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: atomic-versus-complex-formulas
  type: hard
- id: normal-forms-cnf-dnf
  type: hard
builds-toward:
- resolution-propositional
- resolution-fol
tags:
- cnf
- literals
- clauses
- normal-forms
- resolution
stage: formal-systems
status: draft
---

# Literals and Clauses in Conjunctive Normal Form

## Core Idea
A literal is an atomic formula or its negation (e.g., P or ¬P). A clause is a disjunction of literals (e.g., P ∨ ¬Q ∨ R). Conjunctive normal form (CNF) is a formula that is a conjunction of clauses. CNF is important for automated reasoning: the resolution rule operates on clauses, and converting any formula to CNF enables the application of resolution. Every propositional formula can be converted to an equivalent CNF (possibly with an exponential blowup), and CNF is the standard input for SAT solvers.

## How It's Best Learned
Start with propositional formulas and convert them to CNF step-by-step using distributive laws. Understand clauses as OR-of-ANDs. Practice recognizing when a formula is already in CNF. Extend to first-order logic by treating ground atoms as propositional variables.

## Common Misconceptions
- Thinking CNF is unique (multiple CNF forms exist for the same formula).
- Confusing CNF with DNF (CNF is AND of ORs; DNF is OR of ANDs).
- Assuming CNF conversion is efficient in practice (it can lead to exponential growth; better methods use SAT solver techniques).

## Explainer

You already know from atomic versus complex formulas that propositional formulas are built from atomic propositions using connectives, and from normal forms that every formula can be rewritten in a canonical shape. CNF sharpens this: it imposes the tightest regular structure used in automated reasoning. A **literal** is the simplest unit: either an atomic proposition P (a **positive literal**) or its negation ¬P (a **negative literal**). A literal asserts something definite about one variable. A **clause** is a disjunction of literals: P ∨ ¬Q ∨ R says "at least one of these three things holds." A formula is in **conjunctive normal form** if it is a conjunction (AND) of clauses — a formula that looks like (clause₁) ∧ (clause₂) ∧ ... ∧ (clauseₙ).

The mnemonic to nail the distinction from DNF: **CNF is AND of ORs; DNF is OR of ANDs**. In CNF, each clause is an OR that must be satisfied, and *all* clauses must be satisfied simultaneously. Think of it as a list of constraints: every clause is one requirement the assignment must meet. A satisfying assignment must make at least one literal true in *every* clause. An empty clause (disjunction of zero literals) is unsatisfiable by convention — it represents a contradiction. A formula with no clauses is trivially satisfiable.

Converting any propositional formula to CNF uses the distributive laws you know from Boolean algebra. The procedure is: (1) eliminate biconditionals and implications by rewriting them in terms of ∧, ∨, ¬; (2) push negations inward using De Morgan's laws until they appear only on atoms; (3) distribute ∨ over ∧ using the law A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C). Step 3 is where blowup happens: distributing ∨ over ∧ can double the number of clauses at each step, giving exponential blowup in the worst case. Modern SAT solvers avoid this by using **Tseitin's transformation**: introduce a fresh auxiliary variable for each subformula, add clauses relating it to its immediate components, and produce a CNF that is *equisatisfiable* (same satisfiability status) rather than logically equivalent. Tseitin's approach is linear in the size of the original formula.

CNF is the universal input language for SAT solvers and the foundation of the **resolution** proof system you will study next. The resolution rule takes two clauses that share a complementary literal pair — say (A ∨ P) and (B ∨ ¬P) — and derives the **resolvent** (A ∨ B). This rule operates only on clauses, which is why CNF is required. Resolution is both a refutation procedure (derive the empty clause to show unsatisfiability) and the engine behind DPLL and CDCL algorithms that power modern SAT solving. Mastering literals and clauses is therefore not merely a syntactic exercise but the prerequisite to understanding how automated reasoning actually works at scale.
