---
id: cosmic-microwave-background-observations
title: Cosmic Microwave Background Radiation
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: cosmological-redshift-and-hubble-law
  type: soft
- id: blackbody-radiation
  type: soft
- id: atomic-orbitals
  type: soft
- id: electromagnetic-spectrum
  type: soft
- id: electromagnetic-waves
  type: soft
- id: cosmic-inflation-and-early-universe
  type: soft
- id: cosmic-distance-ladder-calibration
  type: soft
tags:
- cosmology
- cmb
- early-universe
stage: advanced
status: validated
---
# Cosmic Microwave Background Radiation

## Core Idea
The cosmic microwave background is the thermal radiation pervading the universe, emitted when the universe became transparent approximately 380,000 years after the Big Bang. Its blackbody spectrum (~2.7 K) and tiny temperature fluctuations (~10^-5 K on degree scales) encode fundamental information about the early universe's composition (baryon and photon densities), geometry (curvature), and the growth of structure. CMB observations have profoundly constrained modern cosmology, revealing a flat, dark-energy-dominated universe.

## Questions

```yaml
- question: "The CMB temperature fluctuations are about 1 part in 100,000. What is the primary scientific significance of these fluctuations?"
  type: multiple-choice
  options:
    - "They represent measurement noise from CMB detectors and limit the precision of cosmological parameter estimates"
    - "They are the seeds of all cosmic structure — density variations that gravity later amplified into galaxies, galaxy clusters, and the large-scale cosmic web"
    - "They encode information about the composition of dark matter particles, which slightly heat certain regions of the early universe"
    - "They demonstrate that the Big Bang was not a perfectly uniform event, but rather that the universe began in a highly chaotic state"
  answer: 1
  explanation: "The tiny temperature fluctuations in the CMB are not a problem to be corrected — they are the most scientifically rich feature of the data. These fluctuations reflect slight density variations in the early universe: regions that were fractionally denser than average compressed their gas, heating it slightly; underdense regions cooled slightly. These density seeds, imprinted at recombination, were amplified by gravity over 13+ billion years into every galaxy, galaxy cluster, and filament we observe today. The detailed pattern of fluctuations — mapped by COBE, WMAP, and Planck — directly encodes the universe's composition and geometry."

- question: "Why did the universe suddenly become transparent at recombination (~380,000 years after the Big Bang), releasing the photons we now observe as the CMB?"
  type: multiple-choice
  options:
    - "The universe expanded enough that photons no longer had sufficient energy to ionize hydrogen atoms, so they stopped being absorbed"
    - "Free electrons combined with protons to form neutral hydrogen atoms, which scatter photons far less efficiently than free electrons, allowing photons to travel freely"
    - "The universe cooled below the temperature at which photons are created, so existing photons stopped being replaced and could begin propagating"
    - "Dark energy began dominating the universe's energy budget, causing photons to decouple from matter through an unknown mechanism"
  answer: 1
  explanation: "Before recombination, the universe was a hot plasma of free protons and electrons. Free electrons scatter photons extremely efficiently (Thomson scattering), making the universe opaque — like a dense fog. As the universe cooled below ~3,000 K, protons and electrons combined to form neutral hydrogen atoms. Neutral atoms scatter photons far less efficiently than free electrons, so the universe became suddenly transparent. The photons that were scattering at that moment were released and have been traveling freely ever since, redshifting from ~3,000 K to the ~2.725 K we observe today as the universe expanded by a factor of ~1,100."

- question: "The tiny temperature variations in the CMB (~10⁻⁵ K) are considered measurement noise that obscures the underlying blackbody signal and must be filtered out before useful cosmological data can be extracted."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. The nearly perfect blackbody spectrum of the CMB is the baseline signal, and the tiny fluctuations superimposed on it are the most scientifically valuable data in all of observational cosmology. Missions like WMAP and Planck were designed specifically to measure these fluctuations with high precision. The angular power spectrum of the fluctuations encodes the baryon density, dark matter density, dark energy content, geometry, and expansion history of the universe. Filtering them out would discard the data that transformed cosmology into a precision science."

- question: "The CMB photons we observe today were emitted when the universe was approximately 380,000 years old and have been traveling through space ever since, redshifting from ~3,000 K to ~2.7 K as the universe expanded."
  type: true-false
  answer: true
  explanation: "This is correct. Recombination occurred ~380,000 years after the Big Bang when the universe cooled enough for neutral hydrogen to form, releasing the photons that had been trapped in the plasma. These photons have been propagating freely since then. As the universe expanded by a factor of ~1,100, the photons' wavelengths stretched proportionally (cosmological redshift), cooling the radiation from ~3,000 K to 2.725 K. The CMB is a snapshot of the universe at that early epoch, and the expansion factor is directly encoded in the temperature ratio: 3000/2.725 ≈ 1100."

- question: "What is the 'surface of last scattering,' and why does the CMB give us a snapshot of the universe at that specific moment rather than at earlier or later times?"
  type: short-answer
  answer: "The surface of last scattering is the epoch of recombination (~380,000 years after the Big Bang) when the universe transitioned from opaque to transparent. Before this moment, photons were constantly scattering off free electrons, carrying no coherent directional information — the universe was like a fog, and we cannot see 'through' it. After recombination, photons traveled freely without further scattering. The CMB photons we detect today are precisely the photons that last scattered at this surface, so they carry the imprint of temperature and density variations at that exact moment. Earlier epochs are inaccessible to photon-based observations; later epochs are transparent and show us ordinary light from galaxies and quasars."
  explanation: "This is why the CMB is the earliest direct observational evidence of the universe's large-scale structure. It represents a physical horizon in our ability to observe: before recombination, the universe was opaque to electromagnetic radiation, creating a wall beyond which photon-based telescopes cannot see."
```

## Explainer

From your understanding of blackbody radiation, you know that any object in thermal equilibrium emits a characteristic spectrum determined solely by its temperature. The **cosmic microwave background** (CMB) is a blackbody spectrum with a temperature of approximately 2.725 K — the thermal afterglow of the entire early universe, now cooled and redshifted into the microwave band. It is the most perfect blackbody ever observed, with deviations from the ideal spectrum smaller than one part in 10,000.

The CMB originated at a specific moment in cosmic history called **recombination**, about 380,000 years after the Big Bang. Before this, the universe was a hot, dense plasma of protons, electrons, and photons. The free electrons scattered photons constantly, making the universe opaque — like being inside a dense fog. As the universe expanded and cooled below roughly 3,000 K, electrons combined with protons to form neutral hydrogen atoms (this is where your knowledge of atomic orbitals connects). Neutral atoms do not scatter photons nearly as efficiently, so the universe suddenly became transparent. The photons released at that moment have been traveling freely ever since, stretching with the expansion of the universe. From Hubble's law and cosmological redshift, you can understand why radiation originally emitted at ~3,000 K now appears at ~2.7 K: the universe has expanded by a factor of about 1,100 since recombination.

The CMB is almost perfectly uniform across the sky, but not quite. Tiny temperature fluctuations of about 1 part in 100,000 are imprinted on it, and these are extraordinarily informative. They represent slight density variations in the early universe — regions that were a bit denser or a bit less dense than average. The denser regions had slightly stronger gravitational attraction, which compressed the gas and heated it, while underdense regions cooled slightly. These fluctuations are the seeds of all structure in the universe: over billions of years, gravity amplified the denser regions into the galaxies, galaxy clusters, and cosmic filaments we observe today.

By mapping these fluctuations in detail — as missions like COBE, WMAP, and Planck have done with increasing precision — cosmologists can extract the fundamental parameters of the universe. The angular size of the fluctuation pattern reveals the universe's geometry (it is flat to within measurement precision). The relative heights of peaks in the fluctuation power spectrum encode the ratio of ordinary matter to dark matter to dark energy, the overall density, and the rate of expansion. The CMB is, in effect, a snapshot of the universe at an age of 380,000 years, and reading it has transformed cosmology from a speculative field into a precision science.
