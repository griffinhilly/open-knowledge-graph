---
id: enriched-categories
title: Enriched Categories and Enrichment
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: monoidal-categories
  type: hard
- id: closed-categories-and-internal-homs
  type: soft
- id: vector-spaces-definition
  type: soft
builds-toward:
- enriched-functors
tags:
- enriched-categories
- enrichment
- hom-objects
- monoidal-category
stage: abstract-reasoning
status: draft
---

# Enriched Categories and Enrichment

## Core Idea
An enriched category over a monoidal category V is a category where hom-sets are replaced by hom-objects in V, with composition and identity axioms formulated internal to V. Enriched categories generalize ordinary categories to settings where morphisms have additional structure—they may be topological spaces, abelian groups, metric spaces, or objects in any monoidal category, unifying many categories of structured objects.

## How It's Best Learned
Study categories enriched over the monoidal category of abelian groups (additive categories), over topological spaces (topological categories), and over a complete lattice (ordered categories). Understand how composition is defined using the monoidal product. Explore how many naturally occurring categories are enriched.

## Common Misconceptions
Enriched categories are not just categories with extra structure on objects; the hom-sets themselves are objects in V. Composition must be expressed in terms of the monoidal structure, which requires care when V is non-cartesian.

## Explainer

In an ordinary category, the morphisms between any two objects A and B form a *set* — hom(A, B) is just a collection of arrows, with no further structure. But in many naturally occurring mathematical settings, the morphisms carry richer data. Linear maps between vector spaces form a *vector space* themselves. Continuous maps between topological spaces can be given a *topology*. Natural transformations between functors organize into a *category*. An **enriched category** formalizes this: instead of hom-sets, you have **hom-objects** living in some ambient monoidal category V.

To make this precise, recall from your study of monoidal categories that a monoidal category V has a tensor product ⊗ and a unit object I. A **V-enriched category** (or category enriched over V) has a set of objects, and for each pair of objects A, B a hom-object hom(A,B) ∈ V. Composition is not a function of sets — it is a *morphism* in V: ∘ : hom(B,C) ⊗ hom(A,B) → hom(A,C). The identity on A is a morphism idₐ : I → hom(A,A). The associativity and unit axioms for composition must be expressed as commutative diagrams *in V*, using the associator and unitors of the monoidal structure. When V = **Set** (with cartesian product as tensor), this reduces exactly to an ordinary category.

The real payoff comes from the examples. A category enriched over **Ab** (abelian groups, with ⊗ as tensor product) is an **Ab-enriched** or **preadditive** category: every hom-set is an abelian group and composition is bilinear. Rings are one-object Ab-enriched categories; the module category over a ring is Ab-enriched. A category enriched over **[0,∞]** (extended non-negative reals, with addition as tensor) is a **Lawvere metric space**: the "hom-object" from A to B is the distance d(A,B), and composition becomes the triangle inequality d(A,C) ≤ d(A,B) + d(B,C). This shows that metric spaces *are* categories — a striking unification. A 2-category is a category enriched over **Cat**.

Enrichment also changes what "functor" and "natural transformation" mean. An **enriched functor** F : C → D between V-enriched categories must provide a morphism in V: F_{A,B} : hom_C(A,B) → hom_D(FA,FB), compatible with composition and identities in V — not merely a function on hom-sets. For Ab-enriched categories, this means additive functors. For metric spaces, this means non-expansive maps. The theory of enriched categories thus simultaneously generalizes and unifies these familiar notions under a single framework, and the closed categories prerequisite — where internal hom-objects exist — makes enrichment over closed monoidal categories particularly natural.
