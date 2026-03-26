---
id: topological-spaces-complex-plane
title: Topology of the Complex Plane
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-plane
  type: hard
- id: open-sets-topology
  type: soft
builds-toward:
- connected-simply-connected-plane
- complex-functions-mappings
- cauchys-theorem
tags:
- topology
- open-sets
- neighborhoods
stage: advanced
status: validated
---

# Topology of the Complex Plane

## Core Idea
The complex plane inherits a metric topology from the Euclidean distance d(z, w) = |z - w|. Open sets are unions of open disks; closed sets are complements of open sets. This topology is what makes limits, continuity, and integration rigorous, and it is key for understanding domains of holomorphic functions and the structure of singularities.

## Questions

```yaml
- question: "A function f is defined on the closed disk S = {z ∈ ℂ : |z| ≤ 1}. A student claims f can be holomorphic on S because S contains every point f would ever need to evaluate. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — holomorphic functions can be defined on any set, open or closed"
    - "The closed disk is unbounded, so derivatives cannot be computed there"
    - "Boundary points of S have no open disk contained entirely within S, so the complex derivative cannot be defined there"
    - "Closed sets cannot be connected, which is required for holomorphic functions"
  answer: 2
  explanation: "Holomorphicity at a point requires the complex derivative to be defined in an entire neighborhood of that point — an open disk around it. At a boundary point of the closed disk (like z = 1), any open disk centered there extends outside S, so the derivative is not defined within the domain. The domain of a holomorphic function must be open precisely to guarantee every point has this necessary breathing room."

- question: "Which of the following subsets of ℂ is an open set?"
  type: multiple-choice
  options:
    - "The closed disk {z : |z − 2| ≤ 1}"
    - "The real axis {z : Im(z) = 0}"
    - "The unit circle {z : |z| = 1}"
    - "The right half-plane {z : Re(z) > 0}"
  answer: 3
  explanation: "The right half-plane is open: for any z with Re(z) > 0, a sufficiently small open disk around z is entirely contained in the half-plane. The closed disk includes its boundary — boundary points have no open disk lying entirely within the set. The real axis and unit circle are both 'thin' sets (1-dimensional curves in ℝ²); no 2D open disk around any point on them is contained within them."

- question: "The open disk D₁(0) = {z ∈ ℂ : |z| < 1} is both open and bounded."
  type: true-false
  answer: true
  explanation: "Both properties hold independently. The disk is open because every point inside has an open neighborhood contained entirely within it. It is bounded because it is contained in the closed disk of radius 1 centered at the origin — no point in D₁(0) has modulus greater than 1. Openness and boundedness are logically independent properties; a set can be any combination of open/closed and bounded/unbounded."

- question: "Most closed subset of ℂ is bounded."
  type: true-false
  answer: false
  explanation: "Closed and bounded are independent properties. The entire real axis {z : Im(z) = 0} is closed — it contains all its limit points and its complement is open — but it is unbounded, extending infinitely in both directions. Similarly, the entire plane ℂ is both open and closed but is unbounded. The misconception often arises from conflating 'closed' with 'compact'; compactness requires both closed and bounded in ℝⁿ."

- question: "Why must the domain of a holomorphic function be an open set rather than an arbitrary subset of ℂ?"
  type: short-answer
  answer: "The complex derivative at a point z₀ is defined as the limit of (f(z) − f(z₀))/(z − z₀) as z → z₀ from any direction. This limit must be taken over points z in the domain, so z must be able to approach z₀ freely from all directions. An open set guarantees that every point has an open disk around it contained in the domain, providing the full two-dimensional neighborhood required for the directional limit to be well-defined. Without openness, the limit might only be defined along restricted paths, which is insufficient for complex differentiability."
  explanation: "Real differentiability only requires limits along the real line (one direction). Complex differentiability requires the limit to exist and be the same from every direction in the plane — horizontally, vertically, diagonally, and all others. This is what makes complex analysis so powerful (and restrictive). The open domain condition is what ensures every point has enough surrounding points for this multi-directional limit to be meaningful."
```

## Explainer

You already know the complex plane: every complex number z = x + iy corresponds to a point (x, y) in ℝ², and the **modulus** |z| = √(x² + y²) measures its distance from the origin. The distance between two complex numbers z and w is |z − w|, which is exactly the Euclidean distance between their corresponding points in the plane. This gives ℂ a **metric** — a notion of "closeness" — and from a metric, you can build a full topology.

An **open disk** of radius r centered at z₀ is the set D_r(z₀) = {z ∈ ℂ : |z − z₀| < r}, all points strictly within distance r of z₀. A set U ⊆ ℂ is called **open** if for every point z ∈ U, there exists some r > 0 such that the entire open disk D_r(z) is contained in U — informally, every point of U has some breathing room. The entire plane ℂ and the empty set are both open; the interior of any disk is open; a half-plane like {z : Re(z) > 0} is open. A **closed** set is one whose complement is open — equivalently, a set that contains all its boundary points. The closed disk {z : |z − z₀| ≤ r} is closed; the real axis {z : Im(z) = 0} is closed.

The reason topology matters for complex analysis is that **holomorphic functions** are always defined on *open* sets, never just at a single point. When we say "f is holomorphic on D," D must be an open connected set — called a **domain**. Openness ensures that at every point of D, f has a full neighborhood in which the complex derivative is defined. The requirement that D be **connected** (cannot be split into two disjoint open pieces) ensures the function hangs together as a single analytic entity; separate components could behave completely independently. **Simply connected** — roughly, a connected domain with no holes — is even stronger and is the hypothesis needed for Cauchy's theorem to guarantee that all closed-contour integrals vanish.

Topological vocabulary also classifies singularities. If f has a singularity at z₀ (a point where f is not holomorphic), the behavior of f in every open disk around z₀ determines the singularity type — removable, pole, or essential. The concept of a **neighborhood** (any open set containing z₀) is the language that makes "local behavior near z₀" precise. Every statement like "f is bounded near z₀" or "f extends continuously to z₀" implicitly refers to some neighborhood, and the topology of ℂ is what gives those statements mathematical content.
