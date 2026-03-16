---
id: fundamental-theorem-line-integrals
title: Fundamental Theorem for Line Integrals
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: line-integrals
  type: hard
builds-toward:
- conservative-fields-potential
tags:
- fundamental-theorem
- path-independence
- potential
stage: formal-systems
status: draft
---

# Fundamental Theorem for Line Integrals

## Core Idea
If F = ∇f (F is conservative), then ∫_C F · dr = f(B) − f(A), depending only on endpoints A and B, not the path C. This extends the single-variable fundamental theorem of calculus and provides a shortcut for line integrals of conservative fields.

## Explainer

Recall from your study of line integrals that ∫_C F · dr measures the work done by a vector field F along a curve C — it depends, in general, on every detail of the path. You integrate dot products F · r'(t) dt all along the curve, weighting the field's contribution by how much the curve moves in the field's direction. For a generic vector field, changing the curve between two fixed endpoints changes the integral. But for a special class of fields, this path-dependence vanishes entirely.

A **conservative field** is a vector field F that can be written as the gradient of a scalar function: F = ∇f. The scalar function f is called a **potential function** for F. The fundamental theorem for line integrals says: if F = ∇f, then ∫_C F · dr = f(B) − f(A), where A and B are the endpoints of C. The entire integral collapses to the difference of potential values at two points — the path in between is irrelevant. This is the direct multivariable generalization of the single-variable fundamental theorem of calculus, which says ∫_a^b F'(x) dx = F(b) − F(a).

The analogy is exact. In one dimension, integrating a derivative over an interval gives the net change in the function. In multiple dimensions, integrating a gradient field (F = ∇f is the gradient of f) over a curve gives the net change in f from start to end. The intermediate behavior of the curve — whether it meanders, loops, or takes a straight line — does not matter, because the gradient field "knows" the potential at every point, and work done is purely a bookkeeping of potential differences.

The practical consequence is **path independence**: for conservative fields, you can choose any convenient path between A and B. A loop from A back to A contributes zero work (f(A) − f(A) = 0). This is the condition for a force field to be conservative in physics — gravity and electrostatic fields are conservative, meaning the work done by gravity on a falling object depends only on the height difference, not the trajectory. Identifying whether a field is conservative (by checking if a potential function exists) is therefore the key step that determines whether this powerful shortcut applies.
