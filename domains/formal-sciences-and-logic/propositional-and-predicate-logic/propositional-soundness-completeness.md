---
id: propositional-soundness-completeness
title: Soundness and Completeness of Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
- id: natural-deduction-propositional
  type: hard
- id: tautologies-and-contradictions
  type: hard
- id: sequent-calculus-intro
  type: soft
- id: mathematical-proof-strategies
  type: soft
builds-toward:
- propositional-compactness
- fol-soundness-completeness
tags:
- soundness
- completeness
- proof-theory
- model-theory
- metatheorem
stage: formal-systems
status: validated
---
# Soundness and Completeness of Propositional Logic

## Core Idea
Soundness means that every formula provable in the proof system is semantically valid: if ⊢ φ then ⊨ φ. Completeness is the converse: every valid formula is provable: if ⊨ φ then ⊢ φ. Together they establish that syntax and semantics perfectly align — proof and truth coincide for propositional logic. Soundness is proved by verifying each inference rule preserves validity. Completeness is proved by showing that any consistent set of formulas has a model (the Lindenbaum–Henkin construction is one approach). These two results certify that the proof system is neither too weak nor too strong.

## How It's Best Learned
Prove soundness first by structural induction on derivations. Then study the completeness proof as an example of the Lindenbaum lemma. See how each direction fails if rules are added or removed.

## Common Misconceptions
- Completeness does not mean 'every truth is provable in general' — it means every logically valid formula is provable.
- A system can be sound but incomplete (missing rules), or complete but unsound (too many rules admitting false conclusions).
