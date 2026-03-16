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
stage: abstract-reasoning
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

## Explainer

Calorimetry is the application of energy conservation — your prerequisite — to heat exchange. Conservation of energy says energy cannot be created or destroyed; in a thermally isolated system, total energy is fixed. Calorimetry turns this into a measurement tool: if you can measure how much one object's temperature changes, and you know its **specific heat capacity**, you can calculate how much heat flowed — and by conservation, that equals the heat gained or lost by everything else in the system.

The central equation is Q_lost + Q_gained = 0, which means the heat released by the hot substance exactly equals the heat absorbed by the cool one. Each term is calculated using Q = mcΔT, where m is mass, c is specific heat capacity, and ΔT = T_final − T_initial. When you drop a hot metal block into cool water in an insulated cup, the metal cools and water warms until they reach a common final temperature. Setting up the energy balance: m_metal × c_metal × (T_f − T_metal) + m_water × c_water × (T_f − T_water) = 0. The single unknown — usually T_f or one of the specific heats — can be solved for directly.

Sign conventions are where most errors occur. Define Q > 0 as heat entering a substance. The hot object has a negative ΔT (it cools), so its Q is negative — it lost heat. The cool object has a positive ΔT, so its Q is positive — it gained heat. The conservation equation ensures these sum to zero. A common mistake is to average the two initial temperatures to find T_f — this ignores differences in mass and specific heat and is only correct when both are equal. If a phase change occurs during the process, a latent heat term Q = mL must be added for the substance undergoing the transition, where L is the latent heat per unit mass.

Two important calorimeter designs capture different physical situations. A **coffee-cup calorimeter** is open to the atmosphere and operates at constant pressure; the heat measured is ΔH, the enthalpy change, which chemists call the heat of reaction. A **bomb calorimeter** is a sealed steel vessel operating at constant volume; the heat measured is ΔU, the change in internal energy. For reactions involving only solids and liquids, the difference is small. For reactions that produce or consume gases, ΔH = ΔU + ΔnRT, where Δn is the moles of gas produced. Understanding which instrument you're using ensures you're measuring the thermodynamic quantity you actually need.
