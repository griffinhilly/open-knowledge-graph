---
id: logical-consequence-and-entailment
title: Logical Consequence and Entailment
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-equivalence-formulas
  type: hard
- id: interpretation-truth-satisfaction-formulas
  type: hard
- id: well-formed-formulas-logic
  type: soft
builds-toward:
- satisfiability-and-unsatisfiability
- deduction-theorem-propositional
- compactness-propositional-logic
tags:
- propositional-logic
- consequence
- inference
stage: formal-systems
status: validated
---

# Logical Consequence and Entailment

## Core Idea
A set of formulas Γ entails a formula φ (written Γ ⊨ φ) if every interpretation that makes all formulas in Γ true also makes φ true. This semantic notion of consequence is central to understanding what it means for one set of premises to logically justify a conclusion.

## How It's Best Learned
Distinguish between entailment (semantic, truth-based) and derivability (syntactic, proof-based). Work with small concrete examples showing when entailment holds and when counterexamples exist.

## Common Misconceptions
- Confusing entailment with the material conditional (→): A ⊨ B means every model of A is a model of B, not that A → B is true.
- Thinking that A ⊨ B means A and B must have similar structure.

## Questions

```yaml
- question: "Which of the following correctly describes what Γ ⊨ φ means?"
  type: multiple-choice
  options: ["There exists a proof of φ from Γ using inference rules", "Every interpretation that satisfies all formulas in Γ also satisfies φ", "φ logically implies every formula in Γ", "φ is a tautology whenever Γ contains at least one tautology"]
  answer: 1
  explanation: "Γ ⊨ φ is a semantic (model-theoretic) definition: φ holds in every interpretation where all of Γ holds. It makes no reference to proofs or derivation rules. Option (a) describes syntactic derivability (Γ ⊢ φ), which is related but distinct — they coincide only because of the soundness and completeness theorems. Options (c) and (d) get the direction and conditions wrong."

- question: "If A ⊨ B (A semantically entails B), then the material conditional A → B is a tautology."
  type: true-false
  answer: true
  explanation: "If every interpretation satisfying A also satisfies B, then no interpretation makes A true and B false. But making A true and B false is the only way to make A → B false. So A → B is true in every interpretation — it is a tautology. This equivalence is the deduction theorem for semantic consequence: {A} ⊨ B if and only if ⊨ (A → B)."

- question: "What is the difference between semantic entailment (Γ ⊨ φ) and syntactic derivability (Γ ⊢ φ), and what theorem relates them?"
  type: short-answer
  answer: "Semantic entailment holds when every model of Γ satisfies φ (truth-based). Syntactic derivability holds when there is a formal proof of φ from Γ using inference rules (proof-based). The soundness and completeness theorems together establish that Γ ⊨ φ if and only if Γ ⊢ φ for standard proof systems."
  explanation: "Soundness says every derivable formula is semantically valid (proofs preserve truth), and completeness says every semantic entailment is derivable (truth implies provability). Together they show the proof system captures exactly the semantic content of the logic — a deep result meaning you can study truth by studying proofs and vice versa."
```

## Explainer

The notion of logical consequence makes precise what it means for a conclusion to *follow from* premises. You already understand logical equivalence — when two formulas are true in exactly the same models. Entailment is a directed version of this: Γ ⊨ φ says the premises in Γ *force* φ to be true, in the sense that φ holds in every interpretation where all of Γ holds. If any interpretation satisfies all of Γ but falsifies φ, that interpretation is a *counterexample*, and the entailment fails.

The definition is entirely semantic — it quantifies over all interpretations with no reference to proofs. To verify Γ ⊨ φ, you consider every possible assignment of truth values to propositional atoms, restrict attention to those satisfying every formula in Γ, and check that φ is satisfied in all of them. For finite sets Γ in propositional logic, this is mechanically checkable via truth tables, though the procedure grows exponentially with the number of atoms.

A common confusion is between entailment and the material conditional. The formula A → B is a sentence in the object language — it may be true in some interpretations and false in others. The entailment {A} ⊨ B is a metalevel claim about all interpretations simultaneously. They are related: {A} ⊨ B if and only if A → B is a *tautology* (true in every interpretation). But "A → B is true in this particular interpretation" is a much weaker statement than "A entails B." Confusing these two levels — the object language and the metalanguage — is one of the most persistent sources of error in logic.

Entailment (⊨) must also be distinguished from syntactic derivability (⊢), which asks whether φ can be derived from Γ using a fixed set of proof rules. These are conceptually independent notions: a proof system is *sound* if Γ ⊢ φ implies Γ ⊨ φ (every derivable formula is a genuine semantic consequence), and *complete* if Γ ⊨ φ implies Γ ⊢ φ (every semantic consequence is provable). Soundness and completeness together establish that for standard logical systems, the semantic and syntactic notions coincide — a profound alignment that is far from obvious a priori.

Understanding entailment also illuminates what makes an argument *invalid*. A deductive argument is valid precisely when the premises entail the conclusion — when there is no interpretation making all premises true and the conclusion false. Finding such a counterexample is the formal version of what informal logicians call "showing the argument is invalid." This connection between model-theoretic semantics and practical argumentation is what gives logical consequence its central role in both formal logic and everyday reasoning.
