---
id: symmetry-breaking-phase-transitions
title: Symmetry Breaking and Phase Transitions
domain: physics
course: statistical-mechanics
prerequisites:
- id: long-range-order
  type: hard
- id: phase-transitions
  type: hard
- id: landau-theory
  type: soft
builds-toward:
- goldstone-theorem
tags:
- symmetry
- order-parameter
- phase-transitions
stage: advanced
status: draft
---

# Symmetry Breaking and Phase Transitions

## Core Idea
Spontaneous symmetry breaking occurs when a system adopts a state with lower symmetry than its governing Hamiltonian (e.g., magnetization breaks rotational symmetry). The order parameter quantifies symmetry breaking and vanishes at the transition, while long-range order emerges below the critical temperature.

## Explainer

You know from long-range order that below a critical temperature, distant regions of a material become correlated — a spin at one end of a magnet "knows" the orientation of a spin at the other end. You also know from phase transitions that macroscopic properties change discontinuously (first order) or continuously (second order) at well-defined temperatures. Symmetry breaking is the conceptual framework that unifies and explains both: it tells you *what kind* of order develops, *why* the ordered state is special, and how to describe the transition in a unified language.

The core idea is a tension between the Hamiltonian and the ground state. The Hamiltonian of a ferromagnet is invariant under rotating all spins simultaneously — it treats all directions equally. But below the Curie temperature, the actual state of the magnet has a definite magnetization pointing in some particular direction, breaking that rotational symmetry. The system has "chosen" one configuration from a family of energetically equivalent ones. Which direction it chose was determined by infinitesimal perturbations (the earth's magnetic field, a tiny grain boundary) during cooling — the ground state breaks the symmetry that the laws of physics respect. This is **spontaneous symmetry breaking**: the symmetry is hidden in the state, not broken in the laws.

The **order parameter** M is the quantity that measures how much symmetry has been broken. For a ferromagnet it is the magnetization (average spin per site); for a liquid-solid transition it is the crystal density wave amplitude; for a superconductor it is the amplitude of the Cooper pair condensate. The order parameter is exactly zero in the disordered (high-symmetry) phase and nonzero in the ordered (broken-symmetry) phase. Near a continuous (second-order) transition, it grows continuously from zero as you lower the temperature below T_c, typically as M ~ (T_c − T)^β where β is a critical exponent. This universal power-law behavior near T_c, independent of microscopic details, is what makes phase transitions a subject of deep theoretical interest.

The Landau theory (your soft prerequisite) captures the essential physics by writing the free energy as a power series in the order parameter: F = a(T)M² + bM⁴ + ... The coefficient a(T) changes sign at T_c: above T_c, a > 0 and the minimum is at M = 0 (disordered); below T_c, a < 0 and the minimum shifts to nonzero M (ordered). This "Mexican hat" or "wine bottle" potential landscape visualizes why the system spontaneously picks a direction at T_c. The symmetry of the potential (the ring of degenerate minima at the bottom) is the original symmetry; the system sitting at one point on that ring has broken it. The existence of that ring of degenerate minima — a continuous family of equivalent broken-symmetry states — implies, through Goldstone's theorem (a topic that builds on this one), the existence of massless excitations: the spin waves in a magnet, sound waves in a crystal, and the photon itself, all understood as consequences of spontaneous symmetry breaking.
