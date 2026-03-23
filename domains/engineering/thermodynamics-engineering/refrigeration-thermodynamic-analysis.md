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
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A refrigeration system removes 5 kJ from a cold space and rejects 7 kJ to the warm surroundings per cycle. What is its coefficient of performance?"
  type: multiple-choice
  options:
    - "COP = 7/5 = 1.4"
    - "COP = 5/2 = 2.5"
    - "COP = 5/7 ≈ 0.71"
    - "COP = 7/2 = 3.5"
  answer: 1
  explanation: "COP for refrigeration = Q_cold / W_net. By the first law, W_net = Q_hot − Q_cold = 7 − 5 = 2 kJ. Therefore COP = 5/2 = 2.5. Option A (7/5 = 1.4) is the common error of using Q_hot in the numerator — this confuses the refrigeration COP with the heat pump COP (COP_HP = Q_hot/W_net). The refrigeration COP counts only the useful effect: heat removed from the cold space."

- question: "A refrigeration engineer raises the condenser temperature from 30°C to 45°C to reject heat more quickly. The evaporator remains at −10°C. What happens to the Carnot COP?"
  type: multiple-choice
  options:
    - "Carnot COP increases — higher rejection temperature improves thermodynamic efficiency"
    - "Carnot COP decreases — the temperature difference between hot and cold reservoirs increases, requiring more work per unit of heat pumped"
    - "Carnot COP is unchanged — the formula depends only on the cold reservoir temperature"
    - "Carnot COP increases marginally because the compressor achieves higher pressure ratios"
  answer: 1
  explanation: "Carnot COP = T_cold / (T_hot − T_cold). Raising T_hot from 303 K to 318 K: original COP = 263/(303−263) = 263/40 = 6.6; new COP = 263/(318−263) = 263/55 = 4.8. A wider temperature gap requires more work per unit of heat pumped uphill. Rejecting heat at a higher temperature is not more efficient thermodynamically — it may allow a smaller condenser, but always at a cost in COP."

- question: "Real vapor-compression refrigerators have lower COPs than the Carnot ideal primarily because real compressors consume more work than an ideal isentropic compressor would."
  type: true-false
  answer: false
  explanation: "Compressor irreversibility does reduce COP, but the dominant sources of inefficiency in most real systems are the finite temperature differences required in the evaporator and condenser. The refrigerant must be colder than the food (evaporator) and hotter than the room (condenser) for heat to flow. These required ΔTs widen the effective temperature gap the cycle spans beyond the nominal reservoir temperatures, directly reducing COP relative to the Carnot ideal. Throttling irreversibility is another major loss. Compressor inefficiency is real but typically not the single dominant factor."

- question: "The Carnot COP formula T_cold / (T_hot − T_cold) implies that a refrigeration cycle operating between temperatures close together is more efficient than one operating across a large temperature difference."
  type: true-false
  answer: true
  explanation: "As (T_hot − T_cold) → 0, COP_Carnot → ∞. Physically, a tiny temperature difference means the thermodynamic 'hill' that heat must be pumped up is nearly flat — very little work is required. Maintaining a very cold space (large temperature gap) requires much more work per unit of heat pumped. This is why industrial freezers at −80°C are far less efficient than household refrigerators at 4°C, and why using larger heat exchangers (which reduce required ΔTs) directly improves COP."

- question: "Why does the Carnot COP formula predict that refrigeration becomes more efficient as the temperature difference between reservoirs decreases? Explain the physical reasoning, not just the algebra."
  type: short-answer
  answer: "Heat naturally flows from hot to cold; forcing it to flow from cold to hot requires overcoming an entropy gradient. Removing Q_cold from the cold reservoir decreases its entropy by Q_cold/T_cold. To satisfy the second law, the warm reservoir's entropy must increase by at least as much: Q_hot/T_hot ≥ Q_cold/T_cold, giving Q_hot ≥ Q_cold × (T_hot/T_cold). The required work W = Q_hot − Q_cold ≥ Q_cold × (T_hot − T_cold)/T_cold. A larger temperature ratio means rejecting proportionally more heat to the warm side than you extract from the cold side — hence more work per unit of cooling. COP = Q_cold/W ≤ T_cold/(T_hot − T_cold)."
  explanation: "The physical insight is that refrigeration pays an entropy tax: to move entropy from cold to hot, external work must supply additional entropy to keep the total non-decreasing. A steeper temperature gradient demands a larger entropy tax. Minimizing the temperature difference minimizes the tax, which is why engineers obsess over heat exchanger approach temperatures — every degree of unnecessary ΔT in the condenser or evaporator costs real compressor work."
```

## Explainer

From the second law of thermodynamics you know that heat spontaneously flows from hot to cold — never the reverse. A refrigeration cycle forces heat to flow the "wrong" way: from the cold interior of a refrigerator to the warm kitchen. This is not a violation of the second law; it only happens because you supply work. The **coefficient of performance** quantifies how much cooling you get per unit of work supplied: **COP = Q_cold / W_net**, where Q_cold is the heat removed from the cold reservoir and W_net is the net compressor work input. By the first law, Q_hot = Q_cold + W_net, so the cycle simultaneously removes heat from the cold space and rejects more heat to the warm surroundings.

The ideal upper bound on COP comes from running the cycle as a reversed Carnot cycle — all processes reversible, heat exchange only at two fixed temperatures. The **Carnot COP** is COP_Carnot = T_cold / (T_hot − T_cold), where temperatures are in Kelvin. This formula reveals the key driver: the smaller the temperature difference between the cold and hot reservoirs, the higher the COP can be. A refrigerator keeping food at 4°C (277 K) while rejecting heat to a 30°C (303 K) kitchen has Carnot COP = 277 / 26 ≈ 10.7. Real refrigerators achieve COPs of 2–4 — a large gap that represents the efficiency lost to real-world irreversibilities.

Two irreversibilities dominate in real systems. First, heat exchangers can only transfer heat when there is a finite temperature difference driving the flow: the refrigerant in the evaporator must be colder than the food, and the refrigerant in the condenser must be hotter than the room. These required temperature differences widen the effective temperature gap the cycle must span, directly reducing COP relative to the Carnot ideal. Second, real compressors are not isentropic — friction, heat losses, and fluid turbulence add entropy and increase the work required. The **expansion device** (a throttling valve or capillary tube) is a third source of irreversibility: the pressure drop is inherently irreversible and generates entropy, replacing the idealized isentropic expansion of the Carnot cycle.

Plotting the cycle on a **P-h diagram** (pressure vs. specific enthalpy) or a **T-s diagram** makes the analysis quantitative. On the P-h diagram, the evaporator is a horizontal line at low pressure (constant pressure phase change), the condenser is a horizontal line at high pressure, the compressor is a roughly vertical line (isentropic) or slightly tilted right (real), and the expansion device is a vertical drop in enthalpy at constant enthalpy (throttling). The cooling capacity Q_cold is the enthalpy change across the evaporator, the compressor work is the enthalpy change across the compressor, and the COP follows directly. Identifying where the actual cycle deviates from the ideal Carnot cycle — specifically the additional temperature differences and entropy generation — reveals exactly where efficiency is lost and how to recover it through design improvements like larger heat exchangers or two-stage compression.
