---
id: two-categories
title: 2-Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: natural-transformations
  type: hard
- id: functor-categories
  type: hard
- id: categories-and-morphisms
  type: soft
builds-toward:
- fibered-categories
tags:
- 2-category
- 2-morphism
- horizontal composition
- vertical composition
- interchange law
- Cat
- bicategory
stage: expert
status: validated
---
# 2-Categories

## Core Idea
A 2-category is a category enriched over Cat: it has objects (0-cells), morphisms between objects (1-cells), and morphisms between morphisms (2-cells or 2-morphisms). The 2-cells can be composed in two ways: vertically (composing 2-cells along shared 1-cells, like composing natural transformations) and horizontally (composing 2-cells along shared 0-cells, like whiskering). These two compositions must satisfy the interchange law. The primary example is Cat itself, where objects are categories, 1-cells are functors, and 2-cells are natural transformations. Strict 2-categories require associativity and unit laws to hold on the nose; the weaker notion of bicategory allows them to hold only up to coherent isomorphism.

## How It's Best Learned
Take Cat as the running example. Identify the 0-cells (small categories), 1-cells (functors), and 2-cells (natural transformations). Practice vertical composition (composing two natural transformations α: F ⇒ G and β: G ⇒ H) and horizontal composition (whiskering a natural transformation with a functor). Verify the interchange law on a concrete example. Then consider the bicategory of spans as a non-strict example.

## Common Misconceptions
- A 2-category is not the same as a double category; 2-categories have one type of 1-cell, while double categories have two (horizontal and vertical).
- Strict and weak (bi)categories are genuinely different notions; not every bicategory is equivalent to a strict 2-category in the naive sense, though the coherence theorem for bicategories provides a strictification result.
- The interchange law is not a consequence of the other axioms; it is an independent condition that constrains how vertical and horizontal composition interact.

## Questions

```yaml
- question: "A student studying 2-categories argues: 'Once I have defined vertical and horizontal composition and verified that each is independently associative, the interchange law must automatically hold.' Why is this reasoning incorrect?"
  type: multiple-choice
  options:
    - "The interchange law is automatic only for strict 2-categories; in bicategories it is replaced by the coherence theorem"
    - "The interchange law constrains how vertical and horizontal composition interact with each other — this interaction is not implied by each composition being individually associative; it is a separate, independent condition"
    - "The student is correct in Cat specifically, because the interchange law follows from naturality of composition there"
    - "Associativity is sufficient for the interchange law only when the 2-category has a single 0-cell"
  answer: 1
  explanation: "Associativity of vertical composition says (γ ∘ β) ∘ α = γ ∘ (β ∘ α) for 2-cells stacked along shared 1-cells. Associativity of horizontal composition says (γ ★ β) ★ α = γ ★ (β ★ α) for 2-cells arranged side by side. Neither says anything about mixing the two operations. The interchange law (β₂ ∘ β₁) ★ (α₂ ∘ α₁) = (β₂ ★ α₂) ∘ (β₁ ★ α₁) is an additional axiom that must be verified separately — it asserts that combining four 2-cells in a 2×2 grid gives the same result regardless of whether you compose rows first or columns first."

- question: "In the 2-category Cat, which of the following is a 2-cell (2-morphism)?"
  type: multiple-choice
  options:
    - "A small category C"
    - "A functor F: C → D between two categories"
    - "A natural transformation α: F ⇒ G between two functors with the same source and target categories"
    - "An adjunction L ⊣ R between two categories"
  answer: 2
  explanation: "In Cat, the three levels are: 0-cells are small categories, 1-cells are functors between categories, and 2-cells are natural transformations between functors with the same source and target. A natural transformation α: F ⇒ G assigns to each object X of C a morphism α_X: F(X) → G(X) in D, satisfying a naturality square. This is exactly the morphism-between-morphisms structure that defines 2-cells. Adjunctions involve more data than a single natural transformation and are not themselves 2-cells in this sense, though they can be characterized using 2-categorical structure."

- question: "A 2-category is equivalent to a double category because both structures have objects, morphisms between objects, and morphisms between morphisms."
  type: true-false
  answer: false
  explanation: "A 2-category has one kind of 1-cell (morphism between objects), and 2-cells are morphisms between those 1-cells. A double category has two distinct kinds of 1-cells — horizontal morphisms and vertical morphisms — which can compose independently, plus 2-cells that are squares with all four boundary types. The structures are genuinely different: Cat is naturally a 2-category, while the category of spans or of rings with bimodules is naturally a double category. The distinction matters for applications in topology, algebra, and theoretical computer science."

- question: "In a strict 2-category, the interchange law must be explicitly imposed as an independent axiom, not derived from the associativity and unit laws for 1-cell and 2-cell composition."
  type: true-false
  answer: true
  explanation: "The axioms of a strict 2-category include: (i) associativity and units for 1-cell composition, (ii) associativity and units for vertical composition of 2-cells (making each Hom(A, B) a category), and (iii) the interchange law relating vertical and horizontal composition. Each is independent. In Cat, the interchange law can be verified from the definition of horizontal composition (whiskering) and naturality — but this verification shows it holds in Cat, not that it follows from the abstract axioms. An abstract 2-category that violates the interchange law would be internally inconsistent."

- question: "Explain in your own words what the interchange law requires and why it cannot be derived from the other axioms of a 2-category."
  type: short-answer
  answer: "The interchange law says that composing four 2-cells arranged in a 2×2 grid gives the same answer regardless of order: (β₂ ∘ β₁) ★ (α₂ ∘ α₁) = (β₂ ★ α₂) ∘ (β₁ ★ α₁). You can either compose rows first (two vertical composites) then compose those horizontally, or compose columns first (two horizontal composites) then compose those vertically — the result must agree. This is a coherence condition between two independent composition operations. It cannot be derived from the other axioms because those axioms govern each composition operation in isolation, saying nothing about how they interact when applied in succession."
  explanation: "The interchange law is analogous to the exchange rule in logic or the Eckmann-Hilton argument in higher algebra: when two binary operations interact on the same set of elements, their interaction must be constrained for the structure to be well-behaved. In Cat, you can verify the interchange law explicitly using the definition of whiskering and naturality squares. In an abstract 2-category, there is no such reduction — it must stand as an axiom. Violation would mean the order of applying vertical then horizontal (or vice versa) composition produces different 2-cells, making the structure incoherent."
```

## Explainer

An ordinary category has objects and morphisms between objects. A **2-category** adds a third level: morphisms between morphisms, called **2-cells** or **2-morphisms**. You already know the paradigmatic example from your prerequisites: in the functor category [C, D], objects are functors and morphisms are natural transformations. A 2-category makes this structure explicit and formalizes two independent ways of composing 2-cells that coexist in [C, D] and in Cat itself.

Take **Cat** as the running example throughout. Its **0-cells** (objects) are small categories, its **1-cells** (morphisms between objects) are functors F: C → D, and its **2-cells** (morphisms between 1-cells) are natural transformations α: F ⇒ G between functors with the same source and target. **Vertical composition** of 2-cells stacks them end-to-end along a shared 1-cell: if α: F ⇒ G and β: G ⇒ H are natural transformations between the same two categories, their vertical composite β ∘ α: F ⇒ H is the natural transformation whose component at each object X is β_X ∘ α_X. This is exactly the composition you know from functor categories. Each hom-category Hom(C, D) is itself a category (with natural transformations as morphisms), and vertical composition is the composition in that category.

**Horizontal composition** combines 2-cells side by side across different hom-categories. If α: F ⇒ G is a natural transformation between functors C → D, and β: H ⇒ K is a natural transformation between functors D → E, the horizontal composite β ★ α: H∘F ⇒ K∘G is a natural transformation between functors C → E. In Cat, this is **whiskering**: (β ★ α)_X = β_{GX} ∘ H(α_X) = K(α_X) ∘ β_{FX} (these are equal by naturality of β). The identity 2-cell for horizontal composition on a functor F is the identity natural transformation id_F.

The **interchange law** (β₂ ∘ β₁) ★ (α₂ ∘ α₁) = (β₂ ★ α₂) ∘ (β₁ ★ α₁) says that composing vertically then horizontally gives the same result as composing horizontally then vertically. Visually: arrange four 2-cells in a 2×2 grid; you can compose the rows first (two vertical composites) then compose the results horizontally — or compose the columns first (two horizontal composites) then compose vertically — and the answer must agree. In Cat, this follows from naturality, but as an axiom in an abstract 2-category it is an independent condition that must be verified.

The **strict vs. weak** distinction becomes significant when you move beyond Cat. In a strict 2-category, all associativity and unit laws for 1-cell composition hold on the nose as equalities. In a **bicategory**, they hold only up to specified 2-cell isomorphisms (associators and unitors) satisfying coherence conditions analogous to Mac Lane's pentagon and triangle identities for monoidal categories. The category of spans in a category with pullbacks, profunctors between categories, and cobordisms between manifolds are all naturally bicategories. The coherence theorem guarantees every bicategory is equivalent (as a bicategory) to a strict 2-category, so you can often "strictify" for computational purposes — but the natural presentation of many important examples is inherently weak.
