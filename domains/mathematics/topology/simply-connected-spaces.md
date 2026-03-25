---
id: simply-connected-spaces
title: Simply Connected Spaces
domain: mathematics
course: topology
prerequisites:
- id: fundamental-group-definition
  type: hard
- id: locally-connected-spaces
  type: soft
- id: connected-components-decomposition
  type: soft
builds-toward:
- covering-spaces
- van-kampen-theorem
tags:
- simply-connected
- trivial-fundamental-group
- contractible
stage: advanced
status: validated
---
# Simply Connected Spaces

## Core Idea
A space is simply connected if it is path-connected and its fundamental group is trivial (every loop is homotopic to the constant loop). Intuitively, a simply connected space is path-connected with no 'holes.' Simply connected spaces form an important class in algebraic topology where global properties are heavily constrained by topology.

## Questions

```yaml
- question: "Which of the following spaces is NOT simply connected?"
  type: multiple-choice
  options:
    - "The plane ℝ²"
    - "The 2-sphere S²"
    - "The circle S¹"
    - "Any contractible space"
  answer: 2
  explanation: "S¹ is not simply connected because its fundamental group π₁(S¹) = ℤ — a loop that winds around the circle once cannot be contracted to a point without leaving S¹. The plane ℝ² and any contractible space are simply connected (π₁ = trivial). S² is also simply connected: any loop on a sphere can be continuously pulled to the north pole, so π₁(S²) = {e}. The winding-number obstruction is the precise 1-dimensional 'hole' that simple connectivity rules out."

- question: "You remove a single point from ℝ². What happens to the simple connectivity of the resulting space?"
  type: multiple-choice
  options:
    - "It remains simply connected — removing one point doesn't create a loop"
    - "It loses simple connectivity — the puncture creates a non-contractible loop"
    - "It becomes simply connected with a different basepoint far from the removed point"
    - "Simple connectivity is undefined for spaces with missing points"
  answer: 1
  explanation: "ℝ² minus a point deformation retracts onto a circle surrounding that point, so it has fundamental group π₁ = ℤ — the same as S¹. A loop encircling the puncture cannot be contracted to a point without passing through the hole. Simple connectivity fails everywhere, not just near the removed point, because the group is a topological invariant of the whole space. This is why complex analysis requires simply connected domains: if the domain has a puncture, contour integrals around it may be non-zero."

- question: "A simply connected space must have trivial homotopy groups πₙ for all n ≥ 1."
  type: true-false
  answer: false
  explanation: "Simple connectivity only requires π₁ = {e} (trivial fundamental group). Higher homotopy groups can be non-trivial. The 2-sphere S² is simply connected — every loop on S² can be contracted to a point — yet π₂(S²) = ℤ, reflecting the existence of non-contractible 2-spheres mapped into S². Simple connectivity rules out 1-dimensional holes, not higher-dimensional ones. This is why it appears as a hypothesis in theorems about 1-dimensional objects (paths, loops, line integrals) but not as a blanket guarantee of topological triviality."

- question: "The circle S¹ is not simply connected because there exist loops based at any point that cannot be continuously deformed to the constant loop while staying in S¹."
  type: true-false
  answer: true
  explanation: "This is precisely the definition of failing simple connectivity. A loop that winds around S¹ once represents the generator of π₁(S¹) = ℤ, and no continuous deformation within S¹ can shrink it to a point. Any deformation that tries to collapse it would have to pass through the 'inside' of the circle, which is not part of S¹. The integer winding number is a topological invariant — it cannot change under continuous deformation — so the loop and the constant loop are in different homotopy classes."

- question: "Why does Cauchy's integral theorem in complex analysis require the domain to be simply connected, and what goes wrong if the domain has a 'hole'?"
  type: short-answer
  answer: "Cauchy's theorem states that the integral of a holomorphic function around any closed loop in a simply connected domain is zero. Simple connectivity ensures that any loop in the domain bounds a disk also contained in the domain — the loop can be contracted, and the integral over each infinitesimal piece cancels. If the domain has a hole (e.g., ℂ minus a point), a loop encircling the hole cannot be contracted; its integral may be non-zero (it equals 2πi times the residue at the missing point). The hole creates a non-contractible loop, and the path-dependence of the integral is precisely the topological obstruction that simple connectivity eliminates."
  explanation: "This is the canonical application of simple connectivity in analysis. The 1/z function on ℂ \ {0} integrates to 2πi around the origin — not zero — because the puncture prevents the loop from being contracted. In a simply connected domain, no such obstruction exists, and holomorphic functions automatically have antiderivatives. The algebraic topology of the domain (π₁) directly controls the analytic behavior of functions on it."
```

## Explainer

From your prerequisite on the **fundamental group**, you know that π₁(X, x₀) records the homotopy classes of loops based at x₀ — loops that can be continuously deformed into each other are identified, and the group operation is concatenation of loops. A **simply connected space** is one where this group is trivial: π₁(X, x₀) = {e}, the group with one element. Combined with path-connectedness, this means every loop in X can be continuously contracted to a point.

The intuition is best built through examples. The plane ℝ² is simply connected: any loop drawn in the plane can be shrunk to a point without leaving the plane. The 2-sphere S² is also simply connected: any loop on a sphere can be pulled to the north pole. But the circle S¹ is not simply connected — a loop that goes around the circle once cannot be contracted to a point without leaving S¹. The **fundamental group of S¹ is ℤ**, with the integer recording how many times a loop winds around. Similarly, the torus T² = S¹ × S¹ has π₁ = ℤ × ℤ, capturing two independent types of non-contractible loops (going around the hole, and going through the hole). The "holes" that obstruct simple connectivity are 1-dimensional tunnels or punctures — removing a point from ℝ² creates a copy of ℝ² \ {0}, which deformation retracts to S¹ and so has π₁ = ℤ.

A subtlety: simple connectivity is specifically about **1-dimensional** holes. A space can be simply connected yet still have interesting higher homotopy groups. The 2-sphere S² is simply connected (no 1-dimensional loops) but has nontrivial π₂ — there are 2-spheres worth of holes. The simply connected condition rules out the "simplest" kind of topological obstruction, which is why it appears as a hypothesis in many theorems. In complex analysis, the proof that every holomorphic function on a simply connected domain has an antiderivative, and Cauchy's theorem that loop integrals vanish, both hinge on simply connectivity: the absence of 1-dimensional holes is exactly what prevents line integrals from being path-dependent.

Simply connected spaces are the "nicely behaved" spaces for much of algebraic topology. **Covering space theory** is most transparent over a simply connected base: the universal cover of any connected, locally path-connected, semi-locally simply connected space is itself simply connected, and it is the "largest" covering space. The **van Kampen theorem**, which you will study next, computes fundamental groups by breaking a space into simpler pieces — and the pieces you want to be "invisible" to the fundamental group computation are exactly the simply connected ones. Simply connected spaces also arise in differential geometry (the Poincaré conjecture concerns which 3-manifolds are simply connected and topologically equivalent to the 3-sphere) and physics (gauge theories and the existence of potentials are constrained by the topology of configuration spaces).
