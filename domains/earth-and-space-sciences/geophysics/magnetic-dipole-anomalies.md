---
id: magnetic-dipole-anomalies
title: Magnetic Dipole Anomalies and 3D Modeling
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earths-magnetic-dipole-field-basics
  type: hard
- id: magnetic-field-reduction-pole
  type: hard
tags:
- magnetic
- dipole
- anomaly
- 3d-modeling
stage: advanced
status: draft
---

# Magnetic Dipole Anomalies and 3D Modeling

## Core Idea
Magnetic sources are modeled as dipoles whose anomalies depend on magnetization direction, moment, and position. 3D forward modeling of magnetic blocks and inversions recover source location and moment from observed anomalies.

## Questions

```yaml
- question: "Two geophysicists survey the same buried magnetized ore deposit — one conducts the survey near the magnetic equator, the other near the magnetic pole. How do their anomaly maps compare?"
  type: multiple-choice
  options:
    - "Both maps show symmetric positive anomalies centered directly over the deposit"
    - "The equatorial survey shows an antisymmetric pattern with offset positive and negative lobes; the polar survey shows a symmetric positive anomaly centered over the deposit"
    - "The equatorial survey gives a larger anomaly amplitude because Earth's background field is weaker there"
    - "Both maps are identical because the deposit's magnetization and depth are the same in both cases"
  answer: 1
  explanation: "Magnetic anomaly shape depends critically on the inclination of Earth's background field. At the magnetic poles, the field is vertical, producing a symmetric positive anomaly centered directly above a magnetized body. At the magnetic equator, the field is horizontal, producing an antisymmetric pattern where the positive and negative lobes appear side by side and the anomaly peak is laterally offset from the source. The same deposit produces fundamentally different anomaly shapes at different latitudes — this is why reduction to the pole is necessary before interpreting source locations."

- question: "What does 'reduction to the pole' accomplish in the processing of magnetic survey data?"
  type: multiple-choice
  options:
    - "It removes the effect of topographic relief on measured magnetic field values"
    - "It mathematically transforms the anomaly data as if the survey had been conducted at the north magnetic pole, converting asymmetric anomalies into symmetric patterns centered above their sources"
    - "It corrects for diurnal and secular variation in Earth's background magnetic field"
    - "It converts measured total-field anomalies from nanoteslas into SI units suitable for forward modeling"
  answer: 1
  explanation: "Reduction to the pole applies a filter in the Fourier domain that accounts for the current survey latitude and field inclination/declination, effectively recomputing what the anomaly would look like if measured where Earth's field is vertical. The result is symmetric anomalies with peaks directly over their sources, making source location and body geometry much easier to interpret. Without this step, the offset lobes at intermediate and equatorial latitudes can make sources appear to be in the wrong location."

- question: "A deeper buried magnetic source produces a narrower, higher-amplitude anomaly at the surface compared to a shallower source of identical magnetization and volume."
  type: true-false
  answer: false
  explanation: "The opposite is true. Anomaly width at the surface increases with source depth because magnetic field strength decreases as the square of distance, and the geometric spreading of the field lines widens the anomaly footprint. A shallow source produces a narrow, sharp, high-amplitude anomaly; a deep source produces a broad, low-amplitude anomaly. This inverse relationship between anomaly width and source depth is one of the primary tools for estimating burial depth from surface magnetic data."

- question: "Unlike gravity anomalies, a magnetic anomaly from a single compact buried source necessarily has both positive and negative lobes."
  type: true-false
  answer: true
  explanation: "This reflects the fundamental difference between scalar (gravitational) and vector dipolar (magnetic) sources. Gravity is a monopolar field — excess mass always produces a positive anomaly above it. Magnetic sources are inherently dipolar: every magnetized body has a north and south pole, and the field it produces has both directions. This means any isolated magnetic source necessarily creates an anomaly with both positive and negative components, whose spatial arrangement depends on the inclination of the background field. There is no magnetic equivalent of a 'purely positive' anomaly from a compact source."

- question: "Explain why the shape and position of a magnetic anomaly depend on the latitude of the survey, and what this implies for locating the source from an anomaly map."
  type: short-answer
  answer: "The anomaly produced by a buried magnetic source is the superposition of the source's magnetization field and Earth's background field. The inclination of Earth's background field — how steeply it dips below horizontal — varies with latitude, from horizontal at the equator to vertical at the poles. At high inclinations (near poles), the positive lobe of the anomaly is centered above the source. At low inclinations (near the equator), the lobes rotate so the positive and negative components appear side by side, and the peak is offset horizontally from the source. This means reading an anomaly peak location as the source location would give an incorrect result at low latitudes. Reduction to the pole corrects for this, making the anomaly symmetric and centered above the source regardless of survey latitude."
  explanation: "The practical implication is that naively identifying source locations from raw anomaly maps is unreliable except near the magnetic poles. Geophysicists routinely apply reduction to the pole (or reduction to the equator) as a preprocessing step before interpretation. Understanding this latitude dependence also explains why comparing magnetic surveys from different parts of the world requires normalizing for field inclination — the same anomaly shape means something very different at 70°N versus 10°N."
```

## Explainer

From your work with Earth's magnetic dipole field, you know that Earth's background field is approximately that of a large dipole. When we conduct a magnetic survey, what we actually measure are small deviations from this background — **anomalies** caused by rocks with contrasting magnetic properties. The fundamental building block for interpreting these anomalies is the **magnetic dipole**, the simplest possible magnetic source, which produces a characteristic spatial pattern that depends on its strength, depth, and the direction it points.

Unlike gravity anomalies, which are always positive for excess mass and negative for mass deficits, magnetic anomalies are inherently more complex because magnetic fields are **dipolar**. Every magnetic source has both a north and south pole, and the anomaly it produces has both positive and negative lobes. The shape of these lobes depends critically on the **inclination** (the angle of Earth's background field from horizontal) and the **declination** (the deviation from geographic north). At the magnetic poles, where the field is vertical, a buried magnetized body produces a symmetric anomaly centered directly above it. At the magnetic equator, where the field is horizontal, the anomaly is antisymmetric — the positive and negative lobes are side by side, and the peak is offset from the source. At intermediate latitudes, you get an asymmetric combination that can be quite confusing to interpret without correction.

This is why **reduction to the pole** (a prerequisite concept) is so valuable — it mathematically transforms the data as if the survey were conducted at the north magnetic pole, simplifying anomaly shapes into symmetric patterns centered over their sources. Once reduced, interpretation becomes more intuitive. **Forward modeling** takes the opposite approach: you propose a 3D body with specified magnetization (direction and intensity), geometry, and depth, then calculate what anomaly it would produce at the surface and compare with observations. By iteratively adjusting the model, you converge on a geologically plausible source. **Inversion** automates this process, systematically searching for the distribution of magnetization that best explains the observed data subject to regularization constraints.

The practical power of dipole modeling lies in its scalability. A large ore body, an igneous intrusion, or even a buried archaeological artifact can each be approximated as one or a few dipoles for initial analysis. The magnetic moment (product of magnetization and volume) tells you how much magnetic material is present, while the anomaly width constrains depth — wider anomalies come from deeper sources, following the same geometric spreading that governs all potential fields. For detailed work, complex bodies are discretized into many small blocks, each treated as a dipole, and the total anomaly is computed as a superposition. This approach connects directly to 3D magnetic inversion, where the goal is to recover a magnetization model of the subsurface from thousands of surface measurements.
