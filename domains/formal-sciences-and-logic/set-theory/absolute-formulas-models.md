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
status: validated
---

# Absolute Formulas and Model-Theoretic Absoluteness

## Core Idea
A formula φ is absolute for a model M if M ⊨ φ(x) holds if and only if V ⊨ φ(x) holds, for parameters x in M. Absolute formulas preserve truth across models and meta-models. Many core set-theoretic notions (∈, ⊆, ordinal, etc.) are absolute, but others (cardinality, measurability) are not. Absoluteness is crucial for inner-model constructions.

## How It's Best Learned
Verify that 'x is an ordinal' is absolute: check that L and V agree on which sets are ordinals. Show that 'κ is measurable' is NOT absolute (measurability can differ between models). Use downward absoluteness to prove properties are preserved by inner models.

## Common Misconceptions
- Confusing absoluteness with truth; a formula can be absolute yet false in both models.
- Assuming all mathematical notions are absolute (cardinality and measurability are examples of non-absolute notions).

## Questions

```yaml
- question: "Which of the following correctly explains why 'x is a finite set' is absolute between a transitive inner model M and the full universe V?"
  type: multiple-choice
  options:
    - "All properties of sets are absolute because sets are defined entirely by their elements"
    - "Finiteness can be expressed using only bounded quantifiers (Δ₀), so evaluating it does not depend on what objects exist outside the set in question"
    - "Finiteness is absolute only in models that satisfy the axiom of choice"
    - "The formula is not actually absolute — a set finite in M might be infinite in V if V has more natural numbers"
  answer: 1
  explanation: "Finiteness can be expressed as: 'there is no injection from ω into x,' and with some work this reduces to a Δ₀ statement about the elements of x. Δ₀ formulas use only bounded quantifiers (∀y ∈ a, ∃y ∈ a), which range only over elements of specific sets and cannot be affected by objects outside those sets. Whether x is finite is an intrinsic property of x itself, not of the ambient model. Note: option D is tempting but wrong — V doesn't have 'more natural numbers' than M; ordinals and natural numbers are absolute."

- question: "Consider the claim 'κ is an uncountable cardinal' evaluated in an inner model M versus the full universe V. Why can this fail to be absolute?"
  type: multiple-choice
  options:
    - "Cardinality claims are never absolute between any two models of ZFC"
    - "In a larger model V, there may exist bijections between κ and ω that M cannot see, making κ countable in V even if M sees no such bijection"
    - "Cardinals are ordinals, and ordinals are absolute, so cardinality claims are always absolute"
    - "The claim fails to be absolute only if M does not satisfy the power set axiom"
  answer: 1
  explanation: "Countability is about the existence of an injection from κ into ω. Whether such an injection exists depends on what functions are available in the model. M may contain no bijection between κ and ω, making κ uncountable in M. A larger model V may include additional sets — in particular, additional functions — including a bijection that M cannot see. This is the mechanism of Cohen forcing: you can add a bijection that collapses ℵ₁ of the ground model to a countable set in the extension. Option C is a common but wrong inference: ordinals are absolute, but cardinality (which ordinal is the 'size' of a set) depends on available bijections."

- question: "An absolute formula should be true in at least one model — a formula that is false in most model can rarely be absolute."
  type: true-false
  answer: false
  explanation: "Absoluteness is about truth-preservation between models, not about truth itself. A formula φ is absolute between M and V if for every parameter a in M: M ⊨ φ(a) ↔ V ⊨ φ(a). This bi-conditional is satisfied whether both sides are true or both sides are false. A formula like '0 ≠ 0' is false in every model but trivially absolute between any two, because M ⊨ '0 ≠ 0' is false and V ⊨ '0 ≠ 0' is false, so the equivalence holds. The common misconception confuses absoluteness (a structural relationship between models) with validity (truth in all models)."

- question: "Δ₀ formulas are absolute between transitive models because their bounded quantifiers range over specific sets and cannot be influenced by objects that exist in V but not in M."
  type: true-false
  answer: true
  explanation: "Yes — this is the core absoluteness theorem. A bounded quantifier ∀x ∈ a ranges over the elements of the specific set a, not over the whole model. Since M is a transitive inner model, elements of sets in M are themselves in M (transitivity), so both M and V 'see' the same objects when evaluating ∀x ∈ a. Nothing outside the bounded range can affect the truth value. This is why x ∈ y, x ⊆ y, 'x is an ordinal,' and 'x is a natural number' are all absolute."

- question: "Explain why cardinality is not absolute between models of set theory, using the notion of what a larger model can 'see' that an inner model cannot."
  type: short-answer
  answer: "Cardinality is defined via bijections: a set x has cardinality κ if there is a bijection between x and κ. Whether such a bijection exists depends on which functions are in the model. An inner model M may lack a bijection between two sets x and κ — making x 'uncountable' relative to M — while a larger model V contains that bijection, making x countable in V. Models differ not in which sets they contain (inner models contain the same ordinals), but in which functions and relations they include. Cardinality is therefore not an intrinsic property of the set itself, but a relational property that depends on the ambient model's function space."
  explanation: "This is one of the deepest lessons in set theory: 'size' is model-relative. Cohen's forcing constructs models where ℵ₁ collapses to countable by adding a bijection. The inner model had no such bijection — ℵ₁ was genuinely uncountable from its perspective — but the extension does. Neither model is wrong; they simply have different function spaces."
```

## Explainer

You know from **model theory basics** that a formula φ is evaluated relative to a structure — given a model M, "M ⊨ φ" means φ is true in M under some assignment. A natural question arises: if M is a submodel of a larger model V (or an inner model of the set-theoretic universe), does truth of φ transfer? The answer depends on the formula. A formula φ(x) is **absolute** between two models M ⊆ V if for every element a ∈ M, M ⊨ φ(a) if and only if V ⊨ φ(a). Absoluteness means the formula's truth value does not depend on which model you evaluate it in, as long as the element is in both.

The simplest absolute formulas are those built only from **bounded quantifiers** — quantifiers of the form ∀x ∈ a or ∃x ∈ a, where the quantifier ranges only over elements of a specific set rather than over the whole model. These are called **Δ₀ formulas**. A Δ₀ formula can only "see" elements of a specific set, so it cannot be affected by adding or removing objects outside that set. For example, "x ∈ y" is Δ₀ and absolute: whether a is in b is a fact about a and b themselves, independent of the ambient model. Similarly, "x is an ordinal" and "x is a natural number" are absolute — these are intrinsic structural properties that inner models cannot change.

Non-absoluteness arises when quantifiers range over the whole universe, because different models may have different universes. **Cardinality** is the classic example. A cardinal κ might be uncountable in an inner model M (M ⊨ "κ is uncountable") but countable in a larger model V where new bijections exist that M could not see. This is precisely what happens in Cohen's forcing: you can build a model where ℵ₁ of the ground model becomes countable. Similarly, **measurability** is not absolute: a cardinal κ can be measurable in an inner model without being measurable in the full universe, or vice versa, depending on the structure of ultrafilters available.

Absoluteness is critical for **inner model constructions**. When building L (Gödel's constructible universe) or other inner models, you want certain key set-theoretic notions to mean the same thing inside L as they do in V. If "x is an ordinal" is absolute between L and V, then L and V agree on what the ordinals are — L's ordinals are exactly V's ordinals, just as seen from within L. This allows results proved in L to transfer to V and vice versa for absolute notions. The technical framework of Δ₀ → Δ₁ → Σ₁/Π₁ absoluteness is the systematic study of which formulas are absolute between which pairs of models, and it underlies virtually every theorem in inner model theory and forcing.
