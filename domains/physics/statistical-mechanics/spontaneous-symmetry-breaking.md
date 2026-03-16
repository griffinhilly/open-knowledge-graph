---
id: spontaneous-symmetry-breaking
title: Spontaneous Symmetry Breaking
domain: physics
course: statistical-mechanics
prerequisites:
- id: phase-transition-equilibrium
  type: hard
- id: landau-theory-phase-transitions
  type: soft
builds-toward:
- renormalization-group-scaling
tags:
- symmetry-breaking
- ground-state
- degeneracy
stage: advanced
status: draft
---

# Spontaneous Symmetry Breaking

## Core Idea
A system with symmetric interactions (H invariant under spin flip, for instance) can develop a state with lower symmetry when the free energy cost is outweighed by entropy gain. The ordered phase selects one of multiple degenerate ground states, breaking symmetry. This mechanism is fundamental to magnetism, superconductivity, and particle physics and emerges from statistical mechanics below a critical temperature.

## Explainer

From phase transitions you know that systems can undergo qualitative changes in behavior at critical temperatures — water freezes, magnets lose magnetism, and so on. **Spontaneous symmetry breaking** is the precise mechanism that explains why the ordered phase that appears below T_c looks different from the symmetric high-temperature phase, even when the underlying Hamiltonian has full symmetry.

Consider a ferromagnet. The Hamiltonian H = −J Σ S_i · S_j is symmetric under flipping all spins simultaneously (S_i → −S_i): if you negate every spin, the energy is the same. At high temperature, this symmetry is manifest — the average magnetization ⟨M⟩ = 0 because up and down spins are equally likely, and the system explores both equally. Below the **Curie temperature** T_c, the free energy develops two minima at ±M₀. The equilibrium state must pick one — say, ⟨M⟩ = +M₀. The ground state is no longer symmetric under spin flip even though the Hamiltonian is. Symmetry is "broken" because the state the system actually occupies does not share the symmetry of the equations that govern it.

The Landau theory you studied makes this quantitative. Near T_c, expand the free energy as F = a(T)M² + bM⁴ + ..., where a(T) changes sign at T_c. Above T_c, a > 0 and the free energy has a single minimum at M = 0 (the **disordered phase**). Below T_c, a < 0 and the shape becomes a **Mexican hat** (or double well in 1D) with minima at ±M₀ = ±√(−a/2b). The system must settle in one of these minima — this selection is the spontaneous symmetry breaking. An infinitesimal symmetry-breaking perturbation (a tiny external field, a fluctuation, a boundary condition) picks which minimum, but the effect persists even after the perturbation is removed.

A crucial consequence is the existence of **Goldstone modes**. Whenever a continuous symmetry (like rotational symmetry of the magnetization direction in a Heisenberg ferromagnet) is spontaneously broken, there appear low-energy, long-wavelength collective excitations — **magnons** in ferromagnets, **phonons** in crystals, **pions** in nuclear physics — that cost zero energy in the long-wavelength limit. These are the "ripples" of the order parameter rotating slowly in space, and they dominate the low-temperature physics of ordered phases. Spontaneous symmetry breaking thus does double duty: it explains *why* ordered phases exist and *what* their low-energy excitation spectrum looks like.
