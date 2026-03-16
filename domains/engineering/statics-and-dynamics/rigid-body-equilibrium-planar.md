---
id: rigid-body-equilibrium-planar
title: 'Rigid Body Equilibrium: Planar Analysis'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: resultant-of-force-moment-systems
  type: hard
- id: equilibrium-rigid-bodies
  type: soft
builds-toward:
- statically-determinate-analysis
- truss-joint-and-section-methods
- frame-and-machine-components
tags:
- rigid body
- equilibrium
- planar
- two-dimensional
- three equations
stage: formal-systems
status: draft
---

# Rigid Body Equilibrium: Planar Analysis

## Core Idea
For a rigid body in two-dimensional equilibrium, three independent equations must be satisfied: ΣF_x = 0, ΣF_y = 0, and ΣM = 0 about any point. These conditions ensure the body is both in translational and rotational equilibrium, with applications to beams, frames, and mechanism design.

## Explainer

From your prerequisite work on resultants and moment systems, you know that any force system acting on a rigid body can be reduced to a single resultant force plus a resultant couple. For a body to remain stationary, both must be zero — the resultant force must vanish (no net tendency to translate) and the resultant couple must vanish (no net tendency to rotate). In two dimensions, this gives exactly **three scalar equations**: force balance in x, force balance in y, and moment balance about any chosen point. Three equations means you can solve for at most three unknown quantities.

The moment equation is your most powerful tool, and the key is choosing the **moment center** wisely. The moment of a force about a point depends on the perpendicular distance from the point to the line of action of the force. If you pick a point where one or more unknown forces intersect (i.e., their lines of action pass through your chosen point), those forces contribute zero moment — they vanish from the moment equation, leaving you with a simpler equation. For a beam with a pin support and a roller, taking moments about the pin eliminates both pin reaction components and lets you solve for the roller reaction directly. This technique of strategic moment center selection is what separates efficient from clumsy free-body analysis.

The free-body diagram is non-negotiable. Every surface that contacts the body exerts a reaction force, and you must correctly model each contact type: a **roller** provides a force perpendicular to the surface (one unknown), a **pin** provides a force in any direction (two unknowns: x and y components), and a **fixed support** provides a force in any direction plus a moment couple (three unknowns). Draw all applied loads and reactions, then apply the three equilibrium equations. With three equations you can determine at most three unknowns — a beam with a pin and roller is exactly **statically determinate** (three equations, three unknowns).

The limitation of this analysis is precisely three unknowns. Add a second pin — now you have four unknowns (two from each pin) but still only three equations — the system becomes **statically indeterminate** and you cannot solve from equilibrium alone. You would need to include deformation compatibility (a topic for mechanics of materials). Recognizing whether a system is determinate or indeterminate before setting up equations is a key engineering judgment skill. Count the unknowns from supports, count the independent equilibrium equations, and if the unknowns exceed the equations, look for additional constraints in the geometry or the deformation of the structure.
