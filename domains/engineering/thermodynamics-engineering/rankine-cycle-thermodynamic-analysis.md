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
- id: heat-engine-efficiency-and-carnot
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

## Explainer

The Rankine cycle is the thermodynamic model underlying every coal, nuclear, and natural gas steam power plant on earth. You already know the Carnot cycle, which defines the theoretical efficiency limit η = 1 − T_L/T_H, and you know how to use steam tables to find enthalpy and entropy values for water at any pressure-temperature state. The Rankine cycle puts these together into a practical cycle that exploits the phase-change properties of water — specifically, the fact that condensing and boiling happen at constant temperature and pressure.

The cycle has four states and four processes. **State 1**: saturated liquid leaving the condenser at low pressure. **Process 1→2**: the **pump** compresses the liquid to high pressure. Because liquids are nearly incompressible, the specific volume ν is approximately constant, and pump work w_pump = ν(P_2 − P_1) is small. **State 2**: subcooled liquid at high pressure. **Process 2→3**: the **boiler** adds heat at constant pressure, heating the water through the subcooled liquid region, across the saturation dome (boiling), and potentially into the superheated vapor region. **State 3**: high-pressure steam (saturated or superheated). **Process 3→4**: the **turbine** expands the steam isentropically (in ideal analysis) to low pressure, doing work. **State 4**: low-quality wet steam at condenser pressure. **Process 4→1**: the **condenser** rejects heat at constant pressure as the steam condenses back to liquid.

Thermal efficiency is η = (w_turbine − w_pump) / q_boiler = (h_3 − h_4 − (h_2 − h_1)) / (h_3 − h_2). The dominant term is the turbine work h_3 − h_4; pump work is small by comparison because pumping liquid requires much less work than compressing vapor. The T-s diagram shows immediately where the cycle loses efficiency relative to Carnot: heat is added over a range of temperatures (from subcooled liquid through the dome to superheated steam), not at a single maximum temperature. The mean temperature of heat addition is less than T_H, which is why Rankine efficiency is always below Carnot efficiency between the same temperature limits.

The levers for improving efficiency follow directly from this picture. **Increasing boiler pressure** raises the saturation temperature and shifts more heat addition to higher temperatures, improving η — but it also increases moisture at the turbine exit (state 4 moves deeper into the two-phase region), which erodes turbine blades. **Superheating** (heating beyond saturation at constant pressure) raises both the mean addition temperature and the turbine exit quality, improving efficiency and reducing moisture simultaneously. **Lowering condenser pressure** (thus lowering T_L) increases the temperature difference and efficiency. These three modifications — higher pressure, superheating, lower condenser pressure — are standard in real power plants and each has a clear thermodynamic explanation once you can read the T-s diagram.
