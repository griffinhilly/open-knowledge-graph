---
id: soundness-theorem-proof-systems
title: Soundness Theorem and Validity of Proof Systems
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-soundness-completeness
  type: hard
- id: fol-soundness-completeness
  type: hard
- id: logical-consequence-and-entailment
  type: hard
builds-toward:
- godel-completeness-theorem-first-order
- syntactic-versus-semantic-consequence
tags:
- proof-theory
- soundness
- validity
- proof-systems
stage: formal-systems
status: draft
---

# Soundness Theorem and Validity of Proof Systems

## Core Idea
A proof system is sound if every formula it can derive is logically valid (true in all models). Formally, soundness says: if Γ ⊢ φ, then Γ ⊨ φ. Soundness is a correctness property: it ensures that a proof system never derives a false conclusion. Natural deduction, sequent calculus, and resolution are all sound. Proving soundness typically involves induction on the structure of proofs, verifying that each inference rule preserves truth. Soundness is necessary but not sufficient for a complete proof system; completeness asks whether all valid formulas are provable.

## How It's Best Learned
Understand soundness as the forward direction of correctness: the system doesn't prove false things. Sketch soundness proofs for simple proof systems (e.g., natural deduction for propositional logic). Contrast with completeness (backward direction). Relate soundness to real-world verification: a sound theorem prover will never certify an invalid formula.

## Common Misconceptions
- Confusing soundness with completeness (sound means all provable formulas are valid; complete means all valid formulas are provable).
- Thinking soundness is trivial (proving soundness requires care and induction).
- Assuming soundness implies correctness (soundness only ensures validity of proofs, not that all valid formulas are provable).
