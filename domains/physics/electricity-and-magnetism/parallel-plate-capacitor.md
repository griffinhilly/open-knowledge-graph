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
status: validated
---

# Parallel Plate Capacitor Geometry and Field

## Core Idea
A parallel plate capacitor consists of two parallel conducting plates separated by distance d with uniform field E = σ/ε₀ between them. The capacitance is C = ε₀A/d, proportional to plate area and inversely proportional to separation. The parallel plate geometry produces a uniform field (neglecting edge effects), making it the simplest capacitor to analyze.

## Questions

```yaml
- question: "Two parallel conducting plates carry surface charge densities +σ and −σ. Using the superposition principle, what is the electric field strength in the region outside the capacitor (beyond either plate)?"
  type: multiple-choice
  options:
    - "σ/ε₀ — both plates contribute fields that add in the exterior region"
    - "σ/(2ε₀) — only the nearer plate contributes outside the capacitor"
    - "Zero — the fields from the two plates cancel exactly outside"
    - "2σ/ε₀ — the exterior field is stronger than the interior field"
  answer: 2
  explanation: "Each plate alone produces a field E = σ/(2ε₀) pointing away from itself on both sides. Outside the capacitor, the +σ plate pushes the field in one direction while the −σ plate pulls it in the opposite direction — they point antiparallel and cancel, giving zero net field. Between the plates, both contributions point in the same direction (from + to −) and add to give σ/ε₀. This cancellation in the exterior is the defining feature of the parallel plate geometry and follows directly from superposition."

- question: "A parallel plate capacitor has capacitance C. If the plate separation is doubled while plate area and charge remain unchanged, what is the new capacitance?"
  type: multiple-choice
  options:
    - "2C — more separation means more room to store charge"
    - "C√2 — separation enters the formula as a square root"
    - "C/2 — capacitance is inversely proportional to plate separation"
    - "C — separation only affects the field, not the capacitance"
  answer: 2
  explanation: "From C = ε₀A/d, doubling d halves C. Physically: with the same charge Q spread over the same area, the field E = σ/ε₀ is unchanged, but voltage V = Ed doubles (because the plates are farther apart). Since C = Q/V, doubling V at constant Q means C is halved. Option A reverses the relationship — larger separation requires more voltage to maintain the same charge, which means lower capacitance, not higher."

- question: "The electric field between the plates of a parallel plate capacitor is exactly twice the field that either plate alone would produce at the same location."
  type: true-false
  answer: true
  explanation: "Each plate, treated as an infinite sheet with surface charge density σ, produces a field of magnitude σ/(2ε₀) at any point. Between the plates, both contributions point in the same direction (from the positive plate toward the negative plate), so they add: E = σ/(2ε₀) + σ/(2ε₀) = σ/ε₀. This is precisely twice what a single sheet produces. Outside the plates, the contributions point in opposite directions and cancel to zero."

- question: "Increasing the plate area of a parallel plate capacitor while keeping plate separation and total stored charge constant will increase the voltage across the capacitor."
  type: true-false
  answer: false
  explanation: "Larger plate area at constant charge Q means the charge spreads out: surface charge density σ = Q/A decreases. The electric field E = σ/ε₀ therefore decreases, and the voltage V = Ed also decreases. Equivalently, C = ε₀A/d increases, and since V = Q/C, higher C at constant Q gives lower V. The voltage drops when area increases at constant charge — the intuition that 'bigger plates must mean more voltage' is wrong."

- question: "Explain physically why the capacitance of a parallel plate capacitor decreases when the plate separation increases, assuming all else is equal."
  type: short-answer
  answer: "The surface charge density σ = Q/A is unchanged, so the electric field E = σ/ε₀ between the plates is unchanged. But the voltage across the capacitor is V = Ed — it increases linearly with separation d. Since capacitance is C = Q/V, and V grows while Q is fixed, C decreases as d increases. Physically, farther plates mean the same amount of stored charge requires a larger potential difference to maintain — the capacitor is less efficient at storing charge per unit voltage."
  explanation: "An alternative physical intuition: moving the plates farther apart weakens the influence of the charges on each other, so the mutual attraction that drives charge to the plates is reduced. To store the same charge with weaker attraction requires a larger applied voltage. Either way, the formula C = ε₀A/d encodes the inverse relationship cleanly."
```

## Explainer

From Gauss's law, you know that an infinite sheet of charge with surface charge density σ produces a field E = σ/(2ε₀), pointing away from the sheet on both sides. The parallel plate capacitor consists of two such sheets facing each other — one carrying +σ, one carrying −σ — separated by a gap d. In the region *between* the plates, the field from each sheet points in the same direction (from + toward −), so they add: E = σ/ε₀. Outside the plates, the fields from the two sheets point in opposite directions and cancel exactly: E = 0. This cancellation — field concentrated inside, absent outside — is the defining feature of the parallel plate geometry and follows directly from the superposition principle applied to Gauss's law results.

The formula for **capacitance** C = ε₀A/d emerges naturally from this field. The voltage between the plates is field times separation: V = Ed = σd/ε₀. The charge stored is Q = σA. Therefore C = Q/V = (σA)/(σd/ε₀) = ε₀A/d. The physical intuitions follow: larger plates hold more charge at the same voltage (bigger A means more Q for the same E), so C grows with A. Closer plates produce a larger field for the same surface charge density, meaning the same Q requires less voltage — so C grows as d shrinks. The formula rewards this reasoning exactly.

The **uniform field** between the plates is what makes this geometry analytically powerful. In a uniform field, the electric potential decreases linearly with distance from the positive plate: V(x) = Ex. A charge placed anywhere between the plates experiences the same force regardless of position. This stands in sharp contrast to point charge fields (which fall off as 1/r²) and makes the parallel plate setup the standard tool for problems requiring controlled, constant electric fields — from electron guns in old cathode-ray tubes to the deflecting plates in oscilloscopes.

The energy stored in a charged capacitor lives in the electric field between the plates. The energy density of an electric field is u = ½ε₀E², and integrating over the volume between the plates (volume = Ad) gives total energy U = ½ε₀E² · Ad = ½(ε₀A/d)V² = ½CV². This equivalence — energy stored in the capacitor equals energy stored in its field — is the starting point for understanding how capacitors store and release energy in circuits, and how energy is stored in electromagnetic fields more generally.
