---
id: mirror-and-lens-aberrations
title: Spherical and Chromatic Aberrations in Mirrors and Lenses
domain: physics
course: waves-and-optics
prerequisites:
- id: paraxial-ray-approximation
  type: hard
builds-toward:
- optical-instruments
tags:
- aberrations
- spherical-aberration
- chromatic-aberration
stage: formal-systems
status: draft
---

# Spherical and Chromatic Aberrations in Mirrors and Lenses

## Core Idea
Spherical aberration occurs when rays at large angles to the optical axis focus at different points than paraxial rays, degrading image quality. Chromatic aberration arises from wavelength dependence of refractive index, causing different colors to focus at different distances. Both limit optical system performance.

## Explainer

Your prerequisite — the paraxial ray approximation — told you that lens and mirror equations work cleanly when rays stay close to the optical axis. The approximation replaces sin θ with θ (in radians), making the math linear and giving a single, sharp focal point. Aberrations are what happens when that approximation breaks down: rays that hit the lens far from the axis, or light made of multiple wavelengths, don't all converge to the same point.

**Spherical aberration** is a direct consequence of using spherical surfaces (the easiest to manufacture) rather than the theoretically perfect parabolic or aspheric surface. For a spherical mirror or lens, rays striking the outer zones of the aperture converge to a focus slightly closer to the lens than rays through the center. The result is that no single image plane captures a perfectly sharp point — you see a blurred disk called the **circle of least confusion**. The size of this blur scales roughly with the cube of the aperture-to-focal-length ratio (the f-number), which is why photographers close their aperture (higher f-number) for sharp images and astronomers work hard to grind parabolic primary mirrors. Parabolic mirrors focus parallel rays exactly at one point regardless of the angle, which is why satellite dishes, car headlights, and telescope primaries use parabolic profiles.

**Chromatic aberration** arises because glass is a dispersive medium — its refractive index n varies with wavelength. Violet light bends more than red light at the same glass surface. For a converging lens, this means violet focuses closer to the lens than red, with the intermediate colors spread between them. The result is a colored fringe around objects near the edge of the field: typically a purple-blue fringe on one side and a yellow-red fringe on the other. The severity is described by the **Abbe number** (V-number) of the glass: high Abbe numbers mean low dispersion (less chromatic aberration). The classic correction is an **achromatic doublet** — a converging crown glass element cemented to a diverging flint glass element. By choosing glass types with different dispersions, the chromatic error of one element partially cancels the other's, bringing red and blue to the same focus while leaving residual error for other wavelengths.

In practice, optical designers never eliminate aberrations entirely — they balance them. A camera lens has multiple elements precisely because each corrects residual aberrations from the others. The lens equation you derived in paraxial optics remains the starting point, but real lens design iterates through aberration calculations that quantify how far real rays deviate from the paraxial ideal. Understanding aberrations also explains otherwise puzzling observations: why images are sharpest at the center of a lens's field, why stopping down a camera lens always improves sharpness (smaller aperture admits only near-paraxial rays), and why the Hubble Space Telescope — initially spherically aberrated by 2.2 microns of mirror-grinding error — produced blurry images until corrective optics were installed to intentionally introduce the opposite aberration.
