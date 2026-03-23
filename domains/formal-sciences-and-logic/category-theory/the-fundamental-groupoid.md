---
id: the-fundamental-groupoid
title: The Fundamental Groupoid of a Space
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: groupoids-and-weak-inverses
  type: hard
builds-toward:
- enriched-categories
tags:
- fundamental-group
- paths
- homotopy
- topological-invariant
stage: expert
status: draft
---

# The Fundamental Groupoid of a Space

## Core Idea
The fundamental groupoid of a topological space has points as objects and homotopy classes of paths as morphisms, with composition given by path concatenation. Unlike the fundamental group (which depends on a basepoint choice), the fundamental groupoid is base-point-free and captures the full homotopy-theoretic information of the space. It provides a more natural and categorical framework for studying connectivity.

## How It's Best Learned
Compute the fundamental groupoid of familiar spaces: the circle, the plane, a figure-eight. Verify that morphisms are invertible and explore how groupoid structure reflects topological properties. Understand the relationship between the fundamental groupoid and fundamental groups at various basepoints.

## Common Misconceptions
The fundamental groupoid is not the same as the fundamental group; it encodes information at all points simultaneously. The automorphism group at a point is the fundamental group at that basepoint, but the groupoid structure includes much more.

## Questions

```yaml
- question: "What are the morphisms from point x to point y in the fundamental groupoid Π₁(X) of a topological space X?"
  type: multiple-choice
  options:
    - "All continuous functions from x to y in the space X"
    - "All continuous paths from x to y, counted without any identification"
    - "Homotopy classes of continuous paths from x to y, where two paths are identified if one can be continuously deformed into the other while keeping endpoints fixed"
    - "The group of loops at x tensored with the group of loops at y"
  answer: 2
  explanation: "Morphisms in Π₁(X) are homotopy classes of paths — not individual paths, because two paths related by a homotopy (a continuous deformation fixing endpoints) are identified as the same morphism. This quotienting is essential: without it, composition (path concatenation) would not be strictly associative, only associative up to homotopy. The identification ensures the groupoid axioms hold on the nose."

- question: "A space X consists of two disjoint circles (disconnected). How does the fundamental groupoid Π₁(X) capture the disconnection better than the fundamental group π₁(X, x₀) based at a point in one circle?"
  type: multiple-choice
  options:
    - "The groupoid contains strictly more morphisms than the fundamental group, encoding more loop information"
    - "The fundamental group at x₀ captures only loops in one component, missing the other component entirely; the groupoid has no morphisms between components, directly encoding the disconnection in its structure"
    - "The fundamental group can be based simultaneously at points in both circles, capturing the full space"
    - "Groupoids always contain more information than groups regardless of the space"
  answer: 1
  explanation: "To use the fundamental group, you must choose a basepoint in one component. That component's loops are captured, but the other component is invisible — there are no paths connecting them. The fundamental groupoid avoids this problem: it has objects in both components, morphisms within each component (the loop information), and crucially no morphisms between components — directly encoding the disconnection as an absence of morphisms. No basepoint choice is required."

- question: "The fundamental group π₁(X, x₀) at a basepoint x₀ is exactly the automorphism group of the object x₀ in the fundamental groupoid Π₁(X)."
  type: true-false
  answer: true
  explanation: "In Π₁(X), the morphisms from x₀ to x₀ are homotopy classes of loops based at x₀ — exactly the elements of π₁(X, x₀). Composition of morphisms in the groupoid corresponds to loop concatenation, and the group structure of π₁ matches the automorphism group structure at x₀. The fundamental groupoid thus packages the fundamental groups at all basepoints simultaneously, with the automorphism groups being the 'diagonal' of the structure."

- question: "For a path-connected space, the fundamental groupoid contains strictly more topological information than the fundamental group at any single basepoint."
  type: true-false
  answer: false
  explanation: "For a path-connected space, all automorphism groups Aut_{Π₁(X)}(x) are isomorphic to each other (conjugate via any path between basepoints), so the groupoid and the fundamental group at any single point contain the same information up to group isomorphism. The advantage of the groupoid is not more information but greater naturality: no arbitrary basepoint choice, cleaner functoriality, and more natural statements of theorems like van Kampen. For disconnected spaces, the groupoid does encode strictly more information."

- question: "Why is the fundamental groupoid considered more natural than the fundamental group for studying topology? What concrete advantage does it provide for disconnected spaces?"
  type: short-answer
  answer: "The fundamental groupoid Π₁(X) requires no basepoint choice — it treats all points of X symmetrically as objects. Any continuous map f: X → Y induces a functor Π₁(f): Π₁(X) → Π₁(Y) without fixing any basepoint, making the construction fully functorial. The fundamental group, by contrast, requires choosing a basepoint, and a map induces a group homomorphism only between groups at corresponding basepoints. For disconnected spaces, the groupoid encodes the full connectivity structure: components with no path between them have no morphisms between them in the groupoid, directly capturing disconnection. The fundamental group at a single basepoint sees only its own component."
  explanation: "The groupoid's naturality also shows up in the van Kampen theorem: the groupoid version (Π₁(X∪Y) is the pushout of Π₁(X) and Π₁(Y) over Π₁(X∩Y)) is cleaner and more general than the group version, which requires basepoint conditions and separate handling of path-connected intersections."
```

## Explainer

You know that a **groupoid** is a category in which every morphism is invertible. Objects can be many, not just one, so a groupoid generalizes both groups (one object, all morphisms invertible) and sets (many objects, only identity morphisms). The **fundamental groupoid** Π₁(X) of a topological space X is the canonical example of a groupoid arising in nature. Its objects are the points of X; its morphisms from point x to point y are **homotopy classes of paths** from x to y — continuous curves γ: [0,1] → X with γ(0) = x and γ(1) = y, where two paths are identified if one can be continuously deformed into the other while keeping the endpoints fixed.

Composition of morphisms is **path concatenation**: given a path from x to y and a path from y to z, you travel first along one, then the other, reparametrized to the unit interval. The identity morphism at x is the constant path that stays at x. The inverse of a path γ is the **reversed path** γ⁻¹(t) = γ(1−t), which traces the same route backwards. Checking the groupoid axioms reduces to standard facts in homotopy theory: concatenation is associative up to homotopy, the constant path is a homotopy identity, and reversing a path gives a homotopy inverse. Every morphism is invertible — that is the groupoid property — because you can always walk backwards.

The **fundamental group** π₁(X, x₀) based at a chosen point x₀ is the automorphism group Aut_{Π₁(X)}(x₀) in the fundamental groupoid — the collection of all homotopy classes of *loops* at x₀ (paths where γ(0) = γ(1) = x₀). The groupoid sees all basepoints simultaneously. When X is **path-connected**, all the automorphism groups Aut(x) are isomorphic to each other (conjugate via any path between them), so choosing a basepoint loses no information up to group isomorphism. But when X is **disconnected** — say, X = {a} ∪ {b}, two separate points — the fundamental groupoid has two objects and only identity morphisms, cleanly encoding the disconnection. No basepoint-based fundamental group can capture this: you'd need to pick a component.

The fundamental groupoid is not merely a notational convenience — it is categorically more natural. Any continuous map f: X → Y induces a **functor** Π₁(f): Π₁(X) → Π₁(Y), sending points to their images and homotopy classes of paths to their images. This makes Π₁ a functor from topological spaces to groupoids, and the functoriality packages the induced homomorphism on fundamental groups (at any basepoint) into a single, basepoint-free statement. The van Kampen theorem, which computes π₁ of a union of spaces, has a cleaner and more general statement at the groupoid level: Π₁(X ∪ Y) is the pushout of Π₁(X) and Π₁(Y) over Π₁(X ∩ Y) in the category of groupoids.
