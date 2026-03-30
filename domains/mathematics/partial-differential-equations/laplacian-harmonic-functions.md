---
id: laplacian-harmonic-functions
title: The Laplacian and Harmonic Functions
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: laplaces-equation
  type: hard
- id: greens-theorem
  type: hard
tags: [pde, laplacian, harmonic, potential-theory, mean-value-property]
stage: advanced
status: validated
---
# The Laplacian and Harmonic Functions

## Core Idea
Harmonic functions—solutions of Laplace's equation Δu = 0—are among the most studied and best-behaved functions in mathematics. They satisfy the mean value property (the value at any point equals the average over any surrounding sphere), are real-analytic (infinitely differentiable and equal to their Taylor series), obey the maximum principle, and are uniquely determined by their boundary values. These properties make harmonic functions the foundation of potential theory and a model for the regularity theory of elliptic PDEs.

## Questions
```yaml
- question: "The mean value property states that for a harmonic function u, u(x₀) equals:"
  type: multiple-choice
  options:
    - "The average of u over any sphere centered at x₀"
    - "The maximum of u on any sphere centered at x₀"
    - "The average of u over the entire domain"
    - "The value of u at the nearest boundary point"
  answer: 0
  explanation: "The mean value property says u(x₀) = (1/|∂B_r|)∫_{∂B_r(x₀)} u dS for any ball B_r(x₀) contained in the domain. This also holds for the volume average: u(x₀) = (1/|B_r|)∫_{B_r(x₀)} u dV. This property characterizes harmonic functions."
- question: "A harmonic function on a bounded domain that is zero on the boundary must be identically zero."
  type: true-false
  answer: true
  explanation: "By the maximum principle, a harmonic function achieves its maximum and minimum on the boundary. If u = 0 on the boundary, then max u ≤ 0 and min u ≥ 0 in the domain, so u ≡ 0. This is the uniqueness result for the Dirichlet problem."
- question: "What is the key regularity property of harmonic functions?"
  type: short-answer
  answer: "They are real-analytic (C^ω): infinitely differentiable and locally equal to their convergent power series"
  explanation: "Despite Laplace's equation being a second-order equation, its solutions are not merely C² or even C^∞ — they are real-analytic. This follows from the mean value property and can be proved using the Poisson integral formula. This extreme regularity is a hallmark of elliptic equations."
- question: "If u is harmonic in ℝⁿ and bounded, then u must be constant."
  type: true-false
  answer: true
  explanation: "This is Liouville's theorem for harmonic functions. It follows from the mean value property: taking the average over larger and larger spheres, the oscillation of u must tend to zero since u is bounded. The analogous result for holomorphic functions in complex analysis is a special case."
```

## Explainer
Harmonic functions are the prototypical solutions of elliptic PDEs, and their rich theory serves as both a model and a source of techniques for the general theory. A function u is harmonic in a domain Ω if Δu = Σ ∂²u/∂x_i² = 0 throughout Ω. The Laplacian Δ is the simplest second-order elliptic operator, and its solutions exhibit all the key features of elliptic regularity: smoothness in the interior, control by boundary data, and the maximum principle.

The mean value property is the most characteristic feature of harmonic functions: u(x₀) equals the average of u over any sphere (or ball) centered at x₀ that lies within the domain. This property has an elegant physical interpretation—a harmonic function represents a state of perfect equilibrium where no point is hotter or cooler than its surroundings. The converse is also true: any continuous function satisfying the mean value property is harmonic (and hence smooth). This provides a powerful alternative characterization that avoids derivatives entirely.

From the mean value property flow all the remarkable regularity results. Harmonic functions are not just infinitely differentiable but real-analytic—they equal their Taylor series in a neighborhood of every point. This is proven via the Poisson integral formula, which represents a harmonic function inside a ball as an integral of its boundary values against the Poisson kernel. The formula also yields derivative estimates: |D^α u(x₀)| ≤ C_{α,n}/r^{n+|α|} · ||u||_{L¹(B_r)}, showing that all derivatives are controlled by the L¹ norm of u on a surrounding ball. These estimates are the prototype for Schauder estimates in general elliptic theory.

Harmonic functions have deep connections to complex analysis (holomorphic functions have harmonic real and imaginary parts), probability (they arise as expected values of Brownian motion stopped at the boundary), and potential theory (they describe gravitational and electrostatic potentials in source-free regions). The study of harmonic functions on Riemannian manifolds connects PDE theory to geometry, with results like the Liouville theorem (bounded harmonic functions on ℝⁿ are constant) having far-reaching geometric consequences. The theory of harmonic functions is the bedrock on which the modern theory of elliptic PDEs is built.
