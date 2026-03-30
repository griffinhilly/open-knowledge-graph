---
id: magnetism-coordination-compounds
title: Magnetism of Coordination Compounds
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: crystal-field-theory
  type: hard
- id: ligand-field-theory
  type: soft
builds-toward:
- jahn-teller-effect
tags:
- paramagnetism
- diamagnetism
- magnetic moment
- spin-only formula
- spin crossover
stage: advanced
status: validated
---

# Magnetism of Coordination Compounds

## Core Idea
The magnetic behavior of coordination compounds is determined by the number of unpaired electrons, which depends on the d-electron configuration and the crystal field splitting. Paramagnetic complexes (with unpaired electrons) are attracted to magnetic fields; diamagnetic complexes (all electrons paired) are weakly repelled. The spin-only magnetic moment formula μ = √(n(n+2)) BM, where n is the number of unpaired electrons, provides a first approximation that connects magnetic measurements directly to electronic structure.

## Questions

```yaml
- question: "A complex has a measured magnetic moment of 4.9 BM. How many unpaired electrons does it have, according to the spin-only formula?"
  type: multiple-choice
  options:
    - "3 unpaired electrons (μ = 3.87 BM)"
    - "4 unpaired electrons (μ = 4.90 BM)"
    - "5 unpaired electrons (μ = 5.92 BM)"
    - "2 unpaired electrons (μ = 2.83 BM)"
  answer: 1
  explanation: "The spin-only formula μ = √(n(n+2)) gives: n=1 → 1.73, n=2 → 2.83, n=3 → 3.87, n=4 → 4.90, n=5 → 5.92 BM. A measured value of 4.9 BM matches n=4 almost exactly. This measurement would be consistent with, for example, a high-spin d⁶ octahedral complex (t₂g⁴ eg², four unpaired) or a d⁴ high-spin complex (t₂g³ eg¹, four unpaired). Distinguishing between these requires additional information like the metal identity and oxidation state."

- question: "[Fe(CN)₆]⁴⁻ is diamagnetic while [Fe(H₂O)₆]²⁺ is paramagnetic with four unpaired electrons, even though both contain Fe²⁺ (d⁶). This difference arises because CN⁻ is a strong-field ligand that forces all electrons into the t₂g set."
  type: true-false
  answer: true
  explanation: "Fe²⁺ has six d-electrons. With CN⁻ (strong field, large Δ_oct), the splitting energy exceeds the pairing energy: all six electrons pair in the t₂g orbitals (t₂g⁶ eg⁰), giving zero unpaired electrons and diamagnetic behavior. With H₂O (weak field, small Δ_oct), the pairing energy exceeds Δ: electrons spread across both t₂g and eg sets following Hund's rule (t₂g⁴ eg², four unpaired electrons), giving paramagnetic behavior. This is the same d⁶ ion with the same total electron count — the ligand environment alone determines the magnetism."

- question: "The spin-only formula always accurately predicts the magnetic moment of any coordination compound."
  type: true-false
  answer: false
  explanation: "The spin-only formula ignores the orbital angular momentum contribution to the magnetic moment. For first-row transition metals, orbital contributions are largely quenched by the crystal field, so the spin-only formula works reasonably well. But for second- and third-row metals (where spin-orbit coupling is stronger), and for first-row ions where the ground state has an orbital degeneracy (like T terms in octahedral fields), the orbital contribution becomes significant and measured moments deviate from spin-only values. Lanthanide complexes require a completely different approach (the full J-based formula) because spin-orbit coupling dominates."

- question: "Explain the phenomenon of spin crossover and describe the conditions under which a coordination compound might switch between high-spin and low-spin states."
  type: short-answer
  answer: "Spin crossover occurs when the crystal field splitting energy Δ is close to the electron pairing energy P, so that the high-spin and low-spin states are nearly degenerate. In this regime, external perturbations — changes in temperature, pressure, or light irradiation — can shift the equilibrium between the two states. Raising temperature favors the high-spin state (higher entropy due to more unpaired electrons and longer metal-ligand bonds). Increasing pressure favors the low-spin state (shorter bonds, smaller volume). The phenomenon is most common for d⁴ through d⁷ octahedral complexes with intermediate-field ligands, particularly Fe²⁺ (d⁶) and Fe³⁺ (d⁵) complexes with nitrogen-donor ligands. Spin-crossover compounds are of interest for molecular switches, sensors, and displays because the spin state change produces measurable changes in color, magnetic moment, and crystal volume."
  explanation: "The spin-crossover transition can be gradual (smooth thermal equilibrium) or abrupt (cooperative, with hysteresis), depending on crystal packing and intermolecular interactions. Abrupt transitions with hysteresis are the most technologically interesting because they provide bistability — the compound has memory of its thermal history."
```

## Explainer

Magnetic measurements are among the simplest and most informative experiments in coordination chemistry. Placing a sample between the poles of a magnet and measuring its response immediately tells you whether it has unpaired electrons: paramagnetic substances are drawn into the field, while diamagnetic substances are weakly repelled. A quantitative measurement of the magnetic susceptibility yields the magnetic moment, from which you can determine the number of unpaired electrons — and from that, the electronic configuration and spin state.

The spin-only magnetic moment formula μ = √(n(n+2)) Bohr magnetons (BM) connects the measured moment directly to the electron count. For n = 1, μ = 1.73 BM; for n = 5, μ = 5.92 BM. This formula assumes that the magnetic moment comes entirely from electron spin with no contribution from orbital angular momentum. This approximation works well for most first-row transition metal complexes because the crystal field quenches the orbital contribution by lifting the orbital degeneracy. For second- and third-row metals, and for lanthanides, spin-orbit coupling contributes significantly and more sophisticated treatments are needed.

The practical power of magnetic measurements lies in distinguishing high-spin from low-spin configurations. Consider Fe²⁺ (d⁶): a high-spin octahedral complex has four unpaired electrons (μ ≈ 4.9 BM), while a low-spin complex has zero (μ = 0, diamagnetic). A simple measurement with a Gouy balance or SQUID magnetometer instantly identifies the spin state, which in turn reveals whether the ligand field is weak or strong. This is one of the primary experimental tools for probing electronic structure, complementing the spectroscopic information from UV-Vis spectra.

Spin-crossover phenomena extend magnetic measurements into the realm of smart materials. When Δ is approximately equal to the pairing energy P, the complex sits at the boundary between high-spin and low-spin states. Temperature changes can push the equilibrium: cooling favors the low-spin state (lower energy), while heating favors the high-spin state (higher entropy from unpaired electrons and the longer, softer metal-ligand bonds). In the solid state, cooperative interactions between molecules can make this transition abrupt with hysteresis — the complex remembers whether it was last heated or cooled. These bistable spin-crossover compounds are actively researched for molecular memory devices and display technologies.
