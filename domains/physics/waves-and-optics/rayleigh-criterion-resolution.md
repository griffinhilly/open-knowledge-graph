---
id: rayleigh-criterion-resolution
title: Rayleigh Criterion and Diffraction-Limited Resolution
domain: physics
course: waves-and-optics
prerequisites:
- id: fraunhofer-diffraction-patterns
  type: hard
builds-toward:
- optical-instruments
tags:
- resolution
- rayleigh-criterion
- diffraction-limit
stage: formal-systems
status: draft
---

# Rayleigh Criterion and Diffraction-Limited Resolution

## Core Idea
The Rayleigh criterion states that two point sources are just resolved when the principal maximum of one's diffraction pattern coincides with the first minimum of the other's. For a circular aperture of diameter D, angular resolution θ ≈ 1.22λ/D. This fundamental limit applies to telescopes, microscopes, and all imaging systems.

## Explainer

From Fraunhofer diffraction, you know that light passing through a circular aperture does not form a perfect geometric point on the far side — diffraction spreads it into an **Airy disk**: a bright central maximum surrounded by alternating dark and bright rings. The angular radius of the first dark ring is approximately 1.22λ/D, where λ is the wavelength and D is the aperture diameter. This is not a flaw in the lens; it is a fundamental consequence of wave physics. Every imaging system — telescope, microscope, camera, human eye — forms Airy disks rather than perfect points, because every imaging system has a finite aperture.

Now consider two stars close together in the sky. Each one forms its own Airy disk at the focal plane of the telescope. When the stars are far apart, the two disks are well separated and clearly distinguishable. As the angular separation decreases, the disks overlap more and more. At some separation, the overlap is so complete that the combined intensity pattern looks like a single elongated blob rather than two distinct peaks — the stars appear as one. Lord Rayleigh proposed a convenient definition of the threshold: two point sources are **just resolved** when the central maximum of one Airy disk falls exactly on the first minimum of the other's. At this separation, there is still a slight dip between the two peaks in the combined pattern — just enough to distinguish two objects from one.

The resulting formula, θ_min ≈ 1.22λ/D, packs in powerful intuition about both λ and D. Shorter wavelengths (smaller λ) produce smaller Airy disks and therefore better resolution — this is why X-ray and electron microscopes can image atoms while optical microscopes cannot. Larger apertures (bigger D) also produce smaller Airy disks — this is why a 10-meter telescope resolves far finer detail than a 0.1-meter telescope, and why the human pupil in bright light (smaller) resolves less finely than a dark-adapted eye (larger). Resolution and light-gathering are both improved by larger apertures, which is why astronomers relentlessly build bigger mirrors.

The practical implications extend across instrumentation. A radio telescope working at centimeter wavelengths needs a dish measured in kilometers to match the angular resolution of a modest optical telescope — which is why radio astronomers use **aperture synthesis** (arrays of dishes spread across basins or continents). In microscopy, the Rayleigh criterion sets the diffraction limit that ordinary optical microscopes cannot beat; techniques like STED and PALM microscopy use clever tricks to work around this limit, earning their inventors a Nobel Prize. Whenever you see a specification for the "resolving power" or "angular resolution" of an instrument, it is this criterion — or one of its variants — that defines the number.
