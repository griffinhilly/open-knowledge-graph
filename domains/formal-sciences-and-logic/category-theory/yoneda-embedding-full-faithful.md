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
- id: hom-functors-and-representability
  type: hard
- id: natural-isomorphisms-universality
  type: hard
builds-toward:
- presheaves
- topos-theory-intro
tags:
- yoneda
- embedding
- representable
- presheaf
stage: expert
status: validated
---

# Yoneda Embedding and Full Faithfulness

## Core Idea
The Yoneda embedding is the functor Y: C → [C^op, Set] sending each object X to Hom(−, X), embedding any small category into its presheaf category. This embedding is always fully faithful, meaning it is injective on morphisms and surjective when restricted to hom-sets. The Yoneda embedding allows any category to be realized as a full subcategory of set-valued functors, making presheaves the universal model for categorical structures.

## How It's Best Learned
Work through the proof that Yoneda embedding is fully faithful using the Yoneda lemma directly. Apply it to finite posets and small categories, noting which presheaves are representable and which are not. Use the embedding to transfer categorical problems to set-valued functor problems.

## Common Misconceptions
The Yoneda embedding is fully faithful but not surjective on objects—many presheaves are not representable. The embedding's usefulness comes from allowing non-representable presheaves to exist and be studied systematically. Full faithfulness means the category is determined by its morphism structure alone.

## Questions

```yaml
- question: "A student argues: 'Since the Yoneda embedding is fully faithful, every presheaf F: C^op → Set must be naturally isomorphic to Hom(−, X) for some object X in C.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Full faithfulness does imply that every presheaf is representable — the student is correct"
    - "Full faithfulness means the embedding preserves and reflects morphisms between representables, but says nothing about presheaves outside the image of Y — many presheaves are non-representable"
    - "The error is that Hom(−, X) is a covariant functor, but presheaves are required to be contravariant"
    - "Full faithfulness only holds when C is a small category; the claim fails in general"
  answer: 1
  explanation: "Full faithfulness is a property about morphisms: the embedding is injective on morphisms (faithful) and surjective on morphisms between objects in its image (full). It says nothing about whether every presheaf is in the image of Y at all — that would be essential surjectivity. Many presheaves are non-representable (e.g., in the category of sets, the presheaf sending every set to the empty set unless the set is empty is not representable). The non-representable presheaves are a feature, not a flaw."

- question: "The Yoneda embedding proves that if Hom(−, X) ≅ Hom(−, Y) as functors, then X ≅ Y in C. Which property of the embedding does this follow from?"
  type: multiple-choice
  options:
    - "Full faithfulness — the embedding is bijective on hom-sets, so isomorphic hom-functors force the representing objects to be isomorphic"
    - "Essential surjectivity — every presheaf is representable by a unique object, so isomorphic functors must have the same representing object"
    - "Cocompleteness of the presheaf category — colimits force the objects to coincide"
    - "The fact that Hom(−, X) is always a sheaf, making representable functors uniquely determined"
  answer: 0
  explanation: "Full faithfulness means Hom_C(X, Y) ≅ Hom_{[C^op,Set]}(Y(X), Y(Y)) — every morphism in C corresponds to exactly one natural transformation between the representables, and vice versa. If Y(X) ≅ Y(Y) (as presheaves), then there are natural transformations in both directions that compose to identities — and full faithfulness pulls these back to morphisms in C that compose to identities, giving X ≅ Y. Essential surjectivity plays no role here."

- question: "The Yoneda embedding Y: C → [C^op, Set] is an equivalence of categories — nearly every presheaf is naturally isomorphic to Hom(−, X) for some X."
  type: true-false
  answer: false
  explanation: "An equivalence of categories requires the functor to be fully faithful AND essentially surjective (every object in the target is isomorphic to something in the image). The Yoneda embedding is fully faithful but not essentially surjective — there are many non-representable presheaves that are not naturally isomorphic to any Hom(−, X). The gap between C and [C^op, Set] is precisely the non-representable presheaves, which are a rich and important class of objects in their own right."

- question: "Two objects X and Y in a category C are isomorphic if and only if their representable functors Hom(−, X) and Hom(−, Y) are naturally isomorphic."
  type: true-false
  answer: true
  explanation: "This is the key corollary of full faithfulness of the Yoneda embedding. If X ≅ Y, then post-composition with the isomorphism gives a natural isomorphism Hom(−, X) ≅ Hom(−, Y). Conversely, if Hom(−, X) ≅ Hom(−, Y), full faithfulness pulls the natural isomorphism back to an isomorphism X ≅ Y in C. An object is therefore completely characterized — up to isomorphism — by its hom-functor."

- question: "What does it mean for the Yoneda embedding to be 'fully faithful,' and what philosophical conclusion does this imply about how objects are determined by their relationships?"
  type: short-answer
  answer: "Fully faithful means the Yoneda embedding Y: C → [C^op, Set] is bijective on hom-sets: Hom_C(X, Y) ≅ Hom_{[C^op,Set]}(Y(X), Y(Y)) for all X, Y. Every morphism in C corresponds to exactly one natural transformation between the representable functors, and every natural transformation between representables comes from a unique morphism. The philosophical consequence is that an object X is completely determined — up to isomorphism — by the functor Hom(−, X), which encodes how every other object maps into X. Two objects with the same mapping-in behavior are the same object. An object is known entirely by its relationships."
  explanation: "This is the categorical formulation of a deep principle: the intrinsic properties of an object are less important than its position in the web of morphisms. The Yoneda embedding makes this precise — you can replace any object with its hom-functor without losing any information. This idea pervades modern mathematics: sheaves, spectra, and moduli spaces are all defined by what maps into them, not by explicit internal structure."
```

## Explainer

From the Yoneda lemma, you know that for any functor F: C^op → Set and any object X in C, natural transformations Nat(Hom(−,X), F) are in natural bijection with elements of F(X). The **Yoneda embedding** is the special case where we fix F = Hom(−,Y) for a second object Y. Plugging this in: Nat(Hom(−,X), Hom(−,Y)) ≅ Hom(Y,X)... wait, let us be careful about contravariance. The Yoneda lemma gives Nat(Hom(−,X), F) ≅ F(X), so with F = Hom(−,Y) we get Nat(Hom(−,X), Hom(−,Y)) ≅ Hom(Y, X) — no, that still isn't right. For the covariant embedding Y: C → [C^op, Set] sending X ↦ Hom(−,X), the Yoneda lemma gives Nat(Hom(−,X), Hom(−,Y)) ≅ Hom(X,Y). The bijection sends a morphism f: X → Y to the natural transformation whose component at Z is post-composition with f.

This single computation is the proof of **full faithfulness**. The embedding Y is **faithful** (injective on morphisms): if two morphisms f, g: X → Y induce the same natural transformation Hom(−,X) ⟹ Hom(−,Y), then in particular their component at X sends id_X to f and to g respectively, forcing f = g. The embedding is **full** (surjective on morphisms between representables): every natural transformation Hom(−,X) ⟹ Hom(−,Y) is post-composition with some morphism X → Y, by the Yoneda bijection above. Together: the hom-set Hom_C(X,Y) is in bijection with the hom-set Hom_{[C^op,Set]}(Y(X), Y(Y)). The functor Y does not distort morphisms at all.

The **philosophical punch line** is: an object X in C is completely determined, up to isomorphism, by the functor Hom(−,X) — that is, by the totality of how other objects map into X. Two objects with naturally isomorphic hom-functors are isomorphic. This is the categorical version of the principle "you are known by your relationships." In your prerequisite on representable functors, you saw that a functor F is representable when it is naturally isomorphic to some Hom(−,X); full faithfulness of the Yoneda embedding means representability is a property of the functor F, uniquely determined up to isomorphism of the representing object X.

The **presheaf category** [C^op, Set] is much larger than C: it contains C as a full subcategory via Y, but also all the non-representable presheaves — functors that do not arise as Hom(−,X) for any X. Think of these as "formal" or "virtual" objects that behave as if they could be in C but are not. This is analogous to the way the rational numbers embed into the reals: ℚ embeds faithfully into ℝ, but ℝ contains limits of Cauchy sequences that are not rational. The presheaf category is the **free cocompletion** of C — it adds all the colimits (formal colimits of diagrams in C) that C might be missing. Any functor from C to a cocomplete category extends uniquely along Y to a colimit-preserving functor from [C^op, Set]. This universal property is what makes the Yoneda embedding indispensable in topos theory and modern categorical logic.

A subtlety worth holding onto: Y is fully faithful but not essentially surjective (not every presheaf is representable), so it is not an equivalence of categories. The gap — the non-representable presheaves — is not a deficiency but a resource. Sheaf theory, for example, is the study of presheaves satisfying a local-gluing condition, and the objects of a Grothendieck topos are exactly the sheaves in this extended presheaf world. The Yoneda embedding is the door into this territory: it embeds the category you understand into a larger, richer world where many constructions that were impossible become routine.

