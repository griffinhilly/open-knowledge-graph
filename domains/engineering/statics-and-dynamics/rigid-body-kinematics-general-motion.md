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
status: validated
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

## Questions

```yaml
- question: "A wheel rolls without slipping at constant angular velocity (α = 0). A student claims that since α = 0, there is no relative acceleration between the contact point and the wheel's center. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — if α = 0, the tangential acceleration term vanishes and no relative acceleration exists"
    - "No — the centripetal term ω²r_{B/A} is nonzero whenever ω ≠ 0, giving the contact point acceleration directed toward the wheel's center even when α = 0"
    - "Yes — the contact point has zero velocity, so it must also have zero acceleration"
    - "No — but only because friction at the contact point introduces an upward reaction acceleration"
  answer: 1
  explanation: "The relative acceleration equation is a_B = a_A + α × r_{B/A} − ω² r_{B/A}. The last term, the centripetal acceleration, depends on ω, not α. Even with α = 0 (constant angular speed), if ω ≠ 0 the centripetal term is nonzero and points from B toward A — from the contact point toward the wheel's center. This is a common and critical mistake: students see α = 0 and conclude acceleration is zero, forgetting that centripetal acceleration exists for any rotating body with nonzero angular velocity. The contact point of a rolling wheel has zero instantaneous velocity but nonzero acceleration (ω²R toward the center)."

- question: "Where is the instantaneous center of zero velocity (IC) for a wheel rolling without slipping on a flat surface?"
  type: multiple-choice
  options:
    - "At the center of the wheel"
    - "At the highest point on the wheel"
    - "At the contact point between the wheel and the ground"
    - "At a point infinitely far ahead in the direction of travel"
  answer: 2
  explanation: "For a rolling wheel, the contact point has zero velocity at that instant (rolling without slipping means the contact point is momentarily at rest). The IC is defined as the point of zero velocity, so it lies at the contact point. Every other point on the wheel moves with velocity proportional to its distance from the IC and in a direction perpendicular to the line from it to the IC. The top of the wheel moves fastest (farthest from IC) and the center moves at an intermediate speed. This is why the IC method is so useful for rolling wheels — the IC is physically meaningful and easy to locate."

- question: "The angular velocity ω in the relative velocity equation v_B = v_A + ω × r_{B/A} is a property of the entire rigid body — every pair of points shares the same ω at any given instant."
  type: true-false
  answer: true
  explanation: "Angular velocity describes how the body rotates as a whole. It is not a property of any particular point — it is a property of the rigid body at that instant. Every pair of points on the body rotates relative to each other with the same angular velocity ω. This is what 'rigid body' means: no deformation, so all points maintain fixed distances from each other, which requires a single, uniform angular velocity. This fact makes the relative velocity equation powerful: ω appears once and applies regardless of which two points you analyze."

- question: "The instantaneous center of zero velocity can be used for both velocity and acceleration analysis because it captures the body's complete kinematic state at that instant."
  type: true-false
  answer: false
  explanation: "The IC is an instantaneous property: it gives zero velocity at one specific moment, but it is itself accelerating and its location changes from instant to instant. Acceleration analysis requires a fixed reference point whose acceleration you know — the IC does not qualify. The relative acceleration equation a_B = a_A + α × r_{B/A} − ω²r_{B/A} must be used for acceleration, not the IC shortcut. This is one of the most common errors in rigid body dynamics: students use the IC to find velocities (correct) and then try to use it for accelerations (incorrect)."

- question: "Why must you include the centripetal acceleration term ω²r_{B/A} in the relative acceleration equation even when the angular acceleration α is zero?"
  type: short-answer
  answer: "The centripetal acceleration term arises from the change in direction of the rotating position vector r_{B/A}, not from any change in angular speed. Even when the body spins at constant ω (α = 0), point B is undergoing circular motion relative to point A — its velocity direction is continuously changing, which is itself an acceleration. This centripetal acceleration always points from B toward A (inward along r_{B/A}) with magnitude ω²|r_{B/A}|. Setting α = 0 removes only the tangential (α × r) term; it has no effect on the centripetal term. Omitting ω²r_{B/A} when α = 0 is incorrect and leads to significant errors in any problem with nonzero angular velocity."
  explanation: "This is the central conceptual mistake in rigid body acceleration problems. Students correctly associate α with angular acceleration and assume α = 0 means 'no acceleration effects.' But centripetal acceleration is not about changing angular speed — it's about changing velocity direction due to rotation at any speed. A body spinning at perfectly constant ω still requires centripetal acceleration for every point on it. The rolling wheel contact point example makes this concrete: zero velocity but ω²R of centripetal acceleration toward the center."
```

## Explainer

From your study of rigid body rotation, you know that when a body rotates about a fixed axis, every point traces a circular arc and you can find velocities using v = omega × r. **General planar motion** removes the fixed-axis constraint: the body can translate and rotate simultaneously. Think of a connecting rod in an engine, a ladder sliding off a wall, or a wheel rolling down a ramp — the rotation axis is itself moving. The key insight is that you can always decompose general motion into a translation of any reference point plus a rotation about that point.

This decomposition gives the **relative velocity equation**: v_B = v_A + ω × r_{B/A}. Pick any point A on the body whose velocity you know. The velocity of any other point B equals v_A (pure translation) plus ω × r_{B/A} (rotation of B around A). The angular velocity ω is the same for every pair of points — it is a property of the whole body, not of a particular point. This equation is always true. It looks like two unknowns (you often need to find v_B and ω simultaneously), but constraints on the motion (a pin joint, a surface contact, a fixed pivot) provide the additional equations needed.

The **instantaneous center of zero velocity (IC)** is a shortcut that makes velocity analysis much faster for many mechanisms. At any given instant, there exists exactly one point (real or imaginary) about which the body is in pure rotation — call it the IC. Every point's velocity is perpendicular to the line from it to the IC, and the speed is v = ω × d where d is the distance to the IC. To find the IC, draw the velocity vectors at two known points and extend perpendiculars to them — they intersect at the IC. For a rolling wheel, the IC is exactly at the contact point, which is why the contact point has zero velocity at that instant (it is the center of rotation). The IC method is elegant for velocities, but you must never use it for accelerations — the IC is an instantaneous property that changes location continuously and has nonzero acceleration itself.

For **acceleration analysis**, return to the relative acceleration equation: a_B = a_A + α × r_{B/A} − ω² r_{B/A}. The last term is the centripetal acceleration, directed from B toward A, that comes from rotation. Even if the angular acceleration α is zero (constant rotation speed), the centripetal term is nonzero whenever ω ≠ 0. This is why the contact point of a rolling wheel, despite having zero velocity, has nonzero centripetal acceleration directed toward the wheel's center. The acceleration equation has two vector unknowns (often a_B and α), which you solve from the constraint equations of the mechanism — typically one pin or slider constraint per equation.
