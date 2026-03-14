---
id: saturated-superheated-property-regions
title: Saturated and Superheated Property Regions and Tables
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: pure-substance-phase-diagrams
  type: hard
builds-toward:
- rankine-cycle-thermodynamic-analysis
- vapor-compression-refrigeration-cycle
tags:
- property-tables
- saturation
- superheated
stage: advanced
status: draft
---

# Saturated and Superheated Property Regions and Tables

## Core Idea
Saturated properties (subscript 'sat') describe matter at phase equilibrium; a saturated liquid is about to evaporate while a saturated vapor is about to condense. Superheated vapor exists above saturation temperature at a given pressure and has properties tabulated or found from equations of state. Engineering devices like steam turbines and refrigeration components operate across saturation lines, making property table navigation essential.

## How It's Best Learned
Work extensively with steam tables and refrigerant tables: locate saturated properties by pressure or temperature, interpolate in superheated regions, and calculate quality in two-phase regions using x = (u - u_f) / u_fg. Understand the difference between saturation temperature (at fixed pressure) and saturation pressure (at fixed temperature).

## Common Misconceptions
- Quality x is the fraction of liquid; it is the mass fraction of vapor (or dryness).
- Superheated vapor properties do not depend on pressure; pressure determines saturation temperature, then T determines other properties at that pressure.
- Interpolating in property tables gives exact values; property tables are discretized and require careful linear interpolation.
