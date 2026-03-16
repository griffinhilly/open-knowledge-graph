---
id: nondestructive-evaluation-and-testing
title: Nondestructive Evaluation and Inspection Methods
domain: engineering
course: materials-science
prerequisites:
- id: mechanical-testing-methods
  type: soft
- id: x-ray-diffraction-materials
  type: soft
tags:
- nondestructive
- inspection
- ultrasonic
- eddy-current
- radiography
stage: formal-systems
status: draft
---

# Nondestructive Evaluation and Inspection Methods

## Core Idea
Nondestructive evaluation techniques assess material condition, detect defects, and identify property variations without damage. Ultrasonic testing uses sound waves to detect internal flaws. Eddy current detects surface and near-surface defects via electromagnetic induction. Radiography reveals internal voids. Thermography identifies heat-flow anomalies. These methods enable in-service inspection of critical components.

## Explainer

Every destructive test you have studied — tensile testing, Charpy impact, hardness testing — destroys the specimen. That is acceptable for quality control of raw materials, but useless for inspecting a bridge, an aircraft wing, or a pressure vessel already in service. **Nondestructive evaluation (NDE)** solves this problem by probing the material with physical fields — sound waves, electromagnetic fields, X-rays, heat — and interpreting the response to infer internal condition without any damage. The challenge in every NDE method is converting a raw sensor signal into a reliable conclusion about whether a defect exists, where it is, and how serious it is.

**Ultrasonic testing (UT)** is the workhorse of subsurface NDE. A piezoelectric transducer emits a high-frequency sound pulse (typically 1–10 MHz) into the material; the wave travels through the bulk, reflects from any discontinuity (a crack, void, inclusion, or the back wall), and the reflected echo returns to the transducer. The time delay gives the depth of the reflector, and the amplitude of the echo relates to the reflector's size and orientation. The method works best for planar cracks oriented perpendicular to the beam; cracks parallel to the beam can be missed entirely. **Phased array ultrasound** uses multiple transducers whose firing delays can be electronically steered to sweep the beam angle and focus at different depths, producing a cross-sectional image of the inspection volume.

**Eddy current testing (ECT)** uses electromagnetic induction. An alternating current in a coil induces circulating **eddy currents** in any nearby conductive material. A crack or void disrupts the eddy current flow, changing the impedance of the coil — a change the instrument detects and localizes. Eddy currents are concentrated near the surface (skin depth effect), so ECT is most sensitive to surface and near-surface defects, typically within a few millimeters. It is extensively used on aircraft fuselage skins, turbine blades, and heat exchanger tubes where surface cracking is the primary concern. ECT cannot penetrate deeply into thick sections.

**Radiographic testing (RT)** passes X-rays or gamma rays through the part; denser material absorbs more radiation, and voids or inclusions create contrast on a film or digital detector on the far side. Radiography excels at detecting volumetric flaws (porosity, inclusions, incomplete fusion in welds) and gives a two-dimensional projection image of the internal structure. Its limitations are the need to access both sides of the part, radiation safety requirements, and reduced sensitivity to cracks oriented parallel to the beam. **Thermographic testing** uses an infrared camera to detect temperature non-uniformities after the surface is thermally excited (flash lamp or hot air): subsurface voids and delaminations insulate the surface above them, producing hot spots that the camera resolves. Thermography is fast, non-contact, and well suited to composites where delaminations are common.

Selecting the right NDE method requires matching the physics of the method to the type of defect expected and the geometry of the part. Surface cracks in a conductive part → eddy current. Subsurface cracks in a thick metallic forging → ultrasound. Internal porosity in a weld → radiography. Delaminations in a composite panel → thermography or ultrasound. In critical applications (aircraft, nuclear, pipeline), multiple methods are combined: one to screen a large area quickly, another to characterize detected indications in detail. The reliability of NDE is quantified by the **probability of detection (POD)** curve — the probability of detecting a crack of size a as a function of a — which sets the minimum detectable flaw size that must be assumed in damage-tolerance calculations.
