---
id: inner-models-relative-consistency
title: Inner Models and Relative Consistency Proofs
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: constructible-universe
  type: hard
- id: reflection-principles-zfc
  type: soft
builds-toward:
- zfc-independence-from-other-axioms
tags:
- inner-models
- consistency
- l
- godel
stage: formal-systems
status: draft
---

# Inner Models and Relative Consistency Proofs

## Core Idea
An inner model M is a transitive class satisfying ZFC, contained in V. Gödel's L (constructible sets) is the canonical inner model; it satisfies GCH, the axiom of choice, and V=L. Other inner models (HOD, L[0#], etc.) capture different set-theoretic properties. Relative consistency is proved by embedding statements into inner models: if M ⊨ φ for a statement φ and M ⊆ V, then Con(ZFC) implies Con(ZFC + φ).

## How It's Best Learned
Define L recursively: L₀ = ∅, L_{α+1} = Def(L_α), and L_λ = ⋃_{α < λ} L_α, where Def denotes definable subsets. Prove L ⊨ ZFC. Show Con(ZFC) → Con(ZFC + CH) via the canonical inner model. Explore other inner models and their properties.

## Common Misconceptions
- Assuming inner models are 'true' (they are one model among many; V may not equal L).
- Confusing relative consistency with resolution (GCH is consistent with and independent of ZFC, so neither is 'correct').
