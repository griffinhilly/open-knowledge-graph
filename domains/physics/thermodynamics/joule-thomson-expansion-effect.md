---
id: joule-thomson-expansion-effect
title: Joule-Thomson Expansion and the Joule-Thomson Effect
domain: physics
course: thermodynamics
prerequisites:
- id: real-gas-deviations
  type: hard
- id: heat-and-internal-energy
  type: soft
builds-toward:
- throttling-process-analysis
- rankine-cycle-steam-power
tags:
- real-gases
- refrigeration
- expansion
stage: formal-systems
status: draft
---

# Joule-Thomson Expansion and the Joule-Thomson Effect

## Core Idea
During isenthalpic expansion of a real gas, the temperature changes according to the Joule-Thomson coefficient μ_JT = (∂T/∂P)_H = (V/C_P)(αT - 1), where α is the thermal expansion coefficient. For most gases below the inversion temperature, μ_JT > 0, so pressure decrease causes temperature decrease (cooling); this effect is the basis for many liquefaction processes. Understanding the Joule-Thomson effect requires knowledge of real gas behavior and the relationship between measurable properties.

## How It's Best Learned
Calculate μ_JT for gases using the van der Waals equation. Identify the inversion temperature where μ_JT changes sign. Compare with experimental data.

## Common Misconceptions
- Thinking the Joule-Thomson effect is the same for all gases.
- Confusing it with adiabatic expansion (which changes enthalpy).
- Assuming ideal gases have zero Joule-Thomson coefficient (they do exactly, real gases don't).

## Explainer

From your study of real gas deviations, you know that real molecules attract each other at intermediate distances and repel at short range. These intermolecular forces mean that it costs energy to pull molecules apart — the potential energy of a real gas depends on the average spacing between molecules, which changes with pressure and volume. The Joule-Thomson expansion exploits this dependence to cool gases, and understanding it requires careful accounting of where energy goes during flow through a constriction.

The setup is a **throttling process**: gas flows steadily through a porous plug or valve from high pressure P₁ to low pressure P₂ < P₁, in a thermally insulated tube. No heat enters or leaves (Q = 0). Work is done on the gas as it enters the plug (P₁V₁) and by the gas as it exits (P₂V₂). The first law gives U₂ − U₁ = P₁V₁ − P₂V₂, which rearranges to U₂ + P₂V₂ = U₁ + P₁V₁, or H₂ = H₁. The throttling process is therefore **isenthalpic** — enthalpy is conserved. This is the key constraint, and it distinguishes throttling from adiabatic expansion (which conserves entropy in the reversible case, not enthalpy).

For an ideal gas, internal energy U depends only on temperature (not volume or pressure), and PV = NkT, so H = U + PV = U(T) + NkT = H(T) — enthalpy depends only on temperature. Conserving H therefore means conserving T: ideal gases have no Joule-Thomson effect. But for a real gas, U depends on intermolecular separation (potential energy), and PV ≠ NkT. When pressure drops across the plug, molecules move farther apart on average. At conditions where attractive forces dominate, pulling molecules apart requires energy — this comes at the expense of kinetic energy, so temperature falls. The **Joule-Thomson coefficient** μ_JT = (∂T/∂P)_H quantifies this: positive μ_JT means cooling as pressure drops (the common case below the **inversion temperature**); negative μ_JT means heating.

The inversion temperature T_inv is the temperature above which μ_JT < 0 for a given gas — expansion causes warming rather than cooling. For nitrogen and oxygen, T_inv is well above room temperature (621 K and 764 K respectively), so throttling these gases at ambient conditions always cools them. Hydrogen's T_inv is only about 202 K: at room temperature, throttling hydrogen causes warming. To liquefy hydrogen by throttling, you must first pre-cool it below 202 K. This is why the Linde process for gas liquefaction pre-cools gases through a cascade of refrigeration stages before the final throttling stage that achieves temperatures low enough for liquid formation. The Joule-Thomson effect, rooted entirely in real-gas intermolecular forces, is thus the thermodynamic heart of industrial gas liquefaction.
