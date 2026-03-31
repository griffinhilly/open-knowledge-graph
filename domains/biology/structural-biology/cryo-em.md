---
id: cryo-em
title: Cryo-EM
domain: biology
course: structural-biology
prerequisites:
- id: protein-folding-and-stability
  type: hard
- id: diffraction-and-fourier-transforms
  type: soft
builds-toward:
- single-particle-analysis
- cryo-et
- macromolecular-assemblies
tags:
- cryo-EM
- electron-microscopy
- vitrification
- resolution-revolution
- near-atomic-resolution
stage: expert
status: validated
---
# Cryo-EM

## Core Idea
Cryo-electron microscopy (cryo-EM) determines the structures of biological macromolecules by imaging individual particles flash-frozen in vitreous (non-crystalline) ice using an electron microscope. Unlike X-ray crystallography, cryo-EM does not require crystals — purified protein in solution is applied to a grid, blotted to a thin film, and rapidly plunged into liquid ethane to trap molecules in their native, hydrated state. The "resolution revolution" (enabled by direct electron detectors and improved image processing algorithms since ~2013) has transformed cryo-EM from a low-resolution technique into a method capable of near-atomic resolution (2-4 Angstroms) for many biological complexes, earning Jacques Dubochet, Joachim Frank, and Richard Henderson the 2017 Nobel Prize.

## Questions

```yaml
- question: "Why was the development of direct electron detectors critical for the cryo-EM resolution revolution?"
  type: multiple-choice
  options:
    - "Direct detectors eliminated the need for electron beams"
    - "Direct detectors have dramatically higher detective quantum efficiency (DQE) than previous film or CCD cameras, capturing more of the signal from each electron. Combined with fast frame rates that enable correction for beam-induced motion during exposure, they transformed the signal-to-noise ratio achievable from radiation-sensitive biological specimens"
    - "Direct detectors produce larger images, which are easier to analyze"
    - "Direct detectors cooled the specimen to prevent ice crystallization"
  answer: 1
  explanation: "Biological specimens are exquisitely radiation-sensitive — they are destroyed by the electron beam needed to image them, limiting the total electron dose. Previous detectors (film, CCD cameras) lost much of the signal (low DQE), wasting the precious electrons that could be used before the specimen is destroyed. Direct electron detectors capture electron events with much higher efficiency (DQE 2-3x higher) and at frame rates (40-400 fps) that enable correction for beam-induced sample movement during exposure. These two improvements — capturing more signal per electron and correcting for motion blur — drove resolution from ~10 Angstroms to 2-4 Angstroms for many biological complexes."

- question: "Cryo-EM can determine structures of any protein, regardless of size, with equal ease."
  type: true-false
  answer: false
  explanation: "Cryo-EM faces a practical size limit: smaller proteins (<100 kDa) have weaker image contrast relative to the ice background, making particle alignment (determining each particle's orientation) difficult or impossible with conventional methods. Most successful cryo-EM structures are of complexes >150 kDa. Strategies for smaller proteins include fusing them to larger scaffolds (Fab fragments, nanobodies), forming complexes with binding partners, or using recently developed methods like phase-plate cryo-EM that enhance contrast. The upper size limit is less restrictive — cryo-EM excels at large complexes (ribosomes, proteasomes, virus capsids) that are difficult to crystallize, which is one of its major advantages over X-ray crystallography."

- question: "What is vitrification and why is it essential for cryo-EM specimen preparation?"
  type: short-answer
  answer: "Vitrification is the rapid cooling of an aqueous sample to produce vitreous (amorphous, glassy) ice rather than crystalline ice. The sample is plunge-frozen into liquid ethane (at ~-180C) at a rate fast enough (~10^6 degrees/second) that water molecules do not have time to arrange into an ice crystal lattice. This is essential because crystalline ice would damage the protein structure, create strong diffraction that overwhelms the weak protein signal, and potentially denature the sample. Vitreous ice preserves the protein in its native, hydrated state — the molecule is essentially flash-frozen in solution, trapped in the same conformation and environment it occupied at the moment of freezing."
  explanation: "Vitrification was developed by Jacques Dubochet in the 1980s and was one of the three key innovations (along with image processing by Joachim Frank and the demonstration of atomic-resolution EM by Richard Henderson) recognized by the 2017 Nobel Prize. The thickness and quality of the vitreous ice film critically affect data quality — too thick increases background noise, too thin causes preferred orientation problems."
```

## Explainer

For most of structural biology's history, determining a protein structure meant growing crystals. Cryo-EM has changed this fundamental constraint. By imaging individual protein molecules frozen in a thin layer of vitreous ice, cryo-EM determines structures without crystals — directly from purified protein in solution. This eliminates the crystallization bottleneck that has frustrated structural biologists for decades and opens the door to structures of flexible complexes, heterogeneous samples, and membrane proteins in lipid environments that resist crystallization.

The specimen preparation is conceptually simple but technically demanding. A few microliters of purified protein (at 0.5-5 mg/mL) are applied to a thin carbon or gold grid with tiny holes. Most of the solution is blotted away, leaving a thin film (~30-100 nm) of protein solution spanning the holes. The grid is then **plunge-frozen** into liquid ethane, cooling it so rapidly that water vitrifies (forms amorphous glass) rather than crystallizing. The frozen grid is kept at liquid nitrogen temperature throughout imaging to prevent ice crystallization and to protect the radiation-sensitive specimen.

In the electron microscope, the frozen specimen is imaged at low electron dose (to minimize radiation damage) using a 200-300 kV electron beam. Each image captures thousands of individual protein particles in random orientations, frozen mid-tumble. The images are noisy — each particle is imaged with very few electrons to limit damage — but computational processing extracts the signal. **Image processing** (the intellectual contribution of Joachim Frank) involves: identifying and extracting individual particle images from the micrographs, classifying them by orientation and conformation (2D classification), determining the 3D orientation of each particle (orientation determination), and averaging many particles in the same orientation to produce a high-signal 3D reconstruction. Hundreds of thousands to millions of particle images are typically needed for a near-atomic resolution reconstruction.

The **resolution revolution** since ~2013 transformed cryo-EM from a niche technique producing blobby shapes into a mainstream structural method producing maps at 2-4 Angstrom resolution — sometimes rivaling crystallography. Three technological advances drove this: **direct electron detectors** (higher sensitivity, faster readout enabling motion correction), **improved algorithms** (maximum-likelihood approaches, GPU-accelerated processing), and **better specimen preparation** (thinner ice, better grids). Cryo-EM now accounts for the majority of new high-resolution structures of large complexes deposited in the PDB. Its advantages over crystallography — no crystals needed, ability to handle conformational heterogeneity (sorting particles into different conformational classes), and visualization of complexes in near-native conditions — make it complementary to crystallography and, for many targets, the method of first choice.
