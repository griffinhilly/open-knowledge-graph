---
id: propositional-compactness
title: Compactness Theorem for Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-soundness-completeness
  type: hard
- id: normal-forms-cnf-dnf
  type: soft
builds-toward:
- fol-compactness
- model-theory-basics
tags:
- compactness
- infinite-sets
- satisfiability
- finiteness
stage: formal-systems
status: validated
---

# Compactness Theorem for Propositional Logic

## Core Idea
The compactness theorem states that an infinite set of propositional formulas is satisfiable if and only if every finite subset of it is satisfiable. This connects local (finite) reasoning to global (infinite) conclusions and is one of the most powerful tools in mathematical logic. It follows naturally from completeness: any proof uses only finitely many formulas. Compactness has striking applications — for instance, it can be used to show that if a graph-coloring problem has no finite obstruction, it has a valid coloring — and it is the key lemma behind many model-theoretic constructions.

## How It's Best Learned
Prove compactness from completeness (proofs are finite objects). Then work through at least one non-trivial application, such as constructing non-standard models or proving König's infinity lemma.

## Common Misconceptions
- Compactness does not mean finite sets are all that matter; infinite sets are fully meaningful, but finitely testable.
- The theorem's converse direction (finite satisfiability implies global satisfiability) is the non-trivial and surprising direction.
