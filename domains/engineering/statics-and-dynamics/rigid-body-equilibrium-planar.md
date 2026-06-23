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
- id: particle-equilibrium-conditions
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
status: validated
---

# Rigid Body Equilibrium: Planar Analysis

## Core Idea
For a rigid body in two-dimensional equilibrium, three independent equations must be satisfied: ΣF_x = 0, ΣF_y = 0, and ΣM = 0 about any point. These conditions ensure the body is both in translational and rotational equilibrium, with applications to beams, frames, and mechanism design.

## Questions

```yaml
- question: "A horizontal beam is supported by a pin at point A (left end) and a roller at point B (right end), with a downward load applied at the midpoint. You want to find the roller reaction at B using a single equation. What is the most efficient strategy?"
  type: multiple-choice
  options:
    - "Sum all forces in the x-direction and set equal to zero"
    - "Sum all forces in the y-direction and solve — B appears in the equation with other unknowns"
    - "Take moments about point A, eliminating both pin reaction components and solving for B directly"
    - "Take moments about the midpoint of the beam, where moments from symmetric loads cancel"
  answer: 2
  explanation: "Taking moments about point A is the efficient choice because the pin at A introduces two unknown force components (Ax and Ay), both of which act through point A and therefore contribute zero moment about A. They vanish from the moment equation entirely, leaving a single equation with B as the only unknown — solvable in one step. Summing forces in y (option B) includes both Ay and B as unknowns, requiring simultaneous equations. This 'strategic moment center' technique is the core skill of efficient planar equilibrium analysis."

- question: "A beam is attached to a wall with a fixed (cantilever) support at one end. How many unknown reaction components does this support provide?"
  type: multiple-choice
  options:
    - "One — a force perpendicular to the wall surface"
    - "Two — horizontal and vertical force components"
    - "Three — horizontal force, vertical force, and a moment couple"
    - "Four — two force components and two independent moment components"
  answer: 2
  explanation: "A fixed support prevents all translation and all rotation at the attachment point. In 2D, preventing translation requires two force components (x and y); preventing rotation requires a moment couple. This gives three unknowns. A roller provides only one unknown (force perpendicular to the surface); a pin provides two (x and y force components, free to rotate). Correctly counting unknowns per support type is essential for determining whether a system is statically determinate before setting up equations."

- question: "For a planar rigid body in equilibrium, the moment equation ΣM = 0 can primarily be validly applied about the body's centroid."
  type: true-false
  answer: false
  explanation: "The moment equation ΣM = 0 is valid about any point in the plane — not just the centroid, not just a support point. The choice of moment center affects which unknowns appear in the equation (forces through the chosen point contribute zero moment), but the equilibrium condition itself holds about any point. This freedom to choose the moment center strategically — placing it where unknowns intersect to eliminate them from the equation — is the key to efficient analysis."

- question: "A planar rigid body supported by two pins has more unknown reaction components than the three equilibrium equations can solve, making it statically indeterminate."
  type: true-false
  answer: true
  explanation: "Each pin support in 2D provides two unknown force components (x and y). Two pins together give four unknowns, but planar equilibrium provides only three independent equations (ΣFx = 0, ΣFy = 0, ΣM = 0). With four unknowns and three equations, the system is statically indeterminate to the first degree — you cannot find the reactions from equilibrium alone. Solving it requires incorporating the body's deformation (compatibility equations from mechanics of materials). Recognizing this before writing equations saves significant wasted effort."

- question: "What is the strategic advantage of choosing a moment center at the intersection of multiple unknown forces, and how does this simplify equilibrium analysis?"
  type: short-answer
  answer: "A force contributes zero moment about any point on its line of action — because the perpendicular distance from that point to the force's line of action is zero. If the moment center lies at the intersection of two unknown forces, both of those unknowns drop out of the moment equation simultaneously, leaving a simpler equation (possibly with only one unknown) that can be solved directly without simultaneous equations. For a beam with a pin at A, taking moments about A eliminates both pin components at once, allowing the roller reaction to be found in one step. This reduces the algebra from a system of equations to a single equation."
  explanation: "This technique scales: if you choose a moment center at the intersection of all unknowns except one, you solve for that remaining unknown immediately. Strategic moment center selection is what separates an efficient statics solution from a clumsy one that solves three equations in three unknowns simultaneously when one equation would have sufficed."
```

## Explainer

From your prerequisite work on resultants and moment systems, you know that any force system acting on a rigid body can be reduced to a single resultant force plus a resultant couple. For a body to remain stationary, both must be zero — the resultant force must vanish (no net tendency to translate) and the resultant couple must vanish (no net tendency to rotate). In two dimensions, this gives exactly **three scalar equations**: force balance in x, force balance in y, and moment balance about any chosen point. Three equations means you can solve for at most three unknown quantities.

The moment equation is your most powerful tool, and the key is choosing the **moment center** wisely. The moment of a force about a point depends on the perpendicular distance from the point to the line of action of the force. If you pick a point where one or more unknown forces intersect (i.e., their lines of action pass through your chosen point), those forces contribute zero moment — they vanish from the moment equation, leaving you with a simpler equation. For a beam with a pin support and a roller, taking moments about the pin eliminates both pin reaction components and lets you solve for the roller reaction directly. This technique of strategic moment center selection is what separates efficient from clumsy free-body analysis.

The free-body diagram is non-negotiable. Every surface that contacts the body exerts a reaction force, and you must correctly model each contact type: a **roller** provides a force perpendicular to the surface (one unknown), a **pin** provides a force in any direction (two unknowns: x and y components), and a **fixed support** provides a force in any direction plus a moment couple (three unknowns). Draw all applied loads and reactions, then apply the three equilibrium equations. With three equations you can determine at most three unknowns — a beam with a pin and roller is exactly **statically determinate** (three equations, three unknowns).

The limitation of this analysis is precisely three unknowns. Add a second pin — now you have four unknowns (two from each pin) but still only three equations — the system becomes **statically indeterminate** and you cannot solve from equilibrium alone. You would need to include deformation compatibility (a topic for mechanics of materials). Recognizing whether a system is determinate or indeterminate before setting up equations is a key engineering judgment skill. Count the unknowns from supports, count the independent equilibrium equations, and if the unknowns exceed the equations, look for additional constraints in the geometry or the deformation of the structure.
