---
id: equilibrium-particles-3d
title: Equilibrium of Particles in 3D
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: equilibrium-particles-2d
  type: hard
- id: vectors-in-3d
  type: hard
builds-toward:
- equilibrium-rigid-bodies
tags:
- statics
- equilibrium
- particles
- 3D
- space structures
stage: formal-systems
status: validated
---

# Equilibrium of Particles in 3D

## Core Idea
In 3D, particle equilibrium requires ΣF = 0, yielding three scalar equations: ΣFx = 0, ΣFy = 0, ΣFz = 0. Forces in 3D are expressed using Cartesian unit vectors, and cables or rod members with known geometry have their force directions determined using unit position vectors: T = T·(r_AB / |r_AB|). Setting up these unit vectors systematically from coordinate geometry is the primary skill required.

## How It's Best Learned
Practice writing 3D forces in Cartesian form using direction cosines or position vectors from geometry. Organize force components in a table before summing in each direction.

## Common Misconceptions
- Errors in computing unit vectors from position vector geometry.
- Forgetting the z-direction equation in 3D.
- Sign errors when resolving inclined cables or rods into Cartesian components.

## Explainer

You already know how to solve 2D particle equilibrium — you set ΣFx = 0 and ΣFy = 0, then solve for unknowns. The 3D case adds one more equation: ΣFz = 0. In principle, this is a straightforward extension; in practice, the challenge is almost entirely geometric. Writing a cable or rod force in Cartesian component form when it points in an arbitrary direction in 3D space is where most errors occur.

The systematic approach is to find a **unit position vector** from the particle to the point where the cable or rod is anchored. If a cable runs from point A to point B, the position vector is **r**_AB = (B_x − A_x)**i** + (B_y − A_y)**j** + (B_z − A_z)**k**. The unit vector along that direction is **û** = **r**_AB / |**r**_AB|, where |**r**_AB| = √(Δx² + Δy² + Δz²). Then the cable force is **T** = T·**û**, giving you the three components Tx, Ty, Tz directly. This process — compute the position vector, find its magnitude, divide to get the unit vector, multiply by the force magnitude — should become automatic.

Once all forces in the problem are expressed in Cartesian form, equilibrium is mechanical: collect all the x-components and set their sum to zero, do the same for y and z. You get a system of three equations in however many unknowns you have. For a particle held by three cables, you typically have three unknown tensions — one equation per unknown. The geometry you computed at the start does all the structural work; the algebra at the end is just solving a 3×3 linear system.

A useful mental check: if you collapse the geometry to 2D (all forces in the x-y plane), your z-equation becomes 0 = 0 trivially, and the x and y equations should reproduce exactly what you would have gotten using your 2D equilibrium method. If they don't, you've made an error in the 3D setup. This check costs nothing and catches sign errors before you submit a wrong answer. The 3D skill is foundational for the space truss problems coming next, where you'll apply this exact process at every joint in a three-dimensional framework.
