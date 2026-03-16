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

## Explainer

You know natural deduction from prior study: proofs build up from hypotheses using introduction and elimination rules, and the structure of a proof mirrors the structure of the formula being proved. Sequent calculus, Gentzen's **LK system**, reorganizes the same logical content into a different shape that makes the global structure of proofs — rather than the local derivation steps — the primary object of study. The central notion is the **sequent**: an expression Γ ⊢ Δ, where Γ (the antecedent) is a set of formulas assumed as hypotheses, and Δ (the succedent) is a set of formulas, at least one of which must be derivable from those hypotheses. Intuitively, Γ ⊢ Δ means "from these assumptions, one of these conclusions follows." When Δ has exactly one formula, this looks exactly like the natural deduction judgment Γ ⊢ φ. Allowing multiple conclusions on the right is what makes the system symmetric and gives it structural elegance.

LK has two kinds of rules: **structural rules** (weakening, contraction, exchange, and cut) that manipulate the shape of the sequent without introducing new connectives, and **logical rules** that decompose formulas on the left or right of the turnstile. For each connective there is a left rule (for using that connective as an assumption) and a right rule (for proving that connective as a conclusion). For example, the right-∧ rule says: to prove A ∧ B on the right, prove A and B separately, keeping the same antecedent. The left-∧ rule says: if you have A ∧ B as an assumption, you can replace it with A (or B) in the antecedent. This left/right decomposition is absent from natural deduction and is what gives sequent calculus its characteristic two-sided structure.

The **cut rule** is the sequent calculus analogue of using a lemma: from Γ ⊢ Δ, A and A, Γ' ⊢ Δ', derive Γ, Γ' ⊢ Δ, Δ'. It lets you prove an intermediate formula A and then use it in a further proof, exactly as a mathematician states a lemma. The cut rule is obviously *sound* — the derivation it summarizes is valid — but Gentzen's profound result, the **Hauptsatz** (cut-elimination theorem), is that it is also *eliminable*: any proof using cut can be systematically transformed into a cut-free proof. Cut-free proofs are longer, but they have the **subformula property**: every formula appearing in a cut-free proof is a subformula of the conclusion. This means cut-free proofs are analytic — you never need to invent formulas not already present in the goal.

Cut-elimination has immediate consequences. First, it gives a syntactic proof of **consistency**: the empty sequent ⊢ ∅ (asserting that a contradiction is provable from nothing) cannot have a cut-free proof, because no logical rule produces it. Therefore the system is consistent without appealing to semantics. Second, it gives a decision procedure for the validity of propositional sequents: proof search in cut-free LK is deterministic and terminating. Third, it implies the **interpolation theorem** and other deep metatheorems about the logic. Sequent calculus thus shifts the focus from "what can be proved?" to "what do proofs look like?" — a move that opened the door to structural proof theory and later to the Curry-Howard correspondence between proofs and programs.
