---
id: color-spectroscopy-coordination-compounds
title: Color and Spectroscopy of Coordination Compounds
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: crystal-field-theory
  type: hard
- id: spectrochemical-series
  type: hard
builds-toward:
- electronic-spectra-tanabe-sugano
tags:
- d-d transitions
- color
- UV-Vis spectroscopy
- selection rules
- charge transfer
stage: formal-systems
status: validated
---

# Color and Spectroscopy of Coordination Compounds

## Core Idea
The vivid colors of transition metal complexes arise from electronic transitions between d-orbitals split by the crystal field. A complex absorbs light at wavelengths corresponding to the energy gap Δ, and we perceive the complementary color to what is absorbed. Selection rules (Laporte and spin) govern which transitions are allowed, explaining why some complexes are intensely colored while others are pale.

## Questions

```yaml
- question: "A complex absorbs strongly in the orange region (~600 nm) of the visible spectrum. What color does the complex appear?"
  type: multiple-choice
  options:
    - "Orange"
    - "Blue"
    - "Green"
    - "Red"
  answer: 1
  explanation: "The observed color is the complement of the absorbed color. Orange light (~600 nm) and blue light (~450 nm) are complementary colors. When the complex absorbs orange, it transmits and reflects all other wavelengths, but the dominant perceived color is blue. This is why the color wheel is so useful in coordination chemistry: find the absorbed color on the wheel, and the opposite side gives you the observed color."

- question: "The Laporte selection rule states that d-d transitions in centrosymmetric (octahedral) complexes are formally forbidden because the transition does not involve a change in parity (g → g)."
  type: true-false
  answer: true
  explanation: "The Laporte rule requires that allowed electronic transitions must involve a change in the orbital angular momentum quantum number (Δl = ±1), which translates to a change in parity: gerade (g) to ungerade (u) or vice versa. In an octahedral complex, d-orbitals are all gerade (even under inversion), so d-d transitions are g → g and formally Laporte-forbidden. This is why d-d transitions are relatively weak (molar absorptivity ε typically 1-100 M⁻¹cm⁻¹) compared to fully allowed transitions (ε > 1000). The transitions are not completely forbidden because vibrational coupling temporarily destroys the inversion center, making them weakly allowed."

- question: "Charge-transfer transitions in coordination compounds are typically much more intense than d-d transitions because they are Laporte-allowed."
  type: true-false
  answer: true
  explanation: "Charge-transfer (CT) transitions involve electron movement between ligand orbitals and metal orbitals — for example, from a ligand-centered orbital (ungerade) to a metal d-orbital (gerade), or vice versa. These transitions involve a change in parity (u → g or g → u) and are therefore Laporte-allowed, giving molar absorptivities of 1000-50,000 M⁻¹cm⁻¹. This is why compounds like permanganate (MnO₄⁻) are so intensely colored — their purple color arises from ligand-to-metal charge transfer, not weak d-d transitions."

- question: "[Mn(H₂O)₆]²⁺ is nearly colorless despite having five d-electrons. Explain why, referencing both the spin and Laporte selection rules."
  type: short-answer
  answer: "Mn²⁺ is d⁵ high-spin with all five electrons having parallel spins (one in each d-orbital). Any d-d transition would require flipping the spin of the promoted electron to pair with an electron in the destination orbital, violating the spin selection rule (ΔS = 0 required). These spin-forbidden transitions are extremely weak. Combined with the Laporte selection rule (d-d transitions in octahedral complexes are parity-forbidden), the absorption is doubly forbidden, making [Mn(H₂O)₆]²⁺ nearly colorless with a very pale pink tint visible only in concentrated solutions."
  explanation: "This is a beautiful example of selection rules in action. The faint pink color that IS visible comes from spin-orbit coupling, which weakly relaxes the spin selection rule. But the double prohibition (spin-forbidden AND Laporte-forbidden) makes d⁵ high-spin octahedral complexes the weakest absorbers among all d-electron configurations."

- question: "Why do tetrahedral complexes often have more intense d-d absorption bands than their octahedral counterparts, even though tetrahedral Δ is smaller?"
  type: short-answer
  answer: "Tetrahedral complexes lack an inversion center, so the Laporte selection rule does not strictly apply. In an octahedral complex, d-d transitions are formally parity-forbidden (g → g) and rely on vibrational coupling to gain intensity. In a tetrahedron, there is no inversion symmetry, so the d-orbitals mix partially with p-orbitals (which have opposite parity), and the transition gains some formally allowed character. This relaxation of the Laporte rule means tetrahedral d-d bands are typically 10-100 times more intense than octahedral ones, even though the absorption energy may be lower due to the smaller Δ_tet."
  explanation: "This explains an otherwise puzzling observation: CoCl₄²⁻ (tetrahedral, intense blue) is deeply colored while [Co(H₂O)₆]²⁺ (octahedral, pale pink) is barely colored, despite cobalt being in the same oxidation state in both."
```

## Explainer

The colors of transition metal complexes are not decorative curiosities — they are direct windows into electronic structure. When white light passes through a solution of a coordination compound, specific wavelengths are absorbed, promoting electrons from lower-energy d-orbitals to higher-energy ones. The light that passes through — the complement of what was absorbed — is the color we perceive. A complex that absorbs red light appears green; one that absorbs blue-violet appears yellow-orange. Crystal field theory provides the framework: the energy gap Δ between split d-orbital sets corresponds to specific photon energies in (or near) the visible spectrum.

Not all d-d transitions are equally probable, and this is where selection rules become critical. Two rules govern the intensity of absorption. The Laporte rule states that transitions must involve a change in parity — gerade to ungerade or vice versa. Since d-orbitals in an octahedral complex are all gerade, d-d transitions are Laporte-forbidden. The spin selection rule states that the spin multiplicity must not change (ΔS = 0) — meaning an electron cannot flip its spin during the transition. Both rules can be relaxed: vibronic coupling (molecular vibrations that temporarily destroy the inversion center) weakly allows Laporte-forbidden transitions, and spin-orbit coupling weakly allows spin-forbidden ones. The net result is that d-d transitions in octahedral complexes are relatively weak, with typical molar absorptivities of 1-100 M⁻¹cm⁻¹.

Charge-transfer transitions provide a dramatic contrast. In a ligand-to-metal charge transfer (LMCT), an electron moves from a ligand-based orbital to an empty or half-filled metal d-orbital; in metal-to-ligand charge transfer (MLCT), the reverse occurs. Because these transitions involve different types of orbitals with different parities, they are Laporte-allowed and intensely colored (ε = 1000-50,000 M⁻¹cm⁻¹). The deep purple of permanganate, the intense yellow of chromate, and the red of [Fe(bipy)₃]²⁺ all arise from charge-transfer transitions rather than d-d transitions. Recognizing whether an intense color comes from CT or d-d transitions is an essential analytical skill.

The interplay of these factors creates the rich palette of coordination chemistry. Weak-field, high-spin d⁵ complexes like [Mn(H₂O)₆]²⁺ are nearly colorless because their transitions are both spin- and Laporte-forbidden. Strong-field, low-spin d⁶ complexes like [Co(NH₃)₆]³⁺ show clear color because spin-allowed transitions exist. Tetrahedral complexes like CoCl₄²⁻ are more deeply colored than their octahedral counterparts because the absence of an inversion center relaxes the Laporte rule. Each color tells a story about geometry, field strength, and electronic configuration.
