---
id: compactness-propositional-logic
title: Compactness Theorem for Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-consequence-and-entailment
  type: hard
builds-toward:
- propositional-compactness
tags:
- propositional-logic
- compactness
- finiteness
stage: formal-systems
status: draft
---

# Compactness Theorem for Propositional Logic

## Core Idea
The compactness theorem states that if every finite subset of an infinite set Γ of formulas is satisfiable, then Γ itself is satisfiable. This powerful result shows that propositional logic has a finiteness property—infinite logical problems reduce to checking finite subproblems.

## Explainer

You've studied logical consequence and entailment — when a set of formulas semantically forces a conclusion. The compactness theorem tells you something striking: propositional logic cannot create "truly infinite" constraints. If an infinite set of formulas Γ is **finitely satisfiable** — meaning every finite subset Δ ⊆ Γ has a satisfying assignment — then the entire infinite set Γ is satisfiable. Unsatisfiability can only arise if some finite "culprit" is already unsatisfiable.

This is not obvious. Imagine Γ = {φ₁, φ₂, φ₃, ...} where each finite prefix {φ₁, ..., φₙ} is satisfiable, but the satisfying assignments become more and more constrained as n grows. You might worry that infinite constraints pile up and force a contradiction that no finite subset witnesses. Compactness guarantees this cannot happen in propositional logic — if you can always satisfy finitely many formulas at once, you can satisfy all of them simultaneously. The logic lacks the expressive power to encode constraints that are "essentially infinite."

One elegant proof route goes through the completeness theorem: Γ is unsatisfiable if and only if Γ ⊢ ⊥ (a contradiction is provable). A formal proof is a *finite* syntactic object that draws on only finitely many premises from Γ. So any derivation of ⊥ from Γ uses only some finite subset Δ ⊆ Γ — meaning if every finite subset is satisfiable, no contradiction is derivable, so Γ is satisfiable. An alternative direct proof uses König's lemma: build the tree of all partial truth assignments consistent with Γ; by König's lemma (the tree is infinite but finitely branching), it has an infinite branch, which defines a global satisfying assignment.

The applications reveal the theorem's depth. You can encode the statement "every finite subgraph of an infinite graph is k-colorable" as a propositional theory and conclude the whole graph is k-colorable. You can build **non-standard models of arithmetic**: take the standard natural numbers, add a constant c, and add axioms c > 0, c > 1, c > 2, ... — every finite subset is satisfiable (in ℕ), so by compactness the whole set is satisfiable, giving a model containing an infinite "number" greater than every standard natural number. This application generalizes to first-order logic, where compactness is one of the most powerful tools for constructing exotic models. Compactness is the fundamental finiteness theorem of classical logic: all logical phenomena are witnessed by finite certificates.
