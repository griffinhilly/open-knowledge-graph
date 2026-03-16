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
stage: advanced
status: draft
---

# Zero Objects and Zero Morphisms

## Core Idea
A zero object is simultaneously both initial and terminal—a unique morphism exists from it to every object and from every object to it. A zero morphism is the composite of these unique morphisms, providing a distinguished 'null' morphism from any object to any other. Zero objects allow categories to encode a notion of triviality, essential for developing homological algebra and exact sequences.

## Explainer

Recall from your study of categories and morphisms that a **morphism** is an arrow between objects — a structure-respecting map. You also know that an **initial object** has exactly one morphism going out to every object, and a **terminal object** has exactly one morphism coming in from every object. A **zero object** is the remarkable case where a single object plays both roles simultaneously: there is a unique morphism from it to every object *and* a unique morphism from every object to it.

The simplest example is the trivial group {e} in the category of groups. Any group homomorphism into the trivial group must send everything to e (unique), and any homomorphism out of the trivial group must send e to e (unique). So the trivial group is both initial and terminal — a zero object. Similarly, in the category of vector spaces over a field, the zero-dimensional vector space {0} is a zero object. In contrast, in the category of sets, the empty set is initial (unique empty function from ∅ to any set) but a one-element set is terminal — neither is both, so **Set** has no zero object.

Once you have a zero object 0, you get a distinguished morphism between *any* two objects A and B for free: compose the unique morphism A → 0 with the unique morphism 0 → B. This composite is called a **zero morphism** and is written 0_{AB}. The zero morphism plays the role of the "do nothing meaningful" arrow — it always factors through the zero object. Crucially, composing any morphism with a zero morphism gives another zero morphism: f ∘ 0_{AB} = 0_{CB} and 0_{AB} ∘ g = 0_{AC}. This absorptive property is exactly what you'd expect of "zero" in an algebraic setting.

Why does this matter? Zero morphisms let you define **kernels** and **cokernels** categorically. The kernel of a morphism f : A → B is (categorically) the equalizer of f and the zero morphism 0_{AB} — it captures "what f sends to zero." Without a zero object, there is no canonical zero morphism and hence no way to define kernels and cokernels in categorical terms. These are the building blocks of **exact sequences**, which in turn underpin all of homological algebra. So the zero object is not a minor technicality — it is the categorical foundation that makes the machinery of algebra work in an abstract setting.

