---
id: rankine-cycle-thermodynamic-analysis
title: Rankine Cycle and Steam Power Plants
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-closed-systems
  type: hard
- id: saturated-superheated-property-regions
  type: hard
- id: carnot-cycle
  type: soft
builds-toward:
- rankine-cycle-reheat-regeneration
tags:
- rankine-cycle
- steam-power
- power-cycles
stage: advanced
status: draft
---

# Rankine Cycle and Steam Power Plants

## Core Idea
The Rankine cycle (pumping, isobaric heating, isentropic expansion, isobaric condensation) models the steam power plant and defines thermal efficiency in terms of heat input and rejection. Typical Rankine cycles operate between fixed saturation pressures with throttling and actual pressure drops reducing efficiency below the Carnot limit. State-by-state analysis using property tables reveals where irreversibilities occur and what pressure ratios maximize output.

## How It's Best Learned
Sketch the Rankine cycle on T-s and h-P diagrams, labeling each state and process. Calculate all four state properties at each state point using steam tables. Compute pump work (approximately ν * ΔP for liquid), turbine work (using isentropic or actual efficiency), heat transfers, and thermal efficiency. Compare to Carnot cycle efficiency to quantify the gap.

## Common Misconceptions
- The Rankine cycle achieves higher efficiency than Carnot because it uses two-phase expansion; Carnot is the absolute upper limit and Rankine achieves less.
- Increasing boiler pressure always increases thermal efficiency; higher pressure increases work but also reduces heat rejected, with complex tradeoffs.
- The pump work is negligible because liquids are incompressible; pumping liquid still requires work proportional to ν ΔP, which increases with boiler pressure.
