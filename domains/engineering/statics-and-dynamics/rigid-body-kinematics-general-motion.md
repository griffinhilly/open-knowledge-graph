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
