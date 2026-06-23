---
id: directional-derivatives
title: Directional Derivatives
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector
  type: hard
- id: dot-product
  type: hard
- id: dot-product-geometry
  type: hard
builds-toward:
- conservative-fields
tags:
- directional-derivative
- gradient
- unit-vector
- rate-of-change
stage: formal-systems
status: validated
---

# Directional Derivatives

## Core Idea
The directional derivative D_u f gives the rate of change of f in an arbitrary direction specified by a unit vector u. It is computed as D_u f = ∇f · u — the dot product of the gradient with the unit direction vector. This unifies partial derivatives (which are directional derivatives along coordinate axes) with the gradient (which is the direction of maximum directional derivative). The maximum value of D_u f over all unit vectors u is |∇f|, achieved when u = ∇f/|∇f|.

## How It's Best Learned
Present directional derivatives as answering the question: 'How fast does f change if I walk in direction u?' Then show that the formula D_u f = ∇f · u follows naturally. Have students compute directional derivatives for several directions at a single point and verify that the maximum occurs in the gradient direction.

## Common Misconceptions
- The direction vector u must be a unit vector; using a non-unit vector gives a scaled result.
- D_u f = ∇f · u, not |∇f| · |u|; the dot product formula includes the angle between ∇f and u.
- Directional derivatives can be negative (when moving in a direction that decreases f).

## Questions

```yaml
- question: "The gradient of f at point P is ∇f = (3, 4). What is the directional derivative D_u f in the direction u = (3/5, 4/5)?"
  type: multiple-choice
  options:
    - "5 — f increases at a rate of 5 per unit step"
    - "25 — the dot product of (3, 4) with (3, 4)"
    - "7 — the sum of the gradient components"
    - "1 — dividing by the gradient magnitude"
  answer: 0
  explanation: "u = (3/5, 4/5) is a unit vector (|u| = √(9/25 + 16/25) = 1). D_u f = ∇f · u = 3(3/5) + 4(4/5) = 9/5 + 16/5 = 5. Since u points in the gradient direction, this equals the maximum rate of change |∇f| = 5. Option B is the most common error: using the non-normalized gradient (3, 4) as the direction vector and computing (3,4)·(3,4) = 25, which conflates direction with gradient magnitude."

- question: "At a point where ∇f = (2, −1), a walker moves in a direction perpendicular to ∇f. What rate of change does she experience?"
  type: multiple-choice
  options:
    - "0 — perpendicular to the gradient means moving along a level curve"
    - "|∇f| = √5 — she is moving at the steepest rate"
    - "−|∇f| = −√5 — perpendicular means opposite direction"
    - "It depends on which of the two perpendicular directions she chooses"
  answer: 0
  explanation: "D_u f = |∇f| cos θ where θ is the angle between u and ∇f. Perpendicular means θ = 90°, cos 90° = 0, so D_u f = 0 regardless of which perpendicular direction is chosen. The level curves of f are exactly the curves perpendicular to ∇f — moving along a level curve means f does not change. Option D is wrong: both perpendicular directions give zero."

- question: "The maximum directional derivative of f at a point equals the magnitude of the gradient at that point."
  type: true-false
  answer: true
  explanation: "D_u f = ∇f · u = |∇f| cos θ. This is maximized when cos θ = 1 (u points in the gradient direction), giving max D_u f = |∇f|. The gradient direction is exactly the direction of steepest ascent, and the gradient's magnitude is the rate of that ascent per unit step."

- question: "The formula D_u f = ∇f · u gives the correct directional derivative for any nonzero vector u — you just interpret the result as 'rate of change per unit step in direction u'."
  type: true-false
  answer: false
  explanation: "If u is not a unit vector, ∇f · u = |∇f||u| cos θ, which is scaled by |u|. This is not the rate of change per unit distance — it conflates direction and step size. Using a non-unit vector v gives ∇f · v = (D_{v/|v|} f) · |v|, a result that depends on the arbitrary magnitude of v rather than the geometry of f. The unit-vector requirement ensures D_u f is purely about slope, independent of step size."

- question: "Why must the direction vector u be a unit vector in the directional derivative formula D_u f = ∇f · u, and what goes wrong if you use a non-unit vector?"
  type: short-answer
  answer: "A unit vector encodes pure direction without a scale. The directional derivative measures rate of change per unit distance traveled; if u has length 2, the formula gives twice the actual rate of change. Using a non-unit vector v produces ∇f · v = (D_{v/|v|} f) · |v| — a result that depends on the arbitrary magnitude of v rather than the geometry of f. Normalization ensures the result is a property of the direction alone."
  explanation: "The intuition: if you could change the directional derivative by stretching your direction vector, the concept would be meaningless. Normalizing removes the arbitrary scale so that D_u f depends only on which way you are pointing, not how long your direction arrow happens to be."
```

## Explainer

From partial derivatives, you know how to measure the rate of change of f in the x-direction (holding y fixed) and the y-direction (holding x fixed). But these are just two special directions among infinitely many. The **directional derivative** D_u f answers the more general question: how fast does f change if you move in an arbitrary direction u? The answer turns out to be completely determined by the gradient you already know: D_u f = ∇f · u, the dot product of the gradient with the unit direction vector.

The dot product formula is not a coincidence — it is the content of the theorem. Since |u| = 1, the dot product gives D_u f = |∇f| cos θ, where θ is the angle between ∇f and u. This single formula encodes all directional information. When u points in the gradient direction (θ = 0°), you get the maximum rate of change: D_u f = |∇f|. When u is perpendicular to ∇f (θ = 90°), the rate of change is zero — you are moving along a **level curve** where f is momentarily constant. When u points directly opposite to ∇f (θ = 180°), you get the steepest descent: D_u f = −|∇f|. The gradient is not just one derivative among many; it is the master object from which every directional derivative is computed as a projection.

This gives the **gradient a precise geometric meaning**: its direction is the direction of steepest ascent, and its magnitude is the rate of steepest ascent in that direction. Every other directional derivative is the cosine-scaled shadow of this maximum onto your chosen direction. The practical consequence is immediate: in gradient descent (used throughout optimization and machine learning), the update step moves in the direction of −∇f because that is exactly the direction that decreases f most steeply per unit step.

The requirement that u be a **unit vector** is not pedantry. Without normalization, the formula ∇f · v for an arbitrary vector v conflates two different things: the direction of travel and the distance of the step. A unit vector encodes pure direction; scaling by |v| changes the rate of change, not the direction. If you use a non-unit vector v, you get ∇f · v = (D_{v/|v|} f) · |v|, which is the directional derivative scaled by the step length. The unit-vector convention ensures that D_u f is purely a geometric quantity about the slope of f in direction u, independent of any chosen step size.
