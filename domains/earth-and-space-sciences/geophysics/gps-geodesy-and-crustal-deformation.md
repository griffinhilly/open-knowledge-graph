---
id: gps-geodesy-and-crustal-deformation
title: GPS Geodesy and Crustal Deformation Monitoring
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: geoid-determination-and-geodesy
  type: hard
tags:
- geodesy
- gps
- deformation
- monitoring
stage: advanced
status: draft
---

# GPS Geodesy and Crustal Deformation Monitoring

## Core Idea
Global Positioning System (GPS) and modern satellite geodesy measure crustal motions with millimeter precision, revealing plate velocities, interseismic strain accumulation, and coseismic/postseismic deformation. GPS networks constrain plate kinematics, validate plate motion models, and detect uplift or subsidence from loading, volcanism, or groundwater withdrawal. Time-series analysis reveals secular trends and transient signals (slow-slip events, postseismic relaxation), providing constraints on lithospheric rheology and fault mechanical properties.

## Explainer

Your prerequisite work on geoid determination and geodesy established how we define positions on a deforming Earth. GPS geodesy takes that foundation and turns it into a tool for watching the Earth move in real time. The basic idea is simple: a network of GPS receivers bolted to bedrock records their positions continuously, and by tracking how those positions change over weeks, months, and years, we can measure how the crust is deforming. Modern processing achieves horizontal precisions of 1–2 mm/year for velocity estimates, making it possible to detect motions far slower than a fingernail grows.

The most straightforward application is measuring **plate velocities**. Dense GPS networks across plate boundaries confirm and refine the predictions of plate motion models like NUVEL and MORVEL. For example, GPS stations across the Pacific-North American boundary in California show about 46 mm/year of right-lateral motion, distributed across the San Andreas fault system and the Eastern California Shear Zone. But GPS reveals something models based on million-year geological averages cannot: how strain is distributed across a boundary right now, and whether it matches the long-term average or deviates from it.

The real power of GPS emerges in the **earthquake cycle**. Between earthquakes, a locked fault accumulates elastic strain in the surrounding crust — a process called **interseismic strain accumulation**. GPS stations near a locked fault show a velocity gradient: stations far from the fault move at the full plate rate, while stations near the fault are dragged along by the locked patch and move more slowly. This velocity profile can be inverted to estimate the depth and extent of fault locking. When the fault finally ruptures, GPS stations record sudden **coseismic displacements** — jumps in position that map the slip distribution on the fault. After the earthquake, stations continue to move in a decaying pattern called **postseismic deformation**, driven by afterslip on the fault and viscoelastic relaxation of the lower crust and mantle.

GPS has also revealed entirely new phenomena that were invisible before continuous monitoring existed. **Slow-slip events** — episodes where a fault slips over days to weeks without generating detectable seismic waves — were first discovered through GPS time series in the Cascadia subduction zone. These events release energy equivalent to magnitude 6–7 earthquakes but do so silently. GPS networks also detect volcanic inflation and deflation (tracking magma movement beneath volcanoes), glacial isostatic adjustment (the ongoing rebound of Scandinavia and Canada after ice-sheet retreat), and even seasonal loading from groundwater and snow. Each of these signals appears as a characteristic pattern in the GPS time series, and disentangling them is both the challenge and the power of modern geodesy.
