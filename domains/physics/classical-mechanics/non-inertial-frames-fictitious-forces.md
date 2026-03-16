---
id: non-inertial-frames-fictitious-forces
title: Non-Inertial Reference Frames and Fictitious Forces
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: circular-motion-kinematics
  type: soft
tags:
- reference-frames
- fictitious-forces
- acceleration
stage: formal-systems
status: draft
---

# Non-Inertial Reference Frames and Fictitious Forces

## Core Idea
In an accelerating reference frame, fictitious forces (inertial forces) appear: a force −ma opposing the frame's acceleration, a centrifugal force −mω²r in a rotating frame, and a Coriolis force −2m(ω × v) for moving objects.

## How It's Best Learned
Analyze simple systems in rotating and linearly accelerating frames. Compare results to the inertial frame to see how fictitious forces simplify the analysis.

## Explainer

From your study of Newton's second law, you know the foundational principle: **F = ma**, where *F* is the net real force on an object, *m* its mass, and *a* its acceleration measured in an **inertial frame** — a frame moving at constant velocity or at rest. This qualifier matters enormously. When you apply Newton's laws inside an accelerating car, a spinning merry-go-round, or the rotating Earth, the equations break down unless you account for the acceleration of the frame itself.

Consider sitting in a car that suddenly accelerates forward. You feel pressed back into your seat. From the ground — an inertial frame — there is no mystery: the seat exerts a real forward force on you, and you accelerate forward with the car. But if you analyze the situation from *inside* the car, a **non-inertial frame** that is itself accelerating, you feel a backward force with no identifiable physical source. This apparent force is a **fictitious force** (also called a pseudo-force or inertial force): it appears in the equations of motion for the accelerating frame not because anything is pushing you, but because the frame is accelerating. Its magnitude is *ma*_frame and it always points opposite to the frame's acceleration, so the accelerating frame looks, from inside, as if there were an extra backward force.

In a **rotating frame** — like a spinning laboratory, a centrifuge, or the Earth's surface — two fictitious forces appear simultaneously. The **centrifugal force** pushes objects radially outward from the rotation axis with magnitude *mω*²*r*, where *ω* is the angular velocity and *r* the distance from the axis. The **Coriolis force** acts on objects that are *moving* within the rotating frame, deflecting them perpendicular to their velocity with magnitude 2*m*(***ω*** × ***v***). The Coriolis force is responsible for the systematic deflection of winds and ocean currents on Earth: in the Northern Hemisphere, moving objects are deflected to the right; in the Southern Hemisphere, to the left. This is why hurricanes rotate counterclockwise in the north and clockwise in the south.

Fictitious forces are not "real" in the sense that they have no reaction partner by Newton's third law, and they vanish entirely when you switch to an inertial frame. But they are **real in their effects** within the non-inertial frame — and working in a rotating frame using fictitious forces is often far simpler than transforming everything to an inertial frame. A person standing still on a rotating platform is in equilibrium from the platform's perspective: the outward centrifugal force and the inward friction sum to zero. This kind of analysis — adding fictitious forces to restore the form of Newton's second law in an accelerating frame — is one of the most powerful tools in classical mechanics and is indispensable for geophysics, atmospheric science, and engineering design of rotating systems.
