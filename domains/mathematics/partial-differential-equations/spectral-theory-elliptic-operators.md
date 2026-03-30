---
id: spectral-theory-elliptic-operators
title: Spectral Theory for Elliptic Operators
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: eigenfunction-expansions-sturm-liouville
  type: hard
- id: elliptic-regularity-theory
  type: hard
- id: spectral-theorem-compact-self-adjoint
  type: soft
tags: [pde, spectral-theory, eigenvalue, elliptic, self-adjoint]
stage: expert
status: validated
---
# Spectral Theory for Elliptic Operators

## Core Idea
The spectral theory of elliptic operators generalizes Sturm-Liouville theory to multiple dimensions: the eigenvalue problem -Δu = λu (or more generally, Lu = λu for a self-adjoint elliptic operator L) on a bounded domain with Dirichlet conditions has a discrete spectrum 0 < λ₁ < λ₂ ≤ λ₃ ≤ ... → ∞ with corresponding eigenfunctions forming an orthonormal basis of L²(Ω). The eigenvalues encode geometric information about the domain (Weyl's law: λ_k ~ C_n(k/|Ω|)^{2/n}), and the eigenfunction expansion provides a complete solution theory for evolution equations on bounded domains.

## Questions
```yaml
- question: "The first eigenvalue λ₁ of -Δ on a bounded domain Ω with Dirichlet conditions satisfies:"
  type: multiple-choice
  options:
    - "λ₁ > 0, and the corresponding eigenfunction does not change sign"
    - "λ₁ = 0 with constant eigenfunction"
    - "λ₁ < 0 for some domains"
    - "λ₁ depends on the choice of coordinates"
  answer: 0
  explanation: "For Dirichlet conditions on a bounded domain, λ₁ > 0 (since ∫|∇u|²dx > 0 for any nonzero u ∈ H¹₀). The first eigenfunction φ₁ does not change sign (it is either strictly positive or strictly negative in Ω), a consequence of the Krein-Rutman theorem or the maximum principle."
- question: "Weyl's asymptotic law states that the eigenvalue counting function N(λ) = #{λ_k ≤ λ} satisfies N(λ) ~ C_n|Ω|λ^{n/2} as λ → ∞."
  type: true-false
  answer: true
  explanation: "Weyl's law (1911) connects the eigenvalue distribution to the volume of the domain: N(λ) ~ ω_n|Ω|/(2π)^n · λ^{n/2}, where ω_n is the volume of the unit ball in ℝⁿ. This means you can 'hear the volume' of a domain from its eigenvalues, answering part of Kac's famous question 'Can one hear the shape of a drum?'"
- question: "How is the first eigenvalue λ₁ of -Δ characterized variationally?"
  type: short-answer
  answer: "λ₁ = min{∫|∇u|²dx / ∫u²dx : u ∈ H¹₀(Ω), u ≠ 0} (the Rayleigh quotient minimum)"
  explanation: "This variational characterization (the Rayleigh-Ritz principle) gives λ₁ as the minimum of the Rayleigh quotient over H¹₀. Higher eigenvalues are characterized similarly via the min-max principle: λ_k = min over k-dimensional subspaces of the max of the Rayleigh quotient."
- question: "The eigenfunctions of -Δ on a bounded domain with smooth boundary are smooth."
  type: true-false
  answer: true
  explanation: "Eigenfunctions satisfy -Δφ = λφ, an elliptic equation with smooth right-hand side (λφ). By elliptic regularity, if the boundary is smooth, φ is smooth up to the boundary. On domains with corners, eigenfunctions may have limited regularity near the corners."
```

## Explainer
The spectral theory of elliptic operators on bounded domains is a cornerstone of PDE theory, providing a complete decomposition of function spaces and solution operators in terms of eigenvalues and eigenfunctions. The starting point is the eigenvalue problem -Δu = λu in Ω, u = 0 on ∂Ω. The inverse of the Laplacian with Dirichlet conditions is a compact, self-adjoint, positive operator on L²(Ω), so the spectral theorem for compact self-adjoint operators guarantees a sequence of positive eigenvalues λ₁ ≤ λ₂ ≤ ... → ∞ with corresponding eigenfunctions {φ_k} forming an orthonormal basis.

The eigenfunction expansion f = Σ⟨f, φ_k⟩φ_k converges in L² for any f ∈ L²(Ω), and in H^s for smoother f. This expansion solves evolution equations explicitly: the heat equation u_t = Δu with initial data f has solution u(x,t) = Σ⟨f, φ_k⟩e^{-λ_k t}φ_k(x), showing exponential decay at rate λ₁ (the spectral gap). The wave equation u_tt = -Δu has solution u(x,t) = Σ[a_k cos(√λ_k t) + b_k sin(√λ_k t)]φ_k(x), showing oscillation at frequencies √λ_k. The spectrum encodes the long-time behavior and resonance structure.

The variational characterization of eigenvalues via the min-max (Courant-Fischer) principle is both theoretically fundamental and computationally practical. The first eigenvalue λ₁ = min_{u≠0} ∫|∇u|²/∫u² measures the "stiffness" of the domain (how hard it is for a function to vary while vanishing on the boundary). Comparing eigenvalues of different domains via domain monotonicity (larger domains have smaller first eigenvalues) and Faber-Krahn inequality (among domains of fixed volume, the ball minimizes λ₁) connects spectral theory to geometric optimization.

Weyl's asymptotic law λ_k ~ C(k/|Ω|)^{2/n} as k → ∞ is a landmark result connecting analysis and geometry. It says the high eigenvalues grow like k^{2/n}, with the coefficient determined by the volume of the domain. Refined asymptotics involving the boundary length (2D) or surface area (3D) and curvature have been extensively studied. The famous question "Can one hear the shape of a drum?" asks whether the eigenvalue spectrum determines the domain uniquely—the answer is no in general (isospectral non-isometric domains exist), but the spectrum does determine the volume, surface area, and other geometric invariants. Spectral theory for elliptic operators remains an active and beautiful area connecting PDEs, geometry, physics, and number theory.
