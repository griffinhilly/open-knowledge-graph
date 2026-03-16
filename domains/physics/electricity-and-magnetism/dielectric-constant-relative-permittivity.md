---
id: dielectric-constant-relative-permittivity
title: Dielectric Constant and Relative Permittivity
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: dielectrics
  type: hard
- id: electric-field
  type: hard
- id: capacitance
  type: hard
builds-toward:
- electric-field-in-dielectrics
- boundary-conditions-em-fields
tags:
- dielectrics
- material properties
- permittivity
stage: formal-systems
status: draft
---

# Dielectric Constant and Relative Permittivity

## Core Idea
The relative permittivity κ (dielectric constant) describes how a material responds to an electric field. The absolute permittivity is ε = κε₀. When a dielectric is placed in an external field, it becomes polarized, creating an internal field that partially cancels the external field. The displacement field satisfies D = ε₀κE.

## How It's Best Learned
Look up dielectric constants for common materials and relate to molecular polarity. Derive how the field inside a dielectric is reduced: E_inside = E_outside/κ.

## Common Misconceptions
- Dielectric constant is absolute permittivity (κ is dimensionless relative quantity).
- Dielectrics 'block' the electric field (they reduce it, not eliminate it).
- All dielectric constants are greater than 1 (this is true for normal materials at low frequencies).

## Explainer

When you learned about electric fields, you saw that charges create fields in empty space. But most real-world capacitors and devices are filled with materials — plastics, glass, water — and these materials respond to electric fields in a subtle way. The **relative permittivity** κ (also called the **dielectric constant**) is the number that quantifies this response. It tells you how much more electric field a material can accommodate compared to vacuum: a material with κ = 4 can support four times as much stored charge for the same applied voltage.

The physical mechanism is polarization. When you studied dielectrics, you saw that an external electric field shifts positive and negative charges inside molecules very slightly — stretching them apart into tiny **electric dipoles**. These induced dipoles collectively produce their own electric field that points *opposite* to the external field. The result is partial cancellation: the total field inside the material is E_inside = E_outside/κ. The material hasn't blocked the field — it has weakened it by κ. This is why inserting a dielectric between capacitor plates increases capacitance by a factor of κ: the reduced field means you can add more charge before the voltage limit is reached.

To handle this cleanly in Maxwell's equations, physicists introduce the **displacement field** D. Recall that in vacuum, Gauss's law reads ∇·E = ρ_free/ε₀. Inside a material, bound charges on polarized molecules also contribute, complicating the bookkeeping. The displacement field absorbs this complexity: D = ε₀κE = εE, where ε = κε₀ is the **absolute permittivity** of the material. With this definition, Gauss's law takes the same clean form ∇·D = ρ_free — only free (externally placed) charges appear on the right. The material's internal response is hidden inside ε. This is why engineers work with ε rather than ε₀ when designing circuits with dielectric-filled capacitors.

The value of κ reflects the microscopic character of the material. Nonpolar molecules like many plastics have κ ≈ 2–4 (small induced dipoles). Water has κ ≈ 80 because its permanent molecular dipoles can rotate to align with the field — a much stronger polarization response. As you go on to study boundary conditions for electromagnetic fields at material interfaces, κ will appear naturally in the continuity conditions for D, determining how field lines bend at dielectric boundaries. The concept also generalizes to frequency-dependent permittivity in AC fields, where κ becomes a complex number capturing both energy storage and absorption — the foundation of microwave and optical material physics.
