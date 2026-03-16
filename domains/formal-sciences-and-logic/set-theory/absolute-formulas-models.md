---
id: absolute-formulas-models
title: Absolute Formulas and Model-Theoretic Absoluteness
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: model-theory-basics
  type: hard
- id: cumulative-hierarchy-ranks
  type: soft
builds-toward:
- elementary-submodels-zfc
- reflection-principles-zfc
tags:
- absoluteness
- models
- inner-models
- formulas
stage: formal-systems
status: draft
---

# Absolute Formulas and Model-Theoretic Absoluteness

## Core Idea
A formula φ is absolute for a model M if M ⊨ φ(x) holds if and only if V ⊨ φ(x) holds, for parameters x in M. Absolute formulas preserve truth across models and meta-models. Many core set-theoretic notions (∈, ⊆, ordinal, etc.) are absolute, but others (cardinality, measurability) are not. Absoluteness is crucial for inner-model constructions.

## How It's Best Learned
Verify that 'x is an ordinal' is absolute: check that L and V agree on which sets are ordinals. Show that 'κ is measurable' is NOT absolute (measurability can differ between models). Use downward absoluteness to prove properties are preserved by inner models.

## Common Misconceptions
- Confusing absoluteness with truth; a formula can be absolute yet false in both models.
- Assuming all mathematical notions are absolute (cardinality and measurability are examples of non-absolute notions).

## Explainer

You know from **model theory basics** that a formula φ is evaluated relative to a structure — given a model M, "M ⊨ φ" means φ is true in M under some assignment. A natural question arises: if M is a submodel of a larger model V (or an inner model of the set-theoretic universe), does truth of φ transfer? The answer depends on the formula. A formula φ(x) is **absolute** between two models M ⊆ V if for every element a ∈ M, M ⊨ φ(a) if and only if V ⊨ φ(a). Absoluteness means the formula's truth value does not depend on which model you evaluate it in, as long as the element is in both.

The simplest absolute formulas are those built only from **bounded quantifiers** — quantifiers of the form ∀x ∈ a or ∃x ∈ a, where the quantifier ranges only over elements of a specific set rather than over the whole model. These are called **Δ₀ formulas**. A Δ₀ formula can only "see" elements of a specific set, so it cannot be affected by adding or removing objects outside that set. For example, "x ∈ y" is Δ₀ and absolute: whether a is in b is a fact about a and b themselves, independent of the ambient model. Similarly, "x is an ordinal" and "x is a natural number" are absolute — these are intrinsic structural properties that inner models cannot change.

Non-absoluteness arises when quantifiers range over the whole universe, because different models may have different universes. **Cardinality** is the classic example. A cardinal κ might be uncountable in an inner model M (M ⊨ "κ is uncountable") but countable in a larger model V where new bijections exist that M could not see. This is precisely what happens in Cohen's forcing: you can build a model where ℵ₁ of the ground model becomes countable. Similarly, **measurability** is not absolute: a cardinal κ can be measurable in an inner model without being measurable in the full universe, or vice versa, depending on the structure of ultrafilters available.

Absoluteness is critical for **inner model constructions**. When building L (Gödel's constructible universe) or other inner models, you want certain key set-theoretic notions to mean the same thing inside L as they do in V. If "x is an ordinal" is absolute between L and V, then L and V agree on what the ordinals are — L's ordinals are exactly V's ordinals, just as seen from within L. This allows results proved in L to transfer to V and vice versa for absolute notions. The technical framework of Δ₀ → Δ₁ → Σ₁/Π₁ absoluteness is the systematic study of which formulas are absolute between which pairs of models, and it underlies virtually every theorem in inner model theory and forcing.
