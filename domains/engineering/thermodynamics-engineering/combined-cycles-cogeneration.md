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
stage: formal-systems
status: draft
---

# Combined Power Cycles and Cogeneration Analysis

## Core Idea
Combined cycles cascade a Brayton cycle (topping) with a Rankine cycle (bottoming) to utilize high-temperature gas turbine exhaust efficiently. Heat recovery steam generators (HRSG) replace the condenser, increasing overall efficiency to 50-60%. Cogeneration simultaneously produces electricity and useful heat (steam or hot water). Pinch point analysis optimizes HRSG design and operating pressure selection.

## Questions

```yaml
- question: "A standalone gas turbine plant achieves 38% thermal efficiency and exhausts 550°C flue gas to the atmosphere. An engineer proposes adding a steam Rankine bottoming cycle using this exhaust as its heat source. What thermodynamic principle most directly explains the efficiency improvement?"
  type: multiple-choice
  options:
    - "The additional turbine capacity allows more fuel to be burned at higher temperatures"
    - "The HRSG recovers exhaust heat that would otherwise be wasted, extending the effective operating temperature range of the combined system"
    - "The Rankine cycle is inherently more efficient than the Brayton cycle at all temperature ranges"
    - "Steam cooling in the HRSG reduces gas turbine inlet temperature, lowering heat rejection losses"
  answer: 1
  explanation: "The Brayton cycle rejects heat at elevated temperatures — the 550°C exhaust represents significant thermodynamic work potential being discarded. The combined cycle treats this as a resource rather than waste: the HRSG uses it as the Rankine cycle's heat source. Carnot efficiency is (T_H - T_L)/T_H. The combined cycle's effective T_H is set by the high combustion temperatures of the gas cycle, while T_L is set by the steam condenser near ambient — achieving the full temperature span that neither cycle exploits alone. The improvement is second-law bookkeeping, not additional fuel."

- question: "A hospital installs a cogeneration (CHP) system achieving 83% utilization factor, compared to 40% thermal efficiency for conventional grid power generation. The hospital previously bought grid electricity and burned gas separately for heating. What is the primary reason CHP achieves higher utilization?"
  type: multiple-choice
  options:
    - "CHP uses a more advanced thermodynamic cycle that converts fuel to electricity more efficiently"
    - "CHP captures heat that would otherwise be rejected in the condenser and uses it for building heating, eliminating the need to burn separate fuel"
    - "CHP systems always operate at higher turbine inlet temperatures than grid-scale plants"
    - "CHP eliminates electrical transmission and distribution losses from the grid"
  answer: 1
  explanation: "The utilization factor is total useful energy (electricity + process heat) divided by fuel input. Conventional power plants condense all steam back to liquid, rejecting the latent heat to the environment — this is the biggest thermodynamic loss in the Rankine cycle. CHP instead extracts some of that steam before or after the turbine and delivers it as useful process heat. The same fuel input that produced electricity also satisfies heating demand that would otherwise require a separate boiler. Utilization factors above 80% are achievable precisely because the 'waste' heat becomes a product."

- question: "A smaller pinch point temperature difference in an HRSG allows more heat to be recovered from exhaust gas but requires a larger and more expensive heat exchanger."
  type: true-false
  answer: true
  explanation: "The pinch point is the minimum temperature difference between the flue gas and the water-steam streams in the HRSG. Thermodynamics requires the flue gas to always be hotter than the fluid it is heating. A smaller pinch (5–10°C) means the heat exchanger extracts heat from the exhaust down to lower temperatures, recovering more energy — but the smaller driving temperature difference means slower heat transfer per unit area, requiring more heat exchanger surface and therefore higher capital cost. A larger pinch (20–30°C) is cheaper to build but leaves more recoverable heat in the stack exhaust."

- question: "Combined-cycle plants achieve higher thermal efficiency than standalone gas turbines primarily because they burn fuel more completely in the combined system."
  type: true-false
  answer: false
  explanation: "Combustion completeness is not the mechanism. Combined-cycle efficiency gains come entirely from thermodynamic heat recovery — the Brayton cycle's exhaust heat is captured and converted to additional work by the Rankine bottoming cycle, rather than being discharged to the atmosphere. The fuel input may actually be similar or even less than running both cycles separately; the point is that the same heat input yields more total work output. The efficiency improvement is a second-law recovery story, not a combustion chemistry story."

- question: "Explain why a combined-cycle plant achieves higher thermal efficiency than either a standalone Brayton or standalone Rankine cycle, using the concept of operating temperature range."
  type: short-answer
  answer: "Carnot efficiency scales with the temperature ratio (T_H - T_L)/T_H. A standalone Brayton cycle has a high T_H (combustion temperatures of 1000–1400°C) but rejects heat at elevated temperatures (400–600°C exhaust), narrowing the useful range. A standalone Rankine cycle is limited by its moderate heat source. The combined cycle uses the HRSG to transfer Brayton exhaust heat to the Rankine boiler: T_H is governed by the gas turbine's high combustion temperature while T_L is set by the steam condenser near ambient. This captures the full temperature span — from high combustion temperatures down to near-ambient rejection — that neither cycle achieves independently, yielding 55–62% efficiency versus 35–40% for either cycle alone."
  explanation: "The key insight is that the Brayton and Rankine cycles have complementary temperature ranges. Brayton excels at high temperatures but wastes high-temperature exhaust; Rankine excels at low-to-moderate temperatures but needs a heat source. Cascading them via the HRSG stitches their temperature ranges together into one thermodynamically superior system. The HRSG is not generating any additional heat — it is simply the conduit that prevents the Brayton cycle's exhaust from being wasted."
```

## Explainer

From your study of the Brayton and Rankine cycles separately, you know that each has characteristic second-law losses. The Brayton cycle operates at very high temperatures (combustion gases at 1000–1400°C at the turbine inlet) but rejects heat at relatively high temperatures too — exhaust leaving the gas turbine is still 400–600°C. A standalone gas turbine simply discards this hot exhaust to the atmosphere. The combined cycle solves this by treating the Brayton cycle's waste heat as the Rankine cycle's heat input. The **heat recovery steam generator (HRSG)** sits between the two cycles: it is a heat exchanger in which hot exhaust gas heats feedwater, generates steam, and superheats it before the steam turbine. The gas turbine provides power on the topping pass; the steam turbine recovers what would otherwise be stack losses.

The thermodynamic efficiency gain follows directly from the second law. Carnot efficiency is limited by (T_H − T_L)/T_H. The combined cycle effectively extends the active temperature range: T_H is set by the high combustion temperature of the gas cycle, while T_L is set by the steam condenser operating near ambient. Neither cycle alone achieves this full range. A modern **combined-cycle gas turbine (CCGT)** plant achieves 55–62% lower-heating-value efficiency, compared to roughly 35–40% for a Brayton cycle alone and 35–45% for a supercritical Rankine cycle alone. The improvement is not magic — it is second-law bookkeeping applied consistently across both cycles.

**Pinch point analysis** is the key design constraint for the HRSG. When you plot flue gas temperature against heat transferred (a T-Q diagram), the flue gas cools from left to right while the water/steam heats and boils at constant pressure. The **pinch point** is the location of minimum temperature difference between the two streams. Thermodynamics requires the flue gas to always be hotter than the water-steam mixture it is heating, so the pinch point temperature difference must remain positive. A smaller pinch (5–10°C) recovers more heat but requires a larger, more expensive heat exchanger; a larger pinch (20–30°C) is cheaper but wastes more exhaust energy. HRSG operating pressure is chosen to place the pinch point optimally — changing the steam pressure shifts the boiling temperature and thus the shape of the water-steam curve on the T-Q diagram.

**Cogeneration** extends the concept beyond pure power generation: rather than condensing all steam back to liquid (discarding its latent heat), some steam is extracted and used for process heating, district hot water, absorption chilling, or industrial applications. The key metric is **utilization factor** — total useful energy output (electricity plus process heat) divided by fuel input. Cogeneration systems routinely achieve utilization factors above 80%, compared to 35–45% for electricity-only plants. This is why hospitals, universities, and manufacturing facilities with simultaneous electricity and heat demands install combined heat and power (CHP) systems: the same fuel input delivers both outputs far more efficiently than purchasing grid electricity and burning fuel separately for heat.
