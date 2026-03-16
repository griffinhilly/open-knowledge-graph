---
id: particle-in-a-box
title: Particle in a Box (Infinite Square Well)
domain: physics
course: modern-physics
prerequisites:
- id: schrodinger-equation-intro
  type: hard
- id: differential-equations-intro
  type: hard
- id: boundary-value-problems-electrostatics
  type: hard
builds-toward:
- quantum-tunneling
- quantum-numbers
- band-theory-intro
tags:
- quantum
- infinite-square-well
- energy-levels
- standing-waves
- zero-point-energy
stage: advanced
status: validated
---

# Particle in a Box (Infinite Square Well)

## Core Idea
A particle confined between rigid walls at x=0 and x=L (where V=0 inside, V=∞ outside) has wavefunctions ψ_n = √(2/L) sin(nπx/L) and quantized energies E_n = n²π²ℏ²/(2mL²) for n = 1, 2, 3, … The lowest allowed energy E₁ > 0 is the zero-point energy — a purely quantum effect arising from the uncertainty principle: confinement in space requires nonzero momentum spread. The model illustrates energy quantization, node structure of wavefunctions, and the role of boundary conditions in selecting allowed states.

## How It's Best Learned
Solve the Schrödinger equation step by step: write down the general solution inside the box, apply boundary conditions to get standing-wave condition kL = nπ, then compute energies. Sketch the first few wavefunctions and probability densities and note the number of nodes.

## Common Misconceptions
- The particle can be at rest at the bottom of the box — the zero-point energy forbids it; E₁ is strictly positive.
- Larger boxes have higher energies — larger L means smaller E_n for fixed n; particles in bigger boxes have lower energy levels.
- The wavefunction outside the box is undefined — it is zero (enforced by infinite potential), and this is what imposes the boundary condition.

## Explainer

The time-independent Schrödinger equation, which you've studied, requires both a wavefunction ψ(x) and a potential V(x). In the particle-in-a-box model, V(x) = 0 inside (0 < x < L) and V(x) = ∞ outside. The infinite potential enforces a hard boundary: the wavefunction must be exactly zero wherever V = ∞ (otherwise the energy eigenvalue equation -ℏ²/(2m)d²ψ/dx² + Vψ = Eψ would require infinite energy). This gives two **boundary conditions**: ψ(0) = 0 and ψ(L) = 0. Boundary conditions are the bridge between the differential equation, which has infinitely many solutions, and the physical constraint that selects the allowed ones.

Inside the box, V = 0, so the Schrödinger equation reduces to -ℏ²/(2m) · d²ψ/dx² = Eψ, or equivalently d²ψ/dx² = −k²ψ where k² = 2mE/ℏ². This is the same differential equation as simple harmonic oscillation in x, with general solution ψ(x) = A sin(kx) + B cos(kx). Applying ψ(0) = 0 forces B = 0 (since cos(0) = 1 ≠ 0). Applying ψ(L) = 0 then requires sin(kL) = 0, which means kL = nπ for integer n = 1, 2, 3, ... (n = 0 would give ψ = 0 everywhere — no particle). This is the **standing wave condition**, the same constraint that determines harmonic frequencies of a guitar string clamped at both ends. Only wavelengths that fit exactly inside the box produce stable solutions.

The **quantized energies** follow from the allowed values of k. Since E = ℏ²k²/(2m) and k = nπ/L, substituting gives E_n = n²π²ℏ²/(2mL²). Notice that energies grow as n² — higher levels are increasingly spread apart, unlike classical oscillator harmonics (which are evenly spaced). The minimum allowed energy E₁ = π²ℏ²/(2mL²) is strictly greater than zero: this **zero-point energy** is not a measurement artifact but a fundamental consequence of confinement. By the Heisenberg uncertainty principle, confining a particle to a region of width L imposes a position uncertainty Δx ~ L, which requires a momentum uncertainty Δp ~ ℏ/L, which means nonzero average kinetic energy. A confined particle *cannot* be at rest — it would require definite zero momentum, violating the uncertainty bound set by the confinement itself.

The normalized wavefunctions ψ_n(x) = √(2/L) sin(nπx/L) have a node structure that is both mathematically and physically meaningful. The n=1 ground state has no nodes between the walls — one smooth half-wave with maximum probability at the center. The n=2 state has one node at the center, two probability peaks near L/4 and 3L/4 — the particle *avoids* the center entirely. The n-th state has (n−1) interior nodes. This node structure directly parallels acoustic standing waves in a tube and provides the foundation for understanding electron behavior in real quantum systems. In a crystal lattice, electrons are confined to periodic potential wells and develop **energy bands** governed by essentially the same physics. In **quantum dots** — semiconductor nanostructures a few nanometers across — the confinement length L appears in E_1 ∝ 1/L², making their color tunable by size. The particle-in-a-box is not just a textbook model; it is the conceptual core of solid-state physics and nanotechnology.
