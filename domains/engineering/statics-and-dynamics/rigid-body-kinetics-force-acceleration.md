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
