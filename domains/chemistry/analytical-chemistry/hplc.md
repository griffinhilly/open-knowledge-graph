---
id: hplc
title: High-Performance Liquid Chromatography (HPLC)
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: chromatography-fundamentals
  type: hard
- id: thin-layer-chromatography
  type: soft
- id: beers-law
  type: soft
tags:
- HPLC
- reverse phase
- gradient elution
- UV detection
- retention time
- C18
stage: advanced
status: validated
---

# High-Performance Liquid Chromatography (HPLC)

## Core Idea
High-performance liquid chromatography pumps a liquid mobile phase through a column packed with small (1.7–5 µm) particles at high pressure, achieving rapid, high-resolution separations of non-volatile and thermally labile compounds. Reverse-phase HPLC (nonpolar stationary phase, aqueous–organic mobile phase) is the dominant mode, separating analytes by hydrophobicity. Gradient elution — progressively increasing organic solvent content — improves peak shape for complex samples. UV/Vis, fluorescence, and mass spectrometric detectors are most common. Method development balances resolution, run time, and mobile phase composition.

## How It's Best Learned
Develop an HPLC method to separate a mixture of drug compounds or amino acid derivatives, systematically varying %organic modifier, pH, and gradient slope. Overlaying chromatograms at each condition and applying resolution calculations makes the theoretical framework concrete.

## Common Misconceptions
- Retention time alone cannot confirm compound identity — co-eluting impurities with similar retention times require spectral confirmation (diode array or MS).
- Ultra-HPLC (UHPLC) is not simply faster HPLC; the sub-2-µm particles require specially designed pumps and low-dead-volume instruments.

## Questions

```yaml
- question: "In reverse-phase HPLC with a C18 column and an aqueous/acetonitrile mobile phase, two compounds are injected: one is polar and hydrophilic, the other is nonpolar and hydrophobic. Which will elute first, and why?"
  type: multiple-choice
  options:
    - "The nonpolar compound, because it is repelled by the polar aqueous mobile phase and moves faster"
    - "The polar compound, because it has low affinity for the nonpolar stationary phase and is carried through quickly by the aqueous mobile phase"
    - "Both elute at the same time, since retention time depends only on molecular weight"
    - "The polar compound, because polar interactions with the C18 phase are stronger than hydrophobic ones"
  answer: 1
  explanation: "In reverse-phase HPLC, the stationary phase (C18) is nonpolar and the mobile phase is predominantly aqueous. Polar, hydrophilic compounds have little affinity for the nonpolar stationary phase and are swept through quickly, eluting early. Nonpolar compounds interact strongly with C18 via hydrophobic interactions and are retained longer, eluting later. Retention time reflects partitioning between stationary and mobile phases, not molecular weight."

- question: "If two compounds have the same retention time in an HPLC run, you can confidently conclude they are the same compound."
  type: true-false
  answer: false
  explanation: "Retention time is necessary but not sufficient for identification. Different compounds can co-elute under a given set of conditions. Definitive identification requires additional spectral data — a UV/Vis diode array detector showing the same absorption spectrum, or mass spectrometric detection confirming the molecular ion and fragmentation pattern. This is one of the most common over-interpretations in HPLC practice."

- question: "What is gradient elution in HPLC, and what problem does it solve when analyzing a complex mixture?"
  type: short-answer
  answer: "Gradient elution progressively increases the proportion of organic solvent (e.g., acetonitrile) in the mobile phase over the course of the run. Early-eluting polar compounds are separated under weak conditions; as the gradient increases organic content, more hydrophobic compounds are pulled off the column. Without gradient elution, a fixed mobile phase composition either fails to retain early peaks adequately or requires very long run times to elute late-eluting compounds."
  explanation: "In complex samples, analytes span a wide range of hydrophobicities. Isocratic (fixed composition) conditions cannot optimize resolution and run time simultaneously for all components. Gradient elution is analogous to adjusting the 'strength' of the mobile phase mid-run to sweep out progressively more retained analytes efficiently."
```

## Explainer

You already know from chromatography fundamentals that separation works by differential partitioning: analytes distribute between a stationary phase and a mobile phase, and compounds that spend more time in the stationary phase travel more slowly. HPLC takes this principle and pushes it to extreme efficiency by using very small particles (1.7–5 µm) packed under high pressure (hundreds to thousands of psi). Smaller particles mean shorter diffusion paths, sharper peaks, and far better resolution than open-column or thin-layer chromatography can achieve — at the cost of specialized pumps and equipment capable of handling the pressure.

Reverse-phase HPLC dominates modern analytical chemistry because it handles the wide range of polar, semi-polar, and moderately nonpolar compounds found in pharmaceuticals, biological samples, and environmental matrices. "Reverse phase" means the stationary phase is nonpolar — typically a silica support with C18 hydrocarbon chains bonded to it — and the mobile phase is polar, usually a mixture of water and an organic solvent like acetonitrile or methanol. Compounds partition based on hydrophobicity: polar compounds prefer the aqueous mobile phase and elute quickly; nonpolar compounds are attracted to the C18 chains and are retained longer. Adjusting the water-to-organic ratio shifts where compounds elute on the chromatogram.

For complex samples containing analytes across a wide range of hydrophobicities, isocratic elution (constant mobile phase composition) forces an impossible compromise — either early peaks are poorly resolved or late peaks require very long run times. Gradient elution solves this by starting with high aqueous content and progressively increasing the organic modifier. Polar compounds elute early under "weak" conditions; as the gradient strengthens, more hydrophobic compounds are efficiently swept from the column. Well-designed gradients can resolve dozens of compounds in a single run.

Detection is separate from separation. The most common detector is UV/Vis absorbance, exploiting the fact that most organic molecules absorb UV light. A diode array detector measures the full UV spectrum at every point in the run, allowing peak identification by absorption spectrum and helping detect co-eluting impurities. Mass spectrometric detection (LC-MS) adds molecular weight and fragmentation information, enabling confident structural identification even for trace components. This is why retention time alone is never sufficient proof of identity — two compounds can co-elute with identical retention times under a given set of conditions but differ completely in their spectra.
