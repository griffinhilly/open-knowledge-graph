---
id: xray-diffraction-structure-determination
title: X-ray Diffraction and Structure Determination
domain: physics
course: condensed-matter-physics
prerequisites:
- id: reciprocal-lattice-brillouin-zones
  type: hard
- id: maxwell-equations-differential-form
  type: soft
tags:
- x-ray-diffraction
- bragg-law
- structure-factor
- crystallography
stage: expert
status: validated
---

# X-ray Diffraction and Structure Determination

## Core Idea
X-ray diffraction is the primary experimental technique for determining crystal structures. When X-rays (wavelength comparable to atomic spacings, ~1 Angstrom) scatter from a crystal, constructive interference occurs only when the Bragg condition 2d sin(theta) = n*lambda is satisfied, or equivalently when the scattering vector equals a reciprocal lattice vector (von Laue condition). The intensity of each diffraction peak is proportional to |F(G)|^2, where F(G) is the structure factor — the Fourier transform of the electron density within one unit cell. Systematic absences in the structure factor reveal the lattice type and basis arrangement.

## Questions

```yaml
- question: "The Bragg condition 2d sin(θ) = nλ and the von Laue condition Δk = G are two different ways of expressing the same physics. What connects them?"
  type: multiple-choice
  options:
    - "They are independent conditions that must both be satisfied simultaneously"
    - "The Bragg condition applies to X-rays while the von Laue condition applies to electrons"
    - "The Bragg condition describes reflection from lattice planes with spacing d, and the perpendicular distance between planes is d = 2π/|G|, so both conditions reduce to the requirement that the path difference equals an integer number of wavelengths"
    - "The von Laue condition is an approximation to the Bragg condition valid only at small angles"
  answer: 2
  explanation: "The Bragg picture treats the crystal as a stack of reflecting planes separated by distance d. The von Laue picture describes scattering from individual atoms with constructive interference when Δk = G. They are exactly equivalent: the reciprocal lattice vector G is perpendicular to the (hkl) planes with |G| = 2π/d, and substituting into either condition gives the same constraint on wavelength and angle. The von Laue formulation is more general and directly connects to the reciprocal lattice framework."

- question: "In a BCC crystal, X-ray diffraction peaks with h + k + l = odd are systematically absent. What causes these extinctions?"
  type: multiple-choice
  options:
    - "The X-ray wavelength is too long to resolve those planes"
    - "The structure factor F(G) vanishes for those reflections because scattering from the body-center atom destructively interferes with scattering from the corner atoms"
    - "Those Miller indices correspond to imaginary lattice planes"
    - "Thermal vibrations suppress those reflections at room temperature"
  answer: 1
  explanation: "In BCC, the basis consists of atoms at (0,0,0) and (1/2,1/2,1/2). The structure factor is F = f[1 + e^{iπ(h+k+l)}], where f is the atomic form factor. When h+k+l is odd, the exponential equals -1 and F = 0. Physically, the body-center atom scatters exactly out of phase with the corner atoms for these reflections, producing perfect destructive interference. These systematic absences are the experimental fingerprint of a BCC lattice."

- question: "The structure factor contains all the information about the arrangement of atoms within the unit cell, while the lattice determines which directions produce diffraction peaks."
  type: true-false
  answer: true
  explanation: "This is the clean separation between lattice and basis in diffraction. The reciprocal lattice (determined by the Bravais lattice) specifies which scattering vectors G can produce peaks — these are the allowed diffraction directions. The structure factor F(G), which depends on the positions and types of atoms in the basis, determines the intensity at each allowed G. Some allowed G may have F = 0 (systematic absences), effectively hiding certain peaks. Determining a crystal structure means measuring peak positions (lattice) and intensities (basis) and inverting the structure factor."

- question: "Why can't we simply inverse-Fourier-transform the measured diffraction pattern to obtain the crystal structure directly?"
  type: short-answer
  answer: "Detectors measure diffraction intensities |F(G)|^2, not the complex structure factor F(G) itself. The phase information — the argument of F(G) — is lost. Since a Fourier transform requires both amplitude and phase to reconstruct the electron density, the measured intensities alone are insufficient. This is the famous 'phase problem' of crystallography. Solving it requires indirect methods: Patterson functions (which use |F|^2 directly), direct methods (statistical relationships between phases), molecular replacement (using known similar structures), or anomalous scattering techniques."
  explanation: "The phase problem is why crystallography remained labor-intensive even after diffraction was well understood. The 1985 Nobel Prize in Chemistry was awarded for 'direct methods' that use probability relationships among structure factor phases to solve the problem computationally."
```

## Explainer

X-ray diffraction is the experimental backbone of crystallography and condensed matter physics. The technique works because X-ray wavelengths (~0.5-2 Angstroms) are comparable to interatomic spacings in crystals, so crystals act as natural diffraction gratings. When a beam of X-rays hits a crystal, most of it passes through, but at specific angles the scattered waves from different atoms interfere constructively and produce sharp intensity peaks — the diffraction pattern. Each peak corresponds to scattering from a family of lattice planes.

The condition for constructive interference can be expressed two equivalent ways. **Bragg's law** — 2d sin(theta) = n*lambda — treats the crystal as a stack of partially reflecting planes separated by distance d and requires the path difference between reflections from successive planes to be an integer number of wavelengths. The **von Laue condition** — Delta k = G — requires the change in wavevector to equal a reciprocal lattice vector. Both encode the same physics: the periodicity of the lattice selects discrete scattering directions. The von Laue picture is more powerful because it connects directly to the reciprocal lattice and works naturally in three dimensions.

The intensities of the diffraction peaks carry information about what sits at each lattice point. This information is encoded in the **structure factor** F(G) = sum_j f_j e^{iG · r_j}, where the sum runs over all atoms j in the unit cell at positions r_j, and f_j is the atomic form factor (the Fourier transform of each atom's electron density). The measured intensity at each reciprocal lattice point is I proportional to |F(G)|^2. Some reflections may have F = 0 even though G is a valid reciprocal lattice vector — these **systematic absences** are diagnostic. For example, FCC lattices show peaks only when h, k, l are all even or all odd, and BCC lattices show peaks only when h + k + l is even. These selection rules immediately distinguish lattice types from the diffraction pattern.

The major challenge in structure determination is the **phase problem**: detectors record |F(G)|^2, losing the complex phase of F(G). Since reconstructing the electron density via inverse Fourier transform requires the full complex F(G), the phase must be recovered by indirect methods. Modern techniques including direct methods, anomalous dispersion, and computational refinement have made structure determination routine for many materials, but the phase problem remains a fundamental limitation. Beyond X-rays, electron diffraction and neutron diffraction complement the technique — electrons are sensitive to electrostatic potential and work well for thin films, while neutrons scatter from nuclei and magnetic moments, providing information invisible to X-rays.
