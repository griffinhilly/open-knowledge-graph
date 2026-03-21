---
id: moment-of-a-force-concepts
title: 'Moment of a Force: Concepts and Calculation'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: vector-analysis-and-components
  type: hard
- id: free-body-diagram-methodology
  type: soft
- id: cross-product
  type: soft
builds-toward:
- resultant-of-force-moment-systems
- rigid-body-equilibrium-planar
tags:
- moment
- torque
- rotation
- perpendicular distance
- cross product
stage: formal-systems
status: draft
---

# Moment of a Force: Concepts and Calculation

## Core Idea
A moment (or torque) is the rotational effect of a force about a point or axis, equal to the force magnitude times the perpendicular distance from the axis to the line of action: M = F × d. Moments have direction (clockwise or counterclockwise in 2D, or vector direction in 3D) and accumulate algebraically; they cause rotational acceleration when not balanced.

## Questions

```yaml
- question: "A horizontal force of 10 N acts at a point 3 m to the right of a pivot, at the same height as the pivot (so the position vector from pivot to application point is purely horizontal, parallel to the force). What is the moment about the pivot?"
  type: multiple-choice
  options:
    - "30 N·m, because the distance from the pivot to the application point is 3 m"
    - "0 N·m, because the force's line of action passes through the pivot — the moment arm is zero"
    - "30 N·m counterclockwise, by the right-hand rule"
    - "10 N·m, because only the perpendicular component of the distance matters"
  answer: 1
  explanation: "The moment arm is the perpendicular distance from the pivot to the *line of action* of the force — not the distance to the application point. Here, the force is horizontal and the application point is also directly horizontal from the pivot. The line of action (extended in both directions) passes straight through the pivot's height, so the perpendicular distance is zero and M = F × 0 = 0 N·m. Option A is the classic misconception: students use the distance to the application point (3 m) instead of the perpendicular distance to the line of action."

- question: "A 20 N force is applied at 30° above horizontal at a point 2 m directly to the right of a pivot (at the same height as the pivot). Using Varignon's theorem, what is the moment about the pivot?"
  type: multiple-choice
  options:
    - "40 N·m, because M = F × d = 20 × 2"
    - "34.6 N·m, because M = F × d × cos30°"
    - "20 N·m, because only the vertical force component (20sin30° = 10 N) has a nonzero moment arm (2 m), giving 10 × 2 = 20 N·m"
    - "17.3 N·m, because only the horizontal component does work against the rotation"
  answer: 2
  explanation: "Varignon's theorem: decompose F into Fx = 20cos30° ≈ 17.3 N (horizontal) and Fy = 20sin30° = 10 N (vertical). The application point is 2 m to the right of and at the same height as the pivot. The moment from Fx: its line of action is horizontal at the pivot's height, so perpendicular distance = 0, moment = 0. The moment from Fy: it acts vertically at a horizontal distance of 2 m from the pivot, so moment = 10 × 2 = 20 N·m. Total = 20 N·m. Option A ignores the angle entirely; options B and D apply the angle incorrectly."

- question: "The moment of a force about a point is zero whenever the line of action of that force passes through the point, regardless of how large the force is."
  type: true-false
  answer: true
  explanation: "The moment is M = F × d, where d is the perpendicular distance from the reference point to the line of action. If the line of action passes through the reference point, d = 0, so M = 0 no matter how large F is. Physically: a force directed exactly at the pivot cannot cause rotation about that pivot — it can only push or pull the pivot itself. This is why you can push a door all day if you push along the hinge axis: zero moment, zero rotation."

- question: "The moment produced by a force about a pivot depends on the distance from the pivot to the specific point where the force is applied to the body."
  type: true-false
  answer: false
  explanation: "The moment depends on the perpendicular distance from the pivot to the *line of action* — not to the specific application point. Two forces with the same magnitude and direction but applied at different points along the same line of action produce identical moments about any reference point. This is the principle of transmissibility: a force can be 'slid' along its line of action without changing its moment about any external point. The location of the application point matters only when computing moments about a point not on the line of action."

- question: "Explain Varignon's theorem and why it is useful. What does it allow you to do instead of finding the perpendicular distance to the line of action directly?"
  type: short-answer
  answer: "Varignon's theorem states that the moment of a force about a point equals the sum of the moments of the force's rectangular components about the same point. Instead of constructing the perpendicular from the pivot to the oblique line of action (which requires trigonometry or geometric constructions), you decompose the force into horizontal and vertical components and compute each component's moment using simple right-angle geometry — usually one component acts through the pivot (moment = 0) and the other acts at a straightforward perpendicular distance."
  explanation: "In practice, most free-body diagram problems involve forces at angles, and the true perpendicular distance to an oblique line of action is cumbersome to find geometrically. Varignon's theorem turns every moment calculation into two simple multiplications: (x-coordinate of application point) × (vertical force component) minus (y-coordinate) × (horizontal force component), which is exactly the cross product M = x·Fy − y·Fx. This is why the cross product formulation and Varignon's theorem are equivalent approaches — they both decompose the moment into orthogonal contributions."
```

## Explainer

A force applied to a free body does two things: it can translate the body (push it sideways) and rotate it (spin it around some axis). The translational effect depends only on the magnitude and direction of the force. The rotational effect — the **moment** — also depends on *where* the force is applied. Specifically, it depends on the perpendicular distance from the reference point to the **line of action** of the force, a distance called the **moment arm** or **lever arm**. The moment M = F · d summarizes this: the same force applied farther from the pivot produces a larger rotational effect, which is why a longer wrench makes a bolt easier to loosen.

In 2D, moments are signed scalars. Counterclockwise is typically taken as positive. If you push downward on the right end of a seesaw, that creates a clockwise (negative) moment about the fulcrum. If you push down on the left end, that's a counterclockwise (positive) moment. When a rigid body is in equilibrium, both the sum of forces and the sum of moments about any point must be zero; this second condition is what allows you to solve for unknown reactions at supports and hinges that force balance alone cannot determine.

In 3D, moments become vectors, computed as the **cross product** M = r × F, where r is the position vector from the reference point to any point on the line of action of the force. The cross product is exactly the tool you studied: it produces a vector perpendicular to both r and F, with magnitude |r||F|sin(θ) = F · d, matching the 2D scalar formula. The direction of the moment vector follows the right-hand rule and indicates the axis about which rotation would occur. This vector formulation is essential when forces are skewed or systems are three-dimensional.

A useful shortcut is **Varignon's theorem**: the moment of a force about a point equals the sum of the moments of its components about the same point. If a force F has components Fx and Fy, and acts at a point (x, y) relative to the reference, then M = x·Fy − y·Fx. You do not need to find the perpendicular distance geometrically — you can decompose the force into components and sum their individual moment contributions. This is almost always easier than finding the true perpendicular distance for an oblique force, and it makes systematic calculation straightforward when working with free body diagrams containing multiple forces at multiple locations.
