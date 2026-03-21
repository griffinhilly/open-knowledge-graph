---
id: turbine-compressor-efficiency-definitions
title: Isentropic Efficiency of Turbines and Compressors
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: isentropic-efficiency-devices
  type: hard
- id: steady-flow-energy-equation-engineering
  type: soft
builds-toward:
- power-cycle-thermal-efficiency
- rankine-power-generation-cycles
- brayton-gas-turbine-cycles
tags:
- isentropic-efficiency
- turbines
- compressors
- performance
stage: advanced
status: draft
---

# Isentropic Efficiency of Turbines and Compressors

## Core Idea
Isentropic efficiency compares actual to reversible work: η_T = W_actual/W_isentropic for turbines, η_C = W_isentropic/W_actual for compressors. Both are <100% due to friction, turbulence, and non-ideal flows. Typical values: turbines 85-90%, compressors 80-88%. Even 1% efficiency improvement in a large power plant saves significant fuel and operating costs annually.

## Questions

```yaml
- question: "A steam turbine expands steam from inlet to outlet pressure. The isentropic enthalpy drop is 400 kJ/kg, but friction and turbulence cause the actual enthalpy drop to be only 340 kJ/kg. What is the isentropic efficiency of this turbine?"
  type: multiple-choice
  options:
    - "85%, computed as 340/400 — actual work divided by isentropic work"
    - "118%, computed as 400/340 — isentropic work divided by actual work"
    - "60 kJ/kg — the lost work due to irreversibilities"
    - "85%, but this means the turbine is operating poorly since ideal efficiency is 100%"
  answer: 0
  explanation: "Turbine isentropic efficiency η_T = W_actual / W_isentropic = (h_in − h_out,actual) / (h_in − h_out,s) = 340/400 = 0.85 = 85%. For a turbine, actual work is always less than isentropic because irreversibilities (friction, turbulence, leakage) convert some shaft work into heating the fluid. Dividing actual by isentropic gives a number ≤ 1. Option B flips the ratio — that structure applies to compressors, not turbines. 85% is considered a good turbine efficiency; real industrial turbines operate in the 85–90% range."

- question: "A compressor's isentropic efficiency formula uses η_C = W_isentropic / W_actual (ideal in numerator, actual in denominator). Why is it structured this way, opposite to a turbine?"
  type: multiple-choice
  options:
    - "Compressors are work-consuming devices, so actual work is always greater than isentropic — putting ideal in the numerator keeps η_C ≤ 1"
    - "Compressors operate at higher pressures, so the energy scale is reversed"
    - "The formula is the same as the turbine; the textbook notation just differs"
    - "Compressors are more efficient than turbines, so their efficiency formula naturally exceeds 1 if structured like a turbine"
  answer: 0
  explanation: "Efficiency must always be ≤ 1. For a compressor, the isentropic (ideal) process requires the *minimum* possible work; the real compressor always requires more due to friction and irreversibilities. W_actual > W_isentropic. If you wrote η_C = W_actual / W_isentropic, you'd get a number > 1, which is meaningless as an efficiency. Inverting the ratio — ideal/actual — gives a number between 0 and 1. The mnemonic: efficiency = (what you want) / (what you pay). For a compressor you want pressure rise and 'pay' in work input."

- question: "A real compressor's exit state is at a higher temperature and enthalpy than the isentropic exit state at the same outlet pressure."
  type: true-false
  answer: true
  explanation: "In an isentropic (ideal) compressor, all the work input goes into raising the fluid's pressure and enthalpy along the isentrope. In a real compressor, the extra work required beyond the isentropic minimum goes into entropy generation — which manifests as additional heating of the working fluid. The real outlet enthalpy h_out,actual = h_in + W_actual/ṁ is higher than the isentropic outlet enthalpy h_out,s = h_in + W_isentropic/ṁ, meaning the fluid exits hotter. This is why compressor efficiency matters in power cycle analysis: a less efficient compressor delivers hotter air to the combustor, wasting fuel."

- question: "A turbine with η_T = 0.90 delivers more work per unit of fluid than the ideal isentropic turbine operating between the same inlet and outlet pressures."
  type: true-false
  answer: false
  explanation: "The isentropic turbine represents the maximum possible work extraction for given inlet and outlet pressures. A real turbine with η_T = 0.90 delivers only 90% of that maximum — the other 10% is lost to internal irreversibilities (friction, turbulence, heat leakage) that heat the fluid rather than turning the shaft. The actual outlet enthalpy is higher than the isentropic outlet enthalpy, meaning less enthalpy was converted to work. No real device can exceed the isentropic limit; efficiency is always < 1."

- question: "Why are the isentropic efficiency formulas for turbines and compressors structured differently (actual/ideal vs. ideal/actual), and how can you remember which applies to which device?"
  type: short-answer
  answer: "Both formulas are structured so that efficiency = (what you want) / (what you pay). For a turbine, you want work output and the isentropic process provides the theoretical maximum; real devices fall short. So η_T = W_actual / W_isentropic < 1. For a compressor, you want pressure rise (achieved at minimum isentropic work cost) but real devices require more work. So η_C = W_isentropic / W_actual < 1. The key question is: which quantity is larger in the real device? For turbines, actual < isentropic (bad = less output), so actual goes in numerator to get < 1. For compressors, actual > isentropic (bad = more input), so actual goes in denominator to get < 1."
  explanation: "A quick check: if you mix up the formulas, you'll get a number > 1, which immediately flags an error. The asymmetry also has a physical interpretation: turbine irreversibilities reduce the enthalpy drop (shaft work), keeping the exit enthalpy above the isentropic exit. Compressor irreversibilities increase the enthalpy rise (shaft work required), pushing the exit enthalpy above the isentropic exit. In both cases, the real exit enthalpy is higher than the isentropic exit enthalpy — but for opposite reasons."
```

## Explainer

You already know that isentropic processes are reversible and adiabatic — they represent the best-case scenario for work-producing or work-consuming devices. **Isentropic efficiency** uses this ideal as a yardstick: it compares what a real device achieves to what a perfect isentropic device would achieve between the same inlet and outlet pressures.

For a **turbine**, the ideal is to extract as much work as possible. The isentropic turbine produces work W_s by expanding from inlet to outlet pressure with no entropy generation. The real turbine, plagued by fluid friction, turbulence, tip leakage, and heat loss, produces less: W_actual < W_s. So turbine isentropic efficiency is η_T = W_actual / W_isentropic = (h_in − h_out,actual) / (h_in − h_out,s), where the denominator is the maximum possible enthalpy drop. If η_T = 0.87, the turbine delivers 87% of the work that a perfect expansion would yield; the other 13% is lost to internal irreversibilities that heat the fluid (raising its entropy and exit enthalpy above the isentropic exit state).

For a **compressor**, the logic flips because work is being consumed, not produced. The ideal isentropic compressor requires the minimum work W_s to achieve a given pressure rise. The real compressor requires more: W_actual > W_s. So compressor isentropic efficiency is η_C = W_isentropic / W_actual = (h_out,s − h_in) / (h_out,actual − h_in). If η_C = 0.83, the compressor consumes 1/0.83 ≈ 1.20 times the minimum necessary work — 20% extra energy wasted to friction and flow irreversibilities. The real compressor exit state is at higher temperature and enthalpy than the isentropic exit state, because the wasted work goes into heating the working fluid.

The asymmetry between the two definitions — numerator for turbines, denominator for compressors — ensures that both efficiencies are numbers between 0 and 1. It is easy to mix them up: always ask "which is larger, actual or ideal?" For turbines, actual work is smaller (bad), so divide actual by ideal. For compressors, actual work is larger (bad), so divide ideal by actual. A good mnemonic: efficiency is always (what you want) / (what you pay). For the turbine, you want work and pay nothing extra; for the compressor, you want pressure rise and pay in work.

These efficiencies are not just academic — they cascade through cycle analysis. In a Brayton gas turbine cycle, combining a turbine at η_T = 0.87 and a compressor at η_C = 0.83 can reduce the overall cycle efficiency from a Carnot-ideal 48% down to a real 30-35%. Improving each device by a few percentage points meaningfully shifts the system thermal efficiency. This is why turbomachinery aerodynamics — blade profiles, tip clearances, inlet conditions — is a major engineering discipline. Every percentage point of isentropic efficiency translates directly into fuel saved and emissions reduced.
