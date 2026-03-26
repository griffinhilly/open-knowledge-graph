---
id: magnetic-dipole-radiation
title: Magnetic Dipole and Quadrupole Radiation
domain: physics
course: electrodynamics
prerequisites:
- id: electric-dipole-radiation
  type: hard
- id: multipole-expansion-radiation
  type: soft
tags:
- radiation
- multipole
- magnetic
stage: expert
status: validated
---

# Magnetic Dipole and Quadrupole Radiation

## Core Idea
When electric dipole moment vanishes, magnetic dipole moment m and electric quadrupole moment Q contribute to radiation. These higher multipoles are suppressed by factors of (a/c)² relative to dipole radiation. Important in nuclear and atomic transitions where dipole selection rules forbid dipole transitions.

## Questions

```yaml
- question: "In a dense laboratory gas, an atomic transition forbidden by electric dipole selection rules is never observed. In an interstellar nebula, the same transition produces bright emission lines. What explains this difference?"
  type: multiple-choice
  options:
    - "The photon emission rate depends on gas density; higher density in a lab increases collisional quenching before emission can occur"
    - "The extremely low collision rate in the nebula gives excited atoms time to radiate via the slow M1 or E2 channel before collisional deexcitation occurs"
    - "The forbidden transition becomes electric dipole allowed at the low pressures found in interstellar space"
    - "The nebula's magnetic field mixes quantum states, activating transitions that are otherwise dormant"
  answer: 1
  explanation: "The key is that 'forbidden' transitions have very long lifetimes — milliseconds to seconds, compared to nanoseconds for electric dipole transitions. In a dense laboratory gas, atoms undergo collisions far more frequently than their M1/E2 emission rate, so they lose their excitation energy through collisions before they can radiate. In an interstellar nebula, the density is so low (often < 1000 atoms/cm³) that the time between collisions exceeds the millisecond-scale lifetime of the forbidden transition. The atom finally has time to emit. This is why nebulae are laboratories for quantum physics impossible to replicate on Earth."

- question: "Why is magnetic dipole radiation suppressed relative to electric dipole radiation by a factor of approximately (v/c)²?"
  type: multiple-choice
  options:
    - "Magnetic fields are inherently weaker than electric fields for any given frequency, reducing radiated power"
    - "Producing an oscillating magnetic dipole moment requires oscillating currents — charges moving at speed v ≪ c — while electric dipole radiation involves static charge separation"
    - "The magnetic dipole angular distribution has a different shape that integrates to less total power"
    - "The magnetic dipole moment is defined relative to the speed of light in the medium, introducing the factor"
  answer: 1
  explanation: "An oscillating magnetic dipole is a current loop whose current or area oscillates. Creating a changing magnetic moment requires moving charges, which necessarily move at some velocity v ≪ c. The suppression factor (v/c)² reflects this: the radiation from the current loop is weaker than from an electric dipole by this velocity ratio. Equivalently, if the source has size a and wavelength λ = c/f, the suppression is (a/λ)². This is why electric dipole dominates whenever it is allowed: it is intrinsically stronger by two powers of the small ratio a/λ."

- question: "An atomic transition labeled 'forbidden' by electric dipole selection rules can still occur via magnetic dipole (M1) or electric quadrupole (E2) radiation, but at a rate suppressed by roughly α² ≈ 1/18,769 relative to an allowed E1 transition."
  type: true-false
  answer: true
  explanation: "Correct. 'Forbidden' in spectroscopy means forbidden by the electric dipole selection rules, not absolutely forbidden. M1 and E2 transitions still occur, but their rates are suppressed by (a₀/λ)² ~ α² where α ≈ 1/137 is the fine structure constant, giving suppression of about (1/137)² ≈ 5 × 10⁻⁵. Lifetimes of E1 transitions are typically ~10 ns; forbidden transitions can have lifetimes of milliseconds, seconds, or even longer. These slow transitions are critical in astrophysics (nebular forbidden lines), quantum computing (long-lived qubit states), and metrology."

- question: "Magnetic dipole (M1) and electric quadrupole (E2) radiation have the same angular distribution as electric dipole (E1) radiation, differing mainly in their total radiated power."
  type: true-false
  answer: false
  explanation: "M1 radiation has the same angular distribution as E1 (∝ sin²θ, the donut pattern), but E2 radiation has a different angular distribution — for the simplest case ∝ sin²θ cos²θ, with more lobes and different nodal surfaces. M1 and E1 also differ in the polarization pattern: for M1, it is the magnetic field that traces the donut pattern, while the electric field orientation is swapped relative to E1. These differences in angular distribution and polarization mean M1 and E2 emissions have observably different intensity patterns on the sky and are distinguishable in astronomical observations."

- question: "Why are 'forbidden' spectral lines observable in nebulae but not in dense laboratory gases? What does this reveal about the meaning of 'forbidden' in atomic spectroscopy?"
  type: short-answer
  answer: "Forbidden transitions have rates suppressed by (v/c)² ~ α² relative to electric dipole transitions, giving lifetimes of milliseconds to seconds instead of nanoseconds. In a dense laboratory gas, atoms collide far more frequently than once per millisecond, so excited atoms lose energy through collisions before they can emit via the slow forbidden channel. In the near-vacuum of a nebula (densities <1000 atoms/cm³), collision times are much longer than the forbidden lifetime, so atoms finally have time to emit. 'Forbidden' means forbidden by the electric dipole selection rules — not physically impossible. The radiation is merely very slow."
  explanation: "This reveals that spectroscopic 'selection rules' are approximations valid in the electric dipole limit, not absolute prohibitions. The true selection rule is only that transitions must conserve energy, momentum, and angular momentum. Electric dipole, magnetic dipole, quadrupole, and higher multipole channels are all available; they differ only in rate. 'Forbidden lines' are simply transitions where E1 is blocked by symmetry and the allowed rate is the much smaller M1 or E2 rate. The astronomer's sky reveals quantum transitions invisible in the terrestrial laboratory precisely because of this rate difference."
```

## Explainer

From electric dipole radiation, you know the dominant term in the multipole expansion: an oscillating electric dipole moment p̈ drives radiation with power P ∝ |p̈|² and a sin²θ angular distribution (the classic donut pattern). But what happens when the electric dipole moment is zero? A charge distribution with this symmetry — for example, two equal positive charges oscillating symmetrically about the origin — still radiates. You must go to the next terms in the expansion.

The **magnetic dipole** contribution comes from an oscillating magnetic dipole moment m — a current loop whose area or current oscillates in time. The radiation fields have the same angular dependence as electric dipole radiation (∝ sin²θ), but the roles of E and B are swapped: it is the magnetic field that has the donut pattern, while the electric field is perpendicular to both the observation direction and m̈. The radiated power is P_M1 ∝ |m̈|²/c². Compared to the electric dipole, there is an extra factor of (v/c)² ∼ (a/λ)² — the suppression comes from the fact that creating oscillating magnetic moments requires oscillating currents, which themselves involve charges moving at speed v ≪ c.

The **electric quadrupole** moment Q involves the second moments of the charge distribution. Physically, it captures how elongated or flattened the charge distribution is along various axes. An oscillating quadrupole (like two opposite dipoles canceling each other) radiates with a different angular pattern (∝ sin²θ cos²θ for the simplest case) and the same (v/c)² suppression relative to electric dipole. Both M1 and E2 radiation are weaker than E1 by the same order of magnitude, but they are not identical — they have different angular distributions and different selection rules governing which quantum states can transition via each mechanism.

This hierarchy — E1 dominant, then M1 and E2, then M2 and E3, etc. — is essential in spectroscopy. In atomic transitions, quantum mechanical **selection rules** forbid the electric dipole transition between certain pairs of states (when Δl ≠ ±1 or ΔS ≠ 0 in the non-relativistic limit). These "forbidden" transitions still occur, but at rates suppressed by (a₀/λ)² ∼ (α)², where α ≈ 1/137 is the fine structure constant. The result is metastable excited states with lifetimes of milliseconds or longer instead of nanoseconds. Astronomers observe such transitions in nebulae (e.g., the green forbidden lines of [O III]) under the ultra-low-collision conditions of interstellar space, where atoms have time to radiate via the slow quadrupole channel.
