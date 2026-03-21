---
id: laplace-poisson-equations-electrostatics
title: Laplace's and Poisson's Equations
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-equations-differential-form
  type: hard
- id: divergence-theorem
  type: hard
builds-toward:
- boundary-value-problems-electrostatics
- separation-variables-elliptic-equations
tags:
- laplace-equation
- poisson-equation
- potential
stage: advanced
status: draft
---

# Laplace's and Poisson's Equations

## Core Idea
Laplace's equation ∇²φ = 0 governs the electrostatic potential in charge-free regions, while Poisson's equation ∇²φ = -ρ/ε₀ includes charge sources. Solutions to these equations determine all electrostatic fields and represent one of the most important PDEs in physics and mathematics. Their rich mathematical theory (harmonic functions, Green's functions, conformal mappings) provides powerful techniques for solving electrostatics problems.

## Questions

```yaml
- question: "A physicist needs the electric potential inside a charge-free cavity in a conductor. She guesses φ = A + B·r² and verifies it satisfies ∇²φ = 0 inside the cavity and φ = 0 on the conductor surface. Can she conclude she has found the correct potential?"
  type: multiple-choice
  options:
    - "No — guessing solutions is not rigorous; she must derive φ using systematic separation of variables"
    - "No — the uniqueness theorem applies only to Dirichlet conditions on flat boundaries, not curved surfaces"
    - "Yes — if a function satisfies ∇²φ = 0 inside and the boundary conditions on all surfaces, the uniqueness theorem guarantees it is the only solution"
    - "Yes, but only provisionally — she must also verify Green's function compatibility"
  answer: 2
  explanation: "The uniqueness theorem for Laplace's equation is what makes this approach rigorous. Given Dirichlet boundary conditions (φ specified on all bounding surfaces), there is exactly one function satisfying ∇²φ = 0 inside and matching those conditions. The method of finding that function is irrelevant — guessing, separation of variables, conformal mapping, physical intuition. Once you have verified the PDE and boundary conditions are satisfied, you have the unique solution. This is what makes techniques like the method of images mathematically legitimate rather than merely a useful fiction."

- question: "What is the fundamental advantage of reformulating an electrostatics problem using Poisson's equation (∇²φ = −ρ/ε₀) rather than applying Coulomb's law directly to every charge element?"
  type: multiple-choice
  options:
    - "The potential φ is a scalar, and uniqueness theorems guarantee that any solution satisfying the PDE and boundary conditions is the correct and only solution"
    - "Poisson's equation eliminates boundary conditions, so the solution region need not be specified"
    - "Poisson's equation applies only inside conductors where Coulomb's law breaks down"
    - "Coulomb's law gives the field directly while Poisson's equation only gives the potential, requiring an extra differentiation step that reduces accuracy"
  answer: 0
  explanation: "The Poisson/Laplace reformulation has two key advantages over Coulomb superposition: (1) the potential φ is a scalar, avoiding the vector addition of field contributions from every charge element — a dramatic simplification for complex geometries where the vector integral is intractable; (2) uniqueness theorems guarantee that any function satisfying the PDE and boundary conditions is the solution, licensing any method of solution. Option D correctly notes the differentiation step (E = −∇φ) but mischaracterizes it as a disadvantage — this trivial step is far simpler than performing vector integrals over distributed charge."

- question: "A harmonic function (solution to Laplace's equation) can attain a local maximum value at an interior point of a charge-free region, provided the boundary values are arranged to create a sufficiently steep potential hill."
  type: true-false
  answer: false
  explanation: "The mean value theorem for harmonic functions prohibits interior extrema. The theorem states that the value of a harmonic function at any interior point equals the average of its values over any sphere centered on that point. If φ had a local maximum at an interior point P, then φ(P) would exceed the values on a small enclosing sphere, violating the mean-value property (an average cannot exceed all of its terms). Therefore all maxima and minima of φ must lie on the boundary — a key physical result: electric potential has no peaks or valleys in empty space."

- question: "Poisson's equation reduces to Laplace's equation in any region where the free charge density is zero."
  type: true-false
  answer: true
  explanation: "Poisson's equation is ∇²φ = −ρ/ε₀. When ρ = 0 (no free charges in the region), the source term vanishes and the equation becomes ∇²φ = 0, which is Laplace's equation. This is why Laplace's equation governs the potential between conductors, outside charge distributions, and inside charge-free cavities — those regions have ρ = 0. Poisson's equation with ρ ≠ 0 applies where charges are present (inside a charged sphere, in a plasma, within a dielectric with polarization charge)."

- question: "What does the uniqueness theorem for Laplace's equation imply about how you are allowed to solve a boundary value problem in electrostatics?"
  type: short-answer
  answer: "The uniqueness theorem states that specifying the potential φ on all boundaries of a charge-free region (Dirichlet conditions) uniquely determines the solution inside. This means you may find the solution by any method — guessing, separation of variables, the method of images, conformal mapping, physical symmetry — and if your candidate satisfies ∇²φ = 0 inside and matches the boundary values, it is provably the only solution that exists. The method of discovery is mathematically irrelevant; only verification against the PDE and boundary conditions matters."
  explanation: "The method of images exploits this directly: to find the potential above a grounded conducting plane with a point charge above it, you place an image charge of opposite sign below the plane (in the excluded region), construct the combined Coulomb potential, and verify φ = 0 on the plane. No image charge actually exists below the plane — it is a mathematical fiction — but uniqueness guarantees that the resulting potential, which satisfies ∇²φ = 0 in the upper half-space and φ = 0 on the boundary, must be the actual physical potential. Uniqueness is what licenses such 'tricks' as rigorous."
```

## Explainer

You already know from Maxwell's equations in differential form that ∇·E = ρ/ε₀ (Gauss's law) and ∇×E = 0 in electrostatics (no time-varying magnetic fields). Since the curl of E vanishes, you can write E = −∇φ, where φ is the electric potential. Substituting into Gauss's law gives ∇·(−∇φ) = ρ/ε₀, or **Poisson's equation**: ∇²φ = −ρ/ε₀. This single PDE encodes all of electrostatics — every static electric field problem reduces to solving it. In a region free of charge (ρ = 0), it simplifies to **Laplace's equation**: ∇²φ = 0. The strategy shift is profound: instead of summing up the contributions of every charge directly, you find a potential function satisfying a partial differential equation and then recover E by differentiation.

Solutions to Laplace's equation are called **harmonic functions**, and they have a remarkable property: the value of φ at any point equals the average of φ over any sphere centered on that point. This **mean value theorem** immediately implies that harmonic functions cannot have local maxima or minima in a charge-free region — the potential must take its extreme values on the boundary. This is not just a mathematical curiosity; it is the foundation of **uniqueness theorems**. If you specify φ (Dirichlet) or ∂φ/∂n (Neumann) on all boundaries of a charge-free region, then the solution inside is unique. This means you can solve a problem in any convenient way — by symmetry, by guessing a form, by conformal mapping — and if you find a solution satisfying the boundary conditions, it is the only one.

The practical approach to solving Laplace's equation in many geometries is **separation of variables**. In Cartesian coordinates, you assume φ(x,y,z) = X(x)Y(y)Z(z) and find that each factor satisfies an ordinary differential equation with a separation constant. In spherical coordinates — natural for problems with a center of symmetry — the radial and angular parts separate into polynomial (Legendre) and exponential solutions, building toward the spherical harmonic decompositions that reappear in quantum mechanics. The key is choosing coordinates that match the symmetry of the boundary conditions.

For Poisson's equation with known source distributions, **Green's functions** provide the general framework. The Green's function G(r, r′) is the potential at r due to a unit point charge at r′, accounting for boundary conditions. Once you know G, the potential for any charge distribution is an integral: φ(r) = ∫ G(r,r′) ρ(r′)/ε₀ dV′. For an unbounded region, G = 1/(4πε₀|r − r′|), which is just the Coulomb potential — recovering the familiar superposition principle as a special case of the Green's function method. The general Green's function machinery handles conductors, cavities, and grounded surfaces by adding image charges or boundary correction terms, revealing the deep unity between seemingly different solution techniques.
