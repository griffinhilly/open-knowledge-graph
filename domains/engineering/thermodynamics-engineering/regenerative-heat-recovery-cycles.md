---
id: regenerative-heat-recovery-cycles
title: Regenerative Heat Recovery and Cycle Efficiency
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: rankine-cycle-reheat-regeneration
  type: hard
- id: heat-exchanger-effectiveness-ntu
  type: hard
builds-toward:
- combined-cycles-cogeneration
tags:
- regeneration
- heat-recovery
- feedwater-heating
- efficiency-improvement
stage: advanced
status: draft
---

# Regenerative Heat Recovery and Cycle Efficiency

## Core Idea
Regeneration recovers heat from turbine exhaust to preheat boiler feedwater, reducing fuel input while increasing thermal efficiency. Multiple extraction points with intermediate heaters improve efficiency further. The regenerative efficiency gain depends on the temperature profile of exhaust steam and the number of heating stages; real systems balance efficiency gains against complexity and cost.

## Explainer

From your study of the basic Rankine cycle, you know that efficiency is limited by the temperature ratio between the heat source and the heat sink. One of the thermodynamic losses in a simple Rankine cycle is that cold feedwater (barely above condensate temperature) enters the boiler, requiring a large heat input just to raise the water to saturation temperature before any steam generation even begins. This "cold-end" heat addition happens at relatively low temperatures, dragging down the average temperature at which heat is absorbed and thus reducing efficiency. Regeneration targets this specific loss.

The idea is to extract a fraction of steam from the turbine at an intermediate pressure — call it the **extraction point** — and use that steam to preheat the feedwater before it reaches the boiler. The extracted steam, still carrying significant enthalpy from the high-pressure stages, transfers heat to the subcooled feedwater in a **feedwater heater** (either open or closed type). An open feedwater heater mixes the streams directly; a closed heater transfers heat across a surface. In either case, the boiler now receives warmer feedwater, so it adds less heat to bring the water to saturation, reducing the fuel input for the same net power output.

The efficiency gain can be understood through the heat exchanger effectiveness concepts you already know. The regenerator has an effectiveness ε that determines how close the feedwater exit temperature comes to the saturation temperature of the extracted steam. Higher effectiveness means more preheating, more heat recovered internally, and less fuel consumed. The tradeoff is that extracting steam from the turbine reduces the mass flow through the lower-pressure stages, so those stages produce less work. Net efficiency improves because the heat saved in the boiler outweighs the work lost from extraction — provided the extraction fraction is optimized.

Adding **multiple extraction points** at successively lower pressures approaches the theoretical Carnot-equivalent limit of supplying heat to the boiler entirely at the highest available temperature. In practice, industrial power plants use five to eight feedwater heaters. Beyond a certain number, the marginal efficiency gain from adding another heater no longer justifies the capital cost, added complexity, and reliability risk. Combined with reheating (which you studied in the Rankine reheat cycle), regeneration is the primary tool for pushing large steam power plants toward thermal efficiencies of 40–50%. The analysis of each stage uses the same energy balance tools you have: write a first-law energy balance around the feedwater heater, introduce the extraction mass fraction y as an unknown, and solve for y using enthalpy values from steam tables.
