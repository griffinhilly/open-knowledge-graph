---
id: coriolis-effect-classical-mechanics
title: Coriolis Effect
domain: physics
course: classical-mechanics
prerequisites:
- id: rotating-reference-frames
  type: hard
tags:
- coriolis
- rotating-frames
- geophysics
- deflection
stage: formal-systems
status: draft
---

# Coriolis Effect

## Core Idea
The Coriolis force F_cor = −2 m ω × v deflects moving objects in rotating frames (e.g., on Earth, which rotates at ω ≈ 7.3 × 10⁻⁵ rad/s). In the Northern Hemisphere, moving objects are deflected rightward; in the Southern Hemisphere, leftward. This effect is crucial for large-scale phenomena: hurricanes rotate due to Coriolis deflection, ocean currents curve, and ballistic trajectories deviate significantly over long distances.

## Questions

```yaml
- question: "Air flows northward toward a low-pressure center in the Northern Hemisphere. The Coriolis force deflects it:"
  type: multiple-choice
  options:
    - "To the left (westward), causing clockwise hurricane rotation"
    - "To the right (eastward), contributing to counter-clockwise hurricane rotation"
    - "Downward, toward the Earth's surface"
    - "It has no effect on air flowing exactly northward"
  answer: 1
  explanation: "In the Northern Hemisphere, the Coriolis force deflects ALL moving objects to their right. Northward-moving air is deflected rightward (eastward). When air flows inward from all directions toward a low-pressure center, consistent rightward deflection produces counter-clockwise circulation. Option A gives the Southern Hemisphere result."

- question: "Why do tropical cyclones never form right at the equator?"
  type: multiple-choice
  options:
    - "Ocean surface temperature at the equator is too low to generate the needed energy"
    - "The vertical component of Earth's angular velocity ω is zero at the equator, so there is no horizontal Coriolis deflection"
    - "Trade winds blow too strongly at the equator to permit organized rotation"
    - "The Coriolis force is strongest at the equator, producing chaotic rather than organized flow"
  answer: 1
  explanation: "The Coriolis acceleration for horizontal motion is 2ωv sinφ, where φ is latitude. At the equator (φ = 0°), sinφ = 0 and horizontal Coriolis deflection vanishes. Without deflection, inflowing air cannot develop organized rotation. Cyclones require a minimum latitude (roughly 5°) for sufficient Coriolis effect."

- question: "The Coriolis force is a real physical force that acts on objects moving in any reference frame, not just rotating ones."
  type: true-false
  answer: false
  explanation: "The Coriolis force is a fictitious (inertial) force that appears only when motion is analyzed in a rotating reference frame. In an inertial frame, no Coriolis force acts — the 'deflection' is simply inertial straight-line motion viewed from a rotating frame. Fictitious forces are real in their effects within rotating frames but have no physical cause independent of the choice of frame."

- question: "The Coriolis effect deflects moving objects in the Southern Hemisphere to the left of their direction of motion."
  type: true-false
  answer: true
  explanation: "This follows from F = −2m(ω×v). In the Southern Hemisphere, the local vertical component of ω points downward (opposite to the Northern Hemisphere), reversing the deflection direction. Moving objects are deflected to their left, which is why Southern Hemisphere cyclones rotate clockwise as inflowing air is deflected leftward from all directions."

- question: "Explain why Coriolis deflection causes hurricanes to rotate counter-clockwise in the Northern Hemisphere — trace the deflection of air flowing inward from different directions rather than just citing the rule."
  type: short-answer
  answer: "Air flows inward from all directions. Northward-moving air (from the south) is deflected right = eastward. Southward-moving air (from the north) is deflected right = westward. Eastward-moving air (from the west) is deflected right = southward. Westward-moving air (from the east) is deflected right = northward. Each inflow direction gets a rightward push that consistently contributes to counter-clockwise rotation around the center."
  explanation: "The CCW rotation is the cumulative result of independent rightward deflections from every compass direction of inflow. In the Southern Hemisphere, leftward deflection from all directions produces clockwise rotation by the same logic. The pattern emerges from the geometry of right-deflection applied symmetrically around a central low."
```

## Explainer

You already know that when you analyze motion in a rotating reference frame, Newton's second law gains extra terms — fictitious forces that account for the fact that the frame itself is accelerating. The two main fictitious forces are the **centrifugal force** (pointing outward from the rotation axis) and the **Coriolis force**, which is the one that depends on velocity. The Coriolis force arises because an object moving in a rotating frame is continuously changing its position relative to the rotation axis, and the frame's angular velocity is continuously rotating the coordinate directions underneath it.

The mathematical expression is **F_Coriolis = −2m(ω × v)**, where **ω** is the angular velocity vector of the rotating frame (pointing along Earth's rotation axis, toward the North Pole) and **v** is the object's velocity as measured in the rotating frame. The cross product **ω × v** gives a vector perpendicular to both. To find the deflection direction in the Northern Hemisphere, point your fingers in the direction of motion and curl them toward **ω** (pointing up): the Coriolis force on a northward-moving object points eastward (rightward), and on an eastward-moving object points southward (also rightward). The general rule is: **moving objects in the Northern Hemisphere are deflected to their right; in the Southern Hemisphere, to their left**. This is reversed in the south because the component of **ω** along the local vertical points downward.

Why do hurricanes rotate counter-clockwise in the Northern Hemisphere? Air flows inward toward a low-pressure center. As it flows inward from the north, it gets deflected right (eastward). As it flows in from the west, it gets deflected right (southward). As it flows in from the south, it gets deflected right (westward). The cumulative effect of all this rightward deflection on inflowing air produces a counter-clockwise circulation. In the Southern Hemisphere the deflection is leftward, producing clockwise rotation. Note: the Coriolis effect is far too weak to affect bathtub drains (which are dominated by local geometry and initial conditions); it only becomes dominant at scales of hundreds of kilometers and time scales of hours to days.

For quantitative problems, the key insight is that the Coriolis acceleration has magnitude **2ωv sin φ**, where **φ** is the latitude. At the equator (φ = 0), the vertical component of ω is zero and horizontal Coriolis deflection vanishes — which is why tropical cyclones cannot form right at the equator. At the poles (φ = 90°), the full ω acts and the deflection is maximum. For a projectile fired horizontally, the Coriolis deviation over distance *d* is approximately **d² ω sin φ / v**, which is tiny for small *d* but becomes significant for artillery shells and long-range ballistic missiles, requiring explicit correction.
