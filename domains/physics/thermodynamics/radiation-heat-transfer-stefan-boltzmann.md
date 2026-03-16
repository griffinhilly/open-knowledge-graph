---
id: radiation-heat-transfer-stefan-boltzmann
title: Thermal Radiation and Stefan-Boltzmann Law
domain: physics
course: thermodynamics
prerequisites:
- id: blackbody-radiation
  type: hard
tags:
- radiation
- heat-transfer
- electromagnetic
stage: formal-systems
status: draft
---

# Thermal Radiation and Stefan-Boltzmann Law

## Core Idea
Stefan-Boltzmann law states that the total power radiated by a blackbody is proportional to the fourth power of its absolute temperature: P = σAT⁴. Emissivity (ε) accounts for non-ideal surfaces. Radiation is the dominant heat transfer mechanism at high temperatures and requires no medium.

## Explainer

Every object with temperature above absolute zero emits electromagnetic radiation. Unlike conduction (which requires molecular contact) or convection (which requires a fluid medium), **thermal radiation** travels through vacuum — it is how the Sun heats the Earth, how your body loses heat in a cold room, and why a glowing iron looks red. The Stefan-Boltzmann law quantifies this emission with a single compact formula that follows directly from integrating the blackbody spectrum you have already studied.

From blackbody radiation, you know that a perfect absorber emits a continuous spectrum peaked at λ_max = b/T (Wien's displacement law). The Stefan-Boltzmann law is the result of integrating the Planck spectrum over all wavelengths and all emission angles: the total power radiated per unit area is j = σT⁴, where σ = 5.67 × 10⁻⁸ W/(m²·K⁴) is the **Stefan-Boltzmann constant**. The T⁴ dependence is steep: doubling the temperature increases radiated power by a factor of 16. This is why radiation is negligible compared to conduction and convection at room temperature but completely dominates at furnace temperatures or stellar surfaces — the fourth-power scaling races ahead of the linear dependence of conductive and convective heat transfer.

For real surfaces the correction factor is **emissivity** ε, a dimensionless number between 0 and 1 measuring how efficiently a surface radiates compared to a blackbody at the same temperature. A perfect blackbody has ε = 1; polished metals have ε ≈ 0.02–0.1 because they are highly reflective and poor emitters of their own thermal radiation. The net power radiated by a surface at temperature T surrounded by an environment at temperature T₀ is P_net = εσA(T⁴ − T₀⁴). The T₀⁴ term accounts for radiation the surface absorbs from its surroundings — by **Kirchhoff's law**, emissivity equals absorptivity for a body in thermal equilibrium, so the same ε governs both emission and absorption.

Emissivity shapes many engineering and scientific choices. A thermos bottle uses a silver-coated inner wall (ε ≈ 0.02) to suppress radiation heat loss between the inner and outer walls. Solar selective coatings on photovoltaic panels aim for high absorptivity in the visible spectrum (where the Sun's radiation is concentrated) but low emissivity in the infrared (where the warm panel would otherwise radiate away the absorbed energy). In astrophysics the Stefan-Boltzmann law gives a star's luminosity as L = 4πR²σT⁴, relating total energy output to radius and surface temperature. Measuring L spectroscopically and reading T from the peak wavelength allows astronomers to determine stellar radii for objects they can never resolve directly — the entire system of stellar classification rests on these two blackbody results working together.
