---
id: rotating-reference-frames
title: Rotating Reference Frames
domain: physics
course: classical-mechanics
prerequisites:
- id: non-inertial-frames-and-pseudo-forces
  type: hard
builds-toward:
- coriolis-effect
tags:
- reference-frames
- rotation
- pseudo-forces
- centrifugal
stage: formal-systems
status: draft
---

# Rotating Reference Frames

## Core Idea
In a reference frame rotating with angular velocity ω, two pseudo-forces appear: the centrifugal force F_cf = m ω² r (pointing outward) and the Coriolis force F_cor = −2 m ω × v (perpendicular to velocity). The centrifugal force vanishes in the inertial frame (it accounts for centripetal acceleration in the rotating frame); the Coriolis force deflects moving objects perpendicular to their velocity.

## Explainer

From your prerequisite on non-inertial frames and pseudo-forces, you know the fundamental idea: Newton's second law *F = ma* holds only in **inertial frames** — frames that are not accelerating relative to the fixed stars. When you work in an accelerating frame, you introduce **pseudo-forces** (fictitious forces) that have no physical source but account for the acceleration of the frame itself. In a car braking hard, you feel "thrown forward" — that's the pseudo-force that appears in the car's non-inertial (decelerating) frame. Rotating frames are a special case: instead of a one-time linear acceleration, the frame is continuously changing direction.

Consider why rotation counts as acceleration at all: **centripetal acceleration** is required to keep any object moving in a circle (it points inward, toward the axis). From the rotating frame, an object that is stationary in the inertial frame appears to be spiraling outward — and to explain this within the rotating frame, you must introduce a pseudo-force pushing it outward. This is the **centrifugal force**: F_cf = mω²r, directed radially outward from the axis of rotation. In the inertial frame, there is no centrifugal force — what exists is centripetal force directed inward, keeping the object on its circular path. In the rotating frame, these cancel: centripetal force pushes in, centrifugal force pushes out, and the object appears stationary.

The second pseudo-force is the **Coriolis force**: F_cor = −2m(ω × v). It appears only when an object is moving within the rotating frame — it is proportional to the object's velocity (as measured in the rotating frame) and directed perpendicular to that velocity. The cross product ω × v gives the direction: always at right angles to both the rotation axis and the object's velocity. The key intuition is this: when an object moves outward in a rotating frame, it is actually moving in a straight line in the inertial frame, but the frame is rotating under it — so from inside the frame, the path appears to curve. The Coriolis force is the pseudo-force that accounts for this apparent curvature.

To build intuition, imagine you are on a rotating merry-go-round and try to roll a ball straight across to a friend on the other side. From above (the inertial frame), the ball travels in a straight line. But from the merry-go-round frame, the ball appears to curve sideways — deflected by the Coriolis force. On Earth, the same effect operates at planetary scale: large air masses moving poleward in the Northern Hemisphere are deflected to the right (from their perspective), generating the counterclockwise rotation of low-pressure weather systems. Earth's rotation is slow (ω ≈ 7.3 × 10⁻⁵ rad/s), so Coriolis effects are negligible for small-scale motion in a kitchen but enormous for hurricanes and ocean currents — phenomena that unfold over thousands of kilometers and days.
