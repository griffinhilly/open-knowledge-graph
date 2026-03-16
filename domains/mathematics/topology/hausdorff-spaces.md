---
id: hausdorff-spaces
title: Hausdorff Spaces
domain: mathematics
course: topology
prerequisites:
- id: separation-axioms-t0-t1-t2
  type: hard
builds-toward:
- compactness-hausdorff-spaces
- metrization-theorems
tags:
- hausdorff
- t2-axiom
- separated
stage: advanced
status: draft
---

# Hausdorff Spaces

## Core Idea
A Hausdorff space (T₂ space) requires any two distinct points to have disjoint open neighborhoods. This is the most commonly studied separation axiom and appears throughout analysis and topology. In Hausdorff spaces, sequences have unique limits, singleton sets are closed, and compact subsets are closed.

## Explainer

From your study of separation axioms, you know there is a hierarchy of ways a topological space can "separate" its points: T₀ asks that for any two distinct points, at least one has a neighborhood not containing the other; T₁ asks that each point can be separated from every other point by some open set; T₂ — the **Hausdorff condition** — asks for something stronger: any two distinct points have *disjoint* open neighborhoods. This is the condition that makes topology behave like the geometry you already know from analysis on ℝ.

The Hausdorff condition can be stated visually: if x ≠ y, you can "separate" them with open sets — find U ∋ x and V ∋ y such that U ∩ V = ∅. Every metric space is Hausdorff: given distinct points x and y at distance d > 0, take open balls of radius d/2 around each. These balls are disjoint by the triangle inequality. So all of the spaces from analysis — ℝⁿ, function spaces with norms, manifolds — are automatically Hausdorff. The Hausdorff condition is interesting precisely for spaces that might fail it, such as certain spaces in algebraic geometry or the quotient topologies that arise when you identify points together carelessly.

The most important consequence of the Hausdorff condition in analysis is **uniqueness of limits**. In a non-Hausdorff space, a sequence can converge to two different points simultaneously — because there is no way to isolate the two limit points from each other. In a Hausdorff space, this cannot happen: if x_n → x and x_n → y, then x = y. The proof uses the Hausdorff condition directly: if x ≠ y, take disjoint neighborhoods U of x and V of y; eventually the sequence must lie entirely in U (by convergence to x) and eventually entirely in V (by convergence to y), but U ∩ V = ∅, a contradiction. From this it follows that singletons {x} are closed in any T₁ space, and in particular in any Hausdorff space.

A crucial theorem linking Hausdorff spaces to compactness is: **in a Hausdorff space, every compact subset is closed**. The proof constructs, for any point y outside a compact set K, a neighborhood of y disjoint from K — using the Hausdorff condition to separate y from each point of K, then using compactness to extract a finite subcover. This interplay between Hausdorff and compactness is one of the central engines of topology: it explains why compact Hausdorff spaces have such clean and complete theory, and it sets up the study of compactification and metrization theorems you will encounter next.
