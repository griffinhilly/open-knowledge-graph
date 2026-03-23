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
status: validated
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

## Questions

```yaml
- question: "A formal proof system derives φ from premises Γ (written Γ ⊢ φ). What does soundness guarantee about this derivation?"
  type: multiple-choice
  options:
    - "That φ is a tautology — true in all models regardless of what Γ says"
    - "That Γ ⊨ φ — every model satisfying all formulas in Γ also satisfies φ"
    - "That Γ ⊢ φ can also be derived in every other proof system"
    - "That Γ is itself consistent and contains no contradictions"
  answer: 1
  explanation: "Soundness says: if there is a formal derivation Γ ⊢ φ, then Γ ⊨ φ (semantic consequence). The proof system never derives a false conclusion from true premises. Option A is wrong — soundness does not require φ to be a tautology; it only guarantees φ is true in every model of Γ. A tautology is true in all models unconditionally; a semantic consequence is true in all models that happen to satisfy Γ. Soundness is the 'safety' direction: ⊢ implies ⊨."

- question: "Gödel's incompleteness theorems show that certain true statements about natural numbers cannot be proved within Peano arithmetic. What does this imply about the soundness of first-order logic?"
  type: multiple-choice
  options:
    - "First-order logic is unsound for sufficiently complex theories — it eventually derives false statements"
    - "First-order logic is incomplete — there are valid formulas in the language that no proof system can derive"
    - "Nothing about soundness — incompleteness is about specific theories lacking the power to prove all their truths; first-order logic itself remains sound and (by Gödel's completeness theorem) complete"
    - "The proof system for Peano arithmetic must be unsound, since it fails to prove things that are true"
  answer: 2
  explanation: "Gödel's incompleteness theorems apply to specific sufficiently strong *theories* (like Peano arithmetic with its fixed axioms), not to first-order logic as a proof system. First-order logic's proof calculus is sound (Γ ⊢ φ implies Γ ⊨ φ) and complete (Γ ⊨ φ implies Γ ⊢ φ) — this is Gödel's *completeness* theorem. The *incompleteness* theorems say that Peano arithmetic as a theory cannot prove all truths about natural numbers within that theory's fixed axioms. The logic itself is fine; the particular theory doesn't have enough axioms to prove everything true in its intended model."

- question: "Soundness is the forward direction of correctness: if a formula is provable (⊢ φ), then it is valid (⊨ φ)."
  type: true-false
  answer: true
  explanation: "Soundness is precisely this forward implication: ⊢ implies ⊨. Provability entails validity. The reverse direction — ⊨ implies ⊢ — is completeness. Soundness is the 'safety' or 'correctness' direction: the proof system only certifies things that are actually true. Completeness is the 'power' direction: the proof system can prove everything that is true. Together they give the equivalence ⊢ iff ⊨. Soundness is easier to establish (holds for any well-designed system); completeness is the deeper result."

- question: "Gödel's incompleteness theorems demonstrate that first-order logic is unsound when applied to sufficiently complex mathematical theories like Peano arithmetic."
  type: true-false
  answer: false
  explanation: "This confuses soundness with completeness, and confuses the logic with the theory. First-order logic as a proof system is sound and complete (Gödel's completeness theorem, 1929). The incompleteness theorems (1931) show that Peano arithmetic — a specific theory formulated in first-order logic — cannot prove all truths expressible in its language. This is a limitation of the theory's axioms, not a failure of soundness. A sound proof system can still be based on insufficient axioms; it will simply fail to prove some true things (incompleteness), but it will never prove false things (soundness is preserved)."

- question: "Explain why soundness of a proof system is not trivially obvious, and give an example of how a proof system could fail to be sound."
  type: short-answer
  answer: "Soundness requires careful verification that every axiom is valid and every inference rule preserves truth — it is not guaranteed by intent. A proof system fails to be sound if any axiom is not logically valid, or if any inference rule allows a false conclusion to follow from true premises. For example, adding the axiom schema φ ∧ ¬φ (a contradiction) makes the system unsound: from a contradiction, any formula is derivable (ex falso quodlibet), including false ones. Historically, Frege's Basic Law V in naive set theory was intended as an axiom but turned out to be inconsistent (Russell's paradox), making any system built on it trivially unsound."
  explanation: "The proof of soundness proceeds by structural induction on derivations: verify all axioms are valid (base case), then show each inference rule preserves semantic truth (inductive step). This is nontrivial work, not an assumption. The history of logic is full of systems that seemed correct but contained subtle flaws — soundness proofs exist precisely to rule these out rigorously."
```

## Explainer

You have already studied soundness and completeness for both propositional and first-order logic, and you understand **logical consequence**: Γ ⊨ φ means every model satisfying all formulas in Γ also satisfies φ. The **soundness theorem** bridges the syntactic and semantic worlds: it says that if there is a formal derivation of φ from Γ (written Γ ⊢ φ), then φ is a semantic consequence of Γ (Γ ⊨ φ). In plain terms: the proof system never derives a false conclusion. Soundness is the *correctness* guarantee — it certifies that provability implies truth.

The proof of soundness proceeds by **induction on the structure of proofs**. Every formal derivation is a finite tree of inference steps. The base case handles **axioms**: you verify that every axiom schema is logically valid — true in all models under all interpretations. For example, the axiom schema A → (B → A) is a tautology: if A is true, then regardless of B, "B → A" is true. The inductive step handles **inference rules**: you show that each rule *preserves* semantic truth. For modus ponens — from Γ ⊢ φ and Γ ⊢ (φ → ψ), conclude Γ ⊢ ψ — the soundness argument is: in every model of Γ, both φ and φ → ψ are true (induction hypothesis), so ψ must be true in that model (by the semantics of →). Repeating this for every inference rule in the system completes the induction. Soundness follows by structural induction over every possible derivation.

It is tempting to think soundness is obvious or trivial — "of course our proof system is correct, we designed it well." But soundness is not automatic. A proof system that includes the axiom φ ∧ ¬φ would be unsound: it derives a contradiction, and from a contradiction any formula is derivable, including false ones. More subtly, certain strong comprehension axioms proposed in the early history of set theory (Frege's Basic Law V) turned out to be inconsistent, making any proof system built on them trivially unsound. Proving soundness is the discipline of carefully verifying that *no* inference rule allows a false conclusion to follow from true premises.

**Soundness is the forward direction; completeness is the backward direction.** Soundness says: ⊢ implies ⊨ (every theorem is valid). Completeness says: ⊨ implies ⊢ (every valid formula is provable). Together they give the equivalence ⊢ iff ⊨ — syntactic derivability coincides exactly with semantic consequence. Note the asymmetry: soundness is the "safety" direction and holds for any well-designed system. Completeness is the "power" direction and requires a deeper theorem — Gödel's completeness theorem for first-order logic. Gödel's *incompleteness* theorems, by contrast, show that for specific sufficiently strong *theories* (like Peano arithmetic), there are true sentences that the theory cannot prove. This is not a failure of soundness; it is a limitation of completeness relative to a fixed set of axioms. The logic itself remains sound and complete; the particular theory does not prove everything true in its intended model.
