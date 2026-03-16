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

## Explainer

From line integrals over vector fields you know that ∫_C **F** · d**r** accumulates the dot product of a vector field **F** with the tangent direction of a curve C. Physically, when **F** is a force field, this integral measures **work** — the total energy transferred by the force as a particle moves along C. The dot product **F** · d**r** captures the key idea: only the component of force *along* the direction of motion contributes to work. A force perpendicular to motion does zero work; a force opposing motion does negative work.

To evaluate ∫_C **F** · d**r**, parametrize the curve as **r**(t) for t ∈ [a, b]. Then d**r** = **r**'(t) dt and the integral becomes ∫_a^b **F**(**r**(t)) · **r**'(t) dt — a standard single-variable integral. The result depends in general on the curve C, not just its endpoints. If you take a different path from the same start to the same end, you may get a different value of work. This path-dependence is the generic situation.

**Circulation** is the line integral around a *closed* curve: ∮_C **F** · d**r**. Think of C as a loop. Circulation measures the net tendency of the field to push fluid (or a particle) around the loop — the net "spinning" effect. Imagine a water wheel placed in a stream: if the current flows preferentially around the wheel in one direction, the circulation around a loop encircling the wheel will be nonzero. Circulation has a sign: positive if the field tends to push counterclockwise around C (by convention), negative for clockwise.

The crucial special case is **conservative fields**. A field **F** is conservative if **F** = ∇f for some scalar potential f. For conservative fields, the work integral depends only on the endpoints: ∫_C **F** · d**r** = f(end) − f(start). This is the multivariable Fundamental Theorem of Calculus. As an immediate consequence, circulation around any closed loop is zero — you return to the starting point and the potential difference is f(start) − f(start) = 0. Non-zero circulation is therefore a signature of a non-conservative field. Green's theorem, which you will study next, quantifies this precisely: it relates circulation around a closed curve to the "curl" of the field over the enclosed region.
