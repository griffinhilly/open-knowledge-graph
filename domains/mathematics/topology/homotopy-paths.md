---
id: homotopy-paths
title: Homotopy of Paths
domain: mathematics
course: topology
prerequisites:
- id: continuous-functions-topology
  type: hard
- id: product-topology
  type: hard
builds-toward:
- fundamental-group-definition
- covering-spaces
tags:
- homotopy
- paths
stage: advanced
status: draft
---

# Homotopy of Paths

## Core Idea
Two paths γ, σ: [0,1] → X with the same endpoints are homotopic if there is a continuous deformation H: [0,1] × [0,1] → X connecting them while keeping endpoints fixed. Homotopy is an equivalence relation on paths.

## Explainer

A **path** in a topological space X is a continuous function γ: [0,1] → X — it traces a journey from the starting point γ(0) to the endpoint γ(1). You already know what continuous functions in topology mean: preimages of open sets are open. Two paths with the same endpoints might take wildly different routes through X. The question homotopy theory asks is: can one path be continuously deformed into the other without lifting the pen from the space and without moving the endpoints?

The formal answer is given by a **homotopy**: a continuous map H: [0,1] × [0,1] → X satisfying H(s, 0) = γ(s) and H(s, 1) = σ(s) for all s (the "time slices" start at γ and end at σ), and H(0, t) = γ(0) = σ(0) and H(1, t) = γ(1) = σ(1) for all t (the endpoints stay fixed throughout the deformation). Think of the first coordinate s as position along the path and the second coordinate t as time. At time t = 0 you are walking along γ; at time t = 1 you are walking along σ; at intermediate times t you are walking along some intermediate path H(·, t). The product topology on [0,1] × [0,1] — which you know from your prerequisite — is exactly the right structure to make "continuous deformation" precise.

The geometric intuition is that of a rubber band being slid along a surface. If X is the plane ℝ², any two paths with the same endpoints are homotopic: you can always slide one smoothly into the other, because the plane has no obstacles. But if X is the plane with a hole punched out — say ℝ² minus the origin — then a path that loops around the hole cannot be deformed into one that does not loop around it. The hole is an obstruction. This is the heart of algebraic topology: the topological structure of X is detected by asking which paths are homotopic to which others.

Homotopy is an **equivalence relation** on the set of paths from p to q: it is reflexive (every path is homotopic to itself via the constant deformation), symmetric (run the deformation backwards), and transitive (concatenate the two deformations in time). The equivalence classes under homotopy — called **homotopy classes** — are the objects that will be combined in the next topic to form the **fundamental group**. Two spaces that have the same pattern of homotopy classes (in a precise sense) are topologically "the same" from the perspective of path structure. Homotopy of paths is thus not just an isolated definition but the foundation of a powerful invariant for distinguishing topological spaces.
