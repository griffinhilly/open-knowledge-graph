---
id: hilbert-system-propositional
title: Hilbert System for Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-soundness-completeness
  type: hard
- id: proof-structure-and-terminology
  type: soft
builds-toward:
- sequent-calculus-intro
tags:
- Hilbert-system
- axiom-schema
- modus-ponens
- deduction-theorem
- axiomatic-proof
stage: formal-systems
status: draft
---

# Hilbert System for Propositional Logic

## Core Idea
A Hilbert system (or Hilbert-style calculus) derives theorems from a small set of axiom schemas using modus ponens as the sole inference rule: from φ and φ → ψ, infer ψ. Typical axiom schemas include φ → (ψ → φ) and (φ → (ψ → χ)) → ((φ → ψ) → (φ → χ)). The deduction theorem — if Γ ∪ {φ} ⊢ ψ then Γ ⊢ φ → ψ — bridges the gap between derivation and implication, making Hilbert proofs tractable despite their apparent rigidity. Hilbert systems are historically important as the first fully formalized proof systems and remain standard in metatheory.

## How It's Best Learned
Prove simple theorems (e.g., φ → φ) from the axiom schemas and modus ponens alone, experiencing the difficulty firsthand. Then prove the deduction theorem and see how it dramatically simplifies subsequent proofs by allowing assumption discharge.

## Common Misconceptions
- Hilbert systems are not impractical — they are unwieldy for finding proofs but powerful for proving metatheorems about proofs.
- Modus ponens is the only rule, but the axiom schemas do the heavy lifting — different choices of axioms yield different but equivalent systems.
- The deduction theorem is not an axiom — it is a metatheorem about the proof system, proved by induction on derivation length.

## Explainer

You know from soundness and completeness that propositional logic has a clean semantic theory: a formula is a tautology iff it is true under every valuation. The Hilbert system asks a different question: can we derive tautologies *syntactically*, from axioms and rules alone, without ever appealing to truth tables? The answer is yes — and the Hilbert system does it with a striking minimalism: just axiom schemas and **modus ponens** (MP), the rule "from φ and φ→ψ, conclude ψ."

The axiom schemas are typically three (there are equivalent alternatives, but the classic set includes):
- **K**: φ → (ψ → φ) — any true thing is implied by anything
- **S**: (φ → (ψ → χ)) → ((φ → ψ) → (φ → χ)) — a form of distribution
- **DN** (or a negation axiom): ¬¬φ → φ — double negation elimination

These three schemas and MP are sufficient to derive *every propositional tautology*. The proof of this is the completeness theorem for Hilbert systems, which mirrors the semantic completeness you already know. **Soundness** is straightforward: every axiom schema is a tautology, and MP preserves tautologies, so every derivable formula is a tautology.

The obstacle is that Hilbert proofs are painful to *find*. Even proving φ → φ (a trivial tautology) takes several steps using K and S. The **deduction theorem** is the key that unlocks tractability: if from Γ ∪ {φ} you can derive ψ, then from Γ alone you can derive φ → ψ. This means you can treat assumptions as temporary hypotheses, discharge them at the end by "moving them into the arrow," and this transformation is always possible. The deduction theorem is proved by induction on the derivation length: for each step in the derivation of ψ from Γ ∪ {φ}, construct a corresponding derivation of φ → (that step) from Γ. The base cases (axioms and the assumption φ itself) require using K and a self-application of K+S; the inductive step for MP is an application of S. It is a metatheorem — a theorem *about* the proof system, not *in* it.

**Why Hilbert systems matter**, despite their awkwardness: they isolate the logical content in the axioms themselves, making it easy to study what changes when you modify the logic. If you want intuitionistic logic, drop the double-negation axiom. If you want modal logic, add a necessity axiom. If you want relevance logic, restrict K. The single inference rule means that any two derivations with the same conclusion are related by a simple structural analysis. Natural deduction and sequent calculi (which you will study next) are more ergonomic for constructing proofs, but Hilbert systems remain the standard tool for **metatheory** — proving things about logics rather than within them.

