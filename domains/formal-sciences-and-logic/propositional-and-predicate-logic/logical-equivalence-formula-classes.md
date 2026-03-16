---
id: logical-equivalence-formula-classes
title: Logical Equivalence and Classes of Equivalent Formulas
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-equivalence
  type: hard
- id: propositional-semantics
  type: soft
builds-toward:
- normal-forms-cnf-dnf
- prenex-normal-form
tags:
- equivalence
- formulas
- transformations
stage: formal-systems
status: draft
---

# Logical Equivalence and Classes of Equivalent Formulas

## Core Idea
Two formulas φ and ψ are logically equivalent (φ ≡ ψ) if they have the same truth value in every interpretation and variable assignment. Logical equivalence partitions formulas into classes; each class represents a distinct semantic contribution. Key equivalences include De Morgan's laws, commutativity, associativity, and distributivity. Recognizing equivalent formulas enables proof simplification and transformation to normal forms. Equivalence is stronger than consistency (two consistent formulas may not be equivalent) but weaker than a tautology (a tautology is equivalent to any true formula).

## How It's Best Learned
Verify equivalences using truth tables or semantic reasoning. Build intuition for common equivalences. Apply equivalences to transform formulas and simplify proofs. Distinguish between logical equivalence (≡) and material equivalence (↔ as a connective).

## Common Misconceptions
- Confusing ≡ (semantic equivalence) with ↔ (the biconditional connective); though they're related, ≡ is a metatheoretic relation.
- Assuming logical equivalence is symmetric (it is) or transitive (it is); these properties are intuitive once clarified.
- Thinking two formulas are equivalent because one implies the other (equivalence requires implication in both directions).

## Explainer

You know that two formulas φ and ψ are **logically equivalent** (φ ≡ ψ) when they have identical truth values under every interpretation — their truth tables are identical column-for-column. Logical equivalence is an *equivalence relation*: reflexive (φ ≡ φ), symmetric (if φ ≡ ψ then ψ ≡ φ), and transitive (if φ ≡ ψ and ψ ≡ χ then φ ≡ χ). An equivalence relation partitions its domain into **equivalence classes** — here, classes of formulas that express exactly the same semantic content, differing only in syntax.

This partition is not just abstract tidiness — it underlies every formula transformation in logic. When you apply De Morgan's law to replace ¬(φ ∧ ψ) with (¬φ ∨ ¬ψ), you are moving within the same equivalence class. The semantic class doesn't change; only the syntactic representative does. The key equivalences to internalize are: De Morgan's laws, double negation (¬¬φ ≡ φ), commutativity of ∧ and ∨, associativity, distributivity of ∧ over ∨ and vice versa, and the definitions of → and ↔ in terms of ∧, ∨, ¬. Each is an equality of equivalence classes, licensed by checking that both sides have the same truth table.

The main application is transformation to **normal forms**. Every formula is equivalent to one in **conjunctive normal form (CNF)** — a conjunction of clauses, each clause being a disjunction of literals — and one in **disjunctive normal form (DNF)** — a disjunction of conjunctions of literals. The conversion algorithm is a sequence of equivalence-preserving steps: eliminate ↔ and →, push ¬ inward using De Morgan, then distribute. Each step keeps you in the same equivalence class while driving the formula toward a canonical representative. CNF is the input format for SAT solvers; DNF is useful for certain reasoning tasks. The normal form exists and is reachable because equivalences let you traverse the class freely.

A crucial distinction to hold precisely: **logical equivalence** (φ ≡ ψ) is a *metatheoretic* relation between two formulas, not a formula itself. The **biconditional** (φ ↔ ψ) is an *object-level connective* — a formula built from φ and ψ using ↔. They are related by the bridge theorem: φ ≡ ψ holds if and only if φ ↔ ψ is a **tautology** (true in every interpretation). This means you can check logical equivalence either semantically (same truth table) or via a tautology check (the biconditional is universally true). Confusing the two levels — writing φ ≡ ψ inside a formula, or treating ↔ as synonymous with class equality — produces subtle errors in proof construction and formula manipulation.
