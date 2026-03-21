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
stage: advanced
status: draft
---

# Thermal Radiation and Stefan-Boltzmann Law

## Core Idea
Stefan-Boltzmann law states that the total power radiated by a blackbody is proportional to the fourth power of its absolute temperature: P = σAT⁴. Emissivity (ε) accounts for non-ideal surfaces. Radiation is the dominant heat transfer mechanism at high temperatures and requires no medium.

## Questions

```yaml
- question: "A blackbody's temperature doubles from 300 K to 600 K. By what factor does its total radiated power increase?"
  type: multiple-choice
  options:
    - "2 — power scales linearly with temperature"
    - "4 — power scales with the square of temperature"
    - "8 — power scales with the cube of temperature"
    - "16 — power scales with the fourth power of temperature"
  answer: 3
  explanation: "The Stefan-Boltzmann law gives P = σAT⁴. Doubling temperature multiplies power by 2⁴ = 16. This steep T⁴ dependence is why radiation is negligible compared to conduction and convection near room temperature but completely dominates at furnace temperatures or stellar surfaces. Options A and B represent the incorrect intuitions that radiation behaves like conductive or convective heat transfer, which scale roughly linearly with temperature difference."

- question: "A polished silver surface has an emissivity of ε ≈ 0.02. Compared to a blackbody at the same temperature, how does this surface behave?"
  type: multiple-choice
  options:
    - "It emits only 2% as much radiation, but absorbs radiation just as readily as a blackbody"
    - "It emits only 2% as much radiation and also absorbs only 2% as much incident radiation"
    - "It emits full blackbody radiation but reflects most incident radiation away"
    - "It emits 98% as much radiation because polished surfaces are near-perfect emitters"
  answer: 1
  explanation: "By Kirchhoff's law, emissivity equals absorptivity for a body in thermal equilibrium. A surface with ε = 0.02 both emits only 2% as much radiation as a blackbody and absorbs only 2% of incident radiation — the same factor governs both. This is why polished metal surfaces are used in thermos bottles: they suppress both emission and absorption, minimizing radiant heat exchange with surroundings. Option A is the common misconception that emissivity and absorptivity are independent properties."

- question: "Unlike conduction and convection, thermal radiation can transfer heat through a perfect vacuum."
  type: true-false
  answer: true
  explanation: "Thermal radiation is electromagnetic radiation — it requires no medium to propagate. This is why the Sun can heat the Earth across 150 million km of near-vacuum space, and why a glowing iron radiates heat even in a vacuum chamber. Conduction requires direct molecular contact; convection requires a fluid medium for bulk flow. Radiation is the only heat transfer mechanism that works in the absence of matter."

- question: "Because the Stefan-Boltzmann law contains T⁴, radiation is the dominant heat transfer mechanism at all temperatures above absolute zero."
  type: true-false
  answer: false
  explanation: "Although T⁴ grows faster than the linear temperature-difference dependence of conductive and convective heat transfer, at low temperatures (near room temperature) the absolute magnitude of radiated power is still small compared to conduction and convection in most practical situations. Radiation becomes *dominant* only at high temperatures — in furnaces, stellar surfaces, or space — where the T⁴ term pulls decisively ahead. The net radiation also depends on the T⁴ − T₀⁴ difference, which is small when T and T₀ are close."

- question: "Why does doubling the temperature of a radiating body increase its emitted power by a factor of 16 rather than 2, and what practical consequence does this have for engineering design at high temperatures?"
  type: short-answer
  answer: "The Stefan-Boltzmann law states that radiated power scales as T⁴. Doubling T gives (2T)⁴ = 16T⁴ — a 16× increase. This means radiation becomes overwhelmingly more important as temperatures rise: a furnace wall at 1200 K radiates 16 times more than the same wall at 600 K. Engineers designing high-temperature systems (furnaces, rocket nozzles, re-entry vehicles) must account for radiation as the dominant heat transfer mode, even if it was negligible at lower operating temperatures."
  explanation: "The T⁴ dependence comes from integrating the Planck spectrum over all wavelengths — the result of quantum statistical mechanics. Its practical consequence is that radiation 'races ahead' of conduction and convection as temperature rises, which is why emissivity control (low-ε coatings for insulation, high-ε coatings for efficient radiators) is central to high-temperature engineering design."
```

## Explainer

Every object with temperature above absolute zero emits electromagnetic radiation. Unlike conduction (which requires molecular contact) or convection (which requires a fluid medium), **thermal radiation** travels through vacuum — it is how the Sun heats the Earth, how your body loses heat in a cold room, and why a glowing iron looks red. The Stefan-Boltzmann law quantifies this emission with a single compact formula that follows directly from integrating the blackbody spectrum you have already studied.

From blackbody radiation, you know that a perfect absorber emits a continuous spectrum peaked at λ_max = b/T (Wien's displacement law). The Stefan-Boltzmann law is the result of integrating the Planck spectrum over all wavelengths and all emission angles: the total power radiated per unit area is j = σT⁴, where σ = 5.67 × 10⁻⁸ W/(m²·K⁴) is the **Stefan-Boltzmann constant**. The T⁴ dependence is steep: doubling the temperature increases radiated power by a factor of 16. This is why radiation is negligible compared to conduction and convection at room temperature but completely dominates at furnace temperatures or stellar surfaces — the fourth-power scaling races ahead of the linear dependence of conductive and convective heat transfer.

For real surfaces the correction factor is **emissivity** ε, a dimensionless number between 0 and 1 measuring how efficiently a surface radiates compared to a blackbody at the same temperature. A perfect blackbody has ε = 1; polished metals have ε ≈ 0.02–0.1 because they are highly reflective and poor emitters of their own thermal radiation. The net power radiated by a surface at temperature T surrounded by an environment at temperature T₀ is P_net = εσA(T⁴ − T₀⁴). The T₀⁴ term accounts for radiation the surface absorbs from its surroundings — by **Kirchhoff's law**, emissivity equals absorptivity for a body in thermal equilibrium, so the same ε governs both emission and absorption.

Emissivity shapes many engineering and scientific choices. A thermos bottle uses a silver-coated inner wall (ε ≈ 0.02) to suppress radiation heat loss between the inner and outer walls. Solar selective coatings on photovoltaic panels aim for high absorptivity in the visible spectrum (where the Sun's radiation is concentrated) but low emissivity in the infrared (where the warm panel would otherwise radiate away the absorbed energy). In astrophysics the Stefan-Boltzmann law gives a star's luminosity as L = 4πR²σT⁴, relating total energy output to radius and surface temperature. Measuring L spectroscopically and reading T from the peak wavelength allows astronomers to determine stellar radii for objects they can never resolve directly — the entire system of stellar classification rests on these two blackbody results working together.
