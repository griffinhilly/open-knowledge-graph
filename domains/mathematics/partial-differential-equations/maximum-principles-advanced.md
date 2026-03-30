---
id: maximum-principles-advanced
title: Maximum Principles (Advanced)
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: maximum-principles-pdes
  type: hard
- id: elliptic-regularity-theory
  type: hard
tags: [pde, maximum-principle, abp, hopf-lemma, comparison, harnack]
stage: expert
status: validated
---
# Maximum Principles (Advanced)

## Core Idea
Advanced maximum principles extend the classical results to general elliptic operators, non-divergence form equations, and quantitative settings. The Hopf lemma establishes that at a boundary maximum, the outward normal derivative is strictly positive—a sharp boundary version of the strong maximum principle. The Alexandrov-Bakelman-Pucci (ABP) estimate gives quantitative L^∞ bounds on solutions in terms of the L^n norm of the right-hand side. Harnack's inequality relates the maximum and minimum of a positive solution, giving a powerful interior estimate. These tools are fundamental for regularity theory and nonlinear PDE analysis.

## Questions
```yaml
- question: "The Hopf lemma states that if u is a supersolution with u(x₀) = max u at a boundary point x₀, then:"
  type: multiple-choice
  options:
    - "∂u/∂ν(x₀) > 0, where ν is the outward normal"
    - "u is constant in a neighborhood of x₀"
    - "∇u(x₀) = 0"
    - "u has a saddle point at x₀"
  answer: 0
  explanation: "The Hopf lemma gives a quantitative version of the strong maximum principle at the boundary: if u achieves its maximum at a boundary point, it must be increasing in the inward normal direction there. The normal derivative is strictly positive (assuming an interior sphere condition at x₀)."
- question: "Harnack's inequality for positive harmonic functions states sup u ≤ C inf u on compact subsets."
  type: true-false
  answer: true
  explanation: "For a positive harmonic function u in a domain Ω, on any compact subdomain K ⊂ Ω, sup_K u ≤ C inf_K u where C depends only on K and Ω. This is a remarkably strong estimate: the maximum and minimum of a positive solution are comparable."
- question: "What is the ABP (Alexandrov-Bakelman-Pucci) maximum principle?"
  type: short-answer
  answer: "A quantitative L^∞ bound: sup u ≤ sup_{∂Ω} u⁺ + C·diam(Ω)·||f||_{Lⁿ(Ω)} for Lu ≥ -f with f ≥ 0"
  explanation: "The ABP estimate controls the maximum of a subsolution by its boundary values and the Lⁿ norm of the right-hand side (not L^∞, which is much stronger). The proof uses the contact set and the area formula. This estimate is the starting point for the Krylov-Safonov regularity theory."
- question: "The strong maximum principle requires the operator to satisfy an interior sphere condition at boundary points."
  type: true-false
  answer: false
  explanation: "The strong maximum principle is an interior result: if u achieves its maximum at an interior point, u is constant. The interior sphere condition is needed for the Hopf lemma (a boundary result). The strong maximum principle holds for general elliptic operators on any connected domain."
```

## Explainer
The classical maximum principle—that a harmonic function achieves its maximum on the boundary—is just the beginning of a deep and powerful theory. The advanced maximum principles provide both qualitative (strong maximum principle, Hopf lemma) and quantitative (ABP estimate, Harnack inequality) information about solutions of elliptic and parabolic equations, and they apply to operators with rough coefficients where explicit solution formulas are impossible.

The Hopf boundary lemma is the sharp boundary version of the strong maximum principle. Suppose Lu ≤ 0 in Ω and u achieves its maximum at a boundary point x₀ with u(x₀) > u(x) for all interior points. If an interior sphere condition holds at x₀ (there exists a ball B ⊂ Ω tangent to ∂Ω at x₀), then ∂u/∂ν(x₀) > 0, where ν is the outward normal. This has immediate applications: for the Neumann problem, if Lu = 0 and ∂u/∂ν = 0 on ∂Ω, the Hopf lemma forces u to be constant. The proof constructs a clever barrier function on the tangent ball.

Harnack's inequality is perhaps the most powerful single result in elliptic PDE theory. For a positive solution of Lu = 0 with bounded measurable coefficients (divergence form), Moser proved that sup_{B_r} u ≤ C inf_{B_r} u, where C depends only on the ellipticity constants, dimension, and the ball radius. This means a positive solution cannot have sharp peaks or deep valleys—it varies by at most a constant factor over any compactly contained region. The parabolic Harnack inequality, due to Moser, has a beautiful asymmetric form reflecting the time direction: sup at an earlier time is controlled by inf at a later time.

The ABP maximum principle, developed by Alexandrov, Bakelman, and Pucci, provides quantitative bounds for non-divergence form operators. For Lu = -a^{ij}u_{ij} + b^i u_i ≥ -f in Ω, it gives sup u ≤ sup_{∂Ω} u⁺ + C||f||_{L^n(Γ⁺)}, where Γ⁺ is the upper contact set (points where u touches its concave envelope from below). The L^n norm (rather than L^∞) is sharp and reflects the geometry of the contact set through the area formula. The ABP estimate is the cornerstone of the Krylov-Safonov theory, which proves Holder regularity for solutions of non-divergence form equations with merely measurable coefficients—the non-divergence counterpart of De Giorgi-Nash-Moser theory.
