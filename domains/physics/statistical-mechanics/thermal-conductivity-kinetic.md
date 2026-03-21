---
id: thermal-conductivity-kinetic
title: Thermal Conductivity from Kinetic Theory
domain: physics
course: statistical-mechanics
prerequisites:
- id: chapman-enskog-expansion
  type: hard
builds-toward: []
tags:
- transport
- kinetic-theory
- heat
stage: advanced
status: draft
---
# Thermal Conductivity from Kinetic Theory

## Core Idea
Thermal conductivity describes heat flow in response to temperature gradients. Kinetic theory shows that hot molecules carry more energy than cold ones; their random motion transports thermal energy. The Chapman-Enskog approach yields κ from first principles, accounting for both translational and internal degrees of freedom.

## Questions

```yaml
- question: "An engineer expects that compressing a gas to twice its pressure will roughly double its thermal conductivity, since twice as many molecules are available to carry heat. Is this reasoning correct?"
  type: multiple-choice
  options:
    - "Yes — more molecules per unit volume means more heat carriers and proportionally higher κ"
    - "No — higher pressure increases molecular density but decreases mean free path proportionally, so the two effects cancel and κ is pressure-independent"
    - "No — κ decreases with pressure because more frequent collisions rapidly dissipate any thermal gradient"
    - "Yes — this is the basis of using high-pressure gases as coolants in industrial applications"
  answer: 1
  explanation: "This is one of kinetic theory's most counterintuitive predictions, confirmed experimentally. κ ~ (1/3) ρ c_v v̄ λ. When pressure doubles, ρ doubles — but λ (the mean free path) halves, because molecules collide twice as often at twice the density. The product ρλ remains constant, so κ is unchanged. The two effects cancel exactly. This pressure-independence was one of Maxwell's surprising early successes with kinetic theory and is well-verified experimentally over many decades of pressure."

- question: "For a monatomic ideal gas, kinetic theory predicts that thermal conductivity κ scales with temperature as:"
  type: multiple-choice
  options:
    - "κ ∝ T (linear in temperature)"
    - "κ ∝ T⁻¹ (decreasing with temperature)"
    - "κ ∝ √T (square root of temperature)"
    - "κ is temperature-independent"
  answer: 2
  explanation: "The mean thermal speed v̄ ∝ √(k_B T / m), and since κ ~ ρ c_v v̄ λ and the product ρλ is pressure-independent, κ grows as v̄ ∝ √T. The Chapman-Enskog result confirms κ = (5/2)(k_B / σ_eff) √(k_B T / πm) ∝ √T. This means hot gases conduct heat better than cold gases — a non-obvious result that distinguishes gases from most solids and liquids, where conductivity typically decreases with temperature."

- question: "Kinetic theory predicts that the thermal conductivity of an ideal gas is independent of pressure, because increasing pressure simultaneously increases molecular density and decreases mean free path, with the two effects exactly canceling."
  type: true-false
  answer: true
  explanation: "The simple mean-free-path estimate κ ~ (1/3) ρ c_v v̄ λ contains the density ρ ~ nM and the mean free path λ ~ 1/(nσ), where n is number density and σ is cross-section. The product ρλ ~ M/σ is independent of n and hence of pressure. This is a genuinely surprising prediction — naively, compressing a gas should make it conduct heat better — and it holds well experimentally over many orders of magnitude of pressure (breaking down only at very low pressures where λ approaches the container size, or very high pressures where molecules interact continuously)."

- question: "Internal degrees of freedom in polyatomic molecules reduce thermal conductivity because energy stored in rotation cannot be transported across a temperature gradient."
  type: true-false
  answer: false
  explanation: "Internal degrees of freedom provide additional channels for energy transport, which INCREASES κ relative to the monatomic case. A rotating molecule can absorb translational kinetic energy in a collision, carry that rotational energy across a temperature gradient, and transfer it to translational motion on the other side. This is an additional transport pathway. The Eucken correction accounts for this by adding the contribution of internal modes to the monatomic result. More channels for energy transport means higher conductivity, not lower."

- question: "Why do kinetic theory derivations show that thermal conductivity and viscosity arise from the same transport mechanism, and how are they related?"
  type: short-answer
  answer: "Both κ (thermal conductivity) and η (viscosity) arise from molecules transporting a conserved quantity down a gradient via random thermal motion and mean-free-path transport. In thermal conductivity, molecules carry energy down a temperature gradient; in viscosity, they carry momentum down a velocity gradient. Because the same mean free path and thermal speed govern both processes, κ and η are proportional: the Eucken relation gives κ = (1/4)(9γ − 5) c_v η. Both are independent of pressure for the same reason (ρλ = constant), and both increase as √T."
  explanation: "This connection is one of kinetic theory's unifying insights: transport coefficients that look macroscopically unrelated (heat flow vs. fluid friction) turn out to be two faces of the same microscopic mechanism — molecules randomly walking across gradients and mixing their properties. The Chapman-Enskog expansion reveals this unity systematically by treating them as different moments of the same distribution-function perturbation."
```

## Explainer

**Fourier's law** states that the heat flux q (energy per unit area per unit time) flowing through a material is proportional to the temperature gradient: q = -κ ∇T, where κ is the thermal conductivity. This is a macroscopic, empirical law — but kinetic theory provides its microscopic derivation. The Chapman-Enskog expansion you've studied produces κ as a systematic result of solving the Boltzmann equation to first order in the gradient. Understanding where κ comes from builds intuition for why different materials conduct heat so differently.

The physical picture starts with a simple thought experiment. Imagine a gas with a temperature gradient in the x-direction: the left side is hotter and the right side cooler. Molecules on the left side have, on average, higher kinetic energy than those on the right. Because molecules are in constant random thermal motion, they travel across the temperature gradient and mix. When a fast (hot) molecule from the left collides with slower (cool) molecules on the right, it transfers energy, carrying heat in the direction of decreasing temperature. The **mean free path** λ — the average distance a molecule travels between collisions — determines how far across the gradient a molecule can carry its excess energy before thermalizing. The **mean thermal speed** v̄ sets how fast this transport happens. Simple mean-free-path analysis gives κ ~ (1/3) ρ c_v v̄ λ, where ρ is mass density and c_v is the specific heat capacity.

The Chapman-Enskog method refines this estimate rigorously by solving the Boltzmann equation perturbatively in the small parameter (λ/L), where L is the macroscopic length scale of the temperature variation. The result for a monatomic ideal gas is κ = (5/2)(k_B / σ_eff) √(k_B T / πm), where σ_eff is an effective collision cross section determined by the intermolecular potential. Several predictions follow immediately: κ is independent of pressure (because higher pressure increases molecular density but decreases λ proportionally — the two effects cancel), it increases with temperature (as v̄ ~ √T grows), and it is larger for lighter gases (which move faster). These are all borne out experimentally.

For polyatomic molecules, the treatment becomes richer because **internal degrees of freedom** — rotation, vibration — also store and transport energy. A rotating molecule can absorb translational energy from a collision and then carry it across the gradient as rotational energy, an additional channel not present for monatomic gases. The Chapman-Enskog calculation must then account for the coupling between translational and internal modes through inelastic collisions, giving a correction factor (the Eucken correction) that modifies the monatomic result. The full result, κ = (1/4)(9γ - 5)(c_v η), where η is viscosity and γ = c_p/c_v, connects thermal conductivity directly to viscosity — both emerge from the same kinetic transport process, differing only in whether molecules carry energy or momentum across the gradient.
