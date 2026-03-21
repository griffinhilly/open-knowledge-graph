---
id: otto-cycle-spark-ignition-engine
title: Otto Cycle and Spark-Ignition Reciprocating Engines
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-closed-systems
  type: hard
- id: isentropic-process-reversible
  type: hard
builds-toward:
- diesel-cycle-compression-ignition
tags:
- otto-cycle
- reciprocating-engine
- combustion
stage: advanced
status: draft
---

# Otto Cycle and Spark-Ignition Reciprocating Engines

## Core Idea
The Otto cycle (isochoric compression, constant-volume heat addition, isochoric expansion, constant-volume heat rejection) models spark-ignition reciprocating engines with fixed volume combustion. Compression ratio (initial to final volume) directly controls thermal efficiency and engine knock tendency; higher ratios increase efficiency but require higher-octane fuel. The cycle reveals why fast fuel burning (high flame speed) and optimal ignition timing are critical for efficiency.

## Questions

```yaml
- question: "An automotive engineer proposes increasing a gasoline engine's fuel injection by 30% at the same compression ratio, expecting to improve thermal efficiency. Based on the ideal Otto cycle, what is the effect on efficiency?"
  type: multiple-choice
  options:
    - "Efficiency increases because more heat input raises the peak cycle temperature"
    - "Efficiency decreases because the higher heat input creates proportionally more waste heat"
    - "Efficiency is unchanged because it depends only on compression ratio and γ, not on heat input"
    - "Efficiency increases up to a stoichiometric limit, then decreases"
  answer: 2
  explanation: "Otto cycle efficiency η = 1 − 1/r_c^(γ−1) contains no term for heat input Q_in. Increasing fuel injection changes the total work output and power, but not the fraction of heat converted to useful work. More fuel means more total work AND more waste heat in the same ratio — efficiency stays constant. This is the key insight: efficiency is a property of the cycle geometry (compression ratio) and working fluid (γ), not the fuel quantity. To improve efficiency you must change r_c or γ, not the amount of fuel."

- question: "Two ideal Otto cycles have compression ratios of r_c = 6 and r_c = 12 respectively, with the same working fluid (γ = 1.4). Compared to the r_c = 6 engine, the r_c = 12 engine:"
  type: multiple-choice
  options:
    - "Has exactly twice the thermal efficiency, because efficiency scales linearly with compression ratio"
    - "Has higher thermal efficiency, but less than twice as high, because efficiency scales as 1 − 1/r_c^(γ−1)"
    - "Has the same efficiency if both operate on the same fuel"
    - "Has lower efficiency because higher compression raises cylinder temperatures and heat losses"
  answer: 1
  explanation: "η = 1 − 1/r_c^(γ−1) is nonlinear in r_c. For γ = 1.4: η(r_c=6) = 1 − 1/6^0.4 ≈ 0.512; η(r_c=12) = 1 − 1/12^0.4 ≈ 0.630. Doubling the compression ratio improved efficiency from ~51% to ~63% — a meaningful gain, but not a doubling. Each increment in r_c yields diminishing returns, which is why the gain from r_c = 14 to r_c = 16 is smaller than the gain from r_c = 6 to r_c = 8. Option C is wrong because efficiency does not depend on fuel type under the air-standard assumption."

- question: "According to the ideal Otto cycle model, a spark-ignition engine running on hydrogen and an engine with identical compression ratio running on gasoline would have the same thermal efficiency (assuming the same γ)."
  type: true-false
  answer: true
  explanation: "Ideal Otto cycle efficiency η = 1 − 1/r_c^(γ−1) depends only on compression ratio and γ, not on the fuel's chemical identity or heating value. Under the air-standard assumption, the working fluid is treated as an ideal gas regardless of the actual fuel. Two engines with identical r_c and γ have identical ideal efficiency. In practice, hydrogen's higher flame speed and different combustion properties affect real engine performance — but these are deviations from the ideal cycle, not predictions of the Otto cycle formula."

- question: "The constant-volume heat addition process in the Otto cycle accurately describes real combustion in gasoline engines — the fuel burns so quickly that the piston barely moves during the process."
  type: true-false
  answer: false
  explanation: "Constant-volume heat addition is an idealization. In reality, combustion takes a finite time — typically 15–40 degrees of crank rotation — during which the piston is moving, so volume changes throughout combustion. The Otto cycle assumes instantaneous heat release at fixed volume to produce a tractable analytical model. Real engines also lose heat through cylinder walls, experience friction, and use fuel-air mixtures rather than pure air. The Otto cycle captures the correct qualitative trends (efficiency rises with r_c) but systematically overpredicts actual efficiencies."

- question: "Why does ideal Otto cycle thermal efficiency depend only on compression ratio and not on the amount of heat input (how much fuel is burned)? Explain using the cycle's structure."
  type: short-answer
  answer: "In the Otto cycle, both heat addition (2→3) and heat rejection (4→1) occur at constant volume. The isentropic compression and expansion processes connect the same two volumes (V_max and V_min), so the temperature ratios T₂/T₁ and T₄/T₃ both equal r_c^(γ−1) regardless of how much heat was added. When efficiency is computed as η = 1 − Q_out/Q_in = 1 − (T₄−T₁)/(T₃−T₂), both temperature differences scale proportionally with the heat added — Q_in cancels out, leaving only the compression ratio. Adding more heat raises all four temperatures proportionally; the fraction rejected stays the same."
  explanation: "This result is analogous to Carnot efficiency depending only on temperature limits. The Otto cycle's efficiency is set by how much the isentropic compression amplifies temperature (determined by r_c), not by absolute temperatures or fuel quantities. A practical implication: you cannot make a gasoline engine more efficient by using a richer mixture. The only paths to higher efficiency are increasing r_c (limited by knock), increasing γ (limited by mixture properties), or redesigning the cycle itself — for example, the Atkinson cycle uses a longer expansion stroke to extract more work from the same heat."
```

## Explainer

The Otto cycle is the idealized thermodynamic model for a gasoline engine piston. Think of the air-fuel mixture in a cylinder as a closed system going through four distinct processes. **Process 1→2** is isentropic compression: the piston moves upward, compressing the mixture with no heat transfer (fast enough to be approximately reversible adiabatic). **Process 2→3** is constant-volume heat addition: the spark fires, combustion releases heat Q_in at essentially fixed volume because the combustion occurs so rapidly that the piston barely moves. **Process 3→4** is isentropic expansion: the high-pressure, high-temperature combustion products push the piston down, doing work on the crankshaft. **Process 4→1** is constant-volume heat rejection: the exhaust valve opens and heat Q_out is released as exhaust gases escape at bottom dead center.

The thermal efficiency follows directly from your isentropic process relations. Because processes 1→2 and 3→4 are both isentropic and they connect the same two volumes (V_max and V_min), the temperature ratios are T₂/T₁ = (V₁/V₂)^(γ−1) = r_c^(γ−1) and T₃/T₄ = r_c^(γ−1), where **r_c** = V_max/V_min is the **compression ratio** and γ = c_p/c_v. The heat added is Q_in = c_v(T₃ − T₂) and rejected is Q_out = c_v(T₄ − T₁). The efficiency η = 1 − Q_out/Q_in = 1 − (T₄ − T₁)/(T₃ − T₂) = 1 − 1/r_c^(γ−1). This clean formula shows that efficiency depends only on the compression ratio and γ — not on the heat input or the fuel properties.

Higher compression ratios always give higher efficiency, which is why engine designers want them as large as possible. The practical limit is **engine knock** (detonation): if the mixture is compressed too much, its temperature rises enough to trigger auto-ignition before the spark fires, creating uncontrolled pressure spikes that can destroy the engine. **Octane rating** measures a fuel's resistance to auto-ignition — higher-octane fuel tolerates higher compression ratios, which is why premium fuel is used in high-performance engines. The Otto cycle also explains ignition timing: the spark must fire slightly before top dead center so that peak pressure occurs just after the piston reaches its highest point, maximizing work output during the expansion stroke. Firing too early wastes energy fighting compression; firing too late loses expansion work.

The Otto cycle is an idealization that assumes air as an ideal gas (the **air-standard assumption**), perfect isentropic processes, and instantaneous heat addition. Real engines suffer from irreversibilities (friction, heat loss through cylinder walls, incomplete combustion) and incomplete isentropic behavior, so actual efficiencies are substantially lower than the ideal cycle predicts. Nevertheless, the cycle provides the correct qualitative trends — efficiency rises with r_c, higher γ (less complex fuel molecules in the working fluid) helps — and gives a useful upper bound for evaluating real engine performance.
