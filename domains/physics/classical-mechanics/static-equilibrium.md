---
id: static-equilibrium
title: Static Equilibrium
domain: physics
course: classical-mechanics
prerequisites:
- id: free-body-diagrams
  type: hard
- id: torque
  type: hard
- id: newtons-first-law
  type: hard
- id: systems-elimination
  type: soft
- id: vectors-in-two-dimensions
  type: soft
builds-toward:
- rotational-dynamics
tags:
- equilibrium
- static
- torque
- force-balance
stage: abstract-reasoning
status: validated
---

# Static Equilibrium

## Core Idea
A rigid body is in static equilibrium when both the net force and the net torque on it are zero: ΣF = 0 and Στ = 0. The torque equation provides additional constraints beyond force balance and is essential for determining where forces act (e.g., normal force position under a beam). The choice of pivot for computing torques is arbitrary — any convenient point may be chosen, often one where unknown forces are applied to eliminate them from the equation.

## How It's Best Learned
Solve beam and ladder problems: draw the FBD, write ΣFx = 0, ΣFy = 0, and Στ = 0 about a strategic pivot. Practice choosing the pivot wisely — placing it at the point of application of an unknown force often simplifies algebra.

## Common Misconceptions
- Thinking the torque pivot must be a physical support point: it can be any point.
- Setting up torque equations without specifying the sign convention for clockwise vs. counterclockwise.

## Explainer

From your study of free-body diagrams, torque, and Newton's first law, you have all the tools needed to analyze rigid objects that are not moving. Newton's first law tells you that an object in equilibrium has zero net force. Your study of torque adds a second, independent condition: an object that is not rotating — one in rotational equilibrium — has zero net torque. **Static equilibrium** requires *both*: ΣF = 0 and Στ = 0. Neither condition alone is sufficient, and understanding why is the key to mastering this topic.

The reason ΣF = 0 is not enough is that forces can cause rotation without causing linear acceleration of the center of mass. Imagine two equal and opposite forces applied to opposite ends of a beam — the net force is zero, but the beam will spin. The torque equation adds the rotational constraint. In two-dimensional problems, this gives three independent scalar equations: ΣF_x = 0, ΣF_y = 0, and Στ = 0 about any chosen pivot. Three equations allow you to solve for up to three unknowns — typically the magnitudes of unknown support forces and where they act. When you have exactly three unknowns and three equations, the system is **statically determinate** and has a unique solution.

The most powerful technique in static equilibrium is **strategic pivot selection**. Since the torque condition Στ = 0 must hold about *any* point you choose, you can pick whichever pivot makes the algebra simplest. The standard strategy is to place the pivot at the point where an unknown force acts: because torque equals force times perpendicular moment arm, an unknown force acting right at the pivot has a zero moment arm and contributes zero torque — it drops out of the equation entirely. For a beam supported at one end and resting against a wall at the other, placing the pivot at the base support eliminates the base reaction from the torque equation, leaving only the wall force and gravity, which is typically trivial to solve.

Consider the classic ladder problem: a uniform ladder of mass *m* leans against a frictionless wall, its base resting on rough ground. Four forces act on the ladder — gravity at the center of mass, the wall's normal force (horizontal), the ground's normal force (vertical), and friction from the ground (horizontal). The procedure is: draw a complete free-body diagram, write ΣF_x = 0 and ΣF_y = 0, then write Στ = 0 about the base of the ladder. Placing the pivot at the base eliminates both ground forces from the torque equation, leaving an equation containing only the wall normal force and gravity — solvable immediately for the wall force. Substituting back into the force equations then gives the ground forces. This sequence — FBD, force equations, strategic torque equation — applies to every static equilibrium problem you will encounter.
