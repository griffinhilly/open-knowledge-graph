---
id: full-and-faithful-functors
title: Full and Faithful Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: injective-surjective-bijective
  type: soft
builds-toward:
- equivalence-of-categories
- representable-functors
- yoneda-lemma
tags:
- full functor
- faithful functor
- embedding
- subcategory
stage: expert
status: validated
---

# Full and Faithful Functors

## Core Idea
A functor F: C → D is faithful if it is injective on each hom-set (F(f) = F(g) implies f = g), and full if it is surjective on each hom-set (every morphism between F(A) and F(B) in D arises as F(f) for some f in C). A fully faithful functor embeds C as a subcategory of D in a strong sense: it reflects isomorphisms and allows C to be identified with its image in D. Forgetful functors are typically faithful but not full; inclusion functors of full subcategories are fully faithful.

## How It's Best Learned
Check the forgetful functor from Ab (abelian groups) to Grp: it is faithful (group homomorphisms between abelian groups are the same in both categories) but not full (not every group homomorphism between two abelian groups is an abelian group homomorphism—actually it is, so check another example). Work out when the inclusion of a subcategory is full.

## Common Misconceptions
- A fully faithful functor need not be an isomorphism of categories; it can fail to be surjective on objects.
- Faithful does not mean injective on objects; a functor can be faithful yet send different objects to the same object.

## Questions

```yaml
- question: "F: C → D is a fully faithful functor and F(f): F(A) → F(B) is an isomorphism in D. What can you conclude about f in C?"
  type: multiple-choice
  options:
    - "Nothing — F may create isomorphisms that do not exist in C"
    - "f must be an isomorphism in C, because fully faithful functors reflect isomorphisms"
    - "F must be surjective on objects, because the isomorphism must come from C"
    - "f must be an identity morphism"
  answer: 1
  explanation: "A fully faithful functor reflects isomorphisms: if F(f) is an isomorphism in D, then f was already an isomorphism in C. This follows because F is bijective on each hom-set — the inverse of F(f) must be in the image of F, so there exists g: B → A in C with F(g) = F(f)⁻¹, and faithfulness forces f and g to be inverses. Option A describes a functor that is merely full or faithful but not both. Option C confuses object-surjectivity with the reflection property."

- question: "The forgetful functor U: Grp → Set sends each group to its underlying set and each group homomorphism to the same function between sets. Which properties does U have?"
  type: multiple-choice
  options:
    - "Full but not faithful, because not every set function is a group homomorphism"
    - "Faithful but not full, because distinct group homomorphisms yield distinct set functions, but not every set function between groups is a homomorphism"
    - "Fully faithful, because it preserves all morphism information"
    - "Neither full nor faithful, because groups have more structure than sets"
  answer: 1
  explanation: "Faithful: if two group homomorphisms f, g: G → H are equal as set functions, they are equal as homomorphisms — so U is injective on hom-sets. Not full: there exist set functions between groups that are not group homomorphisms (e.g., most constant maps). Fullness would require every set function to arise from a group homomorphism, which fails. This is the prototypical example of a faithful-but-not-full functor."

- question: "A fully faithful functor F: C → D must be surjective on objects — every object in D is in the image of F."
  type: true-false
  answer: false
  explanation: "Fully faithful only describes how F behaves on morphisms between pairs of objects (bijective on each hom-set). It says nothing about whether every object in D is hit. The Yoneda embedding is fully faithful but embeds a small category into a much larger presheaf category with far more objects. The failure of surjectivity on objects is exactly why a fully faithful functor need not be an equivalence of categories."

- question: "A functor that is faithful must be injective on objects — if F(A) = F(B) then A = B."
  type: true-false
  answer: false
  explanation: "Faithful means injective on each hom-set: F(f) = F(g) implies f = g for parallel morphisms f, g: A → B. It says nothing about objects. A faithful functor can send many distinct objects to a single object in D — it just cannot confuse two morphisms between the same pair of objects. The hom-set condition and the object condition are entirely independent."

- question: "Explain the difference between a functor being 'full' and being 'faithful,' and give an example of a functor that is one but not the other."
  type: short-answer
  answer: "Faithful means the functor is injective on each hom-set: distinct morphisms f ≠ g in C(A,B) map to distinct morphisms F(f) ≠ F(g) in D(FA,FB). Full means surjective on each hom-set: every morphism in D(FA,FB) arises as F(f) for some f in C(A,B). The forgetful functor Grp → Set is faithful (same set-function implies same homomorphism) but not full (not every set function is a group homomorphism). The inclusion of a non-full subcategory is faithful but not full, because there exist morphisms between the included objects in the larger category that are absent from the subcategory."
  explanation: "A faithful functor loses no information about morphisms between given objects. A full functor has no 'extra' morphisms between images beyond what came from C. Fully faithful means D(FA,FB) and C(A,B) are in bijection for every pair A,B — making F an embedding of morphism structure, though not necessarily of objects."
```

## Explainer

Your prerequisite on functors established that a functor F: C → D must send objects to objects and morphisms to morphisms, preserving composition and identities. But functors can do this in very different ways — some collapse the structure of C, others faithfully preserve it, and others make C appear richer inside D than it actually is. The notions of **full** and **faithful** measure how a functor behaves specifically on *morphisms between pairs of objects*, not on objects themselves.

Think of each hom-set C(A, B) (the set of all morphisms from A to B) as a dataset, and F as a function that sends each morphism f: A → B in C to a morphism F(f): F(A) → F(B) in D. **Faithfulness** means this map is injective: distinct morphisms in C(A, B) produce distinct morphisms in D(F(A), F(B)). If F(f) = F(g) forces f = g, then F is not "forgetting" the distinction between morphisms. Faithful functors preserve morphism identity — they cannot confuse two different morphisms. The forgetful functor from groups to sets is faithful because group homomorphisms are particular set-functions, and if the same set-function arises from two group homomorphisms, those homomorphisms were the same to begin with.

**Fullness** is the opposite requirement: F is surjective on each hom-set. Every morphism in D(F(A), F(B)) is the image of some morphism in C(A, B). Fullness means that D does not have "extra" morphisms between the images of A and B that don't come from C. The inclusion of a **full subcategory** is the prototypical example: if you take a subcategory where you keep all morphisms between chosen objects, that inclusion functor is fully faithful. Contrast with a subcategory that restricts to some morphisms: the inclusion is then faithful but not full.

When F is both full and faithful — **fully faithful** — it embeds C into D in a strong structural sense. A fully faithful functor reflects isomorphisms: if F(f) is an isomorphism in D, then f was already an isomorphism in C. This means F cannot create or destroy isomorphisms between objects. Two objects A and B in C are isomorphic in C if and only if F(A) and F(B) are isomorphic via a morphism in the image of F. This is how category theorists make precise the idea that "the image of F looks exactly like C." It does not mean F is an equivalence of categories, because F might not be surjective on objects — D may contain objects not of the form F(A). The **Yoneda embedding** — which you will encounter next — is the canonical example of a fully faithful functor, embedding any category into its presheaf category, and understanding full-faithfulness is essential to grasping what the Yoneda lemma actually says.
