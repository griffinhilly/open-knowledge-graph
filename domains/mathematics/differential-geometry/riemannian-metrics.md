---
id: riemannian-metrics
title: Riemannian Metrics
domain: mathematics
course: differential-geometry
prerequisites:
  - id: smooth-manifolds
    type: hard
  - id: tangent-vectors-and-tangent-spaces
    type: hard
  - id: inner-product-spaces
    type: hard
  - id: partition-of-unity
    type: soft
tags:
  - riemannian-metric
  - inner-product
  - length
  - riemannian-manifold
stage: expert
status: validated
---

# Riemannian Metrics

## Core Idea
A Riemannian metric on a smooth manifold assigns a smoothly varying inner product to each tangent space, enabling measurement of lengths, angles, areas, and volumes on curved spaces. In local coordinates, the metric is given by a symmetric positive-definite matrix gij(x) that encodes the geometry. Every smooth manifold admits a Riemannian metric (by partition of unity), but different metrics on the same manifold produce dramatically different geometries — the choice of metric is the central datum of Riemannian geometry.

## Questions

```yaml
- question: "The standard metric on ℝ² in polar coordinates (r, θ) is ds² = dr² + r²dθ². The coefficient r² in front of dθ² means that..."
  type: multiple-choice
  options:
    - "The θ-coordinate curves have length r²"
    - "A small displacement dθ at radius r corresponds to an actual distance of r·dθ, so distances in the θ-direction scale with r"
    - "The metric is not flat because the coefficients are not constant"
    - "The Gaussian curvature is 1/r²"
  answer: 1
  explanation: "The metric component gθθ = r² means that the length element in the θ-direction is |ds| = r|dθ|. A circle at radius r has circumference ∫₀²π r dθ = 2πr, as expected. The non-constant coefficient does NOT mean the metric is curved — flat ℝ² has curvature zero regardless of the coordinate system used. The appearance of r² is a coordinate artifact. This illustrates a key principle: the metric components gij depend on the coordinate system, but geometric quantities (curvature, geodesics, distances) do not."

- question: "A Riemannian metric g defines a natural isomorphism between the tangent and cotangent spaces. This isomorphism, called the 'musical isomorphism,' maps a vector field X to the 1-form..."
  type: multiple-choice
  options:
    - "X♭ = g(X, ·), defined by X♭(Y) = g(X, Y) for all Y"
    - "X♭ = dX, the exterior derivative of X"
    - "X♭ = X/|X|, the unit vector in the direction of X"
    - "X♭ = ∇X, the covariant derivative of X"
  answer: 0
  explanation: "The 'flat' operator ♭ sends a vector X to the 1-form X♭ defined by X♭(Y) = g(X,Y). In coordinates, if X = Xⁱ∂/∂xⁱ, then X♭ = gijXⁱ dxʲ — the metric 'lowers the index.' The inverse operation ♯ ('sharp') raises indices: ω♯ is the vector field satisfying g(ω♯, Y) = ω(Y). For example, the gradient ∇f = (df)♯ is obtained by applying sharp to the differential df. Without a metric, there is no natural way to convert vectors to covectors."

- question: "Why does the choice of Riemannian metric matter so much, given that every smooth manifold admits one?"
  type: short-answer
  answer: "While existence is guaranteed, different metrics produce completely different geometric structures: different notions of distance, different geodesics, different curvature, different volume. A sphere with the round metric has positive curvature and finite diameter; with a flat metric (impossible globally, but illustrative locally) it would have zero curvature. The metric determines all of Riemannian geometry — connections, curvature, geodesics, the Laplacian — so choosing the 'right' metric for a given problem is the central question. In general relativity, the metric encodes the gravitational field."
  explanation: "The partition-of-unity construction proves existence but gives a 'generic' metric with no particular geometric significance. Interesting Riemannian geometry comes from metrics with special properties: constant curvature (spheres, hyperbolic space), Einstein metrics (Ricci curvature proportional to metric), Kahler metrics (compatible with complex structure). Finding metrics with prescribed curvature properties is one of the deepest problems in differential geometry."

- question: "On a Riemannian manifold (M, g), the length of a smooth curve γ : [a,b] → M is defined as L(γ) = ∫_a^b √g(γ'(t), γ'(t)) dt."
  type: true-false
  answer: true
  explanation: "The metric g provides an inner product on each tangent space, so g(γ'(t), γ'(t)) is the squared norm of the velocity vector. Its square root is the speed, and integrating speed over time gives arc length. This is the manifold generalization of the familiar formula L = ∫√(dx² + dy²) for curves in the plane. The distance between two points is the infimum of lengths of all curves connecting them, making (M, d) a metric space (in the topology sense) when M is connected."
```

## Explainer

A **Riemannian metric** g on a smooth manifold M is a smooth assignment of an inner product gp to each tangent space TpM. In local coordinates, the metric is specified by a symmetric, positive-definite matrix of smooth functions gij(x), and the inner product of two tangent vectors v = vⁱ∂/∂xⁱ and w = wʲ∂/∂xʲ is g(v,w) = gij vⁱwʲ. The **line element** ds² = gij dxⁱ dxʲ encodes the metric in a compact notation that makes transformation properties transparent. Under a coordinate change, gij transforms as a (0,2)-tensor: g'kl = gij (∂xⁱ/∂x'ᵏ)(∂xʲ/∂x'ˡ).

With a metric in hand, you can measure everything geometric. The **length** of a curve is the integral of the speed |γ'(t)| = √g(γ',γ'). The **distance** between points is the infimum of curve lengths. The **angle** between tangent vectors is cos θ = g(v,w)/(|v||w|). The **volume** of a region is the integral of the Riemannian volume form dVg = √det(gij) dx¹ ∧ ... ∧ dxⁿ. The metric also provides the **musical isomorphisms** ♭ and ♯ that convert between vectors and covectors — this is how the gradient ∇f (a vector) is obtained from the differential df (a covector).

Every smooth manifold admits a Riemannian metric — this follows from the partition-of-unity argument (averaging local Euclidean metrics with non-negative weights preserves positive definiteness). But the specific choice of metric determines the geometry. The flat metric on ℝⁿ, the round metric on Sⁿ, the hyperbolic metric on the Poincare disk, and the Schwarzschild metric of a black hole are all Riemannian metrics on their respective manifolds, each encoding fundamentally different geometry. The study of which manifolds admit metrics with special curvature properties (constant curvature, Einstein, Ricci-flat) is one of the central programs in modern differential geometry.

The Riemannian metric is the starting point for the rest of Riemannian geometry. From the metric, you derive the **Levi-Civita connection** (the unique torsion-free connection compatible with the metric), which defines parallel transport and covariant differentiation. From the connection, you derive **curvature** (measuring the failure of parallel transport to be path-independent). From curvature, you derive geometric and topological consequences via theorems like Gauss-Bonnet, Bonnet-Myers, and the comparison theorems. The metric is the seed from which the entire apparatus grows.
