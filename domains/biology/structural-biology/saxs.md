---
id: saxs
title: SAXS
domain: biology
course: structural-biology
prerequisites:
- id: protein-folding-and-chaperones
  type: hard
- id: diffraction-and-fourier-transforms
  type: soft
builds-toward:
- intrinsically-disordered-proteins
tags:
- SAXS
- small-angle-X-ray-scattering
- solution-scattering
- envelope
- radius-of-gyration
stage: expert
status: validated
---
# SAXS

## Core Idea
Small-angle X-ray scattering (SAXS) measures the scattering of X-rays by macromolecules in solution, providing low-resolution structural information about molecular size, shape, and oligomeric state without requiring crystals or isotope labeling. The scattering curve (intensity vs. scattering angle) encodes the radius of gyration (Rg, from the Guinier approximation), maximum dimension (Dmax, from the pair distribution function), and overall molecular envelope (from ab initio shape reconstruction). SAXS is particularly valuable for characterizing flexible and disordered proteins, multi-domain assemblies, conformational changes upon ligand binding, and quality control of purified samples. It complements high-resolution methods by providing solution-state shape information under nearly any buffer condition.

## Questions

```yaml
- question: "A SAXS experiment measures the radius of gyration (Rg) and maximum dimension (Dmax) of a protein. What structural information do these parameters provide?"
  type: multiple-choice
  options:
    - "The precise position of every atom in the protein"
    - "Rg quantifies the overall compactness of the molecule (the average distance of all atoms from the center of mass), and Dmax gives the longest intramolecular distance — together they characterize the overall size and shape (compact vs. extended, globular vs. elongated) without atomic resolution"
    - "The amino acid sequence of the protein"
    - "The secondary structure content (percent helix, sheet)"
  answer: 1
  explanation: "SAXS provides global shape parameters, not atomic coordinates. Rg is sensitive to the overall mass distribution — a compact, globular protein has a smaller Rg than an extended, multi-domain protein of the same molecular weight. Dmax gives the largest distance within the molecule. Together, they distinguish between globular (small Rg/Dmax), elongated (large Dmax, moderate Rg), and disordered (large Rg relative to mass) conformations. These parameters can be compared to values predicted from crystal structures to assess whether the solution conformation matches the crystal conformation, and they can detect conformational changes (compaction or extension) upon ligand binding."

- question: "SAXS can determine the atomic-resolution structure of a protein without any complementary technique."
  type: true-false
  answer: false
  explanation: "SAXS data is inherently low-resolution — the scattering curve is a rotationally averaged signal from randomly oriented molecules in solution, containing far less information than a crystal diffraction pattern. Ab initio shape reconstruction from SAXS produces a molecular envelope (overall shape) at ~15-25 Angstrom resolution, not atomic coordinates. However, SAXS is extremely valuable when combined with high-resolution structures: it can assess which crystal structure conformation is most consistent with the solution state, distinguish between alternative quaternary structures, model multi-domain arrangements, and characterize conformational ensembles of flexible proteins. Its power is in providing solution-state shape constraints that complement high-resolution crystallographic or cryo-EM structures."

- question: "Why is SAXS particularly useful for studying intrinsically disordered proteins (IDPs) and multi-domain proteins with flexible linkers?"
  type: short-answer
  answer: "These proteins are difficult or impossible to study by crystallography (they do not form ordered crystals) and may be too heterogeneous for cryo-EM (many conformations). SAXS measures the average size and shape of the conformational ensemble in solution — the Rg, Dmax, and Kratky plot (which distinguishes compact from disordered proteins by the shape of the scattering curve) provide direct evidence of disorder or flexibility. For multi-domain proteins, SAXS can determine the relative arrangement and flexibility of domains by fitting scattering curves to multi-domain models with adjustable inter-domain angles. Ensemble methods (like EOM — Ensemble Optimization Method) fit the experimental SAXS curve to a weighted mixture of conformations, characterizing the range of shapes a flexible protein adopts."
  explanation: "The Kratky plot is a key diagnostic: a bell-shaped curve indicates a compact, globular protein, while a plateau or monotonic increase at high angles indicates disorder or flexibility. This simple analysis immediately classifies a protein's conformational state without any modeling, making SAXS an excellent first-pass characterization technique."
```

## Explainer

Not all structural questions require atomic resolution. Before determining a crystal structure or cryo-EM map, a researcher often needs to answer simpler but equally important questions: Is this protein globular or elongated? Is it monomeric or dimeric in solution? Does it undergo a conformational change upon ligand binding? Is it folded or disordered? **SAXS** answers these questions rapidly, in solution, under any buffer conditions, with minimal sample requirements.

In a SAXS experiment, a dilute protein solution (~0.5-5 mg/mL) is exposed to a focused X-ray beam, and the scattering at low angles (0.5-5 degrees) is measured on a detector. Unlike crystallography (where the crystal lattice produces discrete diffraction spots), solution SAXS produces a smooth, continuous scattering curve because the molecules are randomly oriented — the signal is the rotational average of the scattering from all orientations. The scattering curve I(q) as a function of momentum transfer q (proportional to the scattering angle) encodes the overall size and shape of the molecule.

The most fundamental analysis extracts the **radius of gyration** (Rg) from the Guinier region (very low angles, where the scattering curve is approximately Gaussian). Rg quantifies the overall compactness of the molecule — a larger Rg means a more extended molecule. The **pair distribution function** P(r) — obtained by indirect Fourier transform of the scattering curve — shows the distribution of all intramolecular distances, with the maximum distance being Dmax. A spherical protein has a bell-shaped P(r) that drops to zero at a Dmax approximately equal to the diameter. An elongated protein has a skewed P(r) extending to larger distances. A multi-domain protein with a flexible linker shows a P(r) with a shoulder reflecting the inter-domain separation.

For more detailed modeling, **ab initio shape reconstruction** algorithms (like DAMMIF/DAMMIN) build dummy-atom models that reproduce the experimental scattering curve, producing a molecular envelope at ~15-25 Angstrom resolution. When high-resolution structures of individual domains are available, **rigid-body modeling** fits the relative positions and orientations of domains to the SAXS data. For flexible systems, **ensemble methods** (EOM, MultiFoXS) generate thousands of conformations and select a weighted ensemble that best fits the experimental curve — characterizing not a single structure but the range of shapes the molecule adopts in solution. SAXS has become an essential complement to high-resolution methods, providing the solution-state context that crystallographic and cryo-EM structures need for complete biological interpretation.
