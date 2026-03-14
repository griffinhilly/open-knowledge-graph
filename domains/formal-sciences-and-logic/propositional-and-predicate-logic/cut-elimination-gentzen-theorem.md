---
id: cut-elimination-gentzen-theorem
title: Cut Elimination and Gentzen's Hauptsatz
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: sequent-calculus-intro
  type: hard
- id: propositional-soundness-completeness
  type: soft
tags:
- sequent-calculus
- proof-theory
- cut-elimination
- hauptsatz
stage: formal-systems
status: draft
---

# Cut Elimination and Gentzen's Hauptsatz

## Core Idea
The cut rule in sequent calculus allows intermediate lemmas: from Γ ⊢ Δ, φ and φ, Γ' ⊢ Δ', we derive Γ, Γ' ⊢ Δ, Δ'. Gentzen's hauptsatz (main theorem) states that every proof using the cut rule can be transformed into a proof without cut. Cut-elimination has profound consequences: it yields a decision procedure for propositional logic, provides a way to extract witnesses from proofs (proof mining), and offers insight into proof structure. The cut-free sequent calculus is also the basis for many modern proof assistants.

## How It's Best Learned
Understand the cut rule and why it seems necessary (it allows inlining proofs of intermediate formulas). Work through examples of cut elimination on simple sequent proofs. Discuss consequences of cut elimination (subformula property, decidability). Relate to the idea of direct proofs vs. proofs through intermediate lemmas.

## Common Misconceptions
- Thinking cut elimination is only a theoretical result (it has practical applications in proof search and automated reasoning).
- Assuming cut-free proofs are shorter (they can be exponentially longer, but have better structural properties).
- Confusing cut-elimination with weak cut-elimination (different notions with different consequences).
