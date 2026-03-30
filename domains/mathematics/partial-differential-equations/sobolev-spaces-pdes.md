---
id: sobolev-spaces-pdes
title: Sobolev Spaces for PDEs
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: sobolev-spaces-introduction
  type: hard
- id: distribution-theory-pdes
  type: hard
- id: lp-spaces
  type: hard
tags: [pde, sobolev-space, weak-derivative, embedding, trace]
stage: expert
status: validated
---
# Sobolev Spaces for PDEs

## Core Idea
Sobolev spaces W^{k,p}(Ω) consist of functions whose weak derivatives up to order k belong to L^p(Ω). They are the natural function spaces for PDE theory because they measure both the size and the smoothness of functions in a way compatible with integral formulations. The Sobolev embedding theorems determine when membership in W^{k,p} implies classical smoothness or continuity, while trace theorems characterize which boundary values are achievable by Sobolev functions. These spaces provide the analytical infrastructure for the variational and weak formulation of PDEs.

## Questions
```yaml
- question: "The Sobolev space H¹(Ω) = W^{1,2}(Ω) consists of L² functions whose:"
  type: multiple-choice
  options:
    - "First-order weak derivatives are also in L²"
    - "Classical derivatives exist and are in L²"
    - "Fourier transform is in L²"
    - "First-order weak derivatives are bounded"
  answer: 0
  explanation: "H¹(Ω) = {u ∈ L²(Ω) : ∂u/∂x_i ∈ L²(Ω) for all i}, where ∂u/∂x_i is the weak (distributional) derivative. The function need not be classically differentiable. The norm is ||u||² = ∫|u|² + ∫|∇u|²."
- question: "In dimension n = 3, the Sobolev embedding W^{1,2}(Ω) ⊂ L^p(Ω) holds for all p ≤ 6."
  type: true-false
  answer: true
  explanation: "The Sobolev embedding theorem states that W^{1,p}(Ω) ⊂ L^{p*}(Ω) where p* = np/(n-p) when p < n. For n = 3 and p = 2, p* = 6. So H¹ functions in 3D are automatically in L^p for all p ≤ 6, but not necessarily for p > 6."
- question: "What does the trace theorem for Sobolev spaces establish?"
  type: short-answer
  answer: "Functions in W^{1,p}(Ω) have well-defined boundary values (traces) in L^p(∂Ω), even though they are defined only almost everywhere in Ω"
  explanation: "Since L^p functions are only defined up to sets of measure zero, and ∂Ω has zero n-dimensional measure, boundary values are not directly meaningful. The trace theorem shows that the restriction map u → u|_∂Ω extends continuously from smooth functions to all of W^{1,p}, with the trace lying in the fractional Sobolev space W^{1-1/p, p}(∂Ω)."
- question: "H¹₀(Ω) is the closure of C_c^∞(Ω) in the H¹ norm. Functions in H¹₀(Ω) have what boundary behavior?"
  type: multiple-choice
  options:
    - "Zero trace (vanish on ∂Ω in the trace sense)"
    - "Bounded on ∂Ω"
    - "Smooth on ∂Ω"
    - "No condition on the boundary"
  answer: 0
  explanation: "H¹₀(Ω) = {u ∈ H¹(Ω) : trace(u) = 0 on ∂Ω}. This is the natural space for Dirichlet boundary conditions in the weak formulation—functions that 'vanish on the boundary' in the generalized sense."
```

## Explainer
Sobolev spaces are the indispensable functional-analytic framework for modern PDE theory. The fundamental insight is that classical differentiability is too restrictive for PDEs: we need function spaces that allow for the kind of limited regularity that solutions naturally possess. A function u ∈ W^{k,p}(Ω) has weak derivatives up to order k in L^p—it need not be classically differentiable, but its derivatives in the distributional sense are integrable functions. The most important case is H^k(Ω) = W^{k,2}(Ω), which is a Hilbert space and the natural setting for variational formulations.

The Sobolev embedding theorems are the bridge between weak differentiability and classical properties. When kp > n (the dimension), the Morrey embedding states that W^{k,p}(Ω) ⊂ C^{0,α}(Ω) for appropriate α—Sobolev functions with enough derivatives in a strong enough L^p are actually continuous (or Holder continuous). When kp < n, the Sobolev embedding gives W^{k,p} ⊂ L^{p*} for the Sobolev conjugate p* = np/(n-kp), gaining integrability but not continuity. The critical case kp = n has logarithmic corrections. These embeddings determine the minimal regularity assumptions needed in PDE theory.

Trace theory addresses a subtle but crucial point: how do we impose boundary conditions on Sobolev functions? A function in L²(Ω) is defined only almost everywhere, and ∂Ω has zero n-dimensional measure, so the restriction to the boundary is not directly defined. The trace theorem shows that for u ∈ H¹(Ω), the restriction u|_∂Ω is well-defined as an element of H^{1/2}(∂Ω)—a fractional Sobolev space on the boundary—and the trace operator T: H¹(Ω) → H^{1/2}(∂Ω) is bounded and surjective. The space H¹₀(Ω) = ker(T) consists of functions with zero trace, the natural function space for homogeneous Dirichlet conditions.

The Poincare inequality and its variants are essential tools in the Sobolev space framework. On a bounded domain, ||u||_{L²} ≤ C||∇u||_{L²} for u ∈ H¹₀(Ω), meaning the full H¹ norm is equivalent to the seminorm ||∇u||_{L²} on H¹₀. This inequality is crucial for proving coercivity of bilinear forms in the variational formulation of elliptic PDEs. The Rellich-Kondrachov theorem, stating that the embedding H¹(Ω) → L²(Ω) is compact on bounded domains, provides the compactness needed for existence proofs via weak convergence arguments. Together, these tools make Sobolev spaces the engine of the modern existence and regularity theory for PDEs.
