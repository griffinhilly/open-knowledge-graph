---
id: rigid-body-kinematics-general-motion
title: Rigid Body Kinematics — General Planar Motion
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rigid-body-kinematics-rotation
  type: hard
- id: kinematics-particles-curvilinear
  type: soft
builds-toward:
- rigid-body-kinetics-force-acceleration
tags:
- dynamics
- kinematics
- general planar motion
- relative velocity
- instantaneous center
- relative acceleration
stage: formal-systems
status: draft
---

# Rigid Body Kinematics — General Planar Motion

## Core Idea
General planar motion is the combination of translation and rotation, where every point on a rigid body has a velocity that can be decomposed as v_B = v_A + omega x r_{B/A}. Here v_A is the velocity of a reference point A, omega is the body's angular velocity, and r_{B/A} is the position vector from A to B. The instantaneous center of zero velocity (IC) is the unique point about which the entire body appears to be in pure rotation at that instant — every point's velocity is perpendicular to the line from it to the IC, with magnitude v = omega * r_IC. For acceleration analysis, the relative acceleration equation a_B = a_A + alpha x r_{B/A} - omega^2 * r_{B/A} adds the tangential and centripetal components of relative acceleration. General planar motion kinematics is the essential bridge between simple rotation and the full kinetics (force-acceleration) analysis of rigid bodies.

## How It's Best Learned
Master the relative velocity equation first using problems with rolling wheels, connecting rods, and slider-crank mechanisms. Locate the instantaneous center graphically by finding the intersection of velocity perpendiculars, then verify that the IC method and relative velocity equation yield the same answer. For acceleration, always include both the alpha x r (tangential) and omega^2 * r (centripetal) terms.

## Common Misconceptions
- Treating the instantaneous center as a fixed point — it generally changes location from instant to instant and cannot be used for acceleration analysis.
- Omitting the centripetal term omega^2 * r_{B/A} in the relative acceleration equation, even when alpha = 0.
- Assuming a rolling wheel's contact point has zero acceleration — it has zero velocity at the contact point, but its acceleration is nonzero (directed toward the center).

## Explainer

From your study of rigid body rotation, you know that when a body rotates about a fixed axis, every point traces a circular arc and you can find velocities using v = omega × r. **General planar motion** removes the fixed-axis constraint: the body can translate and rotate simultaneously. Think of a connecting rod in an engine, a ladder sliding off a wall, or a wheel rolling down a ramp — the rotation axis is itself moving. The key insight is that you can always decompose general motion into a translation of any reference point plus a rotation about that point.

This decomposition gives the **relative velocity equation**: v_B = v_A + ω × r_{B/A}. Pick any point A on the body whose velocity you know. The velocity of any other point B equals v_A (pure translation) plus ω × r_{B/A} (rotation of B around A). The angular velocity ω is the same for every pair of points — it is a property of the whole body, not of a particular point. This equation is always true. It looks like two unknowns (you often need to find v_B and ω simultaneously), but constraints on the motion (a pin joint, a surface contact, a fixed pivot) provide the additional equations needed.

The **instantaneous center of zero velocity (IC)** is a shortcut that makes velocity analysis much faster for many mechanisms. At any given instant, there exists exactly one point (real or imaginary) about which the body is in pure rotation — call it the IC. Every point's velocity is perpendicular to the line from it to the IC, and the speed is v = ω × d where d is the distance to the IC. To find the IC, draw the velocity vectors at two known points and extend perpendiculars to them — they intersect at the IC. For a rolling wheel, the IC is exactly at the contact point, which is why the contact point has zero velocity at that instant (it is the center of rotation). The IC method is elegant for velocities, but you must never use it for accelerations — the IC is an instantaneous property that changes location continuously and has nonzero acceleration itself.

For **acceleration analysis**, return to the relative acceleration equation: a_B = a_A + α × r_{B/A} − ω² r_{B/A}. The last term is the centripetal acceleration, directed from B toward A, that comes from rotation. Even if the angular acceleration α is zero (constant rotation speed), the centripetal term is nonzero whenever ω ≠ 0. This is why the contact point of a rolling wheel, despite having zero velocity, has nonzero centripetal acceleration directed toward the wheel's center. The acceleration equation has two vector unknowns (often a_B and α), which you solve from the constraint equations of the mechanism — typically one pin or slider constraint per equation.
