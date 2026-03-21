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
stage: advanced
status: draft
---

# Rayleigh Criterion and Diffraction-Limited Resolution

## Core Idea
The Rayleigh criterion states that two point sources are just resolved when the principal maximum of one's diffraction pattern coincides with the first minimum of the other's. For a circular aperture of diameter D, angular resolution θ ≈ 1.22λ/D. This fundamental limit applies to telescopes, microscopes, and all imaging systems.

## Questions

```yaml
- question: "An astronomer wants to resolve two stars separated by a very small angle. She currently uses a 1-meter aperture telescope at λ = 500 nm. What single change would most directly improve her angular resolution?"
  type: multiple-choice
  options:
    - "Using a higher-quality lens with better anti-reflection coatings to reduce aberrations"
    - "Increasing the aperture to 10 meters, since angular resolution scales as 1/D"
    - "Increasing magnification — higher magnification reveals finer detail"
    - "Observing on nights with steady atmospheric seeing to reduce turbulence"
  answer: 1
  explanation: "Angular resolution is determined by θ_min ≈ 1.22λ/D. Only λ (wavelength) and D (aperture) appear in this formula. Increasing D from 1 m to 10 m reduces θ_min by a factor of 10 — a direct, fundamental improvement. Higher magnification simply enlarges the image the telescope already forms, including the Airy disks — it adds no new angular information. Lens quality and seeing affect image quality but not the diffraction limit, which is set by wave physics alone."

- question: "Two stars are separated by exactly the Rayleigh angular resolution limit. What does their combined intensity pattern look like?"
  type: multiple-choice
  options:
    - "Two fully separated, distinct peaks with a dark gap between them"
    - "A single merged blob with no detectable structure — the stars appear as one"
    - "Two overlapping peaks with a slight dip between them — barely but detectably resolved"
    - "A single elongated peak whose shape reveals the presence of two sources"
  answer: 2
  explanation: "The Rayleigh criterion defines 'just resolved' as the condition where the central maximum of one Airy disk falls exactly on the first minimum of the other's. At this separation, there is a ~26% dip in intensity between the two peaks in the combined pattern — enough to distinguish two objects from one, but just barely. Option A describes stars much further apart; option B describes stars closer than the Rayleigh limit. The criterion is a practical definition of threshold resolution, not a binary resolved/unresolved switch."

- question: "The diffraction limit θ ≈ 1.22λ/D arises from imperfections in the lens and can be overcome by using a sufficiently high-quality optical system."
  type: true-false
  answer: false
  explanation: "The diffraction limit is not a lens imperfection — it is a fundamental consequence of wave physics. Any finite aperture necessarily diffracts light, producing an Airy disk rather than a perfect geometric point. Even a theoretically perfect lens with zero aberrations will produce Airy disks, because the diffraction is caused by the finite aperture itself, not by any flaw in the optics. Super-resolution techniques (like STED microscopy) work around this limit by exploiting different physical mechanisms, not by improving lens quality."

- question: "A radio telescope operating at λ = 10 cm requires a much larger aperture than an optical telescope at λ = 500 nm to achieve the same angular resolution."
  type: true-false
  answer: true
  explanation: "Resolution θ_min ≈ 1.22λ/D means that to achieve the same θ_min with a longer wavelength, you need a proportionally larger aperture. Radio wavelengths (~1 cm to 1 m) are roughly 10⁴ to 10⁸ times longer than optical wavelengths (~500 nm). To match a 10 cm optical telescope's resolution at λ = 500 nm (θ ≈ 6 μrad), a radio telescope at λ = 10 cm would need an aperture of ~20 km. This is why radio astronomers use aperture synthesis arrays spanning continents (VLBI)."

- question: "Why does increasing aperture improve angular resolution, and why can't higher magnification achieve the same effect?"
  type: short-answer
  answer: "A larger aperture D produces a smaller Airy disk radius (proportional to λ/D), so two closely spaced point sources produce less overlapping diffraction patterns — they are easier to distinguish. This is a genuine increase in the information content of the image. Higher magnification simply scales up the image the telescope already forms, including the overlapping Airy disks. Magnifying a blurred, unresolved image produces a larger blurred image, not a sharper one. Resolution is set by the size of the Airy disks (determined by D and λ); magnification cannot shrink those disks."
  explanation: "This distinction matters practically. Amateur astronomers often mistake magnification for resolving power. A small telescope at 400× magnification will not resolve what a large telescope at 100× can — the small telescope's Airy disks are simply larger, and enlarging them doesn't reveal sub-disk structure. In professional astronomy, 'resolving power' and 'light-gathering power' both improve with aperture, which is why all progress in astronomy comes from building bigger mirrors, not stronger eyepieces."
```

## Explainer

From Fraunhofer diffraction, you know that light passing through a circular aperture does not form a perfect geometric point on the far side — diffraction spreads it into an **Airy disk**: a bright central maximum surrounded by alternating dark and bright rings. The angular radius of the first dark ring is approximately 1.22λ/D, where λ is the wavelength and D is the aperture diameter. This is not a flaw in the lens; it is a fundamental consequence of wave physics. Every imaging system — telescope, microscope, camera, human eye — forms Airy disks rather than perfect points, because every imaging system has a finite aperture.

Now consider two stars close together in the sky. Each one forms its own Airy disk at the focal plane of the telescope. When the stars are far apart, the two disks are well separated and clearly distinguishable. As the angular separation decreases, the disks overlap more and more. At some separation, the overlap is so complete that the combined intensity pattern looks like a single elongated blob rather than two distinct peaks — the stars appear as one. Lord Rayleigh proposed a convenient definition of the threshold: two point sources are **just resolved** when the central maximum of one Airy disk falls exactly on the first minimum of the other's. At this separation, there is still a slight dip between the two peaks in the combined pattern — just enough to distinguish two objects from one.

The resulting formula, θ_min ≈ 1.22λ/D, packs in powerful intuition about both λ and D. Shorter wavelengths (smaller λ) produce smaller Airy disks and therefore better resolution — this is why X-ray and electron microscopes can image atoms while optical microscopes cannot. Larger apertures (bigger D) also produce smaller Airy disks — this is why a 10-meter telescope resolves far finer detail than a 0.1-meter telescope, and why the human pupil in bright light (smaller) resolves less finely than a dark-adapted eye (larger). Resolution and light-gathering are both improved by larger apertures, which is why astronomers relentlessly build bigger mirrors.

The practical implications extend across instrumentation. A radio telescope working at centimeter wavelengths needs a dish measured in kilometers to match the angular resolution of a modest optical telescope — which is why radio astronomers use **aperture synthesis** (arrays of dishes spread across basins or continents). In microscopy, the Rayleigh criterion sets the diffraction limit that ordinary optical microscopes cannot beat; techniques like STED and PALM microscopy use clever tricks to work around this limit, earning their inventors a Nobel Prize. Whenever you see a specification for the "resolving power" or "angular resolution" of an instrument, it is this criterion — or one of its variants — that defines the number.
