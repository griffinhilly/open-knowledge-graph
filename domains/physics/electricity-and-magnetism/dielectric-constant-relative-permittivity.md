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
status: validated
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

## Questions

```yaml
- question: "A parallel-plate capacitor holds charge Q and has capacitance C₀ in vacuum. A dielectric with κ = 4 is inserted while charge Q is held fixed. What happens to the capacitance and the electric field inside?"
  type: multiple-choice
  options:
    - "Capacitance increases to 4C₀; field decreases to E₀/4"
    - "Capacitance decreases to C₀/4; field increases to 4E₀"
    - "Capacitance increases to 4C₀; field remains E₀"
    - "Both capacitance and field increase by factor κ"
  answer: 0
  explanation: "Inserting a dielectric multiplies capacitance by κ: C = κC₀. At fixed charge Q, voltage V = Q/C decreases by κ, and since E = V/d, the electric field also decreases to E₀/4. This is the key physical effect: the dielectric's polarization creates an internal field opposing the external field, partially canceling it. The dielectric reduces the field — it doesn't block it or leave it unchanged. Options C and D incorrectly assume the field is unaffected or increases."

- question: "The displacement field D is introduced in Maxwell's equations primarily because:"
  type: multiple-choice
  options:
    - "It is easier to measure directly than the electric field E"
    - "It allows Gauss's law to be written in terms of free charges only, absorbing bound charges from polarization into the material constant ε"
    - "It replaces ε₀ entirely in all electromagnetic equations"
    - "It describes the force on a test charge inside a dielectric"
  answer: 1
  explanation: "Inside a dielectric, polarization creates bound charges that contribute to the total field. Tracking both free and bound charges in Gauss's law is cumbersome. The displacement field D = ε₀κE = εE absorbs the bound-charge contribution into the permittivity ε, so ∇·D = ρ_free — only externally placed charges appear on the right. This preserves the clean mathematical form of Gauss's law. D is a bookkeeping device, not a directly observable force field."

- question: "Inserting a dielectric into a capacitor increases its capacitance because the dielectric's polarization partially cancels the internal electric field, allowing more charge to be stored at the same voltage."
  type: true-false
  answer: true
  explanation: "Polarization creates an internal field opposing the applied field, reducing the total field by factor κ. Since V = E·d, the voltage across the capacitor drops at fixed charge. To restore the original voltage (in a battery-connected scenario), more charge must flow onto the plates — hence capacitance C = Q/V increases to κC₀. The dielectric reduces the field; that reduction is precisely the mechanism that increases capacitance."

- question: "The dielectric constant κ represents the absolute permittivity of a material — a quantity with units of farads per meter."
  type: true-false
  answer: false
  explanation: "κ is the relative permittivity — a dimensionless ratio comparing the material's permittivity to that of free space: κ = ε/ε₀. It has no units. The absolute permittivity is ε = κε₀, which has units of F/m. This distinction matters: κ = 80 for water does not mean the permittivity is 80 farads per meter — it means water's permittivity is 80 times that of vacuum."

- question: "Why does water have a dielectric constant of approximately 80 while nonpolar materials like most plastics have κ ≈ 2–4? Explain in terms of molecular structure."
  type: short-answer
  answer: "Water molecules are permanent dipoles — the electronegative oxygen atom pulls electron density away from the hydrogen atoms, creating a persistent charge separation. When an external electric field is applied, these permanent dipoles rotate to align with the field, producing very strong polarization. Nonpolar molecules have no permanent dipole; they develop only induced dipoles when the external field slightly distorts their electron distributions. Induced dipoles are much weaker than aligned permanent dipoles, resulting in far smaller polarization and a much lower κ."
  explanation: "Strong polarization means stronger opposition to the external field, which means a larger reduction in E_inside, corresponding to a higher κ. Materials with large κ are especially useful in capacitors (ceramics like barium titanate, κ > 1000, are widely used in electronics) and in biological contexts, where water's high κ screens electrostatic interactions between charged molecules."
```

## Explainer

When you learned about electric fields, you saw that charges create fields in empty space. But most real-world capacitors and devices are filled with materials — plastics, glass, water — and these materials respond to electric fields in a subtle way. The **relative permittivity** κ (also called the **dielectric constant**) is the number that quantifies this response. It tells you how much more electric field a material can accommodate compared to vacuum: a material with κ = 4 can support four times as much stored charge for the same applied voltage.

The physical mechanism is polarization. When you studied dielectrics, you saw that an external electric field shifts positive and negative charges inside molecules very slightly — stretching them apart into tiny **electric dipoles**. These induced dipoles collectively produce their own electric field that points *opposite* to the external field. The result is partial cancellation: the total field inside the material is E_inside = E_outside/κ. The material hasn't blocked the field — it has weakened it by κ. This is why inserting a dielectric between capacitor plates increases capacitance by a factor of κ: the reduced field means you can add more charge before the voltage limit is reached.

To handle this cleanly in Maxwell's equations, physicists introduce the **displacement field** D. Recall that in vacuum, Gauss's law reads ∇·E = ρ_free/ε₀. Inside a material, bound charges on polarized molecules also contribute, complicating the bookkeeping. The displacement field absorbs this complexity: D = ε₀κE = εE, where ε = κε₀ is the **absolute permittivity** of the material. With this definition, Gauss's law takes the same clean form ∇·D = ρ_free — only free (externally placed) charges appear on the right. The material's internal response is hidden inside ε. This is why engineers work with ε rather than ε₀ when designing circuits with dielectric-filled capacitors.

The value of κ reflects the microscopic character of the material. Nonpolar molecules like many plastics have κ ≈ 2–4 (small induced dipoles). Water has κ ≈ 80 because its permanent molecular dipoles can rotate to align with the field — a much stronger polarization response. As you go on to study boundary conditions for electromagnetic fields at material interfaces, κ will appear naturally in the continuity conditions for D, determining how field lines bend at dielectric boundaries. The concept also generalizes to frequency-dependent permittivity in AC fields, where κ becomes a complex number capturing both energy storage and absorption — the foundation of microwave and optical material physics.
