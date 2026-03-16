---
id: x-ray-diffraction-materials
title: X-Ray Diffraction and Crystal Identification
domain: engineering
course: materials-science
prerequisites:
- id: miller-indices
  type: hard
- id: wave-interference
  type: hard
- id: diffraction-gratings
  type: soft
tags:
- XRD
- bragg-law
- diffraction
- crystal-identification
- lattice-parameter
stage: formal-systems
status: validated
---

# X-Ray Diffraction and Crystal Identification

## Core Idea
X-ray diffraction (XRD) exploits constructive interference of X-rays scattered by periodic crystal planes to determine crystal structure. Bragg's law (nλ = 2d sinθ) relates the X-ray wavelength, the interplanar spacing d (determined by Miller indices and lattice parameter), and the diffraction angle θ. An XRD pattern — peaks at specific 2θ angles with characteristic relative intensities — serves as a fingerprint for phase identification, lattice parameter measurement, and residual stress analysis. XRD is the primary technique for confirming the crystal structure of new materials and for monitoring phase transformations in heat-treated alloys.

## How It's Best Learned
Apply Bragg's law to calculate the expected 2θ angles for the first three peaks of an FCC metal (e.g., copper) and compare to a measured diffractogram. Use systematic absences (structure factor rules) to explain why certain reflections are missing.

## Common Misconceptions
- Bragg's law gives a necessary condition for diffraction but not a sufficient one — the structure factor (from the atomic arrangement within the unit cell) can extinguish peaks that geometry predicts.
- XRD measures average long-range structure; amorphous materials and very small crystallites produce broad, diffuse patterns rather than sharp peaks.

## Explainer

From wave interference, you know that two waves reinforce when their path length difference is an integer number of wavelengths, and cancel when it is a half-integer. From diffraction gratings, you know that a periodic array of scatterers produces sharp peaks at angles determined by the grating spacing and wavelength. X-ray diffraction applies exactly this physics to crystals: the periodic rows of atoms in a crystal act as a three-dimensional diffraction grating, and X-rays of wavelength ~0.1 nm (comparable to atomic spacings) diffract at angles that reveal the crystal geometry. **Bragg's law** nλ = 2d·sinθ is the condition for constructive interference from parallel planes of atoms separated by spacing d: the path length difference for rays reflecting from adjacent planes is 2d·sinθ, and this must equal an integer number of wavelengths λ.

To use Bragg's law, you need the **d-spacing** for each family of planes, which you can calculate from Miller indices. For a cubic crystal with lattice parameter a: d_hkl = a / √(h² + k² + l²). The {100} planes have d = a, the {110} planes have d = a/√2, the {111} planes have d = a/√3, and so on. Each family diffracts at a different 2θ angle, generating a distinct peak in the XRD pattern. The peaks at lower 2θ angles correspond to larger d-spacings (more widely separated planes). By measuring peak positions, you invert Bragg's law to extract d-spacings, then use multiple planes to calculate the lattice parameter a with high precision — a standard technique for monitoring alloy composition and thermal expansion.

Not all geometrically possible planes produce observable peaks. The **structure factor** accounts for interference between waves scattered by different atoms within the same unit cell. For FCC metals, planes with mixed h, k, l indices (like {100} and {110}) scatter with destructive interference between the face atoms and corner atoms — these peaks are **systematically absent**. Only reflections with all-odd or all-even Miller indices survive: {111}, {200}, {220}, {311}, ... This is why an FCC diffractogram looks different from a BCC diffractogram even if both have the same lattice parameter. The pattern of present and absent peaks is a fingerprint that identifies the crystal structure before you even measure peak positions.

The power of XRD as a characterization tool extends beyond simple structure identification. **Residual stress** shifts peak positions from their stress-free values — compressive stress shifts peaks to higher 2θ (smaller d-spacing), tensile stress to lower 2θ. **Crystallite size** broadens peaks: the Scherrer equation L = Kλ/(β·cosθ) relates peak width β to crystallite dimension L, explaining why nanocrystalline materials produce broad humps rather than sharp lines. **Phase transformations** change the XRD pattern in characteristic ways — the face-centered cubic → body-centered cubic transformation in steel replaces the FCC peak set with the BCC peak set, providing a non-destructive diagnostic of heat treatment state. In any laboratory studying a new solid-state material, XRD is almost always the first characterization tool used, because it answers the most basic question — what phase is actually present — before any other technique is applied.


