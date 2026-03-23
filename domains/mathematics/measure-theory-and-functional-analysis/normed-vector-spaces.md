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
stage: expert
status: draft
---

# Normed Vector Spaces

## Core Idea
A normed vector space is a vector space V with a norm ‖·‖: V → [0,∞) satisfying positive definiteness, homogeneity, and the triangle inequality. Norms induce metrics and topologies, making analysis possible in abstract spaces.

## Questions

```yaml
- question: "A student proposes f(v) = v₁ + v₂ as a 'norm' on ℝ² (where v = (v₁, v₂)). Why does this fail?"
  type: multiple-choice
  options:
    - "It violates homogeneity: f(2v) ≠ 2f(v) in general"
    - "It violates positive definiteness: f(1, −1) = 0 but (1, −1) is not the zero vector"
    - "It violates the triangle inequality for most pairs of vectors"
    - "It is actually a valid norm — the ℓ¹ norm on ℝ²"
  answer: 1
  explanation: "f(1, −1) = 1 + (−1) = 0, yet (1, −1) is not the zero vector. A norm requires ‖v‖ = 0 only when v = 0 (positive definiteness). The fix is simple: use |v₁| + |v₂|, which IS the ℓ¹ norm. The key lesson is that signs must be removed — norms measure magnitude, not signed displacement."

- question: "A norm ‖·‖ on a vector space V automatically induces a metric. What is that metric?"
  type: multiple-choice
  options:
    - "d(u, v) = ‖u‖ + ‖v‖"
    - "d(u, v) = ‖u − v‖"
    - "d(u, v) = ‖u‖ · ‖v‖"
    - "d(u, v) = |‖u‖ − ‖v‖|"
  answer: 1
  explanation: "The natural metric is d(u, v) = ‖u − v‖ — the norm of the difference, which measures how 'far apart' u and v are. The triangle inequality for the norm directly gives the triangle inequality for this metric: d(u, w) = ‖u − w‖ = ‖(u − v) + (v − w)‖ ≤ ‖u − v‖ + ‖v − w‖ = d(u, v) + d(v, w). This is the ladder: norm → metric → topology."

- question: "In finite-dimensional vector spaces, the ℓ¹ and ℓ² norms produce different unit balls (diamond vs. circle), but they induce the same topology."
  type: true-false
  answer: true
  explanation: "In finite dimensions, all norms are equivalent: they induce the same open sets, convergent sequences, and continuous functions — only the shape of the unit ball differs. This equivalence breaks down in infinite-dimensional spaces, where different norms can yield genuinely incompatible topologies. This is why the choice of norm becomes a central concern in functional analysis."

- question: "Any metric on a vector space arises from a norm via d(u, v) = ‖u − v‖."
  type: true-false
  answer: false
  explanation: "Not every metric on a vector space comes from a norm. The discrete metric (d(u,v) = 1 if u ≠ v, 0 if u = v) is a valid metric but cannot be expressed as ‖u − v‖ for any norm — a norm-induced metric must scale with scalar multiplication, e.g. d(2u, 0) = 2d(u, 0), which the discrete metric violates. Norms induce a special subclass of metrics compatible with the vector space structure."

- question: "Explain in your own words why each of the three norm axioms — positive definiteness, homogeneity, and the triangle inequality — corresponds to a property we should demand of any reasonable notion of 'length.'"
  type: short-answer
  answer: "Positive definiteness ensures only the zero vector has zero length (nothing else is 'nowhere'). Homogeneity ensures scaling a vector scales its length proportionally — stretching an arrow by 3 triples its length. The triangle inequality ensures that a direct path is never longer than a detour: going from u to w directly can't be longer than going via v."
  explanation: "The power of these axioms is their minimality — they capture exactly the intuitive content of 'length' with nothing extra. Any function satisfying all three can be used for analysis: you can define open balls, speak of convergence, and prove theorems. Functions that fail even one axiom lead to contradictions or unintuitive behavior (e.g., a 'length' that assigns zero to non-zero vectors makes it impossible to distinguish nearby points)."
```

## Explainer

You already know that a vector space is a set where you can add elements and scale them by scalars, satisfying a list of algebraic axioms. But a vector space by itself has no notion of *size* or *distance* — there is no way to say one vector is "closer" to another, and no notion of a sequence converging. A **norm** installs exactly this structure. It is a function ‖·‖ that assigns a non-negative real number to every vector, acting as an abstract length, and it must obey three rules that any reasonable notion of length should satisfy.

The three axioms formalize what "length" means. **Positive definiteness**: ‖v‖ ≥ 0, and ‖v‖ = 0 only when v is the zero vector — the only thing with zero length is nothing. **Homogeneity** (also called absolute scalability): ‖αv‖ = |α| ‖v‖ — scaling a vector by α scales its length by |α|. This matches geometric intuition: stretching an arrow by 3 triples its length. **Triangle inequality**: ‖u + v‖ ≤ ‖u‖ + ‖v‖ — the length of a sum cannot exceed the sum of the lengths. Geometrically, this says a straight path is never longer than a path with one detour.

The power of this setup is that a norm automatically gives you a **metric**: define d(u, v) = ‖u − v‖. This is the distance between u and v, and one can verify all metric axioms from the norm axioms. With a metric in hand, you immediately inherit all of metric space topology: open balls, continuity, convergence of sequences, Cauchy sequences, and completeness. This is the ladder — vector space → norm → metric → topology — that takes you from pure algebra into analysis.

Different norms on the same space lead to genuinely different geometric intuitions, even if they are all "equivalent" in finite dimensions. The Euclidean norm ‖v‖₂ = √(v₁² + v₂² + ... + vₙ²) gives the familiar round ball. The **ℓ¹ norm** ‖v‖₁ = |v₁| + ... + |vₙ| gives a diamond-shaped unit ball. The **ℓ∞ norm** ‖v‖∞ = max|vᵢ| gives a cube. In infinite-dimensional spaces (function spaces, sequence spaces), these norms become genuinely non-equivalent and selecting the right one for a problem becomes a central concern. The normed space framework is the foundation for everything ahead in functional analysis — Banach spaces, linear operators, dual spaces — because all of those require a reliable notion of size.
