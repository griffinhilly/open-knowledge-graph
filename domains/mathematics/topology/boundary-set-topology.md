---
id: boundary-set-topology
title: Boundary of Sets
domain: mathematics
course: topology
prerequisites:
- id: interior-operator-topology
  type: hard
- id: closure-operator-topology
  type: hard
tags:
- boundary
- operators
stage: abstract-reasoning
status: draft
---

# Boundary of Sets

## Core Idea
The boundary ∂A = cl(A) \ int(A) consists of points where every neighborhood intersects both A and its complement. Equivalently, ∂A = cl(A) ∩ cl(X \ A). A set is closed iff ∂A ⊆ A; it is open iff ∂A ∩ A = ∅. Boundaries capture where sets 'edge' into their complement.

## Explainer

From your study of the interior and closure operators, you know that int(A) is the "most open" subset of A — all the points with an open neighborhood entirely inside A — and that cl(A) is the "most closed" superset — all the points that cannot be separated from A by any open set. The **boundary** ∂A lives in the gap between them: it is what cl(A) has that int(A) does not. Formally, ∂A = cl(A) \ int(A), the set of points that are in the closure but not the interior.

The geometric intuition is sharp: a boundary point is one where you cannot take a neighborhood small enough to be entirely inside A, yet also cannot take one small enough to avoid A entirely. Every neighborhood of a boundary point straddles both sides — it intersects A, and it intersects the complement X \ A. This is why the equivalent formula ∂A = cl(A) ∩ cl(X \ A) is so illuminating: boundary points are simultaneously "on the boundary" of A and "on the boundary" of its complement. They are genuinely on the edge.

The classic example is the closed disk A = {(x, y) : x² + y² ≤ 1} in the plane. Its interior is the open disk (strict inequality), and its closure is itself. The boundary ∂A is the circle {(x, y) : x² + y² = 1} — the unit circle, exactly where the inside meets the outside. Every point on the circle has neighborhoods that reach both into the disk and out of it. For the open disk B = {(x, y) : x² + y² < 1}, the interior is again B itself, the closure is the closed disk, so ∂B = the same unit circle. The boundary is the same regardless of whether you start with the open or closed disk — it belongs to neither intrinsically but separates both.

The relationship between a set and its boundary reveals whether the set is open or closed. A **closed** set contains its entire boundary: ∂A ⊆ A. A closed set cannot "reject" a boundary point because closure requires containing all limit points, and boundary points are limit points of A. An **open** set contains none of its boundary: ∂A ∩ A = ∅. If a point is on the boundary, it has no neighborhood entirely inside A, so it fails the definition of an interior point and thus cannot be in an open set. A set is clopen (both open and closed) precisely when it has an empty boundary, meaning there are no transitional points at all. In a connected space, only ∅ and X itself are clopen, which is why the existence of a nonempty proper clopen subset is the definition of disconnectedness.
