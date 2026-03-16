---
id: rigid-body-kinetics-force-acceleration
title: Rigid Body Kinetics — Force and Acceleration
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: dynamics-newtons-second-law
  type: hard
- id: mass-moment-of-inertia
  type: hard
builds-toward:
- rigid-body-work-energy
- angular-impulse-momentum
tags:
- dynamics
- kinetics
- rigid bodies
- Newton's second law
- rotation
- translation
stage: formal-systems
status: draft
---

# Rigid Body Kinetics — Force and Acceleration

## Core Idea
Newton's second law for a rigid body in planar motion consists of three coupled equations: ΣF_x = m*(a_G)_x, ΣF_y = m*(a_G)_y, and ΣM_G = I_G*alpha, where G is the mass center, a_G is the acceleration of the mass center, I_G is the mass moment of inertia about G, and alpha is the angular acceleration. Alternatively, moments can be summed about any point P using ΣM_P = I_G*alpha + (moment of m*a_G about P). For pure translation, alpha = 0 and the moment equation constrains force locations. For fixed-axis rotation, the mass center itself accelerates (normal and tangential components), coupling the force and moment equations. For general planar motion, all three equations are fully coupled and must be solved simultaneously with kinematic constraints.

## How It's Best Learned
Draw a free-body diagram showing all external forces and a kinetic diagram showing m*a_G at the mass center and I_G*alpha as a couple. Match the two diagrams term by term when writing the three equations of motion. For rolling problems, identify whether the wheel rolls without slip (kinematic constraint: a_G = alpha*r) or with slip (friction = mu_k * N). Always check that the number of equations matches the number of unknowns.

## Common Misconceptions
- Summing moments about the mass center and forgetting to use I_G (not I about the contact point or support, unless applying the alternative moment equation with the m*a_G transport term).
- Assuming friction at a rolling contact equals mu*N — for rolling without slip, friction is an unknown that must be solved for, and it is often less than mu_s*N.
- Neglecting the normal component of mass-center acceleration (omega^2*r toward the pivot) for fixed-axis rotation problems, which affects the pin reaction forces.

## Explainer

For a single particle, Newton's second law is F = ma — one vector equation relating the net force to the product of mass and acceleration. A rigid body is more complex: it has both a translational state (where its mass center is going) and a rotational state (how fast it's spinning). From your prerequisite on mass moment of inertia, you know that I_G quantifies a body's resistance to angular acceleration, just as mass quantifies resistance to translational acceleration. Rigid body kinetics couples these two behaviors through three equations of motion.

The translational equations are simply Newton's second law applied to the mass center: ΣF_x = m(a_G)_x and ΣF_y = m(a_G)_y. All external forces, regardless of where they are applied on the body, contribute to accelerating the mass center. The rotational equation ΣM_G = I_G·α is the angular counterpart: net moment about the mass center equals the mass moment of inertia times angular acceleration. This equation accounts for the *torque* effect of forces — the same force applied at different distances from G produces different angular accelerations. Together, these three equations govern all planar rigid body motion.

The coupling between translation and rotation depends on the type of motion. For **pure translation** (no rotation), α = 0, and the moment equation constrains the location of the resultant force. For **fixed-axis rotation** (a door on a hinge, a wheel on a fixed axle), the mass center moves in a circle around the fixed point, so it has both tangential acceleration (r·α, from angular acceleration) and normal acceleration (ω²·r, from existing angular velocity) — this normal component is frequently overlooked. For **general planar motion** (a wheel rolling across the floor, a connecting rod in an engine), both translational and rotational accelerations are nonzero and fully coupled, requiring all three equations plus a kinematic constraint like a_G = α·r.

The diagram method is the clearest way to organize these equations. Draw a free-body diagram showing all external forces (weights, applied loads, normal forces, friction). Draw a separate kinetic diagram showing the inertia terms: a vector m·**a_G** at the mass center and a couple I_G·α representing the rotational inertia. Then match the free-body diagram to the kinetic diagram equation by equation. This visual accounting prevents the most common errors — especially when taking moments about a point other than G, where you must include the moment of the m·**a_G** vector about that point as a transport term.

Rolling contact deserves special attention. When a body rolls without slipping, the contact point has zero velocity, giving the kinematic constraint a_G = α·r. But friction at the contact is *not* µN — it is whatever value is needed to enforce the rolling constraint, which you solve for from the equations of motion. Only after solving do you check whether the required friction is less than µ_s·N; if not, the body slips instead of rolling, and you must redo the problem with kinetic friction µ_k·N as a known force and the no-slip kinematic constraint removed.
