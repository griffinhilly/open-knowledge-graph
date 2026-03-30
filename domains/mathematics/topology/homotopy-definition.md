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
stage: advanced
status: validated
---

# Homotopy of Continuous Maps

## Core Idea
Maps f, g: X → Y are homotopic if there exists a continuous map H: X × [0,1] → Y with H(x,0) = f(x) and H(x,1) = g(x). Homotopy measures when maps are 'continuously deformable.' Homotopy equivalence is weaker than homeomorphism but strong enough to detect topological structure. Fundamental groups and higher homotopy groups are invariants of homotopy type.

## Questions

```yaml
- question: "A student claims: 'A disk D² and a single point {p} cannot be homotopy equivalent, because D² has infinitely many points while {p} has only one — you cannot continuously deform one into the other.' Which response is correct?"
  type: multiple-choice
  options:
    - "The student is right: homotopy equivalence requires the spaces to be homeomorphic, and D² and {p} are not homeomorphic."
    - "The student is wrong: D² and {p} are homotopy equivalent because the constant map D² → {p} and the inclusion {p} → D² compose (in both orders) to maps homotopic to the respective identity maps."
    - "The student is right that homotopy equivalence fails, but the reason is that D² is 2-dimensional while {p} is 0-dimensional."
    - "The student is partially right: D² and {p} are path-connected but not homotopy equivalent."
  answer: 1
  explanation: "Homotopy equivalence is strictly weaker than homeomorphism. Two spaces are homotopy equivalent if there are maps f: X → Y and g: Y → X with g∘f ≃ id_X and f∘g ≃ id_Y. For D² and {p}: the constant map c: D² → {p} and inclusion ι: {p} → D² satisfy ι∘c(x) = p for all x, and the straight-line homotopy H(x,t) = (1−t)x contracts D² to its center — a homotopy from ι∘c to id_{D²}. The other composition is automatically the identity. So D² ≃ {p}, even though they are very different as spaces."

- question: "What is the defining property of a homotopy H between maps f, g: X → Y?"
  type: multiple-choice
  options:
    - "H is a bijective continuous map from X to Y that continuously deforms f into g."
    - "H is a continuous map H: X × [0,1] → Y with H(x,0) = f(x) and H(x,1) = g(x) for all x ∈ X."
    - "H is any map satisfying H(x,0) = f(x) and H(x,1) = g(x), with no continuity requirement."
    - "H is a homeomorphism between X × [0,1] and a subspace of Y."
  answer: 1
  explanation: "A homotopy is a continuous map on the product space X × [0,1], with the unit interval playing the role of a 'time' parameter. At t = 0 you get f; at t = 1 you get g; continuity of H on the whole product ensures the deformation has no jumps or tears. The bijection and homeomorphism conditions (options A and D) are far too strong — homotopies need not be bijective. Dropping continuity (option C) loses the essential content."

- question: "Homotopy equivalence is weaker than homeomorphism: every pair of homeomorphic spaces is homotopy equivalent, but not every homotopy equivalent pair is homeomorphic."
  type: true-false
  answer: true
  explanation: "A homeomorphism f: X → Y with inverse g satisfies g∘f = id_X and f∘g = id_Y as equalities, which are in particular homotopies (the constant homotopy H(x,t) = g(f(x)) = x works). So homeomorphism implies homotopy equivalence. The converse fails: D² and a point are homotopy equivalent but not homeomorphic. Homotopy equivalence allows collapsing and re-expanding in ways that homeomorphism does not."

- question: "If two continuous maps f and g from X to Y are homotopic, then for each fixed point x ∈ X, the path t ↦ H(x,t) is a loop in Y based at f(x)."
  type: true-false
  answer: false
  explanation: "The path t ↦ H(x,t) goes from H(x,0) = f(x) to H(x,1) = g(x). It is a loop only if f(x) = g(x) for that particular x. In general, homotopic maps can send each point to completely different images, and the paths traced by individual points need not be closed. Loops in Y based at a point are the input to the fundamental group, which is a different and more specific construction."

- question: "What is the difference between two maps f and g being homotopic and two spaces X and Y being homotopy equivalent?"
  type: short-answer
  answer: "Map homotopy (f ≃ g) is a relation between two maps with the same domain and codomain: there exists a continuous deformation H: X × [0,1] → Y interpolating between them. Space homotopy equivalence (X ≃ Y) is a relation between two spaces: there exist maps f: X → Y and g: Y → X such that g∘f ≃ id_X and f∘g ≃ id_Y. The round-trip conditions mean each space can be mapped into the other and back with only a homotopic-to-identity distortion. Every homeomorphism gives a homotopy equivalence, but a disk and a point are homotopy equivalent without being homeomorphic."
  explanation: "The distinction matters because the fundamental group and other homotopy invariants are invariants of homotopy equivalence classes of spaces — not of individual maps. Homotopy of maps is the tool used to *define* homotopy equivalence of spaces."
```

## Explainer

You know continuity in the topological sense: a map f: X → Y is continuous if preimages of open sets are open. Homotopy asks a different question — not whether a single map is continuous, but whether two continuous maps can be continuously *deformed* into each other. Think of two rubber-band paths on a surface: can you slide one into the other without leaving the surface? That geometric intuition is exactly what the definition captures.

The formal definition introduces a **homotopy** H: X × [0, 1] → Y, a continuous map on the product of X with the unit interval. The parameter t ∈ [0, 1] plays the role of "time": at t = 0 you have H(x, 0) = f(x), and at t = 1 you have H(x, 1) = g(x). For each fixed t, the map Hₜ(x) = H(x, t) is a continuous map from X to Y. As t varies from 0 to 1, these maps form a continuous one-parameter family interpolating from f to g. Continuity of H as a whole (on the product space) is what ensures the deformation has no jumps or tears. When such an H exists, f and g are **homotopic**, written f ≃ g.

Homotopy is an equivalence relation on the set of continuous maps from X to Y — it is reflexive (H(x,t) = f(x) works), symmetric (reverse the parameter: H(x, 1−t)), and transitive (concatenate two homotopies, spending t ∈ [0,½] on the first and t ∈ [½,1] on the second). The equivalence classes are **homotopy classes of maps**. Two spaces X and Y are **homotopy equivalent** if there exist maps f: X → Y and g: Y → X such that g∘f ≃ id_X and f∘g ≃ id_Y. This is weaker than homeomorphism — homeomorphism requires a single map to be a perfect bijection with continuous inverse, while homotopy equivalence allows a round trip that deforms but does not tear. A disk and a point are homotopy equivalent (the disk can be continuously contracted to a point), even though they are not homeomorphic.

The importance of homotopy is that it defines **invariants**: properties preserved by homotopy equivalence that can distinguish spaces. The **fundamental group** π₁(X, x₀) — the set of homotopy classes of loops based at x₀ — is the first such invariant. A simply connected space has trivial fundamental group (every loop can be contracted to a point); a circle does not (loops that wind around cannot be unlooped). Homotopy thus provides the bridge between topology (continuous structure) and algebra (groups), which is the central program of algebraic topology. Mastering the definition here is the gateway to that entire subject.
