---
id: structure-solution-methods
title: Structure Solution Methods
domain: biology
course: structural-biology
prerequisites:
- id: x-ray-crystallography
  type: hard
- id: diffraction-and-fourier-transforms
  type: hard
builds-toward:
- structure-based-drug-design
tags:
- molecular-replacement
- isomorphous-replacement
- anomalous-dispersion
- SAD
- MAD
- phasing
stage: expert
status: validated
---
# Structure Solution Methods

## Core Idea
Structure solution methods address the phase problem in X-ray crystallography — determining the phases of diffraction reflections that are lost during measurement. Three major approaches exist: molecular replacement (MR) uses a known homologous structure as a search model, rotating and translating it to find the correct orientation and position in the new crystal's unit cell; isomorphous replacement (MIR/SIR) introduces heavy atoms into the crystal and uses the intensity differences between native and derivative data sets to calculate phases; and anomalous dispersion (SAD/MAD) exploits the wavelength-dependent scattering of specific atoms (selenium, introduced via selenomethionine labeling) to extract phase information from a single crystal form. Molecular replacement dominates current practice because of the large number of known structures available as search models.

## Questions

```yaml
- question: "Molecular replacement requires a search model with sufficient structural similarity to the target. Below what approximate sequence identity does molecular replacement typically fail?"
  type: multiple-choice
  options:
    - "Below 95% — only nearly identical structures work"
    - "Below approximately 25-30% sequence identity, because structural divergence becomes too great for the search model to provide useful phases"
    - "Molecular replacement works at any sequence identity"
    - "Below 80% — high homology is always required"
  answer: 1
  explanation: "The success of molecular replacement depends on how closely the search model matches the target structure. Above 30-40% sequence identity, structures are generally similar enough that MR succeeds. Between 20-30%, success depends on the specific case — conserved core regions may be similar enough, but loops and insertions diverge. Below 20%, structural similarity is typically insufficient for MR, and experimental phasing (heavy atom or anomalous methods) is needed. The availability of AlphaFold predictions has extended MR to lower sequence identity targets by providing better search models than any single experimental structure."

- question: "Single-wavelength anomalous dispersion (SAD) using selenomethionine-labeled protein has become the most common experimental phasing method because it requires only one data set from one crystal."
  type: true-false
  answer: true
  explanation: "SAD phasing using selenomethionine (SeMet) has largely replaced MIR and MAD as the experimental phasing method of choice. Selenomethionine is incorporated biosynthetically by expressing the protein in methionine-auxotrophic bacteria grown on SeMet-supplemented media. The selenium atoms provide anomalous scattering signal at wavelengths near their absorption edge. SAD requires only one data set at one wavelength (near the selenium edge), while MAD requires data at multiple wavelengths. Modern computational methods (density modification, automated model building) can resolve the phase ambiguity inherent in SAD, making it robust enough that the additional wavelengths of MAD are usually unnecessary. The simplicity of SAD (one crystal, one data set) has made it the default experimental phasing approach."

- question: "Explain why molecular replacement works — how can phases from a different (homologous) protein help solve the structure of the target protein?"
  type: short-answer
  answer: "If a known structure is sufficiently similar to the target, their electron density distributions are similar. Placing the known structure in the correct position and orientation within the target's unit cell provides an approximate electron density map, from which approximate phases can be calculated. These phases are 'close enough' to the true phases that the resulting electron density map (computed with model phases and experimental amplitudes) reveals features of the target protein not present in the search model — new side chains, different loop conformations, bound ligands. Iterative refinement improves the phases and model simultaneously. The approach works because the phase information is dominated by the overall protein fold (which is conserved between homologs) rather than the sequence-specific details (which differ)."
  explanation: "Molecular replacement's dominance reflects the growth of the PDB — with over 200,000 experimental structures and millions of AlphaFold predictions, the probability of finding a suitable search model for any new protein is high. The method is fast (minutes to hours) compared to experimental phasing (days to weeks), which is why it is tried first for every new crystal structure."
```

## Explainer

The phase problem is the central obstacle in X-ray crystallography: you measure intensities but need phases to calculate the electron density map. Three strategies have been developed to overcome it, each exploiting a different physical or biological principle.

**Molecular replacement (MR)** is the most widely used method. If the structure of a homologous protein is known, it can serve as an initial estimate of the target's structure. The search model is systematically rotated (rotation function) and translated (translation function) to find the orientation and position within the target crystal's unit cell that best explains the observed diffraction data. Once correctly placed, the model provides approximate phases. These approximate phases, combined with the experimental amplitudes, generate an electron density map that shows features of the target not present in the search model. Iterative cycles of model building and refinement improve the phases until the structure converges. MR is fast and requires no special crystal preparation, but it fails when no suitable homolog exists.

**Isomorphous replacement** was the method used to solve the first protein crystal structures (myoglobin, hemoglobin). Heavy atoms (mercury, platinum, gold) are soaked into the crystal, binding at specific sites without disrupting the crystal lattice (isomorphous = same crystal form). The intensity differences between native and heavy-atom-derivative diffraction patterns are attributable to the heavy atoms, whose positions can be determined. These positions provide the initial phase estimates. Multiple isomorphous replacement (MIR) uses two or more derivatives to resolve the phase ambiguity. The method is elegant in principle but laborious in practice — finding derivatives that bind without disrupting the crystal, collecting multiple complete data sets — which is why it has been largely superseded by anomalous methods.

**Anomalous dispersion** exploits the fact that atoms scatter X-rays differently near their absorption edges. Selenium (incorporated as selenomethionine), sulfur (in native cysteine/methionine), or metal ions absorb X-rays at specific wavelengths, producing a small anomalous scattering signal that breaks the symmetry of the diffraction pattern. In **SAD** (single-wavelength anomalous dispersion), data is collected at one wavelength near the absorption edge, and the anomalous differences reveal the positions of the anomalous scatterers (selenium atoms). These positions provide phase estimates, which are improved by density modification (solvent flattening, histogram matching). In **MAD** (multi-wavelength anomalous dispersion), data at multiple wavelengths provides additional constraints for more accurate phasing. Selenomethionine SAD has become the default experimental phasing method because it combines straightforward sample preparation (biosynthetic incorporation), strong anomalous signal, and robust computational methods — making it practical for even moderately diffracting crystals.
