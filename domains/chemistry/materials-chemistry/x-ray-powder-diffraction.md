---
id: x-ray-powder-diffraction
title: X-Ray Powder Diffraction
domain: chemistry
course: materials-chemistry
prerequisites:
- id: crystal-structures-and-unit-cells
  type: hard
- id: crystal-symmetry-and-space-groups
  type: hard
builds-toward:
- characterization-methods-tem-sem-xps
tags:
- XRD
- Bragg's law
- diffraction
- phase identification
- Rietveld refinement
stage: advanced
status: validated
---

# X-Ray Powder Diffraction

## Core Idea
X-ray powder diffraction (XRPD) is the primary technique for identifying crystalline phases and determining crystal structures from polycrystalline samples. When monochromatic X-rays strike a powdered crystalline sample, they diffract from lattice planes according to Bragg's law: n-lambda = 2d sin(theta). Because a powder contains crystallites in all orientations, every set of lattice planes simultaneously satisfies the Bragg condition at its characteristic angle, producing a unique pattern of peak positions and intensities. Peak positions reveal the unit cell dimensions; peak intensities encode the atomic arrangement; peak shapes carry information about crystallite size and strain.

## Questions

```yaml
- question: "A powder diffraction pattern shows peaks at 2-theta values of 38.2, 44.4, 64.5, and 77.5 degrees using Cu K-alpha radiation. These peak positions are consistent with which crystal structure?"
  type: multiple-choice
  options:
    - "Simple cubic — all hkl reflections are allowed"
    - "Body-centered cubic — only reflections where h+k+l is even are allowed"
    - "Face-centered cubic — only reflections where h,k,l are all odd or all even are allowed"
    - "Hexagonal close-packed — peak positions follow no simple selection rule"
  answer: 2
  explanation: "The ratios of sin^2(theta) for these peaks follow the sequence 3:4:8:11, which corresponds to the FCC allowed reflections (111), (200), (220), (311). In FCC, only planes where h,k,l are all odd or all even produce diffraction — the face-centering causes systematic absences for mixed indices. This pattern matches aluminum (a = 4.05 Angstroms). The ability to distinguish BCC from FCC from the pattern of present and absent reflections is one of the most basic applications of XRPD."

- question: "The width of a diffraction peak increases as crystallite size decreases, according to the Scherrer equation."
  type: true-false
  answer: true
  explanation: "The Scherrer equation relates peak broadening to crystallite size: t = K-lambda / (B cos(theta)), where t is crystallite size, B is the peak width at half maximum (in radians), and K is a shape factor near 0.9. Smaller crystallites have fewer lattice planes contributing to diffraction, which reduces the destructive interference that would otherwise sharpen the peak. Below about 100 nm, broadening becomes measurable; below 5 nm, peaks may be so broad they merge into the background. This makes peak width analysis a routine method for estimating nanoparticle size."

- question: "Why does a powder sample produce a complete diffraction pattern while a single crystal at a fixed orientation typically shows only a few reflections?"
  type: short-answer
  answer: "A powder contains millions of tiny crystallites oriented randomly in all directions. For every set of lattice planes (hkl), some crystallites will be oriented at exactly the Bragg angle relative to the incident beam. This means all allowed reflections are observed simultaneously. A single crystal has only one orientation, so only the few planes that happen to satisfy Bragg's law at that orientation will diffract. To get a complete pattern from a single crystal, you must rotate it through many orientations."
  explanation: "This is the fundamental advantage of powder diffraction for routine phase identification — no special sample preparation or orientation is needed. The disadvantage is that 3D structural information is compressed into a 1D pattern (intensity vs. 2-theta), which causes peak overlap and makes structure solution harder than with single-crystal data. Rietveld refinement addresses this by fitting the entire pattern simultaneously using a structural model, extracting maximum information from the overlapping peaks."
```

## Explainer

X-ray diffraction is the most important technique in materials chemistry for answering the question: what crystalline phases are present, and what are their structures? The physical basis is straightforward — X-rays have wavelengths comparable to interatomic distances (about 1.5 Angstroms for Cu K-alpha radiation), so they diffract from the regularly spaced planes of atoms in a crystal. **Bragg's law** gives the condition for constructive interference: the path difference between X-rays reflecting from adjacent planes must equal a whole number of wavelengths.

In a powder diffraction experiment, the sample is a finely ground polycrystalline material. The random orientation of crystallites ensures that for every set of lattice planes, some fraction of crystallites will satisfy the Bragg condition. The detector sweeps through angles, recording intensity as a function of 2-theta. The resulting pattern — a series of peaks at specific angles with specific intensities — is a fingerprint of the crystal structure. Phase identification works by matching the observed pattern against a database (the ICDD Powder Diffraction File contains over 400,000 reference patterns). If your pattern matches entry number 04-0787, your sample contains aluminum.

Beyond identification, XRPD provides quantitative structural information. The **peak positions** are determined by the unit cell dimensions through Bragg's law and the Miller index relation for d-spacings. By fitting peak positions, you extract the lattice parameters a, b, c, alpha, beta, gamma with high precision. The **peak intensities** depend on which atoms are at which positions within the unit cell — heavy atoms scatter X-rays more strongly, and the relative intensity of different reflections encodes the atomic arrangement. **Rietveld refinement** fits a complete structural model (atom types, positions, thermal parameters) to the entire diffraction pattern simultaneously, refining all parameters to minimize the difference between observed and calculated patterns. This method has become the standard approach for structure determination and refinement from powder data.

Peak shapes carry additional information. Broadening beyond the instrumental resolution arises from two main sources: small crystallite size (Scherrer broadening) and microstrain (non-uniform lattice distortions). These can be separated by their different angular dependences. For nanomaterials, where crystallite sizes are below 100 nm, peak broadening analysis is often the quickest way to estimate particle size. For engineering materials, strain broadening reveals residual stresses from processing. The combination of phase identification, structure refinement, and microstructural analysis makes XRPD an indispensable tool across all of materials chemistry.
