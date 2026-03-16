---
id: order-parameter-phase-transition
title: Order Parameters and Phase Transitions
domain: physics
course: statistical-mechanics
prerequisites:
- id: phase-transition-equilibrium
  type: hard
- id: spontaneous-symmetry-breaking
  type: soft
builds-toward:
- landau-theory-phase-transitions
- mean-field-theory-statmech
tags:
- order-parameter
- symmetry-breaking
- magnetization
stage: advanced
status: draft
---

# Order Parameters and Phase Transitions

## Core Idea
An order parameter M characterizes the broken symmetry phase: M=0 above transition, M≠0 below. For magnetism, M is the average magnetization. The free energy as a function of M has a single minimum at M=0 above T_c and splits into two minima below T_c. Minimizing the free energy yields self-consistent equations for M(T), enabling computation of critical exponents.

## Explainer

Phase transitions come with a structural change in the system's symmetry. Above the Curie temperature of a ferromagnet, all directions of magnetization are equally likely — the system has full rotational symmetry and the average magnetization is zero. Below Tc, the system spontaneously picks a direction and remains magnetized even without an external field. The symmetry has been **broken**: the thermodynamic state no longer has the full symmetry of the underlying Hamiltonian. The **order parameter** M is the quantity that is zero in the symmetric (disordered) phase and nonzero in the broken-symmetry (ordered) phase. It is the mathematical fingerprint of order.

The language generalizes far beyond magnets. For a liquid-gas transition, the order parameter is the density difference ρ_liquid − ρ_gas. For a superconductor or Bose-Einstein condensate, it is the complex condensate wavefunction ψ. For a crystal, it is the amplitude of the periodic density wave. What these have in common is that the order parameter is zero in the high-symmetry phase and grows continuously or discontinuously as you cool through the transition. For a **continuous (second-order) transition**, M grows from zero smoothly as T decreases below Tc, following a power law M ~ (Tc − T)^β near the transition. The exponent β is a **critical exponent**, and its value is remarkably universal — it depends not on microscopic details of the material but only on the dimensionality of the system and the symmetry of the order parameter.

The Landau free energy framework (from your prerequisite on phase-transition-equilibrium) makes this precise. Write the free energy as a polynomial in M consistent with the symmetry: F(M) = F₀ + a(T)M² + bM⁴ + .... For the transition to be continuous and M to be small near Tc, you need a(T) to change sign at Tc: a(T) = a₀(T − Tc). Above Tc, a > 0, F has a single minimum at M = 0. Below Tc, a < 0, and F develops a **double-well** (or Mexican-hat in higher dimensions): the minimum shifts to M = ±√(−a/2b) ≠ 0. The system falls into one of these wells — that is spontaneous symmetry breaking. Setting ∂F/∂M = 0 and solving gives the equilibrium order parameter as a function of T.

**Critical exponents** characterize how physical quantities diverge or vanish at Tc. Mean-field theory (which is what Landau theory implements) predicts β = ½ (magnetization), γ = 1 (susceptibility), and ν = ½ (correlation length). Real systems often differ because mean-field ignores spatial fluctuations that become important near the critical point. The **universality class** — which exponents a system falls into — is set by symmetry and dimensionality, not chemistry. This is why the critical exponents of water near its liquid-gas critical point match those of a uniaxial magnet near its Curie point: they belong to the same universality class (Ising model in 3D). This surprising universality is one of the deepest insights of modern statistical mechanics.
