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
status: validated
---

# Rigid Body Equilibrium: Spatial (3D) Analysis

## Core Idea
Three-dimensional equilibrium extends the planar case to six independent equations: ΣF_x = 0, ΣF_y = 0, ΣF_z = 0, and ΣM_x = 0, ΣM_y = 0, ΣM_z = 0. Complex spatial structures, machinery, and foundations require careful analysis in three dimensions using vector methods for moments and reactions.

## Questions

```yaml
- question: "A rigid body in three-dimensional space is supported only by a ball-and-socket joint. How many unknown reaction components does this support contribute to the equilibrium equations?"
  type: multiple-choice
  options:
    - "One — it provides only a single normal force perpendicular to the surface"
    - "Three — it prevents all three translations but permits all three rotations, giving three force unknowns"
    - "Six — it prevents all three translations and all three rotations"
    - "Two — it prevents vertical translation and one rotation"
  answer: 1
  explanation: "A ball-and-socket joint allows the connected body to rotate freely in any direction — it offers no resistance to rotation and therefore provides no moment reactions. It constrains only translation (the ball cannot leave the socket), contributing exactly three unknown force components (one per constrained direction). Compare this to a fixed support, which prevents all six motions and contributes six unknowns (three forces + three moments). Correctly identifying support types before writing equations is the foundational step in 3D statics."

- question: "Why does three-dimensional equilibrium require three independent moment equations rather than just one?"
  type: multiple-choice
  options:
    - "Three equations are needed because moment magnitudes are larger in 3D and require more constraints"
    - "A rigid body in 3D can rotate about three independent axes; preventing rotation about each requires a separate moment equation"
    - "Three moment equations are needed to handle statically indeterminate problems that one equation cannot resolve"
    - "The third moment equation is redundant but included for numerical verification"
  answer: 1
  explanation: "In 3D, a rigid body can rotate about three independent axes (x, y, z). The single moment equation in 2D (ΣM_z = 0) addresses rotation about only the out-of-plane axis. In 3D, ΣM_x = 0, ΣM_y = 0, and ΣM_z = 0 are each independent — a body satisfying ΣM_z = 0 might still be free to rotate about the x-axis. Only all three equations together guarantee rotational equilibrium in all directions."

- question: "A fixed support in a three-dimensional structure contributes exactly three unknown reaction components to the equilibrium equations — one force per spatial direction."
  type: true-false
  answer: false
  explanation: "False. A fixed support prevents all six possible motions of a rigid body in 3D: translation in x, y, and z (three force reactions) and rotation about x, y, and z (three moment reactions). It contributes six unknowns, not three. This contrasts with a 2D fixed support, which contributes only three unknowns (two forces + one moment). Miscounting support reactions leads to incorrect determination of whether a problem is statically determinate, indeterminate, or a mechanism."

- question: "A ball-and-socket joint prevents all translational motion in three dimensions, contributing three force unknowns but zero moment unknowns to the equilibrium equations."
  type: true-false
  answer: true
  explanation: "True. The ball-and-socket joint allows the connected body to rotate freely in any direction, providing no resistance to rotation and therefore no moment reactions. It constrains only translation (three unknowns). This makes it analogous to a pin support in 2D (which also permits rotation), extended to three dimensions. Recognizing this correctly is essential for counting unknowns before writing equilibrium equations."

- question: "Why is counting the number of unknown support reactions and comparing it to the six equilibrium equations considered a necessary diagnostic step before attempting to solve a 3D equilibrium problem?"
  type: short-answer
  answer: "This counting determines whether the problem is solvable by statics alone. If unknowns equal six, the system is statically determinate and solvable. If unknowns exceed six, the system is statically indeterminate and requires additional compatibility equations. If unknowns are fewer than six, the body is a mechanism — it can still move and is not truly in equilibrium under arbitrary loading. Proceeding without this check can waste effort on an unsolvable or ill-posed problem."
  explanation: "The six equilibrium equations are six algebraic equations. Seven unknowns and six equations yield no unique solution — the system is indeterminate, requiring structural deformation analysis. Five unknowns mean the body has a free motion and cannot be in equilibrium under all loading conditions. This diagnostic step tells you what kind of problem you're facing before committing to a solution strategy, and it directly extends the counting skill developed for 2D systems."
```

## Explainer

In planar (2D) equilibrium, you had three equations: two force equations (ΣFₓ = 0, ΣFᵧ = 0) and one moment equation (ΣM_z = 0). These three equations are sufficient because a rigid body in a plane can only translate in two directions or rotate about a single axis perpendicular to the plane. When you move into three dimensions, a free rigid body has six possible independent motions — translation along x, y, and z, and rotation about x, y, and z axes. Equilibrium means preventing all six simultaneously, which requires exactly six independent equations.

The six equations ΣF_x = 0, ΣF_y = 0, ΣF_z = 0, ΣM_x = 0, ΣM_y = 0, ΣM_z = 0 encode this completely. The force equations ensure no net tendency to translate in any direction. The three moment equations ensure no net tendency to rotate about any axis. Unlike the planar case, where you could compute moments about a single point and get one equation, here you need moments about three independent axes to capture all possible rotation tendencies. This is why **vector cross products** become essential: computing a moment in 3D means evaluating M = r × F, which automatically produces a vector with components in all three directions.

The challenge in spatial problems is often setting up the support reactions correctly before writing any equations. A ball-and-socket joint prevents all three translations but allows all three rotations — contributing three unknown force components but zero moment reactions. A journal bearing (smooth cylindrical pin) may prevent two translations and two rotations, contributing up to four unknowns. A fixed support prevents all six motions and contributes six unknowns. Carefully counting reactions and comparing to the six equilibrium equations tells you immediately whether the problem is statically determinate (six unknowns, six equations), indeterminate (more unknowns than equations), or a mechanism (fewer than six unknowns — the body could still move). This counting step, which extends the skill you developed for 2D systems, is the diagnostic that determines whether a system can even be solved by statics alone.

A useful strategy when the reaction configuration is complex is to choose moment axes strategically. Just as in 2D you could choose a moment center that eliminates multiple unknowns, in 3D you can choose a moment axis parallel to an unknown force (eliminating it from that moment equation) or passing through a joint (eliminating its reactions). Strategic axis choice can decouple the system of equations, reducing the algebra dramatically. With three force equations and three well-chosen moment equations, spatial equilibrium problems are solvable — they just require the additional care of tracking vectors in three dimensions rather than scalars in a plane.
