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
