---
id: functor-categories
title: Functor Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: natural-transformations
  type: hard
- id: functors
  type: hard
builds-toward:
- yoneda-lemma
- representable-functors
- limits-and-colimits
tags:
- functor category
- 2-category
- presheaf
- diagram
stage: advanced
status: validated
---

# Functor Categories

## Core Idea
Given categories C and D, the functor category [C, D] (also written D^C) has functors F: C → D as objects and natural transformations as morphisms. Composition of natural transformations is defined component-wise and satisfies all category axioms, making functors and natural transformations into a genuine category. Presheaf categories [C^op, Set] are particularly important in mathematics and logic, providing models for sheaf theory, topos theory, and Kripke semantics for intuitionistic logic.

## How It's Best Learned
Verify that vertical composition of natural transformations (composing η: F ⇒ G and ε: G ⇒ H component-wise) is associative and has identity natural transformations. Then recognize that a diagram of shape J in a category C is simply a functor J → C, making limits and colimits into functors on functor categories.

## Common Misconceptions
- The functor category [C, D] may be large (a proper class) even when C and D are small; size issues matter in foundations.
- Horizontal composition and vertical composition of natural transformations are different operations; both are needed for the full 2-categorical structure.

## Questions

```yaml
- question: "In the functor category [C, D], what plays the role of morphisms?"
  type: multiple-choice
  options: ["Functors from C to D", "Objects of D", "Natural transformations between functors F, G: C → D", "Morphisms of C composed with morphisms of D"]
  answer: 2
  explanation: "In [C, D], the objects are functors F: C → D, and the morphisms between two such functors F and G are natural transformations η: F ⇒ G. Composition of morphisms in [C, D] is vertical composition of natural transformations, defined component-wise at each object of C."

- question: "A diagram of shape J in a category C is a collection of objects and morphisms in C indexed by J — it is not necessarily a functor."
  type: true-false
  answer: false
  explanation: "A diagram of shape J in C is precisely a functor J → C. The index category J specifies which objects and morphisms must appear, and the functor sends each object of J to an object of C and each morphism of J to a morphism of C, respecting composition. This is why limits and colimits can be treated as functors on functor categories."

- question: "What is the significance of presheaf categories [C^op, Set], and why do they appear across mathematics and logic?"
  type: short-answer
  answer: "A presheaf on C is a functor C^op → Set, assigning a set to each object of C contravariantly. Presheaf categories are important because every category C embeds fully and faithfully into [C^op, Set] via the Yoneda embedding, and because presheaves model variable sets over a base, appearing in sheaf theory, topos theory, and Kripke semantics for intuitionistic logic."
  explanation: "The Yoneda embedding sends each object c ∈ C to the representable presheaf Hom(−, c): C^op → Set. The embedding is full and faithful, meaning [C^op, Set] contains a faithful copy of C — any category can be studied by studying its presheaves. The topos-theoretic and logical applications follow from the fact that [C^op, Set] always has limits, colimits, and an internal logic."
```

## Explainer

You have seen that functors are structure-preserving maps between categories, and that natural transformations are maps between functors that respect the functorial structure. The key insight of functor categories is that functors and natural transformations themselves form a category — with functors as objects and natural transformations as morphisms.

Given two categories C and D, the **functor category** [C, D] (also written D^C) is defined as follows: its objects are all functors F: C → D, and for any two functors F, G: C → D, a morphism from F to G in [C, D] is a natural transformation η: F ⇒ G. **Vertical composition** is how morphisms compose in [C, D]: given η: F ⇒ G and ε: G ⇒ H, the composite (ε ∘ η): F ⇒ H is defined component-wise by (ε ∘ η)_c = ε_c ∘ η_c for each object c ∈ C. You can verify that this composite is again natural, and that composition is associative with identity natural transformations as units — all the category axioms hold.

One of the most useful reformulations in category theory is that **a diagram of shape J in C is exactly a functor J → C**. The index category J specifies the "shape" of the diagram — which nodes and arrows should appear. A functor from J to C picks out objects and morphisms in C of that shape. This means that asking whether a limit of a diagram exists is asking whether a certain functor has a terminal object in a comma category, and constructions like limits and colimits become functors on functor categories. This uniformity of language is what makes category theory so efficient.

**Presheaf categories** [C^op, Set] are particularly important. A presheaf on C is a contravariant functor from C to sets — you can think of it as assigning a "set of sections" to each object of C, with restriction maps going backward along morphisms. The Yoneda lemma (which you will study next) shows that every category C embeds fully and faithfully into its presheaf category via the Yoneda embedding c ↦ Hom(−, c): C^op → Set. This means [C^op, Set] contains a faithful copy of C, but is much richer — it always has all limits and colimits, and supports an internal logic. Presheaf categories provide models for sheaf theory, for variable sets in topos theory, and for Kripke frames in intuitionistic logic, making them one of the central constructions in modern mathematics.
