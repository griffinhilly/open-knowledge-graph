---
id: turbine-staging-multistage
title: Multistage Turbine Design and Reheat
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: polytropic-efficiency-real-machinery
  type: hard
- id: rankine-cycle-thermodynamic-analysis
  type: soft
builds-toward:
- rankine-cycle-reheat-regeneration
- brayton-cycle-intercooling-reheating
tags:
- turbine
- multistage
- reheat
- expansion-ratio
- power-output
stage: advanced
status: draft
---

# Multistage Turbine Design and Reheat

## Core Idea
Multistage turbines with intermediate reheat maximize power output by preventing excessive moisture formation in the final stages. Reheat between stages restores enthalpy and increases turbine work. Optimal staging distributes entropy generation such that final conditions remain in the two-phase region while meeting metallurgical temperature limits.

## Explainer

From the Rankine cycle and your study of polytropic efficiency, you know that real turbines suffer from irreversibility: entropy increases as steam expands, and the actual work output is less than the isentropic ideal. For a large pressure ratio — say, expanding from 10 MPa to 10 kPa — a single turbine stage faces a severe problem: by the time the steam reaches low pressure, the expansion trajectory crosses deep into the two-phase (liquid-vapor) region. Liquid droplets in high-speed steam erode turbine blades catastrophically. Multistage design with reheat solves this by intercepting the expansion before it gets wet.

In a **multistage turbine with reheat**, steam expands through a high-pressure (HP) turbine stage, doing work. When the steam temperature has dropped to near saturation, it exits and returns to a **reheater** — a heat exchanger that restores the steam to a high temperature (often back to the original turbine inlet temperature). The reheated steam then enters an intermediate-pressure (IP) or low-pressure (LP) turbine and expands again. This cycle can repeat. Each reheat stage adds heat at an intermediate pressure, which on the h-s (Mollier) diagram shifts the expansion path rightward (toward higher entropy) and upward (higher enthalpy), keeping the steam well within the superheated region for most of the expansion.

The benefit is twofold. First, **moisture is avoided**: the final turbine exhaust quality stays above roughly 88–90% (typically required to prevent blade erosion), even for large overall pressure ratios. Second, **total turbine work increases**: reheating adds enthalpy back into the cycle at intermediate pressure, and that additional enthalpy is converted to additional work output in the subsequent stages. The net plant efficiency often improves as well, because the reheat raises the mean temperature at which heat is added to the cycle — closer to the Carnot ideal of adding all heat at the highest possible temperature.

The engineering tradeoffs in staging design are: how many stages to use, at what pressure to reheat, and to what temperature. More stages yield diminishing returns in efficiency while adding capital cost and complexity. The optimal reheat pressure for a two-reheat cycle is roughly the geometric mean of inlet and exhaust pressures for equal work split. Metallurgical limits cap reheat temperatures — today's advanced superalloys allow inlet temperatures around 650°C, with future targets pushing higher. Understanding staging from a thermodynamic perspective directly informs the more complex Rankine cycle configurations (regeneration + reheat) and the analogous intercooled-reheat Brayton cycles used in gas turbines.
