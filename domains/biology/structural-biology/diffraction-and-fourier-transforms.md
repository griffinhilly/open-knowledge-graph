---
id: diffraction-and-fourier-transforms
title: Diffraction and Fourier Transforms
domain: biology
course: structural-biology
prerequisites:
- id: electromagnetic-waves
  type: soft
- id: fourier-series-intro
  type: soft
builds-toward:
- x-ray-crystallography
- structure-solution-methods
tags:
- diffraction
- Fourier-transform
- Bragg-law
- reciprocal-space
- phase-problem
stage: expert
status: validated
---
# Diffraction and Fourier Transforms

## Core Idea
When X-rays interact with a crystal, the regularly spaced atoms scatter the radiation, and the scattered waves interfere constructively only in specific directions determined by Bragg's law (n-lambda = 2d sin-theta), producing a discrete pattern of diffraction spots. Each spot corresponds to a Fourier component of the crystal's electron density — its intensity gives the amplitude, but the phase is lost during measurement. The electron density is the inverse Fourier transform of the structure factors (complex numbers with amplitude and phase for each reflection). Understanding this Fourier relationship between real space (electron density) and reciprocal space (diffraction pattern) is essential for every step of crystallographic structure determination, from data processing to model building.

## Questions

```yaml
- question: "Bragg's law (n-lambda = 2d sin-theta) relates the angle of diffraction to the spacing of lattice planes in the crystal. If a crystal with larger unit cell dimensions is analyzed, how does the diffraction pattern change?"
  type: multiple-choice
  options:
    - "Fewer reflections are observed because larger cells diffract less"
    - "The diffraction spots are more closely spaced — larger real-space dimensions correspond to finer sampling in reciprocal space, producing more reflections within the same angular range"
    - "The diffraction spots move farther apart because larger cells scatter at larger angles"
    - "The diffraction pattern is unchanged because unit cell size does not affect diffraction"
  answer: 1
  explanation: "This is the reciprocal relationship: large in real space = small in reciprocal space. A crystal with a larger unit cell has more closely spaced lattice planes (more d-values), which according to Bragg's law diffract at more closely spaced angles. The result is more diffraction spots within any given angular range, which means more data (more Fourier components) and ultimately a more finely sampled electron density map. This is why large macromolecular crystals (with unit cells of 50-200 Angstroms) produce many more reflections than small-molecule crystals, but each reflection is weaker because the scattering power is distributed among more spots."

- question: "The phase of each diffraction spot carries more information about the structure than the amplitude."
  type: true-false
  answer: true
  explanation: "This seemingly surprising statement has been demonstrated mathematically and computationally. If you compute an electron density map using the phases from protein A and the amplitudes from protein B, the resulting map looks like protein A — not protein B. Phases determine the overall features of the electron density (the positions of atoms and molecules), while amplitudes modulate the contrast and fine detail. This is why the phase problem is so critical: losing the phases loses most of the structural information. It also explains why approximate phases (from molecular replacement or initial experimental phasing) are often sufficient to produce interpretable electron density maps that can be improved by iterative refinement."

- question: "Explain in simple terms why the electron density and the diffraction pattern are related by a Fourier transform."
  type: short-answer
  answer: "The electron density in a crystal is a periodic function (it repeats with the unit cell). Any periodic function can be decomposed into a sum of sine and cosine waves of different frequencies, amplitudes, and phases — this decomposition is the Fourier series. Each diffraction spot corresponds to one of these component waves: its position in the pattern gives the frequency (the spacing of the corresponding set of lattice planes), its intensity gives the amplitude squared, and its phase (unmeasured) gives the phase of that wave component. The electron density is reconstructed by summing all these waves (inverse Fourier transform). Each reflection adds one wave to the sum, and the more reflections included (higher resolution), the sharper and more detailed the resulting electron density map."
  explanation: "An intuitive analogy: the diffraction pattern is the 'frequency spectrum' of the electron density, just as an audio spectrum shows the frequency components of a sound wave. To reconstruct the sound (electron density), you need both the amplitude and phase of each frequency component (reflection). Crystallography gives you the amplitudes but not the phases — hence the phase problem."
```

## Explainer

The physical basis of X-ray crystallography is the interaction between electromagnetic radiation and matter, and the mathematical framework that connects the experiment to the structure is the **Fourier transform**. Understanding this relationship — between what you measure (the diffraction pattern) and what you want to know (the electron density) — is the intellectual core of crystallography.

When an X-ray beam hits a crystal, each atom scatters the radiation in all directions. In a crystal, atoms are arranged in a regular, repeating lattice. The scattered waves from different atoms interfere with each other — constructively in some directions (producing bright diffraction spots) and destructively in others (producing darkness between spots). **Bragg's law** (n-lambda = 2d-sin-theta) specifies the directions of constructive interference: for a given set of parallel lattice planes with spacing d, constructive interference occurs at an angle theta where the path difference between waves scattered from adjacent planes is an integer multiple of the wavelength. Each family of lattice planes in the crystal produces a diffraction spot at a specific angle.

The key insight is that the diffraction pattern and the electron density are related by a **Fourier transform** — a mathematical operation that decomposes any function into its component frequencies. The electron density in a crystal is periodic (it repeats with the unit cell), so it can be expressed as a Fourier series — a sum of waves with specific frequencies, amplitudes, and phases. Each diffraction spot corresponds to one term in this series: its position tells you the frequency (which lattice planes it corresponds to), its measured intensity tells you the amplitude (specifically, intensity = amplitude squared), and its phase (which is NOT measured) tells you the relative timing of that wave component.

The **phase problem** arises because X-ray detectors record only photon counts (intensities), not the phase of the electromagnetic wave at each detector position. Both amplitude and phase are needed to perform the inverse Fourier transform that yields the electron density map. Remarkably, the phases carry more structural information than the amplitudes — computations using correct phases but wrong amplitudes produce better maps than correct amplitudes with wrong phases. This is why phase determination (by molecular replacement, isomorphous replacement, or anomalous dispersion) is the critical step. Once approximate phases are obtained, the electron density map reveals the molecular structure, and iterative refinement improves both the atomic model and the phases until the calculated diffraction pattern matches the observed pattern to within experimental error.
