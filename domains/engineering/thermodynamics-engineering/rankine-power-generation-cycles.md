---
id: rankine-power-generation-cycles
title: Rankine Cycle and Power Plant Applications
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: rankine-cycle-thermodynamic-analysis
  type: hard
- id: power-cycle-thermal-efficiency
  type: soft
builds-toward:
- rankine-cycle-reheat-regeneration
- combined-gas-steam-cycles
- steam-tables-property-diagrams
tags:
- rankine
- steam-cycle
- power-plants
- efficiency
stage: advanced
status: draft
---

# Rankine Cycle and Power Plant Applications

## Core Idea
The Rankine cycle (pump, boiler, turbine, condenser) is the standard for steam power generation worldwide. Efficiency improves with higher boiler pressure and temperature, lower condenser pressure, and addition of reheat and regenerative feedwater heating. Modern power plants achieve 35-45% electrical efficiency; extending to cogeneration (heat + power) reaches 80%+ total efficiency.

## Explainer

From your prior Rankine cycle analysis you already know the ideal four-process cycle on the T-s diagram: isentropic pumping (1→2), constant-pressure boiling and superheating (2→3), isentropic expansion through the turbine (3→4), and constant-pressure condensation (4→1). You know that the thermal efficiency is η = 1 − Q_out/Q_in and that it improves as you increase the temperature at which heat is added or decrease the temperature at which it is rejected. Real power plants operate on this same cycle but with three important refinements that you now need to understand quantitatively and physically.

The first lever is **increasing boiler pressure and temperature**. Raising boiler pressure increases the average temperature of heat addition in the boiler, improving efficiency — but it also makes the turbine exit steam wetter (lower quality x at state 4), which erodes turbine blades. Superheating the steam beyond saturation at the same pressure shifts the turbine exit state to higher quality and higher enthalpy, improving both efficiency and turbine blade life. Modern supercritical plants operate above the critical pressure (22.1 MPa for water), eliminating the two-phase dome entirely in the boiler and achieving average heat-addition temperatures close to peak cycle temperatures. **Lowering condenser pressure** (and therefore temperature) reduces Q_out at the expense of requiring a condenser cooled by a heat sink well below ambient — cooling towers or river water. Even small reductions in condenser pressure yield meaningful efficiency gains because the condensation temperature appears in the denominator of the Carnot-analog expression.

**Reheat** addresses the blade-erosion problem directly. Steam is expanded partway through the turbine (to an intermediate pressure), extracted, reheated in the boiler back to near the inlet temperature, then expanded through the remainder of the turbine. The T-s diagram shows this as two turbine expansion steps separated by a reheat segment. Reheat raises the average temperature of heat addition slightly (improving efficiency) and — crucially — moves the final turbine exit point to a much higher quality (drier steam), protecting low-pressure blades. Most large coal and nuclear plants use one or two stages of reheat.

**Regeneration** uses steam extracted from intermediate turbine stages to preheat the feedwater before it enters the boiler. Instead of the cold condensate absorbing heat from high-temperature combustion gases (a large irreversibility), it is first heated by steam that would otherwise be condensed and its energy discarded. This increases the average temperature of heat addition, improving efficiency, even though the turbine produces less work (some steam is extracted before full expansion). The T-s diagram for a regenerative Rankine cycle shows multiple **feedwater heaters**: open (direct-contact mixing) or closed (shell-and-tube heat exchangers). The analysis proceeds by applying energy balances to each feedwater heater to find the extraction fractions.

**Cogeneration** (combined heat and power, CHP) abandons the goal of maximizing electricity output and instead exploits the unavoidable heat rejection. In a pure power plant, condenser heat at 30-50°C goes to a river or cooling tower and is worthless. In a cogeneration plant, the condenser (or a back-pressure turbine exhaust) operates at 100-150°C and the heat is piped to buildings for heating, industrial processes, or district heating networks. The first law says you are converting 80-90% of fuel energy to electricity plus useful heat, compared to 35-45% for electricity alone. The second law says you are exploiting the temperature cascade more completely: high-temperature combustion gases deliver work via the turbine, and medium-temperature exhaust still carries enough exergy to satisfy low-grade heat demands. The practical constraint is that electricity and heat demands must be matched geographically and temporally — large cogeneration plants work best in dense urban or industrial settings with steady year-round heat loads.
