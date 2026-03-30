---
id: parabolic-pde-theory
title: Parabolic PDE Theory (Heat Kernel and Regularity)
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: elliptic-regularity-theory
  type: hard
- id: maximum-principles-pdes
  type: hard
- id: heat-equation-pde
  type: soft
tags: [pde, parabolic, heat-kernel, regularity, semigroup]
stage: expert
status: validated
---
# Parabolic PDE Theory (Heat Kernel and Regularity)

## Core Idea
Parabolic PDEs like u_t - Δu = f describe diffusion and heat conduction, combining the spatial ellipticity of the Laplacian with time evolution. The heat kernel K(x,y,t) = (4πt)^(-n/2)exp(-|x-y|²/(4t)) serves as the fundamental solution and reveals the key properties: infinite speed of propagation, instantaneous smoothing, and irreversibility. Parabolic regularity theory shows that solutions gain spatial smoothness instantaneously (u_t = Δu with L² initial data is C^∞ for t > 0) and that the natural function spaces are anisotropic, counting one time derivative as equivalent to two spatial derivatives.

## Questions
```yaml
- question: "The parabolic scaling that relates time and space derivatives is:"
  type: multiple-choice
  options:
    - "One time derivative is equivalent to two spatial derivatives"
    - "One time derivative is equivalent to one spatial derivative"
    - "Two time derivatives are equivalent to two spatial derivatives"
    - "Time and space derivatives are independent"
  answer: 0
  explanation: "The heat equation u_t = Δu shows that ∂/∂t scales like ∂²/∂x². Under the parabolic scaling (x,t) → (λx, λ²t), both sides of the equation scale the same way. This is why parabolic Sobolev spaces W^{1,0;2,1} count one time derivative as worth two spatial derivatives."
- question: "A solution of the heat equation with merely L² initial data becomes C^∞ for all t > 0."
  type: true-false
  answer: true
  explanation: "This is the instantaneous smoothing property of parabolic equations. The heat kernel is C^∞ for t > 0, and the solution u(·,t) = K(·,t) * u₀ inherits all the smoothness of K. This is in stark contrast to hyperbolic equations, where initial singularities persist forever."
- question: "What is the Schauder estimate for the heat equation?"
  type: short-answer
  answer: "If u_t - Δu = f with f ∈ C^{k,α} in space and C^{k/2,α/2} in time, then u ∈ C^{k+2,α} in space and C^{(k+2)/2, α/2} in time"
  explanation: "Parabolic Schauder estimates are the analogue of elliptic Schauder estimates, with the anisotropic parabolic scaling. They provide the optimal regularity in Holder spaces and are essential for nonlinear parabolic equations."
- question: "The heat equation is time-reversible: given the solution at time T, we can uniquely recover the initial data."
  type: true-false
  answer: false
  explanation: "The backward heat equation u_t = -Δu is ill-posed: the smoothing effect of forward evolution destroys information about high-frequency components of the initial data. This irreversibility is connected to the second law of thermodynamics and the arrow of time."
```

## Explainer
Parabolic PDE theory occupies a central position in analysis, combining the elliptic regularity of spatial operators with the evolution structure of time-dependent problems. The prototype is the heat equation u_t = Δu, whose solutions are given by convolution with the heat kernel: u(x,t) = ∫K(x-y,t)u₀(y)dy. This formula reveals the fundamental properties: the Gaussian kernel smooths the initial data instantly (u is C^∞ for any t > 0), propagates effects at infinite speed (K > 0 everywhere for t > 0), and is irreversible (the backward problem is ill-posed because the kernel grows exponentially for t < 0).

The regularity theory for parabolic equations mirrors elliptic theory but with an important twist: the parabolic scaling. Since ∂_t and Δ appear symmetrically in the heat equation, one time derivative counts as two spatial derivatives. The natural Sobolev space is W^{2,1}_p(Q) = {u : u, ∇u, D²u, u_t ∈ L^p(Q)}, and the basic regularity theorem states: if u_t - Δu = f with f ∈ L^p(Q), then u ∈ W^{2,1}_p(Q) with ||u||_{W^{2,1}_p} ≤ C||f||_{L^p}. In Holder spaces, the parabolic Schauder estimates give u ∈ C^{2+α, 1+α/2} when f ∈ C^{α, α/2}.

The maximum principle for parabolic equations takes its strongest form in this theory. The weak maximum principle states that the maximum of u over a space-time cylinder Q_T = Ω × (0,T] occurs on the parabolic boundary (bottom and sides, not the top). The strong maximum principle (due to Nirenberg) says that if u attains its maximum in the interior of Q_T, then u is constant on the entire parabolic past of that point. These principles yield uniqueness and comparison results and are the starting point for the De Giorgi-Nash-Moser theory for parabolic equations with rough coefficients.

For nonlinear parabolic equations like the porous medium equation u_t = Δ(u^m) and the mean curvature flow, the theory becomes considerably more delicate. Degenerate and singular parabolic equations—where the diffusion coefficient vanishes or blows up—exhibit finite propagation speed, waiting times, and free boundaries that are absent in the linear theory. The general theory of quasilinear parabolic systems, developed by Ladyzhenskaya, Solonnikov, Ural'tseva, and others, provides existence and regularity results under structural conditions on the nonlinearity and remains one of the technical pillars of modern PDE theory.
