---
id: index-theory-planar-systems
title: Index Theory for Planar Systems
domain: physics
course: nonlinear-dynamics
prerequisites:
- id: poincare-bendixson-theorem
  type: hard
- id: fixed-points-and-stability
  type: hard
tags:
- index-theory
- winding-number
- topological-methods
- planar-dynamics
stage: expert
status: validated
---

# Index Theory for Planar Systems

## Core Idea
The index of a fixed point measures how many times the vector field rotates as you traverse a small closed curve around it. Nodes, spirals, and centers all have index +1; saddle points have index -1. The index is a topological invariant — it can't change under continuous deformation of the vector field. The index of any closed curve equals the sum of the indices of the fixed points enclosed, and any limit cycle must enclose fixed points whose indices sum to +1. These constraints restrict what phase portrait configurations are topologically possible.

## Questions

```yaml
- question: "A limit cycle in a planar system encloses three fixed points. If two of them are saddles (index -1 each), what must be true about the third?"
  type: multiple-choice
  options:
    - "It must be a saddle as well — saddles attract limit cycles"
    - "It must have index +3 — to make the total index equal +1. But standard fixed points have index ±1, so this configuration is impossible"
    - "It must have index +1 (a node, spiral, or center) — but three fixed points with indices -1, -1, +1 sum to -1, not +1. So this configuration is impossible with only these three"
    - "It could be any type of fixed point — the index theorem places no constraints on enclosed fixed points"
  answer: 2
  explanation: "The index of a limit cycle is +1, and it must equal the sum of indices of enclosed fixed points. Two saddles contribute -2, and a single node/spiral contributes +1, giving a total of -1 ≠ +1. This configuration is impossible. You would need at least two nodes/spirals (contributing +2) plus two saddles (-2) to reach the required sum of +1... but that requires a fourth fixed point. Index theory thus constrains which phase portrait configurations can support limit cycles."

- question: "The index of an isolated fixed point can be determined from the eigenvalues of the Jacobian."
  type: true-false
  answer: true
  explanation: "For a hyperbolic fixed point (no zero or purely imaginary eigenvalues), the index is determined by the sign of the determinant of the Jacobian. If det(Df) > 0, the index is +1 (node, spiral, center). If det(Df) < 0, the index is -1 (saddle). This follows because the index counts the net rotation of the vector field, which is related to how many times the field's direction cycles as you go around the point. Two negative eigenvalues (stable node): arrows all point inward, rotating once → index +1. One positive, one negative (saddle): the field reverses on two axes → index -1."

- question: "On a sphere, the sum of the indices of all fixed points of a smooth vector field must equal 2 (the Euler characteristic of the sphere). What does this imply about combing a hairy ball?"
  type: short-answer
  answer: "Any smooth tangent vector field on a sphere must have fixed points whose indices sum to 2. Since index ±1 are the generic values, the minimum number of fixed points is one (with index +2, a dipole — though this is non-generic) or two (each with index +1, like the north and south poles of a rotational flow). It is impossible to have a smooth, nonvanishing tangent vector field on a sphere — this is the hairy ball theorem. You can't comb a hairy ball flat without creating at least one cowlick (a point where the vector field vanishes)."
  explanation: "The Poincare-Hopf theorem generalizes index theory to arbitrary closed surfaces: the sum of indices equals the Euler characteristic χ. For a sphere χ = 2, for a torus χ = 0 (so a vector field with no fixed points IS possible on a torus — you can comb a hairy donut). This connects dynamical systems to topology in a deep way: the global topology of the space constrains what flows are possible on it."

- question: "A student draws a phase portrait with two stable nodes and nothing else (no saddle points). Can this be correct for a flow on the plane?"
  type: multiple-choice
  options:
    - "Yes — two stable nodes can coexist with all trajectories going to one or the other"
    - "No — two stable nodes (each index +1) require at least one saddle (index -1) between them to separate their basins of attraction"
    - "Yes, but only if the system is non-autonomous"
    - "No — a planar system can have at most one stable fixed point"
  answer: 1
  explanation: "On the plane (not a closed surface), the index theorem doesn't require a global sum constraint. However, the topological structure of basins of attraction forces a saddle between any two stable nodes — the basins must be separated by a boundary, and that boundary must contain a saddle point (or extend to infinity in a specific way). Generically, two attractors in the plane require a saddle between them whose stable manifold forms the separatrix. This is a practical consequence of the flow topology, even though the formal index theorem on the (non-compact) plane is more subtle."
```

## Explainer

Index theory adds a topological lens to the study of planar dynamics. Rather than analyzing individual trajectories, it assigns an integer — the index — to each fixed point based on how the vector field wraps around it. This single number encodes global information: it constrains which fixed points can coexist, which configurations can support limit cycles, and how phase portraits on different surfaces must behave.

The definition is geometric. Pick a fixed point, draw a small closed curve around it (avoiding other fixed points), and walk along the curve while tracking the direction of the vector field. The index is the net number of counterclockwise rotations the vector field completes as you traverse the curve once. For a stable node, all arrows point inward — as you go around, the vector field direction rotates once counterclockwise, giving index +1. For a saddle, the alternating inward-outward pattern causes the field direction to rotate once clockwise, giving index -1. Unstable nodes and spirals also give +1; only saddles give -1 (among generic fixed points). The index is a topological invariant: it can't change under continuous deformations of the system that don't create or destroy fixed points.

The key theorem is additive: the index of any closed curve equals the sum of the indices of all fixed points inside it. For a limit cycle (which is itself a closed curve), the index must be +1. This immediately constrains what fixed points a limit cycle can enclose. A single node or spiral (index +1): yes. A single saddle (index -1): no — a limit cycle cannot surround a lone saddle. Two saddles and three nodes (+3 - 2 = +1): yes. These bookkeeping constraints are surprisingly powerful for ruling out proposed phase portraits.

On closed surfaces, index theory becomes even more powerful through the Poincare-Hopf theorem: the sum of indices of all fixed points equals the Euler characteristic of the surface. For a sphere, this sum is 2, implying that every smooth flow on a sphere must have fixed points (the hairy ball theorem). For a torus, the sum is 0, so fixed-point-free flows are possible. This connection between dynamics and topology — that the shape of the space constrains the behavior of flows on it — is one of the deepest themes in mathematics, linking differential equations to algebraic topology.
