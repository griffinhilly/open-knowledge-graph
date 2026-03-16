---
id: crystallographic-planes-directions
title: Crystallographic Planes and Directions
domain: engineering
course: materials-science
prerequisites:
- id: crystal-lattice-systems-classification
  type: hard
builds-toward:
- dislocation-motion-and-slip
- microstructure-development-control
tags:
- miller-indices
- directions
- planes
- slip-systems
stage: formal-systems
status: draft
---

# Crystallographic Planes and Directions

## Core Idea
Miller indices are a notation system for identifying crystal planes (hkl) and directions [hkl] within a crystal structure. The indices represent the reciprocals of the plane's intercepts on crystallographic axes, normalized to the smallest integers. Crystallographic planes and directions are critical for understanding slip systems, mechanical anisotropy, and X-ray diffraction patterns.

## Explainer

From your study of crystal lattice systems, you know that crystals are built from periodically repeating unit cells defined by lattice vectors **a**, **b**, and **c** along three crystallographic axes. The key insight that motivates Miller indices is that a crystal is *anisotropic* — its properties depend on direction. The atomic density, bond angles, and spacing along [100] are generally different from [110] or [111]. To discuss slip, diffraction, cleavage, or any directional property, you need a systematic language for specifying orientations relative to the lattice. Miller indices provide that language.

**Crystallographic directions** are written [uvw] using square brackets, where the integers u, v, w are the components of the direction vector in terms of the lattice basis vectors. To find them: pick two lattice points, compute the vector from one to the other as a combination of lattice vectors, then reduce to the smallest integers. The direction [100] points along **a**, [010] along **b**, [001] along **c**, and [110] points diagonally in the ab-plane. Negative indices are written with an overbar: [1̄10] means −**a** + **b**. The angle brackets <uvw> denote a **family of directions** — all directions that are crystallographically equivalent by the symmetry of the lattice. In a cubic crystal, <100> includes [100], [010], [001], [1̄00], [01̄0], and [001̄] — all six face-normal directions, which are equivalent because the cube has cubic symmetry.

**Crystallographic planes** use the (hkl) notation with round brackets. The procedure is more abstract: find where the plane intercepts the three crystallographic axes (in units of lattice parameters a, b, c), take the *reciprocals* of those intercepts, and reduce to the smallest integers. The reason for taking reciprocals is elegant: a plane parallel to an axis never intercepts it, which would give ∞ as an intercept — the reciprocal converts this to 0, a finite integer. The (100) plane is perpendicular to **a**; the (110) plane cuts both **a** and **b** at equal intercepts and is parallel to **c**; the (111) plane cuts all three axes at unit intercepts. Curly braces {hkl} denote a **family of planes** equivalent by symmetry: {100} includes all six face planes of a cube.

The practical importance of this notation comes into sharp focus with **slip systems**. Plastic deformation in metals occurs when dislocations move along specific crystallographic planes in specific directions — the combination is a slip system, written as {hkl}<uvw>. FCC metals (like copper and aluminum) preferentially slip on {111} planes in <110> directions because these have the highest atomic density and thus lowest resistance to dislocation motion. BCC metals slip on {110}<111>, {112}<111>, and other systems. The twelve equivalent slip systems of FCC are all derived from the single family designation {111}<110> — and you can only enumerate them by knowing how Miller indices transform under the crystal's symmetry operations. X-ray diffraction leverages the same notation: Bragg's law nλ = 2d·sinθ uses the interplanar spacing d_hkl, which for cubic crystals is simply a/√(h²+k²+l²), to identify which planes are diffracting from the peak positions in a diffraction pattern.
