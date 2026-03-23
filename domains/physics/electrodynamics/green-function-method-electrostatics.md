---
id: green-function-method-electrostatics
title: Green Function Method for Electrostatics
domain: physics
course: electrodynamics
prerequisites:
- id: boundary-value-problems-electrostatics
  type: hard
- id: laplace-poisson-equations-electrostatics
  type: hard
- id: spherical-harmonics-electrostatics
  type: soft
builds-toward:
  - method-of-images
tags:
- greens-functions
- boundary-value-problems
- poisson-equation
stage: expert
status: draft
---
# Green Function Method for Electrostatics

## Core Idea
Green's functions are fundamental solutions to the Poisson equation that encode boundary conditions. The Green function method reduces electrostatic boundary value problems to integral equations over sources and boundaries.

## How It's Best Learned
Derive Green's function for simple geometries (infinite plane, sphere) and verify reciprocity. Apply to conductors and dielectrics to see how boundary conditions determine the Green function.

## Questions

```yaml
- question: "What is the key practical advantage of the Green function method over expanding in eigenfunctions (Fourier series, spherical harmonics) for electrostatic boundary value problems?"
  type: multiple-choice
  options:
    - "It works only for symmetric charge distributions, making it faster for common cases"
    - "Once G is found for a geometry, any charge distribution's potential follows by a single integration — the hard work of satisfying boundary conditions is done once and encoded in G"
    - "It replaces the Poisson equation with an algebraic equation, eliminating differential equations"
    - "It always yields closed-form analytic solutions, unlike eigenfunction expansions which require infinite sums"
  answer: 1
  explanation: "The Green function encodes, once, how a given geometry responds to a unit point source at every location — including all boundary condition effects. After that, computing the potential for any charge distribution ρ(r') is just integration: φ(r) = ∫ G(r,r') ρ(r')/ε₀ d³r'. With eigenfunction methods, each new charge distribution requires re-solving the matching conditions at boundaries. The Green function moves the boundary-condition labor from 'per problem' to 'per geometry,' making it especially powerful for geometries that host many different charge configurations."

- question: "The free-space Green function G₀(r,r') = 1/(4π|r−r'|) satisfies ∇²G₀ = −δ³(r−r'). When a grounded conducting sphere is present, why must G be modified?"
  type: multiple-choice
  options:
    - "The Poisson equation changes form inside conductors, requiring a different differential equation"
    - "The boundary condition requires G = 0 on the conducting surface, which G₀ does not satisfy"
    - "The delta function source must be repositioned to lie on the conducting surface"
    - "Conductors attenuate fields, so G₀ must include an exponential decay factor"
  answer: 1
  explanation: "For a Dirichlet problem (grounded conductor), the Green function must vanish on the boundary: G(r,r') = 0 whenever r is on the conductor surface. G₀ = 1/(4π|r−r'|) is nonzero everywhere except at r = r', so it fails to satisfy this condition. The Green function must be constructed specifically for the geometry — which is exactly where the method of images enters: adding an image charge outside the domain adjusts the potential so that G = 0 on the conductor surface."

- question: "The Green function satisfies reciprocity: G(r,r') = G(r',r), meaning the potential at r due to a unit source at r' equals the potential at r' due to a unit source at r."
  type: true-false
  answer: true
  explanation: "Reciprocity follows from the self-adjoint nature of the Laplacian operator. Applying Green's second identity to G(r,r') and G(r,r'') and using their defining equations yields G(r',r'') = G(r'',r'). Physically, this is the statement that mutual capacitance coefficients are symmetric: how much conductor A's potential rises per unit charge on B equals how much B's potential rises per unit charge on A. Reciprocity provides an important consistency check when computing Green functions numerically or analytically."

- question: "The free-space Green function G₀(r,r') = 1/(4π|r−r'|) is the correct Green function to use for electrostatics problems involving grounded conducting boundaries."
  type: true-false
  answer: false
  explanation: "G₀ is the Green function for free space only — it satisfies the delta function equation but ignores boundary conditions. A problem with a grounded conductor requires a Green function that satisfies both ∇²G = −δ³(r−r') and G = 0 on the conducting surface. This must be constructed separately for each geometry. The method of images is one technique for building the corrected G; the key physical content is that the induced surface charge on the conductor is implicitly encoded in the boundary-satisfying G."

- question: "Explain why the Green function method is analogous to an impulse response in signal processing, and what this analogy reveals about solving the Poisson equation."
  type: short-answer
  answer: "In linear signal processing, a system is fully characterized by its impulse response — the output when the input is a delta function. Any other input is a superposition of scaled and shifted delta functions, so the output is the convolution of the input with the impulse response. The Poisson equation ∇²φ = −ρ/ε₀ is a linear PDE: the 'input' is the charge distribution ρ and the 'output' is the potential φ. The Green function G(r,r') is the response to a unit point source (delta function input) at r', satisfying ∇²G = −δ³(r−r'). Because the equation is linear, the potential for any ρ is the integral (convolution) of G with ρ. The boundary conditions are encoded in G, so this integration gives the correct potential automatically."
  explanation: "This analogy is exact, not just metaphorical. The Poisson operator is self-adjoint and linear, so the theory of linear operators guarantees that G exists and that the convolution integral gives the full solution. The same framework appears in heat conduction, quantum mechanics (propagators), and acoustics."
```

## Explainer

You have worked through boundary value problems by expanding in known eigenfunctions — spherical harmonics, Fourier series — and matching coefficients at boundaries. The Green function method offers a more general and powerful perspective: instead of choosing a basis, you find the potential due to a single point source at every possible source location, encoding all boundary effects, and then superpose. The key question becomes: what potential does the geometry produce in response to a unit charge placed at position r'? That response function is the **Green function** G(r, r').

The connection to what you already know is direct. The Poisson equation ∇²φ = −ρ/ε₀ is a linear differential equation, and linear equations obey superposition. If you know how to solve ∇²G(r,r') = −δ³(r − r') with the appropriate boundary conditions (G = 0 on conducting surfaces for Dirichlet problems), then the solution for any charge distribution ρ follows by integration: φ(r) = ∫ G(r,r') ρ(r')/ε₀ d³r'. The Green function is essentially the impulse response of the Poisson operator — the same idea that appears in signal processing and differential equations for linear systems. You already know that the free-space Poisson equation has the solution φ = kq/r for a point charge; the free-space Green function is just G₀(r,r') = 1/(4π|r − r'|), which encodes that Coulomb law.

The complication — and the power — comes from boundary conditions. In free space, G₀ is simple. But if you introduce a grounded conducting sphere, the Green function must satisfy G = 0 on the sphere's surface. The **method of images** can be seen as a technique for constructing the modified Green function: you place an image charge outside the domain so that the total potential (real charge + image) vanishes on the boundary surface. The Green function with boundary conditions thus contains all the physics of how the conductor responds to a source charge — the induced surface charge distribution is implicitly encoded in G.

**Reciprocity** is one of the most elegant properties: G(r,r') = G(r',r). The potential at r due to a unit source at r' equals the potential at r' due to a unit source at r. This symmetry reflects the self-adjoint nature of the Laplacian operator and has deep physical meaning: the mutual capacitance coefficient between two conductors is symmetric. In practice, reciprocity provides a consistency check on any computed Green function. Once you have G for a given geometry, computing the potential for any charge distribution is reduced to a single integral — the hard work of satisfying boundary conditions is done once and encoded in G, after which new source distributions require only integration, not a new boundary value calculation.
