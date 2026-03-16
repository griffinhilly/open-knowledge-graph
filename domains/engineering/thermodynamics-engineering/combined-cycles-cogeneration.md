---
id: combined-cycles-cogeneration
title: Combined Power Cycles and Cogeneration Analysis
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: rankine-cycle-thermodynamic-analysis
  type: hard
- id: brayton-cycle-gas-turbine
  type: hard
builds-toward:
- second-law-efficiency-exergy-based
tags:
- combined-cycle
- cogeneration
- topping-cycle
- bottoming-cycle
- hrsg
stage: advanced
status: draft
---

# Combined Power Cycles and Cogeneration Analysis

## Core Idea
Combined cycles cascade a Brayton cycle (topping) with a Rankine cycle (bottoming) to utilize high-temperature gas turbine exhaust efficiently. Heat recovery steam generators (HRSG) replace the condenser, increasing overall efficiency to 50-60%. Cogeneration simultaneously produces electricity and useful heat (steam or hot water). Pinch point analysis optimizes HRSG design and operating pressure selection.

## Explainer

From your study of the Brayton and Rankine cycles separately, you know that each has characteristic second-law losses. The Brayton cycle operates at very high temperatures (combustion gases at 1000–1400°C at the turbine inlet) but rejects heat at relatively high temperatures too — exhaust leaving the gas turbine is still 400–600°C. A standalone gas turbine simply discards this hot exhaust to the atmosphere. The combined cycle solves this by treating the Brayton cycle's waste heat as the Rankine cycle's heat input. The **heat recovery steam generator (HRSG)** sits between the two cycles: it is a heat exchanger in which hot exhaust gas heats feedwater, generates steam, and superheats it before the steam turbine. The gas turbine provides power on the topping pass; the steam turbine recovers what would otherwise be stack losses.

The thermodynamic efficiency gain follows directly from the second law. Carnot efficiency is limited by (T_H − T_L)/T_H. The combined cycle effectively extends the active temperature range: T_H is set by the high combustion temperature of the gas cycle, while T_L is set by the steam condenser operating near ambient. Neither cycle alone achieves this full range. A modern **combined-cycle gas turbine (CCGT)** plant achieves 55–62% lower-heating-value efficiency, compared to roughly 35–40% for a Brayton cycle alone and 35–45% for a supercritical Rankine cycle alone. The improvement is not magic — it is second-law bookkeeping applied consistently across both cycles.

**Pinch point analysis** is the key design constraint for the HRSG. When you plot flue gas temperature against heat transferred (a T-Q diagram), the flue gas cools from left to right while the water/steam heats and boils at constant pressure. The **pinch point** is the location of minimum temperature difference between the two streams. Thermodynamics requires the flue gas to always be hotter than the water-steam mixture it is heating, so the pinch point temperature difference must remain positive. A smaller pinch (5–10°C) recovers more heat but requires a larger, more expensive heat exchanger; a larger pinch (20–30°C) is cheaper but wastes more exhaust energy. HRSG operating pressure is chosen to place the pinch point optimally — changing the steam pressure shifts the boiling temperature and thus the shape of the water-steam curve on the T-Q diagram.

**Cogeneration** extends the concept beyond pure power generation: rather than condensing all steam back to liquid (discarding its latent heat), some steam is extracted and used for process heating, district hot water, absorption chilling, or industrial applications. The key metric is **utilization factor** — total useful energy output (electricity plus process heat) divided by fuel input. Cogeneration systems routinely achieve utilization factors above 80%, compared to 35–45% for electricity-only plants. This is why hospitals, universities, and manufacturing facilities with simultaneous electricity and heat demands install combined heat and power (CHP) systems: the same fuel input delivers both outputs far more efficiently than purchasing grid electricity and burning fuel separately for heat.
