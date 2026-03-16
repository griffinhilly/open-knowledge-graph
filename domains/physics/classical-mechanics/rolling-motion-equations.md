---
id: rolling-motion-equations
title: 'Rolling Motion Without Slipping: Equations and Analysis'
domain: physics
course: classical-mechanics
prerequisites:
- id: rolling-without-slipping
  type: hard
- id: rigid-body-planar-motion
  type: hard
builds-toward:
- gyroscopic-motion-precession
tags:
- rolling
- constraints
- motion
stage: formal-systems
status: draft
---

# Rolling Motion Without Slipping: Equations and Analysis

## Core Idea
Rolling without slipping means the contact point has zero velocity, giving the constraint v_cm = Rω. This reduces the degrees of freedom and allows complete analysis of motion down inclines, through loops, and in collisions.

## Explainer

Your prerequisite — rolling without slipping — established the constraint: when a round object rolls without slipping on a surface, the contact point has zero velocity, which forces v_cm = Rω. Taking the time derivative gives a_cm = Rα. These constraints link translation and rotation, reducing what looks like a two-degree-of-freedom problem to a one-degree-of-freedom problem: specify either the linear acceleration or the angular acceleration and the other is determined.

The power of these constraints becomes clear on an incline. A disk of mass m and radius R rolls down a ramp at angle θ. Two forces act: gravity (at the center of mass, pulling down the slope) and static friction (at the contact point, pointing up the slope). Newton's second law for translation gives mg sin θ − f = ma_cm. The rotational equation about the center of mass gives fR = Iα (only friction provides torque about the center — gravity acts through the center and has zero moment arm). Substituting α = a_cm/R from the rolling constraint: f = Ia_cm/R². Plugging back into the translational equation: mg sin θ = ma_cm + Ia_cm/R² = a_cm(m + I/R²). Solving: **a_cm = g sin θ / (1 + I/mR²)**. This single formula predicts everything. For a solid disk (I = ½mR²): a_cm = (2/3)g sin θ. For a solid sphere (I = ⅖mR²): a_cm = (5/7)g sin θ. For a thin ring (I = mR²): a_cm = (1/2)g sin θ. The pattern: more mass concentrated at the rim means more rotational inertia relative to mR², which means the rolling constraint requires more of the available gravitational force to go into spinning rather than accelerating the center, so the center accelerates more slowly. A ring beats a disk beats a sphere in a "slowness" race down a ramp — entirely because of geometry and mass distribution.

Energy methods complement the force approach and are often more direct for initial-to-final problems. The total kinetic energy of a rolling object is KE = ½mv_cm² + ½Iω². Substituting ω = v_cm/R: KE = ½mv_cm²(1 + I/mR²). An object rolling from rest down a height h satisfies mgh = ½mv_cm²(1 + I/mR²), immediately giving v_cm at the bottom without tracking forces or friction at all. This works because **static friction does no work**: the contact point is instantaneously at rest, so no displacement occurs there and the friction force acts through zero distance. Energy is conserved — none goes to heat — and the total mechanical energy simply redistributes between translational and rotational kinetic energy as the object descends.

The two methods — Newton's laws with the rolling constraint, and energy conservation — are complementary. Force methods give you accelerations and friction forces step by step through the motion, which matters when you need forces (to check whether static friction is sufficient, or to find normal forces in loops). Energy methods give you relationships between the initial and final states directly, which is far faster when you only care about speeds at specific points. Rolling motion is a clean test of both approaches, and mastering the constraint v_cm = Rω is the key that unlocks both.
