---
id: refrigeration-thermodynamic-analysis
title: Refrigeration Cycles and Coefficient of Performance
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: second-law-thermodynamics-entropy
  type: hard
- id: first-law-energy-conservation
  type: hard
builds-toward:
- vapor-compression-refrigeration-cycle
- heat-pump-heating-cooling-analysis
tags:
- refrigeration
- COP
- thermodynamic-cycles
stage: advanced
status: draft
---

# Refrigeration Cycles and Coefficient of Performance

## Core Idea
Refrigeration cycles reverse the Rankine cycle direction, using mechanical work input to move heat from a cool space to a warm reservoir. The coefficient of performance COP = Q_in / W_net quantifies efficiency and has an ideal Carnot limit of COP_Carnot = T_cold / (T_hot - T_cold). Real refrigeration systems operate well below Carnot COP due to throttling losses and heat exchanger irreversibilities.

## How It's Best Learned
Sketch refrigeration cycles on P-h and T-s diagrams, locating the evaporator, compressor, condenser, and expansion device. Calculate COP by finding evaporator heat removal rate and compressor work input. Compare actual COP to Carnot limit to identify the efficiency gap and motivate cycle improvements. Understand that temperature differences in heat exchangers (condenser approach, evaporator superheat) are practical necessities that reduce COP.

## Common Misconceptions
- Refrigeration cycles operate at fixed temperatures; they typically involve finite temperature differences in evaporators and condensers.
- Higher COP always indicates better performance; COP alone does not account for heat exchanger size, compressor reliability, or refrigerant environmental impact.
- The cooling effect Q_in comes from an ideal, perfect evaporator; real evaporators operate at finite superheat to ensure liquid refrigerant doesn't reach the compressor.
