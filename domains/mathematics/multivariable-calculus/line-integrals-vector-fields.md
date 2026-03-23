---
id: line-integrals-vector-fields
title: Line Integrals of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-fields
  type: hard
- id: dot-product
  type: hard
builds-toward:
- work-line-integrals
- conservative-fields
tags:
- line-integral
- vector-field
stage: formal-systems
status: validated
---

# Line Integrals of Vector Fields

## Core Idea
The line integral ∫_C F · dr integrates a vector field along a curve. Parametrically: ∫_C F · dr = ∫_a^b F(r(t)) · r'(t) dt. This represents work done by force F along the path.

## Questions

```yaml
- question: "How is the line integral ∫_C F · dr computed parametrically?"
  type: multiple-choice
  options:
    - "∫_a^b |F(r(t))| dt"
    - "∫_a^b F(r(t)) · r'(t) dt"
    - "∫_a^b F(r(t)) × r'(t) dt"
    - "∫_a^b F(r(t)) · r(t) dt"
  answer: 1
  explanation: "The line integral uses the dot product of the field F (evaluated along the path) with the tangent vector r'(t). The dot product extracts the component of F in the direction of travel. Option A ignores direction entirely (just integrates magnitude). Option C uses a cross product, which gives a vector not a scalar. Option D dots with the position vector instead of the tangent, which has no physical meaning here."

- question: "Reversing the orientation of path C in ∫_C F · dr changes the sign of the result."
  type: true-false
  answer: true
  explanation: "When the path is reversed, the parametrization runs the opposite direction, so the tangent vector r'(t) points the other way. This flips the sign of F · r'(t) at every point, making the entire integral negative. Physically: if F is a force and you walk the path backward, the work done is the negative of the original work."

- question: "What physical quantity does the line integral ∫_C F · dr compute when F is a force field?"
  type: short-answer
  answer: "The work done by the force field F on an object moving along the path C."
  explanation: "Work is the integral of force in the direction of displacement. At each infinitesimal step along the path, the displacement vector is dr, and the force is F. The work contribution is F · dr (the component of force along the motion direction times the step size). Integrating over the whole path gives total work. This is the central physical motivation for line integrals of vector fields."
```

## Explainer

A line integral of a vector field asks: what is the cumulative effect of the field along a given path? The key idea is that at each point on the path, only the component of the field **in the direction of travel** matters. You are essentially asking how much the field "goes along with" the motion at each step, then adding it all up.

The formal setup is: parametrize the curve C by r(t) = ⟨x(t), y(t), z(t)⟩ for t ∈ [a, b]. The tangent vector r'(t) points in the direction of travel and has magnitude equal to the speed. The line integral is then ∫_C F · dr = ∫_a^b F(r(t)) · r'(t) dt. The dot product F(r(t)) · r'(t) extracts the component of F along the curve at each t — contributions where F aligns with the path are positive, where F opposes the path are negative, and where F is perpendicular the contribution is zero.

The most important physical interpretation is **work**. If F is a force field and a particle travels along C, the work done by F is exactly ∫_C F · dr. This makes intuitive sense: when you push an object in the direction it is already moving, you do positive work; when you push against its motion, you do negative work; when you push perpendicular to motion (like a normal force), you do no work. The dot product captures all three cases simultaneously.

Orientation matters crucially. The line integral is sensitive to which direction you traverse the path: ∫_{−C} F · dr = −∫_C F · dr, where −C is the same curve traversed backward. This is the opposite of line integrals of scalar functions (which are orientation-independent). It also sets up one of the most important concepts to come — conservative fields, where ∫_C F · dr depends only on the endpoints, not the path taken.
