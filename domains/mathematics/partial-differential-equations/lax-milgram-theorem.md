---
id: lax-milgram-theorem
title: Lax-Milgram Theorem
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: weak-solutions-rigorous
  type: hard
- id: hilbert-spaces
  type: hard
tags: [pde, lax-milgram, bilinear-form, coercivity, existence]
stage: expert
status: validated
---
# Lax-Milgram Theorem

## Core Idea
The Lax-Milgram theorem guarantees the existence and uniqueness of solutions to abstract variational problems: if a bilinear form a(u,v) on a Hilbert space H is continuous and coercive (a(u,u) ≥ α||u||² for some α > 0), then for every continuous linear functional F on H, there exists a unique u ∈ H with a(u,v) = F(v) for all v ∈ H. This abstract result, when applied to the weak formulations of elliptic PDEs, immediately yields existence and uniqueness of weak solutions. It does not require symmetry of the bilinear form, making it more general than the Riesz representation theorem or variational minimization.

## Questions
```yaml
- question: "What are the two hypotheses on the bilinear form a(u,v) in the Lax-Milgram theorem?"
  type: multiple-choice
  options:
    - "Continuity (|a(u,v)| ≤ M||u||||v||) and coercivity (a(u,u) ≥ α||u||²)"
    - "Symmetry (a(u,v) = a(v,u)) and positivity (a(u,u) > 0)"
    - "Linearity and boundedness"
    - "Compactness and injectivity"
  answer: 0
  explanation: "Continuity ensures the bilinear form defines a bounded operator, and coercivity ensures this operator is invertible with a bounded inverse. Together they guarantee unique solvability. Symmetry is NOT required—this is the key advantage over the Riesz representation theorem."
- question: "The Lax-Milgram theorem requires the bilinear form to be symmetric."
  type: true-false
  answer: false
  explanation: "Lax-Milgram works for non-symmetric bilinear forms, which arise in convection-diffusion equations and other PDEs with first-order terms. When the form IS symmetric, the solution also minimizes the associated energy functional, giving additional structure."
- question: "How does coercivity of a(u,v) = ∫∇u·∇v dx on H¹₀(Ω) follow?"
  type: short-answer
  answer: "From the Poincaré inequality: a(u,u) = ∫|∇u|²dx ≥ C||u||²_{H¹₀} because ||u||_{L²} ≤ C_P||∇u||_{L²} on bounded domains"
  explanation: "The Poincaré inequality on bounded domains states that the L² norm of u is controlled by the L² norm of ∇u for functions vanishing on the boundary. Therefore ||∇u||²_{L²} controls the full H¹ norm ||u||²_{H¹₀} = ||∇u||²_{L²}, establishing coercivity."
- question: "The Lax-Milgram theorem also provides a stability estimate for the solution."
  type: true-false
  answer: true
  explanation: "The proof yields ||u|| ≤ (1/α)||F||, where α is the coercivity constant. This says the solution is bounded in terms of the data, and small changes in F produce proportionally small changes in u—continuous dependence on data."
```

## Explainer
The Lax-Milgram theorem is the workhorse existence result for elliptic PDEs. It reduces the question of solvability for a PDE to verifying two functional-analytic properties of a bilinear form: continuity and coercivity. Once these are established—which is typically a matter of applying standard inequalities like Poincare, Cauchy-Schwarz, and trace inequalities—existence, uniqueness, and continuous dependence all follow immediately from the abstract theorem.

The theorem generalizes the Riesz representation theorem, which handles only the case where a(u,v) = (u,v)_H is the inner product itself. When a is symmetric and coercive, the problem a(u,v) = F(v) is equivalent to minimizing J(v) = ½a(v,v) - F(v), and existence follows from the direct method of the calculus of variations. But many important PDEs—convection-diffusion equations -Δu + b·∇u = f, for example—have non-symmetric weak formulations, and the Lax-Milgram theorem handles these directly.

The proof is elegant and short. Define A: H → H by (Au, v) = a(u,v) for all v (possible by Riesz). Continuity of a means A is bounded: ||Au|| ≤ M||u||. Coercivity means A is bounded below: α||u||² ≤ a(u,u) = (Au, u) ≤ ||Au|| ||u||, so ||Au|| ≥ α||u||. This shows A is injective with closed range. A brief argument (or application of the closed range theorem) shows the range is all of H, so A is an isomorphism and u = A⁻¹(RF) where R is the Riesz map.

In applications, verifying the hypotheses of Lax-Milgram for specific PDEs is a systematic exercise. For the diffusion equation -div(a(x)∇u) = f with a(x) ≥ a₀ > 0 (uniformly elliptic), the bilinear form a(u,v) = ∫a(x)∇u·∇v dx is coercive on H¹₀ by ellipticity and the Poincare inequality, and continuous by the bound a ≤ a₁. For the convection-diffusion equation with additional terms ∫b·∇u·v dx + ∫cu·v dx, one verifies that the lower-order terms do not destroy coercivity (which holds when c - ½div b ≥ 0, or when the lower-order terms are dominated by the diffusion). The Lax-Milgram theorem is also the theoretical foundation for the finite element method, where the Galerkin approximation inherits the same existence and stability properties from the continuous problem.
