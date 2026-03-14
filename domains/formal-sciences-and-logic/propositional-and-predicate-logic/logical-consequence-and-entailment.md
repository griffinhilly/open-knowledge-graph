---
id: logical-consequence-and-entailment
title: Logical Consequence and Entailment
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
- id: model-interpretation-and-satisfaction
  type: hard
builds-toward:
- propositional-soundness-completeness
- fol-soundness-completeness
- syntactic-versus-semantic-consequence
tags:
- semantics
- consequence
- entailment
- validity
stage: formal-systems
status: draft
---

# Logical Consequence and Entailment

## Core Idea
A formula φ is a logical consequence of a set of formulas Γ (written Γ ⊨ φ) if φ is true in every model where all formulas in Γ are true. This is the fundamental semantic notion of entailment: it captures the idea that φ must be true whenever Γ is true. Logical consequence is the semantic counterpart to syntactic derivability (⊢), and establishing their equivalence is the subject of completeness theorems.

## How It's Best Learned
Use truth tables for simple propositional examples (e.g., show that {P, P→Q} ⊨ Q). Move to first-order by discussing models and interpretations explicitly. Draw out the difference between a formula being true in a model vs. true under all models. Practice checking entailment by attempting to build counterexamples.

## Common Misconceptions
- Confusing logical consequence (⊨, semantic) with syntactic derivability (⊢) — they're related but different.
- Thinking that φ follows from Γ means Γ logically implies φ in English (close, but the formal definition requires truth in all models).
- Forgetting that entailment is about all models; a single model where Γ→φ holds doesn't prove Γ ⊨ φ.
