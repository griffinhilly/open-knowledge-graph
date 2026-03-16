---
id: groupoids-and-weak-inverses
title: Groupoids and Weak Inverses
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: isomorphisms-in-categories
  type: hard
builds-toward:
- the-fundamental-groupoid
tags:
- groupoids
- invertible-morphisms
- automorphisms
stage: abstract-reasoning
status: draft
---

# Groupoids and Weak Inverses

## Core Idea
A groupoid is a category in which every morphism is an isomorphism, generalizing both groups and equivalence relations. Groupoids provide a framework for studying 'partial' algebraic structures where not all pairs of elements can be composed, and arise naturally in topology, combinatorics, and analysis. The theory of groupoids captures aspects of both group theory and category theory.

## How It's Best Learned
Study the fundamental groupoid of a topological space, the groupoid of a group action, and abstract groupoids given by presentations. Verify that morphisms are invertible and explore the automorphism groups at each object. Compute groupoid homology and cohomology.

## Common Misconceptions
A groupoid is not just a group with extra structure; it has multiple objects. The identity morphisms at different objects are distinct, and composition is only defined when target and source match appropriately.

## Explainer

From your prerequisite on categories and morphisms, you know that a category has objects and arrows between them, with composition satisfying associativity and unit laws. From isomorphisms in categories, you know that a morphism f: A → B is an isomorphism when there exists g: B → A such that g ∘ f = id_A and f ∘ g = id_B. A **groupoid** is simply a category in which *every* morphism is an isomorphism — all arrows are invertible. This single requirement transforms the algebraic structure dramatically.

To see why, consider the two extreme cases. A category with a single object and all morphisms invertible is exactly a **group**: composition is the group operation, the identity morphism is the identity element, and inverses are the morphism inverses. A groupoid generalizes this by allowing many objects, so you can have "partial group structure" — some pairs of elements compose, others do not, depending on whether source and target match. An **equivalence relation** on a set gives another extreme: objects are elements of the set, and there is exactly one morphism from x to y whenever x ~ y (and none otherwise). Invertibility corresponds to symmetry of the relation. So groupoids unify groups and equivalence relations in a single framework.

The richest example is the **fundamental groupoid** Π₁(X) of a topological space X. Objects are points of X, and a morphism from x to y is a homotopy class of paths from x to y. Composition is concatenation of paths; the identity at x is the constant path at x; and the inverse of a path is the same path traversed backwards. This is automatically a groupoid because every path can be reversed. When X is path-connected and you restrict to a single basepoint x₀, you recover the familiar fundamental group π₁(X, x₀) as the **automorphism group** at the object x₀. The fundamental groupoid is strictly more informative: it captures all basepoints and all paths between them simultaneously, without privileging any one basepoint.

The structure of a groupoid is thus richer than a group in one key respect: it has multiple objects, so the automorphism groups at different objects (the "local groups" Aut(x) = Hom(x, x)) may differ. In the fundamental groupoid of a space with multiple path components, the automorphism groups at points in different components are unrelated. In a groupoid arising from a group action — where objects are elements acted upon and a morphism from x to y exists for each group element g with g·x = y — the automorphism group at each object is the **stabilizer** of that object under the action. Groupoids make the relationship between global symmetry and local stabilizers transparent.

**Weak inverses** in the title refer to the morphism-level inverses in a groupoid, to distinguish them from strict inverses in a group. In a group, the inverse of g is unique and satisfies g⁻¹g = e = gg⁻¹ exactly. In higher categorical contexts (bicategories, 2-groupoids), one weakens the notion of invertibility to require only that the composites are *isomorphic* to the identity, rather than equal — this is the "weak" part. Ordinary groupoids are the 1-dimensional version of this tower. Your next topic, the fundamental groupoid, will develop the topological interpretation further and show how groupoids serve as the natural language for describing paths, loops, and homotopies across a space simultaneously.
