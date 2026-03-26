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
- id: zfc-axiom-system-consistency-and-limits
  type: soft
builds-toward:
- reflection-principles-zfc
- inner-models-relative-consistency
tags:
- elementary-submodels
- preservation
- models
- zfc
stage: advanced
status: validated
---
# Elementary Submodels of ZFC

## Core Idea
A submodel M ⊆ V is elementary (M ≺ V) if every first-order formula has the same truth value in M and in V. Elementary submodels are 'small copies' of V satisfying all ZFC axioms locally. By the Löwenheim-Skolem theorem, arbitrarily large countable elementary submodels exist. They are tools for constructing models and proving consistency results.

## How It's Best Learned
Use the Löwenheim-Skolem theorem to construct countable M ≺ V containing desired elements (e.g., all reals). Verify that M satisfies ZFC (even though M is countable, its 'power set' P^M differs from V's P^V). Apply to model-theoretic independence proofs.

## Common Misconceptions
- Assuming M ≺ V means M inherits all properties of V (some properties like uncountability are extrinsic).
- Forgetting that elementary submodels satisfy first-order logic only; second-order properties may differ.

## Questions

```yaml
- question: "A countable set M is constructed so that M ≺ V (the full set-theoretic universe). Inside M, the statement 'ℝ is uncountable' is true — M ⊨ ¬∃ bijection from ω to ℝ^M. From V's perspective, M itself is countable. How is this possible?"
  type: multiple-choice
  options:
    - "It is a contradiction — if M is countable then M cannot satisfy the uncountability of ℝ"
    - "The bijection between ω and M's reals exists in V but not in M, so uncountability is not absolute across models"
    - "M uses a different logic where 'uncountable' means something weaker than in V"
    - "The Löwenheim-Skolem theorem guarantees that M is actually uncountable despite appearances"
  answer: 1
  explanation: "This is Skolem's Paradox, and option B is its resolution. 'Uncountable' means 'no bijection to ω exists in this model.' M lacks the bijection that witnesses countability — that bijection exists in V but not as an element of M — so from M's internal perspective its reals are uncountable. The lesson: uncountability is not an absolute property. It depends on which functions the model contains. Option A is the naive reaction; option C misunderstands that M uses ordinary first-order logic."

- question: "What is the key difference between a formula being 'absolute' for a transitive model and a model being an 'elementary submodel'?"
  type: multiple-choice
  options:
    - "They are the same: absoluteness and elementarity both require all formulas to have the same truth value"
    - "Absoluteness applies only to Δ₀ (bounded) formulas; elementary submodels preserve all first-order formulas simultaneously"
    - "Elementary submodels are stronger because they must be transitive, while absolute formulas hold in non-transitive models"
    - "Absoluteness is a property of a single formula; elementary submodels only guarantee preservation of atomic formulas"
  answer: 1
  explanation: "Absoluteness is formula-specific: a Δ₀ formula has the same truth value in any transitive model as in V, but higher-complexity formulas (Σ₁, Π₁, etc.) may not. An elementary submodel M ≺ V preserves every first-order formula simultaneously — even Σ_n formulas for all n. The price is that M need not be transitive. Option C reverses the relationship: transitive models support absoluteness, but elementary submodels need not be transitive."

- question: "If M ≺ V, then M and V agree on which sets are countable — a set is countable in M if and primarily if it is countable in V."
  type: true-false
  answer: false
  explanation: "False. This is precisely what Skolem's Paradox denies. A set X can be countable in V (there exists a bijection f: ω → X in V) while being 'uncountable' from M's perspective, simply because f is not an element of M. Countability is not absolute — it depends on which functions are present in the model. M ≺ V preserves all first-order sentences, but 'X is countable' quantifies over functions, and the relevant functions may not be in M."

- question: "Every ZFC axiom holds in M if M ≺ V, because each ZFC axiom is a first-order sentence true in V."
  type: true-false
  answer: true
  explanation: "True. The ZFC axioms are first-order sentences (e.g., the Axiom of Extensionality, Pairing, Union, Power Set schema, etc.). Since M ≺ V means M and V agree on the truth of every first-order sentence with parameters from M, and the axioms are sentences with no free variables (or universally quantified), they are all true in M. This is why elementary submodels are useful for constructing models of ZFC: you get ZFC for free from elementarity."

- question: "Explain why a countable elementary submodel M of V can satisfy 'there are uncountably many reals,' and what this reveals about the concept of uncountability in set theory."
  type: short-answer
  answer: "M satisfies 'ℝ is uncountable' because uncountability means 'no bijection from ω to ℝ exists in this model.' The bijection that witnesses M's countability from V's perspective is not itself an element of M — it exists in V but outside M. Since M cannot 'see' this bijection, it correctly (by its own lights) concludes its reals are uncountable. This reveals that uncountability is model-relative, not absolute: it depends on which functions exist within the model, not on any intrinsic cardinality property."
  explanation: "Skolem's Paradox is a feature, not a bug. It shows that 'uncountable' is not an intrinsic property of a set but a relational one: X is uncountable relative to a model M iff no bijection f: ω → X is an element of M. This is why set theorists distinguish between 'internally uncountable' (no such bijection in M) and 'externally countable' (such a bijection exists in V). The same insight drives forcing: by carefully choosing what functions a model contains, you can make it satisfy radically different cardinality claims."
```

## Explainer

From your work on model interpretation and satisfaction, you know what it means for a formula to be true in a structure: M ⊨ φ[ā] when the elements ā from M satisfy φ according to M's interpretation. Now consider a substructure M ⊆ V (the set-theoretic universe): M has the same membership relation ∈ but contains fewer sets. A **submodel** M is **elementary** (written M ≺ V) if for every first-order formula φ(x₁, …, xₙ) and every tuple ā from M, we have M ⊨ φ[ā] iff V ⊨ φ[ā]. Elementarity is not just about preserving some formulas — it is about preserving *all* first-order formulas simultaneously.

You have seen absoluteness of formulas: some formulas (like Δ₀ formulas, bounded quantification) have the same truth value in any transitive model as in V. Elementary submodels are stronger: M ≺ V means *all* first-order formulas are preserved, not just the absolute ones. This comes at a price — elementary submodels need not be transitive. The price reveals a deep feature of set theory: M ≺ V can be countable, even when V ⊨ "there exist uncountably many reals." From M's perspective, its "reals" are uncountable (M ⊨ ¬∃ bijection from ω to ℝ^M), but from V's perspective, M itself is countable. This is **Skolem's Paradox**, and its resolution is that "uncountability" is not absolute — it depends on which bijections exist in which model.

The **Löwenheim-Skolem theorem** guarantees that elementary submodels exist and can be made countable. The construction is explicit: start with any countable set A₀ ⊆ V (say, all the parameters you care about). For each formula φ(x, ā) with ā ∈ A₀ that is satisfiable in V, add one witness to A₁. Iterate: A_{n+1} adds witnesses for all formulas with parameters from Aₙ. Then M = ∪_n Aₙ is a countable elementary submodel of V containing all elements of A₀. This construction is called a **Skolem hull** and it gives fine control: you can ensure M contains any desired countable set of parameters.

Elementary submodels are tools for the construction of independence results. To show a statement S is consistent with ZFC, it suffices to find a model of ZFC in which S holds. Elementary submodels provide "small" models of ZFC that are easier to work with: since M ≺ V, M satisfies every ZFC axiom (each being a first-order sentence true in V). The restriction to first-order truth is critical — properties like "M is well-founded" or "M has the same power set as V" may differ between M and V. Learning to track which properties are absolute and which are not is the central skill that your prerequisite on absolute formulas prepared you for, and elementary submodels are the context where that skill becomes indispensable.
