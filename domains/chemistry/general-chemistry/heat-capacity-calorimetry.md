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

## Questions

```yaml
- question: "Two 100 g samples are each supplied with 1,000 J of heat: one sample is water (c = 4.184 J/g·°C) and one is iron (c = 0.449 J/g·°C). Which sample reaches a higher final temperature, and why?"
  type: multiple-choice
  options:
    - "Water, because its high specific heat allows it to store more energy per gram"
    - "Iron, because its low specific heat means the same energy input produces a much larger temperature increase"
    - "Both reach the same final temperature because they received identical amounts of energy"
    - "Iron, because metals conduct heat more efficiently than liquids"
  answer: 1
  explanation: "From q = mcΔT, rearranging gives ΔT = q/(mc). With identical q and m, the sample with the smaller specific heat c shows a larger temperature increase. Iron's specific heat is about nine times smaller than water's, so iron's temperature rises roughly nine times more for the same energy input. This is why a metal pan handle becomes dangerously hot while the water inside barely warms — and why water is such an effective coolant. Option 3 confuses thermal conductivity (how fast heat moves through a material) with specific heat (how much energy is needed per degree of temperature change)."

- question: "A chemist burns a sample inside a sealed, rigid steel vessel submerged in a water bath and measures a temperature rise of 3.5°C. The calorimeter constant is 5.0 kJ/°C. What thermodynamic quantity does this experiment directly measure?"
  type: multiple-choice
  options:
    - "ΔH (enthalpy change at constant pressure)"
    - "ΔG (Gibbs free energy change)"
    - "ΔE (internal energy change at constant volume)"
    - "The activation energy of the combustion reaction"
  answer: 2
  explanation: "The sealed, rigid vessel means the volume cannot change, so no pressure-volume work is done on or by the surroundings. Under constant-volume conditions, the heat flow equals the change in internal energy (ΔE), not enthalpy (ΔH). This is why bomb calorimeters measure ΔE directly. The enthalpy can be calculated afterward using ΔH = ΔE + ΔnRT, where Δn is the moles of gas produced minus consumed. For combustion reactions with significant gas moles, the correction can be non-trivial. The coffee-cup calorimeter (constant pressure, open to atmosphere) measures ΔH directly."

- question: "A large pot of water at 30°C contains more total thermal energy than a small thimble of water at 90°C."
  type: true-false
  answer: true
  explanation: "This illustrates the critical distinction between temperature and heat. Temperature measures the average kinetic energy per molecule — the thimble's molecules are more energetic on average. But total thermal energy depends on both average energy per molecule AND the number of molecules. The large pot has vastly more water molecules, so the total energy stored (q = mcΔT, relative to some reference) can far exceed the thimble's total. This is why the ocean, even at a relatively cool 15°C, stores an enormous amount of thermal energy — enough to significantly moderate coastal climates."

- question: "In a well-insulated coffee-cup calorimeter, if the solution temperature rises after two reactants are mixed, the reaction that occurred was endothermic."
  type: true-false
  answer: false
  explanation: "A temperature rise in the calorimeter solution means heat was released by the reaction into the solution — this is an exothermic reaction (ΔH < 0). In calorimetry, q(reaction) = −q(solution): heat lost by the reaction equals heat gained by the solution. If the solution temperature goes up, the solution absorbed heat, meaning the reaction released heat — exothermic. An endothermic reaction would cool the solution as it draws heat from the surroundings. This sign-convention confusion is one of the most common errors in calorimetry problems."

- question: "A bomb calorimeter and a coffee-cup calorimeter are used to measure the heat of combustion of the same compound. Explain why they give slightly different numerical results, and identify which thermodynamic quantity each one directly measures."
  type: short-answer
  answer: "A coffee-cup calorimeter operates at constant pressure (open to the atmosphere), so the heat measured directly equals the enthalpy change ΔH. A bomb calorimeter operates at constant volume (sealed rigid vessel), so the heat measured directly equals the internal energy change ΔE. The two quantities are related by ΔH = ΔE + ΔnRT, where Δn is the change in moles of gas during the reaction. For combustion reactions that produce or consume gas, Δn ≠ 0, so ΔH and ΔE differ by a small but non-negligible amount. For reactions with no change in gas moles, the two are essentially equal."
  explanation: "The conceptual key is that enthalpy accounts for the energy of expansion against atmospheric pressure (the PV work term), while internal energy does not. In a sealed bomb, no expansion work is possible — all the energy shows up as heat. In an open coffee cup, if the reaction produces gas, some energy goes into pushing back the atmosphere, which is why ΔH (which includes this work) differs from ΔE. For most aqueous reactions with no gas involvement, the difference is negligible."
```

## Explainer

From your study of thermochemistry and enthalpy, you know that chemical reactions either release or absorb heat. But how do we actually *measure* that heat in practice? The answer lies in a deceptively simple observation: when heat flows into a substance, its temperature rises by an amount that depends on how much substance is present and what that substance is made of. **Heat capacity** is the property that quantifies this relationship — it tells you how much energy a substance can absorb per degree of temperature change.

The foundational equation is **q = mcΔT**, where q is the heat transferred (in joules), m is the mass (in grams), c is the **specific heat capacity** (in J/g·°C), and ΔT is the temperature change. Specific heat capacity varies dramatically between materials: water's specific heat is 4.184 J/g·°C, which is unusually high — metals like iron (0.449 J/g·°C) or copper (0.385 J/g·°C) heat up much faster with the same energy input. This is why a metal pan gets scorching hot on the stove while the water inside barely warms. Water's high specific heat also explains why coastal climates are milder than inland ones: the ocean absorbs and releases enormous amounts of heat with relatively small temperature swings.

**Calorimetry** applies this equation to measure the heat of chemical reactions. The principle is conservation of energy: heat lost by the reaction equals heat gained by the surroundings (the water and calorimeter). In a **coffee-cup calorimeter** — literally a styrofoam cup with a thermometer — you mix reactants in aqueous solution and measure the temperature change of the water. Since the cup is open to the atmosphere, the pressure is constant, and the heat you measure corresponds directly to the enthalpy change (ΔH) of the reaction. If the temperature rises, the reaction is exothermic (ΔH < 0); if it falls, the reaction is endothermic (ΔH > 0).

A **bomb calorimeter** works differently. The reaction takes place inside a sealed, rigid steel vessel (the "bomb") submerged in water. Because the volume cannot change, this measures the internal energy change (ΔE) rather than enthalpy. Bomb calorimeters are used for combustion reactions, where the large energy release needs containment. The relationship between the two quantities is ΔH = ΔE + ΔnRT, where Δn is the change in moles of gas. For many reactions this correction is small, but it matters when precision counts. The key to accurate calorimetry in either setup is accounting for all heat sinks — the water, the calorimeter walls, the thermometer — and calibrating the calorimeter's own heat capacity so that no energy goes untracked.
