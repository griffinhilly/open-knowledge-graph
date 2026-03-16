---
id: yoneda-embedding-full-faithful
title: Yoneda Embedding and Full Faithfulness
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: yoneda-lemma
  type: hard
- id: representable-functors
  type: hard
- id: injective-surjective-bijective
  type: soft
- id: functions-and-function-properties
  type: soft
builds-toward:
- presheaves
- topos-theory-intro
tags:
- yoneda
- embedding
- representable
- presheaf
stage: advanced
status: draft
---

# Yoneda Embedding and Full Faithfulness

## Core Idea
The Yoneda embedding is the functor Y: C → [C^op, Set] sending each object X to Hom(−, X), embedding any small category into its presheaf category. This embedding is always fully faithful, meaning it is injective on morphisms and surjective when restricted to hom-sets. The Yoneda embedding allows any category to be realized as a full subcategory of set-valued functors, making presheaves the universal model for categorical structures.

## How It's Best Learned
Work through the proof that Yoneda embedding is fully faithful using the Yoneda lemma directly. Apply it to finite posets and small categories, noting which presheaves are representable and which are not. Use the embedding to transfer categorical problems to set-valued functor problems.

## Common Misconceptions
The Yoneda embedding is fully faithful but not surjective on objects—many presheaves are not representable. The embedding's usefulness comes from allowing non-representable presheaves to exist and be studied systematically. Full faithfulness means the category is determined by its morphism structure alone.

## Explainer

From the Yoneda lemma, you know that for any functor F: C^op → Set and any object X in C, natural transformations Nat(Hom(−,X), F) are in natural bijection with elements of F(X). The **Yoneda embedding** is the special case where we fix F = Hom(−,Y) for a second object Y. Plugging this in: Nat(Hom(−,X), Hom(−,Y)) ≅ Hom(Y,X)... wait, let us be careful about contravariance. The Yoneda lemma gives Nat(Hom(−,X), F) ≅ F(X), so with F = Hom(−,Y) we get Nat(Hom(−,X), Hom(−,Y)) ≅ Hom(Y, X) — no, that still isn't right. For the covariant embedding Y: C → [C^op, Set] sending X ↦ Hom(−,X), the Yoneda lemma gives Nat(Hom(−,X), Hom(−,Y)) ≅ Hom(X,Y). The bijection sends a morphism f: X → Y to the natural transformation whose component at Z is post-composition with f.

This single computation is the proof of **full faithfulness**. The embedding Y is **faithful** (injective on morphisms): if two morphisms f, g: X → Y induce the same natural transformation Hom(−,X) ⟹ Hom(−,Y), then in particular their component at X sends id_X to f and to g respectively, forcing f = g. The embedding is **full** (surjective on morphisms between representables): every natural transformation Hom(−,X) ⟹ Hom(−,Y) is post-composition with some morphism X → Y, by the Yoneda bijection above. Together: the hom-set Hom_C(X,Y) is in bijection with the hom-set Hom_{[C^op,Set]}(Y(X), Y(Y)). The functor Y does not distort morphisms at all.

The **philosophical punch line** is: an object X in C is completely determined, up to isomorphism, by the functor Hom(−,X) — that is, by the totality of how other objects map into X. Two objects with naturally isomorphic hom-functors are isomorphic. This is the categorical version of the principle "you are known by your relationships." In your prerequisite on representable functors, you saw that a functor F is representable when it is naturally isomorphic to some Hom(−,X); full faithfulness of the Yoneda embedding means representability is a property of the functor F, uniquely determined up to isomorphism of the representing object X.

The **presheaf category** [C^op, Set] is much larger than C: it contains C as a full subcategory via Y, but also all the non-representable presheaves — functors that do not arise as Hom(−,X) for any X. Think of these as "formal" or "virtual" objects that behave as if they could be in C but are not. This is analogous to the way the rational numbers embed into the reals: ℚ embeds faithfully into ℝ, but ℝ contains limits of Cauchy sequences that are not rational. The presheaf category is the **free cocompletion** of C — it adds all the colimits (formal colimits of diagrams in C) that C might be missing. Any functor from C to a cocomplete category extends uniquely along Y to a colimit-preserving functor from [C^op, Set]. This universal property is what makes the Yoneda embedding indispensable in topos theory and modern categorical logic.

A subtlety worth holding onto: Y is fully faithful but not essentially surjective (not every presheaf is representable), so it is not an equivalence of categories. The gap — the non-representable presheaves — is not a deficiency but a resource. Sheaf theory, for example, is the study of presheaves satisfying a local-gluing condition, and the objects of a Grothendieck topos are exactly the sheaves in this extended presheaf world. The Yoneda embedding is the door into this territory: it embeds the category you understand into a larger, richer world where many constructions that were impossible become routine.

