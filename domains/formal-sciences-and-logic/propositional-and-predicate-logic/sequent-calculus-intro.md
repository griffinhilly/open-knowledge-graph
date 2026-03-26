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
status: validated
---

# Sequent Calculus

## Core Idea
Sequent calculus, introduced by Gentzen as the LK system, formalizes proofs as derivations of sequents of the form Γ ⊢ Δ, where Γ is a set of assumptions and Δ is a set of possible conclusions. Rules operate on both sides of the turnstile simultaneously, making structural properties of proofs (weakening, contraction, exchange) explicit. The most profound result about sequent calculus is the cut-elimination theorem (Gentzen's Hauptsatz): every proof using the cut rule can be transformed into a cut-free proof. Cut-elimination has deep implications for proof search and consistency.

## How It's Best Learned
Compare the same theorem proved in natural deduction and in LK side by side. Practice applying left and right introduction rules, and trace a simple cut-elimination step manually.

## Common Misconceptions
- The cut rule is not unsound — it is eliminable but useful as a 'lemma' mechanism.
- Sequent calculus and natural deduction are equally expressive; the difference is in how proofs are structured and what meta-theorems become visible.

## Questions

```yaml
- question: "The cut rule in LK allows deriving Γ,Γ' ⊢ Δ,Δ' by first proving Γ ⊢ Δ,A and then using A as an assumption in A,Γ' ⊢ Δ'. Cut-elimination (the Hauptsatz) proves that this rule can always be eliminated. What is the key consequence?"
  type: multiple-choice
  options:
    - "Cut-free proofs are shorter and therefore more efficient to verify"
    - "Cut-free proofs have the subformula property — every formula in the proof is a subformula of the conclusion — giving a syntactic consistency proof and making proof search deterministic"
    - "Eliminating cut shows that LK can derive more theorems than it could with cut"
    - "Cut-elimination proves that sequent calculus is more expressive than natural deduction"
  answer: 1
  explanation: "Cut-free proofs have the subformula property: no formula appears in the proof that isn't already present in the conclusion. This has two major consequences: (1) a syntactic consistency proof — ⊢ ∅ (provable contradiction) has no cut-free proof, so the system is consistent; and (2) proof search becomes analytic and terminating, since you only need to work with subformulas of the goal. Cut-free proofs are typically longer, not shorter. And cut-elimination shows the cut rule is redundant, not that it adds new theorems — LK with and without cut prove the same things."

- question: "How does LK's treatment of logical connectives differ from natural deduction's treatment of the same connectives?"
  type: multiple-choice
  options:
    - "LK has no elimination rules; it uses only introduction rules, unlike natural deduction which has both"
    - "Natural deduction uses sequents while LK uses individual judgment forms"
    - "LK provides both a left rule (for using a connective as an assumption) and a right rule (for proving a connective as a conclusion), making the system two-sided in a way natural deduction is not"
    - "LK can only handle classical logic; natural deduction handles both classical and intuitionistic logic"
  answer: 2
  explanation: "In natural deduction, rules are either introduction rules (proving a connective) or elimination rules (using a connective). In LK, for each connective there is a right rule (decomposing it on the right of ⊢, i.e., in the conclusion) and a left rule (decomposing it on the left of ⊢, i.e., as an assumption). This two-sided structure makes the symmetry between hypothesis-use and conclusion-proof explicit. Natural deduction does have both introduction and elimination rules, but they are not organized symmetrically around a turnstile — that reorganization is what gives LK its structural clarity."

- question: "The cut rule in LK is unsound — it can produce invalid derivations, which is why Gentzen proved it should be eliminated from any valid proof."
  type: true-false
  answer: false
  explanation: "This is the central misconception about cut-elimination. The cut rule is perfectly sound — any derivation using cut derives only valid sequents. Cut-elimination shows that cut is *eliminable* (redundant) — every proof using cut can be transformed into a cut-free proof of the same sequent. The reason to care about cut-free proofs is not soundness but the subformula property they carry, which enables consistency proofs and analytic proof search. Soundness is never in question."

- question: "A cut-free proof in LK contains only formulas that are subformulas of the sequent being proved."
  type: true-false
  answer: true
  explanation: "This is the subformula property, and it is the key structural fact about cut-free proofs. It means that to prove Γ ⊢ Δ without cut, you never need to invent a formula from outside — you only decompose the formulas already present. This makes proof search analytic: you work top-down from the goal, breaking formulas into subformulas, and the process terminates because formulas can only get smaller. With cut, you can introduce an arbitrary intermediate formula A, which is what makes cut proofs shorter but proof search harder."

- question: "What does cut-elimination imply about the consistency of LK, and why is this a syntactic rather than semantic argument?"
  type: short-answer
  answer: "Cut-elimination implies consistency because the empty sequent ⊢ ∅ — which would represent a derivable contradiction — cannot have a cut-free proof. No right-side rule produces an empty succedent from valid inputs, and the subformula property ensures no formula can be conjured from nothing. Therefore the system cannot prove a contradiction, and is consistent. This is syntactic because the argument works entirely within the proof system itself — it does not appeal to a model or an interpretation of the formulas. Consistency is derived from the structure of the rules, not from semantic truth."
  explanation: "Semantic consistency proofs show 'no model satisfies a contradiction, and LK is sound, so it cannot derive one.' Syntactic consistency proofs (like Gentzen's) show 'no proof exists' by analyzing the shapes of derivations directly. Syntactic proofs are valued because they don't presuppose a semantic framework — they work even in settings where the semantics is unclear or disputed, which is important for foundational work in proof theory."
```

## Explainer

You know natural deduction from prior study: proofs build up from hypotheses using introduction and elimination rules, and the structure of a proof mirrors the structure of the formula being proved. Sequent calculus, Gentzen's **LK system**, reorganizes the same logical content into a different shape that makes the global structure of proofs — rather than the local derivation steps — the primary object of study. The central notion is the **sequent**: an expression Γ ⊢ Δ, where Γ (the antecedent) is a set of formulas assumed as hypotheses, and Δ (the succedent) is a set of formulas, at least one of which must be derivable from those hypotheses. Intuitively, Γ ⊢ Δ means "from these assumptions, one of these conclusions follows." When Δ has exactly one formula, this looks exactly like the natural deduction judgment Γ ⊢ φ. Allowing multiple conclusions on the right is what makes the system symmetric and gives it structural elegance.

LK has two kinds of rules: **structural rules** (weakening, contraction, exchange, and cut) that manipulate the shape of the sequent without introducing new connectives, and **logical rules** that decompose formulas on the left or right of the turnstile. For each connective there is a left rule (for using that connective as an assumption) and a right rule (for proving that connective as a conclusion). For example, the right-∧ rule says: to prove A ∧ B on the right, prove A and B separately, keeping the same antecedent. The left-∧ rule says: if you have A ∧ B as an assumption, you can replace it with A (or B) in the antecedent. This left/right decomposition is absent from natural deduction and is what gives sequent calculus its characteristic two-sided structure.

The **cut rule** is the sequent calculus analogue of using a lemma: from Γ ⊢ Δ, A and A, Γ' ⊢ Δ', derive Γ, Γ' ⊢ Δ, Δ'. It lets you prove an intermediate formula A and then use it in a further proof, exactly as a mathematician states a lemma. The cut rule is obviously *sound* — the derivation it summarizes is valid — but Gentzen's profound result, the **Hauptsatz** (cut-elimination theorem), is that it is also *eliminable*: any proof using cut can be systematically transformed into a cut-free proof. Cut-free proofs are longer, but they have the **subformula property**: every formula appearing in a cut-free proof is a subformula of the conclusion. This means cut-free proofs are analytic — you never need to invent formulas not already present in the goal.

Cut-elimination has immediate consequences. First, it gives a syntactic proof of **consistency**: the empty sequent ⊢ ∅ (asserting that a contradiction is provable from nothing) cannot have a cut-free proof, because no logical rule produces it. Therefore the system is consistent without appealing to semantics. Second, it gives a decision procedure for the validity of propositional sequents: proof search in cut-free LK is deterministic and terminating. Third, it implies the **interpolation theorem** and other deep metatheorems about the logic. Sequent calculus thus shifts the focus from "what can be proved?" to "what do proofs look like?" — a move that opened the door to structural proof theory and later to the Curry-Howard correspondence between proofs and programs.
