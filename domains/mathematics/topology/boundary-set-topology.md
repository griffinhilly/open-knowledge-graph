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
stage: formal-systems
status: validated
---

# Boundary of Sets

## Core Idea
The boundary ∂A = cl(A) \ int(A) consists of points where every neighborhood intersects both A and its complement. Equivalently, ∂A = cl(A) ∩ cl(X \ A). A set is closed iff ∂A ⊆ A; it is open iff ∂A ∩ A = ∅. Boundaries capture where sets 'edge' into their complement.

## Questions

```yaml
- question: "Let A = (0, 1) be the open interval in ℝ with the standard topology. Which statement about its boundary ∂A is correct?"
  type: multiple-choice
  options:
    - "∂A = ∅, because A is open and open sets have no boundary"
    - "∂A = {0, 1}, because these points are in cl(A) but not in int(A)"
    - "∂A = (0, 1), because every point of A is a limit point and thus a boundary point"
    - "∂A = [0, 1], because the closure of A is the full closed interval"
  answer: 1
  explanation: "The interior of (0,1) is (0,1) itself (every point has an open neighborhood entirely inside A). The closure of (0,1) is [0,1] (the endpoints are limit points not in A). The boundary is cl(A) \\ int(A) = [0,1] \\ (0,1) = {0, 1}. The endpoints are exactly the boundary points: every neighborhood of 0 or 1 reaches into both (0,1) and its complement. Option A is the key misconception — open sets *contain none* of their boundary points, but that doesn't mean the boundary is empty."

- question: "A set U in a topological space is open, meaning ∂U ∩ U = ∅. What does this tell us about where the boundary points of U are located?"
  type: multiple-choice
  options:
    - "U has no boundary points at all"
    - "The boundary points of U lie entirely in the complement of U"
    - "U is also closed, since open sets in Hausdorff spaces are closed"
    - "U contains all of its limit points and is therefore complete"
  answer: 1
  explanation: "∂U ∩ U = ∅ means the boundary and U are disjoint — boundary points exist but are not in U. Since every point is either in U or not in U, and ∂U misses U entirely, the boundary points must lie in the complement X \\ U. This makes sense geometrically: a boundary point of U has neighborhoods that reach into both U and its complement, so it can't be an interior point of U and therefore can't be in an open U."

- question: "The open disk {(x,y) : x²+y² < 1} and the closed disk {(x,y) : x²+y² ≤ 1} have different boundaries."
  type: true-false
  answer: false
  explanation: "Both have the same boundary: the unit circle {(x,y) : x²+y² = 1}. For the open disk B: int(B) = B, cl(B) = closed disk, so ∂B = cl(B) \\ int(B) = unit circle. For the closed disk A: int(A) = open disk, cl(A) = A itself, so ∂A = A \\ open disk = unit circle. The boundary is the same object — it separates both from their complement. What differs is whether the set *contains* its boundary: A does (it's closed), B does not (it's open)."

- question: "A point p is a boundary point of A if and only if every open neighborhood of p intersects both A and its complement."
  type: true-false
  answer: true
  explanation: "This is the equivalent characterization ∂A = cl(A) ∩ cl(X \\ A) in neighborhood language. A point is in cl(A) iff every neighborhood hits A; it is in cl(X \\ A) iff every neighborhood hits the complement. A boundary point must satisfy both — it is on the 'edge' in the strongest sense, with no neighborhood small enough to land entirely on one side. This characterization is often more intuitive than the formula ∂A = cl(A) \\ int(A) and is equivalent to it."

- question: "Explain why the open disk and the closed disk have the same boundary. What does this reveal about the relationship between a set and its boundary?"
  type: short-answer
  answer: "The boundary ∂A = cl(A) ∩ cl(X \\ A) depends on where A meets its complement, not on whether A includes those meeting points. For both disks, the closure includes the unit circle and the closure of the complement also includes the unit circle — so the intersection is the unit circle in both cases. The difference is that the closed disk *contains* its boundary (so it is closed) while the open disk *excludes* its boundary (so it is open). The boundary itself is a neutral separator that belongs intrinsically to neither set."
  explanation: "The deeper insight is that a set's boundary is determined by the topology of the surrounding space and the structure of the set, not by whether the set 'claims' the boundary points. The same circle separates inside from outside regardless of which side of the line you draw. A closed set is precisely one that absorbs its boundary; an open set is precisely one that rejects it. This is why clopen sets (both open and closed) have empty boundaries — there are no transitional points at all."
```

## Explainer

From your study of the interior and closure operators, you know that int(A) is the "most open" subset of A — all the points with an open neighborhood entirely inside A — and that cl(A) is the "most closed" superset — all the points that cannot be separated from A by any open set. The **boundary** ∂A lives in the gap between them: it is what cl(A) has that int(A) does not. Formally, ∂A = cl(A) \ int(A), the set of points that are in the closure but not the interior.

The geometric intuition is sharp: a boundary point is one where you cannot take a neighborhood small enough to be entirely inside A, yet also cannot take one small enough to avoid A entirely. Every neighborhood of a boundary point straddles both sides — it intersects A, and it intersects the complement X \ A. This is why the equivalent formula ∂A = cl(A) ∩ cl(X \ A) is so illuminating: boundary points are simultaneously "on the boundary" of A and "on the boundary" of its complement. They are genuinely on the edge.

The classic example is the closed disk A = {(x, y) : x² + y² ≤ 1} in the plane. Its interior is the open disk (strict inequality), and its closure is itself. The boundary ∂A is the circle {(x, y) : x² + y² = 1} — the unit circle, exactly where the inside meets the outside. Every point on the circle has neighborhoods that reach both into the disk and out of it. For the open disk B = {(x, y) : x² + y² < 1}, the interior is again B itself, the closure is the closed disk, so ∂B = the same unit circle. The boundary is the same regardless of whether you start with the open or closed disk — it belongs to neither intrinsically but separates both.

The relationship between a set and its boundary reveals whether the set is open or closed. A **closed** set contains its entire boundary: ∂A ⊆ A. A closed set cannot "reject" a boundary point because closure requires containing all limit points, and boundary points are limit points of A. An **open** set contains none of its boundary: ∂A ∩ A = ∅. If a point is on the boundary, it has no neighborhood entirely inside A, so it fails the definition of an interior point and thus cannot be in an open set. A set is clopen (both open and closed) precisely when it has an empty boundary, meaning there are no transitional points at all. In a connected space, only ∅ and X itself are clopen, which is why the existence of a nonempty proper clopen subset is the definition of disconnectedness.
