---
id: particle-dynamics-accelerated-motion
title: Particle Dynamics and Accelerated Motion
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: curvilinear-motion-particles
  type: hard
- id: dynamics-newtons-second-law
  type: soft
builds-toward:
- work-energy-systems-analysis
- linear-momentum-impulse-systems
tags:
- dynamics
- Newton's second law
- force
- mass
- acceleration
- F=ma
stage: formal-systems
status: draft
---

# Particle Dynamics and Accelerated Motion

## Core Idea
Newton's second law, F = ma, relates the net force on a particle to its mass and acceleration, forming the foundation of kinetics. Dynamic equilibrium (d'Alembert's principle) treats inertial forces as applied forces, converting dynamics problems into statics-like equations solvable through free-body diagrams and equilibrium.

## Explainer

Up to now, you have analyzed particles in equilibrium — the net force was zero, and everything was stationary or moving at constant velocity. Kinetics begins when the net force is not zero. **Newton's second law**, ΣF = ma, tells you that the net force vector equals the product of mass and the acceleration vector. This is the bridge between the geometry of motion (kinematics, which you studied in curvilinear motion) and the forces that cause it.

The procedure for solving kinetics problems is a direct extension of your equilibrium FBD technique. Draw a free-body diagram showing all forces on the particle — gravity, normal forces, tension, friction — exactly as you would for a statics problem. Then write ΣF = ma along each coordinate axis. In Cartesian coordinates: ΣFx = max and ΣFy = may. In the normal-tangential coordinate system you learned for curvilinear motion, the equations become ΣFn = m·(v²/ρ) (centripetal acceleration directed toward the center of curvature) and ΣFt = m·(dv/dt) (tangential acceleration along the path). Choosing the right coordinate system — Cartesian, polar, or normal-tangential — is the first decision in any dynamics problem, and you make it based on the geometry of the motion.

**D'Alembert's principle** offers an alternative formulation that many engineers find intuitive. Add a fictitious **inertial force** of magnitude ma directed opposite to the acceleration, and the system returns to formal equilibrium: ΣF - ma = 0. This converts every dynamics problem into the format of a statics problem. You can then apply the same moment-balance and force-balance techniques you already know. Critics argue this is conceptually misleading (the inertial force is not a real force), but it is algebraically equivalent and widely used in practice, especially for systems with mixed static and dynamic loads.

The key practical skill is correctly identifying the direction of acceleration before setting up equations. On a banked curve, the acceleration points horizontally toward the center of the turn — not along the road surface. In circular orbital motion, the acceleration is centripetal, perpendicular to velocity. Confusing the direction of acceleration (which appears on the right side of ΣF = ma) with the direction of motion or velocity is the most common error. Draw the acceleration arrow on a separate kinetic diagram alongside your FBD, and check that your ΣF equations' right-hand sides match its direction and magnitude before solving.
