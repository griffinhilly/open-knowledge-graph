---
id: syntactic-versus-semantic-consequence
title: Syntactic Consequence (⊢) Versus Semantic Consequence (⊨)
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-consequence-and-entailment
  type: hard
- id: propositional-soundness-completeness
  type: hard
- id: fol-soundness-completeness
  type: hard
builds-toward:
- godel-completeness-theorem-first-order
tags:
- consequence
- entailment
- soundness
- completeness
stage: formal-systems
status: draft
---

# Syntactic Consequence (⊢) Versus Semantic Consequence (⊨)

## Core Idea
Γ ⊢ φ (syntactic consequence) means φ can be derived from Γ using inference rules of a proof system. Γ ⊨ φ (semantic consequence) means φ is true in all models where Γ is true. The two notions are distinct: ⊢ is about provability, ⊨ is about validity. Soundness says ⊢ ⇒ ⊨ (no false proofs), and completeness says ⊨ ⇒ ⊢ (no missing proofs). For first-order logic, completeness holds, so the two notions coincide. Understanding their relationship is key to foundational logic.

## How It's Best Learned
Illustrate with examples in propositional logic using truth tables. Discuss a simple proof system and verify soundness. Distinguish the two notions by considering unprovable but valid formulas (before completeness is proved) and unprovable invalid formulas. Understand that completeness is a non-trivial metatheorem, not an axiom.

## Common Misconceptions
- Using ⊢ and ⊨ interchangeably without understanding the distinction.
- Thinking that ⊨ is decidable (it's not in general — even checking semantic consequence requires reasoning about all models).
- Assuming ⊢ and ⊨ differ substantially (completeness shows they align for first-order logic).

## Explainer

You already know that logical consequence (⊨) is a semantic relation — Γ ⊨ φ when φ is true in every model satisfying Γ — and you know the soundness and completeness results for both propositional logic and first-order logic. The distinction between **⊢** and **⊨** is the distinction between *how reasoning is implemented* and *what reasoning is about*. One is a mechanical, syntactic procedure; the other is a mathematical relationship defined by truth in models. They answer the same question from different angles.

Concretely: Γ ⊢ φ says that starting from Γ, you can derive φ by applying the rules of some proof system in a finite sequence of steps. The derivation is a formal object — a string of symbols manipulated according to fixed rules, with no reference to meaning. Γ ⊨ φ says that for every interpretation that makes Γ true, that interpretation also makes φ true. This is an infinitary claim about all possible models, which may be uncountable in number. The two notions are defined entirely independently; their relationship is a theorem, not a definition.

**Soundness** (⊢ implies ⊨) is proved by structural induction on proofs: every axiom is semantically valid, and every rule of inference preserves truth. This shows the proof system is trustworthy — it cannot derive something false from true premises. **Completeness** (⊨ implies ⊢) is the non-trivial direction. For propositional logic, completeness can be established by a truth-table argument or by a normal form argument. For first-order logic, Gödel's 1929 proof constructs a model from "syntactic objects" — maximal consistent sets of sentences — and shows that the constructed model satisfies exactly what is consistent with Γ. Completeness says the proof system is *powerful enough* to capture all semantic truth.

With both soundness and completeness in hand, ⊢ and ⊨ are extensionally equivalent for first-order logic: Γ ⊢ φ if and only if Γ ⊨ φ. This does *not* mean they are the same concept. They can diverge in weaker or stronger logics: **second-order logic** is sound but *not complete* — there are semantic truths with no second-order proof. **Intuitionistic logic** has a proof system that differs from classical logic even though both target "truth in models." The distinction between ⊢ and ⊨ remains conceptually crucial even when they coincide, because it separates the question of *what can be proved* (a computational, proof-search question) from *what is true* (a model-theoretic question). Completeness is the lucky coincidence that, for classical first-order logic, the two questions have the same answer.
