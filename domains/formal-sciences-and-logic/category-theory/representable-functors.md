---
id: representable-functors
title: Representable Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: functors
  type: hard
- id: natural-transformations
  type: soft
- id: opposite-categories-and-duality
  type: soft
- id: full-and-faithful-functors
  type: soft
- id: functor-categories
  type: soft
builds-toward:
- yoneda-lemma
- adjoint-functors
tags:
- representable functor
- hom-functor
- Yoneda
- presheaf
stage: expert
status: validated
---
# Representable Functors

## Core Idea
For each object A in a locally small category C, the hom-functor Hom(A, -): C → Set sends each object B to the set of morphisms Hom(A, B) and each morphism f: B → C to post-composition with f. A functor F: C → Set is representable if it is naturally isomorphic to Hom(A, -) for some object A, called the representing object. Representability is a powerful concept: many construction functors (tensor product, free algebras, cohomology groups) are representable, and their representing objects carry universal properties.

## How It's Best Learned
Show that the forgetful functor from Grp to Set is representable by the free group on one generator ℤ: a group homomorphism ℤ → G is uniquely determined by where 1 goes, so Grp(ℤ, G) ≅ G as sets, naturally in G. Identify the representing objects for other familiar functors.

## Common Misconceptions
- Not every functor C → Set is representable; representability is a non-trivial condition checked via the Yoneda lemma.
- The representing object is unique up to unique isomorphism, not unique as a set-theoretic construction.
- The contravariant hom-functor Hom(-, A) is representable in C^op, not in C.

## Questions

```yaml
- question: "The forgetful functor U: Grp → Set is represented by ℤ. A student asks why a homomorphism φ: ℤ → G is completely determined by φ(1). What is the correct explanation?"
  type: multiple-choice
  options:
    - "ℤ is the smallest group, so there are fewer homomorphisms to track than for any other choice of representing group"
    - "Every integer n equals 1+1+...+1 (or its negatives), so the homomorphism property forces φ(n) = φ(1)^n, making φ(1) the only free choice"
    - "Homomorphisms from ℤ are always injective, so specifying any element of G determines the rest by injectivity"
    - "ℤ is abelian, and homomorphisms from abelian groups are always determined by a single generator in any target group"
  answer: 1
  explanation: "ℤ is the free group on one generator (the integer 1). The homomorphism property requires φ(m + n) = φ(m)φ(n), so φ(n) = φ(1+1+...+1) = φ(1)^n for positive n, and the rule extends to negatives via φ(-n) = φ(n)⁻¹. This means once you choose where 1 maps, the values at all other integers are forced. Conversely, any element g ∈ G defines a valid homomorphism by φ(1) = g (no relations in ℤ can fail in G). So Hom_Grp(ℤ, G) ≅ G as sets, naturally in G — this is exactly representability. The key is that ℤ imposes no relations that might obstruct extension to a target group."

- question: "You find a bijection α_B: F(B) ≅ Hom(A, B) for one specific object B in a category C. Is this sufficient to conclude that F is representable by A?"
  type: multiple-choice
  options:
    - "Yes — a bijection at any single object establishes representability, since functoriality will propagate the isomorphism"
    - "No — representability requires a natural isomorphism: the bijection must commute with all morphisms f: B → C in C, not just exist at one object"
    - "Yes — once the bijection holds at B, it holds at all objects isomorphic to B, which covers the important cases"
    - "No — you need bijections at two objects to confirm the pattern, then naturality follows automatically"
  answer: 1
  explanation: "Representability requires a *natural* isomorphism, not just a pointwise bijection. Naturality means: for every morphism f: B → C, the bijection α commutes with the induced maps — F(f) on the F-side must correspond to post-composition with f on the Hom-side. A bijection at a single object B might be completely ad hoc, failing to respect morphisms from B to other objects. Checking naturality is what distinguishes a genuine representation (the bijection 'works with the category structure') from an accidental set-level coincidence at one point."

- question: "Every functor F: C → Set is representable, since for any functor we can always construct a representing object by taking a colimit."
  type: true-false
  answer: false
  explanation: "Representability is a non-trivial condition that most functors do not satisfy. A functor F: C → Set is representable only if there exists an object A and a *natural* isomorphism F ≅ Hom(A, -). There is no general construction that produces a representing object for an arbitrary functor. The Yoneda lemma characterizes representability precisely: F is representable iff there is a universal element u ∈ F(A) such that every element of every F(B) is of the form F(f)(u) for a unique f: A → B. This is a strong condition that many functors fail. For example, a functor that sends all objects to a fixed set with more than one element may not be representable."

- question: "If a functor F: C → Set is representable by both A and A', then A and A' must be isomorphic in C (though not necessarily equal as sets or constructions)."
  type: true-false
  answer: true
  explanation: "The representing object is unique up to unique isomorphism — a fundamental consequence of universal properties. If both A and A' represent F, then Hom(A, -) ≅ F ≅ Hom(A', -) naturally. By the Yoneda lemma, natural transformations between hom-functors correspond bijectively to morphisms in C: a natural isomorphism Hom(A, -) ≅ Hom(A', -) corresponds to a unique isomorphism A ≅ A' in C. This uniqueness-up-to-unique-isomorphism is a hallmark of categorical universal constructions: the representing object is determined by its universal property, not by any particular set-theoretic construction."

- question: "In the representability setup, why is the element u = α_A(id_A) ∈ F(A) called a 'universal element,' and how does it generate all other elements of the functor F?"
  type: short-answer
  answer: "The element u is universal because every element of F(B), for any object B, can be obtained from u by applying F to some morphism. Specifically, the natural bijection α_B: Hom(A, B) → F(B) sends each morphism f: A → B to F(f)(u) ∈ F(B). This means every element of every F(B) is the image of u under F(f) for a unique morphism f: A → B. The identity id_A maps to u itself under α_A. In this sense u is a single 'seed' element that generates the entire functor via the morphisms of C — which is why finding a universal element in F(A) is the standard way to prove a functor is representable and identify its representing object."
  explanation: "The universal element perspective reframes representability: instead of F being a family of sets (one per object) with a complicated functorial structure, everything is encoded in a single element u of a single set F(A). The morphisms of C 'transport' u to all other elements. This is analogous to how a group homomorphism from a free group is determined by one generator's image — the universal element plays the same role for functors that the generator plays for free groups. The Yoneda lemma formalizes this by showing that natural transformations Hom(A, -) → F correspond exactly to elements of F(A), with u corresponding to the identity natural transformation."
```

## Explainer

You know that a functor F: C → Set assigns a set to each object and a function to each morphism. Most functors you encounter in practice have an interesting feature: the sets F(B) can be identified with sets of morphisms in C. When this identification is natural — meaning compatible with all morphisms in C in the precise sense you learned from natural transformations — the functor is called **representable**. Representability is a way of saying "this functor is really just about morphisms out of a fixed object."

The **hom-functor** Hom(A, −): C → Set is the prototype. Fix any object A. For each object B, define Hom(A, B) to be the set of all morphisms from A to B in C. For each morphism f: B → C, define Hom(A, f) to be post-composition: send each g: A → B to f ∘ g: A → C. This construction is functorial — it respects identity morphisms and composition — and it is the canonical example of a representable functor, with representing object A. A functor F: C → Set is **representable** if there exists an object A and a natural isomorphism α: F ≅ Hom(A, −). The object A is called the **representing object** of F.

A concrete example clarifies what representability means. Consider the forgetful functor U: Grp → Set. Does there exist a group A such that group homomorphisms from A to any group G are in natural bijection with elements of G? Yes: take A = ℤ. A homomorphism φ: ℤ → G is completely determined by φ(1) ∈ G (since φ(n) = φ(1)^n by the homomorphism property), and any element g ∈ G determines a valid homomorphism by φ(1) = g. So Hom_Grp(ℤ, G) ≅ U(G) naturally in G — the forgetful functor is represented by ℤ. The "naturally in G" condition means this bijection commutes with all group homomorphisms G → G', which is exactly the naturality square you learned with natural transformations.

The power of representability is that it converts abstract functor questions into questions about morphisms in C, which are often more tractable. The **representing object** plays the role of a "universal element" — the bijection Hom(A, B) ≅ F(B) maps the identity morphism id_A ∈ Hom(A, A) to a distinguished element u ∈ F(A) with the property that every element of every F(B) is the image of u under some morphism. This universal element characterizes the representing object up to unique isomorphism, and recognizing it is the standard way to prove representability. The Yoneda lemma, which you will study next, sharpens this: natural transformations Hom(A, −) → F are in bijection with elements of F(A), giving a complete and powerful description of all representable functors.
