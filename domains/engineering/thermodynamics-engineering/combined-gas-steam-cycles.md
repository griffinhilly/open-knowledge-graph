---
id: combined-gas-steam-cycles
title: Combined Cycle Systems and Cogeneration
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: combined-cycles-cogeneration
  type: hard
- id: rankine-power-generation-cycles
  type: soft
- id: brayton-gas-turbine-cycles
  type: soft
builds-toward:
- regenerative-cycle-analysis-thermodynamics
tags:
- combined-cycle
- cogeneration
- efficiency
- power-plants
stage: advanced
status: draft
---

# Combined Cycle Systems and Cogeneration

## Core Idea
Combined cycles couple a Brayton (gas) cycle with a Rankine (steam) cycle, using gas turbine exhaust waste heat to drive a steam generator. Overall electrical efficiency reaches 60-65% compared to ~40% for standalone gas turbines. Cogeneration adds useful heat output for process steam or district heating, achieving >80% total energy utilization.

## Explainer

Recall the fundamental limitation of any single thermodynamic cycle: efficiency is bounded by the Carnot limit, which rises as you increase the gap between the highest and lowest temperatures in the cycle. The Brayton gas turbine cycle operates at very high temperatures (combustion inlet ≈ 1200-1500°C) but rejects exhaust heat at still-high temperatures (500-600°C). The Rankine steam cycle operates efficiently at lower temperatures. The insight of the **combined cycle** is to stack these two cycles: use the Brayton cycle where temperatures are high, then capture the hot exhaust and use it as the heat source for a Rankine cycle where temperatures are lower. The combined system uses a wider temperature range than either cycle alone.

The physical connection is the **heat recovery steam generator (HRSG)** — a heat exchanger that sits in the exhaust stream of the gas turbine. Rather than venting 550°C exhaust to atmosphere (discarding ~30% of the fuel's energy as waste heat), the HRSG uses it to boil and superheat steam. That steam then drives a conventional steam turbine. The gas turbine produces perhaps 60% of the plant's total electricity; the steam turbine adds another 30-40%, all from heat that would otherwise be wasted. This is why combined-cycle plants routinely achieve 60-65% thermal efficiency, compared to 38-42% for a standalone gas turbine or coal plant.

**Energy analysis** of a combined cycle applies the first law to each component in sequence. For the Brayton topping cycle, compute net work (turbine output minus compressor input) and heat added in the combustion chamber. For the HRSG, an energy balance sets the steam-side heat gain equal to the exhaust-side heat loss (accounting for the pinch point — the minimum temperature difference between gas and steam at any cross-section, which constrains steam production). For the Rankine bottoming cycle, compute steam turbine work and condenser heat rejection. Overall efficiency is total net work divided by fuel heat input.

**Cogeneration** is a variant where the goal is not maximum electricity but maximum useful energy. Instead of condensing all steam to recover work, you extract steam at an intermediate pressure and supply it as process heat to an industrial facility or district heating network. This sacrifices some electricity generation but raises total energy utilization from ~60% to over 80%, because the latent heat of the steam — which a pure power plant throws away in the condenser — now does useful work. The tradeoff is that the economic value of heat is lower per unit than electricity, so the financial optimization depends heavily on local energy prices and heat demand.

When analyzing combined cycle problems, always track energy at system boundaries and account for the HRSG pinch point as a design constraint. The pinch temperature difference (typically 10-15°C minimum) limits how much steam you can generate from a given exhaust stream. A tighter pinch means more steam (higher efficiency) but requires a larger, more expensive heat exchanger — a classic engineering tradeoff between capital cost and operating performance.
