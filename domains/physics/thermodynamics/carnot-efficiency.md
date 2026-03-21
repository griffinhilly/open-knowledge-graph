---
id: carnot-efficiency
title: Carnot Efficiency and Maximum Efficiency Theorem
domain: physics
course: thermodynamics
prerequisites:
- id: carnot-cycle
  type: hard
- id: thermal-efficiency
  type: hard
- id: entropy-in-thermodynamic-processes
  type: soft
- id: heat-transfer-radiation
  type: soft
tags:
- Carnot-efficiency
- maximum-efficiency
- temperature-ratio
- reversible-engine
stage: advanced
status: validated
---
# Carnot Efficiency and Maximum Efficiency Theorem

## Core Idea
The efficiency of a Carnot engine is e_Carnot = 1 − T_C/T_H, where temperatures are in Kelvin. This is the maximum possible efficiency for any engine operating between T_H and T_C — no real engine can exceed it. Carnot's theorem states that all reversible engines operating between the same two reservoirs have the same efficiency, and any irreversible engine has strictly lower efficiency. Improving efficiency requires raising T_H or lowering T_C, with diminishing returns as T_C approaches absolute zero.

## How It's Best Learned
Calculate Carnot efficiency for realistic temperature ranges: a steam turbine at 600°C rejecting to 30°C gives e_Carnot ≈ 66%. Compare to actual efficiencies of 35–45% — the gap is due to irreversibilities. Notice that efficiency is determined entirely by temperature ratio, independent of the working fluid.

## Common Misconceptions
- Carnot efficiency gives an upper bound, not a target — real engineers optimize for power output per unit cost, not maximum theoretical efficiency.
- Efficiency approaching 100% requires T_C → 0 K or T_H → ∞, both physically unattainable.
- The Carnot limit applies to heat engines; it does not directly apply to fuel cells or other non-thermal converters.

## Questions

```yaml
- question: "An engineer claims to have built an engine operating between a hot reservoir at 500K and a cold reservoir at 300K with an efficiency of 42%. The Carnot efficiency for these temperatures is 1 − 300/500 = 40%. How should this claim be evaluated?"
  type: multiple-choice
  options:
    - "The engine is impressively efficient and nearly at the theoretical maximum of 40%"
    - "The claimed 42% efficiency is physically impossible — it exceeds the Carnot limit and would violate the second law of thermodynamics"
    - "The claim is plausible if the engine uses an unusually effective working fluid or clever engineering design"
    - "The Carnot limit is a theoretical ideal that applies only to idealized gas cycles, so real engineered systems may exceed it"
  answer: 1
  explanation: "No engine operating between fixed reservoirs can exceed the Carnot efficiency — this is a theorem derived directly from the second law, not an engineering target. The proof is by contradiction: if such an engine existed, you could use it to drive a Carnot refrigerator between the same reservoirs, and the net effect would be a spontaneous heat flow from cold to hot — a second-law violation. The Carnot limit applies regardless of working fluid, design, or engineering ingenuity. A claimed efficiency above the Carnot bound is a claim to violate thermodynamics."

- question: "A power plant raises its steam temperature from 400K to 800K while keeping its cold reservoir (condenser) fixed at 300K. What happens to the Carnot efficiency?"
  type: multiple-choice
  options:
    - "It doubles from 25% to 50%, because doubling T_H doubles the efficiency"
    - "It increases from 25% to 62.5%, but not by a factor of two — the relationship between T_H and efficiency is nonlinear"
    - "It stays the same because efficiency depends only on the temperature difference, not the ratio"
    - "It doubles only if the cold reservoir temperature also changes proportionally"
  answer: 1
  explanation: "η_Carnot = 1 − T_C/T_H. At 400K: η = 1 − 300/400 = 25%. At 800K: η = 1 − 300/800 = 62.5%. Doubling T_H does not double efficiency because η depends on the ratio T_C/T_H, not on T_H alone. The gain diminishes as T_H grows large: at 400K vs 800K, the ratio T_C/T_H drops from 0.75 to 0.375. The relationship is intrinsically nonlinear in absolute temperature, which is why modest gains become harder to achieve at already-high temperatures."

- question: "Carnot's theorem states that all reversible engines operating between the same two temperature reservoirs must have the same efficiency, regardless of working fluid or cycle design."
  type: true-false
  answer: true
  explanation: "True. This follows from the same reductio argument used to prove the Carnot limit. If two reversible engines between the same reservoirs had different efficiencies, you could run the less efficient one in reverse (as a refrigerator) driven by the more efficient one, and extract net work while violating the second law. Since both are reversible, either can be run in either direction — so they must have exactly equal efficiency. The Carnot efficiency formula is therefore universal for reversible engines, independent of the specific design."

- question: "Because fuel cells convert chemical energy directly to electrical energy, they are not bound by the Carnot efficiency limit and can in principle achieve 100% conversion efficiency."
  type: true-false
  answer: true
  explanation: "True. The Carnot limit applies specifically to heat engines — devices that convert thermal energy to work by operating between two temperature reservoirs. Fuel cells are electrochemical devices that do not rely on heat as an intermediate step; they convert Gibbs free energy directly to electrical work. The theoretical maximum efficiency of a fuel cell is determined by the ratio of the Gibbs free energy change to the enthalpy change of the reaction (ΔG/ΔH), which can approach or exceed 100% for some reactions at certain temperatures. This is why fuel cells are not subject to the T_C/T_H thermodynamic bound."

- question: "Describe the logical structure of the proof of Carnot's theorem: what is assumed, how the machine arrangement exposes the contradiction, and which physical law is violated."
  type: short-answer
  answer: "Assume, for contradiction, that some engine E has efficiency greater than the Carnot efficiency η_C between reservoirs T_H and T_C. Now run a Carnot engine in reverse as a refrigerator R, driven by the output of E. Calibrate the sizes so that E does just enough work to drive R. Because E is assumed more efficient than the Carnot refrigerator, it extracts less heat from T_H per unit of work output than R pumps back. The net result: heat is transferred spontaneously from the cold reservoir to the hot reservoir with no other effect on the surroundings. This violates the Clausius statement of the second law, which prohibits spontaneous heat flow from cold to hot. The contradiction shows that no engine can exceed Carnot efficiency; an identical argument for two unequal reversible engines shows they must have equal efficiency."
  explanation: "The elegance of the proof is that it requires no detailed knowledge of the engine's internals — only that it converts heat to work between two fixed reservoirs. The second law alone, in its most general statement, determines the maximum efficiency."
```

## Explainer

From your study of the Carnot cycle and thermal efficiency, you know that a heat engine absorbs heat Q_H from a hot reservoir, does work W, and rejects heat Q_C to a cold reservoir. Thermal efficiency is defined as η = W/Q_H = 1 − Q_C/Q_H. The Carnot cycle is special: it consists entirely of reversible processes (two isothermal and two adiabatic legs), and it is this reversibility that determines its efficiency. The question that Carnot's theorem answers is: what is the maximum efficiency any engine can achieve between the same two temperature reservoirs?

The proof of Carnot's theorem uses a clever reductio ad absurdum. Suppose an engine exists with efficiency greater than the Carnot efficiency. Run the Carnot engine in reverse as a refrigerator, pumping heat from cold to hot. Drive this refrigerator using the output of the super-efficient engine. If the hypothetical engine could beat Carnot, the net effect would be a spontaneous flow of heat from the cold reservoir to the hot reservoir with no other effect — a violation of the second law of thermodynamics. Since that is impossible, no engine can exceed Carnot efficiency. The same argument shows that all reversible engines between the same reservoirs must have the same efficiency: if one reversible engine were more efficient than another, the less efficient one could run in reverse to create the same violation.

The formula **η_Carnot = 1 − T_C/T_H** (with temperatures in Kelvin) follows from computing the heat exchanged in each isothermal leg. During the isothermal expansion at T_H, the engine absorbs Q_H; during the isothermal compression at T_C, it rejects Q_C. For a reversible process, the entropy change of the reservoir equals −Q/T. Since the cycle returns the engine to its initial state (zero net entropy change for the engine), the entropy changes in the two reservoirs must cancel: Q_H/T_H = Q_C/T_C. Substituting this into the efficiency formula gives the Carnot result immediately.

The practical implications are stark. A coal power plant operating between a steam temperature of 600°C (873 K) and a condenser at 30°C (303 K) has a Carnot limit of 1 − 303/873 ≈ 65%. Real plants achieve 35–45% due to friction, heat losses, and irreversibilities. Raising T_H or lowering T_C both improve the limit, but with diminishing returns: halving T_C/T_H doesn't halve the gap to 100%. The formula also reveals a deep asymmetry — a small increase in T_H at already high temperatures buys less efficiency than the same increase near the bottom of the temperature scale. This is why cryogenic engineering can achieve striking efficiencies for refrigeration, but why no practical heat engine can approach 100% efficiency given any realistic temperature constraints.
