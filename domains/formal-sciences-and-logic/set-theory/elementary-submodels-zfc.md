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
stage: formal-systems
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
