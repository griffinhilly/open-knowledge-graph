---
id: weak-solutions-rigorous
title: Weak Solutions (Rigorous Theory)
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: sobolev-spaces-pdes
  type: hard
- id: conservation-laws-weak-solutions-intro
  type: hard
tags: [pde, weak-solution, variational, bilinear-form, existence]
stage: expert
status: validated
---
# Weak Solutions (Rigorous Theory)

## Core Idea
A weak solution of a PDE is a function in an appropriate Sobolev space that satisfies the equation when tested against all smooth test functions via integration by parts. For the equation -Δu = f with Dirichlet boundary conditions, the weak formulation is: find u ∈ H¹₀(Ω) such that ∫∇u·∇v dx = ∫fv dx for all v ∈ H¹₀(Ω). This transfers derivatives from the solution to the test function, allowing solutions with less regularity than the classical formulation requires. The Lax-Milgram theorem and variational methods then guarantee existence and uniqueness under natural conditions.

## Questions
```yaml
- question: "To derive the weak formulation of -Δu = f, we multiply by a test function v and apply:"
  type: multiple-choice
  options:
    - "Integration by parts (Green's first identity)"
    - "The Fourier transform"
    - "The method of characteristics"
    - "Taylor expansion"
  answer: 0
  explanation: "Multiplying -Δu = f by v ∈ H¹₀ and integrating by parts gives ∫∇u·∇v dx = ∫fv dx. The boundary term vanishes because v = 0 on ∂Ω. This moves one derivative from u to v, requiring only u ∈ H¹ rather than u ∈ H² (which the classical formulation Δu would need)."
- question: "A weak solution of an elliptic PDE is always a classical (C²) solution."
  type: true-false
  answer: false
  explanation: "A weak solution is an element of a Sobolev space and need not be twice differentiable. However, elliptic regularity theory shows that if the data (domain, coefficients, right-hand side) are sufficiently smooth, then the weak solution is in fact classical. This is a nontrivial theorem, not automatic."
- question: "What advantage does the weak formulation have over the classical formulation?"
  type: short-answer
  answer: "It requires fewer derivatives on the solution, allowing existence proofs in Sobolev spaces using functional analysis (Lax-Milgram, compactness, variational methods)"
  explanation: "The classical formulation of -Δu = f requires u to be twice differentiable, which is hard to establish directly. The weak formulation only needs u ∈ H¹, and existence in H¹ can be proved by abstract functional analysis. Regularity theory then bootstraps: if f and the domain are smooth, the weak solution is also smooth."
- question: "In the weak formulation, the bilinear form a(u,v) = ∫∇u·∇v dx is coercive on H¹₀(Ω), meaning:"
  type: multiple-choice
  options:
    - "a(u,u) ≥ α||u||²_{H¹₀} for some α > 0"
    - "a(u,v) = a(v,u) for all u,v"
    - "a(u,v) ≤ M||u|| ||v|| for some M"
    - "|a(u,v)| = 0 implies u = 0"
  answer: 0
  explanation: "Coercivity (also called ellipticity) means the bilinear form controls the norm: a(u,u) = ∫|∇u|²dx ≥ α||u||²_{H¹₀} by the Poincaré inequality. Coercivity is the key hypothesis of the Lax-Milgram theorem that guarantees existence and uniqueness of the weak solution."
```

## Explainer
The weak formulation of PDEs is the central concept of modern PDE theory, bridging the gap between the differential equation (which requires smooth solutions) and the functional-analytic machinery (which provides existence in Sobolev spaces). The idea is conceptually simple: multiply the PDE by a test function, integrate over the domain, and use integration by parts to transfer derivatives from the unknown solution to the known test function. The result is an integral equation that makes sense for functions with fewer derivatives than the original PDE demands.

For the model problem -Δu = f in Ω with u = 0 on ∂Ω, the weak formulation seeks u ∈ H¹₀(Ω) satisfying a(u,v) = F(v) for all v ∈ H¹₀(Ω), where a(u,v) = ∫∇u·∇v dx is a bilinear form and F(v) = ∫fv dx is a linear functional. This is an equation in the Hilbert space H¹₀(Ω), and the Lax-Milgram theorem guarantees a unique solution provided a is continuous and coercive (which follows from the Poincaré inequality). The proof is constructive: u is the unique element of H¹₀ such that a(u,·) = F(·), essentially a generalization of the Riesz representation theorem.

The weak formulation also reveals the variational structure of elliptic PDEs. The weak solution u minimizes the energy functional J(v) = ½a(v,v) - F(v) over H¹₀(Ω). This is the Dirichlet principle, rigorously justified by the direct method of the calculus of variations: the energy is bounded below and coercive, so a minimizing sequence converges weakly in H¹₀ to the minimizer. This variational perspective is the basis for finite element methods, where one minimizes the energy over a finite-dimensional subspace of H¹₀.

The passage from weak to classical solutions is the content of elliptic regularity theory. The interior regularity theorem states that if f ∈ L²(Ω), the weak solution u ∈ H¹₀ is actually in H²_{loc}(Ω) and satisfies -Δu = f almost everywhere. With smoother data (f ∈ H^k, smooth boundary), the solution gains correspondingly more regularity: u ∈ H^{k+2}. When enough Sobolev regularity is gained to trigger the Sobolev embedding into continuous functions, the weak solution becomes a classical solution. This two-step approach—first prove existence in a weak sense, then bootstrap regularity—is the standard paradigm for modern elliptic PDE theory.
