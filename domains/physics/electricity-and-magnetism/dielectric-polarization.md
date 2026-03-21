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

## Questions

```yaml
- question: "A capacitor is charged to voltage V and then disconnected from the battery. A dielectric with κᵣ = 4 is inserted between the plates. What happens to the electric field inside the capacitor?"
  type: multiple-choice
  options:
    - "It increases by a factor of 4, because the dielectric amplifies the field"
    - "It decreases to E/4, because the dielectric's bound charges oppose the applied field"
    - "It stays the same — the dielectric only affects capacitance, not the field inside"
    - "It drops to zero, because the dielectric perfectly cancels the applied field"
  answer: 1
  explanation: "Inserting a dielectric reduces the field inside by a factor of κᵣ: E_inside = E_free/κᵣ. The physical mechanism is that the bound surface charges create a field opposing the original field, partially canceling it. With κᵣ = 4, the internal field becomes E/4. Note: if the capacitor were connected to a battery (fixed voltage), the field would remain the same but charge would increase. Here, disconnected from the battery means charge Q is fixed, so reducing the field means voltage across the capacitor also drops by a factor of 4."

- question: "Why does water (κᵣ ≈ 80) reduce the electric field inside it far more than most plastics (κᵣ ≈ 2–4)?"
  type: multiple-choice
  options:
    - "Water is a conductor, so it redistributes charge to cancel the internal field"
    - "Water molecules are permanent electric dipoles that align strongly with applied fields, producing large opposing bound charge sheets"
    - "Water's higher density packs more molecules per unit volume, multiplying the bound charge effect"
    - "Water is transparent to electric fields, allowing them to pass through with reduced strength"
  answer: 1
  explanation: "Water molecules have a permanent dipole moment (they are polar) due to the asymmetric arrangement of hydrogen and oxygen. In an applied field, these permanent dipoles align very effectively, creating a large macroscopic polarization P. This polarization produces bound surface charges whose opposing field is much stronger than what non-polar molecules (like most plastics) can produce through induced dipoles alone. The result: E_inside = E_free/80 for water. Water is an insulator in this context — its large κᵣ comes from polarization, not conduction."

- question: "The electric field inside a dielectric is stronger than the applied external field, because the aligned dipoles add their fields to the original."
  type: true-false
  answer: false
  explanation: "The aligned dipoles create bound surface charges — positive on the face toward the negative plate, negative on the face toward the positive plate. These surface charges produce a field pointing opposite to the applied field, partially canceling it. The net internal field is always weaker than the applied field: E_inside = E_free/κᵣ, where κᵣ ≥ 1. The polarization reduces the field; it does not amplify it."

- question: "If a dielectric is inserted between capacitor plates while the voltage is held constant by a connected battery, the capacitor stores more charge than without the dielectric."
  type: true-false
  answer: true
  explanation: "Capacitance increases by a factor of κᵣ when a dielectric fills the gap: C = κᵣε₀A/d. With fixed voltage V, the charge stored is Q = CV = κᵣε₀AV/d — a factor of κᵣ more than without the dielectric. The battery supplies additional charge to maintain the same voltage while the dielectric's bound charges effectively increase the capacitance. This is the primary practical reason dielectrics are used in capacitors."

- question: "Explain the microscopic mechanism by which a dielectric reduces the electric field inside it. What role do bound charges play, and where do they appear?"
  type: short-answer
  answer: "When an external field is applied, the microscopic dipoles in the dielectric (permanent or induced) align with the field. Inside the bulk, neighboring dipoles cancel — the positive end of one dipole sits next to the negative end of the next. But at the two surfaces perpendicular to the field, this cancellation breaks down: a net sheet of positive bound charge appears on one face and negative bound charge on the other. These surface charge sheets create their own electric field pointing opposite to the applied field, reducing the total field inside to E_inside = E_applied/κᵣ."
  explanation: "The key is that bound charges appear only at surfaces (in a uniform dielectric), not in the bulk. This is because internal dipoles cancel each other. The opposing field from the surface charges is what produces the screening effect. Materials with larger κᵣ align their dipoles more effectively, producing stronger bound surface charge sheets and more screening. This mechanism — macroscopic screening by microscopic dipole alignment — is captured by replacing ε₀ with ε₀κᵣ in Gauss's law, eliminating the need to explicitly track bound charges."
```

## Explainer

You already know the **electric dipole moment**: a pair of equal and opposite charges ±q separated by a small distance d forms a dipole with moment p = qd, pointing from negative to positive. A dielectric material is simply a substance packed with many such dipoles — either permanent ones (polar molecules like water) or ones that can be induced (non-polar molecules whose electron clouds shift when an external field is applied). When you place a dielectric in an electric field, these microscopic dipoles align with the field, all pointing roughly in the same direction.

Now picture what this alignment does at the macroscopic level. Inside the bulk of the material, each positive end of one dipole sits next to the negative end of its neighbor — the bound charges cancel internally. But at the two faces of the material perpendicular to the external field, there is no cancellation: a sheet of positive bound charge appears on one face and a sheet of negative bound charge on the other. These surface charges create their own electric field, pointing *opposite* to the applied field. The result is that the total field inside the dielectric is weaker than the applied field. This is the physical mechanism behind the **polarization** P⃗ — it quantifies, per unit volume, how much dipole moment has been induced and in which direction.

The **relative permittivity** κᵣ (also called the dielectric constant) measures how effective the material is at polarizing and screening the field. κᵣ = 1 for vacuum (no polarization). For typical plastics, κᵣ ≈ 2–4. For water, κᵣ ≈ 80 — meaning water's polar molecules align so strongly with the field that the internal electric field is eighty times weaker than the applied field. The formula E_inside = E_free/κᵣ makes this concrete: inserting a dielectric between capacitor plates while holding the voltage constant increases the stored charge by a factor of κᵣ, which is precisely why dielectrics are used in capacitors.

The macroscopic field equation ∇·(ε₀κᵣE⃗) = ρ_free generalizes Gauss's law to handle materials. In free space, ∇·(ε₀E⃗) = ρ_total, where ρ_total includes both free and bound charges. In a dielectric, the bound charges are automatically accounted for by replacing ε₀ with ε₀κᵣ — you only need to track free charges explicitly. This simplification is the practical payoff: instead of solving for the microscopic bound charge distribution, you fold it all into one material parameter κᵣ and proceed with the familiar form of Gauss's law.
