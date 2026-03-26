---
id: reflective-subcategories
title: Reflective and Coreflective Subcategories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: functors
  type: hard
builds-toward:
- topos-theory-intro
tags:
- reflective
- coreflective
- localization
- adjoint
- inclusion
stage: expert
status: validated
---

# Reflective and Coreflective Subcategories

## Core Idea
A full subcategory D ⊆ C is reflective if the inclusion functor i: D ↪ C has a left adjoint, called the reflector. The reflector provides a universal way to 'project' objects of C into D while preserving structure. Coreflective subcategories are defined dually, with the inclusion having a right adjoint. Reflective subcategories arise in completion, localization, and in constructing quotient structures.

## How It's Best Learned
Study the reflection of finite sets into all sets (not reflective), abelian groups into groups via abelianization (reflective), and divisible groups as a reflective subcategory of abelian groups. For each example, identify the reflector explicitly and verify the adjunction.

## Common Misconceptions
Not every full subcategory is reflective; reflectivity requires an adjoint to exist and satisfy naturality. The reflector is not surjective on objects—the image of the reflector covers only some objects of C. A full subcategory being reflective does not mean it is closed under limits or colimits in the original category.

## Questions

```yaml
- question: "A student says: 'The category Ab of abelian groups is reflective inside Grp because we can quotient any group G by its commutator subgroup [G,G] to get an abelian group. That's the whole story.' What crucial fact is missing from this description?"
  type: multiple-choice
  options:
    - "The construction is wrong — the reflection is the center Z(G), not the commutator quotient"
    - "The construction is not functorial and cannot be applied consistently to group homomorphisms"
    - "The reflection G → G/[G,G] has a universal property: every group homomorphism from G to any abelian group factors uniquely through it — this is what makes it the *reflector*, not just any quotient"
    - "Ab is not reflective in Grp; it is coreflective because the inclusion has a right adjoint"
  answer: 2
  explanation: "The abelianization construction G ↦ G/[G,G] is correct, but the student describes it as if the quotient is just a convenient construction. The key is the *universal property*: G/[G,G] is the initial abelian group that G maps to. Any group homomorphism f: G → A with A abelian factors uniquely as G → G/[G,G] → A. This universal factorization property is what makes it a reflector — the reflection is not merely *an* abelian quotient but the *best* one. Without the universal property, you just have a quotient; with it, you have an adjunction."

- question: "Which of the following correctly characterizes the reflector L: C → D in a reflective subcategory D ⊆ C?"
  type: multiple-choice
  options:
    - "L is a functor that sends each object of C to an arbitrarily chosen object of D"
    - "For each object X in C, L(X) is the object of D such that any morphism from X to any object A in D factors uniquely through the unit map η_X: X → L(X) in C"
    - "L is the right adjoint of the inclusion functor i: D ↪ C"
    - "L is surjective on objects: every object of D appears as L(X) for some X in C"
  answer: 1
  explanation: "The reflector L is characterized by the universal property of the unit map η_X: X → L(X). This map is not just any morphism into D — it is the *initial* morphism from X to any D-object, meaning all other maps from X into D factor through it uniquely. This is the adjunction condition Hom_D(L(X), A) ≅ Hom_C(X, i(A)) made concrete. Option C has the variance wrong: L is the *left* adjoint of the inclusion, not the right adjoint. Being a left adjoint (the reflector) is what defines a reflective subcategory."

- question: "The Stone-Čech compactification βX is the reflection of a topological space X into the subcategory of compact Hausdorff spaces, meaning every continuous map from X to any compact Hausdorff space factors uniquely through the canonical map X → βX."
  type: true-false
  answer: true
  explanation: "This is precisely the universal property of the Stone-Čech compactification, and it is exactly the statement that compact Hausdorff spaces form a reflective subcategory of completely regular spaces with βX as the reflector. The canonical map X → βX is the unit of the adjunction. Any continuous f: X → K with K compact Hausdorff extends uniquely to a continuous f̃: βX → K. This universal property is what distinguishes βX from all other compactifications of X — it is the *maximal* compactification in the sense that it maps onto all others."

- question: "Nearly every full subcategory of a category is reflective, as long as it is closed under isomorphisms."
  type: true-false
  answer: false
  explanation: "Being a full subcategory closed under isomorphisms is not sufficient for reflectivity. Reflectivity requires that the inclusion functor i: D ↪ C has a left adjoint — a reflector L: C → D — satisfying a universal property for every object of C. Many full subcategories do not have this property. For example, the subcategory of finite sets inside all sets is a full subcategory closed under isomorphisms, but it is not reflective: there is no 'best finite approximation' to an infinite set in the required sense. The existence of the adjoint is a genuine and nontrivial condition."

- question: "What does it mean for a subcategory D to be reflective in C, and why is the universal property of the unit map η_X: X → L(X) the central fact — rather than merely the existence of a functor L: C → D?"
  type: short-answer
  answer: "D is reflective in C if the inclusion functor i: D ↪ C has a left adjoint L: C → D. This means for every X ∈ C there is a morphism η_X: X → L(X) in C such that any morphism f: X → A with A ∈ D factors uniquely as f = g ∘ η_X for some g: L(X) → A in D. The universal property is central because it is what makes L(X) the *best* D-approximation to X, not just *some* D-object related to X. Without it, L is just a functor that maps into D — many such functors exist and most have no special status. The universal property gives L(X) a canonical role: it is the initial object in the category of morphisms from X to D-objects, which is precisely the adjunction condition."
  explanation: "The distinction matters practically: sheafification is the unique functor from presheaves to sheaves that is left adjoint to the inclusion, and this determines it up to unique isomorphism. Without the universal property, you would have no canonical way to extend maps from presheaves to sheaves, and the construction would lose its functorial coherence. The universal property is not extra structure on top of the functor — it *is* the reason the reflector is well-defined and useful."
```

## Explainer

From your study of adjoint functors, you know that an adjunction L ⊣ R between categories C and D provides a universal relationship: L is "free" and R is "forgetful" in a precise sense, connected by the unit η: id_C → R ∘ L and counit ε: L ∘ R → id_D. A **reflective subcategory** is a special case of this pattern where the right adjoint is an inclusion functor. Specifically, a full subcategory D ⊆ C is reflective when the inclusion i: D ↪ C has a left adjoint L: C → D, called the **reflector** (or reflection functor). The adjunction L ⊣ i means: for every object X in C and every object A in D, there is a natural bijection Hom_D(LX, A) ≅ Hom_C(X, iA).

The unit of the adjunction gives, for each X ∈ C, a morphism η_X: X → L(X) in C (the inclusion of LX back into C via i). This is the **reflection** of X into D — the "best approximation" to X that lives in D. The universal property says: any morphism X → A in C with A ∈ D factors uniquely through η_X. There is no better D-approximation to X than LX; any map from X to a D-object factors through it. This is exactly the universal property you know from free constructions: the abelianization Ab(G) of a group G is the best abelian group that G maps to, and the map G → Ab(G) is the unit of the reflection adjunction between abelian groups and all groups.

Concrete examples anchor the concept. **Abelianization**: the subcategory Ab of abelian groups inside Grp is reflective; L(G) = G/[G,G] is the quotient by the commutator subgroup. **Sheafification**: the category of sheaves on a site is a reflective subcategory of presheaves; the sheafification functor F ↦ F^+ is the reflector. **Completion**: the category of complete metric spaces is reflective inside metric spaces; the reflector sends a metric space to its Cauchy completion. **Stone-Čech compactification**: compact Hausdorff spaces form a reflective subcategory of completely regular spaces, with the Stone-Čech compactification βX as the reflection of X. In each case, the reflection map η_X: X → LX is universal: it is the initial morphism from X to an object of the subcategory.

The **counit** of the adjunction i ∘ L → id_D specializes here: since D is a full subcategory and i is the inclusion, the counit at A ∈ D is a morphism L(iA) → A. For the adjunction to be a reflective subcategory, this counit must be an isomorphism (D is "closed" under the reflector applied to its own objects). This is equivalent to saying i is fully faithful, which holds because i is an inclusion of a full subcategory. The combination of fully faithful right adjoint and left adjoint is what makes the subcategory "reflective" rather than just "adjointly related" — the unit η_X: X → LX is a D-localization, not merely a map to a related category.

**Coreflective subcategories** are defined dually: the inclusion i: D ↪ C has a right adjoint R: C → D (the coreflector). Examples include the subcategory of discrete topological spaces inside all topological spaces (the coreflector sends X to the set of points with discrete topology), or the subcategory of abelian groups inside Ab that are divisible. Reflective and coreflective subcategories appear throughout mathematics wherever you want to "project" into a better-behaved class: reflective subcategories are preserved under limits in C (the inclusion i preserves limits because right adjoints do), which is why they are used in localization — inverting maps or enforcing exactness conditions — and in topos theory where the category of sheaves is a reflective subcategory of presheaves with the sheafification reflector playing a central structural role.
