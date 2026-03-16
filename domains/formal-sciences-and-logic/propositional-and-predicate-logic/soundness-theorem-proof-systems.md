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

## Explainer

You have already studied soundness and completeness for both propositional and first-order logic, and you understand **logical consequence**: Γ ⊨ φ means every model satisfying all formulas in Γ also satisfies φ. The **soundness theorem** bridges the syntactic and semantic worlds: it says that if there is a formal derivation of φ from Γ (written Γ ⊢ φ), then φ is a semantic consequence of Γ (Γ ⊨ φ). In plain terms: the proof system never derives a false conclusion. Soundness is the *correctness* guarantee — it certifies that provability implies truth.

The proof of soundness proceeds by **induction on the structure of proofs**. Every formal derivation is a finite tree of inference steps. The base case handles **axioms**: you verify that every axiom schema is logically valid — true in all models under all interpretations. For example, the axiom schema A → (B → A) is a tautology: if A is true, then regardless of B, "B → A" is true. The inductive step handles **inference rules**: you show that each rule *preserves* semantic truth. For modus ponens — from Γ ⊢ φ and Γ ⊢ (φ → ψ), conclude Γ ⊢ ψ — the soundness argument is: in every model of Γ, both φ and φ → ψ are true (induction hypothesis), so ψ must be true in that model (by the semantics of →). Repeating this for every inference rule in the system completes the induction. Soundness follows by structural induction over every possible derivation.

It is tempting to think soundness is obvious or trivial — "of course our proof system is correct, we designed it well." But soundness is not automatic. A proof system that includes the axiom φ ∧ ¬φ would be unsound: it derives a contradiction, and from a contradiction any formula is derivable, including false ones. More subtly, certain strong comprehension axioms proposed in the early history of set theory (Frege's Basic Law V) turned out to be inconsistent, making any proof system built on them trivially unsound. Proving soundness is the discipline of carefully verifying that *no* inference rule allows a false conclusion to follow from true premises.

**Soundness is the forward direction; completeness is the backward direction.** Soundness says: ⊢ implies ⊨ (every theorem is valid). Completeness says: ⊨ implies ⊢ (every valid formula is provable). Together they give the equivalence ⊢ iff ⊨ — syntactic derivability coincides exactly with semantic consequence. Note the asymmetry: soundness is the "safety" direction and holds for any well-designed system. Completeness is the "power" direction and requires a deeper theorem — Gödel's completeness theorem for first-order logic. Gödel's *incompleteness* theorems, by contrast, show that for specific sufficiently strong *theories* (like Peano arithmetic), there are true sentences that the theory cannot prove. This is not a failure of soundness; it is a limitation of completeness relative to a fixed set of axioms. The logic itself remains sound and complete; the particular theory does not prove everything true in its intended model.
