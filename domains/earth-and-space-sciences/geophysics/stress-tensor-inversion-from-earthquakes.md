---
id: stress-tensor-inversion-from-earthquakes
title: Stress Tensor Inversion from Focal Mechanisms
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: focal-mechanisms-and-stress-tensors
  type: hard
- id: moment-tensor-inversion
  type: hard
builds-toward:
- coulomb-stress-transfer-faults
tags:
- seismic
- stress
- inversion
- focal-mechanisms
stage: expert
status: validated
---

# Stress Tensor Inversion from Focal Mechanisms

## Core Idea
Focal mechanisms from earthquake populations can be inverted to determine the regional stress tensor (principal stress orientations and relative magnitudes). Methods like the Michael method assume earthquakes occur on planes optimally oriented for slip given the stress state. Stress tensors inferred from seismicity illuminate plate boundary mechanics and lithospheric stress states.

## Questions

```yaml
- question: "A seismologist inverts 300 focal mechanisms from a transform fault zone. Which quantities can the stress tensor inversion reliably determine, and which cannot?"
  type: multiple-choice
  options:
    - "It determines the absolute magnitudes of σ₁, σ₂, and σ₃ in MPa, but not their orientations"
    - "It determines the orientations of the three principal stress axes and the stress ratio R = (σ₂ − σ₃)/(σ₁ − σ₃), but not the absolute magnitudes of the stresses"
    - "It determines all six independent components of the full stress tensor, including absolute magnitudes"
    - "It determines only whether the tectonic regime is compressional, extensional, or strike-slip — nothing more"
  answer: 1
  explanation: "The reduced stress tensor has four parameters: the three principal stress axis orientations and the stress ratio R, which describes the relative shape of the stress ellipsoid. Absolute magnitudes of stress are not recoverable from focal mechanism data alone — focal mechanisms record slip direction, which depends on stress orientations and relative magnitudes (R), but not the absolute scale of the stresses. Obtaining absolute magnitudes requires independent measurements like borehole breakouts or hydraulic fracturing."

- question: "A colleague argues that a single, well-constrained focal mechanism from a M6.5 earthquake is sufficient to determine the regional stress tensor. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — one focal mechanism from a large earthquake fully constrains the regional stress state"
    - "A single focal mechanism only reveals the geometry of slip on one fault plane; it takes many focal mechanisms from faults with different orientations to overdetermine the stress tensor, because each provides only one constraint on the shear traction direction"
    - "Focal mechanisms from large earthquakes are less reliable than those from small ones for stress inversion"
    - "The colleague is wrong only because M6.5 earthquakes are too shallow for stress inversion methods"
  answer: 1
  explanation: "A single focal mechanism constrains the shear traction direction on one fault plane, which is consistent with many possible stress tensors. The inversion requires multiple focal mechanisms from faults with different orientations to overdetermine the system: each provides one equation relating the unknown stress tensor to the observed slip direction (via the Wallace-Bott hypothesis). A single observation leaves the system massively underdetermined."

- question: "The Wallace-Bott hypothesis used in stress tensor inversion assumes that earthquake slip on a fault occurs in the direction of maximum resolved shear stress on that fault plane."
  type: true-false
  answer: true
  explanation: "This is the foundational physical assumption linking individual earthquake focal mechanisms to the regional stress field. For a fault plane sitting in a known stress field, the shear traction direction on the plane is geometrically determined by the fault's orientation relative to the principal stress axes. The Wallace-Bott hypothesis says the slip vector parallels this shear traction direction. Each focal mechanism then provides a constraint: the observed slip direction should match the predicted shear traction direction for the best-fitting stress tensor."

- question: "Stress tensor inversion from earthquake focal mechanisms can determine the absolute magnitudes of the principal stresses, allowing engineers to directly calculate the force per unit area acting on structures at depth."
  type: true-false
  answer: false
  explanation: "Stress tensor inversion recovers only the reduced stress tensor: the orientations of the three principal stress axes and the stress ratio R. It cannot determine absolute stress magnitudes because focal mechanisms record slip directions, which depend on stress axis orientations and the relative shape of the stress ellipsoid (R), not the absolute scale. Absolute stress magnitudes require independent measurements such as borehole breakouts, hydraulic fracturing tests, or overcoring, which measure actual forces acting on the rock."

- question: "Why does stress tensor inversion require many focal mechanisms rather than just one, and what assumption connects individual earthquake slip directions to the regional stress state?"
  type: short-answer
  answer: "The Wallace-Bott hypothesis provides the link: it assumes each earthquake slips in the direction of maximum resolved shear stress on its fault plane. This means each focal mechanism provides one observed shear traction direction — one constraint on the unknown stress tensor. But the reduced stress tensor has four parameters (three principal axis orientations plus the stress ratio R), and any single focal mechanism is consistent with a wide range of stress states. Only by combining many focal mechanisms from faults with different orientations does the system become overdetermined, allowing least-squares inversion to find the stress tensor that best fits all observations simultaneously. More focal mechanisms improve robustness, quantifiable via bootstrap resampling."
  explanation: "The analogy is triangulation: a single bearing tells you a direction but not a location; multiple bearings from different vantage points pin down the target. Here, each focal mechanism gives a bearing on the stress state from one fault geometry; the collection of many constrains the four-parameter reduced stress tensor."
```

## Explainer

From your work with focal mechanisms, you know that each earthquake's radiation pattern reveals the geometry of faulting — the orientation of the fault plane and the direction of slip. From moment tensor inversion, you know how to extract this information from seismic waveforms. **Stress tensor inversion** asks the inverse question: given many earthquakes, each with its own focal mechanism, what single stress field could have caused all of them to slip the way they did?

The physical foundation is the **Wallace-Bott hypothesis**: slip on a fault occurs in the direction of maximum resolved shear stress on that fault plane. Imagine you have a regional stress field — three principal stress axes (σ₁ > σ₂ > σ₃) with fixed orientations. Any fault plane sitting in this stress field will experience a shear traction that points in a specific direction on that plane, determined by the fault's orientation relative to the stress axes. The Wallace-Bott assumption says the earthquake slip vector should parallel this shear traction direction. So each focal mechanism is an observation of the shear traction direction on one particular fault plane, and the collection of many such observations constrains the stress tensor that generated them all.

The **Michael (1984) method** is the most widely used approach. It formulates the problem as a linear inverse problem: given N focal mechanisms (each providing a fault plane orientation and a slip direction), find the four parameters that define the reduced stress tensor — the orientations of σ₁, σ₂, and σ₃ plus the **stress ratio** R = (σ₂ − σ₃)/(σ₁ − σ₃). Note that the inversion cannot determine absolute stress magnitudes, only the principal directions and the relative shape of the stress ellipsoid. The method minimizes the angular misfit between the observed slip directions and those predicted by the best-fitting stress tensor. Because each focal mechanism has a fault-plane ambiguity (two nodal planes, only one of which actually slipped), the algorithm must either try both planes or use external information to select the correct one.

Robustness testing is essential because real focal mechanism catalogs contain errors and may span regions with non-uniform stress. **Bootstrap resampling** randomly resamples the catalog thousands of times, solving the inversion each time, and the scatter in results reveals confidence intervals on the principal stress orientations. If the bootstrap solutions cluster tightly, the stress tensor is well resolved. If they scatter broadly, the data may be too noisy, too few, or the region may contain multiple stress domains that need to be analyzed separately. Some advanced methods (like the Hardebeck and Michael 2006 approach) allow the stress field to vary spatially, solving for a smoothly varying stress tensor on a grid — a damped inversion that balances spatial resolution against data constraints.

The practical payoff is substantial. Stress tensor inversions reveal the tectonic forces driving seismicity: compressional, extensional, or strike-slip regimes become quantitatively characterized. Changes in stress orientation across fault systems, with depth, or over time (before and after large earthquakes) illuminate how the lithosphere partitions and transfers stress. These results feed directly into **Coulomb stress transfer models** that forecast where future earthquakes are more likely — making stress inversion a bridge between observational seismology and seismic hazard assessment.
