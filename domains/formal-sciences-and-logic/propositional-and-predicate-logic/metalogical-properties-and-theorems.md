---
id: metalogical-properties-and-theorems
title: Metalogical Properties and Foundational Theorems
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: deductive-reasoning-and-formal-proofs
  type: hard
- id: logical-consequence-and-validity
  type: hard
builds-toward:
- fol-soundness-completeness
- compactness-theorem-model-theory
- undecidability-and-gödel
tags:
- metatheory
- foundational-theorems
- formal-systems
stage: formal-systems
status: draft
---

# Metalogical Properties and Foundational Theorems

## Core Idea
Metalogical theorems relate syntax and semantics. Soundness: if Γ ⊢ φ then Γ ⊨ φ. Completeness: if Γ ⊨ φ then Γ ⊢ φ. Gödel's completeness theorem (1929) establishes both for first-order logic. Other results include the Compactness Theorem, Löwenheim-Skolem Theorem, and Gödel's Incompleteness Theorems, which reveal fundamental formal system limitations.

## How It's Best Learned
Study the statements and intuitive meanings of key theorems. Understand why soundness and completeness are desirable. Explore consequences: Compactness follows from completeness; Incompleteness shows arithmetic cannot be finitely axiomatized.

## Common Misconceptions
Thinking Incompleteness Theorem means logic is broken (it reveals profound insights). Confusing logic completeness with theory completeness. Assuming that validity makes finding proofs easy (Completeness is non-constructive).

## Explainer

You already know how to construct formal proofs from premises using inference rules, and you know that logical consequence (⊨) means truth in all models. Metalogical theorems live *above* the formal system: they are mathematical theorems *about* logic, proved using ordinary mathematical reasoning, not within the formal system itself. The two most fundamental properties are **soundness** and **completeness**, and they pair like two halves of a guarantee about the relationship between syntax (proofs) and semantics (truth).

**Soundness** says the proof system never lies: if Γ ⊢ φ (φ is derivable from Γ), then Γ ⊨ φ (φ is true in every model of Γ). Proving soundness is usually straightforward — you verify that every inference rule preserves truth, then argue by induction on proof length. Soundness is a minimum bar for a proof system to be worth using: a system that proves false things is useless. **Completeness** says the proof system never misses: if Γ ⊨ φ, then Γ ⊢ φ. Gödel's 1929 completeness theorem established this for first-order logic. Completeness is surprising and non-trivial: it says that *every* semantic truth has a syntactic proof, however long.

Beyond soundness and completeness, three theorems reshape how you think about the reach of formal systems. The **Compactness Theorem** (a consequence of completeness) says: if every finite subset of Γ has a model, then Γ itself has a model. This seems obvious but is powerful — it lets you build non-standard models by adding axioms one at a time and applying compactness to the whole infinite set. The **Löwenheim-Skolem Theorem** says that any first-order theory with an infinite model has models of every infinite cardinality. Combined, these theorems imply that first-order logic cannot "pin down" a unique structure up to isomorphism — there is no first-order sentence that uniquely characterizes the natural numbers, for instance.

Gödel's **Incompleteness Theorems** (1931) are metalogical results of a different kind. They concern not the proof system for logic but the axiomatic theories of arithmetic. The first theorem says that any consistent, sufficiently strong axiom system for arithmetic is **incomplete** in the sense of *theory completeness*: there exist sentences neither provable nor refutable from the axioms. Note the distinction: this is *not* a failure of logical completeness (the proof system still derives everything that is semantically valid). It is a limitation on what any fixed set of arithmetic axioms can prove. The second theorem adds that such a system cannot prove its own consistency. These results do not mean logic is broken — they reveal a fundamental, unavoidable horizon for formal axiomatic systems.
