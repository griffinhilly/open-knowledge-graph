---
id: wavefunctions-boundary-conditions
title: Wavefunctions and Boundary Conditions
domain: physics
course: modern-physics
prerequisites:
- id: schrodinger-equation-time-dependent
  type: hard
- id: uncertainty-relation-measurements
  type: soft
- id: stopping-potential-kinetic-energy
  type: soft
builds-toward:
- probability-amplitude-interpretation
- particle-in-box-1d
tags:
- quantum-mechanics
- boundary-conditions
stage: advanced
status: validated
---
# Wavefunctions and Boundary Conditions

## Core Idea
Wavefunctions must be continuous, single-valued, and normalizable; at potential barriers they must vanish (or approach zero). These boundary conditions arise from the physical requirement that the wavefunction represents probability and from continuity of the probability current. Boundary conditions quantize energy levels: only certain discrete energies satisfy both the Schrödinger equation and the boundary conditions.

## How It's Best Learned
Solve the particle-in-a-box problem explicitly, deriving the quantization condition from boundary conditions. Visualize low-energy wavefunctions to see how nodes emerge.

## Questions

```yaml
- question: "A student argues: 'Energy is quantized in a particle-in-a-box because particles are wave-like, and waves naturally come in integer multiples of half-wavelengths.' What is the most precise critique of this reasoning?"
  type: multiple-choice
  options:
    - "Particles are not actually wave-like — only photons are, so the analogy fails"
    - "The reasoning is correct — wave-particle duality is the source of quantization"
    - "The reasoning is imprecise: discreteness emerges from imposing physical boundary conditions (ψ = 0 at the walls) on the Schrödinger equation, not from the wave nature alone — many wave-like systems have continuous spectra"
    - "Energy quantization only occurs in infinite potential wells; finite wells have continuous spectra"
  answer: 2
  explanation: "Wave-particle duality does not by itself produce discrete energy. What produces discreteness is the *combination* of: (1) a differential equation whose general solution is sinusoidal, and (2) boundary conditions that restrict which solutions are physically allowed. A free particle (no walls) is wave-like but has a continuous energy spectrum. Quantization enters specifically because the boundary conditions ψ(0) = 0 and ψ(L) = 0 force kL = nπ, selecting discrete k values and hence discrete energies. The boundary conditions are the mathematical source of quantization."

- question: "Inside a particle-in-a-box of length L (0 < x < L), the Schrödinger equation gives the general solution ψ = A sin(kx) + B cos(kx). Applying the boundary condition at x = 0 and then at x = L gives which result?"
  type: multiple-choice
  options:
    - "B = 0 from ψ(0) = 0; then sin(kL) = 0 forces kL = nπ, selecting discrete energies"
    - "A = 0 from ψ(0) = 0; then cos(kL) = 0 forces kL = (2n-1)π/2, selecting discrete energies"
    - "Both A = B from symmetry; then the combined condition gives k = nπ/2L"
    - "k = 0 is required, so ψ is constant — a trivial solution that must be normalized"
  answer: 0
  explanation: "ψ(0) = A·sin(0) + B·cos(0) = B = 0, so the cosine term is eliminated. The solution reduces to ψ = A sin(kx). Then ψ(L) = A sin(kL) = 0. Since A ≠ 0 (non-trivial solution), sin(kL) = 0, which requires kL = nπ for positive integers n. Each n gives a distinct energy E_n = n²π²ℏ²/(2mL²). This is the canonical derivation: the boundary conditions, not any physical assumption about quantization, force k to take discrete values."

- question: "Energy quantization in the particle-in-a-box arises from the boundary conditions imposed on the wavefunction, not from any prior assumption that energy must be discrete."
  type: true-false
  answer: true
  explanation: "This is the central conceptual point. The Schrödinger equation inside the box has solutions for any value of k — continuous energies are mathematically valid solutions to the differential equation. What eliminates all but the discrete set kL = nπ is the physical requirement that the wavefunction vanish at both walls (ψ = 0 where V = ∞). Solutions that don't vanish at the walls are solutions to the Schrödinger equation but not physically acceptable wavefunctions. Quantization is a consequence of physical constraints, not an assumption."

- question: "The condition that dψ/dx is expected to be continuous should hold everywhere, including at infinite potential steps."
  type: true-false
  answer: false
  explanation: "The continuity of dψ/dx is required where the potential V is finite, because a discontinuous slope would imply infinite kinetic energy (the kinetic energy operator involves the second derivative of ψ). At an *infinite* potential step, however, ψ must equal zero inside the wall, and the derivative of ψ just outside may be nonzero while ψ = 0 inside — the slope can be discontinuous. The infinite potential can supply an infinite force, which is what permits the discontinuous derivative. This exception is why the particle-in-a-box boundary condition is simply ψ = 0 at the walls, not dψ/dx = 0."

- question: "Why must a wavefunction be both continuous and normalizable, and how do these requirements together produce energy quantization in a confined system?"
  type: short-answer
  answer: "Normalizability requires that ∫|ψ|² dx = 1 (finite), so ψ cannot diverge anywhere and must go to zero at infinity (or at hard walls). Continuity is required because |ψ|² represents probability density, and a jump discontinuity in ψ would imply a delta-function-like spike in probability current, which is unphysical. Together, these constraints act as selection filters on the solutions to the Schrödinger equation: inside a box, the general solution is A sin(kx) + B cos(kx) for any k. Normalizability forces ψ = 0 at the walls; continuity forces the solution to match smoothly. Only discrete values of k satisfy both: those for which the sinusoidal solution completes an integer number of half-wavelengths and vanishes at both walls. Each allowed k corresponds to a discrete energy, producing the quantized spectrum."
  explanation: "The key conceptual insight is that differential equations always have families of solutions, and physical interpretation narrows this family dramatically. Continuity and normalizability are not independent axioms — they follow from interpreting |ψ|² as a probability density. The boundary conditions that express these requirements in specific geometries are what convert a continuous family of solutions into a discrete spectrum."
```

## Explainer

The time-dependent Schrödinger equation is a differential equation, and like all differential equations it requires boundary conditions to select a unique solution from the infinitely many functions that satisfy the equation in its interior. The physical interpretation of the wavefunction — that |ψ(x)|² is a probability density — immediately constrains what ψ can do. A probability density must be non-negative and integrable over all space (so the total probability is 1), which means ψ must be **normalizable**: it cannot blow up at infinity or diverge anywhere. At hard walls (infinite potential), there is zero probability of finding the particle inside the wall, so ψ must vanish at the boundary.

Two further conditions complete the set. First, ψ must be **continuous** everywhere: a jump discontinuity in ψ would require an infinite probability current at that point, which is unphysical (it would imply particles teleporting). Second, the derivative dψ/dx must also be continuous wherever the potential is finite — a discontinuous slope would require an infinite kinetic energy (since the kinetic energy operator involves the second derivative). The exception is an *infinite* potential step, where dψ/dx can be discontinuous because the infinite potential can supply an infinite force. These three rules — normalizability, continuity of ψ, and continuity of dψ/dx at finite potentials — are the complete set of wavefunction boundary conditions.

The particle-in-a-box illustrates how these conditions produce **energy quantization**. Inside the box (0 < x < L), the Schrödinger equation gives sinusoidal solutions ψ(x) = A sin(kx) + B cos(kx). The boundary condition ψ(0) = 0 forces B = 0, leaving ψ(x) = A sin(kx). The boundary condition ψ(L) = 0 then requires sin(kL) = 0, which means kL = nπ for positive integers n = 1, 2, 3, ... Each allowed value of k corresponds to one allowed energy E = ℏ²k²/(2m) = n²π²ℏ²/(2mL²). The quantization did not come from assuming energy is discrete — it came from enforcing the boundary conditions. Continuous energies would correspond to wavefunctions that do not vanish at the walls: they are solutions to the differential equation but not physically acceptable ones.

The number of **nodes** (zero crossings inside the box) equals n−1 for the nth energy level. This is a general pattern in quantum mechanics: the ground state has no nodes, the first excited state has one, and higher states have more. Nodes accumulate kinetic energy because more oscillations mean a larger second derivative of ψ — physically, more curvature in the wavefunction means the particle has more kinetic energy on average. This node-counting rule, forced by boundary conditions, is why energy levels are ordered the way they are and why no two bound eigenstates have the same energy in a one-dimensional confining potential.
