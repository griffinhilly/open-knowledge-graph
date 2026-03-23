---
id: right-adjoint-functors
title: Right Adjoint Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: natural-transformations
  type: hard
builds-toward:
- adjoint-functors
- adjunction-as-hom-bijection
- limits-and-colimits
tags:
- adjunction
- functor-pairs
- universal-properties
stage: expert
status: draft
---

# Right Adjoint Functors

## Core Idea
A functor R: D → C is a right adjoint if there exists L: C → D such that morphisms Lc → d in D correspond bijectively to morphisms c → Rd in C, naturally in both variables. Right adjoints preserve limits and characterize objects as 'universal targets' for maps from given sources. They are dual to left adjoints via opposite categories.

## Questions

```yaml
- question: "The forgetful functor U: Grp → Set sends each group to its underlying set. It is a right adjoint to the free group functor F: Set → Grp. Does U preserve products — i.e., is U(G₁ × G₂) ≅ U(G₁) × U(G₂)?"
  type: multiple-choice
  options:
    - "Not necessarily — U forgets group structure, so it might not respect the product construction"
    - "Yes — right adjoints preserve all limits, and products are limits, so U must preserve products"
    - "Yes, but only for abelian groups, where products and coproducts coincide"
    - "Whether U preserves products depends on the specific groups G₁ and G₂, not on U being a right adjoint"
  answer: 1
  explanation: "Preservation of limits is the key structural property of ALL right adjoints, not just some. Since U is a right adjoint, it preserves every limit that exists in Grp — including products, terminal objects, equalizers, and pullbacks. Concretely, the underlying set of G₁ × G₂ is indeed the cartesian product of the underlying sets, which is exactly what the theorem predicts. The 'forgetting structure' intuition is misleading — forgetful functors are often right adjoints precisely because they represent the 'remembering the structure is there' view."

- question: "For an adjunction L ⊣ R with counit ε_d: L(Rd) → d, what does the counit represent in terms of the adjunction's universal property?"
  type: multiple-choice
  options:
    - "The identity morphism on d, showing R and L are inverse equivalences"
    - "The universal morphism expressing that any map Lc → d factors uniquely through L(Rd) → d via the corresponding map c → Rd in C"
    - "The unit η of the adjunction applied to the object Rd"
    - "A natural isomorphism between L and R showing they define an equivalence of categories"
  answer: 1
  explanation: "The counit ε_d: L(Rd) → d is the 'evaluation' morphism for the right adjoint. By the hom-bijection, a map c → Rd in C corresponds to a map Lc → d in D. The counit is the specific morphism corresponding to the identity on Rd — it is the universal such map, in the sense that every Lc → d factors as Lc → L(Rd) → d where the first map comes from the unique c → Rd and the second is ε_d. This is the precise sense in which d is a 'universal target' for maps from the image of L."

- question: "If R: D → C is a right adjoint and D has products, then R preserves products: R(d₁ × d₂) ≅ R(d₁) × R(d₂) in C."
  type: true-false
  answer: true
  explanation: "Products are limits (they satisfy a universal cone property), and right adjoints preserve all limits. This is the single most important structural theorem about right adjoints. The proof follows from the limit-preservation property, which is itself a consequence of the hom-bijection: the universal property of limits in D transfers through the natural bijection to establish the universal property of the image under R in C."

- question: "To show that a right adjoint R preserves limits, one must verify each type of limit separately — products, equalizers, terminal objects, and pullbacks each require a distinct argument."
  type: true-false
  answer: false
  explanation: "The theorem that right adjoints preserve limits is a single, uniform result. Once you know R is a right adjoint, all limit preservation follows immediately — products, equalizers, terminal objects, pullbacks, and every other limit shape. No separate verification is needed for each type. This is the power of the categorical framework: a single structural fact (R is a right adjoint) implies an entire family of preservation results simultaneously."

- question: "Explain why right adjoints preserve limits. Use the duality between left and right adjoints to make the argument as concise as possible."
  type: short-answer
  answer: "A functor R is a right adjoint iff its opposite R^op: D^op → C^op is a left adjoint. Left adjoints preserve colimits. Limits in D correspond to colimits in D^op, and limits in C correspond to colimits in C^op. Since R^op (a left adjoint) sends colimits in D^op to colimits in C^op, passing back through the opposite-category correspondence shows R sends limits in D to limits in C. Right adjoint preserves limits by duality from the fact that left adjoints preserve colimits."
  explanation: "This duality argument is the cleanest proof available — it converts the right-adjoint case into the left-adjoint case for free, requiring no additional work. The slogan is: 'Left adjoints preserve colimits, right adjoints preserve limits' — and these two facts are not independent theorems but dual statements about the same underlying structure viewed from opposite categories."
```

## Explainer

To understand right adjoints, start from the adjunction hom-bijection you know: an adjunction L ⊣ R gives a natural bijection Hom_D(Lc, d) ≅ Hom_C(c, Rd) for all objects c in C and d in D. Both functors are defined by this bijection, and each one is right or left depending on which side of the hom-set it appears on. **R is the right adjoint** because it appears on the right side of Hom_C(c, Rd) — it maps into the hom-set's target. Dually, L is the left adjoint because it appears on the left side of Hom_D(Lc, d). Every adjoint pair has exactly one left adjoint and one right adjoint; neither role is more "fundamental" — they define each other.

The most important structural property of right adjoints is that they **preserve limits**. Limits are the categorical generalization of products, equalizers, terminal objects, and pullbacks — all constructions that satisfy a "universal cone" property. If D has limits of a particular shape and R: D → C is a right adjoint, then R sends those limits to limits in C. Concretely: the right adjoint functor sends a product d₁ × d₂ in D to R(d₁ × d₂) ≅ R(d₁) × R(d₂) in C. It sends terminal objects to terminal objects, and pullbacks to pullbacks. You can verify this in familiar examples: the forgetful functor from groups to sets (which is a right adjoint to the free group functor) preserves the underlying set of a product group, which is the product of the underlying sets.

A right adjoint R: D → C characterizes Rd as the **best approximation** of d within C — the "universal target" for morphisms arriving from the image of L. The unit morphism η_c: c → R(Lc) and the counit morphism ε_d: L(Rd) → d encode the adjunction's universal properties. For a right adjoint, it is the counit that is primary: ε_d: L(Rd) → d expresses that d is the "universal element" that the left adjoint maps to. Any morphism Lc → d in D factors through Lc → L(Rd) → d, with the first map determined by the unique morphism c → Rd in C. Right adjoints arise naturally when you want to "freely add structure" on the left and "remember structure" on the right.

Duality gives the cleanest way to reason about right adjoints: R is a right adjoint in category C if and only if R^op: D^op → C^op (the opposite functor) is a left adjoint. Since left adjoints preserve colimits, right adjoints preserve limits. This duality is not merely formal — it is a template for generating theorems. If you prove something about left adjoints (they preserve initial objects, they send colimits to colimits), you immediately get the dual statement about right adjoints for free, by passing to opposite categories. The most economical way to think about a specific right adjoint is to identify its left adjoint partner and read off the bijection: once you know what the left adjoint does, the right adjoint is characterized as the functor that makes the hom-bijection work.
