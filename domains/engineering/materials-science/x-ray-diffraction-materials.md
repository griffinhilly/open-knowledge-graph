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
- id: crystal-systems-and-bravais-lattices
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

## Questions

```yaml
- question: "An XRD scan of copper (FCC crystal structure) produces no peak at the 2θ position predicted by Bragg's law for the {100} planes. The most accurate explanation is:"
  type: multiple-choice
  options:
    - "The X-ray wavelength is too long to satisfy Bragg's law for the large {100} d-spacing at achievable angles"
    - "Copper atoms are too light to scatter X-rays effectively from {100} planes"
    - "Destructive interference between waves scattered by corner atoms and face-center atoms in the FCC unit cell eliminates the {100} reflection — a systematic absence"
    - "The {100} reflection is present but overlaps with a stronger adjacent peak and cannot be resolved"
  answer: 2
  explanation: "Bragg's law gives a necessary condition for diffraction (correct path length difference between planes), but the structure factor determines whether waves scattered by different atoms within the same unit cell add constructively or destructively. For FCC metals, planes with mixed h, k, l Miller indices (like {100}: indices 1, 0, 0 — mixed) experience destructive interference between rays from corner atoms and face-center atoms. This systematic absence is not a measurement artifact but an intrinsic consequence of the FCC arrangement. Only planes with all-odd or all-even Miller indices ({111}, {200}, {220}, {311}…) produce peaks. This pattern of absences fingerprints the FCC structure before a single peak position is measured."

- question: "An engineer measures the XRD pattern of a shot-peened steel surface (which introduces compressive residual stress) and compares it to an unstressed reference. How will the diffraction peaks shift?"
  type: multiple-choice
  options:
    - "Peaks shift to lower 2θ (larger d-spacing), because compressive in-plane stress pushes lattice planes apart in the normal direction"
    - "Peaks shift to higher 2θ (smaller d-spacing), because compressive in-plane stress squeezes lattice planes closer together in the direction normal to the surface via the Poisson effect"
    - "Peak positions do not change; only peak widths increase with compressive residual stress"
    - "Peaks shift to lower 2θ because shot-peening increases the lattice parameter uniformly in all directions"
  answer: 1
  explanation: "Compressive residual stress in the surface plane causes the lattice to contract in the direction perpendicular to the surface via the Poisson effect — in-plane compression leads to through-thickness tension, reducing the spacing between planes parallel to the surface. XRD typically measures d-spacings of planes parallel to the surface (perpendicular to the normal direction). A smaller d-spacing means a larger sinθ by Bragg's law (nλ = 2d sinθ: smaller d → larger θ → larger 2θ). Thus compressive stress shifts peaks to higher 2θ. This is the basis for non-destructive residual stress measurement by XRD in engineering components."

- question: "The pattern of systematic absences in an XRD diffractogram can distinguish an FCC crystal from a BCC crystal of the same element, independently of the lattice parameter value."
  type: true-false
  answer: true
  explanation: "Systematic absences are determined by crystal structure type, not by lattice parameter. FCC crystals allow only reflections with all-odd or all-even Miller indices: {111}, {200}, {220}, {311}… BCC crystals allow only reflections where h+k+l is even: {110}, {200}, {211}, {220}… These different selection rules produce distinct peak patterns. FCC shows a peak at {111} but not {110}; BCC shows {110} but not {111}. By examining which peaks are present and absent, you can identify the crystal structure type before any quantitative analysis of lattice parameter. This is routinely used to identify phase transformations in steel (FCC austenite → BCC ferrite produces a completely different peak set)."

- question: "Any crystal planes that satisfy Bragg's law — for which the equation nλ = 2d sinθ has a solution at an achievable angle — will produce an observable diffraction peak."
  type: true-false
  answer: false
  explanation: "Bragg's law is a necessary but not sufficient condition for diffraction. The structure factor — which accounts for interference between waves scattered by all atoms within the unit cell — can produce complete destructive interference (systematic absence) for planes that are geometrically permitted by Bragg's law. For FCC metals, the {100} planes satisfy Bragg's law geometrically, but the structure factor is zero: face-center atoms produce waves exactly out of phase with corner atom waves, eliminating the peak. Bragg's law predicts where a peak could appear; the structure factor determines whether it actually does. This is one of the key subtleties of XRD: geometry and atomic arrangement are both required for a complete prediction."

- question: "Why do amorphous materials produce broad, diffuse XRD patterns rather than sharp peaks, and what does this reveal about the relationship between crystal order and diffraction sharpness?"
  type: short-answer
  answer: "Sharp XRD peaks arise from long-range periodic order: when thousands of identical planes are arranged periodically, their scattered X-rays add constructively only at precise Bragg angles, producing narrow peaks. Amorphous materials lack long-range periodicity — atomic positions are only correlated over a few bond lengths, not across extended crystallites. Without periodic repetition extending over many unit cells, scattered X-rays add constructively over a broad range of angles rather than at a precise angle, producing a diffuse hump. Diffraction sharpness is therefore a direct measure of long-range order: the narrower the peak, the larger the coherently scattering crystallite domain, quantified by the Scherrer equation L = Kλ/(β·cosθ)."
  explanation: "This principle has practical consequences: nanocrystalline materials with 5–10 nm crystallites produce noticeably broad peaks even though they are crystalline; truly amorphous materials have no crystallite size at all and produce only a broad background hump. XRD can therefore distinguish crystalline from amorphous phases in a mixture and estimate crystallite size from peak breadth — two capabilities that come directly from understanding the relationship between periodic order and diffraction sharpness."
```

## Explainer

From wave interference, you know that two waves reinforce when their path length difference is an integer number of wavelengths, and cancel when it is a half-integer. From diffraction gratings, you know that a periodic array of scatterers produces sharp peaks at angles determined by the grating spacing and wavelength. X-ray diffraction applies exactly this physics to crystals: the periodic rows of atoms in a crystal act as a three-dimensional diffraction grating, and X-rays of wavelength ~0.1 nm (comparable to atomic spacings) diffract at angles that reveal the crystal geometry. **Bragg's law** nλ = 2d·sinθ is the condition for constructive interference from parallel planes of atoms separated by spacing d: the path length difference for rays reflecting from adjacent planes is 2d·sinθ, and this must equal an integer number of wavelengths λ.

To use Bragg's law, you need the **d-spacing** for each family of planes, which you can calculate from Miller indices. For a cubic crystal with lattice parameter a: d_hkl = a / √(h² + k² + l²). The {100} planes have d = a, the {110} planes have d = a/√2, the {111} planes have d = a/√3, and so on. Each family diffracts at a different 2θ angle, generating a distinct peak in the XRD pattern. The peaks at lower 2θ angles correspond to larger d-spacings (more widely separated planes). By measuring peak positions, you invert Bragg's law to extract d-spacings, then use multiple planes to calculate the lattice parameter a with high precision — a standard technique for monitoring alloy composition and thermal expansion.

Not all geometrically possible planes produce observable peaks. The **structure factor** accounts for interference between waves scattered by different atoms within the same unit cell. For FCC metals, planes with mixed h, k, l indices (like {100} and {110}) scatter with destructive interference between the face atoms and corner atoms — these peaks are **systematically absent**. Only reflections with all-odd or all-even Miller indices survive: {111}, {200}, {220}, {311}, ... This is why an FCC diffractogram looks different from a BCC diffractogram even if both have the same lattice parameter. The pattern of present and absent peaks is a fingerprint that identifies the crystal structure before you even measure peak positions.

The power of XRD as a characterization tool extends beyond simple structure identification. **Residual stress** shifts peak positions from their stress-free values — compressive stress shifts peaks to higher 2θ (smaller d-spacing), tensile stress to lower 2θ. **Crystallite size** broadens peaks: the Scherrer equation L = Kλ/(β·cosθ) relates peak width β to crystallite dimension L, explaining why nanocrystalline materials produce broad humps rather than sharp lines. **Phase transformations** change the XRD pattern in characteristic ways — the face-centered cubic → body-centered cubic transformation in steel replaces the FCC peak set with the BCC peak set, providing a non-destructive diagnostic of heat treatment state. In any laboratory studying a new solid-state material, XRD is almost always the first characterization tool used, because it answers the most basic question — what phase is actually present — before any other technique is applied.


