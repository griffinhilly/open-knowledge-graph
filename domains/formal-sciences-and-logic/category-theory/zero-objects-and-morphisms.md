---
id: zero-objects-and-morphisms
title: Zero Objects and Zero Morphisms
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: initial-and-terminal-objects
  type: soft
builds-toward:
- additive-categories
- abelian-structure-properties
tags:
- special-objects
- morphisms
- algebraic-structure
stage: expert
status: validated
---

# Zero Objects and Zero Morphisms

## Core Idea
A zero object is simultaneously both initial and terminal—a unique morphism exists from it to every object and from every object to it. A zero morphism is the composite of these unique morphisms, providing a distinguished 'null' morphism from any object to any other. Zero objects allow categories to encode a notion of triviality, essential for developing homological algebra and exact sequences.

## Questions

```yaml
- question: "In the category of sets (Set), why does no zero object exist?"
  type: multiple-choice
  options:
    - "Because Set has too many objects for a zero object to be well-defined"
    - "Because the empty set is initial but not terminal — a terminal object in Set must have exactly one element, not zero"
    - "Because zero objects only exist in algebraic categories, not in set-theoretic categories"
    - "Because morphisms in Set are too general to admit a dual initial-terminal object"
  answer: 1
  explanation: "A zero object must be simultaneously initial AND terminal. In Set, the empty set ∅ is initial (there is a unique empty function from ∅ to any set). But terminal objects in Set are singleton sets {*} — there is exactly one function from any set into a one-element set. Since ∅ ≠ {*}, no single object is both initial and terminal, so Set has no zero object. This is why kernels cannot be defined in Set the same way as in groups or vector spaces — there is no canonical zero morphism."

- question: "Given a zero object 0 in a category with objects A and B, what is the zero morphism 0_{AB}?"
  type: multiple-choice
  options:
    - "A morphism that maps every element of A to the zero element of B"
    - "The composite of the unique morphism A → 0 followed by the unique morphism 0 → B"
    - "The identity morphism on the zero object, extended to act between A and B"
    - "Any morphism whose image is contained in the subobject 0 of B"
  answer: 1
  explanation: "The zero morphism 0_{AB} is defined as the composite: take the unique morphism A → 0 (which exists because 0 is terminal), then compose with the unique morphism 0 → B (which exists because 0 is initial). This composite is canonical — unique, determined entirely by the zero object with no choices involved. Option A describes a concrete element-level action specific to groups or vector spaces, not the categorical definition. The categorical definition via composition works in any category with a zero object, regardless of what 'elements' mean."

- question: "A category can have at most one zero object, up to isomorphism."
  type: true-false
  answer: true
  explanation: "This follows from the universal property. Suppose 0 and 0' are both zero objects. Since 0 is initial, there is a unique morphism f: 0 → 0'. Since 0' is initial, there is a unique morphism g: 0' → 0. The composite g∘f: 0 → 0 must equal the identity (since 0 is initial, there is only one morphism 0 → 0). Similarly f∘g = id_{0'}. So f and g are mutual inverses — they are isomorphisms. This is the standard uniqueness argument for universal objects: initial objects, terminal objects, and zero objects are all unique up to unique isomorphism."

- question: "Zero morphisms are trivial and structurally unimportant — they simply represent 'doing nothing' and have no consequences for the category."
  type: true-false
  answer: false
  explanation: "Zero morphisms are foundational to categorical algebra. Their absorptive property (f ∘ 0_{AB} = 0_{CB} and 0_{AB} ∘ g = 0_{AC}) makes them behave like zero in a ring. More importantly, zero morphisms are required to define kernels and cokernels categorically: the kernel of f : A → B is the equalizer of f and the zero morphism 0_{AB}. Without canonical zero morphisms, these fundamental constructions are undefined, and homological algebra — exact sequences, chain complexes, derived functors — cannot be developed in the category. The zero morphism is the categorical counterpart of the number zero: essential, not trivial."

- question: "Explain why the existence of a zero object automatically provides a canonical zero morphism between any two objects, and why 'canonical' matters here."
  type: short-answer
  answer: "Given a zero object 0, there is a unique morphism from any object A to 0 (since 0 is terminal) and a unique morphism from 0 to any object B (since 0 is initial). The composite A → 0 → B is therefore determined uniquely — there is exactly one way to factor through the zero object. 'Canonical' means this construction requires no choices: you don't pick which morphism A → 0 or 0 → B to use, because each is the only one. This uniqueness is crucial: if the zero morphism required a choice, different choices might give different morphisms with no algebraic coherence, and the absorptive law f ∘ 0 = 0 would fail to hold uniformly across the category."
  explanation: "Compare with Set, where you might try to define a 'zero morphism' A → B as the function mapping everything to some fixed element b ∈ B. But this requires choosing b, and there is no canonical choice — different choices give different morphisms with no consistent algebraic behavior. The zero object forces a canonical choice by routing through the unique initial-terminal object, which is why categories with zero objects are so much better-behaved algebraically than Set."
```

## Explainer

Recall from your study of categories and morphisms that a **morphism** is an arrow between objects — a structure-respecting map. You also know that an **initial object** has exactly one morphism going out to every object, and a **terminal object** has exactly one morphism coming in from every object. A **zero object** is the remarkable case where a single object plays both roles simultaneously: there is a unique morphism from it to every object *and* a unique morphism from every object to it.

The simplest example is the trivial group {e} in the category of groups. Any group homomorphism into the trivial group must send everything to e (unique), and any homomorphism out of the trivial group must send e to e (unique). So the trivial group is both initial and terminal — a zero object. Similarly, in the category of vector spaces over a field, the zero-dimensional vector space {0} is a zero object. In contrast, in the category of sets, the empty set is initial (unique empty function from ∅ to any set) but a one-element set is terminal — neither is both, so **Set** has no zero object.

Once you have a zero object 0, you get a distinguished morphism between *any* two objects A and B for free: compose the unique morphism A → 0 with the unique morphism 0 → B. This composite is called a **zero morphism** and is written 0_{AB}. The zero morphism plays the role of the "do nothing meaningful" arrow — it always factors through the zero object. Crucially, composing any morphism with a zero morphism gives another zero morphism: f ∘ 0_{AB} = 0_{CB} and 0_{AB} ∘ g = 0_{AC}. This absorptive property is exactly what you'd expect of "zero" in an algebraic setting.

Why does this matter? Zero morphisms let you define **kernels** and **cokernels** categorically. The kernel of a morphism f : A → B is (categorically) the equalizer of f and the zero morphism 0_{AB} — it captures "what f sends to zero." Without a zero object, there is no canonical zero morphism and hence no way to define kernels and cokernels in categorical terms. These are the building blocks of **exact sequences**, which in turn underpin all of homological algebra. So the zero object is not a minor technicality — it is the categorical foundation that makes the machinery of algebra work in an abstract setting.

