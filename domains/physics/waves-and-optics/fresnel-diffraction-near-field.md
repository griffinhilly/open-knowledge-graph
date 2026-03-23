---
id: fresnel-diffraction-near-field
title: 'Fresnel Diffraction: Near-Field Diffraction Phenomena'
domain: physics
course: waves-and-optics
prerequisites:
- id: diffraction-and-huygen-principle
  type: hard
builds-toward:
- rayleigh-criterion-resolution
tags:
- fresnel-diffraction
- near-field
- diffraction
stage: formal-systems
status: validated
---

# Fresnel Diffraction: Near-Field Diffraction Phenomena

## Core Idea
Fresnel diffraction occurs when source or observation point is near the diffracting aperture, requiring consideration of wavefront curvature. More complex than Fraunhofer diffraction, it involves Fresnel zones and Cornu spirals. Important for understanding diffraction near edges and apertures.

## Questions

```yaml
- question: "A small circular disk is illuminated by coherent monochromatic light. A screen is placed a short distance behind the disk — well within the near-field region. Wave optics predicts what at the geometric center of the disk's shadow?"
  type: multiple-choice
  options:
    - "A bright spot, because wavelets diffracting around the entire rim of the disk travel nearly equal path lengths and interfere constructively"
    - "Complete darkness, matching the geometric shadow"
    - "A pattern identical to the far-field Fraunhofer diffraction from a circular aperture"
    - "A dark fringe, because the disk blocks the central Fresnel zone"
  answer: 0
  explanation: "This is the Poisson (Arago) bright spot: all the edge wavelets travel nearly equal distances to the geometric center of the shadow, so they arrive in phase and interfere constructively — producing a bright spot exactly where geometric optics predicts darkness. Option 1 is the geometric-optics intuition that Fresnel diffraction directly contradicts. The bright spot was confirmed experimentally in 1818 and became a landmark test of wave optics."

- question: "The Fresnel zone construction divides a wavefront into concentric rings so that consecutive zones contribute path lengths differing by λ/2. What is the consequence for the total amplitude at the observation point?"
  type: multiple-choice
  options:
    - "Contributions from odd-numbered zones interfere constructively with each other, while even-numbered zones tend to cancel them — so the total amplitude depends on how many zones are uncovered by the aperture"
    - "All zones contribute equally in phase, so amplitude increases without limit as more zones are exposed"
    - "Only the innermost zone contributes significantly; outer zones are negligible due to their large angle of incidence"
    - "Fresnel zones only apply when the aperture diameter is smaller than one wavelength"
  answer: 0
  explanation: "Because adjacent zones are λ/2 apart in path length, they arrive roughly out of phase with each other. Odd zones add constructively to the amplitude and even zones subtract. The total amplitude at a point is therefore sensitive to whether an even or odd number of zones is exposed — which is why a small aperture can actually produce a brighter spot than an open wavefront (if it exposes exactly one zone). This has no analog in geometric optics."

- question: "The intensity at the geometric center of a circular aperture in Fresnel diffraction can exceed the unobstructed (no aperture) intensity, depending on the aperture size and distance."
  type: true-false
  answer: true
  explanation: "If the aperture exposes exactly one Fresnel zone, the amplitude at the center is roughly twice the unobstructed amplitude, giving four times the unobstructed intensity. This counterintuitive result — an aperture that increases intensity — follows directly from the zone construction: the full wavefront has contributions from all zones that partially cancel, whereas a single exposed zone avoids that cancellation. Fraunhofer (far-field) diffraction does not produce this effect."

- question: "Fresnel diffraction reduces to Fraunhofer diffraction when the source and observation point are very close to the aperture."
  type: true-false
  answer: false
  explanation: "The relationship is the opposite. Fraunhofer diffraction is the far-field limit — it applies when source and observation screen are far from the aperture (or equivalently, when lenses are used to collimate and focus the light). Fresnel diffraction is the near-field regime, valid when the observation distance is comparable to or smaller than a²/λ (where a is the aperture size). Moving the screen closer to the aperture does not simplify the analysis; it enters the Fresnel regime where wavefront curvature must be accounted for."

- question: "Why does a bright spot appear at the center of a circular obstacle's geometric shadow in coherent light, and why does this result contradict geometric optics?"
  type: short-answer
  answer: "All diffracted wavelets originating from around the rim of the circular obstacle travel nearly equal path lengths to the center of the geometric shadow, so they arrive approximately in phase and interfere constructively — producing a bright spot. Geometric optics predicts darkness there because it treats light as straight rays blocked by the obstacle. The bright spot is possible only because light is a wave: it bends around the obstacle's edge, and the phase coherence of the rim wavelets produces constructive interference at precisely the location where geometric reasoning expects maximum shadow."
  explanation: "This is the Poisson (Arago) bright spot, named because Poisson derived it as a seemingly absurd prediction of Fresnel's wave theory — and Arago confirmed it experimentally. It illustrates the core insight of Fresnel diffraction: near-field intensity patterns are governed by interference of curved wavefronts, not by geometric shadow boundaries, and the result can be qualitatively opposite to the geometric prediction."
```

## Explainer

In your study of Huygens' principle and Fraunhofer diffraction, you learned to treat every point on a wavefront as a secondary source of spherical wavelets. In the far field — when the observation screen is very far from the aperture relative to its size — those wavelets arrive at the screen with nearly flat (planar) wavefronts, and the geometry simplifies to a Fourier transform relationship between aperture shape and intensity pattern. **Fresnel diffraction** drops this simplifying assumption. When the screen is close enough that the curvature of the incoming wavefronts matters, the analysis must explicitly account for the varying path lengths from different points on the aperture to the observation point.

The central bookkeeping tool is the **Fresnel zone** construction. Imagine drawing concentric rings on the aperture such that successive rings contribute path lengths that differ by λ/2. The first zone contains all wavelet sources within λ/2 of the shortest path; the second zone adds another λ/2; and so on. Contributions from odd-numbered zones arrive roughly in phase with each other and tend to constructively interfere, while even-numbered zones arrive out of phase and tend to cancel. The total amplitude at the observation point depends on how many Fresnel zones are uncovered by the aperture — a dramatic dependence on geometry that has no analog in geometric optics.

One striking consequence is the **Poisson bright spot** (also called the Arago spot): a circular obstacle should, by geometric reasoning, cast a dark shadow. But diffraction theory predicts — and experiments confirm — that a bright spot appears at the geometric center of the shadow, because all the wavelet paths around the edge of the obstacle are nearly equal in length and interfere constructively. This was a famous historical test of wave optics in the early nineteenth century, and it remains a vivid demonstration that near-field diffraction can produce intensity maxima exactly where shadows are geometrically expected.

The **Cornu spiral** is the graphical tool for computing Fresnel diffraction amplitudes when dealing with straight edges rather than circular apertures. As you sweep the integration variable along the aperture, the amplitude vector traces a spiral in the complex plane (phasor space). The intensity at any observation point corresponds to the squared length of the chord connecting two points on the spiral. Near a sharp edge, the spiral's curling tail explains why the intensity doesn't simply snap from bright to dark — it oscillates with diminishing amplitude into the geometric shadow before settling to half the unobstructed intensity exactly at the edge. These oscillations (the bright and dark fringes near an edge) are the signature of Fresnel diffraction in everyday settings like the bright-dark fringe you can observe at the silhouette of a razor blade in coherent light.

