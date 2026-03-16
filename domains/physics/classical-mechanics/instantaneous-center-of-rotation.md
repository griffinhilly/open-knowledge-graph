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

## Explainer

Your prerequisite — rotational kinematics — established the fundamental relationships for pure rotation: angular velocity ω, the tangential velocity v = ωr at a distance r from the axis, and the direction of that velocity (always perpendicular to the radius). The instantaneous center of rotation applies precisely these relationships to **general plane motion**, where a rigid body is simultaneously translating *and* rotating — like a rolling wheel, a connecting rod in an engine, or a door swinging while its hinge slides along a track.

The key insight is that any such motion, at any instant, can be analyzed *as if* the body were in pure rotation about one special point. This point — the **instantaneous center** (IC) — has zero velocity at that instant. Every other point in the body moves in a circle around the IC with speed v = ωr, where r is the distance from that point to the IC, and with a velocity direction perpendicular to the line from the point to the IC. The word "instantaneous" is important: the IC is not a fixed pivot but a point that can move over time; it's only valid for the velocity analysis at one moment.

Finding the IC is a geometric construction. If you know the *direction* of velocity for two different points on the body, the IC must lie on the perpendicular to each of those velocity vectors (because velocity is always perpendicular to the radius from the center of rotation). Draw the perpendicular to the velocity of point A through A, and the perpendicular to the velocity of point B through B — the IC is their intersection. No equations needed; just geometry.

The rolling wheel is the canonical example. The center of mass moves horizontally at speed v_cm, so its velocity direction is horizontal and the perpendicular through it is vertical. The contact point with the ground has zero velocity (the no-slip condition), which means the contact point *is* the IC. Now every point's velocity is determined geometrically: the top of the wheel is at distance 2R from the contact point, so its speed is 2Rω = 2v_cm — twice the center's speed, directed horizontally. A point at the wheel's 3 o'clock position is at distance R√2 from the contact point, so it moves at v_cm√2, directed at 45° upward and forward. All of these follow from a single principle without resolving vector components or solving simultaneous equations. For complex linkages — four-bar mechanisms, slider-cranks, robotic arms — the IC method turns what would be a system of equations into a sequence of geometric constructions, making velocity analysis tractable even for mechanisms with many moving parts.
