---
id: variational-methods-pdes
title: Variational Methods for PDEs
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: lax-milgram-theorem
  type: hard
- id: sobolev-spaces-pdes
  type: hard
- id: energy-methods-pdes
  type: soft
tags: [pde, variational, calculus-of-variations, minimization, direct-method]
stage: expert
status: validated
---
# Variational Methods for PDEs

## Core Idea
Many PDEs arise as the Euler-Lagrange equations of variational problems: they characterize critical points of energy functionals. The Dirichlet problem -Δu = f is equivalent to minimizing J(v) = ½∫|∇v|²dx - ∫fv dx over H¹₀(Ω). The direct method of the calculus of variations proves existence by showing that minimizing sequences converge (using weak compactness in Sobolev spaces and lower semicontinuity of the functional). Beyond simple minimization, variational methods include mountain pass theorems and minimax principles for finding saddle-point solutions of nonlinear PDEs.

## Questions
```yaml
- question: "The direct method of the calculus of variations proves existence by:"
  type: multiple-choice
  options:
    - "Showing a minimizing sequence converges weakly to a minimizer"
    - "Constructing an explicit solution formula"
    - "Applying the maximum principle"
    - "Using the method of characteristics"
  answer: 0
  explanation: "The direct method takes a minimizing sequence {u_n} with J(u_n) → inf J, extracts a weakly convergent subsequence (using reflexivity and boundedness), and shows the limit is a minimizer (using weak lower semicontinuity of J). No explicit formula is needed."
- question: "Weak lower semicontinuity of the functional J(u) = ∫|∇u|²dx means that if u_n ⇀ u weakly in H¹, then J(u) ≤ lim inf J(u_n)."
  type: true-false
  answer: true
  explanation: "This is the key property that ensures the limit of a minimizing sequence is actually a minimizer. The norm in a Hilbert space is weakly lower semicontinuous, and J(u) = ||∇u||² inherits this property. Without weak lower semicontinuity, the infimum might not be attained."
- question: "What is the Euler-Lagrange equation associated with minimizing J(v) = ½∫|∇v|²dx - ∫fv dx?"
  type: short-answer
  answer: "-Δu = f (Poisson's equation)"
  explanation: "Setting the first variation δJ = 0 gives ∫∇u·∇φ dx = ∫fφ dx for all test functions φ, which is the weak form of -Δu = f. This shows that the Poisson equation is the gradient-flow equation for the Dirichlet energy."
- question: "The mountain pass theorem is used to find:"
  type: multiple-choice
  options:
    - "Saddle point (minimax) critical points of nonlinear functionals"
    - "Global minimizers of convex functionals"
    - "Maximum principles for elliptic equations"
    - "Eigenvalues of self-adjoint operators"
  answer: 0
  explanation: "When a functional has a local minimum and the energy is unbounded below along some direction, the mountain pass theorem guarantees a saddle point at the 'mountain pass' level. This is crucial for nonlinear elliptic equations where the functional is not convex and simple minimization is insufficient."
```

## Explainer
Variational methods exploit the deep connection between PDEs and optimization. Many fundamental PDEs—including the equations of elasticity, electrostatics, minimal surfaces, and general relativity—are Euler-Lagrange equations of action or energy functionals. Solving the PDE is equivalent to finding critical points of the functional, and the rich machinery of optimization theory (convexity, compactness, topological methods) becomes available.

The direct method, developed by Tonelli and refined by subsequent generations, is the primary tool for proving existence of minimizers. The recipe is: (1) show the functional J is bounded below on the admissible set, (2) take a minimizing sequence {u_n} with J(u_n) → inf J, (3) extract a weakly convergent subsequence u_{n_k} ⇀ u (using the reflexivity of H¹ and the coercivity-induced boundedness), (4) show J(u) ≤ lim inf J(u_{n_k}) by weak lower semicontinuity. The minimizer u then satisfies the Euler-Lagrange equation, which is the PDE of interest.

For convex functionals, the direct method gives a unique global minimizer. The Dirichlet energy J(v) = ½∫|∇v|²dx - ∫fv dx is strictly convex, so the minimizer (= weak solution of -Δu = f) is unique. For nonlinear problems, the functional may be non-convex, possessing multiple critical points. The mountain pass theorem (Ambrosetti-Rabinowitz, 1973) handles a common non-convex geometry: if J has a local minimum at 0, and J(e) < J(0) for some distant point e, but J is large on a "mountain range" separating 0 from e, then there exists a critical point at the "mountain pass" level c = inf_{γ} max_{t∈[0,1]} J(γ(t)), where γ ranges over paths from 0 to e.

Beyond the mountain pass theorem, the landscape of variational methods includes the Ljusternik-Schnirelman theory (finding multiple critical points using topological index), the linking theorem, saddle point theorems, and concentration-compactness (handling loss of compactness for problems on unbounded domains). These methods have been spectacularly successful for nonlinear Schrodinger equations, semilinear elliptic problems, and geometric PDEs. The variational perspective also connects PDE theory to differential geometry (harmonic maps, minimal surfaces, Yamabe problem) and to physics (least action principle, Ginzburg-Landau theory), making it one of the most productive viewpoints in modern mathematics.
