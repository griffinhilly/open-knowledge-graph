---
id: adjoint-functors
title: Adjoint Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: natural-transformations
  type: hard
- id: universal-properties
  type: soft
- id: representable-functors
  type: soft
- id: comma-categories
  type: soft
- id: initial-and-terminal-objects
  type: soft
- id: products-and-coproducts
  type: soft
- id: pullbacks-and-pushouts
  type: soft
- id: yoneda-lemma
  type: soft
- id: group-homomorphisms
  type: soft
- id: composition-of-functions
  type: soft
- id: functions-and-function-properties
  type: hard
- id: function-composition-and-inverses
  type: soft
- id: linear-transformations
  type: soft
- id: binary-relations-definition-and-properties
  type: soft
- id: dual-spaces-bounded-functionals
  type: soft
- id: commutative-diagrams-in-categories
  type: soft
- id: left-adjoint-functors
  type: hard
- id: right-adjoint-functors
  type: hard
builds-toward:
- adjunction-unit-and-counit
- monads-in-category-theory
tags:
- adjunction
- left adjoint
- right adjoint
- hom-set bijection
- universal arrow
stage: expert
status: validated
---
# Adjoint Functors

## Core Idea
A pair of functors F: C → D and G: D → C form an adjunction (F ⊣ G, F left adjoint to G) if there is a natural bijection Hom_D(F(A), B) ≅ Hom_C(A, G(B)) for all A in C and B in D. Adjunctions are one of the most pervasive structures in mathematics: free–forgetful pairs (free group ⊣ forgetful), product–exponential pairs in Set, left Kan extensions, and many constructions in algebra and topology arise as adjunctions. Right adjoints preserve limits; left adjoints preserve colimits—a powerful tool for computing limits in many categories.

## How It's Best Learned
Verify the free-forgetful adjunction: a function from a set S to the underlying set of a group G corresponds naturally to a group homomorphism from the free group F(S) to G. Draw the natural bijection explicitly and verify naturality in both variables. Internalize the slogan: 'adjoint functors arise naturally and are ubiquitous'.

## Common Misconceptions
- Not every functor has an adjoint; existence of adjoints is a substantive condition (addressed by adjoint functor theorems).
- Left and right adjoints are not symmetric roles: the left adjoint preserves colimits while the right adjoint preserves limits.
- An adjunction is not an equivalence of categories; additional conditions (the unit and counit being isomorphisms) are required for an equivalence.

## Questions

```yaml
- question: "The hom-set bijection Hom_D(F(A), B) ≅ Hom_C(A, G(B)) must satisfy what additional condition beyond being a bijection of sets?"
  type: multiple-choice
  options: ["It must be defined only for finite categories", "It must be natural in both A and B", "It must be the identity function when A = B", "It must send identity morphisms to identity morphisms"]
  answer: 1
  explanation: "A mere bijection that varies erratically with A and B would not capture a structural relationship. Naturality means the bijection is preserved under morphisms in both variables — this coherence is what makes the adjunction a structural fact about the categories rather than an accidental correspondence."

- question: "If F ⊣ G is an adjunction (F left adjoint to G), then F and G together form an equivalence of categories."
  type: true-false
  answer: false
  explanation: "An equivalence requires both the unit η: 1_C → GF and counit ε: FG → 1_D to be natural isomorphisms. An adjunction only requires them to satisfy the triangle identities without being isomorphisms. Many important adjunctions (e.g., free group ⊣ forgetful) are not equivalences."

- question: "In what sense does the free–forgetful adjunction between Set and Grp illustrate the hom-set bijection?"
  type: short-answer
  answer: "A function from a set S to the underlying set U(G) of a group G corresponds naturally to a group homomorphism from the free group F(S) to G; this bijection Hom_Grp(F(S), G) ≅ Hom_Set(S, U(G)) is natural in both S and G."
  explanation: "The free group construction provides exactly the structure needed to uniquely extend any set-function to a group homomorphism. This is the hom-set bijection in action: morphisms out of the free object on the left correspond perfectly to structure-preserving maps on the right."
```

## Explainer

Adjoint functors are one of the grand organizing principles of mathematics — once you see them, you find them everywhere. The central idea is that two functors F: C → D and G: D → C are "adjoint" if there is a natural way to translate maps in one category into maps in the other. Precisely, F is left adjoint to G (written F ⊣ G) when there is a natural bijection: a morphism F(A) → B in D corresponds perfectly to a morphism A → G(B) in C. The hom-set formulation is Hom_D(F(A), B) ≅ Hom_C(A, G(B)), natural in both A and B.

The word "natural" is doing essential work. It means the bijection is not just a coincidence for one pair of objects but persists coherently as A and B vary — it is a natural isomorphism of functors Hom_D(F(−), −) ≅ Hom_C(−, G(−)). This is the same naturality you studied with natural transformations, now applied to hom-sets rather than individual objects.

The free–forgetful adjunction makes this concrete. The forgetful functor G: Grp → Set "forgets" the group structure, viewing a group as a plain set. Its left adjoint F: Set → Grp builds the free group on any set of generators. The bijection says: any function from a generating set S to any group G extends uniquely to a group homomorphism from the free group F(S) to G. You specify where the generators go, and the rest is forced by the group axioms. This is the universal property of the free group, and universal properties almost always arise as adjunctions.

From your study of natural transformations, you know functors can be compared via maps between them. Adjoints go further: they describe pairs of functors that are "inverses" in a weak, one-sided sense. The unit η: 1_C → GF and counit ε: FG → 1_D are natural transformations satisfying the triangle identities — they capture how close FG and GF come to being identities. An equivalence of categories is the special case where both are natural isomorphisms; an adjunction is the weaker but far more ubiquitous situation.

One of the most powerful consequences: right adjoints preserve limits; left adjoints preserve colimits. If you can prove that G is a right adjoint, it automatically preserves products, equalizers, and pullbacks — without checking each separately. Similarly, left adjoints preserve coproducts, coequalizers, and pushouts. This single theorem justifies much of the theoretical interest in adjunctions: establishing that a functor is an adjoint immediately yields an entire list of preservation results for free.
