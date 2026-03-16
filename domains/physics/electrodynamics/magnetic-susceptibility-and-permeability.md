---
id: magnetic-susceptibility-and-permeability
title: Magnetic Susceptibility and Permeability
domain: physics
course: electrodynamics
prerequisites:
- id: magnetic-field-intro
  type: hard
- id: magnetization-and-fields
  type: soft
builds-toward:
- ferromagnetism-microscopic-view
- em-waves-anisotropic-media
tags:
- magnetization
- permeability
- magnetic-materials
stage: advanced
status: draft
---

# Magnetic Susceptibility and Permeability

## Core Idea
Magnetic susceptibility χₘ relates magnetization M to applied field through M = χₘH, while permeability μ relates B to H. Materials are classified as diamagnetic (χₘ < 0), paramagnetic (χₘ > 0), or ferromagnetic (χₘ >> 1 and nonlinear).

## Explainer

When you first studied magnetic fields, you learned about B⃗ in free space or in ideal configurations. But real materials are not empty space — they are filled with atoms whose electrons constitute tiny magnetic dipoles. When you place a material in an external magnetic field, those dipoles can respond, and their collective response modifies the field inside the material. **Magnetic susceptibility** and **permeability** are the quantities that characterize this response.

The framework requires three distinct fields. **B⃗** is the total magnetic flux density — the measurable field that appears in the Lorentz force law. **H⃗** is the **auxiliary field** or magnetic field intensity, defined by H⃗ = B⃗/μ₀ − M⃗; it represents, loosely, the contribution to the field from free currents only, excluding the material's own magnetization. **M⃗** is the **magnetization**, the magnetic dipole moment per unit volume of the material — it captures how much the material has magnetized in response to H⃗. The defining relationship for linear materials is M⃗ = χₘH⃗, where **χₘ** is the dimensionless **magnetic susceptibility**. Combining this with B⃗ = μ₀(H⃗ + M⃗) gives B⃗ = μ₀(1 + χₘ)H⃗ = μH⃗, where **μ = μ₀(1 + χₘ)** is the material's **permeability**.

The sign and magnitude of χₘ classify the material. **Diamagnetic** materials (χₘ < 0, typically −10⁻⁵ to −10⁻³) weakly oppose applied fields — the induced magnetization points against H⃗. This is a quantum effect related to Lenz's law: applied fields induce tiny orbital currents in all atoms that oppose the change, slightly reducing the net field inside. Diamagnetism is universal but very weak. **Paramagnetic** materials (χₘ > 0, typically 10⁻⁵ to 10⁻²) have atoms with permanent magnetic dipole moments (unpaired electrons) that tend to align with the applied field. The alignment is partial because thermal fluctuations fight it — this is why paramagnetic susceptibility increases at lower temperatures (Curie's law). **Ferromagnetic** materials like iron are qualitatively different: χₘ can be hundreds or thousands, the response is highly nonlinear, and the relationship between B and H exhibits **hysteresis** — the material "remembers" its magnetic history. Ferromagnetism arises from quantum mechanical exchange interactions that lock neighboring atomic spins into parallel alignment over macroscopic domains.

The practical consequence of permeability is that fields are amplified inside high-μ materials. A solenoid with an iron core has B ≈ μ_r × μ₀nI instead of just μ₀nI, where μ_r = μ/μ₀ = 1 + χₘ is the **relative permeability**. For iron, μ_r can be 1,000–10,000, which is why transformer cores and electromagnet yokes are made of iron — they concentrate the magnetic field enormously. Understanding χₘ and μ also matters for electromagnetic wave propagation in media: the wave speed becomes c/√(ε_r μ_r), the index of refraction has a magnetic as well as electric component, and in materials with μ_r < 0 (metamaterials), exotic wave behavior including negative refraction becomes possible.
