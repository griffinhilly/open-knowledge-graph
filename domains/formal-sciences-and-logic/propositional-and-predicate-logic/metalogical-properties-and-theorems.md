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
