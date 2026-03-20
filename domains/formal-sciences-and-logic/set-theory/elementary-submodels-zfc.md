---
id: elementary-submodels-zfc
title: Elementary Submodels of ZFC
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: model-interpretation-and-satisfaction
  type: hard
- id: absolute-formulas-models
  type: hard
builds-toward:
- reflection-principles-zfc
- inner-models-relative-consistency
tags:
- elementary-submodels
- preservation
- models
- zfc
stage: advanced
status: draft
---

# Elementary Submodels of ZFC

## Core Idea
A submodel M ⊆ V is elementary (M ≺ V) if every first-order formula has the same truth value in M and in V. Elementary submodels are 'small copies' of V satisfying all ZFC axioms locally. By the Löwenheim-Skolem theorem, arbitrarily large countable elementary submodels exist. They are tools for constructing models and proving consistency results.

## How It's Best Learned
Use the Löwenheim-Skolem theorem to construct countable M ≺ V containing desired elements (e.g., all reals). Verify that M satisfies ZFC (even though M is countable, its 'power set' P^M differs from V's P^V). Apply to model-theoretic independence proofs.

## Common Misconceptions
- Assuming M ≺ V means M inherits all properties of V (some properties like uncountability are extrinsic).
- Forgetting that elementary submodels satisfy first-order logic only; second-order properties may differ.

## Explainer

From your work on model interpretation and satisfaction, you know what it means for a formula to be true in a structure: M ⊨ φ[ā] when the elements ā from M satisfy φ according to M's interpretation. Now consider a substructure M ⊆ V (the set-theoretic universe): M has the same membership relation ∈ but contains fewer sets. A **submodel** M is **elementary** (written M ≺ V) if for every first-order formula φ(x₁, …, xₙ) and every tuple ā from M, we have M ⊨ φ[ā] iff V ⊨ φ[ā]. Elementarity is not just about preserving some formulas — it is about preserving *all* first-order formulas simultaneously.

You have seen absoluteness of formulas: some formulas (like Δ₀ formulas, bounded quantification) have the same truth value in any transitive model as in V. Elementary submodels are stronger: M ≺ V means *all* first-order formulas are preserved, not just the absolute ones. This comes at a price — elementary submodels need not be transitive. The price reveals a deep feature of set theory: M ≺ V can be countable, even when V ⊨ "there exist uncountably many reals." From M's perspective, its "reals" are uncountable (M ⊨ ¬∃ bijection from ω to ℝ^M), but from V's perspective, M itself is countable. This is **Skolem's Paradox**, and its resolution is that "uncountability" is not absolute — it depends on which bijections exist in which model.

The **Löwenheim-Skolem theorem** guarantees that elementary submodels exist and can be made countable. The construction is explicit: start with any countable set A₀ ⊆ V (say, all the parameters you care about). For each formula φ(x, ā) with ā ∈ A₀ that is satisfiable in V, add one witness to A₁. Iterate: A_{n+1} adds witnesses for all formulas with parameters from Aₙ. Then M = ∪_n Aₙ is a countable elementary submodel of V containing all elements of A₀. This construction is called a **Skolem hull** and it gives fine control: you can ensure M contains any desired countable set of parameters.

Elementary submodels are tools for the construction of independence results. To show a statement S is consistent with ZFC, it suffices to find a model of ZFC in which S holds. Elementary submodels provide "small" models of ZFC that are easier to work with: since M ≺ V, M satisfies every ZFC axiom (each being a first-order sentence true in V). The restriction to first-order truth is critical — properties like "M is well-founded" or "M has the same power set as V" may differ between M and V. Learning to track which properties are absolute and which are not is the central skill that your prerequisite on absolute formulas prepared you for, and elementary submodels are the context where that skill becomes indispensable.
