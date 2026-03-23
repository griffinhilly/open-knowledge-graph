---
id: magnetic-field-reduction-pole
title: Magnetic Field Reduction to the Pole
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earths-magnetic-dipole-field-basics
  type: hard
- id: potential-field-methods-gravity-magnetics
  type: hard
builds-toward:
- magnetic-dipole-anomalies
tags:
- magnetic
- reduction-to-pole
- anomaly
stage: expert
status: draft
---

# Magnetic Field Reduction to the Pole

## Core Idea
Magnetic anomalies are displaced from their sources in non-equatorial regions. Reduction-to-the-pole transforms data as if the dipole field were vertical, relocating anomalies to their true positions and enhancing small anomalies.

## Questions

```yaml
- question: "A geophysicist surveys a mid-latitude region and finds that the magnetic anomaly peak is offset several kilometers to the south of where drilling confirms the ore body to be. After applying reduction-to-the-pole (RTP) processing, what should happen to the anomaly peak?"
  type: multiple-choice
  options:
    - "It shifts further south, because RTP amplifies the displacement caused by field inclination"
    - "It moves to center over the ore body, because RTP corrects for the asymmetry caused by the inclined ambient field"
    - "It remains in the same location but becomes sharper, because RTP only improves resolution, not position"
    - "It disappears, because RTP removes induced anomalies and only remanent anomalies remain"
  answer: 1
  explanation: "Reduction to the pole transforms the measured data as if the survey had been conducted at the magnetic pole, where the ambient field is vertical. This removes the lateral displacement and asymmetry introduced by the inclined field, repositioning anomaly peaks directly above their sources. The displacement at mid-latitudes occurs because the inclined ambient field causes the source's magnetization to produce an asymmetric anomaly with the peak offset in the poleward direction. RTP corrects this systematically, making the map geologically interpretable."

- question: "A surveying team attempts to apply RTP processing to airborne magnetic data collected near the magnetic equator (inclination ≈ 3°). Why is this problematic?"
  type: multiple-choice
  options:
    - "Near the equator, magnetic anomalies are too small to detect, so there is no signal to process"
    - "The RTP algorithm requires dividing by a term containing sin(inclination), which approaches zero at the equator, causing numerical instability"
    - "Remanent magnetization is always dominant near the equator, violating the RTP assumption"
    - "The international geomagnetic reference field (IGRF) is not defined near the equator"
  answer: 1
  explanation: "In the frequency domain, RTP involves a filter that divides by terms containing sin(I) and cos(I) where I is the magnetic inclination. At low inclinations (near the magnetic equator), sin(I) ≈ 0, causing the filter to amplify noise catastrophically — the division becomes unstable. For this reason, RTP is generally not applied to data collected within about 10–15° of the magnetic equator. Alternatives such as reduction to the equator or pseudogravity transformation are used instead in these regions."

- question: "After RTP processing is applied, a volcanic sequence still shows anomaly peaks displaced from known volcanic vents. This is unexpected because RTP should have centered all anomalies. What is the most likely explanation?"
  type: true-false
  answer: false
  explanation: "Standard RTP assumes all sources are magnetized parallel to the present ambient field (induced magnetization only). Volcanic rocks commonly acquire remanent magnetization in the direction of the ancient field at the time they cooled — this direction may differ substantially from the current ambient field. When remanence direction and ambient field direction diverge, the standard RTP correction (which assumes they are identical) will not correctly relocate the anomaly peak. The statement is false because it implies RTP corrects for all sources unconditionally; it does not work for bodies with significant remanent magnetization in a non-ambient direction."

- question: "Reduction to the pole makes magnetic anomaly interpretation easier at mid-latitudes because, at the pole, a simple induced source produces a symmetric anomaly centered directly above the body."
  type: true-false
  answer: true
  explanation: "This is exactly the logic behind RTP. At the magnetic pole, the ambient field is vertical and the induced magnetization is also vertical. A vertically magnetized source produces a symmetric, positive anomaly centered over it with no lateral offset and no negative lobe — a 'bulls-eye' pattern. This symmetry is what makes anomaly shapes easy to interpret in terms of source geometry and depth. At mid-latitudes, the inclined field creates asymmetric patterns with off-center peaks and flanking negative lobes, which complicate interpretation. RTP transforms the data to the simpler polar geometry."

- question: "Why does an inclined (non-vertical) magnetic field cause a buried induced source to produce an asymmetric anomaly that is offset from the source, rather than a symmetric anomaly centered above it?"
  type: short-answer
  answer: "An induced source magnetizes parallel to the ambient field. When the field is inclined rather than vertical, the magnetization vector has both vertical and horizontal components. The horizontal component introduces a dipolar pattern in the horizontal direction — a positive lobe on one side and a negative lobe on the other — superimposed on the vertical component's symmetric pattern. The combined effect shifts the net anomaly peak to one side of the source (toward the pole) and creates an asymmetric shape. The degree of asymmetry increases as inclination decreases toward the equator."
  explanation: "The key insight is that magnetic anomalies depend on both the magnetization direction of the source and the direction of the field in which measurements are made. RTP effectively rotates both to vertical, eliminating the horizontal components that cause the asymmetry. Without this correction, geologists trying to locate buried sources from anomaly peaks will systematically drill in the wrong place."
```

## Explainer

From your study of Earth's dipole field, you know that the magnetic field is not vertical everywhere — it dips at an angle (the inclination) that varies with latitude, from horizontal at the magnetic equator to vertical at the poles. From potential field methods, you know that magnetic surveys measure anomalies caused by subsurface bodies with contrasting magnetic properties. The problem that **reduction to the pole (RTP)** solves is that these two facts interact in a way that makes magnetic maps misleading at most latitudes.

Consider a simple case: a vertically magnetized, roughly spherical ore body buried beneath the surface. If you were at the magnetic pole, where the ambient field is vertical, this body would produce a symmetric anomaly directly above it — a clean bulls-eye pattern with the peak centered over the source. Interpretation would be straightforward. But at mid-latitudes, where the field is inclined, the same body produces an **asymmetric anomaly**: the peak is displaced to one side of the source, and a negative lobe appears on the other side. The anomaly no longer sits directly over the body that causes it. At the magnetic equator, where the field is horizontal, the distortion is even more pronounced — the anomaly pattern can look completely different from what you might naively expect. This latitude-dependent distortion occurs because the magnetic anomaly depends on both the magnetization direction of the source and the direction of the ambient field in which the measurement is made.

**Reduction to the pole** is a mathematical transformation applied in the frequency domain (using Fourier transforms) that recalculates the magnetic data as if the survey had been conducted at the magnetic pole, where inclination is 90°. The transformation effectively rotates the magnetization and ambient field vectors to vertical, converting every anomaly into the symmetric, centered pattern it would have at the pole. After RTP processing, anomaly peaks sit directly above their sources, positive and negative lobes resolve into clean shapes, and the map becomes far easier to interpret geologically. Small anomalies that were partially obscured by the asymmetric lobes of nearby larger anomalies become visible.

The RTP operation does have limitations. It requires knowledge of the local magnetic field direction (inclination and declination), which is typically obtained from the International Geomagnetic Reference Field (IGRF) model. At **low magnetic latitudes** — within about 15° of the magnetic equator — the transformation becomes numerically unstable because it involves dividing by quantities that approach zero when the inclination is small. In these regions, alternative approaches such as **reduction to the equator** or **pseudogravity transformation** are used instead. Additionally, RTP assumes that all sources are magnetized parallel to the ambient field (induced magnetization only). Bodies with strong **remanent magnetization** in a different direction — common in volcanic rocks — will not be correctly repositioned by standard RTP and require modified approaches that account for the remanence direction.
