---
id: greens-theorem
title: Green's Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: line-integrals-vector-fields
  type: hard
- id: double-integrals-cartesian
  type: hard
builds-toward:
- stokes-theorem
- divergence-theorem
tags:
- greens-theorem
- circulation
stage: formal-systems
status: draft
---

# Green's Theorem

## Core Idea
Green's theorem: ∮_C (P dx + Q dy) = ∬_D (Q_x - P_y) dA. This relates line integrals around a closed curve to a double integral of curl over the region, converting circulation to an area integral.

## Questions

```yaml
- question: "Green's theorem converts a line integral around a closed curve C into what type of integral?"
  type: multiple-choice
  options:
    - "A surface integral over a 3D region bounded by C"
    - "A double integral of the 2D curl (Q_x − P_y) over the region D enclosed by C"
    - "A triple integral over a volume"
    - "A line integral along a different path connecting the endpoints of C"
  answer: 1
  explanation: "Green's theorem states ∮_C (P dx + Q dy) = ∬_D (Q_x − P_y) dA. It converts circulation around a closed boundary into a double integral of the local rotation rate (2D curl) over the enclosed region. This is a special case of the general principle: an integral over a region equals an integral of a related quantity over its boundary."

- question: "A vector field F = (P, Q) satisfies Q_x − P_y = 0 everywhere in a simply connected region D. What does Green's theorem imply about the line integral of F around any closed curve C enclosing a subset of D?"
  type: multiple-choice
  options:
    - "The line integral depends on the shape and size of C"
    - "The line integral equals zero"
    - "The line integral equals the area of the region enclosed by C"
    - "Green's theorem cannot be applied when the curl is zero"
  answer: 1
  explanation: "Green's theorem gives ∮_C F·dr = ∬_D (Q_x − P_y) dA. If Q_x − P_y = 0 everywhere, the double integral is zero regardless of the shape or size of C. A field with zero 2D curl everywhere is called irrotational or conservative, and path independence (and zero circulation) follows directly from Green's theorem."

- question: "Green's theorem says the circulation around a closed curve is determined entirely by the behavior of the vector field on the boundary curve — the interior is irrelevant."
  type: true-false
  answer: false
  explanation: "This is backwards. Green's theorem says the OPPOSITE: the circulation on the boundary is *determined by* the double integral of the curl over the INTERIOR. The boundary behavior is the consequence of what happens inside. This is the theorem's deep insight: you can replace a hard boundary integral with an area integral, or vice versa, precisely because interior and boundary behavior are linked."

- question: "When a region D is tiled with tiny squares, adjacent squares share interior edges where their line integral contributions cancel, leaving only the outer boundary — this geometric cancellation is why Green's theorem works."
  type: true-false
  answer: true
  explanation: "This is the key intuition. Each tiny square's boundary integral captures local circulation (Q_x − P_y multiplied by the tiny area). When you stitch adjacent squares together, the shared interior edge is traversed once clockwise by one square and once counterclockwise by the other — they cancel. Only the outermost boundary has unpaired edges. Summing over all squares gives the full boundary integral, with the double integral of curl as the running total."

- question: "Explain in your own words why Green's theorem connects a line integral on a boundary to a double integral over the interior. What is the geometric insight?"
  type: short-answer
  answer: "The geometric insight is cancellation. Tile the enclosed region D with tiny squares. Each square's boundary contributes a small circulation (proportional to the local curl times the tiny area). Adjacent squares share edges, but they traverse them in opposite directions — those contributions cancel perfectly. What remains uncanceled is only the outer boundary. So the sum of local circulations (the double integral of curl) equals the circulation around the full outer boundary (the line integral). The interior completely cancels out; only the boundary survives."
  explanation: "This cancellation argument is the same underlying logic as in the Fundamental Theorem of Calculus (interior values cancel, boundary values survive), Stokes' theorem, and the Divergence theorem. Recognizing this 'interior cancels, boundary survives' structure is the key to all the major theorems of vector calculus."
```

## Explainer

From line integrals over vector fields and double integrals, you have two seemingly unrelated tools. Line integrals measure cumulative effect along a path — work done by a force, circulation of a fluid. Double integrals sum quantities spread over a 2D region. **Green's theorem** bridges them: it says the circulation of a vector field around a closed curve equals the double integral of a local rotation quantity over the enclosed region. This is one of the deepest results in multivariable calculus, and its key intuition is that **boundary behavior is determined by interior behavior**.

To see why, think of the region D partitioned into many tiny squares. Around each tiny square, the line integral of the field measures the local circulation. When you tile adjacent squares together, the shared interior edges cancel — the contribution along an edge from one square runs in the opposite direction from the neighboring square. What survives is only the outer boundary: the entire interior cancels, leaving the circulation around the full perimeter C. So summing local circulation over all tiny cells gives exactly the boundary circulation. The double integral captures this summation, and the quantity being summed is the **2D curl** Q_x − P_y — the local rotation rate of the vector field at each point.

The quantity Q_x − P_y has a concrete meaning. If F = (P, Q) is a vector field representing fluid velocity, then Q_x − P_y measures how much the field rotates (curls) at a given point: Q_x measures how Q increases in the x-direction, and P_y measures how P increases in the y-direction. Their difference captures net rotation. A field with Q_x − P_y = 0 everywhere has no local rotation; it is called **irrotational** or **conservative**, and the line integral around any closed loop in the region is zero. Green's theorem makes this precise: ∮_C F·dr = ∬_D (curl F) dA, and if curl F = 0 everywhere, the right side is 0.

Green's theorem is a 2D special case of a family of theorems — all sharing the same deep structure: an integral over a region equals an integral over its boundary. The 3D versions are Stokes' theorem (relating surface integrals of curl to boundary line integrals) and the Divergence theorem (relating volume integrals of divergence to surface integrals). Learning to recognize this structure — "integrate something over the interior ↔ integrate something related on the boundary" — is the key to all the major theorems of vector calculus.
