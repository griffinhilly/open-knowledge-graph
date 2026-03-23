---
id: rotational-quantum-numbers-energy
title: Rotational Quantum Numbers and Energy Levels
domain: chemistry
course: physical-chemistry
prerequisites:
- id: rigid-rotor-model
  type: hard
- id: rotational-spectroscopy
  type: hard
builds-toward:
- vibrational-energy-levels-selection-rules
tags:
- rotational-spectroscopy
- quantum-numbers
- energy-levels
stage: advanced
status: validated
---

# Rotational Quantum Numbers and Energy Levels

## Core Idea
Rotational energy levels scale as E_J = BJ(J+1) where J is the angular momentum quantum number and B is the rotational constant proportional to 1/I (moment of inertia). Rotational transitions follow ΔJ = ±1 selection rule. Microwave spectroscopy directly measures closely-spaced rotational levels and yields precise bond lengths via moment of inertia.

## Questions

```yaml
- question: "A student argues that because rotational energy levels in a diatomic molecule are unevenly spaced, the absorption lines in a microwave spectrum should also be unevenly spaced. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — lines are unevenly spaced because the levels are unevenly spaced"
    - "Although levels are unevenly spaced, the ΔJ = ±1 selection rule produces transitions at 2B, 4B, 6B, ... which are separated by a constant 2B — so lines are evenly spaced"
    - "Rotational energy levels are actually evenly spaced, so the student's premise is wrong"
    - "Microwave spectra do not consist of discrete lines, so spacing is irrelevant"
  answer: 1
  explanation: "The energy levels E_J = BJ(J+1) are indeed unevenly spaced — the gap between J and J+1 is 2B(J+1), which grows with J. But each transition J → J+1 appears at frequency 2B(J+1), giving lines at 2B, 4B, 6B, 8B, ... These are separated from each other by exactly 2B. So the spectral lines are evenly spaced even though the underlying energy levels are not. This uniform 2B spacing is the experimental signature of a rigid rotor and is exactly what allows B to be extracted from the spectrum."

- question: "Two isotopes, H³⁵Cl and H³⁷Cl, both appear in a microwave rotational spectrum. Which will have the larger rotational constant B, and what does this imply about their spectral line spacing?"
  type: multiple-choice
  options:
    - "H³⁷Cl has larger B because the heavier chlorine isotope makes the molecule more rigid"
    - "Both isotopes have the same B because the bond length does not change with isotope substitution"
    - "H³⁵Cl has larger B because its smaller reduced mass gives a smaller moment of inertia, making B = ℏ²/2I larger"
    - "H³⁵Cl has larger B because heavier isotopes always have lower rotational constants"
  answer: 2
  explanation: "B = ℏ²/(2I) and I = μr², where μ is the reduced mass. H³⁵Cl has a slightly smaller reduced mass than H³⁷Cl (because ³⁵Cl is lighter), so its moment of inertia is smaller and B is larger. Larger B means more widely spaced spectral lines. This is why isotope substitution shifts rotational line positions — a useful analytical technique. The bond length r is essentially unchanged between isotopologues, so the difference in B traces directly to the reduced mass."

- question: "The rotational energy levels of a diatomic rigid rotor are equally spaced."
  type: true-false
  answer: false
  explanation: "False. The energy levels are E_J = BJ(J+1), which gives gaps of 2B, 4B, 6B, ... between successive levels. The gap between J and J+1 is 2B(J+1), which increases with J. Equal spacing would imply E_J ∝ J, as in a harmonic oscillator. The J(J+1) dependence is a hallmark of angular momentum quantization and leads to the equally spaced spectral lines (despite unequally spaced levels) via the ΔJ = ±1 selection rule."

- question: "Molecular nitrogen (N₂) does not produce a pure rotational microwave spectrum because it lacks a permanent electric dipole moment."
  type: true-false
  answer: true
  explanation: "True. To absorb microwave radiation, a molecule must have a permanent dipole moment that can interact with the oscillating electric field of the photon. N₂ is a homonuclear diatomic — its electron distribution is symmetric and there is no permanent dipole. The same applies to O₂, H₂, and Cl₂. Heteronuclear diatomics like HCl, CO, and HF do have permanent dipoles and show rich rotational spectra. The distinction is critical: microwave spectroscopy is inherently limited to polar molecules."

- question: "Why do successive absorption lines in a pure rotational spectrum appear at equally spaced frequencies, and what quantity does this spacing directly measure?"
  type: short-answer
  answer: "The ΔJ = ±1 selection rule means absorption lines occur at transitions J → J+1, with energies 2B, 4B, 6B, ... The spacing between consecutive lines is always 2B, making the spectrum a ladder of lines uniformly separated by 2B. This constant spacing directly measures the rotational constant B = ℏ²/(2I), from which the moment of inertia I and ultimately the bond length can be determined."
  explanation: "The uniform 2B spacing follows because each successive transition energy (J → J+1 vs. J+1 → J+2) differs by exactly 2B: [2B(J+2)] − [2B(J+1)] = 2B. This elegant regularity means that a single measurement of the line spacing immediately yields B, and B encodes the molecular geometry through I = μr². The ability to extract bond lengths to sub-picometer precision from this simple pattern is one of the triumphs of microwave spectroscopy."
```

## Explainer

From the rigid rotor model, you know that a diatomic molecule rotating about its center of mass behaves like a quantum mechanical rigid rotor — a system whose angular momentum is quantized rather than continuous. The **rotational quantum number J** takes integer values 0, 1, 2, 3, ... and determines both the angular momentum and the energy of each rotational state. The energy formula E_J = BJ(J+1) tells you something immediately important: rotational energy levels are not evenly spaced. The gap between J=0 and J=1 is 2B, between J=1 and J=2 is 4B, between J=2 and J=3 is 6B, and so on. Each successive gap grows by exactly 2B. This unequal spacing is a direct consequence of quantization and is the fingerprint that microwave spectroscopy exploits.

The **rotational constant B** equals ℏ²/(2I), where I is the moment of inertia of the molecule. For a diatomic molecule, I = μr², with μ being the reduced mass and r the bond length. This means B is inversely proportional to both the atomic masses and the square of the bond length. Light molecules with short bonds (like HF) have large B values and widely spaced rotational levels, while heavy molecules with long bonds (like ICl) have tiny B values and closely packed levels. Measuring B from a spectrum therefore gives you the moment of inertia directly, and from that you can extract the bond length with extraordinary precision — often to within 0.001 Å.

The **selection rule ΔJ = ±1** means that a molecule can only jump one rotational level at a time when it absorbs or emits a photon. This restriction comes from the conservation of angular momentum: a photon carries one unit of angular momentum, so the molecule must gain or lose exactly one quantum of rotational angular momentum. In absorption spectroscopy (ΔJ = +1), the absorbed frequencies form a pattern: ν = 2B, 4B, 6B, 8B, ... — a series of equally spaced lines separated by 2B. This beautifully regular pattern in the microwave spectrum is how rotational constants are measured in practice. Each line in the spectrum corresponds to a specific J → J+1 transition, and the uniform spacing 2B is the hallmark of a rigid rotor.

There is one additional subtlety from rotational spectroscopy that connects here: not every molecule has a pure rotational spectrum. A molecule must possess a permanent dipole moment to interact with the oscillating electric field of microwave radiation. Homonuclear diatomics like N₂ and O₂ are rotationally invisible in microwave spectroscopy because they lack a dipole moment, while heteronuclear diatomics like CO and HCl produce textbook rotational spectra. The degeneracy of each level also matters — each J level has (2J+1) degenerate states corresponding to different spatial orientations of the angular momentum vector, which affects the relative intensities of spectral lines through the Boltzmann distribution.
