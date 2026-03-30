---
id: josephson-effect
title: Josephson Effect
domain: physics
course: condensed-matter-physics
prerequisites:
- id: bcs-theory-detailed
  type: hard
- id: ginzburg-landau-theory
  type: soft
tags:
- josephson-effect
- josephson-junction
- squid
- macroscopic-quantum
stage: expert
status: validated
---

# Josephson Effect

## Core Idea
When two superconductors are connected by a weak link (thin insulating barrier, narrow constriction, or normal metal), a supercurrent flows that depends on the phase difference phi = phi_1 - phi_2 between the two superconducting order parameters: I = I_c sin(phi) (DC Josephson effect). If a voltage V is applied across the junction, the phase evolves as d(phi)/dt = 2eV/hbar, producing an AC current at frequency f = 2eV/h (AC Josephson effect). The Josephson effects are macroscopic quantum phenomena that directly manifest the phase of the superconducting wavefunction and form the basis of SQUIDs (superconducting quantum interference devices), voltage standards, and superconducting qubits.

## Questions

```yaml
- question: "The DC Josephson effect — supercurrent flowing through a barrier with zero voltage — seems to violate intuition. What makes it possible?"
  type: multiple-choice
  options:
    - "The current tunnels through the barrier due to the kinetic energy of the electrons"
    - "Cooper pairs tunnel coherently through the weak link, maintaining phase coherence between the two superconductors. The supercurrent I = I_c sin(φ) depends only on the phase difference, not on any applied voltage, because the pairs tunnel as quantum mechanical entities without breaking — no energy dissipation occurs"
    - "The barrier becomes superconducting due to proximity effect"
    - "Normal electrons carry the current through the barrier"
  answer: 1
  explanation: "The DC Josephson effect is a direct consequence of macroscopic quantum coherence. The superconducting order parameter ψ = |ψ|e^{iφ} exists on both sides of the barrier, and the overlap of these wavefunctions through the thin barrier allows Cooper pairs to tunnel without dissipation. The current depends on the phase difference because quantum mechanical tunneling rates depend on the relative phase of the wavefunctions. This is entirely analogous to tunneling in a double-well potential, but operating at the macroscopic scale with ~10²³ Cooper pairs participating coherently."

- question: "The AC Josephson effect relates a DC voltage to an oscillating current at frequency f = 2eV/h. Why does the factor 2e (rather than e) appear?"
  type: multiple-choice
  options:
    - "Two electrons tunnel simultaneously by coincidence"
    - "The charge carriers are Cooper pairs with charge 2e. The phase evolves as dφ/dt = 2eV/ħ because the energy of a Cooper pair in a potential difference V is 2eV, and the quantum phase accumulates as E/ħ per unit time"
    - "It accounts for spin degeneracy"
    - "The factor of 2 is an approximation that works for conventional superconductors"
  answer: 1
  explanation: "The 2e is direct experimental proof that the fundamental charge carriers in a superconductor are Cooper pairs, not single electrons. When Shapiro (1963) irradiated a Josephson junction with microwaves and observed voltage steps at V_n = nhf/2e, the factor of 2e was confirmed precisely. The AC Josephson effect now defines the international voltage standard: applying a known microwave frequency f to a junction produces voltage steps at exactly V = nhf/2e, with no material-dependent corrections."

- question: "A SQUID (Superconducting Quantum Interference Device) uses two Josephson junctions in a superconducting loop to detect magnetic flux changes as small as a fraction of Φ₀. Explain the operating principle."
  type: short-answer
  answer: "In a DC SQUID, a superconducting loop containing two Josephson junctions has its critical current modulated by the magnetic flux Φ through the loop. Flux quantization requires that the total phase around the loop (including the two junction phase drops) equals 2πΦ/Φ₀. This creates interference between the supercurrents through the two junctions: the maximum critical current oscillates as I_c(Φ) = 2I₀|cos(πΦ/Φ₀)|. By biasing the SQUID just above its critical current, tiny changes in flux produce measurable voltage changes. The sensitivity can reach 10⁻⁶ Φ₀/√Hz, making SQUIDs the most sensitive magnetic flux detectors, used in magnetoencephalography, geological surveys, and fundamental physics experiments."
  explanation: "The SQUID is essentially a superconducting analog of Young's double-slit experiment: the two junctions are the 'slits,' and the magnetic flux controls the phase difference, creating an interference pattern in the critical current."

- question: "Josephson junctions are the building blocks of superconducting quantum computers. What property makes them suitable as qubits?"
  type: short-answer
  answer: "A Josephson junction acts as a nonlinear, dissipation-free inductor (the Josephson energy is E_J cos(φ)), which when combined with the capacitive charging energy E_C = (2e)²/2C of the junction, creates an anharmonic quantum oscillator. The anharmonicity — the fact that energy levels are not equally spaced — is essential: it allows selective addressing of the two lowest levels (|0⟩ and |1⟩) as a qubit without exciting higher levels. The dissipation-free nature of supercurrents gives long coherence times. Different qubit designs (charge, flux, transmon) correspond to different ratios of E_J/E_C, optimizing the tradeoff between sensitivity to noise and anharmonicity."
  explanation: "Without the nonlinearity of the Josephson junction, a superconducting circuit would be a harmonic oscillator with equally spaced levels — useless as a qubit because a pulse exciting 0→1 would also excite 1→2. The cos(φ) nonlinearity is the crucial ingredient that makes superconducting qubits possible."
```

## Explainer

The Josephson effects, predicted by Brian Josephson in 1962 (Nobel Prize 1973), are among the most remarkable manifestations of macroscopic quantum mechanics. They arise whenever two superconductors are connected by a **weak link** — a region where the superconducting order parameter is suppressed but not zero. The weak link can be a thin insulating barrier (~1-2 nm of oxide), a point contact, a narrow constriction, or a short normal-metal bridge.

The **DC Josephson effect** states that a supercurrent I = I_c sin(phi) flows through the junction with zero voltage, where phi = phi_1 - phi_2 is the phase difference between the two superconductors and I_c is the critical current of the junction. The current is carried by Cooper pairs tunneling coherently through the barrier. This is truly remarkable: a macroscopic current (microamps to milliamps) flows through an insulating barrier with no applied voltage, driven entirely by the quantum phase difference. The maximum current I_c depends exponentially on the barrier thickness and on the gap values of the superconductors.

The **AC Josephson effect** emerges when a DC voltage V is applied across the junction. The phase evolves as d(phi)/dt = 2eV/hbar, so the supercurrent oscillates: I = I_c sin(phi_0 + 2eVt/hbar), with frequency f = 2eV/h. For V = 1 mV, f = 484 GHz — in the far-infrared range. The frequency-voltage ratio 2e/h = 483.5979 GHz/mV is a fundamental constant with no material dependence, making the AC Josephson effect the basis of the international voltage standard. When microwaves at frequency f are applied simultaneously, the junction develops constant-voltage steps at V_n = nhf/2e (Shapiro steps), providing a precise voltage reference.

The combination of Josephson junctions with superconducting loops produces **SQUIDs** — the most sensitive magnetic flux detectors known. A DC SQUID (two junctions in a loop) exploits the interference of supercurrents from the two junctions, modulated by the magnetic flux through the loop via flux quantization. SQUIDs can detect flux changes of 10^{-6} Phi_0, corresponding to magnetic fields of ~10^{-15} T. Beyond sensing, Josephson junctions are the active elements in **superconducting qubits**: their nonlinear inductance creates the anharmonic energy spectrum needed to define a two-level quantum system, and the absence of dissipation enables coherence times sufficient for quantum computation. Superconducting quantum processors from IBM, Google, and others are built entirely from Josephson junction circuits.
