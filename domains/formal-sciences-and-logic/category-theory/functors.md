---
id: functors
title: Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: composition-of-functions
  type: soft
- id: functions-and-function-properties
  type: soft
- id: function-composition
  type: hard
- id: functions-and-mappings-formal
  type: soft
- id: composition-of-functions-sets
  type: soft
builds-toward:
- natural-transformations
- functor-categories
- representable-functors
- full-and-faithful-functors
tags:
- functors
- structure-preserving maps
- covariant
- contravariant
stage: advanced
status: validated
---

# Functors

## Core Idea
A functor F: C → D between categories assigns to each object A in C an object F(A) in D, and to each morphism f: A → B a morphism F(f): F(A) → F(B), preserving composition and identities: F(g∘f) = F(g)∘F(f) and F(id_A) = id_{F(A)}. Functors are the morphisms of the category of categories; they include familiar constructions like the forgetful functor from Grp to Set, the free group functor, and the fundamental group functor in topology. A contravariant functor reverses the direction of morphisms and can be viewed as a covariant functor from C^op.

## How It's Best Learned
Work through at least three concrete functors: the forgetful functor from groups to sets, the power set functor on Set, and the hom-functor Hom(A, -). Verify functoriality axioms explicitly for each. Then identify where contravariance arises naturally (e.g., Hom(-, B) reverses arrows).

## Common Misconceptions
- Functors need not be injective or surjective on objects or morphisms; they can collapse structure.
- A contravariant functor is not a functor 'going backward'—it is a covariant functor from the opposite category.
- Functors do not require the categories to have the same size or type.

## Questions

```yaml
- question: "The forgetful functor U: Grp → Set sends each group (G, ·) to its underlying set G and each group homomorphism to the same function. Which functor law does this illustrate most directly?"
  type: multiple-choice
  options: ["It reverses the direction of morphisms, showing contravariance", "It sends identity morphisms to identity morphisms and preserves composition, satisfying the functoriality axioms", "It creates new morphisms in Set that did not exist in Grp", "It requires the groups to be isomorphic to their image sets"]
  answer: 1
  explanation: "The forgetful functor preserves the two defining laws: F(id_G) = id_{U(G)} (identities go to identities) and U(h∘g) = U(h)∘U(g) (composition is preserved). It 'forgets' the group structure but does not alter the morphisms themselves — a homomorphism is also a function, so no new morphisms are created. The functor is covariant (arrows go in the same direction), not contravariant."

- question: "A contravariant functor from C to D is the same as a covariant functor from C to D^op, where D^op is D with most morphisms reversed."
  type: true-false
  answer: false
  explanation: "Almost — but the direction is slightly off. A contravariant functor F: C → D is equivalently described as a covariant functor F: C^op → D (from the opposite of C to D), or equivalently C → D^op. The key point is that contravariance means arrows in C get reversed when mapped into D, which is captured by saying F is covariant on the opposite category C^op. This reframing allows all general theorems about covariant functors to apply automatically to contravariant ones."

- question: "What distinguishes a functor from a mere object-level mapping between categories — that is, what additional structure must a functor preserve?"
  type: short-answer
  answer: "A functor must also act on morphisms: for every morphism f: A → B in C, it must produce a morphism F(f): F(A) → F(B) in D. Moreover, it must preserve composition (F(g∘f) = F(g)∘F(f)) and identity morphisms (F(id_A) = id_{F(A)})."
  explanation: "A mapping that only assigns objects to objects ignores the relational structure that makes a category meaningful — the morphisms. Functoriality laws ensure the mapping is coherent with the categorical structure: it respects how morphisms compose and how identity morphisms behave. Without these laws, the mapping would be a function between the object-classes of two categories but would carry no structural information."
```

## Explainer

In category theory, you have seen that a category consists of objects, morphisms between them, composition of morphisms, and identity morphisms — and that all of the interesting information lives in the morphisms, not just in the objects. A functor is the natural notion of a structure-preserving map between categories: it translates one category into another in a way that respects all of this structure.

Formally, a functor F: C → D has two components. First, an object map: for every object A in C, it assigns an object F(A) in D. Second, a morphism map: for every morphism f: A → B in C, it assigns a morphism F(f): F(A) → F(B) in D. These two components must satisfy the functoriality axioms: F preserves composition, meaning F(g∘f) = F(g)∘F(f), and F preserves identities, meaning F(id_A) = id_{F(A)}. If either axiom fails, the map is not a functor — it does not respect categorical structure.

The forgetful functor U: Grp → Set is the most accessible example. It sends each group (G, ·) to its underlying set G, forgetting the multiplication structure. Each group homomorphism h: G → H is already a function between sets, so U(h) = h as a bare function. Composition and identities are preserved trivially. The power set functor P: Set → Set is another example: it sends each set X to its power set P(X), and each function f: X → Y to the function P(f): P(X) → P(Y) defined by P(f)(S) = {f(s) | s ∈ S}. Checking functoriality here requires a small calculation worth doing.

Contravariant functors arise when the morphism map reverses arrows: F sends f: A → B to F(f): F(B) → F(A). The most important example is the contravariant hom-functor Hom(-, B): C^op → Set, which sends each object A to the set of morphisms Hom(A, B) and each morphism f: A → A' to the pre-composition function f*: Hom(A', B) → Hom(A, B). This reversal is not an anomaly but a fundamental feature: contravariant functors appear naturally whenever you are mapping into a target rather than out of it. The clean way to handle them is to note that a contravariant functor C → D is the same as a covariant functor C^op → D, so all theorems about covariant functors apply.

Functors are not merely curiosities — they are the morphisms of the category Cat (the category of all small categories), so they allow you to reason about categories as objects in their own right. More concretely, every major construction in mathematics that maps between mathematical structures and does so coherently — fundamental groups in topology, homology groups in algebraic topology, free constructions in algebra — is a functor. The discipline of checking that a construction is actually functorial (rather than just defined on objects) is what forces mathematical precision and reveals hidden structure. Natural transformations, which you will study next, are the morphisms between functors, and together they give you the tools to compare mathematical structures at a level of abstraction that pays off across all of modern mathematics.
