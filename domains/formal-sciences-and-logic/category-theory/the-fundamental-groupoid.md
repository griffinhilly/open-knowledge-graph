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
stage: advanced
status: draft
---

# The Fundamental Groupoid of a Space

## Core Idea
The fundamental groupoid of a topological space has points as objects and homotopy classes of paths as morphisms, with composition given by path concatenation. Unlike the fundamental group (which depends on a basepoint choice), the fundamental groupoid is base-point-free and captures the full homotopy-theoretic information of the space. It provides a more natural and categorical framework for studying connectivity.

## How It's Best Learned
Compute the fundamental groupoid of familiar spaces: the circle, the plane, a figure-eight. Verify that morphisms are invertible and explore how groupoid structure reflects topological properties. Understand the relationship between the fundamental groupoid and fundamental groups at various basepoints.

## Common Misconceptions
The fundamental groupoid is not the same as the fundamental group; it encodes information at all points simultaneously. The automorphism group at a point is the fundamental group at that basepoint, but the groupoid structure includes much more.

## Explainer

You know that a **groupoid** is a category in which every morphism is invertible. Objects can be many, not just one, so a groupoid generalizes both groups (one object, all morphisms invertible) and sets (many objects, only identity morphisms). The **fundamental groupoid** Π₁(X) of a topological space X is the canonical example of a groupoid arising in nature. Its objects are the points of X; its morphisms from point x to point y are **homotopy classes of paths** from x to y — continuous curves γ: [0,1] → X with γ(0) = x and γ(1) = y, where two paths are identified if one can be continuously deformed into the other while keeping the endpoints fixed.

Composition of morphisms is **path concatenation**: given a path from x to y and a path from y to z, you travel first along one, then the other, reparametrized to the unit interval. The identity morphism at x is the constant path that stays at x. The inverse of a path γ is the **reversed path** γ⁻¹(t) = γ(1−t), which traces the same route backwards. Checking the groupoid axioms reduces to standard facts in homotopy theory: concatenation is associative up to homotopy, the constant path is a homotopy identity, and reversing a path gives a homotopy inverse. Every morphism is invertible — that is the groupoid property — because you can always walk backwards.

The **fundamental group** π₁(X, x₀) based at a chosen point x₀ is the automorphism group Aut_{Π₁(X)}(x₀) in the fundamental groupoid — the collection of all homotopy classes of *loops* at x₀ (paths where γ(0) = γ(1) = x₀). The groupoid sees all basepoints simultaneously. When X is **path-connected**, all the automorphism groups Aut(x) are isomorphic to each other (conjugate via any path between them), so choosing a basepoint loses no information up to group isomorphism. But when X is **disconnected** — say, X = {a} ∪ {b}, two separate points — the fundamental groupoid has two objects and only identity morphisms, cleanly encoding the disconnection. No basepoint-based fundamental group can capture this: you'd need to pick a component.

The fundamental groupoid is not merely a notational convenience — it is categorically more natural. Any continuous map f: X → Y induces a **functor** Π₁(f): Π₁(X) → Π₁(Y), sending points to their images and homotopy classes of paths to their images. This makes Π₁ a functor from topological spaces to groupoids, and the functoriality packages the induced homomorphism on fundamental groups (at any basepoint) into a single, basepoint-free statement. The van Kampen theorem, which computes π₁ of a union of spaces, has a cleaner and more general statement at the groupoid level: Π₁(X ∪ Y) is the pushout of Π₁(X) and Π₁(Y) over Π₁(X ∩ Y) in the category of groupoids.
