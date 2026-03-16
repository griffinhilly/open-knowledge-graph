---
id: gravimeter-types-calibration
title: Gravimeter Types, Calibration, and Field Operations
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-surveys-and-data-inversion
  type: hard
builds-toward:
- gravity-data-reduction
tags:
- gravimeter
- calibration
- survey
- instruments
stage: advanced
status: draft
---

# Gravimeter Types, Calibration, and Field Operations

## Core Idea
Relative gravimeters (spring-based) measure gravity differences with high precision; absolute gravimeters determine actual g. Drift, temperature sensitivity, and site calibration affect data quality. Base-station networks and careful instrument handling are essential.

## Explainer

From your background in gravity surveys and data inversion, you know that gravity anomalies — tiny variations in gravitational acceleration from place to place — encode information about subsurface density structure. But measuring those anomalies requires instruments sensitive enough to detect changes on the order of microgals (1 μGal = 10⁻⁸ m/s²), which is roughly one billionth of Earth's surface gravity. The instruments that achieve this precision fall into two categories with fundamentally different operating principles.

A **relative gravimeter** measures the *difference* in gravity between two stations rather than the absolute value of g. The most common type is the LaCoste-Romberg spring gravimeter, which uses a zero-length spring — a spring engineered so that its restoring force is proportional to its total length, not just its extension. A test mass hangs on this spring, and when gravity changes, the mass shifts. The operator adjusts a micrometer screw to return the beam to its null position, and the screw reading gives the gravity difference. Modern electronic versions (like the Scintrex CG-series) use electrostatic feedback to keep the mass stationary and record the required restoring force digitally, achieving precisions of a few microgals. The key limitation is **drift**: the spring slowly creeps over time, so readings at the same station will change over hours. Surveys therefore return to a **base station** repeatedly throughout the day, and the drift is removed by assuming it varies linearly (or polynomially) between base-station reoccupations.

An **absolute gravimeter** measures the actual value of g directly, typically by dropping a test mass in a vacuum and tracking its free-fall trajectory with a laser interferometer. The distance-time data are fit to the kinematic equation of free fall, yielding g to precisions better than 1 μGal. Because the measurement is self-contained — based on the definitions of length and time — it does not drift and needs no base-station corrections. However, absolute gravimeters are expensive, heavy, and slow (each measurement takes minutes of stacking drops), so they are used to establish benchmark stations that anchor relative survey networks rather than for dense field surveys.

Field operations for a gravity survey require meticulous attention to calibration and logistics. The gravimeter must be **calibrated** on a known gravity range — a set of stations with established absolute gravity values spanning the expected range of the survey — to convert instrument readings to milligals. Temperature control matters because spring stiffness is temperature-dependent; most modern instruments have internal thermostats, but rapid temperature swings can still introduce noise. Transport shocks can cause "tares" — sudden offsets in the spring's zero position — which show up as unexplained jumps in repeated base-station readings. A well-designed survey loops through base stations frequently enough that both drift and tares can be identified and corrected, ensuring that the subtle density signals you are after are not buried in instrumental artifacts.
