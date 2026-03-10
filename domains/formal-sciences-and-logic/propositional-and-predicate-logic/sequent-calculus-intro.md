---
id: sequent-calculus-intro
title: Sequent Calculus
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: natural-deduction-propositional
  type: hard
- id: normal-forms-cnf-dnf
  type: soft
builds-toward:
- propositional-soundness-completeness
tags:
- sequent-calculus
- Gentzen
- LK
- cut-elimination
- proof-theory
stage: formal-systems
status: draft
---

# Sequent Calculus

## Core Idea
Sequent calculus, introduced by Gentzen as the LK system, formalizes proofs as derivations of sequents of the form Γ ⊢ Δ, where Γ is a set of assumptions and Δ is a set of possible conclusions. Rules operate on both sides of the turnstile simultaneously, making structural properties of proofs (weakening, contraction, exchange) explicit. The most profound result about sequent calculus is the cut-elimination theorem (Gentzen's Hauptsatz): every proof using the cut rule can be transformed into a cut-free proof. Cut-elimination has deep implications for proof search and consistency.

## How It's Best Learned
Compare the same theorem proved in natural deduction and in LK side by side. Practice applying left and right introduction rules, and trace a simple cut-elimination step manually.

## Common Misconceptions
- The cut rule is not unsound — it is eliminable but useful as a 'lemma' mechanism.
- Sequent calculus and natural deduction are equally expressive; the difference is in how proofs are structured and what meta-theorems become visible.
