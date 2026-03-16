---
id: inductively-coupled-plasma-mass-spectrometry-icp-ms
title: 'Inductively Coupled Plasma-Mass Spectrometry: ICP-MS'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: inductively-coupled-plasma
  type: hard
- id: mass-spectrometry-analytical
  type: hard
tags:
- ICP-MS
- trace-analysis
- isotope-analysis
- elemental-mass-spectrometry
stage: advanced
status: draft
---

# Inductively Coupled Plasma-Mass Spectrometry: ICP-MS

## Core Idea
ICP-MS combines the multi-element capability and sensitivity of ICP with mass spectrometric detection, achieving ultra-trace detection limits (ng/L to pg/L) for most elements. Applications include isotope ratio determination, speciation analysis, and trace metal quantitation in biological, environmental, and geological samples with unprecedented sensitivity.

## Explainer

You already understand the two technologies that ICP-MS combines. From your ICP prerequisite, you know that an **inductively coupled plasma** — an argon gas heated to 6,000–10,000 K by radiofrequency energy — atomizes and ionizes virtually every element introduced into it. From your mass spectrometry background, you know that a **mass analyzer** separates ions by their mass-to-charge ratio (m/z) and counts them with extraordinary sensitivity. ICP-MS connects these two capabilities: the plasma serves as an ion source that converts dissolved elements into singly charged positive ions, and the mass spectrometer sorts and counts those ions. The result is an instrument that can detect most elements in the periodic table at concentrations below one part per billion, and many below one part per trillion.

The sample journey through an ICP-MS begins with a liquid solution nebulized into a fine aerosol, which enters the plasma torch. In the plasma, solvent evaporates, molecules dissociate into atoms, and atoms lose one electron to become M⁺ ions. These ions are then extracted from the atmospheric-pressure plasma into the high-vacuum mass spectrometer through a pair of metal cones (the **sampler** and **skimmer** cones) with small orifices. This interface is one of the most critical and delicate parts of the instrument — it must efficiently transfer ions while transitioning from atmospheric pressure to the ~10⁻⁶ torr vacuum the mass analyzer requires. Ion optics then focus the beam, and the mass analyzer (most commonly a quadrupole, though time-of-flight and sector-field instruments exist) filters ions by m/z before they strike an electron multiplier detector.

The primary challenge in ICP-MS is **isobaric and polyatomic interferences**. Because the plasma generates ions from everything in the sample, species with the same nominal mass as your analyte create false signals. The classic example is ⁴⁰Ar¹⁶O⁺ at m/z = 56, which directly overlaps with ⁵⁶Fe⁺ — and since argon is the plasma gas and oxygen comes from the solvent, this interference is always present. **Collision/reaction cells** (CRCs) address this by introducing a gas (helium for kinetic energy discrimination, or hydrogen/ammonia for selective reactions) that destroys polyatomic interferences before they reach the analyzer. High-resolution sector-field instruments can physically resolve many of these overlaps, but at higher cost.

What sets ICP-MS apart from ICP-OES (optical emission) is not just sensitivity but the ability to measure **isotope ratios**. Because the mass analyzer distinguishes ⁶³Cu from ⁶⁵Cu or ²⁰⁶Pb from ²⁰⁷Pb and ²⁰⁸Pb, ICP-MS enables isotope dilution quantification (a primary method requiring no external calibration curve), provenance studies (lead isotope fingerprinting of archaeological artifacts or environmental pollutants), and tracer experiments using enriched stable isotopes. When coupled with chromatographic separation before the plasma (LC-ICP-MS or GC-ICP-MS), it also performs **speciation analysis** — distinguishing, for instance, toxic methylmercury from less harmful inorganic mercury in a fish tissue sample. This combination of ultra-trace sensitivity, multi-element capability, and isotopic information makes ICP-MS the most powerful tool in modern elemental analysis.
