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
stage: expert
status: draft
---

# Spontaneous Symmetry Breaking

## Core Idea
A system with symmetric interactions (H invariant under spin flip, for instance) can develop a state with lower symmetry when the free energy cost is outweighed by entropy gain. The ordered phase selects one of multiple degenerate ground states, breaking symmetry. This mechanism is fundamental to magnetism, superconductivity, and particle physics and emerges from statistical mechanics below a critical temperature.

## Questions

```yaml
- question: "A ferromagnet is cooled below its Curie temperature with no external magnetic field applied at any point. It develops a net magnetization pointing in one direction. Which statement best explains this outcome?"
  type: multiple-choice
  options:
    - "The Hamiltonian changes at Tc to favor one spin orientation over the other"
    - "Although the Hamiltonian remains spin-flip symmetric, the system must choose one of two degenerate free-energy minima, and even infinitesimal fluctuations select one"
    - "Thermal fluctuations above Tc permanently break the spin-flip symmetry before cooling begins"
    - "Quantum mechanical effects in the spin Hamiltonian force a preferred orientation below Tc"
  answer: 1
  explanation: "The key is that the Hamiltonian is always symmetric — flipping all spins leaves the energy unchanged. But below Tc, the free energy develops two minima (±M₀). The system cannot sit at M=0 (that becomes a local maximum) and must choose one minimum. The selection is made by infinitesimal asymmetries — a stray field, a fluctuation, a boundary effect — but the symmetry-breaking state persists even after these perturbations vanish. The symmetry of the equations does not prevent the state from being asymmetric."

- question: "Breaking a continuous symmetry (e.g., the full rotational symmetry of magnetization direction in a Heisenberg ferromagnet) has a consequence that breaking a discrete symmetry (e.g., spin-flip in an Ising model) does NOT. What is it?"
  type: multiple-choice
  options:
    - "The ordered phase is thermodynamically stable only for continuous symmetries"
    - "Gapless Goldstone modes appear — low-energy collective excitations (like magnons) that cost zero energy in the long-wavelength limit"
    - "The phase transition occurs at a uniquely defined critical temperature only for continuous symmetries"
    - "Multiple degenerate ground states exist only when a continuous symmetry is broken"
  answer: 1
  explanation: "Goldstone's theorem applies specifically to continuous symmetries: whenever a continuous symmetry is spontaneously broken, gapless excitations appear corresponding to slow spatial rotations of the order parameter. Magnons in ferromagnets, phonons in crystals, and pions in nuclear physics are all Goldstone modes. Discrete symmetry breaking (like the Ising model's Z₂ spin flip) does not produce Goldstone modes — there is no continuous direction to rotate the order parameter."

- question: "A system can occupy a ground state with lower symmetry than its own Hamiltonian."
  type: true-false
  answer: true
  explanation: "This is precisely what spontaneous symmetry breaking means. The Hamiltonian (and all the laws governing the system) may be fully symmetric, yet the actual state the system occupies — the ground state selected from among degenerate minima — can break that symmetry. The ferromagnet is the textbook example: H is spin-flip symmetric, but the ground state has ⟨M⟩ ≠ 0."

- question: "Spontaneous symmetry breaking requires a finite external symmetry-breaking field to be permanently applied in order to maintain the ordered state below Tc."
  type: true-false
  answer: false
  explanation: "The word 'spontaneous' means exactly that no sustained external field is required. An infinitesimal perturbation (a tiny field, a fluctuation, a boundary condition) can select which minimum the system falls into, but once there, the system stays even after the perturbation is removed. This is the thermodynamic limit effect: in a finite system, quantum or thermal tunneling between minima is possible, but in the thermodynamic limit (N → ∞), the barrier becomes infinite and the broken-symmetry state is stable indefinitely."

- question: "Why is the term 'spontaneous' essential in 'spontaneous symmetry breaking'? How does it differ from explicit symmetry breaking?"
  type: short-answer
  answer: "Spontaneous symmetry breaking occurs when the Hamiltonian (the fundamental equations) retains full symmetry, but the system's actual state does not share that symmetry — it has selected one of several equivalent ground states. No asymmetric term appears in the equations. Explicit symmetry breaking, by contrast, occurs when the Hamiltonian itself is modified by an asymmetric term (e.g., adding an external field H·M), so the equations themselves are no longer symmetric."
  explanation: "The distinction matters because spontaneous breaking is an emergent property of the many-body system, not a feature of the fundamental laws. It explains how ordered phases arise in systems governed by symmetric physics. In the Mexican-hat free-energy picture: spontaneous breaking means the hat is symmetric, but the ball rolls to the rim and stays there; explicit breaking would mean the hat is tilted from the start, with one part of the rim lower than the rest."
```

## Explainer

From phase transitions you know that systems can undergo qualitative changes in behavior at critical temperatures — water freezes, magnets lose magnetism, and so on. **Spontaneous symmetry breaking** is the precise mechanism that explains why the ordered phase that appears below T_c looks different from the symmetric high-temperature phase, even when the underlying Hamiltonian has full symmetry.

Consider a ferromagnet. The Hamiltonian H = −J Σ S_i · S_j is symmetric under flipping all spins simultaneously (S_i → −S_i): if you negate every spin, the energy is the same. At high temperature, this symmetry is manifest — the average magnetization ⟨M⟩ = 0 because up and down spins are equally likely, and the system explores both equally. Below the **Curie temperature** T_c, the free energy develops two minima at ±M₀. The equilibrium state must pick one — say, ⟨M⟩ = +M₀. The ground state is no longer symmetric under spin flip even though the Hamiltonian is. Symmetry is "broken" because the state the system actually occupies does not share the symmetry of the equations that govern it.

The Landau theory you studied makes this quantitative. Near T_c, expand the free energy as F = a(T)M² + bM⁴ + ..., where a(T) changes sign at T_c. Above T_c, a > 0 and the free energy has a single minimum at M = 0 (the **disordered phase**). Below T_c, a < 0 and the shape becomes a **Mexican hat** (or double well in 1D) with minima at ±M₀ = ±√(−a/2b). The system must settle in one of these minima — this selection is the spontaneous symmetry breaking. An infinitesimal symmetry-breaking perturbation (a tiny external field, a fluctuation, a boundary condition) picks which minimum, but the effect persists even after the perturbation is removed.

A crucial consequence is the existence of **Goldstone modes**. Whenever a continuous symmetry (like rotational symmetry of the magnetization direction in a Heisenberg ferromagnet) is spontaneously broken, there appear low-energy, long-wavelength collective excitations — **magnons** in ferromagnets, **phonons** in crystals, **pions** in nuclear physics — that cost zero energy in the long-wavelength limit. These are the "ripples" of the order parameter rotating slowly in space, and they dominate the low-temperature physics of ordered phases. Spontaneous symmetry breaking thus does double duty: it explains *why* ordered phases exist and *what* their low-energy excitation spectrum looks like.
