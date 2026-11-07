---
id: ricci-curvature-and-scalar-curvature
title: Ricci Curvature and Scalar Curvature
domain: mathematics
course: differential-geometry
prerequisites:
  - id: curvature-tensor
    type: hard
  - id: riemannian-metrics
    type: hard
tags:
  - ricci-curvature
  - scalar-curvature
  - einstein-equations
  - volume-comparison
stage: expert
status: validated
---

# Ricci Curvature and Scalar Curvature

## Core Idea
The Ricci curvature Ric(v,v) averages the sectional curvatures of all 2-planes containing v, measuring how volumes of geodesic balls grow compared to Euclidean space. The scalar curvature R further averages the Ricci curvature over all directions, giving a single number at each point. These contractions of the Riemann tensor are central to Einstein's field equations (Ric - ½Rg = 8πT), comparison geometry, and global theorems constraining manifold topology from curvature bounds.

## How It's Best Learned
Compute both contractions for the round n-sphere of radius r: every sectional curvature is 1/r², so Ric = ((n − 1)/r²) g and R = n(n − 1)/r². Then check the small-ball formula on the unit S². There R = 2, and the geodesic disk area 2π(1 − cos ε) expands to πε²(1 − ε²/12 + …), matching 1 − Rε²/(6(n + 2)).

## Common Misconceptions
- Ric(v, v) is the sectional curvature in the direction v. (For a unit vector v, it is the sum of the sectional curvatures of n − 1 orthogonal planes containing v.)
- Positive scalar curvature implies positive Ricci curvature. (On S² × S¹ the scalar curvature is positive, but Ric is zero in the circle direction.)
- A Ricci-flat manifold is flat. (In dimension 3 that holds. In dimension 4 and up, there are Ricci-flat metrics with nonzero curvature tensor, such as Ricci-flat metrics on the K3 surface.)

## Questions

```yaml
- question: "The Ricci tensor is obtained from the Riemann tensor by contracting one pair of indices: Ric(X,Y) = trace(Z ↦ R(Z,X)Y). What geometric information does positive Ricci curvature encode?"
  type: multiple-choice
  options:
    - "Geodesics curve toward each other, and geodesic balls have smaller volume than Euclidean balls of the same radius"
    - "The manifold has positive Gaussian curvature at every point"
    - "Parallel transport around any loop is the identity"
    - "The manifold is diffeomorphic to a sphere"
  answer: 0
  explanation: "Positive Ricci curvature in a direction v means that a thin cone of geodesics emanating from p in directions near v converges — the volume of a small geodesic ball grows slower than in Euclidean space. The Bishop-Gromov volume comparison theorem makes this precise. Positive Ricci curvature does not imply positive Gaussian curvature (that is a stronger condition in dimensions > 2). It also does not force the manifold to be a sphere, although the Bonnet-Myers theorem does force compactness and finite fundamental group."

- question: "The scalar curvature R = gⁱʲRicᵢⱼ is the simplest curvature invariant. On a 2-dimensional surface, R equals twice the Gaussian curvature K."
  type: true-false
  answer: true
  explanation: "In two dimensions, the Riemann tensor has only one independent component (up to symmetries), and all curvature notions reduce to the Gaussian curvature K. Specifically, Rᵢⱼₖₗ = K(gᵢₖgⱼₗ - gᵢₗgⱼₖ), the Ricci tensor is Ricᵢⱼ = Kgᵢⱼ, and the scalar curvature is R = 2K. In higher dimensions, scalar curvature carries much less information than the full Riemann tensor — it is the weakest curvature condition."

- question: "In Einstein's field equations Ric - ½Rg + Λg = 8πT, the left side involves only the Ricci tensor and scalar curvature, not the full Riemann tensor. Why is the full Riemann tensor not needed?"
  type: short-answer
  answer: "The Einstein equations govern the relationship between matter (T) and curvature. The Ricci tensor captures how matter sources curve spacetime (specifically, how geodesic balls change volume), while the remaining part of the Riemann tensor — the Weyl tensor — describes gravitational radiation (curvature in vacuum). The Weyl tensor propagates freely via the Bianchi identities and does not need to be specified by the field equations. The Einstein equations determine the Ricci part; the Weyl part is determined by boundary/initial conditions and propagation."
  explanation: "The decomposition Riemann = Ricci part + Weyl part separates curvature into the 'matter-determined' piece and the 'freely propagating' piece. In 3 dimensions, the Weyl tensor vanishes identically, so the Ricci tensor determines the full Riemann tensor and there is no gravitational radiation. In 4+ dimensions, the Weyl tensor is nonzero and carries independent information about the geometry."
```

## Explainer

The Riemann curvature tensor has n²(n²-1)/12 independent components — far too many to grasp directly in high dimensions. The **Ricci tensor** and **scalar curvature** are successive contractions that extract the most important geometric information. The Ricci tensor Ric is a symmetric (0,2)-tensor obtained by tracing the Riemann tensor: Ricᵢⱼ = Rᵏᵢₖⱼ. It has n(n+1)/2 independent components — the same count as the metric tensor. The scalar curvature R = gⁱʲRicᵢⱼ contracts further to a single function on M.

The **geometric meaning** of Ricci curvature is volume distortion. Consider a small geodesic ball of radius ε centered at p. Its volume compares to the Euclidean ball as Vol(Bε(p)) = ωₙεⁿ(1 - R(p)ε²/(6(n+2)) + ...), where ωₙ is the Euclidean ball volume. Positive scalar curvature means balls are smaller than Euclidean. More refined: Ric(v,v) controls the volume of thin tubes in the direction v. Positive Ricci curvature in all directions means geodesic balls shrink in every direction, and the **Bishop-Gromov comparison theorem** gives sharp volume comparison bounds.

The Ricci and scalar curvatures have powerful topological consequences. The **Bonnet-Myers theorem** says: if Ric ≥ (n-1)κg for some κ > 0, then the manifold is compact with diameter ≤ π/√κ and finite fundamental group. This means strong positive Ricci curvature forces topological constraints. Conversely, negative Ricci curvature allows for richer topology. The **scalar curvature** constrains topology more subtly — for instance, the torus Tⁿ admits no metric of positive scalar curvature (Schoen-Yau, Gromov-Lawson).

In physics, the **Einstein field equations** Gᵢⱼ = Ricᵢⱼ - ½Rgᵢⱼ = 8πTᵢⱼ relate the Einstein tensor G (built from Ricci and scalar curvature) to the stress-energy tensor T of matter. The remaining piece of the Riemann tensor — the **Weyl tensor** — is the trace-free part and represents the free gravitational field (gravitational waves). The decomposition Riem = Ricci part + Weyl part is the curvature analogue of decomposing a matrix into trace and traceless parts. In Riemannian geometry, finding manifolds with prescribed Ricci curvature is the **Ricci flow** program initiated by Hamilton and completed by Perelman for the Poincare conjecture.
