---
id: logical-implication-entailment
title: Logical Implication and Semantic Entailment
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: truth-assignments-and-valuations
  type: hard
builds-toward:
- logical-consequence-and-validity
- natural-deduction-propositional
- resolution-propositional
tags:
- semantics
- entailment
- validity
stage: formal-systems
status: draft
---

# Logical Implication and Semantic Entailment

## Core Idea
A set of formulas Γ semantically entails φ (written Γ ⊨ φ) if every truth assignment making all formulas in Γ true also makes φ true. This formalizes the intuition that φ logically follows from Γ. Valid formulas are entailed by the empty set.

## Explainer

You already know how to evaluate a formula under a truth assignment — you know which rows of a truth table make a formula true and which make it false. **Semantic entailment** (written Γ ⊨ φ, read "Γ entails φ" or "Γ semantically implies φ") extends this: instead of asking whether φ is true under one assignment, you ask whether φ is true under *every* assignment that makes all of Γ true. The set Γ acts as a filter, narrowing the space of assignments you care about, and φ must hold in all of them.

A concrete example: let Γ = {P, P → Q}. Under any assignment making both P true and P → Q true, Q must also be true (since P is true and the conditional is true, Q cannot be false). So {P, P → Q} ⊨ Q. This is **modus ponens** stated as a semantic fact, not as a proof rule — you are checking the truth tables, not deriving anything. Now consider a different case: {P ∨ Q, ¬P} ⊨ Q. Any assignment making P ∨ Q true and ¬P true must have P = F, which forces Q = T for the disjunction to hold. So Q is guaranteed.

Two special cases sharpen the definition. First, when Γ is empty (∅ ⊨ φ), the condition is that φ is true under *every* truth assignment — there are no premises to satisfy, so φ must be universally true. This is exactly the definition of **validity** (also written ⊨ φ). Tautologies like P ∨ ¬P are entailed by the empty set. Second, the **material conditional** P → Q is a syntactic connective in the object language, while Γ ⊨ φ is a meta-level statement about truth preservation across all assignments. These are different levels of discourse: {P} ⊨ Q is a claim about every row where P is true; P → Q is a formula that can itself be assigned a truth value. They come apart: {P} ⊭ Q in general (make P = T, Q = F), but ⊨ (P → Q) → (P → Q) is trivially valid.

Understanding entailment is the foundation for proof systems. When you study natural deduction or resolution, you will find that these are **syntactic proof systems** — they derive conclusions by applying formal rules. The correctness requirement is that these proof systems agree with semantic entailment: you want every syntactically derivable conclusion to be a semantic consequence, and ideally every semantic consequence to be syntactically derivable. These are **soundness** and **completeness** respectively. The semantic notion (Γ ⊨ φ) is the ground truth — it defines what "logically follows" means. The syntactic notion (Γ ⊢ φ) is the algorithmic approximation. The relationship between them — and the remarkable fact that for classical logic they coincide — is the central theorem of mathematical logic.
