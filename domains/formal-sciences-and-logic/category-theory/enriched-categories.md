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
- id: vector-spaces
  type: soft
builds-toward:
- enriched-functors
tags:
- enriched-categories
- enrichment
- hom-objects
- monoidal-category
stage: expert
status: validated
---

# Enriched Categories and Enrichment

## Core Idea
An enriched category over a monoidal category V is a category where hom-sets are replaced by hom-objects in V, with composition and identity axioms formulated internal to V. Enriched categories generalize ordinary categories to settings where morphisms have additional structure—they may be topological spaces, abelian groups, metric spaces, or objects in any monoidal category, unifying many categories of structured objects.

## How It's Best Learned
Study categories enriched over the monoidal category of abelian groups (additive categories), over topological spaces (topological categories), and over a complete lattice (ordered categories). Understand how composition is defined using the monoidal product. Explore how many naturally occurring categories are enriched.

## Common Misconceptions
Enriched categories are not just categories with extra structure on objects; the hom-sets themselves are objects in V. Composition must be expressed in terms of the monoidal structure, which requires care when V is non-cartesian.

## Questions

```yaml
- question: "A mathematician observes that in her category C, every hom-collection hom(A,B) is a real vector space, and composition hom(B,C) × hom(A,B) → hom(A,C) is bilinear (linear in each argument separately). The correct description of C is:"
  type: multiple-choice
  options:
    - "An ordinary category with extra notation — the vector space structure is incidental"
    - "A category enriched over Vect, the monoidal category of real vector spaces"
    - "A 2-category, since the linear structure introduces morphisms between morphisms"
    - "A monoidal category, since the hom-sets carry a tensor product structure"
  answer: 1
  explanation: "The defining feature of enrichment is that hom-sets become hom-objects in a monoidal category V, and composition is expressed as a morphism in V. Here, hom-objects are vector spaces (objects in Vect) and composition is bilinear — precisely a morphism in Vect via the tensor product hom(B,C) ⊗ hom(A,B) → hom(A,C). This is Vect-enrichment (stronger than Ab-enrichment, which requires only abelian group structure). A 2-category is enriched over Cat, not Vect, and monoidal structure refers to a tensor product on the category's objects, not on its hom-sets."

- question: "In the Lawvere metric space construction, a set X with a distance function d(A,B) ≥ 0 satisfying d(A,A) = 0 and d(A,C) ≤ d(A,B) + d(B,C) is viewed as a category enriched over ([0,∞], +, 0). Which pairing makes this interpretation work?"
  type: multiple-choice
  options:
    - "Objects = distances, morphisms = points; the triangle inequality encodes composition"
    - "Objects = points, hom-object hom(A,B) = d(A,B); the triangle inequality is exactly the composition axiom"
    - "Objects = points, morphisms = paths; the distance is the cost of following a morphism"
    - "The metric space is monoidal, not enriched, because addition is commutative"
  answer: 1
  explanation: "In a category enriched over V = ([0,∞], +, 0), each hom-object hom(A,B) is a non-negative real number. Setting hom(A,B) = d(A,B), the composition axiom becomes: d(B,C) + d(A,B) ≥ d(A,C), exactly the triangle inequality. The identity axiom gives d(A,A) ≤ 0, hence d(A,A) = 0. Every metric space is thus an enriched category — a striking unification of geometry and category theory that shows these familiar structures are instances of the same abstract framework."

- question: "In an enriched category, it is the objects (not the hom-sets) that gain additional structure from the ambient monoidal category V."
  type: true-false
  answer: false
  explanation: "This is the central misconception about enrichment. The objects of an enriched category remain unstructured (or carry their own separate structure unrelated to V). What enrichment changes is the hom-collections: instead of plain sets, each hom(A,B) becomes an object in V. Composition is no longer a function between sets — it is a morphism in V: hom(B,C) ⊗ hom(A,B) → hom(A,C). The enrichment lives entirely in the morphism-structure, not in the object-structure."

- question: "When V = Set with cartesian product as tensor product, a V-enriched category is exactly an ordinary category."
  type: true-false
  answer: true
  explanation: "Set-enrichment is the base case. Hom-objects in Set are just sets, the tensor product (cartesian product) of hom-sets is the ordinary set-product, and composition is an ordinary function — reducing to the familiar definition of a category. All the enriched axioms collapse to the standard unit and associativity laws. This confirms that ordinary categories are 'Set-enriched categories,' and every choice of non-trivial V (Ab, Vect, Cat, metric spaces, etc.) generalizes this foundation."

- question: "What is the key structural difference between an ordinary category and a V-enriched category, and why does the choice of V matter for composition?"
  type: short-answer
  answer: "In an ordinary category, hom(A,B) is a plain set and composition is a function of sets. In a V-enriched category, hom(A,B) is an object in a monoidal category V, and composition is a morphism in V: hom(B,C) ⊗ hom(A,B) → hom(A,C), where ⊗ is V's tensor product. The choice of V determines the structure of the morphism-collections and how composition behaves: V = Ab gives bilinear composition (preadditive categories), V = [0,∞] gives the triangle inequality (metric spaces), V = Cat gives 2-categories. Different choices of V thus simultaneously generalize many distinct mathematical structures under a single framework."
  explanation: "The identity is also enriched: instead of selecting an element id_A from hom(A,A), it is a morphism I → hom(A,A) from the unit object I of V. All axioms (associativity, unitality) are expressed as commutative diagrams in V using V's associator and unitors. This means enrichment is a genuine generalization, not just notation — it forces us to think of composition and identity as internal operations in V rather than as set-level functions."
```

## Explainer

In an ordinary category, the morphisms between any two objects A and B form a *set* — hom(A, B) is just a collection of arrows, with no further structure. But in many naturally occurring mathematical settings, the morphisms carry richer data. Linear maps between vector spaces form a *vector space* themselves. Continuous maps between topological spaces can be given a *topology*. Natural transformations between functors organize into a *category*. An **enriched category** formalizes this: instead of hom-sets, you have **hom-objects** living in some ambient monoidal category V.

To make this precise, recall from your study of monoidal categories that a monoidal category V has a tensor product ⊗ and a unit object I. A **V-enriched category** (or category enriched over V) has a set of objects, and for each pair of objects A, B a hom-object hom(A,B) ∈ V. Composition is not a function of sets — it is a *morphism* in V: ∘ : hom(B,C) ⊗ hom(A,B) → hom(A,C). The identity on A is a morphism idₐ : I → hom(A,A). The associativity and unit axioms for composition must be expressed as commutative diagrams *in V*, using the associator and unitors of the monoidal structure. When V = **Set** (with cartesian product as tensor), this reduces exactly to an ordinary category.

The real payoff comes from the examples. A category enriched over **Ab** (abelian groups, with ⊗ as tensor product) is an **Ab-enriched** or **preadditive** category: every hom-set is an abelian group and composition is bilinear. Rings are one-object Ab-enriched categories; the module category over a ring is Ab-enriched. A category enriched over **[0,∞]** (extended non-negative reals, with addition as tensor) is a **Lawvere metric space**: the "hom-object" from A to B is the distance d(A,B), and composition becomes the triangle inequality d(A,C) ≤ d(A,B) + d(B,C). This shows that metric spaces *are* categories — a striking unification. A 2-category is a category enriched over **Cat**.

Enrichment also changes what "functor" and "natural transformation" mean. An **enriched functor** F : C → D between V-enriched categories must provide a morphism in V: F_{A,B} : hom_C(A,B) → hom_D(FA,FB), compatible with composition and identities in V — not merely a function on hom-sets. For Ab-enriched categories, this means additive functors. For metric spaces, this means non-expansive maps. The theory of enriched categories thus simultaneously generalizes and unifies these familiar notions under a single framework, and the closed categories prerequisite — where internal hom-objects exist — makes enrichment over closed monoidal categories particularly natural.
