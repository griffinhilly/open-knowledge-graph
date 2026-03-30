---
id: elliptic-regularity-theory
title: Elliptic Regularity Theory
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: weak-solutions-rigorous
  type: hard
- id: sobolev-spaces-pdes
  type: hard
- id: laplacian-harmonic-functions
  type: soft
tags: [pde, elliptic, regularity, sobolev, smoothness]
stage: expert
status: validated
---
# Elliptic Regularity Theory

## Core Idea
Elliptic regularity theory establishes that weak solutions of elliptic PDEs are smoother than initially apparent—the equation itself forces regularity. For -Δu = f, if f ∈ H^k(Ω), then u ∈ H^{k+2}(Ω): the solution gains two orders of Sobolev regularity beyond the right-hand side. If f is smooth and the domain has a smooth boundary, u is smooth. This "regularity bootstrap" is a hallmark of elliptic equations and does not hold for hyperbolic equations. The theory extends to general elliptic operators with variable coefficients via Schauder estimates and L^p theory.

## Questions
```yaml
- question: "If u ∈ H¹₀(Ω) is a weak solution of -Δu = f with f ∈ L²(Ω), what regularity does u have?"
  type: multiple-choice
  options:
    - "u ∈ H²(Ω)"
    - "u ∈ H¹(Ω) only"
    - "u ∈ C^∞(Ω)"
    - "u ∈ L^∞(Ω)"
  answer: 0
  explanation: "The basic elliptic regularity theorem states that if f ∈ L²(Ω) and ∂Ω is smooth (or Ω = ℝⁿ), then u ∈ H². This is a gain of two Sobolev derivatives beyond f, matching the order of the Laplacian. If f ∈ H^k, then u ∈ H^{k+2} by induction."
- question: "Elliptic regularity is a local property: u is smooth wherever f is smooth, regardless of boundary regularity."
  type: true-false
  answer: true
  explanation: "Interior regularity holds independently of boundary conditions or boundary smoothness. If f ∈ C^∞(ω) for an open set ω ⊂⊂ Ω, then u ∈ C^∞(ω). Boundary regularity requires additional assumptions on the smoothness of ∂Ω and the boundary data."
- question: "What is the Weyl lemma?"
  type: short-answer
  answer: "Every distribution satisfying Δu = 0 is a smooth (C^∞) function, and in fact real-analytic"
  explanation: "The Weyl lemma is the simplest case of elliptic regularity: if u is merely a distribution solving Laplace's equation, it must be an infinitely differentiable (and even real-analytic) function. This shows that the elliptic operator Δ cannot have genuinely distributional solutions."
- question: "For a domain with a corner (non-smooth boundary), the H² regularity theorem for -Δu = f may fail."
  type: true-false
  answer: true
  explanation: "Corners and edges in the boundary cause singularities in the solution that limit its Sobolev regularity. Near a reentrant corner of angle > π, the solution may be only in H^s for s < 1 + π/angle, even if f is smooth. Understanding these corner singularities is crucial for numerical methods on non-smooth domains."
```

## Explainer
Elliptic regularity is one of the deepest and most useful results in PDE theory. It says that elliptic equations are "smoothing operators"—solutions are more regular than the data. This is in sharp contrast to hyperbolic equations, where solutions are exactly as smooth as the data (and no smoother), and to parabolic equations, which smooth in the forward time direction only. For elliptic equations, the regularity gain is automatic and comes solely from the structure of the equation.

The proof of interior regularity for the Laplacian proceeds by difference quotients: one shows that finite-difference approximations to second derivatives of u are uniformly bounded in L², which implies u has genuine second derivatives in L². The argument is: if u ∈ H¹ and Δu = f ∈ L², take difference quotients, test the weak formulation against the difference quotient of u, and use the equation to bound the second-order differences. This bootstraps: if f ∈ H^k, repeating the argument k times gives u ∈ H^{k+2}. By the Sobolev embedding theorem, if k + 2 > n/2, then u is continuous; if k is large enough, u is C^m for any desired m.

Schauder estimates provide the analogous regularity theory in Holder spaces. If f ∈ C^{k,α}(Ω) (k times differentiable with α-Holder continuous kth derivatives) and the coefficients are in C^{k,α}, then u ∈ C^{k+2,α}(Ω). These estimates are sharper than the Sobolev theory in that they measure regularity in a pointwise (rather than average) sense and are essential for the study of nonlinear elliptic equations, where the regularity of coefficients depends on the solution itself.

The regularity theory for general elliptic operators -∂_i(a^{ij}∂_j u) + b^i∂_i u + cu = f extends the Laplacian theory under the ellipticity condition a^{ij}ξ_iξ_j ≥ λ|ξ|². When the coefficients are smooth, the same gain of two derivatives holds. When the coefficients are merely bounded and measurable, the theory is more delicate: De Giorgi-Nash-Moser theory shows that weak solutions are Holder continuous (but not necessarily C^{1,α} or better), which was a groundbreaking result in the 1950s. This theory is the foundation for the regularity theory of nonlinear PDEs and earned Nash the Abel Prize and De Giorgi lasting fame. Boundary regularity depends critically on the smoothness of ∂Ω—Lipschitz domains, convex domains, and smooth domains each yield different regularity results.
