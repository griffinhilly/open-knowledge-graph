---
id: fourier-transform-methods-pdes
title: Fourier Transform Methods for PDEs
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: fourier-series-definition
  type: hard
- id: separation-variables-pde
  type: hard
- id: heat-equation-pde
  type: soft
tags: [pde, fourier-transform, spectral-methods, frequency-domain]
stage: advanced
status: validated
---
# Fourier Transform Methods for PDEs

## Core Idea
The Fourier transform converts a PDE with constant coefficients into an algebraic equation (or ODE) by transforming spatial derivatives into multiplication by frequency variables. Applying the transform û(ξ,t) = ∫u(x,t)e^(-iξ·x)dx to a PDE like u_t = ku_xx yields û_t = -kξ²û, a simple ODE in t for each frequency ξ. Solving in frequency space and inverting the transform produces the solution. This method is particularly effective for problems on the whole real line or in ℝⁿ where Fourier series are not applicable.

## Questions
```yaml
- question: "What does the Fourier transform do to the operation ∂²u/∂x²?"
  type: multiple-choice
  options:
    - "Replaces it with -ξ²û(ξ)"
    - "Replaces it with iξû(ξ)"
    - "Replaces it with ξ²û(ξ)"
    - "Replaces it with -iξ²û(ξ)"
  answer: 0
  explanation: "Each spatial derivative ∂/∂x becomes multiplication by iξ under the Fourier transform. Two derivatives give (iξ)² = -ξ². This is the key property that converts differential equations into algebraic ones."
- question: "The Fourier transform method works directly for PDEs with variable coefficients."
  type: true-false
  answer: false
  explanation: "The Fourier transform converts constant-coefficient differential operators into polynomial multiplication. Variable coefficients become convolution operators in frequency space, which are generally no simpler than the original PDE. Other methods (such as pseudodifferential operators) are needed for variable-coefficient problems."
- question: "Using the Fourier transform, what is the solution to the heat equation u_t = ku_xx on ℝ with initial data u(x,0) = f(x)?"
  type: short-answer
  answer: "Convolution of f with the heat kernel: u(x,t) = (4πkt)^(-1/2) ∫ f(y)e^(-(x-y)²/(4kt)) dy"
  explanation: "In frequency space, û(ξ,t) = f̂(ξ)e^(-kξ²t). Inverting gives a convolution of f with the inverse transform of e^(-kξ²t), which is the Gaussian heat kernel (4πkt)^(-1/2)e^(-x²/(4kt))."
- question: "For the wave equation u_tt = c²u_xx on ℝ, the Fourier transform in x yields what ODE in t?"
  type: multiple-choice
  options:
    - "û_tt = -c²ξ²û"
    - "û_tt = c²ξ²û"
    - "û_t = -c²ξ²û"
    - "û_t = icξû"
  answer: 0
  explanation: "Transforming u_xx gives -ξ²û, so the wave equation becomes û_tt = -c²ξ²û. This is a simple harmonic oscillator in t for each frequency ξ, with solution û(ξ,t) = A(ξ)cos(cξt) + B(ξ)sin(cξt)."
```

## Explainer
The Fourier transform is one of the most powerful techniques for solving PDEs with constant coefficients on unbounded domains. The fundamental idea is that the Fourier transform diagonalizes constant-coefficient differential operators: it converts ∂/∂x into multiplication by iξ. This transforms a PDE—an equation relating partial derivatives—into an algebraic equation or a simpler ODE in the transform variable. Once solved in the frequency domain, the inverse Fourier transform recovers the solution in physical space.

Consider the heat equation u_t = ku_xx on the real line. Taking the Fourier transform in x gives û_t(ξ,t) = -kξ²û(ξ,t), an ODE whose solution is û(ξ,t) = f̂(ξ)e^(-kξ²t). The factor e^(-kξ²t) is a Gaussian in ξ that decays faster for high frequencies, reflecting the smoothing effect of diffusion. Inverting the transform and using the convolution theorem gives u = f * K_t, where K_t is the heat kernel. This derivation reveals why diffusion smooths out rough initial data: high-frequency components are exponentially damped.

For the wave equation u_tt = c²Δu, the Fourier transform gives û_tt = -c²|ξ|²û, a harmonic oscillator in t. Each Fourier mode oscillates at frequency c|ξ| without growing or decaying—energy is conserved at each frequency. The inverse transform recovers D'Alembert's formula in one dimension and Kirchhoff's formula in three dimensions. The dispersion relation ω = c|ξ| being linear (nondispersive) explains why waves in this equation maintain their shape.

The method extends naturally to higher dimensions and to other equations. For Schrödinger's equation iu_t = -Δu, the transform gives û_t = i|ξ|²û with solution û = f̂·e^(i|ξ|²t). The quadratic dispersion relation ω = |ξ|² means different frequencies travel at different speeds, causing wave packets to spread (dispersion). For Helmholtz's equation Δu + k²u = f, the transform yields (-|ξ|² + k²)û = f̂, which is algebraic but has singularities on the sphere |ξ| = k, corresponding to resonant frequencies and requiring careful treatment.

The Fourier transform approach connects directly to spectral theory and distribution theory. The solution operator e^(-kξ²t) for the heat equation is an example of a Fourier multiplier, and the general theory of pseudodifferential operators extends these ideas to variable-coefficient and nonlinear settings. Computationally, the Fast Fourier Transform (FFT) makes these methods practical for numerical PDE solving, underlying spectral methods that achieve exponential convergence for smooth problems.
