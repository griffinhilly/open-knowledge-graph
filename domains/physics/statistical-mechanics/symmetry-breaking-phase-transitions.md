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

## Questions

```yaml
- question: "A ferromagnet's Hamiltonian is invariant under rotating all spins simultaneously. Below the Curie temperature, the magnet develops a net magnetization pointing north. What does this imply?"
  type: multiple-choice
  options:
    - "The Hamiltonian has changed — it now favors the north direction over others"
    - "The ground state has broken the rotational symmetry that the Hamiltonian still respects"
    - "The order parameter enforces the symmetry of the Hamiltonian onto the ground state"
    - "The symmetry is broken because the critical temperature removes the rotational invariance from the equations"
  answer: 1
  explanation: "This is the core of spontaneous symmetry breaking: the Hamiltonian remains rotationally invariant — it still treats all spin directions equally. The ground state, however, has 'chosen' one direction from the family of equivalent low-energy configurations. Tiny perturbations during cooling determined which direction was chosen, but the laws themselves did not change. The symmetry is hidden in the state, not broken in the physics."

- question: "At a continuous (second-order) phase transition, how does the order parameter behave as temperature passes through T_c?"
  type: multiple-choice
  options:
    - "It jumps discontinuously from zero to a finite value at T_c"
    - "It remains zero above T_c and grows continuously from zero below T_c"
    - "It is nonzero on both sides of T_c but changes sign at T_c"
    - "It diverges to infinity at T_c, then decreases below it"
  answer: 1
  explanation: "The order parameter is the signature of symmetry breaking: it is exactly zero in the disordered phase (T > T_c, where the full symmetry is intact) and grows continuously from zero below T_c, typically as M ~ (T_c − T)^β. The discontinuous jump describes a first-order transition, not a continuous one. Divergence at T_c is characteristic of susceptibility or correlation length, not the order parameter itself."

- question: "In spontaneous symmetry breaking, the Hamiltonian retains the symmetry that the ground state breaks."
  type: true-false
  answer: true
  explanation: "This is the defining feature of spontaneous symmetry breaking: the laws (Hamiltonian) are symmetric, but the equilibrium state the system occupies is not. A ferromagnet's Hamiltonian treats all spin directions equally, yet below T_c the magnet points in a definite direction. The symmetry is spontaneously broken by the state, not by the forces."

- question: "The 'Mexican hat' free energy landscape of Landau theory means the system below T_c is trapped in a unique, stable minimum with no symmetry."
  type: true-false
  answer: false
  explanation: "The Mexican hat potential has a continuous ring of degenerate minima at the bottom — every point on the ring is equally valid. The system sits at one point on the ring, which breaks the symmetry, but that point is not unique: all points on the ring are equivalent ground states related by the symmetry that was broken. This continuous family of degenerate ground states is exactly what implies the existence of Goldstone modes (massless excitations) through Goldstone's theorem."

- question: "Why does a ferromagnet below its Curie temperature spontaneously magnetize in a particular direction, even though the Hamiltonian treats all directions equally?"
  type: short-answer
  answer: "Because the symmetric Hamiltonian has a family of energetically equivalent ordered states (all pointing in different directions), and the system must occupy one of them. Infinitesimal perturbations — the Earth's magnetic field, microscopic imperfections — select which of these degenerate minima the system falls into during cooling. The symmetry is broken by the state the system occupies, not by the laws governing it."
  explanation: "This question targets the key conceptual move: the distinction between symmetry of the laws and symmetry of the state. Many students conflate the two, thinking that if a magnet points north, the physics must somehow favor north. Instead, the physics is indifferent — but the system must pick one direction, and it does so through the amplification of microscopic fluctuations. Understanding this prepares students for Goldstone's theorem, where the continuous degeneracy of ground states is the direct cause of massless excitations."
```

## Explainer

You know from long-range order that below a critical temperature, distant regions of a material become correlated — a spin at one end of a magnet "knows" the orientation of a spin at the other end. You also know from phase transitions that macroscopic properties change discontinuously (first order) or continuously (second order) at well-defined temperatures. Symmetry breaking is the conceptual framework that unifies and explains both: it tells you *what kind* of order develops, *why* the ordered state is special, and how to describe the transition in a unified language.

The core idea is a tension between the Hamiltonian and the ground state. The Hamiltonian of a ferromagnet is invariant under rotating all spins simultaneously — it treats all directions equally. But below the Curie temperature, the actual state of the magnet has a definite magnetization pointing in some particular direction, breaking that rotational symmetry. The system has "chosen" one configuration from a family of energetically equivalent ones. Which direction it chose was determined by infinitesimal perturbations (the earth's magnetic field, a tiny grain boundary) during cooling — the ground state breaks the symmetry that the laws of physics respect. This is **spontaneous symmetry breaking**: the symmetry is hidden in the state, not broken in the laws.

The **order parameter** M is the quantity that measures how much symmetry has been broken. For a ferromagnet it is the magnetization (average spin per site); for a liquid-solid transition it is the crystal density wave amplitude; for a superconductor it is the amplitude of the Cooper pair condensate. The order parameter is exactly zero in the disordered (high-symmetry) phase and nonzero in the ordered (broken-symmetry) phase. Near a continuous (second-order) transition, it grows continuously from zero as you lower the temperature below T_c, typically as M ~ (T_c − T)^β where β is a critical exponent. This universal power-law behavior near T_c, independent of microscopic details, is what makes phase transitions a subject of deep theoretical interest.

The Landau theory (your soft prerequisite) captures the essential physics by writing the free energy as a power series in the order parameter: F = a(T)M² + bM⁴ + ... The coefficient a(T) changes sign at T_c: above T_c, a > 0 and the minimum is at M = 0 (disordered); below T_c, a < 0 and the minimum shifts to nonzero M (ordered). This "Mexican hat" or "wine bottle" potential landscape visualizes why the system spontaneously picks a direction at T_c. The symmetry of the potential (the ring of degenerate minima at the bottom) is the original symmetry; the system sitting at one point on that ring has broken it. The existence of that ring of degenerate minima — a continuous family of equivalent broken-symmetry states — implies, through Goldstone's theorem (a topic that builds on this one), the existence of massless excitations: the spin waves in a magnet, sound waves in a crystal, and the photon itself, all understood as consequences of spontaneous symmetry breaking.
