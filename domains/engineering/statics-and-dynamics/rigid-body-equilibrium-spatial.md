---
id: rigid-body-equilibrium-spatial
title: 'Rigid Body Equilibrium: Spatial (3D) Analysis'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rigid-body-equilibrium-planar
  type: hard
- id: moment-of-force-3d
  type: soft
builds-toward:
- statically-determinate-analysis
tags:
- rigid body
- equilibrium
- spatial
- three-dimensional
- six equations
stage: formal-systems
status: draft
---

# Rigid Body Equilibrium: Spatial (3D) Analysis

## Core Idea
Three-dimensional equilibrium extends the planar case to six independent equations: ΣF_x = 0, ΣF_y = 0, ΣF_z = 0, and ΣM_x = 0, ΣM_y = 0, ΣM_z = 0. Complex spatial structures, machinery, and foundations require careful analysis in three dimensions using vector methods for moments and reactions.

## Explainer

In planar (2D) equilibrium, you had three equations: two force equations (ΣFₓ = 0, ΣFᵧ = 0) and one moment equation (ΣM_z = 0). These three equations are sufficient because a rigid body in a plane can only translate in two directions or rotate about a single axis perpendicular to the plane. When you move into three dimensions, a free rigid body has six possible independent motions — translation along x, y, and z, and rotation about x, y, and z axes. Equilibrium means preventing all six simultaneously, which requires exactly six independent equations.

The six equations ΣF_x = 0, ΣF_y = 0, ΣF_z = 0, ΣM_x = 0, ΣM_y = 0, ΣM_z = 0 encode this completely. The force equations ensure no net tendency to translate in any direction. The three moment equations ensure no net tendency to rotate about any axis. Unlike the planar case, where you could compute moments about a single point and get one equation, here you need moments about three independent axes to capture all possible rotation tendencies. This is why **vector cross products** become essential: computing a moment in 3D means evaluating M = r × F, which automatically produces a vector with components in all three directions.

The challenge in spatial problems is often setting up the support reactions correctly before writing any equations. A ball-and-socket joint prevents all three translations but allows all three rotations — contributing three unknown force components but zero moment reactions. A journal bearing (smooth cylindrical pin) may prevent two translations and two rotations, contributing up to four unknowns. A fixed support prevents all six motions and contributes six unknowns. Carefully counting reactions and comparing to the six equilibrium equations tells you immediately whether the problem is statically determinate (six unknowns, six equations), indeterminate (more unknowns than equations), or a mechanism (fewer than six unknowns — the body could still move). This counting step, which extends the skill you developed for 2D systems, is the diagnostic that determines whether a system can even be solved by statics alone.

A useful strategy when the reaction configuration is complex is to choose moment axes strategically. Just as in 2D you could choose a moment center that eliminates multiple unknowns, in 3D you can choose a moment axis parallel to an unknown force (eliminating it from that moment equation) or passing through a joint (eliminating its reactions). Strategic axis choice can decouple the system of equations, reducing the algebra dramatically. With three force equations and three well-chosen moment equations, spatial equilibrium problems are solvable — they just require the additional care of tracking vectors in three dimensions rather than scalars in a plane.
