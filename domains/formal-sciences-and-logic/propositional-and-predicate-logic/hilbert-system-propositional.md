---
id: hilbert-system-propositional
title: Hilbert System for Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-soundness-completeness
  type: hard
- id: proof-structure-and-terminology
  type: soft
builds-toward:
- sequent-calculus-intro
tags:
- Hilbert-system
- axiom-schema
- modus-ponens
- deduction-theorem
- axiomatic-proof
stage: formal-systems
status: draft
---

# Hilbert System for Propositional Logic

## Core Idea
A Hilbert system (or Hilbert-style calculus) derives theorems from a small set of axiom schemas using modus ponens as the sole inference rule: from φ and φ → ψ, infer ψ. Typical axiom schemas include φ → (ψ → φ) and (φ → (ψ → χ)) → ((φ → ψ) → (φ → χ)). The deduction theorem — if Γ ∪ {φ} ⊢ ψ then Γ ⊢ φ → ψ — bridges the gap between derivation and implication, making Hilbert proofs tractable despite their apparent rigidity. Hilbert systems are historically important as the first fully formalized proof systems and remain standard in metatheory.

## How It's Best Learned
Prove simple theorems (e.g., φ → φ) from the axiom schemas and modus ponens alone, experiencing the difficulty firsthand. Then prove the deduction theorem and see how it dramatically simplifies subsequent proofs by allowing assumption discharge.

## Common Misconceptions
- Hilbert systems are not impractical — they are unwieldy for finding proofs but powerful for proving metatheorems about proofs.
- Modus ponens is the only rule, but the axiom schemas do the heavy lifting — different choices of axioms yield different but equivalent systems.
- The deduction theorem is not an axiom — it is a metatheorem about the proof system, proved by induction on derivation length.
