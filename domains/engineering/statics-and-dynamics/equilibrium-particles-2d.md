---
id: equilibrium-particles-2d
title: Equilibrium of Particles in 2D
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: force-systems-resultants
  type: hard
- id: free-body-diagrams
  type: hard
- id: newtons-first-law
  type: hard
builds-toward:
- equilibrium-particles-3d
- equilibrium-rigid-bodies
- truss-method-of-joints
tags:
- statics
- equilibrium
- particles
- 2D
- free body diagram
stage: abstract-reasoning
status: validated
---

# Equilibrium of Particles in 2D

## Core Idea
A particle is in static equilibrium when the vector sum of all forces acting on it is zero: ΣF = 0. In 2D, this yields two scalar equations — ΣFx = 0 and ΣFy = 0 — allowing solution of up to two unknowns. The free body diagram is essential: isolate the particle, remove supports, and draw all external forces including reaction forces. Tension in cables, normal forces, applied loads, and weight are the most common force types.

## How It's Best Learned
Always draw and label the free body diagram completely before writing equilibrium equations. Assign unknowns consistent directions and let the math determine sign. Check solutions by verifying both equations are satisfied.

## Common Misconceptions
- Including internal forces or forces acting on other bodies in the free body diagram.
- Forgetting reaction forces at constraints (cables, rollers, pins).
- Assuming all cable tensions are equal without justification.

## Explainer

Newton's first law — your prerequisite — says that an object with no net force experiences no acceleration. Static equilibrium is simply that principle applied to the special case where velocity is also zero: nothing moves, nothing accelerates, all forces balance perfectly. The condition ΣF = 0 is not a coincidence or a convention; it is Newton's first law in vector form. In 2D, this one vector equation splits into two independent scalar equations, ΣFx = 0 and ΣFy = 0, giving you two equations to work with. That means you can solve for at most two unknown force quantities from a single equilibrium problem.

The **free body diagram (FBD)** is the operational heart of the method. The logic is precise: you mentally cut away everything surrounding the particle and replace the removed objects with the forces they exerted. A cable doesn't just "attach" — it pulls with a tension force directed along the cable. A smooth surface doesn't just "support" — it pushes with a normal force perpendicular to the surface. Weight pulls straight down with magnitude mg. Drawing the FBD correctly is not bookkeeping — it is the step that defines the physics. If you include forces that act on *other* objects, or omit reaction forces from constraints, your equations describe the wrong problem. The math after the FBD is just arithmetic.

Once the FBD is complete, apply the equilibrium equations by projecting every force onto your chosen x and y axes. The choice of axes is yours: horizontal and vertical is standard, but tilting your axes to align with an inclined surface often eliminates unknown components from one of the equations, making the algebra simpler. Assign unknown forces a positive assumed direction; if the solution gives a negative value, the force actually acts in the opposite direction. This is not an error — it is the math correcting your initial guess. Never flip the arrow and re-solve; just interpret the negative sign.

A useful check is to count unknowns before writing equations. Two equilibrium equations in 2D can solve for exactly two unknowns. If your FBD has three unknown forces, you cannot solve the problem with equilibrium alone — the problem is **statically indeterminate**. If it has only one unknown, you have a check available. Real-world examples where this matters: a hanging traffic light on two cables at different angles, a boat anchor held by two ropes, or a weight suspended from a frictionless pulley. In each case, the geometry of the cables and the condition ΣF = 0 completely determine the tensions — no guessing, no measuring, just the constraint that all forces cancel.
