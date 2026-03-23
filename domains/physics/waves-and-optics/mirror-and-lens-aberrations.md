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
status: validated
---

# Spherical and Chromatic Aberrations in Mirrors and Lenses

## Core Idea
Spherical aberration occurs when rays at large angles to the optical axis focus at different points than paraxial rays, degrading image quality. Chromatic aberration arises from wavelength dependence of refractive index, causing different colors to focus at different distances. Both limit optical system performance.

## Questions

```yaml
- question: "A photographer shoots a portrait at f/2 and notices the background is sharp but the subject looks slightly soft. They stop down to f/11 and sharpness dramatically improves. What is the primary optical reason?"
  type: multiple-choice
  options:
    - "Higher f-numbers increase the depth of field, so more of the scene is in focus simultaneously"
    - "Stopping down restricts light to near-paraxial rays that pass through the center of the lens, where spherical aberration is minimal, so all admitted rays converge to nearly the same focal point"
    - "Smaller apertures reduce chromatic aberration by filtering out blue wavelengths"
    - "Higher f-numbers increase the refractive index of the lens glass, sharpening the image"
  answer: 1
  explanation: "Both answers A and B point at real effects, but the question targets spherical aberration specifically. Spherical aberration is worse for rays that pass through the outer zones of a lens (far from the optical axis) — these focus at a different point than central rays. Stopping down physically blocks the outer zones, admitting only near-paraxial rays that obey the paraxial approximation closely. All admitted rays then converge to nearly the same point, reducing the blur circle. (Depth of field does also increase with smaller aperture, but that's a separate geometric phenomenon.)"

- question: "An achromatic doublet lens corrects chromatic aberration by:"
  type: multiple-choice
  options:
    - "Using a single lens element made from glass with zero dispersion (constant refractive index across wavelengths)"
    - "Coating the lens with an antireflection layer that blocks the most aberrant wavelengths"
    - "Cementing two elements — a converging crown glass and a diverging flint glass with different dispersions — so the chromatic errors of one partially cancel the other's"
    - "Placing a prism in the light path to recombine wavelengths after they diverge"
  answer: 2
  explanation: "Chromatic aberration arises because refractive index varies with wavelength — different colors focus at different distances. No single glass element eliminates this because all glass disperses light to some degree. The achromatic doublet exploits the fact that two glass types (crown and flint) have different dispersion characteristics. The converging element's chromatic error and the diverging element's chromatic error partially cancel each other, bringing red and blue to the same focus. This correction is wavelength-specific — residual error remains for other wavelengths — but it eliminates the dominant first-order chromatic error."

- question: "Parabolic primary mirrors, unlike spherical ones, focus all parallel on-axis rays to a single point regardless of how far from the optical axis those rays strike the mirror."
  type: true-false
  answer: true
  explanation: "This is why parabolic mirrors are used in telescopes, satellite dishes, and car headlights. The paraboloid is the mathematically exact surface that reflects parallel rays to a perfect focus — it satisfies the law of reflection precisely for all ray heights, not just paraxial ones. A spherical mirror is only an approximation of the paraboloid valid for small angles (the paraxial regime). Outside that regime, marginal rays focus closer than paraxial rays — spherical aberration. Grinding a parabolic surface is harder than grinding a sphere, but it eliminates spherical aberration for on-axis imaging."

- question: "Chromatic aberration affects mirrors and lenses equally, since both refract and bend light to form images."
  type: true-false
  answer: false
  explanation: "Chromatic aberration is exclusively a lens (refraction) phenomenon — it does not affect mirrors. Chromatic aberration arises because the refractive index of glass varies with wavelength, causing different colors to bend by different amounts at a glass-air interface. Mirrors work by reflection, not refraction, and the law of reflection (angle of incidence = angle of reflection) does not depend on wavelength. This is why large telescope primaries are mirrors rather than lenses: a mirror has no chromatic aberration, and it can be supported from behind rather than just at the rim, allowing much larger apertures."

- question: "Explain how both spherical aberration and chromatic aberration are, in different ways, failures of assumptions built into the paraxial ray approximation."
  type: short-answer
  answer: "The paraxial approximation assumes two things: (1) rays stay close to the optical axis so that sin θ ≈ θ, and (2) the refractive index is a single constant for all light. Spherical aberration violates assumption 1 — real rays far from the axis do not satisfy sin θ ≈ θ and therefore focus at a different point than predicted. Chromatic aberration violates assumption 2 — real glass has wavelength-dependent refractive index, so different colors focus at different distances. Both aberrations are the gap between the idealized model and physical reality."
  explanation: "This framing shows that aberrations are not separate, unrelated problems but two facets of the same idealization breaking down. The paraxial approximation is a first-order model that linearizes the optics. Real optical design is the engineering task of managing the higher-order terms it ignores — both the angular nonlinearity (spherical aberration) and the wavelength dependence of material properties (chromatic aberration). Recognizing both as approximation failures also suggests the correction strategy: use surfaces (parabolas) that don't rely on the linear approximation, and use material combinations (doublets) that cancel wavelength dependence."
```

## Explainer

Your prerequisite — the paraxial ray approximation — told you that lens and mirror equations work cleanly when rays stay close to the optical axis. The approximation replaces sin θ with θ (in radians), making the math linear and giving a single, sharp focal point. Aberrations are what happens when that approximation breaks down: rays that hit the lens far from the axis, or light made of multiple wavelengths, don't all converge to the same point.

**Spherical aberration** is a direct consequence of using spherical surfaces (the easiest to manufacture) rather than the theoretically perfect parabolic or aspheric surface. For a spherical mirror or lens, rays striking the outer zones of the aperture converge to a focus slightly closer to the lens than rays through the center. The result is that no single image plane captures a perfectly sharp point — you see a blurred disk called the **circle of least confusion**. The size of this blur scales roughly with the cube of the aperture-to-focal-length ratio (the f-number), which is why photographers close their aperture (higher f-number) for sharp images and astronomers work hard to grind parabolic primary mirrors. Parabolic mirrors focus parallel rays exactly at one point regardless of the angle, which is why satellite dishes, car headlights, and telescope primaries use parabolic profiles.

**Chromatic aberration** arises because glass is a dispersive medium — its refractive index n varies with wavelength. Violet light bends more than red light at the same glass surface. For a converging lens, this means violet focuses closer to the lens than red, with the intermediate colors spread between them. The result is a colored fringe around objects near the edge of the field: typically a purple-blue fringe on one side and a yellow-red fringe on the other. The severity is described by the **Abbe number** (V-number) of the glass: high Abbe numbers mean low dispersion (less chromatic aberration). The classic correction is an **achromatic doublet** — a converging crown glass element cemented to a diverging flint glass element. By choosing glass types with different dispersions, the chromatic error of one element partially cancels the other's, bringing red and blue to the same focus while leaving residual error for other wavelengths.

In practice, optical designers never eliminate aberrations entirely — they balance them. A camera lens has multiple elements precisely because each corrects residual aberrations from the others. The lens equation you derived in paraxial optics remains the starting point, but real lens design iterates through aberration calculations that quantify how far real rays deviate from the paraxial ideal. Understanding aberrations also explains otherwise puzzling observations: why images are sharpest at the center of a lens's field, why stopping down a camera lens always improves sharpness (smaller aperture admits only near-paraxial rays), and why the Hubble Space Telescope — initially spherically aberrated by 2.2 microns of mirror-grinding error — produced blurry images until corrective optics were installed to intentionally introduce the opposite aberration.
