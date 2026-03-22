---
id: rigid-rotor-model
title: The Rigid Rotor Model of Molecular Rotation
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: rotational-kinematics
  type: soft
- id: moment-of-inertia
  type: soft
- id: angular-momentum
  type: soft
builds-toward:
- rotational-spectroscopy
- selection-rules-spectroscopy
tags:
- rotation
- rigid-rotor
- moment-of-inertia
- rotational-energy
stage: advanced
status: validated
---

# The Rigid Rotor Model of Molecular Rotation

## Core Idea
The rigid rotor treats a diatomic molecule as two masses connected by a fixed bond, rotating freely in space. Its quantum energy levels are E_J = ℏ²J(J+1)/(2I), where J = 0, 1, 2, … is the rotational quantum number and I is the moment of inertia. Each level has degeneracy 2J+1 from the magnetic quantum number M_J. The rotational constant B = ℏ/(4πcI) directly connects spectroscopic measurements to molecular bond lengths and masses. Polyatomic molecules require specifying up to three principal moments of inertia (symmetric, spherical, and asymmetric tops).

## How It's Best Learned
Derive the energy levels for a diatomic from first principles, then use them to predict the spacing of lines in a microwave spectrum. Extract bond length from B to solidify the connection between model and measurement.

## Common Misconceptions
- Assuming all rotational levels are equally spaced — they are not; spacing increases as 2B(J+1).
- Forgetting that I depends on reduced mass, not just bond length.

## Questions

```yaml
- question: "A student argues: 'Because the rotational energy levels of a diatomic are not equally spaced, the absorption lines in its microwave spectrum must also be unevenly spaced.' Is this reasoning correct?"
  type: multiple-choice
  options:
    - "Yes — unequal level spacing always produces unequal spectral line spacing"
    - "No — the energy levels are actually equally spaced in the rigid rotor"
    - "No — the energy levels are unequally spaced, but the spectral lines are equally spaced (separated by 2B) because the transition energies form an arithmetic sequence"
    - "Partially — lines are equally spaced only for low values of J"
  answer: 2
  explanation: "The energy levels E_J = BJ(J+1) are not equally spaced — the gap between level J and J+1 is 2B(J+1), which grows with J. However, the microwave selection rule requires ΔJ = +1, so the observed transition frequencies are 2B, 4B, 6B, 8B, … These form a perfectly even progression, each line separated from the next by 2B. The spectral lines ARE equally spaced even though the energy levels are not. This is why measuring the line spacing directly gives you 2B."

- question: "You measure the microwave spectrum of H₂ and D₂ (deuterium). The bond length of D₂ is essentially the same as H₂. How does the rotational constant B of D₂ compare to that of H₂?"
  type: multiple-choice
  options:
    - "B is the same for both, since bond length determines I and the bond length is unchanged"
    - "B is larger for D₂ because heavier atoms rotate faster"
    - "B is smaller for D₂ because the larger reduced mass increases the moment of inertia, which decreases B"
    - "B is larger for D₂ because the heavier nuclei require higher energy to rotate"
  answer: 2
  explanation: "The rotational constant B = ℏ/(4πcI) and the moment of inertia I = μr², where μ is the reduced mass. For D₂, each deuterium atom has roughly twice the mass of hydrogen, so the reduced mass μ ≈ doubles. Since r is unchanged, I doubles. Because B is inversely proportional to I, B roughly halves for D₂. This demonstrates why B depends on reduced mass — not just bond length. A student who only thinks about bond length will incorrectly predict no change."

- question: "The degeneracy of rotational level J is 2J+1, meaning that J = 3 has seven distinct quantum states all at the same energy."
  type: true-false
  answer: true
  explanation: "The magnetic quantum number M_J can take integer values from −J to +J, giving 2J+1 possible values. For J = 3, M_J ∈ {−3, −2, −1, 0, 1, 2, 3}, which is 7 states. In the absence of an external field, all have the same energy. This degeneracy matters for spectroscopy: higher-J levels contain more states, so more molecules can populate them (weighted by the Boltzmann factor), which affects the relative intensities of spectral lines and produces the characteristic intensity envelope seen in real microwave spectra."

- question: "The spacing between adjacent rotational energy levels decreases as the quantum number J increases."
  type: true-false
  answer: false
  explanation: "The energy gap between level J and level J+1 is E_{J+1} − E_J = 2B(J+1), which increases linearly with J. So the higher you go in J, the larger the energy gap between adjacent levels. This is the opposite of, say, a particle in a box or the harmonic oscillator (where levels are equally spaced). The increasing spacing is a direct consequence of the J(J+1) dependence of rotational energies, which itself comes from the quantization of angular momentum."

- question: "A microwave spectrum of CO shows equally spaced absorption lines. Describe the steps you would take to extract the C–O bond length from this spectrum."
  type: short-answer
  answer: "Measure the spacing between adjacent lines; this equals 2B. Divide by 2 to get B in cm⁻¹. Use B = ℏ/(4πcI) to compute I = ℏ/(4πcB). Use I = μr² where μ = m_C m_O/(m_C + m_O) is the reduced mass of the CO molecule. Solve for r = √(I/μ)."
  explanation: "The procedure works because every observable in a microwave spectrum is a direct consequence of the rigid rotor model. The line spacing encodes 2B; B encodes I (the moment of inertia); I encodes the bond geometry through I = μr². The reduced mass uses atomic masses from the periodic table, which are precisely known, so the only remaining unknown is r. This is why microwave spectroscopy is one of the most accurate methods for measuring bond lengths."
```

## Explainer

The rigid rotor model is the quantum-mechanical treatment of molecular rotation, and it connects directly to what you already know about angular momentum and moment of inertia from classical mechanics. Imagine a diatomic molecule like HCl as a dumbbell: two masses (the H and Cl atoms) connected by a rigid bond of fixed length. In classical mechanics, this system can rotate with any angular velocity and any kinetic energy. But quantum mechanics imposes a constraint you've seen before — just as the particle in a box can only have discrete energy levels, a rotating molecule can only spin at specific quantized energies.

The allowed rotational energy levels are E_J = ℏ²J(J+1)/(2I), where J is the **rotational quantum number** (J = 0, 1, 2, …) and I is the **moment of inertia**, equal to μr² for a diatomic (μ is the reduced mass, r is the bond length). Notice the energy depends on J(J+1), not J² — this means the spacing between adjacent levels is not constant. The gap between J and J+1 is proportional to 2B(J+1), where B = ℏ/(4πcI) is the **rotational constant** expressed in wavenumber units (cm⁻¹). So the higher you go in J, the larger the gaps between successive levels. This non-uniform spacing is the fingerprint of the rigid rotor and shows up directly in microwave spectra as a series of evenly spaced absorption lines (each separated by 2B), because the selection rule requires ΔJ = ±1.

Each energy level J has a **degeneracy** of 2J+1, arising from the magnetic quantum number M_J, which ranges from −J to +J. Physically, this means a molecule in state J = 2 can rotate with five different orientations of its angular momentum vector in space, all at the same energy (in the absence of an external field). This degeneracy matters enormously for spectroscopy: higher-J levels have more states, so more molecules can populate them, which affects the relative intensities of spectral lines.

The remarkable practical payoff of the rigid rotor model is that measuring a microwave spectrum directly gives you the bond length of a molecule. If you observe spectral lines spaced by 2B, you extract B, then compute I = ℏ/(4πcB), and finally solve for r = √(I/μ). For example, the rotational spectrum of ¹²C¹⁶O shows lines spaced by about 3.84 cm⁻¹, giving B ≈ 1.92 cm⁻¹ and a bond length of 1.128 Å — matching high-precision measurements. For polyatomic molecules, the model extends to **symmetric tops** (two equal moments of inertia, like NH₃), **spherical tops** (all three equal, like CH₄), and **asymmetric tops** (all three different, like H₂O), each with increasingly complex energy-level patterns but built on the same foundational physics.
