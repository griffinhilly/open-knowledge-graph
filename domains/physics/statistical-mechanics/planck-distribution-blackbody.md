---
id: planck-distribution-blackbody
title: Planck Distribution and Blackbody Radiation
domain: physics
course: statistical-mechanics
prerequisites:
- id: blackbody-radiation
  type: hard
- id: photon-model
  type: hard
builds-toward:
- photon-gas-thermodynamics
tags:
- blackbody
- photons
- thermal-radiation
stage: advanced
status: draft
---

# Planck Distribution and Blackbody Radiation

## Core Idea
Planck's law describes the spectral energy density of blackbody radiation: u_ν(ν,T) dν = (8πhν^3/c^3) dν / [exp(hν/kT)−1]. Integrating over all frequencies recovers the Stefan-Boltzmann law u(T) ∝ T^4. The Planck distribution arises from counting the partition function of a gas of photons in thermal equilibrium.

## Questions

```yaml
- question: "Classical physics (Rayleigh-Jeans law) treats each electromagnetic mode as having average energy kT. At what part of the spectrum does this prediction break down most catastrophically?"
  type: multiple-choice
  options:
    - "Low frequencies (radio waves), where classical physics predicts too little energy"
    - "High frequencies (ultraviolet and beyond), where classical physics predicts diverging energy"
    - "The visible spectrum only, where quantum corrections are largest"
    - "Classical physics is accurate at all frequencies — only the total integrated energy is wrong"
  answer: 1
  explanation: "The Rayleigh-Jeans law assigns energy kT to every mode regardless of frequency, so the total radiated power diverges as frequency increases — the 'ultraviolet catastrophe.' At low frequencies (kT ≫ hν), Planck's law reduces to the classical result, so classical physics is actually correct there. It's at high frequencies where the quantum suppression exp(−hν/kT) → 0 cuts off the classical prediction, resolving the catastrophe. A common misconception is that the failure is broad or applies equally at all frequencies."

- question: "What happens to the mean energy per mode ⟨E⟩ = hν / [exp(hν/kT) − 1] in the high-temperature limit (kT ≫ hν)?"
  type: multiple-choice
  options:
    - "It approaches zero, because high temperatures excite all modes equally"
    - "It approaches kT, recovering the classical equipartition result"
    - "It approaches hν, because the mode is always singly occupied at high temperature"
    - "It diverges, reproducing the ultraviolet catastrophe"
  answer: 1
  explanation: "When kT ≫ hν, we have exp(hν/kT) ≈ 1 + hν/kT, so exp(hν/kT) − 1 ≈ hν/kT. Therefore ⟨E⟩ ≈ hν / (hν/kT) = kT — exactly the classical equipartition result. This is the correct classical limit: quantum mechanics reduces to classical physics at low frequencies (or high temperatures). The Planck distribution is not a replacement that always gives different results from classical physics; it agrees with classical physics where classical physics is valid."

- question: "Photons in a blackbody cavity have chemical potential μ = 0, unlike most particles in statistical mechanics."
  type: true-false
  answer: true
  explanation: "Photons can be freely created and absorbed by the cavity walls — there is no conservation law fixing their total number. This means there is no free energy cost to changing the photon number, which is precisely what μ = 0 means. Setting μ = 0 in the Bose-Einstein distribution gives ⟨n⟩ = 1/(exp(hν/kT) − 1) — the Planck occupation number. This is a crucial distinction from, say, electrons or atoms, where the chemical potential is determined by particle number conservation."

- question: "Hotter blackbodies emit radiation that peaks at longer wavelengths (lower frequencies) than cooler blackbodies."
  type: true-false
  answer: false
  explanation: "This is backwards. Wien's displacement law states that the peak frequency of the Planck spectrum is proportional to temperature: ν_max ∝ T. Hotter objects peak at higher frequency (shorter wavelength). This is why a piece of iron glows red at lower temperatures (peak in the infrared, with a visible red tail), then orange, then white (all visible wavelengths), then blue-white as it gets hotter. The confusion likely arises from conflating 'higher temperature = more energy at all frequencies' with 'the peak shifts to lower frequency.'"

- question: "Why does the Planck distribution exponentially suppress high-frequency modes, and how does this resolve the ultraviolet catastrophe?"
  type: short-answer
  answer: "At high frequencies, the quantum of energy hν is much larger than kT. To excite such a mode even once requires a thermal fluctuation of magnitude hν ≫ kT, which is exponentially unlikely. The mean occupation number ⟨n⟩ = 1/(exp(hν/kT) − 1) → exp(−hν/kT) → 0 exponentially as ν → ∞. Classical physics assigned kT to every mode regardless of frequency, ignoring the quantization that makes high-frequency excitation costly. Quantization provides a natural cutoff: modes with hν ≫ kT are effectively frozen out, making the total integrated energy density finite."
  explanation: "The key is understanding what quantization does mechanically. In classical physics, a harmonic oscillator can have any energy and always averages kT. In quantum mechanics, the same oscillator can only have energies 0, hν, 2hν, … and the probability of excited states falls exponentially with ν. This exponential damping — not a gentle correction — is what makes the integral over all frequencies finite and equal to σT⁴."
```

## Explainer

From the blackbody radiation problem you know the historical puzzle: classical physics (the Rayleigh-Jeans law) predicts that radiation intensity grows without bound as frequency increases — the **ultraviolet catastrophe** — because it treats each electromagnetic mode as having average energy kT regardless of frequency. Planck resolved this by quantizing the radiation field, and from the photon model you know that light comes in discrete quanta each carrying energy hν. The statistical mechanics of a photon gas is what turns these ingredients into a complete, correct formula.

A photon mode at frequency ν is a quantum harmonic oscillator that can be excited with 0, 1, 2, … photons. The key difference from classical particles: photons are bosons with no conservation law (you can have any number, and photons can be created and absorbed by the walls). The chemical potential μ = 0 for a photon gas. The mean number of photons in a mode at frequency ν is then the **Bose-Einstein distribution** with μ = 0: ⟨n⟩ = 1/(exp(hν/kT) − 1). Multiplying by hν gives the mean energy per mode: ⟨E⟩ = hν / [exp(hν/kT) − 1]. This replaces the classical kT: at high temperatures (kT ≫ hν), ⟨E⟩ → kT recovering the classical limit; at low temperatures (kT ≪ hν), ⟨E⟩ → hν exp(−hν/kT) → 0, exponentially suppressing high-frequency modes.

To get the full spectral density, multiply ⟨E⟩ by the number of modes per unit volume per unit frequency. In a 3D cavity, the mode density is 8πν²/c³ (accounting for two polarizations). This gives Planck's law: u_ν = (8πhν³/c³) / [exp(hν/kT) − 1]. The spectrum has a peak at ν_max ∝ T (**Wien's displacement law** — hotter objects peak at higher frequency, which is why iron glows red then white then blue as it heats). Integrating over all frequencies using the standard integral ∫₀^∞ x³/(eˣ−1)dx = π⁴/15 gives the total energy density u ∝ T⁴ — the **Stefan-Boltzmann law**, which you can now derive from first principles rather than treating as empirical.

The Planck distribution is the prototype for a broader class of results. The same Bose-Einstein factor with μ = 0 governs phonons (quantized lattice vibrations), which gives the Debye model of heat capacities. The factor 1/(exp(βε) − 1) for bosons versus 1/(exp(βε) + 1) for fermions (which you will encounter in the Fermi-Dirac distribution) are the two fundamental quantum statistics, replacing the classical Maxwell-Boltzmann e^{−βε}. Planck's original insight — that energy comes in discrete quanta — thus has consequences far beyond radiation, anchoring the entire framework of quantum statistical mechanics.


