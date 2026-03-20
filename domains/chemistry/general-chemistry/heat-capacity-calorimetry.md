---
id: heat-capacity-calorimetry
title: Heat Capacity and Calorimetry
domain: chemistry
course: general-chemistry
prerequisites:
- id: thermochemistry-enthalpy
  type: hard
builds-toward:
- entropy-and-gibbs-free-energy
tags:
- specific-heat
- heat-capacity
- calorimetry
- coffee-cup-calorimeter
- bomb-calorimeter
- q-equals-mcDeltaT
stage: advanced
status: draft
---
# Heat Capacity and Calorimetry

## Core Idea
Heat capacity is the amount of heat required to raise the temperature of a substance by one degree. Specific heat capacity (c) is heat capacity per gram (J/g·°C), while molar heat capacity is per mole. The foundational equation q = mcΔT relates heat (q), mass (m), specific heat (c), and temperature change (ΔT). In calorimetry, heat lost by one substance equals heat gained by another (assuming no heat loss to surroundings). A coffee-cup calorimeter measures enthalpy changes at constant pressure for solution-phase reactions, while a bomb calorimeter measures internal energy changes at constant volume for combustion reactions.

## How It's Best Learned
Solve calorimetry problems by setting q(lost) = −q(gained) and solving for the unknown. Practice distinguishing between constant-pressure calorimetry (ΔH) and constant-volume calorimetry (ΔE). Use water's specific heat (4.184 J/g·°C) as a reference point to develop intuition for the relative heat capacities of other materials.

## Common Misconceptions
- Temperature and heat are not the same. Temperature measures average kinetic energy; heat is the total energy transferred. A large mass of water at 30°C contains more thermal energy than a small mass at 80°C.
- Bomb calorimetry measures ΔE (constant volume), not ΔH (constant pressure). For reactions involving gases, ΔH = ΔE + ΔnRT, though the difference is often small.

## Explainer

From your study of thermochemistry and enthalpy, you know that chemical reactions either release or absorb heat. But how do we actually *measure* that heat in practice? The answer lies in a deceptively simple observation: when heat flows into a substance, its temperature rises by an amount that depends on how much substance is present and what that substance is made of. **Heat capacity** is the property that quantifies this relationship — it tells you how much energy a substance can absorb per degree of temperature change.

The foundational equation is **q = mcΔT**, where q is the heat transferred (in joules), m is the mass (in grams), c is the **specific heat capacity** (in J/g·°C), and ΔT is the temperature change. Specific heat capacity varies dramatically between materials: water's specific heat is 4.184 J/g·°C, which is unusually high — metals like iron (0.449 J/g·°C) or copper (0.385 J/g·°C) heat up much faster with the same energy input. This is why a metal pan gets scorching hot on the stove while the water inside barely warms. Water's high specific heat also explains why coastal climates are milder than inland ones: the ocean absorbs and releases enormous amounts of heat with relatively small temperature swings.

**Calorimetry** applies this equation to measure the heat of chemical reactions. The principle is conservation of energy: heat lost by the reaction equals heat gained by the surroundings (the water and calorimeter). In a **coffee-cup calorimeter** — literally a styrofoam cup with a thermometer — you mix reactants in aqueous solution and measure the temperature change of the water. Since the cup is open to the atmosphere, the pressure is constant, and the heat you measure corresponds directly to the enthalpy change (ΔH) of the reaction. If the temperature rises, the reaction is exothermic (ΔH < 0); if it falls, the reaction is endothermic (ΔH > 0).

A **bomb calorimeter** works differently. The reaction takes place inside a sealed, rigid steel vessel (the "bomb") submerged in water. Because the volume cannot change, this measures the internal energy change (ΔE) rather than enthalpy. Bomb calorimeters are used for combustion reactions, where the large energy release needs containment. The relationship between the two quantities is ΔH = ΔE + ΔnRT, where Δn is the change in moles of gas. For many reactions this correction is small, but it matters when precision counts. The key to accurate calorimetry in either setup is accounting for all heat sinks — the water, the calorimeter walls, the thermometer — and calibrating the calorimeter's own heat capacity so that no energy goes untracked.
