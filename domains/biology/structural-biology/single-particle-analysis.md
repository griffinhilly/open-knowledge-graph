---
id: single-particle-analysis
title: Single-Particle Analysis
domain: biology
course: structural-biology
prerequisites:
- id: cryo-em
  type: hard
- id: diffraction-and-fourier-transforms
  type: soft
builds-toward:
- macromolecular-assemblies
tags:
- single-particle
- image-processing
- 2D-classification
- 3D-reconstruction
- RELION
- cryoSPARC
stage: expert
status: validated
---
# Single-Particle Analysis

## Core Idea
Single-particle analysis is the computational pipeline that converts thousands to millions of noisy 2D cryo-EM images of individual molecules into a high-resolution 3D density map. The process involves particle picking (identifying and extracting individual molecule images from micrographs), 2D classification (grouping similar views and removing junk), 3D reconstruction (determining the orientation of each particle and combining them into a 3D map), and refinement (iteratively improving the orientation assignments and map quality). Modern software (RELION, cryoSPARC) uses maximum-likelihood statistical frameworks and GPU-accelerated computation. A key capability is 3D classification, which can separate conformationally heterogeneous particles into distinct classes, revealing multiple functional states from a single specimen.

## Questions

```yaml
- question: "Why does single-particle cryo-EM require averaging tens of thousands to millions of individual particle images?"
  type: multiple-choice
  options:
    - "Because each particle image is unique and cannot be compared to others"
    - "Because each individual particle image has extremely low signal-to-noise ratio (the electron dose must be kept low to prevent radiation damage), and averaging many images of particles in the same orientation builds up the signal while averaging out the noise"
    - "Because the microscope can only image one particle at a time"
    - "Because statistical significance requires large sample sizes for any measurement"
  answer: 1
  explanation: "Biological specimens are radiation-sensitive — high electron doses destroy the structure. Each particle image is therefore taken with very few electrons (~20-40 electrons per Angstrom squared), resulting in extremely noisy images where the protein signal is barely distinguishable from noise. Averaging N images in the same orientation improves the signal-to-noise ratio by a factor of sqrt(N). To achieve near-atomic resolution, the SNR must be improved by a factor of ~100-1000, requiring tens of thousands to millions of particle images. This is why cryo-EM is fundamentally a statistical method — the resolution depends on having enough particles to average."

- question: "3D classification in single-particle analysis can only separate particles by their orientation, not by their conformation."
  type: true-false
  answer: false
  explanation: "3D classification is one of cryo-EM's most powerful capabilities — it can sort particles into groups that differ in both orientation AND conformation. If a sample contains molecules in multiple functional states (e.g., a ribosome in pre- and post-translocation states, or a channel in open and closed conformations), 3D classification assigns each particle to the conformational class it best matches. The result is separate 3D reconstructions for each conformational state, revealing the structural basis of functional dynamics. This is a major advantage over X-ray crystallography, where the crystal lattice typically selects for a single conformation, and heterogeneity smears out the electron density."

- question: "Explain the problem of preferred orientation in cryo-EM and why it limits the achievable resolution."
  type: short-answer
  answer: "Single-particle reconstruction requires views of the molecule from many different orientations to reconstruct the full 3D structure — analogous to how CT scanning requires X-ray projections from many angles. If particles preferentially adsorb to the ice-air interface in one orientation (preferred orientation), the dataset lacks views from certain directions. The missing orientations create an 'angular gap' in Fourier space, producing an anisotropic reconstruction that is well-resolved in some directions but smeared in others (like a CT scan with missing projections). Severe preferred orientation can prevent structure determination entirely. Solutions include tilting the grid during data collection, using different grid surfaces, adding surfactants, or engineering the protein with asymmetric features."
  explanation: "Preferred orientation is one of the most common practical problems in cryo-EM. Many proteins have a flat face that preferentially sits on the ice surface, producing mostly 'top views' with few 'side views.' The problem is exacerbated on thin ice films, where both surfaces constrain particle orientation."
```

## Explainer

A single cryo-EM micrograph contains thousands of individual protein molecules, each frozen in a random orientation, embedded in noisy vitreous ice. Each particle image is a 2D projection of the 3D molecule viewed from whatever angle the particle happened to be at when it was frozen. The challenge of single-particle analysis is to take these millions of noisy, randomly oriented 2D snapshots and reconstruct the 3D structure of the molecule.

The pipeline begins with **particle picking** — automated algorithms (often using neural networks trained on manually selected examples) scan micrographs and identify locations where individual protein particles are located, extracting small image windows centered on each particle. Next, **2D classification** groups particles with similar views, aligns them, and averages within each class. This serves two purposes: it verifies particle quality (classes should show recognizable molecular features) and removes junk (ice contamination, aggregates, denatured particles that do not classify into sensible averages).

The core of the reconstruction is **orientation determination** — figuring out the three Euler angles (the viewing direction) for each particle. Early methods used common-lines algorithms (each pair of 2D projections of the same 3D object shares a common one-dimensional line). Modern methods use **maximum-likelihood approaches** (implemented in RELION and cryoSPARC) that do not assign a single orientation to each particle but instead compute the probability of each particle having each possible orientation, weighting contributions accordingly. This probabilistic approach is more robust to noise. Once orientations are assigned, particles are combined into a 3D reconstruction using Fourier inversion — essentially filling in a 3D Fourier volume with the 2D Fourier transforms of each particle at their determined orientations, then inverting to real-space density.

**3D classification** extends the method to heterogeneous samples. If the molecule exists in multiple conformational states, forcing all particles into a single 3D reconstruction produces a blurred average. Classification algorithms assign each particle to one of K conformational classes (K is specified by the user or determined automatically), producing separate 3D maps for each class. This capability is uniquely powerful — it reveals the structural basis of functional dynamics from a single frozen sample. A ribosome dataset might yield separate maps for initiation, elongation, and termination states; a membrane channel might show open, closed, and desensitized conformations. Combined with time-resolved experiments (mixing reactants and freezing at defined time points), 3D classification can capture the complete conformational trajectory of a molecular machine in action.
