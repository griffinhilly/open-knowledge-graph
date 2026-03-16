---
id: neighborhoods-in-topology
title: Neighborhoods and Local Properties
domain: mathematics
course: topology
prerequisites:
- id: basis-for-a-topology
  type: hard
builds-toward:
- limit-points-convergence-topology
- continuity-topological-spaces
tags:
- neighborhoods
- local-properties
- topology
stage: advanced
status: draft
---

# Neighborhoods and Local Properties

## Core Idea
A neighborhood of a point x is any set containing an open set that contains x. Neighborhoods allow us to study local behavior in a topological space—properties that depend only on what happens near a particular point, not on the space globally. Convergence and continuity are fundamentally local concepts expressed via neighborhoods.

## Explainer

The concept of a **neighborhood** formalizes the intuitive idea of "near a point." You already know that a topology on a set X is a collection of open sets satisfying certain axioms, and that a basis generates all open sets. A neighborhood of a point x is simply any set N that contains some open set U with x ∈ U ⊆ N. The neighborhood need not itself be open — what matters is that there is an open "cushion" around x sitting inside N. In metric spaces, the familiar open balls B(x, ε) are the prototypical neighborhoods, and every metric topology can be understood entirely in terms of them.

Why introduce neighborhoods at all, rather than working directly with open sets? Because many key concepts in topology are fundamentally **local** — they describe behavior near a single point, not behavior across the whole space. Convergence is the clearest example. A sequence (x₁, x₂, …) converges to x if every neighborhood of x eventually contains all terms of the sequence: for every N containing an open set around x, there exists some index M such that xₙ ∈ N for all n > M. This is exactly the topological generalization of the familiar ε-N definition from metric spaces, where ε-balls play the role of neighborhoods.

Continuity at a point has an equally clean neighborhood formulation. A function f: X → Y is continuous at x if for every neighborhood V of f(x) in Y, there exists a neighborhood U of x in X such that f(U) ⊆ V — the image of a small region around x lands inside any prescribed region around f(x). This phrasing makes the local character of continuity explicit: whether f is continuous at x depends only on what f does near x, not on the global structure of X or Y.

Because a basis generates all opens, it suffices to check neighborhoods against **basis elements**. If B is a basis for the topology on X, then N is a neighborhood of x if and only if some basis element B ∈ B with x ∈ B is contained in N. This means neighborhood arguments can often be reduced to checking finitely describable basic sets — a practical simplification that carries through to all the local concepts built on neighborhoods.
