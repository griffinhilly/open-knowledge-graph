---
id: exponential-map
title: Exponential Map
domain: mathematics
course: differential-geometry
prerequisites:
  - id: geodesics
    type: hard
  - id: tangent-vectors-and-tangent-spaces
    type: hard
tags:
  - exponential-map
  - normal-coordinates
  - geodesics
  - local-diffeomorphism
stage: expert
status: validated
---

# Exponential Map

## Core Idea
The exponential map exp_p : TpM → M sends a tangent vector v to the point reached by following the geodesic from p with initial velocity v for unit time. It is a local diffeomorphism near the origin of TpM, providing "normal coordinates" centered at p in which geodesics through p are straight lines and the metric is Euclidean to first order. The exponential map connects the linear algebra of the tangent space to the nonlinear geometry of the manifold and is the fundamental tool for local geometric analysis.

## Questions

```yaml
- question: "The exponential map exp_p : TpM → M is defined by exp_p(v) = γ_v(1), where γ_v is the geodesic with γ_v(0) = p and γ_v'(0) = v. What does exp_p(tv) equal for t ∈ [0,1]?"
  type: multiple-choice
  options:
    - "The point at parameter t on the geodesic from p with initial velocity v"
    - "The point t · exp_p(v) (scalar multiplication in M)"
    - "The parallel transport of v along the geodesic for time t"
    - "The Riemannian exponential e^{tv} of the matrix v"
  answer: 0
  explanation: "By the scaling property of geodesics, the geodesic with initial velocity tv is a reparametrization of the geodesic with initial velocity v: γ_{tv}(1) = γ_v(t). So exp_p(tv) = γ_v(t), which is the point reached by following the geodesic from p with velocity v for time t. The curve t ↦ exp_p(tv) traces out the geodesic ray from p in the direction v. Option D refers to the matrix exponential, which motivates the name — on a Lie group, the two notions coincide."

- question: "The exponential map exp_p is a diffeomorphism from all of TpM onto M."
  type: true-false
  answer: false
  explanation: "The exponential map is only guaranteed to be a local diffeomorphism near the origin 0 ∈ TpM (by the inverse function theorem, since d(exp_p)_0 = id). Globally, it can fail to be injective (geodesics from p may intersect at other points, like antipodal points on a sphere) or fail to be defined for all v (if geodesics are not complete). The injectivity radius at p is the largest radius for which exp_p is a diffeomorphism on the open ball of that radius in TpM."

- question: "What is the geometric significance of the injectivity radius of a Riemannian manifold?"
  type: short-answer
  answer: "The injectivity radius inj(p) at a point p is the supremum of radii r such that exp_p is a diffeomorphism on the ball B_r(0) ⊂ TpM. Within this radius, every point has a unique minimizing geodesic from p, and normal coordinates are valid. The injectivity radius of M is inj(M) = inf_p inj(p). A positive injectivity radius guarantees that the manifold has uniformly 'Euclidean-like' neighborhoods. The injectivity radius is bounded below by curvature: Klingenberg's theorem gives inj(M) ≥ π/√K_max for even-dimensional manifolds with sectional curvature ≤ K_max."
  explanation: "The injectivity radius controls how 'locally Euclidean' the manifold is from the perspective of geodesics. Small injectivity radius means geodesics refocus quickly (due to positive curvature or topological complexity), making the manifold geometrically 'small.' Many theorems in Riemannian geometry require lower bounds on the injectivity radius to ensure analytic estimates work."

- question: "In normal coordinates at p, the Riemannian metric satisfies gij(p) = δij and ∂kgij(p) = 0."
  type: true-false
  answer: true
  explanation: "Normal coordinates are defined via the exponential map: the coordinate of exp_p(vⁱeᵢ) is (v¹,...,vⁿ). At the origin (the point p), the metric is the identity (because d(exp_p)_0 = id maps the standard inner product on TpM to itself), and the first derivatives of the metric vanish (equivalently, all Christoffel symbols vanish at p). The first nonzero correction to gij = δij is at second order and is controlled by the curvature: gij(x) = δij - ⅓Rikjl xᵏxˡ + O(|x|³)."
```

## Explainer

The tangent space TpM is a vector space — linear, flat, and easy to work with. The manifold M is curved and nonlinear. The **exponential map** is the bridge between them: it takes a tangent vector v ∈ TpM and maps it to the point in M you reach by "walking along the geodesic" in the direction v for unit time. For small v, this is a diffeomorphism, and the inverse map provides **normal coordinates** — a coordinate system centered at p where geodesics through p are straight lines.

Precisely, for v ∈ TpM with |v| small, let γ_v(t) be the unique geodesic with γ_v(0) = p and γ_v'(0) = v. Then exp_p(v) = γ_v(1). By rescaling: exp_p(tv) = γ_v(t) — the exponential map sends rays through the origin in TpM to geodesic rays from p in M. The map d(exp_p)_0 : T_0(TpM) → TpM is the identity, so by the inverse function theorem, exp_p is a diffeomorphism from a neighborhood of 0 in TpM to a neighborhood of p in M. This neighborhood, described in the linear coordinates of TpM, gives normal coordinates.

In normal coordinates, the metric is optimally simple. At the center point p: gij(0) = δij (the metric looks Euclidean) and Γᵏij(0) = 0 (the Christoffel symbols vanish). The Taylor expansion gij(x) = δij - ⅓Rikjl(p) xᵏxˡ + O(|x|³) shows that the curvature tensor is the leading correction to flatness. This is why curvature controls local geometry: within normal coordinates, the manifold looks like Euclidean space up to first order, with curvature appearing at second order.

The **injectivity radius** inj(p) is the largest r such that exp_p is injective on the ball {v ∈ TpM : |v| < r}. Beyond this radius, geodesics from p may cross each other or form conjugate points. On the sphere Sⁿ of radius 1, the injectivity radius is π — geodesics from any point refocus at the antipodal point. On hyperbolic space, the injectivity radius is infinite. The exponential map also connects to Lie theory: on a Lie group G with Lie algebra 𝔤 = TeG, the Riemannian exponential map (for a bi-invariant metric) coincides with the Lie group exponential map, which is why both share the name. This is the historical origin of the term "exponential map" in Riemannian geometry.
