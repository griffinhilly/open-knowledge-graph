---
id: work-circulation
title: Work and Circulation
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: line-integrals-vector-fields
  type: hard
builds-toward:
- greens-theorem
- stokes-theorem
tags:
- work
- circulation
stage: formal-systems
status: draft
---

# Work and Circulation

## Core Idea
Work done by force F moving along curve C: W = ∫_C F · dr. For a closed curve, ∮_C F · dr is circulation (net rotation). Circulation = 0 for conservative fields.

## Questions

```yaml
- question: "A vector field F has nonzero circulation ∮_C F · dr around some closed loop C. What can you conclude?"
  type: multiple-choice
  options:
    - "F must be undefined at some point inside the loop"
    - "F cannot be expressed as the gradient of any scalar potential function"
    - "F has constant magnitude throughout the enclosed region"
    - "The work done by F along any open path in the region is zero"
  answer: 1
  explanation: "For a conservative field F = ∇f, the work integral depends only on endpoints: ∫_C F · dr = f(end) − f(start). Around any closed loop, start = end, so circulation = f(start) − f(start) = 0. Nonzero circulation therefore proves the field is not conservative — no scalar potential can exist. Option A is tempting (Stokes' theorem relates singularities to circulation in specific cases) but nonzero circulation alone doesn't require a singularity inside; it simply rules out conservativeness."

- question: "A particle moves from point P to point Q along two different paths in a vector field F. The work done is 10 J on the first path and 7 J on the second. What does this imply?"
  type: multiple-choice
  options:
    - "F is conservative but the particle moved faster on one path, changing the work done"
    - "F is conservative, and f(Q) − f(P) = 10 J along the first path and 7 J along the second"
    - "F is not conservative — work is path-dependent, so no scalar potential exists for F"
    - "The particle must have moved in a closed loop on one of the paths"
  answer: 2
  explanation: "Path independence of work is the defining property of conservative fields. If F = ∇f, the work from P to Q must equal f(Q) − f(P) regardless of which path is taken — any two paths give the same answer. Different work values (10 J vs. 7 J) for the same endpoints proves the work is path-dependent, which proves F is not conservative. Options A and B misunderstand conservation: for conservative fields, speed and path shape are irrelevant — only endpoints matter."

- question: "For a conservative vector field, the circulation around any closed curve is zero."
  type: true-false
  answer: true
  explanation: "This follows directly from the Fundamental Theorem of Line Integrals: if F = ∇f, then ∫_C F · dr = f(end) − f(start). For a closed curve, the endpoint is the same as the starting point, so the integral equals f(start) − f(start) = 0. Zero circulation is therefore a necessary consequence of conservativeness. (It is also sufficient under appropriate conditions, which Green's theorem makes precise.)"

- question: "The work done by a conservative force field along a path depends on the length and shape of that path."
  type: true-false
  answer: false
  explanation: "This is precisely what 'conservative' means: work depends only on the starting and ending points, never on the path connecting them. ∫_C ∇f · dr = f(end) − f(start) — a formula with no reference to the path. A longer, curving path gives the same work as a straight-line shortcut between the same two points. Gravitational and electrostatic force fields are conservative for this reason: the energy gained or lost depends only on the height difference or potential difference, not on the route taken."

- question: "Explain why nonzero circulation around a closed loop proves that a vector field is not conservative."
  type: short-answer
  answer: "If F were conservative (F = ∇f), the work integral around any closed loop would equal f(end) − f(start) = f(start) − f(start) = 0. A nonzero circulation value means the integral around the closed loop is not zero, which contradicts the requirement for a conservative field. Therefore the field cannot have a scalar potential, and is not conservative."
  explanation: "The argument is a proof by contradiction: assume conservativeness → circulation = 0. Contrapositive: circulation ≠ 0 → not conservative. This is exactly why circulation is the diagnostic tool for non-conservativeness, and why Green's theorem (which equates circulation to an area integral of the curl) is so powerful — curl measures how much the field 'rotates' locally, and nonzero curl anywhere inside a loop produces nonzero circulation around it."
```

## Explainer

From line integrals over vector fields you know that ∫_C **F** · d**r** accumulates the dot product of a vector field **F** with the tangent direction of a curve C. Physically, when **F** is a force field, this integral measures **work** — the total energy transferred by the force as a particle moves along C. The dot product **F** · d**r** captures the key idea: only the component of force *along* the direction of motion contributes to work. A force perpendicular to motion does zero work; a force opposing motion does negative work.

To evaluate ∫_C **F** · d**r**, parametrize the curve as **r**(t) for t ∈ [a, b]. Then d**r** = **r**'(t) dt and the integral becomes ∫_a^b **F**(**r**(t)) · **r**'(t) dt — a standard single-variable integral. The result depends in general on the curve C, not just its endpoints. If you take a different path from the same start to the same end, you may get a different value of work. This path-dependence is the generic situation.

**Circulation** is the line integral around a *closed* curve: ∮_C **F** · d**r**. Think of C as a loop. Circulation measures the net tendency of the field to push fluid (or a particle) around the loop — the net "spinning" effect. Imagine a water wheel placed in a stream: if the current flows preferentially around the wheel in one direction, the circulation around a loop encircling the wheel will be nonzero. Circulation has a sign: positive if the field tends to push counterclockwise around C (by convention), negative for clockwise.

The crucial special case is **conservative fields**. A field **F** is conservative if **F** = ∇f for some scalar potential f. For conservative fields, the work integral depends only on the endpoints: ∫_C **F** · d**r** = f(end) − f(start). This is the multivariable Fundamental Theorem of Calculus. As an immediate consequence, circulation around any closed loop is zero — you return to the starting point and the potential difference is f(start) − f(start) = 0. Non-zero circulation is therefore a signature of a non-conservative field. Green's theorem, which you will study next, quantifies this precisely: it relates circulation around a closed curve to the "curl" of the field over the enclosed region.
