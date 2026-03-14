---
id: deductive-reasoning-and-formal-proofs
title: Deductive Reasoning and Formal Proof Systems
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-implication-entailment
  type: soft
builds-toward:
- natural-deduction-propositional
- natural-deduction-fol
- resolution-fol
- sequent-calculus-intro
tags:
- proof-theory
- inference
- deduction
stage: formal-systems
status: draft
---

# Deductive Reasoning and Formal Proof Systems

## Core Idea
Deductive reasoning formalizes proving conclusions from premises using explicit inference rules. A proof system defines axioms and rules that allow deriving new formulas from given ones. A formula is provable from Γ (Γ ⊢ φ) if there exists a finite derivation sequence using the rules.

## How It's Best Learned
Study concrete proof systems and practice constructing proofs. Compare different systems (natural deduction is intuitive; sequent calculus is systematic; resolution is computational). Understand the syntactic/semantic distinction.

## Common Misconceptions
Thinking proof systems are purely mechanical. Confusing a proof of φ with proof that φ is true. Assuming different systems prove different theorems (Completeness Theorem shows they do not for first-order logic).
