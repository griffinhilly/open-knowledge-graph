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

## Explainer

You already know that when you analyze motion in a rotating reference frame, Newton's second law gains extra terms — fictitious forces that account for the fact that the frame itself is accelerating. The two main fictitious forces are the **centrifugal force** (pointing outward from the rotation axis) and the **Coriolis force**, which is the one that depends on velocity. The Coriolis force arises because an object moving in a rotating frame is continuously changing its position relative to the rotation axis, and the frame's angular velocity is continuously rotating the coordinate directions underneath it.

The mathematical expression is **F_Coriolis = −2m(ω × v)**, where **ω** is the angular velocity vector of the rotating frame (pointing along Earth's rotation axis, toward the North Pole) and **v** is the object's velocity as measured in the rotating frame. The cross product **ω × v** gives a vector perpendicular to both. To find the deflection direction in the Northern Hemisphere, point your fingers in the direction of motion and curl them toward **ω** (pointing up): the Coriolis force on a northward-moving object points eastward (rightward), and on an eastward-moving object points southward (also rightward). The general rule is: **moving objects in the Northern Hemisphere are deflected to their right; in the Southern Hemisphere, to their left**. This is reversed in the south because the component of **ω** along the local vertical points downward.

Why do hurricanes rotate counter-clockwise in the Northern Hemisphere? Air flows inward toward a low-pressure center. As it flows inward from the north, it gets deflected right (eastward). As it flows in from the west, it gets deflected right (southward). As it flows in from the south, it gets deflected right (westward). The cumulative effect of all this rightward deflection on inflowing air produces a counter-clockwise circulation. In the Southern Hemisphere the deflection is leftward, producing clockwise rotation. Note: the Coriolis effect is far too weak to affect bathtub drains (which are dominated by local geometry and initial conditions); it only becomes dominant at scales of hundreds of kilometers and time scales of hours to days.

For quantitative problems, the key insight is that the Coriolis acceleration has magnitude **2ωv sin φ**, where **φ** is the latitude. At the equator (φ = 0), the vertical component of ω is zero and horizontal Coriolis deflection vanishes — which is why tropical cyclones cannot form right at the equator. At the poles (φ = 90°), the full ω acts and the deflection is maximum. For a projectile fired horizontally, the Coriolis deviation over distance *d* is approximately **d² ω sin φ / v**, which is tiny for small *d* but becomes significant for artillery shells and long-range ballistic missiles, requiring explicit correction.
