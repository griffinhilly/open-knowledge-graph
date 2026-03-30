---
id: electronic-spectra-tanabe-sugano
title: Electronic Spectra and Tanabe-Sugano Diagrams
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: color-spectroscopy-coordination-compounds
  type: hard
- id: ligand-field-theory
  type: hard
- id: term-symbols-d-electron
  type: soft
builds-toward:
- nephelauxetic-effect-covalency
tags:
- Tanabe-Sugano diagrams
- electronic spectra
- d-d transitions
- Racah parameters
- term symbols
stage: advanced
status: validated
---

# Electronic Spectra and Tanabe-Sugano Diagrams

## Core Idea
Tanabe-Sugano diagrams plot the energies of all electronic states of a d^n ion as a function of the crystal field splitting parameter Δ/B, where B is the Racah interelectronic repulsion parameter. They provide a complete picture of the allowed electronic transitions for any d-electron configuration in an octahedral field, enabling quantitative analysis of absorption spectra — including the prediction and assignment of multiple absorption bands, the determination of Δ and B from experimental data, and the identification of spin-crossover points.

## Questions

```yaml
- question: "In a Tanabe-Sugano diagram for a d² ion, the x-axis plots Δ/B and the y-axis plots E/B. Why are energies normalized to the Racah parameter B rather than plotted as absolute energies?"
  type: multiple-choice
  options:
    - "To ensure all transition metals produce identical diagrams regardless of their identity"
    - "To create a universal, dimensionless diagram where the ratio Δ/B captures the competition between crystal field splitting and interelectron repulsion — making the diagram applicable to any d² ion by adjusting B"
    - "To eliminate the need for experimental measurements"
    - "Because absolute energies cannot be calculated from quantum mechanics"
  answer: 1
  explanation: "The Racah parameter B quantifies the magnitude of electron-electron repulsion within the d-shell. By normalizing both Δ and E to B, the diagram becomes dimensionless and universal for a given d^n configuration. Every d² octahedral complex, regardless of the specific metal and ligands, falls somewhere on the same d² Tanabe-Sugano diagram — the position is determined by the ratio Δ/B. To extract actual transition energies for a specific complex, you read E/B from the diagram and multiply by the experimentally determined B value. This normalization is what makes the diagrams so powerful: one diagram serves all d² systems."

- question: "A d⁵ Tanabe-Sugano diagram shows a discontinuity in the ground state at a specific Δ/B value. This discontinuity corresponds to the spin-crossover point between high-spin and low-spin configurations."
  type: true-false
  answer: true
  explanation: "For configurations where both high-spin and low-spin ground states are possible (d⁴ through d⁷), the Tanabe-Sugano diagram shows two regimes. At low Δ/B (weak field), the high-spin term is the ground state; at high Δ/B (strong field), the low-spin term becomes the ground state. The transition between regimes appears as a discontinuity because the ground-state line changes from one term symbol to another. At the crossover point, both states have the same energy. For d⁵, this is the transition from ⁶A₁g (high-spin, all electrons unpaired) to ²T₂g (low-spin), and it occurs at a relatively high Δ/B value because the pairing energy for five electrons is large."

- question: "From a Tanabe-Sugano diagram, you observe that a d³ octahedral complex has three spin-allowed absorption bands. This is consistent with the Tanabe-Sugano diagram, which shows three spin-allowed excited states above the ⁴A₂g ground state."
  type: true-false
  answer: true
  explanation: "For d³ in an octahedral field, the ground state is ⁴A₂g (derived from the ⁴F free-ion term). The spin selection rule (ΔS = 0) allows transitions only to other quartet states. The Tanabe-Sugano diagram shows three such states: ⁴T₂g, ⁴T₁g(F), and ⁴T₁g(P). These correspond to three spin-allowed d-d transitions, each producing an absorption band. The classic example is [Cr(H₂O)₆]³⁺, which shows exactly three bands in its UV-Vis spectrum, assignable using the d³ Tanabe-Sugano diagram to determine Δ and B."

- question: "A chemist measures two absorption band energies for a d³ octahedral complex and wants to determine both Δ and B. Explain how the Tanabe-Sugano diagram enables this from just two experimental values."
  type: short-answer
  answer: "The ratio of two transition energies (E₁/E₂) is a function of Δ/B only — it does not depend on the absolute value of B. On the Tanabe-Sugano diagram, the chemist calculates the experimental ratio E₁/E₂ and finds the Δ/B value where the diagram predicts the same ratio between the corresponding transitions. This gives Δ/B. Then, reading E₁/B from the diagram at that Δ/B value and dividing the experimental E₁ by this number gives B. Once B is known, Δ = (Δ/B) × B. Two equations, two unknowns — and the Tanabe-Sugano diagram provides the functional relationship between them."
  explanation: "This method works because the Tanabe-Sugano diagram encodes the full energy-level structure as a function of the single variable Δ/B. The ratio method eliminates B from the initial step, making it a self-consistent determination. A third band, if available, serves as an internal check on the assignments."
```

## Explainer

The absorption spectrum of a transition metal complex typically shows multiple bands, each corresponding to a different electronic transition. Crystal field theory and the spectrochemical series tell you that the primary transition occurs across the Δ gap, but they do not explain the full set of observed bands or their relative energies. Tanabe-Sugano diagrams fill this gap by providing a complete energy-level picture for each d^n configuration as a function of crystal field strength.

A Tanabe-Sugano diagram is constructed by calculating the energies of all electronic terms (from Russell-Saunders coupling) of a d^n configuration as the octahedral crystal field is turned on from zero (free-ion limit) to large values. The x-axis is Δ/B (crystal field strength normalized to the Racah parameter B, which measures electron-electron repulsion), and the y-axis is E/B (state energy normalized to B). The ground state is always plotted along the x-axis (E/B = 0). Excited states curve upward, and their slopes and curvatures encode how each state responds to the crystal field. Lines that run roughly parallel to the x-axis correspond to states insensitive to Δ; steeply rising lines correspond to states strongly destabilized by the crystal field.

The power of the diagram lies in its direct connection to experiment. For a d³ complex like [Cr(H₂O)₆]³⁺, you measure the UV-Vis spectrum and find three absorption bands. The d³ Tanabe-Sugano diagram shows three spin-allowed excited states above the ⁴A₂g ground state: ⁴T₂g, ⁴T₁g(F), and ⁴T₁g(P). By taking the ratio of two band energies and matching it to the diagram, you determine the Δ/B value for that complex. From there, you extract both Δ and B individually. The value of B for the complex is always less than the free-ion B₀ — this reduction (measured as the nephelauxetic ratio β = B/B₀) reflects the covalency of the metal-ligand bond, a topic explored further in the nephelauxetic effect.

For d⁴ through d⁷ configurations, Tanabe-Sugano diagrams also reveal the spin-crossover boundary. At low Δ/B, the ground state is a high-spin term; at high Δ/B, it switches to a low-spin term, marked by a vertical discontinuity in the diagram. Near this crossover, both spin states are close in energy, and external perturbations (temperature, pressure) can switch the complex between them — the basis for spin-crossover materials used in molecular switches and sensors. The Tanabe-Sugano diagram thus connects spectroscopy, magnetism, and materials science through a single, elegant graphical tool.
