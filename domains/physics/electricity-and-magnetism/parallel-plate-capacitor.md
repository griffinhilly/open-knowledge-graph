---
id: parallel-plate-capacitor
title: Parallel Plate Capacitor Geometry and Field
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: capacitance
  type: hard
- id: gauss-law
  type: hard
- id: electric-field
  type: hard
builds-toward:
- capacitor-field-energy-storage
- dielectric-constant-relative-permittivity
tags:
- capacitors
- geometry
- field calculation
stage: formal-systems
status: draft
---

# Parallel Plate Capacitor Geometry and Field

## Core Idea
A parallel plate capacitor consists of two parallel conducting plates separated by distance d with uniform field E = σ/ε₀ between them. The capacitance is C = ε₀A/d, proportional to plate area and inversely proportional to separation. The parallel plate geometry produces a uniform field (neglecting edge effects), making it the simplest capacitor to analyze.

## Explainer

From Gauss's law, you know that an infinite sheet of charge with surface charge density σ produces a field E = σ/(2ε₀), pointing away from the sheet on both sides. The parallel plate capacitor consists of two such sheets facing each other — one carrying +σ, one carrying −σ — separated by a gap d. In the region *between* the plates, the field from each sheet points in the same direction (from + toward −), so they add: E = σ/ε₀. Outside the plates, the fields from the two sheets point in opposite directions and cancel exactly: E = 0. This cancellation — field concentrated inside, absent outside — is the defining feature of the parallel plate geometry and follows directly from the superposition principle applied to Gauss's law results.

The formula for **capacitance** C = ε₀A/d emerges naturally from this field. The voltage between the plates is field times separation: V = Ed = σd/ε₀. The charge stored is Q = σA. Therefore C = Q/V = (σA)/(σd/ε₀) = ε₀A/d. The physical intuitions follow: larger plates hold more charge at the same voltage (bigger A means more Q for the same E), so C grows with A. Closer plates produce a larger field for the same surface charge density, meaning the same Q requires less voltage — so C grows as d shrinks. The formula rewards this reasoning exactly.

The **uniform field** between the plates is what makes this geometry analytically powerful. In a uniform field, the electric potential decreases linearly with distance from the positive plate: V(x) = Ex. A charge placed anywhere between the plates experiences the same force regardless of position. This stands in sharp contrast to point charge fields (which fall off as 1/r²) and makes the parallel plate setup the standard tool for problems requiring controlled, constant electric fields — from electron guns in old cathode-ray tubes to the deflecting plates in oscilloscopes.

The energy stored in a charged capacitor lives in the electric field between the plates. The energy density of an electric field is u = ½ε₀E², and integrating over the volume between the plates (volume = Ad) gives total energy U = ½ε₀E² · Ad = ½(ε₀A/d)V² = ½CV². This equivalence — energy stored in the capacitor equals energy stored in its field — is the starting point for understanding how capacitors store and release energy in circuits, and how energy is stored in electromagnetic fields more generally.
