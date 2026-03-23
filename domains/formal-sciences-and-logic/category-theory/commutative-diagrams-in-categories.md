---
id: commutative-diagrams-in-categories
title: Commutative Diagrams in Category Theory
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: soft
builds-toward:
- natural-transformations
- adjoint-functors
tags:
- diagrams
- commutative
- morphisms
- composition
stage: expert
status: draft
---

# Commutative Diagrams in Category Theory

## Core Idea
A commutative diagram is a visual representation of morphism compositions where different paths between objects yield identical morphisms. Commutative diagrams serve as both rigorous notation and pedagogical tools for expressing categorical properties and proofs. They are essential for verifying the consistency of constructions involving multiple objects and morphisms, especially when proving universal properties and naturality conditions.

## How It's Best Learned
Begin with simple two or three-object diagrams, computing compositions along different paths to verify commutativity. Practice translating categorical statements (adjunctions, natural transformations) into diagram form, then verifying each required commutativity directly.

## Common Misconceptions
Commutativity requires paths to compose identically, not merely to yield isomorphic objects. Not every diagram should commute—commutativity must be explicitly required or proven. A diagram being drawable does not imply the relationships depicted are satisfied.

## Questions

```yaml
- question: "A category has objects A, B, C, D and morphisms f: A → B, g: B → D, h: A → C, k: C → D. It is known that g ∘ f ≅ k ∘ h — the two compositions are isomorphic as objects of a functor category, but not equal as morphisms. Does the square commute?"
  type: multiple-choice
  options:
    - "Yes, because the two paths yield isomorphic objects, which is sufficient for commutativity in any reasonable category"
    - "No, commutativity of a diagram requires the two compositions to be equal as morphisms in the hom-set, not merely isomorphic"
    - "Yes, because isomorphic morphisms are equal in any skeletal category, and every category is equivalent to a skeletal one"
    - "No, but the diagram is still considered homotopy-commutative, which is sufficient for most categorical purposes"
  answer: 1
  explanation: "Commutativity is a strict equality condition: g ∘ f = k ∘ h must hold as morphisms in the hom-set Hom(A, D). Isomorphism is weaker — it says there exists an invertible morphism between the two results, but does not say the morphisms themselves are the same arrow. Relaxing to isomorphism requires specifying the isomorphism, tracking coherence conditions between multiple such isomorphisms, and verifying compatibility — this is the subject of higher category theory (2-categories, ∞-categories). Classical commutative diagram arguments depend on strict equality; the power of the notation comes precisely from this strictness."

- question: "What does it mean for a functor F: C → D to 'preserve composition'?"
  type: multiple-choice
  options:
    - "F assigns to each object of C an object of D, and to each morphism a morphism of the same type"
    - "For every morphism f in C, F(f) has the same domain and codomain as f in the same category"
    - "Every commutative diagram in C is sent to a commutative diagram in D — that is, F(g ∘ f) = F(g) ∘ F(f)"
    - "F is injective on hom-sets, so distinct morphisms in C map to distinct morphisms in D"
  answer: 2
  explanation: "Functoriality requires two things: F(id_A) = id_{F(A)} (identity preservation) and F(g ∘ f) = F(g) ∘ F(f) (composition preservation). The composition law says exactly that if a triangle or square commutes in C — if two paths compose to the same morphism — then their images under F also compose to the same morphism in D. In diagram language: every commutative diagram in C maps to a commutative diagram in D. This is the precise meaning of 'F respects the structure of C.'"

- question: "A diagram drawn with objects as vertices and morphisms as arrows automatically commutes, because drawing it implies the depicted relationships are satisfied."
  type: true-false
  answer: false
  explanation: "This is one of the most common misconceptions in category theory. Drawing a diagram only requires that morphisms exist with the depicted domains and codomains — it makes no assertion about commutativity. Commutativity is an additional equality condition on the compositions, which must be separately proven or explicitly stipulated. An author might draw a diagram to illustrate the objects and morphisms involved in a construction, then separately state 'and this diagram commutes' as a theorem to be proven. If diagrams automatically commuted by virtue of being drawn, there would be nothing to prove."

- question: "The naturality condition for a natural transformation η: F ⇒ G requires, for every morphism f: A → B in the source category, that a specific square involving η_A, η_B, F(f), and G(f) commutes."
  type: true-false
  answer: true
  explanation: "The naturality square for f: A → B states: η_B ∘ F(f) = G(f) ∘ η_A. This must hold for every morphism f in the source category C, not just for objects. The square has corners F(A), F(B), G(A), G(B), with F(f) and G(f) as horizontal edges and η_A, η_B as vertical edges. A natural transformation is not just a family of morphisms indexed by objects — it is a family of morphisms that makes all these squares commute. Commutativity of the naturality squares is exactly what 'natural' means."

- question: "Explain why the distinction between 'isomorphic' and 'equal' is crucial for the definition of commutativity in a diagram."
  type: short-answer
  answer: "Commutativity requires that two different paths of composition yield the same morphism — exact equality in the hom-set, not merely an isomorphism between the results. If the condition were relaxed to isomorphism, we would need to specify the isomorphism itself (adding extra data), verify that multiple such isomorphisms cohere with each other (coherence conditions), and ensure these isomorphisms are compatible with composition (further axioms). The strictness of equality is what makes commutative diagrams a clean, self-contained notation: you simply verify that composing morphisms along different paths gives the identical arrow, with no auxiliary data, no coherence obligations, and no additional proof burden."
  explanation: "Higher category theory (2-categories, ∞-categories) does relax commutativity to 'commutes up to a specified isomorphism,' which is the correct setting for homotopy theory and derived algebraic geometry. But this requires a substantially richer framework. Classical category theory works with strict equality, and the power of commutative diagram arguments — their transferability between algebra, topology, and logic — rests on this strictness."
```

## Explainer

From your study of categories and morphisms, you know that a category consists of objects and arrows (morphisms), with composition defined when arrows connect sequentially. Commutative diagrams are the natural language for expressing that two different sequences of compositions produce the same result — and they are to category theory what equations are to algebra: a way to assert an equality visually.

The simplest commutative diagram is a **triangle**: objects A, B, C and morphisms f: A → B, g: B → C, and h: A → C. The diagram commutes if g ∘ f = h — following the two-step path via B gives the same morphism as taking the direct path h. You can verify this by checking the equation, but drawing it as a diagram makes the structure immediately visible and scales gracefully as the number of objects grows. A **square** with corners A, B, C, D and arrows f: A → B, g: B → D, h: A → C, k: C → D commutes when g ∘ f = k ∘ h — both paths from A to D agree.

The real power emerges with functors. A functor F: C → D must send every commutative diagram in C to a commutative diagram in D — this is the precise meaning of "F preserves composition." A **natural transformation** η: F ⇒ G between functors is exactly the data that makes a family of squares commute: for every morphism f: A → B in C, the square with corners F(A), F(B), G(A), G(B) and edges F(f), G(f), η_A, η_B must commute. The condition η_B ∘ F(f) = G(f) ∘ η_A is the **naturality square**. Without commutative diagram notation, this condition would require several lines of prose to state clearly.

Commutative diagrams also encode **universal properties**. The product A × B in a category is defined by: there exists a unique morphism from any object C into A × B making a certain triangle commute. The pushout of two morphisms is the object making a certain square commute universally. Recognizing these patterns — which diagram shape corresponds to which universal property — is what lets you transfer theorems between algebra, topology, and logic. Once you prove that a result holds for any category containing a commuting triangle of a particular shape, it applies everywhere that shape appears.
