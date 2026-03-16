---
id: rolling-motion-analysis
title: 'Rolling Without Slipping: Kinematics and Dynamics'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: holonomic-and-nonholonomic-constraints
  type: hard
- id: rigid-body-rotation-theory
  type: hard
builds-toward:
- systems-of-particles-mechanics
tags:
- rolling
- constraints
- contact-mechanics
stage: formal-systems
status: draft
---

# Rolling Without Slipping: Kinematics and Dynamics

## Core Idea
Rolling without slipping (v = ωr) is a nonholonomic constraint that couples translational and rotational motion. The no-slip condition at the contact point relates acceleration (a = αr) and, through energy analysis, reveals that rolling motion distributes kinetic energy between translation and rotation—the rolling object accelerates slower than one sliding freely.

## Explainer

You've studied rigid body rotation and the constraints that govern mechanical systems. Rolling without slipping is the most important constrained rigid-body motion in engineering, appearing in wheels, gears, planetary rollers, and ball bearings. The "without slipping" condition is a constraint that links translational and rotational motion in a precise way — and understanding that link transforms what seems like a complex problem into a tractable one.

The **no-slip condition** at the contact point is the foundation. When a disk of radius r rolls without slipping on a flat surface, the contact point is instantaneously at rest relative to the ground. This means the velocity of the center must equal the arc length swept per unit time: **v = ωr**, where v is the translational speed of the center and ω is the angular velocity. Differentiating gives **a = αr**, linking translational and angular accelerations. These two equations are the complete statement of the rolling constraint — they eliminate one degree of freedom, reducing the system from two independent motions to one. If you know ω, you know v; if you know α, you know a.

The instantaneous contact point being at rest has a useful geometric interpretation: it acts as an **instantaneous center of rotation**. All points on the rolling object rotate about this contact point at each instant, even as that center itself moves along the ground. The topmost point of the disk therefore moves at twice the center's velocity (2v), the center moves at v, and the contact point moves at zero. This is verifiable by adding translational and rotational velocity vectors at each point, and it has a practical consequence: a wheel spinning in place with a locked axle has its contact point moving at maximum speed, while a properly rolling wheel has its contact point momentarily still. The constraint is what converts rotary drive into net translation.

Energy analysis reveals a profound consequence of rolling: the total kinetic energy is KE = ½mv² + ½Iω². Using v = ωr to eliminate ω, this becomes KE = ½mv²(1 + I/mr²). Compare this to a frictionless sliding object of the same mass, which has only ½mv². The rolling object effectively carries higher inertia — part of its energy budget goes to spinning, leaving less available for translational acceleration. A solid disk (I = ½mr²) rolling down a ramp will always arrive at the bottom slower than a frictionless sliding block, regardless of mass. Two objects of different mass but the same shape will tie — what matters is the dimensionless ratio I/mr², which depends only on geometry. A thin ring (I = mr²) rolls even more slowly than a solid disk; a sphere (I = 2mr²/5) rolls faster than a disk. This geometry-dependence is a clean consequence of the rolling constraint and serves as an elegant experimental test of rotational inertia.
