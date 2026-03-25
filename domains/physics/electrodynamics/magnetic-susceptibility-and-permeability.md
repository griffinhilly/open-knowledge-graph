---
id: magnetic-susceptibility-and-permeability
title: Magnetic Susceptibility and Permeability
domain: physics
course: electrodynamics
prerequisites:
- id: magnetic-field-intro
  type: hard
builds-toward:
- ferromagnetism-microscopic-view
- em-waves-anisotropic-media
tags:
- magnetization
- permeability
- magnetic-materials
stage: expert
status: validated
---

# Magnetic Susceptibility and Permeability

## Core Idea
Magnetic susceptibility χₘ relates magnetization M to applied field through M = χₘH, while permeability μ relates B to H. Materials are classified as diamagnetic (χₘ < 0), paramagnetic (χₘ > 0), or ferromagnetic (χₘ >> 1 and nonlinear).

## Questions

```yaml
- question: "An iron core with relative permeability μ_r = 5000 is inserted into a solenoid with n turns per meter carrying current I. How does the magnetic flux density B inside change compared to the air-core solenoid?"
  type: multiple-choice
  options:
    - "B increases by a factor of 5000, because B = μ_r μ₀ nI"
    - "B stays the same; the iron core only affects H, not B"
    - "B decreases because iron is diamagnetic and opposes applied fields"
    - "B increases by a factor of √5000 because permeability enters as a square root"
  answer: 0
  explanation: "For a linear magnetic material, B = μH = μ_r μ₀ H. In a solenoid, H = nI regardless of the core material (H is determined by free currents). So B = μ_r μ₀ nI — a factor of μ_r larger than the air-core case B = μ₀ nI. With μ_r = 5000, the field is enhanced 5000-fold. This is why transformer and electromagnet cores are made of iron: high permeability concentrates the magnetic flux enormously. Iron is ferromagnetic, not diamagnetic, so it enhances rather than opposes the field."

- question: "What physical quantity does the auxiliary field H represent in a magnetic material, and how does it differ from B?"
  type: multiple-choice
  options:
    - "H represents the total magnetic field including both free currents and magnetization; B represents only the free-current contribution"
    - "H is defined by H = B/μ₀ − M and represents the field due to free currents alone, excluding the contribution of the material's own magnetization"
    - "H and B represent the same physical quantity measured in different unit systems"
    - "H is the externally applied field before the material is inserted; B is the field after the material is inserted"
  answer: 1
  explanation: "H is defined by H = B/μ₀ − M, which isolates the contribution from free currents (those under experimental control, like current in a coil) from the magnetization M (the material's own magnetic response). B is the total field — the one entering the Lorentz force law — and includes both contributions: B = μ₀(H + M). This three-field framework (B, H, M) is necessary because materials magnetize in response to H, and that magnetization feeds back into B. H provides a handle on the externally imposed driving; B captures the physical result."

- question: "Diamagnetic materials are attracted toward regions of stronger magnetic field because χₘ < 0 means they acquire a magnetization in the same direction as the applied field."
  type: true-false
  answer: false
  explanation: "Both clauses are wrong. Diamagnetic materials are *repelled* from regions of stronger field (they are weakly expelled from magnets). And χₘ < 0 means M = χₘH is antiparallel to H — the magnetization opposes the applied field, not aligns with it. This opposing magnetization is why diamagnets are repelled: a magnet induces a magnetization that pushes back. Paramagnetic materials (χₘ > 0) acquire magnetization aligned with H and are attracted toward stronger fields. Superconductors are the extreme diamagnetic case (χₘ = −1), expelling all field from their interior (Meissner effect)."

- question: "The permeability μ and susceptibility χₘ satisfy μ = μ₀(1 + χₘ), so a material with χₘ = 0 (no magnetic response) has permeability μ = μ₀, the same as free space."
  type: true-false
  answer: true
  explanation: "By definition, μ = μ₀(1 + χₘ). When χₘ = 0, the material acquires no magnetization in response to an applied field (M = χₘH = 0), so B = μ₀(H + M) = μ₀H — exactly the free-space relation. A material with χₘ = 0 is magnetically transparent: it neither enhances nor weakens the field inside. Relative permeability μ_r = 1 + χₘ = 1 in this case, confirming the material behaves like vacuum."

- question: "Why are three distinct fields (B, H, and M) needed to describe magnetism in materials, and what does each represent physically?"
  type: short-answer
  answer: "B is the total magnetic flux density — the physical field entering the Lorentz force law and Faraday's law. M is the magnetization — the magnetic dipole moment per unit volume of the material, representing the material's own magnetic response. H is the auxiliary field (H = B/μ₀ − M), representing the contribution from free currents alone, independent of the material's magnetization. Three fields are needed because materials magnetize: an externally applied field (described by H, driven by free currents) induces a magnetization M in the material, which adds to the total field B. Without distinguishing what we control (H) from what the material contributes (M) and what results (B), the feedback between field and material response cannot be cleanly expressed."
  explanation: "The three-field framework is forced by the physics of magnetized media. In free space, B and H are proportional (B = μ₀H) and one field suffices. In a material, the material's own dipoles contribute to B in addition to whatever currents we impose, creating the feedback loop M = χₘH and B = μ₀(H + M). The H field is the clean input (controlled by free currents via ∇ × H = J_free), M is the material's response, and B is the measurable output. Collapsing H and B to a single field would make the constitutive relation circular and hide the causal structure of how materials respond to applied fields."
```

## Explainer

When you first studied magnetic fields, you learned about B⃗ in free space or in ideal configurations. But real materials are not empty space — they are filled with atoms whose electrons constitute tiny magnetic dipoles. When you place a material in an external magnetic field, those dipoles can respond, and their collective response modifies the field inside the material. **Magnetic susceptibility** and **permeability** are the quantities that characterize this response.

The framework requires three distinct fields. **B⃗** is the total magnetic flux density — the measurable field that appears in the Lorentz force law. **H⃗** is the **auxiliary field** or magnetic field intensity, defined by H⃗ = B⃗/μ₀ − M⃗; it represents, loosely, the contribution to the field from free currents only, excluding the material's own magnetization. **M⃗** is the **magnetization**, the magnetic dipole moment per unit volume of the material — it captures how much the material has magnetized in response to H⃗. The defining relationship for linear materials is M⃗ = χₘH⃗, where **χₘ** is the dimensionless **magnetic susceptibility**. Combining this with B⃗ = μ₀(H⃗ + M⃗) gives B⃗ = μ₀(1 + χₘ)H⃗ = μH⃗, where **μ = μ₀(1 + χₘ)** is the material's **permeability**.

The sign and magnitude of χₘ classify the material. **Diamagnetic** materials (χₘ < 0, typically −10⁻⁵ to −10⁻³) weakly oppose applied fields — the induced magnetization points against H⃗. This is a quantum effect related to Lenz's law: applied fields induce tiny orbital currents in all atoms that oppose the change, slightly reducing the net field inside. Diamagnetism is universal but very weak. **Paramagnetic** materials (χₘ > 0, typically 10⁻⁵ to 10⁻²) have atoms with permanent magnetic dipole moments (unpaired electrons) that tend to align with the applied field. The alignment is partial because thermal fluctuations fight it — this is why paramagnetic susceptibility increases at lower temperatures (Curie's law). **Ferromagnetic** materials like iron are qualitatively different: χₘ can be hundreds or thousands, the response is highly nonlinear, and the relationship between B and H exhibits **hysteresis** — the material "remembers" its magnetic history. Ferromagnetism arises from quantum mechanical exchange interactions that lock neighboring atomic spins into parallel alignment over macroscopic domains.

The practical consequence of permeability is that fields are amplified inside high-μ materials. A solenoid with an iron core has B ≈ μ_r × μ₀nI instead of just μ₀nI, where μ_r = μ/μ₀ = 1 + χₘ is the **relative permeability**. For iron, μ_r can be 1,000–10,000, which is why transformer cores and electromagnet yokes are made of iron — they concentrate the magnetic field enormously. Understanding χₘ and μ also matters for electromagnetic wave propagation in media: the wave speed becomes c/√(ε_r μ_r), the index of refraction has a magnetic as well as electric component, and in materials with μ_r < 0 (metamaterials), exotic wave behavior including negative refraction becomes possible.
