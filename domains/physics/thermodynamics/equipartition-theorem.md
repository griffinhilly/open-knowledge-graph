---
id: equipartition-theorem
title: The Equipartition Theorem
domain: physics
course: thermodynamics
prerequisites:
- id: rms-speed-and-kinetic-energy
  type: hard
builds-toward:
- heat-capacity-of-gases
- adiabatic-processes
tags:
- equipartition
- degrees-of-freedom
- internal-energy
- heat-capacity
stage: formal-systems
status: validated
---

# The Equipartition Theorem

## Core Idea
The equipartition theorem states that each quadratic degree of freedom (each independent way a molecule can store energy) contributes (1/2)kT to the average energy per molecule. Monatomic gases have 3 translational degrees, so U = (3/2)NkT. Diatomic molecules add 2 rotational degrees at room temperature (U = (5/2)NkT) and 2 vibrational degrees at high temperatures. This explains why different gases have different heat capacities and why heat capacity can change with temperature.

## How It's Best Learned
Physically interpret each degree of freedom: three independent directions of translation, two rotation axes for a dumbbell-shaped diatomic molecule. Predict Cv for monatomic, diatomic, and triatomic gases and compare to experimental values.

## Common Misconceptions
- Vibrational modes are not always active — at room temperature, quantum effects 'freeze out' vibrational degrees in diatomic gases; classical equipartition overestimates Cv in that regime.
- The theorem is statistical and holds only on average over many molecules.

## Questions

```yaml
- question: "A diatomic gas is heated to a high enough temperature that vibrational modes are fully active. What is the molar heat capacity at constant volume C_v?"
  type: multiple-choice
  options:
    - "(5/2)R — 3 translational + 2 rotational degrees"
    - "(3/2)R — only translational motion contributes"
    - "(7/2)R — 3 translational + 2 rotational + 2 vibrational quadratic terms"
    - "(6/2)R — 3 translational + 2 rotational + 1 vibrational degree"
  answer: 2
  explanation: "At high temperature, a diatomic molecule has 3 translational degrees (x, y, z motion), 2 rotational degrees (two perpendicular axes), and 2 vibrational quadratic terms (1 kinetic + 1 potential, since both ½mv² and ½kx² are quadratic). That's 7 total quadratic terms, each contributing (1/2)kT, giving U = (7/2)kT per molecule and C_v = (7/2)R. The common mistake is counting 6 — vibrational modes always contribute two quadratic terms (kinetic and potential), not one."

- question: "Nitrogen gas (N₂) at room temperature has a measured C_v of approximately (5/2)R, not (7/2)R. What explains this?"
  type: multiple-choice
  options:
    - "N₂ molecules lack vibrational modes entirely due to their bond structure"
    - "Rotational modes are also frozen out at room temperature for N₂"
    - "Vibrational modes are 'frozen out' because the quantum energy level spacing ħω >> kT at room temperature, so those modes cannot absorb thermal energy"
    - "The equipartition theorem does not apply to diatomic molecules"
  answer: 2
  explanation: "Quantum mechanics discretizes the energy levels of each mode. Vibrational modes in N₂ have large energy spacing ħω. At room temperature, kT is much smaller than this spacing, so molecules cannot climb to the first vibrational excited state — the mode stays frozen in its ground state and contributes nothing to heat capacity. Rotational modes in N₂ have much smaller energy spacing and are fully active at room temperature, giving the observed (5/2)R."

- question: "A harmonic oscillator has both kinetic energy ½mv² and potential energy ½kx². By the equipartition theorem, the total average thermal energy of this oscillator is (1/2)kT."
  type: true-false
  answer: false
  explanation: "Each quadratic term independently contributes (1/2)kT. The kinetic energy ½mv² is one quadratic term contributing (1/2)kT, and the potential energy ½kx² is a second quadratic term also contributing (1/2)kT. The total average energy is therefore kT, not (1/2)kT. This is why vibrational modes contribute twice as much to heat capacity as translational or rotational modes — they have two quadratic terms, not one."

- question: "The equipartition theorem gives reliable predictions for heat capacities of most real gases at any temperature."
  type: true-false
  answer: false
  explanation: "The equipartition theorem is a classical result assuming all modes can absorb energy continuously. Quantum mechanics restricts modes to discrete energy levels — if kT is much smaller than the level spacing ħω, the mode is frozen and contributes nothing. This quantum freezing makes classical equipartition an overestimate at low temperatures or for modes with large energy spacing (like vibrations in light diatomic molecules). The theorem gives good predictions only when kT >> ħω for the relevant mode."

- question: "Why does a vibrational degree of freedom contribute kT (not (1/2)kT) to average molecular energy, while a translational degree of freedom contributes only (1/2)kT?"
  type: short-answer
  answer: "The equipartition theorem assigns (1/2)kT to each quadratic term in the energy expression. Translational motion in one direction has a single quadratic term — ½mv² — so it contributes (1/2)kT. A vibrational mode has two quadratic terms: kinetic energy ½mv² and potential energy ½kx². Each independently gets (1/2)kT, summing to kT for the complete vibrational mode."
  explanation: "This is why counting 'degrees of freedom' requires care — a vibrational mode counts as two contributions to energy, not one. Mistakenly treating vibration as one degree of freedom predicts C_v = (6/2)R for a fully activated diatomic, when the correct answer is (7/2)R."
```

## Explainer

From your study of the kinetic theory of gases — specifically rms speed and kinetic energy — you know that the average translational kinetic energy of a molecule in thermal equilibrium is (3/2)kT. This result came from computing ⟨½mv²⟩ = ½m⟨v_x² + v_y² + v_z²⟩ and using the Maxwell-Boltzmann distribution. The equipartition theorem generalizes this: the factor of (3/2) comes from having three independent translational directions, and each one contributes exactly (1/2)kT. The theorem says this is not a coincidence — it is a universal rule that applies to any quadratic term in the energy, regardless of whether it is kinetic or potential.

The precise statement is: for any degree of freedom that appears **quadratically** in the total energy — of the form ½ax² for any constant a and generalized coordinate x — the thermal average of that term is exactly (1/2)kT, independent of a. "Quadratic" is the key word. A spring has potential energy ½kx² and kinetic energy ½mv²: both are quadratic, so each contributes (1/2)kT to the average energy. A vibrational mode thus contributes (1/2)kT from kinetic energy plus (1/2)kT from potential energy = kT total, compared to (1/2)kT per direction of pure translation. This is why heat capacities differ so dramatically by molecular type.

Applying the theorem: a **monatomic** gas molecule (e.g., argon) has only three translational degrees of freedom, so its internal energy per molecule is U = 3 × (½kT) = (3/2)kT, and its molar heat capacity at constant volume is C_v = (3/2)R. A **diatomic** molecule (e.g., N₂) at room temperature adds two rotational degrees (rotation about the two axes perpendicular to the bond axis — rotation about the bond axis has negligible moment of inertia and does not contribute), giving U = (5/2)kT and C_v = (5/2)R. At high temperatures, the two vibrational modes (one kinetic, one potential) activate, pushing C_v toward (7/2)R. These predictions match experiment beautifully in the appropriate temperature ranges.

The important caveat is **quantum freezing**. The equipartition theorem is a classical result. Quantum mechanics imposes discrete energy levels on each mode, with level spacing ΔE = ħω for vibrations and ΔE ∝ ħ²/I for rotations. If the thermal energy kT is much smaller than ΔE, the mode cannot absorb thermal energy in the small increments that equipartition assumes — it stays in its ground state and contributes essentially zero to the heat capacity. This is why vibrational modes in H₂ are frozen out at room temperature (their ħω is large), while rotational modes in N₂ are not (their ħ²/I is much smaller). The failure of classical equipartition at low temperatures was one of the early clues that classical mechanics was incomplete, and its resolution by quantum statistics was a triumph of early quantum theory.
