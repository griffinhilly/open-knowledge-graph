---
id: instantaneous-center-of-rotation-method
title: Instantaneous Center of Rotation Method
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rigid-body-plane-motion-analysis
  type: hard
tags:
- instantaneous-center
- ic
- rotation
- kinematics
stage: formal-systems
status: draft
---

# Instantaneous Center of Rotation Method

## Core Idea
For any instant during plane motion, there exists a point (the instantaneous center) about which the body appears to be in pure rotation. Velocities of all points are perpendicular to their position vectors from the IC, with magnitudes v = ω r. The IC method simplifies kinematics by converting plane motion to instantaneous rotation, eliminating the need to account for translation separately.

## Explainer

From your study of general plane motion, you know that any rigid body's velocity field can be decomposed into translation of a reference point plus rotation about that point — v_B = v_A + ω × r_{A→B}. The **instantaneous center of rotation (IC)** takes this a step further: it asks, is there some special point P (possibly not on the body at all) where v_P = 0 at this instant? If so, the entire body looks like it is in pure rotation about P right now.

The existence of such a point is guaranteed whenever the body is not in pure translation (ω ≠ 0). To find it, use the key constraint: every point's velocity must be perpendicular to the line connecting it to the IC. So if you know the direction of the velocity at two points on the body, draw perpendiculars to those velocities — the IC is where those perpendiculars intersect. For a wheel rolling without slipping on a flat surface, the contact point has zero velocity (no slip), so the IC is right there at the contact point. This is why the top of a rolling wheel moves at twice the axle speed: the top is twice as far from the IC as the axle, and v = ω·r from the IC.

The power of the method is computational: once you locate the IC, every velocity calculation reduces to v = ω·r, where r is the distance from the IC to the point of interest, and the direction is perpendicular to that line. There's no vector addition of translation and rotation — it's as if the body were spinning on a fixed axle, just for this instant. For linkage problems with several interconnected bars (think slider-crank mechanisms, robotic arms), the IC lets you propagate velocity through the system link by link without setting up systems of equations.

A critical subtlety: the IC is an instantaneous concept. It moves as the body moves — often rapidly — so you cannot use the IC to find accelerations without additional care. The velocity field is correct; the acceleration field is not simply ω²·r toward the IC. For accelerations, you still need the full kinematic equations. Think of the IC as a snapshot tool: perfect for velocities at one moment in time, not a substitute for the full kinematic description when you need how things change moment to moment.
