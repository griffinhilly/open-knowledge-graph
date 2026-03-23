---
id: brewster-angle-and-polarization
title: Brewster's Angle and Polarization by Reflection
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-and-snells-law
  type: hard
builds-toward:
- polarization-of-light
tags:
- brewster-angle
- polarization
- reflection
stage: formal-systems
status: validated
---

# Brewster's Angle and Polarization by Reflection

## Core Idea
At Brewster's angle θB = arctan(n₂/n₁), light reflected from a dielectric interface is completely polarized perpendicular to the plane of incidence (s-polarized). Light in the plane of incidence (p-polarized) is fully transmitted, with no reflection. This effect is exploited to eliminate reflections using polarizers at Brewster's angle.

## Questions

```yaml
- question: "A glass plate is tilted to Brewster's angle (≈56° for glass). A beam of randomly polarized light hits the plate. Which of the following correctly describes what happens to the reflected beam?"
  type: multiple-choice
  options:
    - "The reflected beam contains both s- and p-polarized light in equal proportions"
    - "The reflected beam is completely s-polarized — no p-polarized component is reflected"
    - "The reflected beam is completely p-polarized — no s-polarized component is reflected"
    - "The reflected beam is unpolarized but reduced in intensity by exactly half"
  answer: 1
  explanation: "At Brewster's angle, the reflected and refracted rays are perpendicular. The oscillating dipoles responsible for re-radiating p-polarized light cannot radiate along their own axis (the direction of the reflected ray), so zero p-polarized light is reflected. Only s-polarized light is reflected. Option C has it backwards — p-polarized light is fully *transmitted*, not reflected. Option A is the intuitive-but-wrong guess that both polarizations behave the same."

- question: "Polarized sunglasses dramatically reduce glare from wet roads and water surfaces. This works because glare from horizontal surfaces is predominantly which type, and the lenses block which orientation?"
  type: multiple-choice
  options:
    - "Glare is p-polarized (vertical oscillation); lenses block vertical polarization"
    - "Glare is s-polarized (horizontal oscillation); lenses block horizontal polarization"
    - "Glare is circularly polarized; lenses convert it to linear polarization"
    - "Glare is p-polarized (horizontal oscillation); lenses block horizontal polarization"
  answer: 1
  explanation: "Glare from near-horizontal surfaces like roads and water is reflected near Brewster's angle, making it predominantly s-polarized — the electric field oscillates horizontally (perpendicular to the plane of incidence, which is vertical for a horizontal surface). Polarized sunglass lenses have a vertical transmission axis, blocking this horizontal s-polarization. Option A confuses the s/p labeling: s-polarization on a horizontal surface means horizontal oscillation, not vertical."

- question: "At Brewster's angle, both s-polarized and p-polarized components of incident light are partially reflected."
  type: true-false
  answer: false
  explanation: "At Brewster's angle, p-polarized light has zero reflectance — it is entirely transmitted. Only s-polarized light is reflected. This is the defining feature of Brewster's angle: complete polarization of the reflected beam by eliminating one polarization component entirely from reflection."

- question: "Brewster windows in laser cavities are tilted at Brewster's angle so that p-polarized light passes through with essentially zero reflection loss."
  type: true-false
  answer: true
  explanation: "This is the direct application of Brewster's angle in optics engineering. At normal incidence, each glass surface reflects about 4% of the light due to Fresnel reflection. Tilting the window to Brewster's angle makes the reflectance for p-polarized light exactly zero, eliminating cavity losses for that polarization component. It simultaneously selects and preserves p-polarized light inside the laser resonator."

- question: "Why does p-polarized light experience zero reflection at Brewster's angle? Explain in terms of the geometry of the reflected and refracted rays and the physics of dipole radiation."
  type: short-answer
  answer: "At Brewster's angle, the reflected ray and the refracted ray are exactly perpendicular to each other (separated by 90°). The p-polarized component's electric field oscillates in the plane of incidence, driving dipole oscillations along that axis. A dipole does not radiate along its own oscillation axis — it radiates perpendicular to it. Because the 'would-be' reflected ray direction coincides with the dipole's oscillation axis, no p-polarized light can be re-radiated into that direction. The result is complete cancellation of p-polarized reflection."
  explanation: "This is the physical mechanism behind Brewster's angle. The condition θB + θr = 90° (reflected and refracted rays perpendicular) combined with Snell's law yields tan(θB) = n₂/n₁. The zero-reflection result is not a coincidence or just a mathematical result — it follows directly from the dipole radiation pattern, which has a null along the oscillation axis."
```

## Explainer

From Snell's law — your prerequisite — you know that when light crosses from one medium to another with different refractive indices, both a reflected ray and a refracted ray are produced, and the angles are governed by n₁sin(θ₁) = n₂sin(θ₂). What Brewster's angle adds is a special geometric condition: there exists a specific angle of incidence where the reflected and refracted rays are exactly perpendicular to each other, separated by 90°. At that angle, something remarkable happens to polarization.

To understand why, think about how electromagnetic waves work. Light is a transverse wave: the electric field oscillates perpendicular to the direction of propagation. The **p-polarization** component is the part of the electric field oscillating in the **plane of incidence** (the plane containing the incoming ray and the surface normal). The **s-polarization** component oscillates perpendicular to that plane. When the reflected and refracted rays are at 90° to each other, the oscillating dipoles that would re-radiate the p-component into the reflected direction cannot do so — a dipole doesn't radiate along its own axis. So all of the p-polarized light passes through, and only s-polarized light is reflected.

The formula θB = arctan(n₂/n₁) comes directly from combining Snell's law with this 90° condition. If θB + θᵣ = 90° (reflected and refracted rays perpendicular), and Snell's law says n₁sin(θB) = n₂sin(θᵣ) = n₂sin(90° − θB) = n₂cos(θB), then dividing both sides gives tan(θB) = n₂/n₁. For light going from air (n₁ ≈ 1) into glass (n₂ ≈ 1.5), Brewster's angle is arctan(1.5) ≈ 56°. The reflected beam at that angle is 100% s-polarized — completely linearly polarized.

This effect has practical consequences you can observe directly. Glare from a wet road or the surface of water is predominantly s-polarized (horizontal). **Polarized sunglasses** work by blocking s-polarized light, which is why they dramatically cut glare from horizontal surfaces. Photographers use **polarizing filters** to suppress reflections from windows and water, making them transparent or revealing what lies beneath. Laser systems use **Brewster windows** — glass plates tilted at Brewster's angle — so that p-polarized light passes through with zero reflection loss, avoiding the ~4% loss that would occur at each surface at normal incidence.
