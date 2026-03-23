---
id: beta-decay-energy-conservation
title: Beta Decay and Energy Conservation in Weak Interactions
domain: physics
course: modern-physics
prerequisites:
- id: radioactive-decay
  type: hard
- id: mass-energy-equivalence
  type: soft
tags:
- beta-decay
- radioactive-decay
- weak-interaction
stage: advanced
status: validated
---

# Beta Decay and Energy Conservation in Weak Interactions

## Core Idea
Beta decay is the transformation of a neutron into a proton (or vice versa) via the weak nuclear force, accompanied by emission of an electron (or positron) and an antineutrino (or neutrino). The Q-value (energy available) is shared among the products in a continuous spectrum, with the antineutrino carrying away a variable amount. This was historically puzzling until the neutrino was hypothesized to explain the missing energy.

## How It's Best Learned
Identify the Q-value from initial and final nuclear masses. Understand that the continuous energy spectrum of electrons arises from variable antineutrino carries-off. Distinguish between beta-minus (n → p), beta-plus (p → n), and electron capture decay modes.

## Common Misconceptions
Not all the Q-value goes to the electron (it shares energy with the neutrino, producing the continuous spectrum). Electron capture does not emit an electron; rather, the nucleus absorbs an inner-shell electron and emits a neutrino. The weak force acts on flavor-changing quark transitions, a concept beyond classical nuclear models.

## Questions

```yaml
- question: "Alpha particles emitted from a given isotope always have a single discrete energy, but beta particles from the same decay mode have a continuous range of energies. What is the fundamental reason for this difference?"
  type: multiple-choice
  options:
    - "Alpha particles are heavier and therefore lose energy more predictably as they travel through matter"
    - "Beta decay involves a three-body final state (daughter nucleus, electron, and antineutrino), so the Q-value is shared among three particles in variable proportions"
    - "Beta decay is governed by the weak force, which operates over a broader energy range than the strong force behind alpha decay"
    - "The electron's small mass allows it to receive varying fractions of the Q-value due to quantum uncertainty"
  answer: 1
  explanation: "The number of final-state particles determines whether the energy spectrum is discrete or continuous. Alpha decay has two final-state particles (alpha particle + daughter nucleus): conservation of energy and momentum uniquely fixes each particle's energy for a given Q-value, producing a discrete line. Beta decay has three final-state particles: the Q-value is shared between the electron and the antineutrino in continuously variable proportions, with the daughter nucleus taking a small recoil. This three-body kinematics produces a continuous spectrum. The weak force (option C) and quantum uncertainty (option D) are not the reason — it is strictly the counting of final-state particles."

- question: "A nucleus undergoes beta-plus decay (p → n + e⁺ + νe). What minimum Q-value is required for this decay to proceed?"
  type: multiple-choice
  options:
    - "Q > 0 — any positive Q-value is sufficient, just as in beta-minus decay"
    - "Q > mec² ≈ 0.511 MeV — one positron mass must be created"
    - "Q > 2mec² ≈ 1.022 MeV — a positron and electron are created as a pair"
    - "Q > mpc² — a proton mass must be converted to a neutron mass"
  answer: 2
  explanation: "Beta-plus decay creates a positron from rest mass-energy. Since the positron is an antiparticle not present in the initial nucleus, its rest mass (mec² ≈ 0.511 MeV) must come from the Q-value. Unlike beta-minus decay (where the electron was already present in the atomic electron cloud and not created from nuclear mass), beta-plus decay requires creating new mass. The minimum Q-value is 2mec² ≈ 1.022 MeV — the factor of 2 arises when working with atomic (rather than nuclear) masses, as the atomic mass accounting effectively requires paying for two electron masses. When Q < 1.022 MeV, electron capture (the competing process) occurs instead."

- question: "In beta-minus decay, the maximum kinetic energy of the emitted electron is approximately equal to the Q-value of the decay."
  type: true-false
  answer: true
  explanation: "True. The electron achieves maximum kinetic energy when the antineutrino carries away near-zero energy (and the daughter nucleus takes a small but negligible recoil). In the limit of a nearly massless neutrino carrying zero energy, essentially all the Q-value goes to the electron. This maximum electron energy — called the endpoint energy — is what is measured in beta spectroscopy and was the key experimental observable that revealed the continuous spectrum and the 'missing' energy in the first place. Pauli's neutrino hypothesis explained why most decays produce electrons with less than the maximum energy."

- question: "In electron capture decay, the nucleus emits an inner-shell electron, which can be detected by particle detectors."
  type: true-false
  answer: false
  explanation: "False. In electron capture, the nucleus *absorbs* an inner-shell atomic electron (p + e⁻ → n + νe) and emits a neutrino — no electron is emitted from the nucleus. The name describes what happens to the electron (it is captured), not that an electron is produced. After the inner-shell electron is absorbed, a higher-shell electron drops to fill the vacancy, emitting a characteristic X-ray — which *is* detectable, but is not an electron. This is a common source of confusion between electron capture and beta-minus decay."

- question: "Why did the continuous energy spectrum of beta decay electrons appear to threaten the law of conservation of energy, and how did Pauli's neutrino hypothesis resolve the apparent violation?"
  type: short-answer
  answer: "In a two-body decay (like alpha decay), the Q-value uniquely fixes the energy of each product via conservation of energy and momentum, producing a discrete spectral line. In beta decay, physicists initially assumed a two-body decay (electron + daughter nucleus). The observed continuous spectrum meant that different electrons emerged with different energies, with the 'missing' energy varying decay by decay — a seemingly random violation of conservation of energy. Pauli hypothesized a third particle (the neutrino) that is emitted simultaneously with the electron, with the Q-value split between them. The electron's energy is continuous because the neutrino's energy varies decay by decay, but in every single decay the total energy (electron + neutrino + nuclear recoil) equals the Q-value. Conservation of energy is preserved in every individual event; the neutrino's energy is just undetected."
  explanation: "Pauli's proposal was bold because the neutrino had never been observed and seemed to violate the spirit of Occam's razor. But the alternative — abandoning conservation of energy — was unacceptable to most physicists (though Niels Bohr temporarily proposed it). Fermi's 1934 theory quantitatively predicted the shape of the beta spectrum; the neutrino was directly detected by Cowan and Reines in 1956, confirming Pauli's hypothesis."
```

## Explainer

From your study of radioactive decay, you know that unstable nuclei release energy by transforming into more stable configurations. In alpha and gamma decay, the energy available — the **Q-value** — goes into kinetic energy of the products in a well-defined way: because only two bodies emerge (the alpha particle and the daughter nucleus, or the gamma photon and the recoiling nucleus), conservation of energy and momentum dictate a unique energy for each product. Alpha particles from a given isotope are emitted with a single discrete energy. This discreteness was considered a universal feature of radioactive decay — until beta decay experiments revealed something deeply puzzling.

When physicists measured the energy of electrons emitted in beta-minus decay (n → p + e⁻ + ν̄_e), they found not a discrete line but a **continuous spectrum**: electrons emerged with energies ranging from near zero up to a maximum Q-value. The Q-value is calculated from the mass difference between the initial and final nuclei using mass-energy equivalence: Q = (M_parent − M_daughter − m_e)c². If only the electron and the daughter nucleus were produced, energy conservation would demand a unique electron energy just as in alpha decay. The continuous spectrum seemed to imply that energy was not conserved — a crisis serious enough that Niels Bohr temporarily proposed abandoning conservation of energy in nuclear processes.

In 1930, Wolfgang Pauli proposed a bold resolution: a third particle — he called it the **neutrino** (small neutral one) — is produced alongside the electron, and the two share the Q-value between them in continuously variable proportions. Because the neutrino is nearly massless and interacts extremely weakly with matter (so weakly it escaped detection in Pauli's time), it carries away the "missing" energy unobserved. The electron spectrum has a continuous shape precisely because the energy split between electron and neutrino is probabilistic, with the maximum electron energy corresponding to a neutrino carrying away near-zero energy. Fermi formalized this into a quantitative theory in 1934; the neutrino was not directly detected until 1956.

The three modes of beta decay differ in which particle is emitted and the underlying nuclear transformation. **Beta-minus** decay (the common form) converts a neutron to a proton and emits an electron and an electron antineutrino: n → p + e⁻ + ν̄_e. **Beta-plus** decay converts a proton to a neutron and emits a positron and an electron neutrino: p → n + e⁺ + ν_e; this can only occur when the Q-value exceeds 2m_ec² (≈ 1.02 MeV) because the positron mass must be created. **Electron capture** is a competing process to beta-plus: the nucleus absorbs an inner-shell electron and emits a neutrino (p + e⁻ → n + ν_e), without producing a positron. In all three modes, a neutrino or antineutrino carries away a portion of the Q-value, producing the characteristic continuous spectrum — a clean experimental signature of the three-body final state that vindicated Pauli's hypothesis.
