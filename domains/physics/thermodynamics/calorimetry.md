---
id: calorimetry
title: Calorimetry
domain: physics
course: thermodynamics
prerequisites:
- id: specific-heat-capacity
  type: hard
- id: conservation-of-energy
  type: hard
builds-toward:
- latent-heat
tags:
- calorimetry
- heat-exchange
- thermal-equilibrium
- conservation-of-energy
stage: formal-systems
status: validated
---

# Calorimetry

## Core Idea
Calorimetry is the experimental measurement of heat exchanged in physical or chemical processes. When two objects at different temperatures are mixed in an insulated container, the heat lost by the hotter object equals the heat gained by the cooler one: Q_lost = Q_gained. This conservation principle allows determination of specific heats, heats of reaction, and latent heats. A bomb calorimeter measures heat at constant volume; a coffee-cup calorimeter approximates constant pressure.

## How It's Best Learned
Set up energy balance equations for mixing scenarios — hot metal into cool water, for example. Pay careful attention to sign conventions: heat leaving one system is heat entering another. Include latent heat terms when phase changes occur.

## Common Misconceptions
- Assuming the final temperature is simply the average of the two initial temperatures ignores differences in mass and specific heat.
- Calorimeters are not perfectly insulated — real experiments must account for heat absorbed by the calorimeter itself.

## Questions

```yaml
- question: "A 100 g metal block at 80°C is dropped into 100 g of water at 20°C in an insulated cup. A student predicts the final temperature will be 50°C by averaging the two initial temperatures. What is wrong with this prediction?"
  type: multiple-choice
  options:
    - "The prediction is correct — equal masses always reach the midpoint temperature"
    - "It ignores the difference in specific heat capacities; water's specific heat is much higher than most metals, so the final temperature will be closer to 20°C than 50°C"
    - "The prediction overcounts the heat exchanged because both objects cool simultaneously"
    - "It is wrong only if the metal undergoes a phase change during cooling"
  answer: 1
  explanation: "The simple average only works when both objects have identical mass AND specific heat capacity. Water has a specific heat of ~4186 J/kg·K while most metals are much lower (~400 J/kg·K). Because water requires far more energy per degree of temperature change, the equilibrium temperature will be much closer to the water's initial temperature. The correct approach is to set m_metal × c_metal × (T_f − 80) + m_water × c_water × (T_f − 20) = 0 and solve for T_f."

- question: "A student dissolves a salt in water inside a coffee-cup calorimeter and observes that the temperature of the solution drops by 4°C. Which conclusion is correct?"
  type: multiple-choice
  options:
    - "The dissolution is exothermic; heat flowed from the solution into the salt"
    - "The dissolution is endothermic; the salt absorbed heat from the water, cooling the solution"
    - "The temperature drop indicates a violation of conservation of energy"
    - "The result is inconclusive because coffee-cup calorimeters only work for temperature increases"
  answer: 1
  explanation: "A temperature drop in the solution means the solution lost thermal energy — it was the 'hot' object that gave up heat. The salt absorbed that heat during dissolution, making the process endothermic (Q_solution < 0, so Q_dissolution > 0). Conservation of energy still holds: heat lost by the solution equals heat gained by the dissolution process. This is exactly how instant cold packs work — ammonium nitrate dissolving in water is endothermic."

- question: "In the standard calorimetry equation Q_lost + Q_gained = 0, the hot object's Q term is negative because its temperature decreases, giving a negative ΔT in Q = mcΔT."
  type: true-false
  answer: true
  explanation: "This is the key to correct sign conventions. Q = mcΔT where ΔT = T_final − T_initial. For the hot object, T_final < T_initial, so ΔT < 0 and Q < 0 — it lost heat. For the cool object, T_final > T_initial, so ΔT > 0 and Q > 0 — it gained heat. Setting up the equation this way (rather than writing |Q_lost| = |Q_gained|) keeps the signs consistent and automatically satisfies conservation of energy."

- question: "A bomb calorimeter is used to measure the enthalpy change ΔH of a combustion reaction."
  type: true-false
  answer: false
  explanation: "A bomb calorimeter is a sealed, rigid vessel — it operates at constant volume, so it measures the change in internal energy ΔU, not enthalpy ΔH. It is the coffee-cup calorimeter (open to the atmosphere, constant pressure) that approximates ΔH. For reactions involving only liquids and solids the difference is small, but for reactions producing gases, ΔH = ΔU + ΔnRT, where Δn is the change in moles of gas. Confusing the two calorimeter types leads to reporting the wrong thermodynamic quantity."

- question: "Why is the final equilibrium temperature in a calorimetry experiment not simply the arithmetic average of the two initial temperatures, even when the masses of the two objects are equal?"
  type: short-answer
  answer: "Because equilibrium temperature depends on both mass and specific heat capacity. The equation Q_lost + Q_gained = 0 expands to m₁c₁(T_f − T₁) + m₂c₂(T_f − T₂) = 0. If the specific heat capacities c₁ and c₂ differ, T_f is a weighted average biased toward the substance with higher heat capacity, not a simple midpoint. For example, water has a much higher specific heat than iron, so mixing equal masses of hot iron and cool water gives a final temperature much closer to the water's initial temperature."
  explanation: "The arithmetic average assumes each degree of temperature change transfers the same amount of heat for both objects, which is only true when mc is identical for both. Specific heat capacity quantifies how much energy is stored per gram per degree — water stores roughly ten times as much as iron. This is why oceans moderate coastal climates: water's high specific heat means it absorbs a huge amount of energy for a small temperature change."
```

## Explainer

Calorimetry is the application of energy conservation — your prerequisite — to heat exchange. Conservation of energy says energy cannot be created or destroyed; in a thermally isolated system, total energy is fixed. Calorimetry turns this into a measurement tool: if you can measure how much one object's temperature changes, and you know its **specific heat capacity**, you can calculate how much heat flowed — and by conservation, that equals the heat gained or lost by everything else in the system.

The central equation is Q_lost + Q_gained = 0, which means the heat released by the hot substance exactly equals the heat absorbed by the cool one. Each term is calculated using Q = mcΔT, where m is mass, c is specific heat capacity, and ΔT = T_final − T_initial. When you drop a hot metal block into cool water in an insulated cup, the metal cools and water warms until they reach a common final temperature. Setting up the energy balance: m_metal × c_metal × (T_f − T_metal) + m_water × c_water × (T_f − T_water) = 0. The single unknown — usually T_f or one of the specific heats — can be solved for directly.

Sign conventions are where most errors occur. Define Q > 0 as heat entering a substance. The hot object has a negative ΔT (it cools), so its Q is negative — it lost heat. The cool object has a positive ΔT, so its Q is positive — it gained heat. The conservation equation ensures these sum to zero. A common mistake is to average the two initial temperatures to find T_f — this ignores differences in mass and specific heat and is only correct when both are equal. If a phase change occurs during the process, a latent heat term Q = mL must be added for the substance undergoing the transition, where L is the latent heat per unit mass.

Two important calorimeter designs capture different physical situations. A **coffee-cup calorimeter** is open to the atmosphere and operates at constant pressure; the heat measured is ΔH, the enthalpy change, which chemists call the heat of reaction. A **bomb calorimeter** is a sealed steel vessel operating at constant volume; the heat measured is ΔU, the change in internal energy. For reactions involving only solids and liquids, the difference is small. For reactions that produce or consume gases, ΔH = ΔU + ΔnRT, where Δn is the moles of gas produced. Understanding which instrument you're using ensures you're measuring the thermodynamic quantity you actually need.
