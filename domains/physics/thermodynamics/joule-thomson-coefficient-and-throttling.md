---
id: joule-thomson-coefficient-and-throttling
title: Joule-Thomson Coefficient and Throttling
domain: physics
course: thermodynamics
prerequisites:
- id: enthalpy-definition-and-significance
  type: hard
- id: partial-derivatives
  type: soft
tags:
- joule-thomson
- throttling
- real-gas
- cooling
stage: formal-systems
status: draft
---

# Joule-Thomson Coefficient and Throttling

## Core Idea
The Joule-Thomson coefficient μ_JT = (∂T/∂P)_H describes temperature change during throttling (isenthalpic) expansion. For ideal gases, μ_JT = 0; real gases deviate. Gases cool (μ_JT > 0) if attractive forces dominate, or heat (μ_JT < 0) if repulsive forces dominate. This is the principle behind refrigeration cycles.

## Questions

```yaml
- question: "A gas is throttled through a valve and its temperature rises. What does this tell us about the gas?"
  type: multiple-choice
  options:
    - "The process was not isenthalpic, so the Joule-Thomson analysis does not apply"
    - "The gas must be below its inversion temperature, where attractive forces dominate"
    - "The gas is above its inversion temperature, where repulsive intermolecular forces dominate"
    - "The gas behaves as an ideal gas at these conditions"
  answer: 2
  explanation: "The sign of the Joule-Thomson coefficient depends on which intermolecular forces dominate. Above the inversion temperature, repulsive forces dominate; as the gas expands, molecules move apart more freely, reducing repulsive potential energy and converting it to kinetic energy — raising temperature (μ_JT < 0). Below the inversion temperature, attractive forces dominate and expansion cools the gas. An ideal gas shows no effect. The isenthalpic constraint still applies in all real-gas cases."

- question: "Why does an ideal gas show no temperature change during throttling (μ_JT = 0)?"
  type: multiple-choice
  options:
    - "Ideal gas molecules have no collisions, so no energy is lost during expansion"
    - "For an ideal gas, H = U + PV depends only on temperature, so conserving H at constant T means T cannot change"
    - "Throttling is not truly isenthalpic for ideal gases, so the analysis does not apply"
    - "The pressure drop exactly cancels the temperature drop in an ideal gas"
  answer: 1
  explanation: "For an ideal gas, internal energy U depends only on temperature (no intermolecular interactions), and PV = nRT also depends only on T. Therefore H = U + PV depends only on T. Throttling conserves H. If H is conserved and H depends only on T, then T cannot change — μ_JT = 0 exactly. Real gases deviate because intermolecular interactions make U depend on molecular separation (volume), so expansion changes the balance of kinetic and potential energy."

- question: "Throttling always cools a gas, which is why it is used in refrigeration."
  type: true-false
  answer: false
  explanation: "Throttling only cools gases that are below their inversion temperature, where attractive intermolecular forces dominate. Above the inversion temperature, throttling heats the gas. This is why gases with low inversion temperatures — like hydrogen (T_inv ≈ 205 K) and helium (T_inv ≈ 40 K) — must be pre-cooled below their inversion temperatures before throttling can be used to liquefy them. Nitrogen (T_inv ≈ 620 K) can be throttled at room temperature to produce cooling."

- question: "The throttling process is isenthalpic — that is, H₁ = H₂ — as an exact consequence of energy conservation."
  type: true-false
  answer: true
  explanation: "This is an exact result, not an approximation. Work-energy bookkeeping shows that the work done on the gas by the high-pressure side (P₁V₁) minus the work done by the gas pushing into the low-pressure region (P₂V₂) equals the change in internal energy: U₂ − U₁ = P₁V₁ − P₂V₂, which rearranges to H₁ = H₂. The apparatus being insulated (no heat exchange) is the only assumption. This makes H the correct thermodynamic potential for analyzing throttling."

- question: "Why must hydrogen be pre-cooled below approximately 205 K before throttling can be used to liquefy it, even though nitrogen can be liquefied by throttling at room temperature?"
  type: short-answer
  answer: "Hydrogen's inversion temperature is about 205 K — below room temperature. Above the inversion temperature, μ_JT is negative, meaning throttling heats the gas rather than cooling it. If you tried to throttle hydrogen starting at room temperature (~293 K), it would warm up. Nitrogen's inversion temperature (~620 K) is well above room temperature, so throttling nitrogen at room conditions does cool it. Hydrogen must first be pre-cooled below its inversion temperature (using liquid nitrogen as a cooling stage) before throttling will produce further cooling toward liquefaction."
  explanation: "The inversion temperature marks the crossover where the dominant intermolecular force shifts from repulsive to attractive. Only below T_inv does expansion work against attractive forces and cool the gas. The Linde liquefaction process stages coolants in exactly this order — nitrogen first, then hydrogen, then helium — each pre-cooling the next gas to below its inversion temperature."
```

## Explainer

You know enthalpy H = U + PV as the natural thermodynamic potential for constant-pressure processes, and you know how to use partial derivatives to relate thermodynamic variables along constrained paths. The Joule-Thomson experiment combines both: by forcing gas through a porous plug or valve, it probes the molecular interactions of real gases through a cleverly constructed isenthalpic constraint — and the result underlies all modern refrigeration and industrial gas liquefaction.

The **throttling process** is analyzed by energy balance, not by assuming a specific mechanism. Gas at high pressure P₁, temperature T₁ is steadily pushed through a porous plug into a region of lower pressure P₂. The work done by the gas pushing into the low-pressure region is P₂V₂; the work done on the gas by the high-pressure side is P₁V₁. The apparatus is insulated (no heat exchange). First-law energy conservation gives U₂ − U₁ = P₁V₁ − P₂V₂, which rearranges to U₁ + P₁V₁ = U₂ + P₂V₂, or **H₁ = H₂**. Throttling is isenthalpic — an exact result from energy conservation, not an approximation. This makes H the right thermodynamic potential: at constant H, the **Joule-Thomson coefficient** μ_JT = (∂T/∂P)_H tells us how temperature changes as pressure drops.

For an **ideal gas**, internal energy depends only on temperature, and PV = nRT, so H = U + PV depends only on T. If H is conserved and H depends only on T, temperature cannot change: μ_JT = 0 for ideal gases. Real gases deviate because intermolecular interactions make U depend on volume (intermolecular separation) as well as temperature. When gas expands, molecules move apart — doing work against their mutual **attractive forces** (negative potential energy becomes less negative), converting kinetic energy to potential energy, lowering temperature. If **repulsive forces** dominate (high temperature, high density), expansion lets molecules move apart *more freely*, reducing the repulsive contribution to potential energy, releasing kinetic energy, and *raising* temperature. The crossover between these regimes is the **inversion temperature** T_inv, where μ_JT changes sign. Below T_inv, throttling cools; above it, throttling heats.

The practical implications are large. Nitrogen has T_inv ≈ 620 K, well above room temperature, so throttling a nitrogen cylinder at room conditions produces useful cooling — the basis of the **Linde process** for industrial air liquefaction. Hydrogen (T_inv ≈ 205 K) and helium (T_inv ≈ 40 K) must be pre-cooled below their inversion temperatures before throttling will cool them further; this is why liquid nitrogen is used as a pre-cooler stage before liquefying hydrogen, and liquid hydrogen before helium. Refrigerators and air conditioners use the same principle in reverse: a refrigerant gas is compressed, cooled by rejecting heat at high pressure, then throttled through an expansion valve to drop to low temperature, where it absorbs heat from the refrigerated space before returning to the compressor. The choice of refrigerant is partly driven by where its inversion temperature and μ_JT values fall relative to the operating temperature range.
