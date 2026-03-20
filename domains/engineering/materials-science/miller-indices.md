---
id: miller-indices
title: 'Miller Indices: Crystallographic Planes and Directions'
domain: engineering
course: materials-science
prerequisites:
- id: crystal-structure-basics
  type: hard
- id: vectors-in-3d
  type: soft
builds-toward:
- plastic-deformation-mechanisms
- x-ray-diffraction-materials
tags:
- miller-indices
- crystallography
- planes
- directions
stage: advanced
status: validated
---

# Miller Indices: Crystallographic Planes and Directions

## Core Idea
Miller indices provide a standardized notation for identifying planes and directions within a crystal lattice. A direction [uvw] is specified as the smallest integer vector components along the lattice axes, while a plane (hkl) is defined by the reciprocals of its intercepts with the unit cell axes, cleared to integers. Families of equivalent planes {hkl} and directions <uvw> are related by crystal symmetry. Miller indices are essential for understanding slip systems in plastic deformation and interpreting diffraction patterns.

## How It's Best Learned
Practice on a cubic unit cell by first indexing simple planes (cube faces, body diagonal), then generalizing. Sketch the planes corresponding to given indices and verify by checking axis intercepts.

## Common Misconceptions
- Negative indices are written with an overbar, not a minus sign, but computationally they work identically.
- The direction [111] and the plane (111) are perpendicular only in cubic systems — this does not hold for non-cubic lattices.

## Explainer

From your study of crystal structures, you know that a crystal is an infinite periodic arrangement of atoms, and the **unit cell** is the repeating building block. To describe any geometric feature of this periodic structure — a specific plane of atoms, a direction of atomic bonding, a slip system — engineers need a compact, unambiguous notation that takes advantage of the periodicity. Miller indices provide exactly that notation, using a small set of integers derived directly from the geometry of the unit cell.

For **directions**, the procedure is straightforward. Pick a vector pointing in the direction of interest, express it as components along the three lattice axes (a, b, c), scale to the smallest integers with no common factor, and enclose in square brackets: [uvw]. The direction [100] points along the a-axis; [110] is the face diagonal in the a-b plane; [111] is the body diagonal. Negative components indicate the vector goes in the negative direction along that axis, written with an overbar. The family notation <uvw> collects all crystallographically equivalent directions — in a cubic system, <100> includes [100], [010], [001], [1̄00], [01̄0], and [001̄], all of which are equivalent by symmetry.

For **planes**, the procedure is slightly less obvious, and the key is the use of reciprocals. You identify where the plane intersects each of the three unit cell axes (in multiples of the lattice parameter), take the reciprocal of each intercept, then clear to integers. A plane that intersects the a-axis at 1, the b-axis at 2, and runs parallel to the c-axis (intercept at ∞) gives reciprocals 1/1, 1/2, 1/∞ = 1, ½, 0 → clearing to (210). The reason for the reciprocal procedure is mathematical elegance: it ensures that the Miller indices (hkl) appear naturally in the equations governing X-ray diffraction (Bragg's law with lattice planes), making interpretation of diffraction patterns direct. Parallel planes are members of the same family {hkl}.

The payoff for learning this notation becomes clear when you study plastic deformation. Metals deform by slip — the sliding of one plane of atoms over another along a direction within that plane. The combination of slip plane and slip direction is a **slip system**, written (hkl)[uvw]. The most favorable slip systems are the closest-packed planes and directions, and Miller indices let you identify them precisely. In FCC metals, the {111} planes are the closest-packed; the <110> directions within them are the closest-packed directions. This gives 12 independent slip systems and explains why FCC metals like copper and aluminum are so ductile. In BCC metals the slip direction is <111> but the slip plane is less well-defined, leading to different deformation behavior. The same notation connects directly to X-ray diffraction: the d-spacing of planes (hkl) determines which Bragg peaks appear in a diffraction pattern, so Miller indices link crystal geometry, mechanical behavior, and structural characterization into a unified descriptive language.
