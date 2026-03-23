---
id: beta-emission-weak-force
title: Beta Decay and the Weak Nuclear Force
domain: physics
course: modern-physics
prerequisites:
- id: spontaneous-radioactive-decay
  type: hard
- id: nuclear-structure
  type: soft
builds-toward:
- gamma-emission-nuclear-transitions
tags:
- nuclear-physics
- decay
stage: advanced
status: validated
---

# Beta Decay and the Weak Nuclear Force

## Core Idea
Beta-minus decay (n → p + e⁻ + ν̄_e) transforms a neutron into a proton, emitting an electron and antineutrino; beta-plus decay (p → n + e⁺ + ν_e) transforms a proton. These weak interactions change N and Z, moving nuclei toward stability. Neutrinos carry away variable energy, explaining the continuous beta spectrum. Beta decay is the most common decay mode for neutron-rich nuclei, powered by the weak nuclear force—distinct from strong and electromagnetic forces.

## Questions

```yaml
- question: "Alpha decay produces particles with discrete, fixed kinetic energies. Beta decay produces electrons with a continuous range of energies up to a maximum. What is the correct explanation for this difference?"
  type: multiple-choice
  options:
    - "Electrons have mass while alpha particles are massless, so electrons can carry variable energy"
    - "Beta decay is a three-body final state — the electron and antineutrino share the available energy variably, so neither has a fixed energy"
    - "The weak force is inherently random in the energy it releases, unlike the strong force that drives alpha decay"
    - "Beta particles lose variable energy to electromagnetic interactions as they exit the nucleus"
  answer: 1
  explanation: "This is the historical key insight that led Pauli to postulate the neutrino in 1930. Alpha decay is a two-body decay: nucleus → daughter + alpha particle. Two-body kinematics with conserved energy and momentum requires the alpha to have a single fixed energy. If beta decay were simply n → p + e⁻, the electron would also have a fixed energy. But experiments showed a continuous spectrum — electrons with all energies from zero to a maximum. The only resolution consistent with energy and momentum conservation is a third particle (the antineutrino) that carries away variable energy, making beta decay three-body."

- question: "A nucleus has too many neutrons relative to protons and lies above the valley of stability on the binding energy landscape. Which decay mode would most directly move it toward stability?"
  type: multiple-choice
  options:
    - "Alpha decay — it reduces both N and Z, lowering the neutron excess"
    - "Beta-plus decay — converting a proton to a neutron would further increase the neutron count"
    - "Beta-minus decay — converting a neutron to a proton reduces the neutron excess while leaving A unchanged"
    - "Electron capture — it removes an electron from the atom, reducing the neutron count"
  answer: 2
  explanation: "Beta-minus decay converts a neutron to a proton (n → p + e⁻ + ν̄_e), reducing N by 1 and increasing Z by 1 while leaving the mass number A = N + Z unchanged. For a neutron-rich nucleus, this is exactly the transformation needed: it moves the nucleus toward the valley of stability by improving its N/Z ratio. Beta-plus decay does the opposite (p → n + e⁺ + ν_e), which would worsen the neutron excess. Electron capture also converts p → n, also worsening it. Alpha decay reduces both N and Z by 2, which might not improve N/Z efficiently."

- question: "Beta decay changes the mass number A of a nucleus, while alpha decay does not."
  type: true-false
  answer: false
  explanation: "This is precisely backwards. Alpha decay reduces A by 4 (losing two protons and two neutrons as a helium-4 nucleus). Beta decay does NOT change A — it converts a neutron into a proton (or vice versa), leaving the total nucleon count A = N + Z unchanged. Only Z changes (by ±1), which is why beta decay changes the element while leaving the isotope in the same mass region. This is the defining feature of beta decay: it adjusts the proton-neutron ratio without adding or removing nucleons."

- question: "The existence of the neutrino was inferred from the continuous energy spectrum of beta decay electrons, because energy conservation requires that the 'missing' energy be carried away by an invisible particle."
  type: true-false
  answer: true
  explanation: "Pauli's 1930 proposal was driven by energy and momentum accounting. If beta decay were two-body (n → p + e⁻), energy conservation would require the electron to have a single fixed kinetic energy, just as alpha particles do. Instead, electrons appeared with all energies from nearly zero to a maximum (Q-value), with the average around one-third of the maximum. The missing energy and momentum in each event had to go somewhere. Pauli proposed a very light, electrically neutral particle — the neutrino — that was undetectable but real. The neutrino was not directly detected until 1956 (Cowan-Reines experiment), but its existence was accepted long before on this indirect thermodynamic argument."

- question: "Why did the continuous energy spectrum of beta decay electrons lead physicists to postulate the neutrino? What would the spectrum look like if the neutrino did not exist?"
  type: short-answer
  answer: "If beta decay were a two-body process (n → p + e⁻), energy and momentum conservation in the rest frame of the decaying neutron would require the electron and proton to emerge with fixed, definite momenta — exactly as in alpha decay, which produces a sharp energy peak. Instead, experiments showed a broad, continuous distribution of electron energies up to a maximum. In any given decay, the electron could have anywhere from nearly zero to the full Q-value of kinetic energy. The 'missing' energy in each event had to go somewhere without being detected. Pauli proposed that a third particle — very light and electrically neutral — was emitted simultaneously, sharing the available energy variably with the electron. This three-body final state explains the continuous spectrum: in each decay, the electron and antineutrino share the energy in varying proportions, so neither has a fixed energy."
  explanation: "The neutrino postulate was driven entirely by conservation laws. Energy was apparently not conserved in two-body beta decay, which was deeply troubling. Rather than abandon conservation of energy (which Bohr seriously considered), Pauli proposed an undetectable particle as the carrier of the missing energy. This is a model example of inferring a new particle from indirect thermodynamic evidence before any direct detection."
```

## Explainer

From your study of spontaneous radioactive decay, you know that unstable nuclei shed energy to reach more stable configurations. Alpha decay changes A by 4 and Z by 2. But many nuclei have the wrong proton-to-neutron ratio to be stable without changing the identity of their nucleons — they need to convert a neutron to a proton or vice versa. This is the role of **beta decay**: it adjusts Z (and therefore the chemical element) while leaving the mass number A unchanged, allowing the nucleus to move toward the valley of stability on the nuclear binding energy landscape.

In **beta-minus decay**, a neutron inside the nucleus converts to a proton: n → p + e⁻ + ν̄_e. The nucleus gains a proton, loses a neutron, and emits an electron (the "beta particle") and an antineutrino. This is the dominant decay mode for neutron-rich nuclei — those that lie above the valley of stability. In **beta-plus decay**, a proton converts to a neutron: p → n + e⁺ + ν_e, emitting a positron and a neutrino. This is favored by proton-rich nuclei. A closely related process is **electron capture**, where the nucleus captures an inner-shell electron and converts a proton to a neutron — same outcome as beta-plus but no positron emitted. All three processes are mediated by the **weak nuclear force**.

The existence of the neutrino was originally inferred from the **continuous beta spectrum** — the observation that emitted electrons have a range of kinetic energies up to a maximum, rather than the sharp, fixed energy expected from a two-body decay. Pauli proposed in 1930 that a third, invisible particle must carry away variable amounts of energy and momentum, explaining why the electron energy is not fixed. Fermi later named it the neutrino. If beta decay were simply n → p + e⁻, energy and momentum conservation would require a fixed electron energy — like alpha decay, which shows a sharp energy peak. The continuous spectrum is a direct signature of the three-body final state.

The weak force differs from the strong and electromagnetic forces in several fundamental ways. It is extremely short-ranged (mediated by the massive W and Z bosons, with range ~10⁻¹⁸ m), violates parity symmetry (neutrinos are always left-handed), and can change quark flavor — a proton's up quark converts to a down quark in beta-minus decay (u → d + W⁺, then W⁺ → e⁺ + ν). Beta decay is responsible for the stability of most ordinary matter: free neutrons decay in about 15 minutes via beta-minus decay, but neutrons bound in stable nuclei are stabilized by the strong force. The slow timescales of beta decay compared to nuclear reactions reflect the weakness of the force — hence the name.
