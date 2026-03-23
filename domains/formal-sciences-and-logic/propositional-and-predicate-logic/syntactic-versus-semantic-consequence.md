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
status: validated
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

## Questions

```yaml
- question: "A logician says: 'I can verify that Γ ⊢ φ by checking all possible interpretations.' What is wrong with this?"
  type: multiple-choice
  options:
    - "Nothing — checking all interpretations is exactly how ⊢ is defined"
    - "The ⊢ relation is syntactic: it is verified by inspecting a finite proof derivation, not by examining models"
    - "You can only check interpretations for propositional logic, not first-order logic"
    - "The statement should use ⊨, not ⊢, since both notations mean the same thing"
  answer: 1
  explanation: "Γ ⊢ φ (syntactic consequence) means a finite derivation exists from Γ to φ using the proof system's rules. Verification is mechanical: examine the sequence of rule applications. Γ ⊨ φ (semantic consequence) is the one defined by checking all models — an infinitary claim. Using 'check all interpretations' to verify ⊢ confuses the two notions. Option D reflects the common error of treating ⊢ and ⊨ as synonymous; their coincidence for FOL is a theorem (soundness + completeness), not a definition."

- question: "Gödel's completeness theorem for first-order logic states:"
  type: multiple-choice
  options:
    - "Every true sentence in any model of arithmetic is provable in FOL"
    - "If Γ ⊨ φ (φ is true in every model of Γ), then Γ ⊢ φ (φ is provable from Γ)"
    - "No consistent formal system can prove all truths about the natural numbers"
    - "Every syntactically valid FOL formula is also semantically valid"
  answer: 1
  explanation: "Completeness (⊨ ⇒ ⊢) is the direction that says: if φ holds in every model where Γ holds, then φ is provable from Γ in the proof system. This is non-trivial — it says the proof system is powerful enough to capture all semantic truth expressible in FOL. Option C describes Gödel's *incompleteness* theorem for arithmetic (a different, later result). Option A confuses FOL completeness with second-order or arithmetic completeness. Option D mixes up 'syntactically valid formula' with 'semantically valid formula', neither of which captures the Γ ⊢ φ / Γ ⊨ φ distinction."

- question: "Soundness of a proof system means: anything provable (⊢) is semantically valid (⊨)."
  type: true-false
  answer: true
  explanation: "Soundness (⊢ ⇒ ⊨) says the proof system is trustworthy — it cannot derive a false conclusion from true premises. Proof: show that every axiom is semantically valid, then show by structural induction that every inference rule preserves truth. A sound system never produces a provable but false formula. Without soundness, the proof system would be useless for establishing truth. Completeness is the converse direction (⊨ ⇒ ⊢) — a much harder theorem."

- question: "Because Γ ⊢ φ and Γ ⊨ φ are equivalent for first-order logic (by soundness and completeness), they refer to the same concept and the distinction between them is merely notational."
  type: true-false
  answer: false
  explanation: "Extensional equivalence (same extension — same set of provable/valid pairs) does not imply conceptual identity. ⊢ is defined syntactically: a finite proof derivation exists. ⊨ is defined semantically: truth in every model (an infinitary claim). Their definitions are completely independent; their coincidence for classical FOL is a theorem. The distinction matters: in second-order logic, ⊢ and ⊨ come apart — there are semantic truths with no second-order proof (incompleteness). In intuitionistic logic, ⊢ and ⊨ diverge in different ways. Preserving the conceptual distinction is what lets us recognize and reason about logics where they fail to align."

- question: "Why is the distinction between ⊢ and ⊨ conceptually important even in classical first-order logic, where they coincide by soundness and completeness?"
  type: short-answer
  answer: "The distinction separates two fundamentally different questions: 'What can be proved?' (computational, proof-search, syntactic) versus 'What is true in all models?' (model-theoretic, semantic). Even when they have the same answer in FOL, they are answered by entirely different methods and can come apart in other logics. Second-order logic is sound but not complete — ⊨ is strictly larger than ⊢. Intuitionistic logic has different ⊢ and ⊨ relations. Understanding the distinction as conceptual rather than notational is what lets you recognize incompleteness (when ⊨ outstrips ⊢) and what the completeness theorem actually achieves: it identifies classical FOL as a fortunate special case where the two coincide."
  explanation: "A student who treats ⊢ and ⊨ as notational variants cannot understand what Gödel's incompleteness theorems say — because those theorems are precisely about the gap between provability and truth in certain formal systems. The completeness theorem closes the gap for FOL; incompleteness opens it for arithmetic. Neither result makes sense without a clear prior understanding that ⊢ and ⊨ are defined independently and can diverge."
```

## Explainer

You already know that logical consequence (⊨) is a semantic relation — Γ ⊨ φ when φ is true in every model satisfying Γ — and you know the soundness and completeness results for both propositional logic and first-order logic. The distinction between **⊢** and **⊨** is the distinction between *how reasoning is implemented* and *what reasoning is about*. One is a mechanical, syntactic procedure; the other is a mathematical relationship defined by truth in models. They answer the same question from different angles.

Concretely: Γ ⊢ φ says that starting from Γ, you can derive φ by applying the rules of some proof system in a finite sequence of steps. The derivation is a formal object — a string of symbols manipulated according to fixed rules, with no reference to meaning. Γ ⊨ φ says that for every interpretation that makes Γ true, that interpretation also makes φ true. This is an infinitary claim about all possible models, which may be uncountable in number. The two notions are defined entirely independently; their relationship is a theorem, not a definition.

**Soundness** (⊢ implies ⊨) is proved by structural induction on proofs: every axiom is semantically valid, and every rule of inference preserves truth. This shows the proof system is trustworthy — it cannot derive something false from true premises. **Completeness** (⊨ implies ⊢) is the non-trivial direction. For propositional logic, completeness can be established by a truth-table argument or by a normal form argument. For first-order logic, Gödel's 1929 proof constructs a model from "syntactic objects" — maximal consistent sets of sentences — and shows that the constructed model satisfies exactly what is consistent with Γ. Completeness says the proof system is *powerful enough* to capture all semantic truth.

With both soundness and completeness in hand, ⊢ and ⊨ are extensionally equivalent for first-order logic: Γ ⊢ φ if and only if Γ ⊨ φ. This does *not* mean they are the same concept. They can diverge in weaker or stronger logics: **second-order logic** is sound but *not complete* — there are semantic truths with no second-order proof. **Intuitionistic logic** has a proof system that differs from classical logic even though both target "truth in models." The distinction between ⊢ and ⊨ remains conceptually crucial even when they coincide, because it separates the question of *what can be proved* (a computational, proof-search question) from *what is true* (a model-theoretic question). Completeness is the lucky coincidence that, for classical first-order logic, the two questions have the same answer.
