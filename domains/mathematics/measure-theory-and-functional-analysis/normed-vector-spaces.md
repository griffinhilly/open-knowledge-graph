---
id: normed-vector-spaces
title: Normed Vector Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: vector-spaces
  type: hard
builds-toward:
- banach-spaces-definition
tags:
- functional-analysis
- normed-spaces
stage: abstract-reasoning
status: draft
---

# Normed Vector Spaces

## Core Idea
A normed vector space is a vector space V with a norm ‖·‖: V → [0,∞) satisfying positive definiteness, homogeneity, and the triangle inequality. Norms induce metrics and topologies, making analysis possible in abstract spaces.

## Explainer

You already know that a vector space is a set where you can add elements and scale them by scalars, satisfying a list of algebraic axioms. But a vector space by itself has no notion of *size* or *distance* — there is no way to say one vector is "closer" to another, and no notion of a sequence converging. A **norm** installs exactly this structure. It is a function ‖·‖ that assigns a non-negative real number to every vector, acting as an abstract length, and it must obey three rules that any reasonable notion of length should satisfy.

The three axioms formalize what "length" means. **Positive definiteness**: ‖v‖ ≥ 0, and ‖v‖ = 0 only when v is the zero vector — the only thing with zero length is nothing. **Homogeneity** (also called absolute scalability): ‖αv‖ = |α| ‖v‖ — scaling a vector by α scales its length by |α|. This matches geometric intuition: stretching an arrow by 3 triples its length. **Triangle inequality**: ‖u + v‖ ≤ ‖u‖ + ‖v‖ — the length of a sum cannot exceed the sum of the lengths. Geometrically, this says a straight path is never longer than a path with one detour.

The power of this setup is that a norm automatically gives you a **metric**: define d(u, v) = ‖u − v‖. This is the distance between u and v, and one can verify all metric axioms from the norm axioms. With a metric in hand, you immediately inherit all of metric space topology: open balls, continuity, convergence of sequences, Cauchy sequences, and completeness. This is the ladder — vector space → norm → metric → topology — that takes you from pure algebra into analysis.

Different norms on the same space lead to genuinely different geometric intuitions, even if they are all "equivalent" in finite dimensions. The Euclidean norm ‖v‖₂ = √(v₁² + v₂² + ... + vₙ²) gives the familiar round ball. The **ℓ¹ norm** ‖v‖₁ = |v₁| + ... + |vₙ| gives a diamond-shaped unit ball. The **ℓ∞ norm** ‖v‖∞ = max|vᵢ| gives a cube. In infinite-dimensional spaces (function spaces, sequence spaces), these norms become genuinely non-equivalent and selecting the right one for a problem becomes a central concern. The normed space framework is the foundation for everything ahead in functional analysis — Banach spaces, linear operators, dual spaces — because all of those require a reliable notion of size.
