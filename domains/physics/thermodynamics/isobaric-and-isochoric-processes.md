---
id: isobaric-and-isochoric-processes
title: Isobaric and Isochoric Processes
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: hard
builds-toward:
- heat-capacity-of-gases
- heat-engines
tags:
- isobaric
- isochoric
- constant-pressure
- constant-volume
- heat-capacity
stage: formal-systems
status: validated
---

# Isobaric and Isochoric Processes

## Core Idea
An isobaric process occurs at constant pressure; work done is W = PΔV = nRΔT and heat added is Q = nCpΔT. An isochoric (isovolumetric) process occurs at constant volume; no work is done (W = 0), so all heat input goes directly to internal energy: Q = nCvΔT. These processes define the two heat capacities Cp and Cv, which differ for gases because at constant pressure the gas must also do expansion work in addition to raising its temperature.

## How It's Best Learned
Contrast heating water in an open pot (approximately isobaric) with heating a gas in a sealed rigid container (isochoric). Verify that Cp > Cv and derive the Mayer relation Cp − Cv = R using the first law and ideal gas law.

## Common Misconceptions
- Cp > Cv does not mean isobaric heating is less efficient — it means the gas does extra work expanding; total energy input per mole is greater.
- For solids and liquids, Cp ≈ Cv because they expand very little; the difference only matters significantly for gases.

## Explainer

Every thermodynamic process involves exchanging energy as heat and work between a system and its surroundings. But the same amount of heat can produce very different temperature changes depending on what is held constant during the process. The distinction between **isobaric** (constant pressure) and **isochoric** (constant volume) processes is the clearest illustration of why: it determines whether any of the energy input is diverted into doing mechanical work, or whether all of it stays in the system as internal energy.

In an **isochoric process**, the container walls are rigid — volume cannot change. Since W = ∫ P dV = 0, the first law gives ΔU = Q exactly. Every joule of heat added goes directly into raising the internal energy (and thus temperature) of the gas. This defines the **constant-volume heat capacity** Cᵥ: Q = nCᵥΔT. Isochoric heating is in a sense the "pure" temperature-raising process, with no energy leaking away as work.

In an **isobaric process**, the gas expands freely against a constant external pressure as it heats. Now W = PΔV = nRΔT for an ideal gas (from the ideal gas law PV = nRT at constant P), and Q = ΔU + W = nCᵥΔT + nRΔT = n(Cᵥ + R)ΔT. This defines Cₚ = Cᵥ + R — the **Mayer relation**. Cₚ is larger than Cᵥ because you must supply extra heat to do the expansion work in addition to raising the temperature. Imagine heating a gas in an open piston versus a sealed cylinder: the open piston requires more heat input to achieve the same temperature rise, because some energy is "wasted" pushing the piston outward.

The ratio γ = Cₚ/Cᵥ — the **adiabatic index** or heat capacity ratio — is a fundamental parameter that determines the thermodynamic character of a gas. For monatomic ideal gases (3 translational degrees of freedom, Cᵥ = 3R/2), γ = 5/3 ≈ 1.67. For diatomic gases at room temperature (5 degrees of freedom, Cᵥ = 5R/2), γ = 7/5 = 1.4. γ appears throughout thermodynamics: it governs the adiabatic relations (TV^{γ−1} = const, PV^γ = const), the efficiency limits of heat engines, and the speed of sound in a gas (c = √(γRT/M)). The fact that you can measure γ from the speed of sound, or from the ratio of specific heats, means the microscopic degrees of freedom of a gas are directly reflected in its macroscopic acoustic properties — a beautiful connection between molecular structure and thermodynamics.
