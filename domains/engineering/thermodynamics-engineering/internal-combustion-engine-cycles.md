---
id: internal-combustion-engine-cycles
title: 'Otto and Diesel Cycles: Internal Combustion Engines'
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: otto-cycle-spark-ignition-engine
  type: hard
- id: diesel-cycle-compression-ignition
  type: hard
builds-toward:
- combustion-stoichiometry-energy-release
- adiabatic-flame-temperature-calculation
tags:
- otto-cycle
- diesel-cycle
- internal-combustion
- efficiency
stage: advanced
status: draft
---

# Otto and Diesel Cycles: Internal Combustion Engines

## Core Idea
The Otto cycle (spark-ignition, constant-volume heat addition) achieves efficiency η = 1 - 1/r_c^(γ-1), where r_c is compression ratio. The Diesel cycle (compression-ignition, constant-pressure heat addition) uses higher compression and air-fuel stratification. Diesel engines typically achieve 40-50% brake thermal efficiency; spark-ignition engines 25-35%, with modern direct injection improving both.

## Questions

```yaml
- question: "A student claims: 'Diesel engines are thermodynamically superior to gasoline engines because the Diesel cycle formula always gives higher efficiency.' A second student disagrees. Who is correct, and why?"
  type: multiple-choice
  options:
    - "The first student is correct — the Diesel cycle's constant-pressure heat addition is always more efficient than the Otto cycle's constant-volume addition"
    - "The second student is correct — at the same compression ratio, the Otto cycle is more efficient; diesels win in practice because they access much higher compression ratios that gasoline engines cannot use without knock"
    - "Neither student is correct — efficiency depends entirely on fuel type, not cycle type"
    - "The second student is correct — the Diesel cycle is fundamentally inefficient, and any advantage over gasoline engines comes only from diesel fuel's higher energy density"
  answer: 1
  explanation: "At the same compression ratio r, the Otto cycle (constant-volume heat addition) is thermodynamically more efficient than the Diesel cycle (constant-pressure heat addition) — the cutoff ratio term in the Diesel efficiency formula is always greater than 1, penalizing it relative to Otto at equal r. However, gasoline engines are knock-limited to r ≈ 9–12 because the air-fuel mixture autoignites at high compression. Diesel engines compress only air, so they can safely reach r = 16–22. Since efficiency rises steeply with compression ratio, the diesel's access to higher r more than compensates for the cycle's lower efficiency at equal r. Real diesel engines outperform real gasoline engines — but for reasons of *achievable compression ratio*, not cycle formulas."

- question: "Why can diesel engines use compression ratios of 16–22:1 while gasoline engines are limited to roughly 9–12:1?"
  type: multiple-choice
  options:
    - "Diesel engines are built with heavier materials that can withstand higher pressures"
    - "Diesel fuel has a higher energy density, so less compression is needed to ignite it"
    - "Diesel engines compress only air during the compression stroke, so there is no flammable mixture present to autoignite prematurely"
    - "Gasoline engines use spark plugs, which limit the compression ratio to values where plug heat doesn't pre-ignite the charge"
  answer: 2
  explanation: "The knock limit arises because the air-fuel mixture in a gasoline engine has an autoignition temperature. At high enough compression ratios, the mixture temperature at top dead center exceeds this threshold before the spark fires — producing knock, a damaging pressure spike. Diesel engines solve this by not introducing fuel until after compression is complete. They compress only air, which has a much higher autoignition temperature than any fuel-air mixture. When diesel fuel is injected into the hot compressed air, the controlled autoignition that occurs is the entire ignition mechanism — what is a hazard in gasoline engines is the design intent in diesel. This architectural difference unlocks the higher compression ratios responsible for diesel's efficiency advantage."

- question: "At the same compression ratio, the Diesel cycle achieves higher thermal efficiency than the Otto cycle."
  type: true-false
  answer: false
  explanation: "False — this is the central misconception about diesel efficiency. At equal compression ratios, the Otto cycle is more efficient because constant-volume heat addition (occurring in a fixed volume at TDC) is thermodynamically preferable to constant-pressure heat addition (occurring as the piston moves down). The Diesel efficiency formula includes a cutoff ratio term [r_c^γ − 1] / [γ(r_c − 1)] that is always greater than 1, representing a penalty compared to Otto. Diesel engines achieve higher *real-world* efficiency because they can use higher compression ratios than gasoline engines — but the thermodynamic formula comparison at equal r favors Otto."

- question: "Diesel engines can achieve higher compression ratios than gasoline engines without knock because they compress only air (no fuel) during the compression stroke."
  type: true-false
  answer: true
  explanation: "True. Knock in gasoline engines occurs when the compressed air-fuel mixture reaches its autoignition temperature before the spark fires, causing uncontrolled combustion. In a diesel engine, only air is present during compression — air alone has a much higher autoignition temperature than any fuel-air mixture. Diesel fuel is injected at top dead center directly into the hot, high-pressure air, and the resulting autoignition is precisely the intended mechanism (it is a compression-ignition engine). This structural difference allows diesel engines to operate at r = 16–22:1 versus r = 9–12:1 for gasoline, which is the primary reason real diesel engines achieve higher thermal efficiency despite the Diesel cycle being thermodynamically less efficient than Otto at equal r."

- question: "Explain why diesel engines achieve higher real-world thermal efficiency than gasoline engines, despite the Diesel cycle formula predicting lower efficiency than the Otto cycle at the same compression ratio."
  type: short-answer
  answer: "The Diesel cycle formula is indeed less efficient than the Otto formula at the same compression ratio r — the constant-pressure heat addition carries an efficiency penalty compared to constant-volume. However, gasoline engines cannot use compression ratios above about 10–12:1 because the air-fuel mixture will autoignite before the spark fires (knock), causing damaging pressure spikes. Diesel engines compress only air during the compression stroke, so there is no premixture to autoignite; they safely reach r = 16–22:1. Since thermal efficiency rises steeply with r (for the Otto formula, η = 1 − 1/r^(γ−1)), the diesel's access to much higher compression ratios outweighs the efficiency penalty of constant-pressure heat addition. The diesel's real efficiency advantage is a consequence of its architecture enabling higher compression — not because the Diesel cycle formula is thermodynamically superior."
  explanation: "This reconciliation — 'worse formula, better real performance' — is a common source of confusion. It illustrates that ideal cycle analysis must be combined with engineering constraints to understand real performance. The efficiency ceiling imposed by knock on gasoline engines is a practical constraint that the ideal cycle comparison ignores. Modern turbocharged direct-injection gasoline engines have narrowed the gap (up to ~40–42% peak vs. ~44–48% for diesel) through improved combustion management and downsizing, but the fundamental compression ratio advantage of diesel remains."
```

## Explainer

Having studied the Otto and Diesel cycles individually, the key task here is deepening the comparison and connecting ideal cycle analysis to real engine performance. The essential distinction is **how heat is added**: in the Otto cycle, a nearly homogeneous air-fuel mixture ignites simultaneously at top dead center, adding heat at approximately constant volume in a single rapid event. In the Diesel cycle, fuel injects progressively after compression and burns at approximately constant pressure while the piston descends. This difference in heat addition mode drives all the performance differences between the two engine families.

The **Otto cycle efficiency** η = 1 − 1/r^(γ−1) depends only on the compression ratio r and the specific heat ratio γ ≈ 1.4 for air. Efficiency rises monotonically with r — so why don't gasoline engines use r = 20:1? Because at high compression ratios, the air-fuel mixture reaches its autoignition temperature during compression, before the spark fires. This uncontrolled ignition — **knock** — causes pressure spikes that damage pistons and bearings. Gasoline engines are therefore limited to compression ratios of roughly 9:1 to 12:1, directly limiting their efficiency. High-octane fuel resists autoignition, allowing slightly higher compression ratios, which is why premium fuel exists.

Diesel engines escape this constraint because they compress **pure air** during the compression stroke — there is no fuel present to autoignite. Fuel injects at top dead center into the hot, high-pressure air, and autoignition of the mixture is the goal, not the hazard. This allows compression ratios of 16:1 to 22:1. The Diesel cycle efficiency formula, η = 1 − (1/r^(γ−1)) · [(r_c^γ − 1)/(γ(r_c − 1))], includes a **cutoff ratio** r_c (the ratio of volume when fuel injection ends to volume at TDC) that penalizes the constant-pressure heat addition. At the same compression ratio, the Diesel efficiency is always lower than the Otto efficiency — the constant-pressure heat addition is thermodynamically less favorable than constant-volume. But because diesels operate at much higher compression ratios than gasoline engines can achieve, real diesel engines attain higher actual efficiency. This reconciliation is critical: the formula is "worse" at equal r, but real engines access higher r.

Real engines deviate from ideal cycles through friction, heat transfer to cylinder walls, incomplete combustion, valve flow restrictions, and the finite duration of combustion. **Brake thermal efficiency** — useful crankshaft work divided by fuel energy input — captures all these losses and is the practically relevant metric. Modern turbocharged direct-injection diesels achieve 44–48% brake thermal efficiency in passenger vehicles and exceed 50% in large marine two-stroke diesels. Modern spark-ignition engines with turbocharging, direct injection, and variable valve timing now reach 40–42% peak efficiency under optimal operating conditions. The efficiency gap has narrowed considerably through engineering, but the fundamental thermodynamic advantage of high compression ratio for the Diesel cycle remains.
