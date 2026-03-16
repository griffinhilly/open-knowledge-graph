---
id: dielectric-polarization
title: Dielectrics and Polarization
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-dipole-moment
  type: hard
builds-toward:
- capacitor-geometry
tags:
- dielectric
- polarization
- permittivity
stage: formal-systems
status: draft
---

# Dielectrics and Polarization

## Core Idea
Dielectric materials contain bound charges that polarize in response to applied electric fields. The polarization P⃗ (dipole moment per unit volume) reduces the net field inside. The relative permittivity κᵣ (dielectric constant) relates the field inside the dielectric to the applied field: E_inside = E_free/κᵣ. The macroscopic field satisfies ∇·(ε₀κᵣE⃗) = ρ_free.

## Explainer

You already know the **electric dipole moment**: a pair of equal and opposite charges ±q separated by a small distance d forms a dipole with moment p = qd, pointing from negative to positive. A dielectric material is simply a substance packed with many such dipoles — either permanent ones (polar molecules like water) or ones that can be induced (non-polar molecules whose electron clouds shift when an external field is applied). When you place a dielectric in an electric field, these microscopic dipoles align with the field, all pointing roughly in the same direction.

Now picture what this alignment does at the macroscopic level. Inside the bulk of the material, each positive end of one dipole sits next to the negative end of its neighbor — the bound charges cancel internally. But at the two faces of the material perpendicular to the external field, there is no cancellation: a sheet of positive bound charge appears on one face and a sheet of negative bound charge on the other. These surface charges create their own electric field, pointing *opposite* to the applied field. The result is that the total field inside the dielectric is weaker than the applied field. This is the physical mechanism behind the **polarization** P⃗ — it quantifies, per unit volume, how much dipole moment has been induced and in which direction.

The **relative permittivity** κᵣ (also called the dielectric constant) measures how effective the material is at polarizing and screening the field. κᵣ = 1 for vacuum (no polarization). For typical plastics, κᵣ ≈ 2–4. For water, κᵣ ≈ 80 — meaning water's polar molecules align so strongly with the field that the internal electric field is eighty times weaker than the applied field. The formula E_inside = E_free/κᵣ makes this concrete: inserting a dielectric between capacitor plates while holding the voltage constant increases the stored charge by a factor of κᵣ, which is precisely why dielectrics are used in capacitors.

The macroscopic field equation ∇·(ε₀κᵣE⃗) = ρ_free generalizes Gauss's law to handle materials. In free space, ∇·(ε₀E⃗) = ρ_total, where ρ_total includes both free and bound charges. In a dielectric, the bound charges are automatically accounted for by replacing ε₀ with ε₀κᵣ — you only need to track free charges explicitly. This simplification is the practical payoff: instead of solving for the microscopic bound charge distribution, you fold it all into one material parameter κᵣ and proceed with the familiar form of Gauss's law.
