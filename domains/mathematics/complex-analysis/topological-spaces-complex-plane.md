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
status: draft
---

# Topology of the Complex Plane

## Core Idea
The complex plane inherits a metric topology from the Euclidean distance d(z, w) = |z - w|. Open sets are unions of open disks; closed sets are complements of open sets. This topology is what makes limits, continuity, and integration rigorous, and it is key for understanding domains of holomorphic functions and the structure of singularities.

## Explainer

You already know the complex plane: every complex number z = x + iy corresponds to a point (x, y) in ℝ², and the **modulus** |z| = √(x² + y²) measures its distance from the origin. The distance between two complex numbers z and w is |z − w|, which is exactly the Euclidean distance between their corresponding points in the plane. This gives ℂ a **metric** — a notion of "closeness" — and from a metric, you can build a full topology.

An **open disk** of radius r centered at z₀ is the set D_r(z₀) = {z ∈ ℂ : |z − z₀| < r}, all points strictly within distance r of z₀. A set U ⊆ ℂ is called **open** if for every point z ∈ U, there exists some r > 0 such that the entire open disk D_r(z) is contained in U — informally, every point of U has some breathing room. The entire plane ℂ and the empty set are both open; the interior of any disk is open; a half-plane like {z : Re(z) > 0} is open. A **closed** set is one whose complement is open — equivalently, a set that contains all its boundary points. The closed disk {z : |z − z₀| ≤ r} is closed; the real axis {z : Im(z) = 0} is closed.

The reason topology matters for complex analysis is that **holomorphic functions** are always defined on *open* sets, never just at a single point. When we say "f is holomorphic on D," D must be an open connected set — called a **domain**. Openness ensures that at every point of D, f has a full neighborhood in which the complex derivative is defined. The requirement that D be **connected** (cannot be split into two disjoint open pieces) ensures the function hangs together as a single analytic entity; separate components could behave completely independently. **Simply connected** — roughly, a connected domain with no holes — is even stronger and is the hypothesis needed for Cauchy's theorem to guarantee that all closed-contour integrals vanish.

Topological vocabulary also classifies singularities. If f has a singularity at z₀ (a point where f is not holomorphic), the behavior of f in every open disk around z₀ determines the singularity type — removable, pole, or essential. The concept of a **neighborhood** (any open set containing z₀) is the language that makes "local behavior near z₀" precise. Every statement like "f is bounded near z₀" or "f extends continuously to z₀" implicitly refers to some neighborhood, and the topology of ℂ is what gives those statements mathematical content.
