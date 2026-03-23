---
id: presheaves
title: Presheaves
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: yoneda-lemma
  type: hard
- id: functor-categories
  type: hard
- id: opposite-categories-and-duality
  type: soft
- id: set-operations
  type: soft
- id: indexed-families-of-sets
  type: soft
builds-toward:
- sheaves-and-sheafification
- topos-theory-intro
tags:
- presheaf
- functor category
- representable presheaf
- Yoneda embedding
- Set-valued functor
stage: expert
status: validated
---
# Presheaves

## Core Idea
A presheaf on a category C is a functor F: C^op → Set. The category of presheaves [C^op, Set] is a fundamental construction: it is complete, cocomplete, and cartesian closed, making it a topos. Every object A of C determines a representable presheaf Hom(−, A), and the Yoneda embedding y: C → [C^op, Set] sending A to Hom(−, A) is full and faithful, so C embeds as a full subcategory of its presheaf category. The presheaf category can be thought of as the free cocompletion of C—it freely adds all colimits.

## How It's Best Learned
Take a small concrete category such as a poset (P, ≤) and write out several presheaves as contravariant functors to Set. Compute the representable presheaves and verify that the Yoneda embedding is injective on objects and morphisms. Then explore a non-representable presheaf and understand why it cannot arise as Hom(−, A) for any A.

## Common Misconceptions
- A presheaf is a functor from C^op to Set, not from C to Set; the contravariance is essential and reflects the restriction maps in geometric examples.
- Not every presheaf is representable; representability is a strong condition equivalent to the presheaf preserving all limits that exist in C.
- The presheaf category [C^op, Set] is not the same as the functor category [C, Set]; the two are related by the opposite category construction.

## Questions

```yaml
- question: "In the category Open(X) of open sets of a topological space, with morphisms being inclusions U ↪ V whenever U ⊆ V, a presheaf F assigns data to each open set. When U ⊆ V, what map does F provide between F(U) and F(V)?"
  type: multiple-choice
  options:
    - "A map F(U) → F(V), sending local data on U to global data on V"
    - "A map F(V) → F(U), restricting data defined on the larger set V to the smaller set U"
    - "A bijection between F(U) and F(V), since they contain the same data up to restriction"
    - "No map between them, since U and V are not directly comparable in C^op"
  answer: 1
  explanation: "A presheaf is a contravariant functor F: C^op → Set. In C = Open(X), a morphism U ↪ V (inclusion) becomes a morphism V → U in C^op (morphisms reverse). The functor F sends this to a map F(V) → F(U) — a restriction map from larger sets to smaller sets. This is the direction data actually flows: a function defined on all of V can be restricted to the subset U, but not conversely. The contravariance of the functor exactly captures this restriction direction. Option A gets the direction backwards and would describe a covariant functor (a 'copresheaf')."

- question: "Which statement best describes the relationship between representable presheaves and all presheaves on a category C?"
  type: multiple-choice
  options:
    - "Every presheaf on C is representable — all presheaves arise as Hom(−, A) for some object A ∈ C"
    - "No presheaf is representable unless C is a small complete category"
    - "The representable presheaves Hom(−, A) correspond to objects of C, but many presheaves exist that encode 'generalized objects' with no representative in C itself"
    - "Representable presheaves only exist when the category C has a terminal object"
  answer: 2
  explanation: "The Yoneda embedding shows that every object A ∈ C gives a representable presheaf Hom(−, A), and these are faithfully encoded in [C^op, Set]. But the presheaf category contains far more: non-representable presheaves exist that do not arise from any single object of C. These encode 'generalized objects' — for instance, in algebraic geometry, moduli problems that have no representing scheme still define perfectly good presheaves. Non-representability is not a deficiency but a feature: it means the presheaf category freely extends C with all the 'formal colimits' that C might be missing."

- question: "The Yoneda embedding y: C → [C^op, Set], which sends each object A to the representable presheaf Hom(−, A), is full and faithful — meaning C embeds as a full subcategory of its presheaf category."
  type: true-false
  answer: true
  explanation: "Fullness means every natural transformation between representable presheaves Hom(−, A) → Hom(−, B) arises from a unique morphism A → B in C. Faithfulness means distinct morphisms in C give distinct natural transformations. Together, they say that the embedding y: C → [C^op, Set] is injective on both objects and morphisms — C sits inside its presheaf category without distortion. This is the Yoneda lemma's payoff: an object is completely determined by the maps into it, so we can replace the object with its 'generalized points' functor without losing information."

- question: "The presheaf category [C^op, Set] and the functor category [C, Set] are the same category — the notational difference is purely conventional."
  type: true-false
  answer: false
  explanation: "These are genuinely distinct categories. [C^op, Set] consists of contravariant functors from C to Set (equivalently, covariant functors from C^op to Set), while [C, Set] consists of covariant functors from C to Set. The two categories are related by the opposite category construction: [C^op, Set] ≅ [C, Set]^op as categories (roughly). In the geometric setting, presheaves on Open(X) assign data that restricts to smaller open sets; covariant functors would assign data that extends to larger sets (a very different structure). The distinction is not notational — it reflects a fundamental difference in the direction of the data flow."

- question: "What does it mean to say that the presheaf category [C^op, Set] is the 'free cocompletion' of C, and why is this a useful way to think about presheaves?"
  type: short-answer
  answer: "Free cocompletion means that [C^op, Set] is the universal way to add all small colimits to C. More precisely: given any functor F: C → D where D is cocomplete (has all small colimits), there exists a unique (up to unique natural isomorphism) colimit-preserving extension F̃: [C^op, Set] → D through the Yoneda embedding y: C → [C^op, Set], so that F̃ ∘ y ≅ F. In other words, presheaves are the 'formal colimits' you get by freely adjoining all colimits to C. This is useful because it means any cocomplete target category can receive a unique colimit-preserving functor from the presheaf category, making [C^op, Set] the universal cocomplete extension of C."
  explanation: "The practical implication: if you want to build colimits out of objects of C (formal quotients, pushouts, filtered colimits), you can work in [C^op, Set] where all colimits exist, do your construction there, and then ask whether the result is representable (i.e., lies in the image of C under Yoneda). This is exactly the strategy used in algebraic geometry when constructing moduli spaces and algebraic spaces."
```

## Explainer

The Yoneda lemma you've already mastered tells you that each object A in a category C determines a contravariant functor Hom(−, A): C^op → Set, sending each object X to the set of morphisms X → A, and sending each morphism f: X → Y to the precomposition map (− ∘ f): Hom(Y, A) → Hom(X, A). The Yoneda embedding y: C → [C^op, Set] shows that this assignment is full and faithful — so C embeds into a larger category whose objects are *all* contravariant functors from C to Set. A **presheaf** on C is simply any such functor: F: C^op → Set. The presheaves include the representable ones (Hom(−, A) for each A) but also many others that don't correspond to any single object of C.

The geometric motivation makes the contravariance feel natural. Take C to be the category **Open(X)** of open sets of a topological space X, with morphisms being inclusions U ↪ V whenever U ⊆ V. A presheaf F on this category assigns a set F(U) to each open set U — think of it as "local data over U" (functions, sections, observations). When U ⊆ V, the morphism V → U in C^op (remember, morphisms reverse in the opposite category) corresponds to a **restriction map** F(V) → F(U): data defined on a larger open set can be restricted to a smaller one. This is exactly the covariant direction for data flow — data restricts to smaller sets, which is why the functor must be contravariant on the original category. Every presheaf you encounter in geometry, topology, or algebra has this restriction-map flavor.

The presheaf category [C^op, Set] has remarkable categorical properties: it has all small limits and colimits (computed pointwise), it is cartesian closed (you can form "function presheaves"), and it is a **topos** — a category with enough structure to do logic and set theory internally. None of this requires C itself to be well-behaved; the presheaf construction freely adds whatever C lacks. The slogan is that [C^op, Set] is the **free cocompletion** of C: every functor from C into a cocomplete category extends uniquely (up to unique natural isomorphism) through the Yoneda embedding. This makes presheaves the universal device for "adding formal colimits" to C.

Not all presheaves are representable, and this non-representability is important rather than a deficiency. A representable presheaf Hom(−, A) knows exactly where every morphism in C points; a non-representable presheaf can encode "generalized objects" that C doesn't contain. In algebraic geometry, for instance, moduli problems (classify all curves of genus g, all elliptic curves with a level structure) often have no representing object in the category of schemes, but they do define perfectly good presheaves — and the project of sheafification and algebraic spaces is essentially about deciding which of these presheaves are "geometric enough" to count as spaces. Understanding presheaves is thus the entry point not just to sheaf theory but to the modern approach to geometry where spaces are defined by what you can map *into* them.

