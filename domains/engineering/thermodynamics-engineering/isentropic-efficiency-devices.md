---
id: isentropic-efficiency-devices
title: Isentropic Efficiency of Turbines, Compressors, and Pumps
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: isentropic-process-reversible
  type: hard
tags:
- efficiency
- isentropic
- devices
stage: advanced
status: draft
---

# Isentropic Efficiency of Turbines, Compressors, and Pumps

## Core Idea
Isentropic efficiency compares actual device performance to an ideal isentropic process, quantifying the fraction of available energy extracted (turbines) or the additional work required (compressors). For a turbine, η_s = (actual work)/(isentropic work); for a pump or compressor, η_s = (isentropic work)/(actual work). Typical values range 0.75–0.95 depending on machine design and operating conditions.

## How It's Best Learned
Calculate isentropic work (assuming S = const) using property tables, then use actual outlet conditions to find actual work and efficiency. Recognize that turbine efficiency is always less than 100% (actual work less than isentropic), while compressor efficiency is also less than 100% (actual work greater than isentropic). Use typical efficiency values (0.85 for turbines, 0.80 for compressors) to estimate real performance when exact data is unavailable.

## Common Misconceptions
- Isentropic efficiency is the same for turbines and compressors; the definitions have numerator and denominator reversed.
- Improving isentropic efficiency requires only smoother passages; it also depends on Reynolds number, stage design, and multi-stage effects.
- An isentropic efficiency of 0.90 means 90% of energy is converted to useful work; it means the device extracts 90% of the maximum possible work in an ideal process.

## Questions

```yaml
- question: "A compressor has an isentropic efficiency of 0.80. Compared to an ideal isentropic compressor performing the same pressure rise, the actual compressor requires..."
  type: multiple-choice
  options:
    - "80% of the work an ideal compressor would require — it is more efficient than the ideal"
    - "The same work as the ideal compressor — isentropic efficiency only affects heat transfer"
    - "More work than the ideal compressor — specifically, actual work = isentropic work / 0.80"
    - "20% less work than the ideal compressor, since 80% efficiency means 20% is saved"
  answer: 2
  explanation: "Compressor isentropic efficiency is defined as η_c = w_isentropic / w_actual. Rearranging: w_actual = w_isentropic / η_c = w_isentropic / 0.80. Since 0.80 < 1, w_actual > w_isentropic — the real compressor requires MORE work than the ideal. Irreversibilities (friction, flow separation) convert some of the input work to heat within the fluid rather than raising pressure, so you must supply extra work to achieve the same pressure rise. Options A and D reverse this logic — they reflect the mistaken intuition that higher efficiency always means using less of something, forgetting that for a compressor, the 'something' being minimized is work input."

- question: "Why is the isentropic efficiency formula for a compressor the inverse of the formula for a turbine (η_c = w_s/w_actual vs. η_t = w_actual/w_s)?"
  type: multiple-choice
  options:
    - "Because compressors use a different thermodynamic cycle than turbines"
    - "In both formulas, the smaller quantity is in the numerator and the larger is in the denominator, so that efficiency is always less than 1"
    - "Because turbine efficiency accounts for heat transfer while compressor efficiency does not"
    - "Because the isentropic process produces more work in a compressor than in a turbine"
  answer: 1
  explanation: "The formulas are constructed to keep efficiency below 1 for both devices. For a turbine: actual work output < isentropic (ideal) work output, so putting actual in the numerator gives a ratio < 1. For a compressor: actual work input > isentropic (ideal) work input, so putting isentropic in the numerator gives a ratio < 1. In both cases, efficiency = (what you actually get or ideally need) / (the larger quantity). The inversion is not arbitrary — it reflects the different direction of energy flow (out vs. in) while maintaining the logical meaning that η = 1 is the unattainable ideal."

- question: "For a real turbine operating between fixed inlet and exit pressures, the actual exit enthalpy is higher than the isentropic exit enthalpy."
  type: true-false
  answer: true
  explanation: "In a turbine, the isentropic exit state (2s) represents maximum work extraction — the fluid loses as much enthalpy as thermodynamically possible while entropy stays constant. Real irreversibilities (friction, turbulence) convert some of that potential work to internal heat within the fluid, leaving the fluid with more enthalpy at the exit than it would have after a perfect isentropic expansion. On an h-s diagram, the actual exit state (2a) lies to the right and above the isentropic exit state (2s). Since actual work = h1 − h2a and h2a > h2s, actual work < isentropic work — confirming η_t < 1."

- question: "An isentropic efficiency of 0.90 for a turbine means that 90% of the kinetic energy entering the turbine is converted to shaft work."
  type: true-false
  answer: false
  explanation: "Isentropic efficiency compares actual work output to the maximum work that could be extracted in a hypothetical isentropic process between the same inlet state and exit pressure — not to the total energy content of the incoming fluid. The fluid still retains significant enthalpy at the exit even in the ideal case (it doesn't become zero-energy). Isentropic efficiency = (actual work) / (maximum possible work from an isentropic expansion). This is a relative, not absolute, efficiency measure. Stating it as '90% of total energy converted' would require knowing absolute inlet enthalpy relative to a reference state, which is not how the definition works."

- question: "A steam turbine inlet is at state 1 with enthalpy h1 and entropy s1. The isentropic exit state (2s) and actual exit state (2a) are both at the same exit pressure. On an h-s diagram, which state has higher enthalpy — 2s or 2a — and what does this tell you about actual versus ideal turbine work output?"
  type: short-answer
  answer: "State 2a (actual) has higher enthalpy than state 2s (isentropic). Actual turbine work = h1 − h2a; isentropic work = h1 − h2s. Because h2a > h2s, the actual work output is smaller than the isentropic work — the turbine delivers less shaft work than the ideal. The 'missing' work went into increasing the fluid's entropy through irreversibilities (friction, heat transfer, turbulence), which appears as extra enthalpy in the exit steam."
  explanation: "On the h-s (Mollier) diagram, both exit states sit on the same isobar (same exit pressure). The isentropic path is a vertical line (constant s), while the actual path curves to the right as entropy increases. Since enthalpy generally increases with entropy at constant pressure in the two-phase and superheated regions, the actual exit state 2a is above and to the right of 2s. This diagram-reading skill is essential for turbine and compressor problem-solving."
```

## Explainer

You already know that an isentropic process is reversible and adiabatic — entropy stays constant. In that ideal world, a turbine would extract the maximum possible work from a steam or gas stream, and a compressor would require the minimum possible work to raise pressure. Real devices cannot achieve this because of friction, flow separation, heat transfer, and turbulence. **Isentropic efficiency** is the single number that quantifies how far a real device falls short of the isentropic ideal.

For a **turbine**, the isentropic process represents the most work you could possibly extract from a fluid entering at state 1 and leaving at the exit pressure. The ideal exit state (state 2s, with "s" for isentropic) is found by drawing a vertical line on an h-s diagram down to the exit pressure — entropy constant, pressure drops. The actual exit state (state 2a) lies to the right of this ideal point on the h-s diagram, at higher entropy and higher enthalpy, because irreversibilities dissipate energy as heat within the fluid rather than converting it to shaft work. The turbine isentropic efficiency is η_t = w_actual / w_isentropic = (h1 - h2a) / (h1 - h2s). Since h2a > h2s, the numerator is smaller than the denominator, giving η_t < 1.

For a **compressor or pump**, the situation is exactly reversed. The isentropic ideal minimizes the work you must input to raise the fluid's pressure. Real irreversibilities make you do more work than this minimum. The actual exit enthalpy h2a is higher than the isentropic ideal h2s (more energy stored in the fluid, mostly as heat from friction). The compressor isentropic efficiency is η_c = w_isentropic / w_actual = (h2s - h1) / (h2a - h1). Both numerator and denominator represent work inputs, but isentropic work is always less than actual, so again η_c < 1. The important asymmetry: the definition is inverted relative to turbines — you divide by the larger quantity in both cases to keep efficiency below 1.

To solve a practical problem, you work in three steps. First, locate the inlet state on steam tables or using the ideal gas relations and read off h1 and s1. Second, set s2s = s1 and find h2s at the exit pressure — this gives the isentropic work. Third, apply the efficiency definition to find h2a, then use h2a to find the actual exit state and any other desired properties (temperature, quality, entropy). The h-s (Mollier) diagram is your visualization tool: turbines move down-right (expanding, entropy increasing), compressors move up-right (compressing, entropy increasing).

The efficiency value matters enormously in cycle analysis. In a Rankine cycle, reducing turbine efficiency from 0.90 to 0.80 might drop overall cycle efficiency by 3-5 percentage points — a significant penalty. In a Brayton cycle, both turbine and compressor efficiency appear, and their effects compound: a slightly less efficient compressor forces the turbine to work harder just to recover the compressor penalty, before producing any net work. This sensitivity is why turbomachinery design invests heavily in blade geometry, tip clearance, and stage matching to push isentropic efficiencies toward 0.90 and above.
