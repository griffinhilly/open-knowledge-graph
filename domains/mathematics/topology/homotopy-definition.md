---
id: homotopy-definition
title: Homotopy of Continuous Maps
domain: mathematics
course: topology
prerequisites:
- id: continuity-topological-definition
  type: hard
- id: path-connected-spaces
  type: soft
builds-toward:
- fundamental-group-definition
tags:
- homotopy
- algebraic-topology
stage: formal-systems
status: draft
---

# Homotopy of Continuous Maps

## Core Idea
Maps f, g: X → Y are homotopic if there exists a continuous map H: X × [0,1] → Y with H(x,0) = f(x) and H(x,1) = g(x). Homotopy measures when maps are 'continuously deformable.' Homotopy equivalence is weaker than homeomorphism but strong enough to detect topological structure. Fundamental groups and higher homotopy groups are invariants of homotopy type.

## Explainer

You know continuity in the topological sense: a map f: X → Y is continuous if preimages of open sets are open. Homotopy asks a different question — not whether a single map is continuous, but whether two continuous maps can be continuously *deformed* into each other. Think of two rubber-band paths on a surface: can you slide one into the other without leaving the surface? That geometric intuition is exactly what the definition captures.

The formal definition introduces a **homotopy** H: X × [0, 1] → Y, a continuous map on the product of X with the unit interval. The parameter t ∈ [0, 1] plays the role of "time": at t = 0 you have H(x, 0) = f(x), and at t = 1 you have H(x, 1) = g(x). For each fixed t, the map Hₜ(x) = H(x, t) is a continuous map from X to Y. As t varies from 0 to 1, these maps form a continuous one-parameter family interpolating from f to g. Continuity of H as a whole (on the product space) is what ensures the deformation has no jumps or tears. When such an H exists, f and g are **homotopic**, written f ≃ g.

Homotopy is an equivalence relation on the set of continuous maps from X to Y — it is reflexive (H(x,t) = f(x) works), symmetric (reverse the parameter: H(x, 1−t)), and transitive (concatenate two homotopies, spending t ∈ [0,½] on the first and t ∈ [½,1] on the second). The equivalence classes are **homotopy classes of maps**. Two spaces X and Y are **homotopy equivalent** if there exist maps f: X → Y and g: Y → X such that g∘f ≃ id_X and f∘g ≃ id_Y. This is weaker than homeomorphism — homeomorphism requires a single map to be a perfect bijection with continuous inverse, while homotopy equivalence allows a round trip that deforms but does not tear. A disk and a point are homotopy equivalent (the disk can be continuously contracted to a point), even though they are not homeomorphic.

The importance of homotopy is that it defines **invariants**: properties preserved by homotopy equivalence that can distinguish spaces. The **fundamental group** π₁(X, x₀) — the set of homotopy classes of loops based at x₀ — is the first such invariant. A simply connected space has trivial fundamental group (every loop can be contracted to a point); a circle does not (loops that wind around cannot be unlooped). Homotopy thus provides the bridge between topology (continuous structure) and algebra (groups), which is the central program of algebraic topology. Mastering the definition here is the gateway to that entire subject.
