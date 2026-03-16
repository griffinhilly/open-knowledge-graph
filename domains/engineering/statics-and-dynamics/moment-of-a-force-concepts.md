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

## Explainer

A force applied to a free body does two things: it can translate the body (push it sideways) and rotate it (spin it around some axis). The translational effect depends only on the magnitude and direction of the force. The rotational effect — the **moment** — also depends on *where* the force is applied. Specifically, it depends on the perpendicular distance from the reference point to the **line of action** of the force, a distance called the **moment arm** or **lever arm**. The moment M = F · d summarizes this: the same force applied farther from the pivot produces a larger rotational effect, which is why a longer wrench makes a bolt easier to loosen.

In 2D, moments are signed scalars. Counterclockwise is typically taken as positive. If you push downward on the right end of a seesaw, that creates a clockwise (negative) moment about the fulcrum. If you push down on the left end, that's a counterclockwise (positive) moment. When a rigid body is in equilibrium, both the sum of forces and the sum of moments about any point must be zero; this second condition is what allows you to solve for unknown reactions at supports and hinges that force balance alone cannot determine.

In 3D, moments become vectors, computed as the **cross product** M = r × F, where r is the position vector from the reference point to any point on the line of action of the force. The cross product is exactly the tool you studied: it produces a vector perpendicular to both r and F, with magnitude |r||F|sin(θ) = F · d, matching the 2D scalar formula. The direction of the moment vector follows the right-hand rule and indicates the axis about which rotation would occur. This vector formulation is essential when forces are skewed or systems are three-dimensional.

A useful shortcut is **Varignon's theorem**: the moment of a force about a point equals the sum of the moments of its components about the same point. If a force F has components Fx and Fy, and acts at a point (x, y) relative to the reference, then M = x·Fy − y·Fx. You do not need to find the perpendicular distance geometrically — you can decompose the force into components and sum their individual moment contributions. This is almost always easier than finding the true perpendicular distance for an oblique force, and it makes systematic calculation straightforward when working with free body diagrams containing multiple forces at multiple locations.
