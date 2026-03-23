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
status: validated
---

# Fundamental Theorem for Line Integrals

## Core Idea
If F = ∇f (F is conservative), then ∫_C F · dr = f(B) − f(A), depending only on endpoints A and B, not the path C. This extends the single-variable fundamental theorem of calculus and provides a shortcut for line integrals of conservative fields.

## Questions

```yaml
- question: "A particle moves from point A to point B through a vector field F along three different paths. The work done is 7 J, 7 J, and 19 J respectively. What does this tell you about F?"
  type: multiple-choice
  options:
    - "F is conservative — two of the three paths agree"
    - "F is definitely not conservative, since at least one path gives a different value"
    - "F might be conservative; more paths must be tested to be certain"
    - "F is conservative only along the paths that give 7 J"
  answer: 1
  explanation: "For a conservative field, the line integral depends only on the endpoints — every path from A to B must give the same value. A single discrepancy (19 J ≠ 7 J) proves the field is not conservative. There is no threshold of 'most paths agree'; path independence is absolute."

- question: "You want to compute the work done by Earth's gravitational field on a satellite as it moves from low orbit to a higher orbit via a complex spiraling maneuver. The most efficient calculation strategy is:"
  type: multiple-choice
  options:
    - "Parametrize the spiral path and integrate F · dr along it"
    - "Compute the average gravitational force and multiply by path length"
    - "Use the potential energy difference U(r₂) − U(r₁), since gravity is a conservative field"
    - "Apply the virial theorem to find the average kinetic energy along the path"
  answer: 2
  explanation: "Gravity is conservative (F = ∇f where f = −GMm/r), so the fundamental theorem applies: ∫_C F · dr = f(B) − f(A). The entire path integral collapses to a difference of potential values at the two orbital radii — the spiraling route in between is irrelevant. This is the whole power of the theorem: path-independence lets you avoid computing the integral at all."

- question: "If F is a conservative vector field, then the work done by F on a particle that travels along any closed loop (returning to its starting point) is zero."
  type: true-false
  answer: true
  explanation: "This follows directly from the fundamental theorem: ∫_C F · dr = f(B) − f(A). If A = B (a closed loop), then f(B) − f(A) = 0. This is the defining property of conservative fields, and it is physically meaningful — gravity and electrostatic forces are conservative, meaning no net work is done over a closed trajectory. Non-conservative forces like friction always do negative work on a closed loop."

- question: "The fundamental theorem for line integrals states that any vector field can be integrated by evaluating its associated scalar function at the path's endpoints."
  type: true-false
  answer: false
  explanation: "Only conservative fields — those that can be written as F = ∇f for some scalar potential f — admit this shortcut. A generic vector field has no potential function, so its line integral genuinely depends on every detail of the path. The key step before applying the theorem is always: verify that F is conservative (e.g., by checking that curl F = 0 in a simply connected domain)."

- question: "Explain the analogy between the single-variable fundamental theorem of calculus and the fundamental theorem for line integrals."
  type: short-answer
  answer: "In one variable, ∫_a^b F'(x) dx = F(b) − F(a): integrating a derivative over an interval gives the net change in the function. In multiple dimensions, if F = ∇f (F is the gradient of f), then ∫_C F · dr = f(B) − f(A): integrating a gradient field over a curve gives the net change in the potential function. The analogy is exact — the gradient is the multivariable generalization of the derivative, and in both cases the integral collapses to boundary values, making the interior path irrelevant."
  explanation: "The key is recognizing that ∇f is the multivariable counterpart of F' in one dimension. Both theorems express the same idea: if you integrate the 'rate of change' of a function, you get the total change. The multivariable case is more powerful because it handles arbitrary paths in space, not just intervals on a line — but only for fields that are gradients of some scalar function."
```

## Explainer

Recall from your study of line integrals that ∫_C F · dr measures the work done by a vector field F along a curve C — it depends, in general, on every detail of the path. You integrate dot products F · r'(t) dt all along the curve, weighting the field's contribution by how much the curve moves in the field's direction. For a generic vector field, changing the curve between two fixed endpoints changes the integral. But for a special class of fields, this path-dependence vanishes entirely.

A **conservative field** is a vector field F that can be written as the gradient of a scalar function: F = ∇f. The scalar function f is called a **potential function** for F. The fundamental theorem for line integrals says: if F = ∇f, then ∫_C F · dr = f(B) − f(A), where A and B are the endpoints of C. The entire integral collapses to the difference of potential values at two points — the path in between is irrelevant. This is the direct multivariable generalization of the single-variable fundamental theorem of calculus, which says ∫_a^b F'(x) dx = F(b) − F(a).

The analogy is exact. In one dimension, integrating a derivative over an interval gives the net change in the function. In multiple dimensions, integrating a gradient field (F = ∇f is the gradient of f) over a curve gives the net change in f from start to end. The intermediate behavior of the curve — whether it meanders, loops, or takes a straight line — does not matter, because the gradient field "knows" the potential at every point, and work done is purely a bookkeeping of potential differences.

The practical consequence is **path independence**: for conservative fields, you can choose any convenient path between A and B. A loop from A back to A contributes zero work (f(A) − f(A) = 0). This is the condition for a force field to be conservative in physics — gravity and electrostatic fields are conservative, meaning the work done by gravity on a falling object depends only on the height difference, not the trajectory. Identifying whether a field is conservative (by checking if a potential function exists) is therefore the key step that determines whether this powerful shortcut applies.
