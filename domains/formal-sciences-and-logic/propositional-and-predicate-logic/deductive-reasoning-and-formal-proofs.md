---
id: deductive-reasoning-and-formal-proofs
title: Deductive Reasoning and Formal Proof Systems
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-implication-entailment
  type: soft
- id: mathematical-proof-strategies
  type: soft
- id: mathematical-induction
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

## Explainer

You already understand logical implication: Γ ⊨ φ means every interpretation that satisfies all formulas in Γ also satisfies φ. That is a **semantic** notion — it talks about truth in models. A **proof system** introduces a parallel **syntactic** notion: Γ ⊢ φ means φ can be derived from Γ by applying a finite sequence of explicit rules, without ever asking what is "true." The relationship between ⊨ and ⊢ is the central question of proof theory.

A proof system has two components: **axioms** (formulas taken as given) and **inference rules** (patterns like "from formula A and formula A → B, derive B" — this particular rule is called modus ponens). A **proof** of φ from Γ is a finite sequence of formulas where each step is either an axiom, a member of Γ, or the result of applying an inference rule to earlier steps. The last formula in the sequence is φ. This is entirely syntactic: you can verify a proof by checking, line by line, that each step is licensed — no semantic judgment required.

Different proof systems — **natural deduction**, **sequent calculus**, **Hilbert-style axiom systems**, **resolution** — differ in how they organize the same logical machinery. Natural deduction mirrors mathematical practice: it has introduction and elimination rules for each connective (∧-introduction, →-elimination = modus ponens, etc.), and proofs look like the reasoning a mathematician actually writes. Sequent calculus uses a different format (Γ ⊢ Δ, asserting that not all of Γ can be true while all of Δ are false) and is more symmetric and algorithmic. Hilbert-style systems push almost everything into axioms and use very few rules. Resolution (your prerequisite for CNF) is designed for automated theorem proving.

The **Completeness Theorem** for first-order logic states that these systems all prove exactly the same theorems: Γ ⊢ φ if and only if Γ ⊨ φ. Provability and semantic consequence coincide. This is not trivially obvious — it is a deep theorem (proved by Gödel in 1929) that guarantees proof systems are not missing anything. **Soundness** (⊢ implies ⊨) is the easy direction: if you can prove φ from Γ, then φ really follows from Γ. **Completeness** (⊨ implies ⊢) is the hard direction: if φ follows semantically, then there is always a formal proof. Together they mean the syntactic game of proof and the semantic game of truth are perfectly matched — for first-order logic. (Gödel's *incompleteness* theorems, which you will encounter later, show arithmetic is a different story.)
