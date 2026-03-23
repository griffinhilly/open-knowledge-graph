---
id: equivalence-of-categories
title: Equivalence of Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: full-and-faithful-functors
  type: hard
- id: natural-transformations
  type: hard
- id: isomorphisms-in-categories
  type: soft
- id: adjunction-unit-and-counit
  type: soft
- id: equivalence-relations
  type: soft
- id: yoneda-lemma
  type: soft
- id: injective-surjective-bijective
  type: soft
- id: function-composition
  type: soft
- id: function-composition-and-inverses
  type: soft
- id: injections-surjections-bijections-classification
  type: soft
tags:
- equivalence of categories
- essentially surjective
- skeleton
- categorical equivalence
stage: expert
status: validated
---
# Equivalence of Categories

## Core Idea
Two categories C and D are equivalent if there exist functors F: C → D and G: D → C with natural isomorphisms GF ≅ Id_C and FG ≅ Id_D. Equivalence is weaker than isomorphism (which requires GF = Id_C exactly) but is the correct notion of 'sameness' for categories, since categorical properties are invariant under equivalence. A functor F: C → D is an equivalence if and only if it is full, faithful, and essentially surjective (every object of D is isomorphic to some F(C)). Skeleta, opposite categories of finite sets, and many duality theorems (Stone duality, Pontryagin duality) are equivalences.

## How It's Best Learned
Verify that the inclusion of the full subcategory of finite sets {∅, {1}, {1,2}, {1,2,3}, ...} into FinSet is an equivalence, even though it is not an isomorphism. Check full faithfulness and essential surjectivity explicitly. Then compare with the non-equivalence of Set and Grp to understand why all three conditions are necessary.

## Common Misconceptions
- Equivalent categories can look very different set-theoretically; equivalence ignores the choice of specific objects in favor of isomorphism classes.
- An equivalence does not require the functors F and G to be inverses on objects; GF(A) need only be isomorphic to A, not equal.
- Essential surjectivity alone is far from sufficient; faithfulness ensures F reflects structural distinctions and fullness ensures no morphisms are missed.

## Questions

```yaml
- question: "A functor F: C → D is an equivalence of categories if and only if it satisfies which three properties?"
  type: multiple-choice
  options: ["Full, faithful, and surjective on objects", "Full, faithful, and essentially surjective", "Injective on objects, surjective on morphisms, and faithful", "Bijective on objects and morphisms"]
  answer: 1
  explanation: "Essentially surjective means every object of D is *isomorphic* to some F(c) — not necessarily equal. Surjective on objects would be too strict (closer to isomorphism). All three conditions are necessary: faithful ensures F reflects structural distinctions, full ensures no morphisms are missed, and essentially surjective ensures every object of D is 'reached' up to isomorphism."

- question: "If two categories are equivalent, they must also be isomorphic as categories."
  type: true-false
  answer: false
  explanation: "Equivalence is strictly weaker than isomorphism. Isomorphism requires GF = Id_C and FG = Id_D exactly (functors are inverses on the nose). Equivalence only requires natural isomorphisms GF ≅ Id_C and FG ≅ Id_D, so objects may be sent to isomorphic rather than identical objects. The inclusion of a skeleton into FinSet is an equivalence but not an isomorphism."

- question: "What distinguishes 'essentially surjective' from 'surjective on objects,' and why does equivalence use the weaker condition?"
  type: short-answer
  answer: "Essentially surjective means every object d in D is isomorphic to F(c) for some c in C, while surjective on objects means every d equals F(c) for some c. Category theory treats isomorphic objects as 'the same,' so requiring exact equality would impose set-theoretic rigidity incompatible with categorical reasoning."
  explanation: "Category theory operates 'up to isomorphism' — objects are defined by their relationships to other objects, not as labeled points. Insisting on equality of objects would ignore the categorical notion of sameness. Essentially surjective captures the correct notion: if D contains an object isomorphic to something in the image of F, then categorically speaking, F 'covers' that object."
```

## Explainer

When you studied natural transformations and isomorphisms in categories, you learned that two objects in a category can be 'the same' in the categorical sense if they are isomorphic — even if they are not literally equal. Equivalence of categories extends this idea to entire categories: two categories C and D are equivalent if there exist functors F: C → D and G: D → C such that GF is naturally isomorphic to the identity on C, and FG is naturally isomorphic to the identity on D. Crucially, GF does not have to *equal* the identity — it only needs to be naturally isomorphic to it, meaning each component GF(A) ≅ A naturally and coherently.

This distinction from isomorphism of categories is profound. A true isomorphism would require GF = Id_C — going from C to D and back gives you the *same* objects and morphisms, not merely isomorphic ones. Equivalence allows F and G to reshuffle objects as long as the reshuffled objects are isomorphic to the originals. This makes equivalence the correct notion of 'sameness' for categories, since all categorical properties (limits, colimits, adjunctions) are invariant under natural isomorphism — not just under equality.

The three-condition characterization gives a practical test: a functor F: C → D is an equivalence if and only if it is (1) **full** — every morphism in D between objects in the image of F lifts back to C; (2) **faithful** — F reflects distinctions, so distinct morphisms in C remain distinct in D; and (3) **essentially surjective** — every object of D is isomorphic to some F(c). All three conditions are necessary. Faithful ensures F doesn't collapse structure; full ensures no new structure appears in D that wasn't in C; essentially surjective ensures every object of D is covered up to isomorphism.

A concrete example makes this vivid: consider the category FinSet of all finite sets and functions, and the full subcategory S consisting of exactly the sets {1}, {1,2}, {1,2,3}, ... — one representative of each finite cardinality. The inclusion S → FinSet is not surjective on objects (there are many 2-element sets, but only {1,2} is in S). But every finite set is isomorphic to exactly one representative, so the inclusion is essentially surjective. Since S is a full subcategory, the functor is also full and faithful. Therefore the inclusion is an equivalence — S and FinSet are 'the same category' categorically, even though they have very different object sets.

This is why equivalence is the standard notion used in duality theorems across mathematics. Stone duality, Pontryagin duality, and Morita equivalence are all equivalences of categories that translate between seemingly different mathematical worlds while preserving all relevant categorical structure. Recognizing an equivalence means recognizing that two areas of mathematics are, at a deep structural level, the same.
