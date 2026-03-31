---
id: x-ray-crystallography
title: X-ray Crystallography
domain: biology
course: structural-biology
prerequisites:
- id: protein-crystallization
  type: hard
- id: diffraction-and-fourier-transforms
  type: hard
builds-toward:
- structure-solution-methods
- structure-based-drug-design
tags:
- X-ray-crystallography
- crystal-structure
- diffraction-pattern
- resolution
- electron-density
stage: expert
status: validated
---
# X-ray Crystallography

## Core Idea
X-ray crystallography determines the three-dimensional atomic structure of molecules by directing an X-ray beam at a crystal, measuring the diffraction pattern produced by the regularly repeating lattice of molecules, and computationally reconstructing the electron density map from which atomic coordinates are derived. It has been the dominant method for protein structure determination, contributing the majority of structures in the Protein Data Bank. The method requires well-ordered crystals, and the resulting structure represents a time-averaged and space-averaged snapshot of the molecule in the crystal environment. Resolution (typically 1.5-3.0 Angstroms for protein crystals) determines the level of atomic detail visible in the electron density map.

## Questions

```yaml
- question: "A protein crystal diffracts X-rays to 2.0 Angstrom resolution. What level of structural detail can be reliably determined?"
  type: multiple-choice
  options:
    - "Only the overall protein shape with no atomic detail"
    - "Individual atoms can be resolved in well-ordered regions, water molecules are visible, and side chain conformations can be assigned with confidence"
    - "Only the positions of alpha-carbon backbone atoms"
    - "Hydrogen atom positions are precisely determined"
  answer: 1
  explanation: "At 2.0 Angstrom resolution, the electron density map shows distinct features for individual atoms (though not fully resolved as separate peaks), backbone and side chain conformations are clear, ordered water molecules appear as discrete density peaks, and ligand binding modes can be determined. This is considered good resolution for drug design and mechanistic analysis. At lower resolution (3.0+ A), only the backbone trace and large side chains are reliable. At very high resolution (<1.2 A), individual hydrogen atoms become visible. The 2.0 A resolution represents the 'sweet spot' where most biologically important structural features are well defined."

- question: "X-ray crystallography captures the dynamic motion of a protein in solution."
  type: true-false
  answer: false
  explanation: "Crystallography produces a static, time-averaged and space-averaged structure. The crystal lattice constrains molecular motion, and the diffraction experiment averages over billions of molecules and the duration of data collection. Dynamic information is partially encoded in B-factors (temperature factors), which reflect the degree of atomic disorder — higher B-factors indicate more mobile regions. But B-factors conflate true dynamics with crystal packing disorder and data quality issues. For genuine dynamic information, NMR spectroscopy, molecular dynamics simulations, or time-resolved crystallography (using X-ray free-electron lasers) are needed."

- question: "Why is the 'phase problem' the central computational challenge in X-ray crystallography?"
  type: short-answer
  answer: "The diffraction experiment measures the intensities (squared amplitudes) of the diffracted X-rays, but not their phases. Both amplitude and phase are needed to reconstruct the electron density map via Fourier transform. The phase information is lost during measurement because X-ray detectors record only intensity (number of photons), not the relative timing of the waves. Without phases, the electron density cannot be calculated — the intensities alone are compatible with an astronomically large number of possible electron density maps. Phase determination methods (molecular replacement, isomorphous replacement, anomalous dispersion) are therefore essential and often the rate-limiting step in structure determination."
  explanation: "The phase problem has driven much of the methodological innovation in crystallography. Molecular replacement (using a known homologous structure's phases as a starting estimate) works when a similar structure exists. For novel folds, experimental phasing using heavy atoms (isomorphous replacement) or anomalous scattering (selenomethionine labeling) provides initial phase estimates that are refined iteratively."
```

## Explainer

X-ray crystallography has been the engine of structural biology for nearly a century, from the first protein structure (myoglobin, 1958) to the vast majority of the ~200,000 structures in the Protein Data Bank today. The method exploits a fundamental physical principle: when X-rays (electromagnetic radiation with wavelength ~1 Angstrom, comparable to interatomic distances) interact with the regular array of atoms in a crystal, they scatter in specific directions determined by the crystal's atomic arrangement. The resulting **diffraction pattern** — a collection of spots (reflections) on the detector, each with a measurable intensity — encodes the information needed to reconstruct the three-dimensional distribution of electrons in the crystal.

The reconstruction requires solving the **Fourier transform** that relates the diffraction pattern to the electron density map. Each reflection contributes a wave to the electron density, characterized by its amplitude (derivable from the measured intensity, which is the amplitude squared) and its phase (the relative timing of the wave). The fundamental problem is that detectors measure only intensity — the phases are lost. This is the **phase problem**, the central computational challenge. Without phases, the Fourier transform cannot be computed. Solutions include **molecular replacement** (using the phases from a known similar structure), **isomorphous replacement** (introducing heavy atoms into the crystal and using the intensity differences to derive phases), and **anomalous dispersion** (exploiting the wavelength-dependent scattering of atoms like selenium to extract phase information).

Once phases are obtained, the electron density map is calculated and interpreted. At good resolution (1.5-2.5 A), the density reveals the protein backbone, side chain orientations, bound ligands, and ordered water molecules. The atomic model is iteratively refined against the experimental data — adjusting atomic coordinates and B-factors (which model atomic mobility/disorder) to minimize the difference between the calculated and observed diffraction patterns. The R-factor and R-free (cross-validation metric) assess agreement between model and data, and stereochemical validation (Ramachandran plot, bond geometry) checks the model against known chemical constraints.

The limitations of crystallography are well understood: it requires crystals (which not all proteins form, especially membrane proteins and large flexible complexes), the crystal environment may distort the structure, and it provides a static picture that obscures dynamics. Despite these limitations, crystallography remains the gold standard for high-resolution structural information and the foundation for structure-based drug design, enzyme mechanism analysis, and understanding molecular recognition. Its combination of atomic resolution, mature methodology, and vast database of solved structures makes it an indispensable tool in structural biology.
