---
id: capillary-electrophoresis-separations
title: Capillary Electrophoresis Separations
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
tags:
- capillary electrophoresis
- CE
- electrophoresis
stage: advanced
status: draft
---

# Capillary Electrophoresis Separations

## Core Idea
Capillary electrophoresis separates charged analytes by applying high voltage across a narrow capillary, exploiting differences in charge-to-size ratio. CE offers high resolution, minimal sample requirements, and rapid analysis times.

## Explainer

From your study of electrochemistry, you know that charged species migrate in an electric field — cations toward the cathode and anions toward the anode. **Capillary electrophoresis** (CE) takes this principle and confines it inside a very narrow fused-silica capillary, typically 25–75 micrometers in internal diameter and 30–100 cm long. By applying a high voltage (typically 10–30 kV) across the capillary filled with a buffer solution, ions migrate at speeds determined by their **electrophoretic mobility**, which depends on the ratio of their charge to their hydrodynamic size. Small, highly charged ions move fastest; large, weakly charged ions move slowest. This simple physical principle produces remarkably efficient separations.

What makes CE unique among separation techniques is the role of **electroosmotic flow** (EOF). The inner surface of a silica capillary carries negative charges (deprotonated silanol groups) at typical buffer pH values. These negative charges attract a layer of cations from the buffer, and when voltage is applied, this cation layer drags the bulk solution toward the cathode. The result is a flat flow profile — unlike the parabolic flow in HPLC columns — which means virtually no band broadening from flow dynamics. EOF is usually strong enough to carry even anions (which would otherwise migrate toward the anode) toward the detector at the cathode end, so cations, neutral species, and anions can all be detected in a single run, separated by their different net velocities.

In practice, a CE experiment requires remarkably little: nanoliter injection volumes, a few milliliters of buffer, and a standard UV or fluorescence detector positioned near the capillary outlet. This makes CE ideal for situations where sample is precious — biological fluids, forensic evidence, or single-cell analysis. The technique achieves theoretical plate counts of 100,000 to 1,000,000, far exceeding typical HPLC performance, because the flat EOF profile and narrow capillary minimize all major sources of band broadening. Variants of the technique extend its reach: **capillary zone electrophoresis** (CZE) separates ions in free solution, **micellar electrokinetic chromatography** (MEKC) adds surfactant micelles to separate neutral molecules, and **capillary gel electrophoresis** (CGE) uses a gel-filled capillary for size-based separations of proteins and DNA fragments.
