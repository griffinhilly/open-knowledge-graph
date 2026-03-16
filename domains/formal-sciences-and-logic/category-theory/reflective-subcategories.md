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
stage: advanced
status: draft
---

# Reflective and Coreflective Subcategories

## Core Idea
A full subcategory D ⊆ C is reflective if the inclusion functor i: D ↪ C has a left adjoint, called the reflector. The reflector provides a universal way to 'project' objects of C into D while preserving structure. Coreflective subcategories are defined dually, with the inclusion having a right adjoint. Reflective subcategories arise in completion, localization, and in constructing quotient structures.

## How It's Best Learned
Study the reflection of finite sets into all sets (not reflective), abelian groups into groups via abelianization (reflective), and divisible groups as a reflective subcategory of abelian groups. For each example, identify the reflector explicitly and verify the adjunction.

## Common Misconceptions
Not every full subcategory is reflective; reflectivity requires an adjoint to exist and satisfy naturality. The reflector is not surjective on objects—the image of the reflector covers only some objects of C. A full subcategory being reflective does not mean it is closed under limits or colimits in the original category.

## Explainer

From your study of adjoint functors, you know that an adjunction L ⊣ R between categories C and D provides a universal relationship: L is "free" and R is "forgetful" in a precise sense, connected by the unit η: id_C → R ∘ L and counit ε: L ∘ R → id_D. A **reflective subcategory** is a special case of this pattern where the right adjoint is an inclusion functor. Specifically, a full subcategory D ⊆ C is reflective when the inclusion i: D ↪ C has a left adjoint L: C → D, called the **reflector** (or reflection functor). The adjunction L ⊣ i means: for every object X in C and every object A in D, there is a natural bijection Hom_D(LX, A) ≅ Hom_C(X, iA).

The unit of the adjunction gives, for each X ∈ C, a morphism η_X: X → L(X) in C (the inclusion of LX back into C via i). This is the **reflection** of X into D — the "best approximation" to X that lives in D. The universal property says: any morphism X → A in C with A ∈ D factors uniquely through η_X. There is no better D-approximation to X than LX; any map from X to a D-object factors through it. This is exactly the universal property you know from free constructions: the abelianization Ab(G) of a group G is the best abelian group that G maps to, and the map G → Ab(G) is the unit of the reflection adjunction between abelian groups and all groups.

Concrete examples anchor the concept. **Abelianization**: the subcategory Ab of abelian groups inside Grp is reflective; L(G) = G/[G,G] is the quotient by the commutator subgroup. **Sheafification**: the category of sheaves on a site is a reflective subcategory of presheaves; the sheafification functor F ↦ F^+ is the reflector. **Completion**: the category of complete metric spaces is reflective inside metric spaces; the reflector sends a metric space to its Cauchy completion. **Stone-Čech compactification**: compact Hausdorff spaces form a reflective subcategory of completely regular spaces, with the Stone-Čech compactification βX as the reflection of X. In each case, the reflection map η_X: X → LX is universal: it is the initial morphism from X to an object of the subcategory.

The **counit** of the adjunction i ∘ L → id_D specializes here: since D is a full subcategory and i is the inclusion, the counit at A ∈ D is a morphism L(iA) → A. For the adjunction to be a reflective subcategory, this counit must be an isomorphism (D is "closed" under the reflector applied to its own objects). This is equivalent to saying i is fully faithful, which holds because i is an inclusion of a full subcategory. The combination of fully faithful right adjoint and left adjoint is what makes the subcategory "reflective" rather than just "adjointly related" — the unit η_X: X → LX is a D-localization, not merely a map to a related category.

**Coreflective subcategories** are defined dually: the inclusion i: D ↪ C has a right adjoint R: C → D (the coreflector). Examples include the subcategory of discrete topological spaces inside all topological spaces (the coreflector sends X to the set of points with discrete topology), or the subcategory of abelian groups inside Ab that are divisible. Reflective and coreflective subcategories appear throughout mathematics wherever you want to "project" into a better-behaved class: reflective subcategories are preserved under limits in C (the inclusion i preserves limits because right adjoints do), which is why they are used in localization — inverting maps or enforcing exactness conditions — and in topos theory where the category of sheaves is a reflective subcategory of presheaves with the sheafification reflector playing a central structural role.
