---
id: concrete-categories
title: Concrete Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: hard
- id: full-and-faithful-functors
  type: soft
builds-toward:
- free-objects
tags:
- concrete category
- forgetful functor
- faithful functor
- Set
- Grp
- Top
stage: advanced
status: validated
---
# Concrete Categories

## Core Idea
A concrete category is a category C equipped with a faithful functor U: C → Set, called the forgetful functor, that assigns to each object its underlying set and to each morphism the underlying function. Most familiar algebraic and topological categories are concrete: Grp (groups with homomorphisms), Top (topological spaces with continuous maps), Vect_k (vector spaces with linear maps), and Ring (rings with ring homomorphisms). The faithfulness of U means that morphisms in C are completely determined by their action on underlying sets, but the functor need not be full—not every set function is a group homomorphism, for instance.

## How It's Best Learned
Pick three concrete categories (Grp, Top, Vect) and for each one explicitly identify the forgetful functor, verify it is faithful, and determine whether it is full. Then find an example of a non-concrete category (the homotopy category of topological spaces) and understand why no faithful functor to Set exists.

## Common Misconceptions
- Not every category is concrete; the homotopy category hoTop is a standard counterexample, shown by Freyd's theorem.
- The forgetful functor is part of the structure of a concrete category, not a property—the same category may be concretized in different ways.
- Faithfulness does not imply fullness: the forgetful functor Grp → Set is faithful but not full, since not every set function is a homomorphism.

## Questions

```yaml
- question: "A student argues: 'Since every group homomorphism is a set function, the forgetful functor U: Grp → Set must be full — every morphism in Grp maps to a morphism in Set, so nothing is lost.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The reasoning is correct; U: Grp → Set is both faithful and full"
    - "Fullness would require every set function between underlying sets to be a morphism in Grp — that is, every function between groups to be a homomorphism — which is false; U is faithful but not full"
    - "The forgetful functor is not well-defined because groups have multiple valid underlying set representations"
    - "Fullness and faithfulness are equivalent for forgetful functors, so the distinction is irrelevant in this context"
  answer: 1
  explanation: "Fullness of U: Grp → Set would mean that for any two groups G, H, every set function from U(G) to U(H) is the image of some group homomorphism G → H. That is obviously false: most set functions between groups fail to preserve the group operation. Faithful means U is injective on each hom-set — distinct homomorphisms in Grp give distinct set functions, so morphisms are 'determined by their action on elements.' The student confused the direction: every morphism maps *to* a set function (that's just functoriality), but not every set function comes *from* a morphism (that would be fullness)."

- question: "The homotopy category hoTop — whose objects are topological spaces and whose morphisms are homotopy classes of continuous maps — is not a concrete category. What does this mean precisely?"
  type: multiple-choice
  options:
    - "There exists no faithful functor from hoTop to Set"
    - "hoTop is not a legitimate category because homotopy classes are not well-defined morphisms"
    - "The objects of hoTop do not have underlying sets, so no forgetful functor can be defined"
    - "hoTop is too large to be a category, since there are too many homotopy classes"
  answer: 0
  explanation: "By Freyd's theorem, no faithful functor hoTop → Set exists. This is a non-trivial result — it means homotopy classes of maps are not 'faithfully represented' by any assignment of elements to spaces. Contrast this with Top: the forgetful functor Top → Set is faithful because continuous maps are genuine set functions, and distinct continuous maps are distinct set functions. In hoTop, two homotopic maps become the same morphism even though they are different set functions — the identification collapses morphism sets in a way that is incompatible with faithfulness to Set."

- question: "Faithfulness of a functor U: C → Set ensures that two distinct morphisms in C cannot have the same underlying set function — morphisms in C are completely determined by their action on elements."
  type: true-false
  answer: true
  explanation: "Faithfulness means U is injective on each hom-set: if f ≠ g in C, then U(f) ≠ U(g) as set functions. This captures the intuition that morphisms in a concrete category 'are' structure-preserving functions — they cannot differ in some abstract categorical sense while agreeing on all elements. For the forgetful functor Grp → Set, two distinct homomorphisms must send some element to different images, since if they agree on all elements they are the same homomorphism."

- question: "Concreteness is an intrinsic property of a category: if a category's objects 'have underlying sets' and its morphisms 'are functions,' it is automatically concrete without needing to specify any additional structure."
  type: true-false
  answer: false
  explanation: "Concreteness is structure on a category, not a property of the abstract category. A concrete category is a pair (C, U) — the category together with a chosen faithful functor U: C → Set. The same abstract category can be made concrete in genuinely different ways: Grp can be concretized by sending each group to its underlying set (standard), or to its set of subgroups, or to its set of automorphisms. Different concretizations give different notions of 'elements.' Even when a canonical forgetful functor is obvious, it must be specified as part of the structure — concreteness is not automatic."

- question: "Explain the difference between a faithful functor and a full functor, and give a concrete example showing why the forgetful functor Grp → Set is faithful but not full."
  type: short-answer
  answer: "A functor F: C → D is faithful if it is injective on each hom-set: distinct morphisms in C map to distinct morphisms in D. It is full if it is surjective on each hom-set: every morphism in D between images of C-objects comes from some morphism in C. The forgetful functor U: Grp → Set is faithful because two distinct group homomorphisms f, g: G → H must disagree on at least one element of G — so U(f) ≠ U(g) as set functions. It is not full because there exist set functions between groups that are not homomorphisms: for example, the function f: ℤ → ℤ defined by f(n) = n + 1 is a perfectly valid set function but does not preserve the group operation (f(a + b) = a + b + 1 ≠ f(a) + f(b) = a + b + 2). Such a function is not in the image of U on hom-sets."
  explanation: "The faithful-not-full situation is generic for forgetful functors: morphisms in the category must be structure-preserving functions, but not every function preserves the structure. The forgetful functor 'sees' all the morphisms correctly but also sees many extra set functions that are not morphisms. Fullness would be pathologically strong — it would mean every function is a homomorphism, that every function between topological spaces is continuous, etc."
```

## Explainer

Most categories you've encountered — groups with homomorphisms, vector spaces with linear maps, topological spaces with continuous maps — come with an implicit understanding that their objects "have elements" and their morphisms "are functions" that preserve some structure. **Concrete categories** make this intuition precise in categorical language, using the functor machinery you've already developed.

A concrete category is not just a category C; it is a pair (C, U) where **U: C → Set** is a **faithful functor**, called the **forgetful functor**. "Forgetful" because U forgets the structure: it sends a group (G, ·) to its underlying set G, a topological space (X, τ) to the set X, a vector space V to the set of its elements — the algebraic or topological structure is discarded. Faithfulness (which you know means U is injective on each hom-set) captures the idea that the morphisms of C are completely determined by their underlying set-functions. Two distinct group homomorphisms must induce two distinct set functions; there are no "phantom morphisms" that look the same on elements but differ categorically.

The crucial asymmetry is that faithfulness does not imply fullness. **Fullness** of U: C → Set would mean every set function between underlying sets is a morphism in C — that every function between groups is a homomorphism, that every function between topological spaces is continuous. That is obviously false. Faithful-but-not-full is the generic situation for forgetful functors: morphisms in C must be structure-preserving functions, but not every function preserves the structure. The forgetful functor "sees" the morphisms correctly but sees more set functions than actually exist in C.

Concreteness is **structure on** a category, not an intrinsic property of the abstract category. The same abstract category can be concretized in multiple genuinely different ways: the category of groups can be concretized via U: Grp → Set (the standard forgetful functor), but also by sending each group to its set of subgroups, or to the set of its automorphisms. Different concretizations give different notions of "elements." Conversely, some categories cannot be made concrete at all. The homotopy category **hoTop** — whose morphisms are homotopy classes of continuous maps rather than the maps themselves — is a standard example: Freyd's theorem proves no faithful functor hoTop → Set exists, because the morphism sets are too "large" in a structurally inconsistent way. This non-concreteness reflects that homotopy classes are not faithfully represented by their action on points.
