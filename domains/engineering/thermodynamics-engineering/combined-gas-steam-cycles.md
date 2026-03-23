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
stage: formal-systems
status: validated
---

# Combined Cycle Systems and Cogeneration

## Core Idea
Combined cycles couple a Brayton (gas) cycle with a Rankine (steam) cycle, using gas turbine exhaust waste heat to drive a steam generator. Overall electrical efficiency reaches 60-65% compared to ~40% for standalone gas turbines. Cogeneration adds useful heat output for process steam or district heating, achieving >80% total energy utilization.

## Questions

```yaml
- question: "A standalone gas turbine plant achieves 40% thermal efficiency. A standalone steam plant achieves 35%. An engineer proposes combining them into a combined cycle where gas turbine exhaust drives a steam generator. Which efficiency outcome best describes the combined plant?"
  type: multiple-choice
  options:
    - "Approximately 75% — the combined cycle adds both efficiencies since two independent cycles are running"
    - "Approximately 40% — efficiency is limited by the Brayton topping cycle, and the bottoming cycle cannot exceed it"
    - "Approximately 60–65% — the steam turbine generates additional electricity from exhaust heat that would otherwise be wasted, without burning more fuel"
    - "Approximately 35% — the combined system is limited by the Rankine bottoming cycle since that is the final energy converter"
  answer: 2
  explanation: "Combined cycle efficiency is not the sum of the two individual efficiencies — that would violate the first law. The key insight is that the steam turbine is powered by exhaust heat that would otherwise be vented to atmosphere. The fuel energy produces Brayton cycle work (~40% of input) plus exhaust heat (~50% of input at 500–600°C). Capturing that exhaust heat to run a steam cycle produces additional work without burning any more fuel. The combined efficiency ends up around 60–65%, not because both cycles magically add up, but because less energy is wasted as hot exhaust."

- question: "In a combined cycle plant, reducing the HRSG 'pinch point' temperature difference from 20°C to 5°C would have what effect?"
  type: multiple-choice
  options:
    - "No effect on plant efficiency, since the pinch point only affects condenser sizing at the cold end"
    - "Decrease efficiency because a smaller temperature difference reduces the thermodynamic driving force for heat transfer, slowing steam generation"
    - "Increase steam generation from the exhaust heat and improve bottoming cycle output, but require a larger and more expensive heat exchanger"
    - "Allow the gas turbine to operate at higher turbine inlet temperatures, increasing topping cycle efficiency"
  answer: 2
  explanation: "The pinch point is the minimum temperature difference between the flue gas and the steam at any cross-section of the HRSG. A tighter pinch means the gas can be cooled closer to the steam temperature — extracting more heat and generating more steam. This directly increases bottoming cycle power output. But the rate of heat transfer is Q = U·A·ΔT_lm, so for the same heat duty, a smaller ΔT requires a larger heat exchanger area (and cost). This is a classic tradeoff: tighter pinch = higher efficiency + higher capital cost. Typical designs use 10–15°C pinch as a balance point."

- question: "In a combined cycle plant, the gas turbine exhaust is used to generate steam rather than being vented to atmosphere, and roughly 30–40% of the plant's total electricity comes from what would otherwise be wasted heat."
  type: true-false
  answer: true
  explanation: "A gas turbine producing 40% efficiency has about 60% of the fuel energy leaving as hot exhaust. The steam cycle captures enough of this exhaust heat to generate an additional 20–25 percentage points of electrical efficiency — bringing the total to 60–65%. Relative to the gas turbine alone, roughly one-third of total output comes from steam. This is why combined cycle plants dominate new gas-fired power generation: the 'free' steam electricity dramatically improves fuel economics with only modest additional capital cost (the HRSG and steam turbine)."

- question: "Cogeneration achieves higher electrical efficiency than a standard combined cycle plant because it extracts more turbine work from the steam before condensing it."
  type: true-false
  answer: false
  explanation: "Cogeneration sacrifices electrical efficiency in exchange for total energy utilization. Instead of expanding steam fully through the turbine (maximizing electricity), cogeneration extracts steam at an intermediate pressure and supplies it as process heat or district heating — consuming the steam's latent heat usefully rather than rejecting it in the condenser. This reduces electricity output but raises total energy utilization from ~60% to over 80%, because the latent heat that a pure power plant discards in the condenser now does useful thermal work. Cogeneration optimizes total energy value, not electricity output."

- question: "Why can a combined cycle plant achieve 60–65% thermal efficiency when neither the gas turbine alone nor the steam cycle alone can exceed about 42%, and what role does the HRSG play in this?"
  type: short-answer
  answer: "A gas turbine exhausts large amounts of heat at 500–600°C — far too hot to simply discard but too cool for further gas turbine work. The HRSG is a heat exchanger that captures this exhaust heat and uses it to generate and superheat steam, which then drives a steam turbine to produce additional electricity. No extra fuel is burned for the steam cycle — it runs entirely on heat that would otherwise be wasted. The combined plant extracts work from a wider temperature range than either cycle alone can span, approaching the limit set by the highest gas turbine temperature and the cold condenser. The HRSG pinch point constrains how efficiently the handoff happens."
  explanation: "The thermodynamic principle is simple: efficiency rises when you operate over a wider temperature range. The Brayton cycle tops out at combustion temperature (~1400°C) but rejects heat at 500–600°C instead of at ambient. The Rankine cycle accepts heat at 500–600°C and rejects at ~40°C (condenser). Together they span from ~1400°C to ~40°C — a far wider range than either alone. The Carnot efficiency for this range is approximately 1 − (313 K / 1673 K) ≈ 81%, so the 60–65% achievable in real systems represents capturing much of the theoretical maximum beyond what single-cycle designs can reach."
```

## Explainer

Recall the fundamental limitation of any single thermodynamic cycle: efficiency is bounded by the Carnot limit, which rises as you increase the gap between the highest and lowest temperatures in the cycle. The Brayton gas turbine cycle operates at very high temperatures (combustion inlet ≈ 1200-1500°C) but rejects exhaust heat at still-high temperatures (500-600°C). The Rankine steam cycle operates efficiently at lower temperatures. The insight of the **combined cycle** is to stack these two cycles: use the Brayton cycle where temperatures are high, then capture the hot exhaust and use it as the heat source for a Rankine cycle where temperatures are lower. The combined system uses a wider temperature range than either cycle alone.

The physical connection is the **heat recovery steam generator (HRSG)** — a heat exchanger that sits in the exhaust stream of the gas turbine. Rather than venting 550°C exhaust to atmosphere (discarding ~30% of the fuel's energy as waste heat), the HRSG uses it to boil and superheat steam. That steam then drives a conventional steam turbine. The gas turbine produces perhaps 60% of the plant's total electricity; the steam turbine adds another 30-40%, all from heat that would otherwise be wasted. This is why combined-cycle plants routinely achieve 60-65% thermal efficiency, compared to 38-42% for a standalone gas turbine or coal plant.

**Energy analysis** of a combined cycle applies the first law to each component in sequence. For the Brayton topping cycle, compute net work (turbine output minus compressor input) and heat added in the combustion chamber. For the HRSG, an energy balance sets the steam-side heat gain equal to the exhaust-side heat loss (accounting for the pinch point — the minimum temperature difference between gas and steam at any cross-section, which constrains steam production). For the Rankine bottoming cycle, compute steam turbine work and condenser heat rejection. Overall efficiency is total net work divided by fuel heat input.

**Cogeneration** is a variant where the goal is not maximum electricity but maximum useful energy. Instead of condensing all steam to recover work, you extract steam at an intermediate pressure and supply it as process heat to an industrial facility or district heating network. This sacrifices some electricity generation but raises total energy utilization from ~60% to over 80%, because the latent heat of the steam — which a pure power plant throws away in the condenser — now does useful work. The tradeoff is that the economic value of heat is lower per unit than electricity, so the financial optimization depends heavily on local energy prices and heat demand.

When analyzing combined cycle problems, always track energy at system boundaries and account for the HRSG pinch point as a design constraint. The pinch temperature difference (typically 10-15°C minimum) limits how much steam you can generate from a given exhaust stream. A tighter pinch means more steam (higher efficiency) but requires a larger, more expensive heat exchanger — a classic engineering tradeoff between capital cost and operating performance.
