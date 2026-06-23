---
id: equilibrium-rigid-bodies
title: Equilibrium of Rigid Bodies
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: support-reactions-beams
  type: hard
- id: equivalent-force-systems
  type: hard
- id: static-equilibrium
  type: soft
- id: torque
  type: soft
- id: equilibrium-particles-3d
  type: soft
- id: free-body-diagram-method
  type: hard
- id: moment-of-force-3d
  type: soft
- id: support-reactions-classification
  type: soft
builds-toward:
- truss-method-of-joints
- frames-machines-analysis
- dry-friction-coulombs-law
tags:
- statics
- equilibrium
- rigid body
- moment equilibrium
stage: formal-systems
status: validated
---
# Equilibrium of Rigid Bodies

## Core Idea
A rigid body is in static equilibrium when both the resultant force and the resultant moment about any point are zero: ΣF = 0 and ΣM_O = 0. In 2D, this yields three scalar equations (ΣFx = 0, ΣFy = 0, ΣM_O = 0), permitting solution of three unknowns. Choosing the moment reference point at the intersection of unknown forces eliminates those unknowns from the moment equation. Statically determinate structures have exactly as many unknowns as equilibrium equations; indeterminate structures have surplus constraints requiring additional analysis.

## How It's Best Learned
Choose the moment point strategically to eliminate the most unknowns simultaneously. After solving, verify equilibrium about a second point as a check. For distributed loads, replace them with equivalent point loads (resultant force at centroid of the load diagram) before applying equilibrium.

## Common Misconceptions
- Choosing a poor moment point that unnecessarily includes multiple unknowns.
- Forgetting that distributed loads must be converted to resultant forces before summing moments.
- Confusing a statically indeterminate structure with one that is simply harder to analyze.

## Questions

```yaml
- question: "A simply supported beam carries a single vertical load. You write ΣFx = 0, ΣFy = 0, and ΣM_A = 0 for the three equilibrium equations. How many unknown support reactions can this system of equations solve?"
  type: multiple-choice
  options: ["1", "2", "3", "4"]
  answer: 2
  explanation: "In 2D, three independent equilibrium equations are available (ΣFx = 0, ΣFy = 0, ΣM = 0). A simply supported beam has exactly three unknown reactions (one horizontal pin component and two vertical supports), making it statically determinate — three equations solve three unknowns. Choosing four unknowns would make the system indeterminate."

- question: "When summing moments for a rigid body in equilibrium, the moment reference point should be located at the body's center of mass."
  type: true-false
  answer: false
  explanation: "The moment equilibrium condition ΣM_O = 0 holds for any reference point O when the body is in static equilibrium. The choice of reference point is a mathematical convenience, not a physical requirement. Strategically placing the reference point at the intersection of two or more unknown forces eliminates those unknowns from the moment equation, simplifying the algebra significantly."

- question: "Explain the strategy for choosing an optimal moment reference point when solving a rigid body equilibrium problem."
  type: short-answer
  answer: "Choose the moment reference point at the location where the most unknown forces intersect (i.e., pass through). A force passing through the moment point contributes zero moment (zero moment arm), so it drops out of the equation, leaving fewer unknowns to solve simultaneously."
  explanation: "Moment = Force × perpendicular distance. If the reference point lies on the line of action of an unknown force, the perpendicular distance is zero and that unknown does not appear in the moment equation. By choosing the point where the maximum number of unknowns intersect, you can often reduce the moment equation to a single unknown, which can be solved directly without simultaneous equations."
```

## Explainer

When you studied particle equilibrium, you required only that the net force on the particle be zero: ΣF = 0. A rigid body adds a second requirement — the net moment must also be zero about every point: ΣM_O = 0. The reason is that a rigid body has spatial extent: even if the net force is zero, forces could still cause the body to rotate. Equilibrium of a rigid body means no translation and no rotation.

In two dimensions, these conditions produce three independent scalar equations: ΣFx = 0, ΣFy = 0, and ΣM_O = 0 about any chosen point. Three equations can solve exactly three unknowns. When you have exactly three unknown support reactions, the structure is statically determinate — the equations fully determine the reactions. Add a fourth support and you have more unknowns than equations; additional information (deformation compatibility) is needed, and the structure is statically indeterminate. This distinction is fundamental: indeterminacy is not about difficulty, it is about whether equilibrium equations alone are sufficient.

The power of strategic moment point selection cannot be overstated. Any unknown force that passes through your chosen moment point contributes zero moment (zero moment arm), so it disappears from that equation. By placing the moment reference at the intersection of two unknown forces, you can often reduce the moment equation to a single unknown that solves directly. For a simply supported beam with a pin and a roller, summing moments about the pin eliminates the two pin reaction components at once, leaving only the roller reaction as the unknown — a one-step calculation.

Distributed loads require one more step before applying equilibrium: replace the distributed load with its statically equivalent point force. For a uniform distributed load of intensity w over length L, the resultant is wL acting at the centroid of the load diagram (the midpoint for a uniform load, a third-point for a triangular load). Only after this replacement can the force and moment equilibrium equations be applied. Skipping this step and treating the distributed load as a series of discrete forces — while technically correct — is far more laborious and unnecessary for rigid body analysis.
