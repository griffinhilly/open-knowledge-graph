---
id: instantaneous-center-of-rotation
title: Instantaneous Center of Rotation
domain: physics
course: classical-mechanics
prerequisites:
- id: rotational-kinematics
  type: hard
builds-toward:
- rolling-without-slipping
tags:
- rotation
- kinematics
- rolling
stage: formal-systems
status: draft
---

# Instantaneous Center of Rotation

## Core Idea
At any instant, a rigid body undergoing plane motion can be viewed as rotating about a unique point (the instantaneous center). The velocity of every point is perpendicular to the line from that point to the instantaneous center, with magnitude v = ω·r. For a wheel rolling without slipping, the instantaneous center is the contact point where v = 0.

## Questions

```yaml
- question: "A student analyzes a wheel rolling without slipping and says: 'The center of mass has velocity v_cm forward, so the contact point also moves forward at the same speed v_cm since they're both part of the same rigid body.' Why is this wrong?"
  type: multiple-choice
  options:
    - "The contact point moves backward at velocity v_cm due to the rolling constraint"
    - "For rolling without slipping, the contact point is the instantaneous center — it has zero velocity at that instant, not v_cm. This is the no-slip condition, and it implies the top of the wheel moves at 2v_cm, not v_cm."
    - "All points on a rolling wheel have the same speed as the center of mass"
    - "The contact point has velocity v_cm/2 because it is halfway between the center and the ground"
  answer: 1
  explanation: "The no-slip condition requires the contact point velocity to be zero at every instant — if it had any forward velocity, the wheel would be sliding. This is precisely why the contact point is the instantaneous center of rotation. The velocity of any other point is then v = ωr, where r is its distance from the contact point. The top of the wheel is at distance 2R, so v_top = 2ωR = 2v_cm. The student's error is applying translational velocity uniformly across a body in combined translation and rotation."

- question: "How would you geometrically locate the instantaneous center (IC) of a rigid rod if you know the direction of velocity for two points A and B on the rod?"
  type: multiple-choice
  options:
    - "Find the point where the velocity vectors of A and B, extended as lines, intersect"
    - "Draw a line perpendicular to the velocity of A through A, and a line perpendicular to the velocity of B through B — their intersection is the instantaneous center"
    - "Locate the midpoint of A and B and project it outward by the angular velocity"
    - "Average the positions of A and B weighted by their speeds"
  answer: 1
  explanation: "Velocity in rotation is always perpendicular to the radius from the center. So if a point has a certain velocity direction, the center of rotation must lie somewhere on the line perpendicular to that velocity through the point. Two perpendiculars for two different points intersect at exactly one location — the IC. This is a purely geometric construction requiring no equations, which is what makes the IC method so powerful for analyzing mechanisms."

- question: "The instantaneous center of rotation is a fixed pivot point that remains stationary throughout the motion of a rigid body in plane motion."
  type: true-false
  answer: false
  explanation: "The IC is only valid instantaneously — it is the point with zero velocity at one specific moment, and it generally moves as the body's configuration changes. For a rolling wheel, the IC is the contact point at each instant, but the contact point itself moves forward along the ground as the wheel rolls. The word 'instantaneous' in the name is essential: treat the IC as fixed only for the purpose of velocity analysis at a single moment, never over a finite time interval."

- question: "The velocity of any point on a rigid body undergoing plane motion is proportional to its distance from the instantaneous center of rotation."
  type: true-false
  answer: true
  explanation: "Since all plane motion at any instant is treated as pure rotation about the IC, the formula v = ωr applies exactly, where r is the distance from the point to the IC and ω is the instantaneous angular velocity of the body. A point twice as far from the IC moves at twice the speed; a point at the IC has zero speed. This proportionality is the key computational tool: once the IC and ω are known, the velocity of every point follows immediately from its distance to the IC, with direction perpendicular to the line connecting it to the IC."

- question: "Why can any general plane motion (simultaneous translation and rotation) be analyzed as pure rotation about the instantaneous center, even though no physical pivot exists at that point?"
  type: short-answer
  answer: "At any instant, the velocity field of a rigid body in plane motion must be consistent with a single angular velocity ω. This means there exists a unique point where the translational and rotational velocity contributions cancel exactly to give zero velocity — the IC. This is not a physical constraint but a mathematical theorem about rigid body kinematics: the superposition of a uniform translation and a rotation about any point is always equivalent to a pure rotation about some specific other point. Since the IC is the point where velocity is zero, and since all other velocities follow from v = ωr with the correct perpendicular direction, the full velocity field is determined by the IC location and ω alone — exactly as in pure rotation."
  explanation: "The IC method works because it exploits the mathematical structure of rigid body motion rather than fighting it. Instead of decomposing every velocity into translational and rotational components and adding them — which requires two pieces of information and vector arithmetic — you find the IC (one geometric construction) and apply v = ωr directly. For complex linkages, this geometric shortcut is the difference between a tractable and an intractable problem."
```

## Explainer

Your prerequisite — rotational kinematics — established the fundamental relationships for pure rotation: angular velocity ω, the tangential velocity v = ωr at a distance r from the axis, and the direction of that velocity (always perpendicular to the radius). The instantaneous center of rotation applies precisely these relationships to **general plane motion**, where a rigid body is simultaneously translating *and* rotating — like a rolling wheel, a connecting rod in an engine, or a door swinging while its hinge slides along a track.

The key insight is that any such motion, at any instant, can be analyzed *as if* the body were in pure rotation about one special point. This point — the **instantaneous center** (IC) — has zero velocity at that instant. Every other point in the body moves in a circle around the IC with speed v = ωr, where r is the distance from that point to the IC, and with a velocity direction perpendicular to the line from the point to the IC. The word "instantaneous" is important: the IC is not a fixed pivot but a point that can move over time; it's only valid for the velocity analysis at one moment.

Finding the IC is a geometric construction. If you know the *direction* of velocity for two different points on the body, the IC must lie on the perpendicular to each of those velocity vectors (because velocity is always perpendicular to the radius from the center of rotation). Draw the perpendicular to the velocity of point A through A, and the perpendicular to the velocity of point B through B — the IC is their intersection. No equations needed; just geometry.

The rolling wheel is the canonical example. The center of mass moves horizontally at speed v_cm, so its velocity direction is horizontal and the perpendicular through it is vertical. The contact point with the ground has zero velocity (the no-slip condition), which means the contact point *is* the IC. Now every point's velocity is determined geometrically: the top of the wheel is at distance 2R from the contact point, so its speed is 2Rω = 2v_cm — twice the center's speed, directed horizontally. A point at the wheel's 3 o'clock position is at distance R√2 from the contact point, so it moves at v_cm√2, directed at 45° upward and forward. All of these follow from a single principle without resolving vector components or solving simultaneous equations. For complex linkages — four-bar mechanisms, slider-cranks, robotic arms — the IC method turns what would be a system of equations into a sequence of geometric constructions, making velocity analysis tractable even for mechanisms with many moving parts.
